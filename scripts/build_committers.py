"""Build `page_committers.json` — per-page contributors, incrementally.

WHAT THIS IS FOR
----------------
This replaces `mkdocs-git-committers-plugin-2`: the avatars that used to appear
in the footer of each dataset page showing who edited *that page*.

It is NOT the same thing as `issues-summary.json`, which the existing
`scripts/issues_summary.py` builds. That one is site-wide issue/PR contributors
for `contributors.html`. This one is per-markdown-file commit authorship, which
nothing in the repo currently produces.

WHY IT IS FAST
--------------
`git-committers` issues one GitHub API request PER PAGE — ~390 requests, ~131s,
and a 403 rate limit part-way through. But this repo has only **18 distinct
author emails** across 1,906 commits touching `docs/`. Resolving an email to a
GitHub identity is therefore an 18-entry lookup, not a 390-entry one.

So:
  * identity resolution  -> at most one API call per UNSEEN email, then cached
  * per-page authorship  -> computed entirely locally from a single `git log`
  * steady state         -> ZERO API calls when no new authors appear

INCREMENTAL BEHAVIOUR
---------------------
The cache records the commit it was last built from. On each run only commits
since then are examined, so only pages actually touched are recomputed, and only
genuinely new emails cost an API call.

USAGE
-----
    python build_committers.py                     # incremental
    python build_committers.py --rebuild           # ignore cache, full rebuild
    python build_committers.py --token-file gh_token.json

Token resolution order: --token-file, then $GH_TOKEN / $GITHUB_TOKEN.
In CI, prefer the environment variable and never commit a token file.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

CACHE = "page_committers.json"
API = "https://api.github.com"


# Pages renamed as part of the migration. A single `git log --name-only` pass
# does not follow renames, so without this map the renamed file looks brand new
# and loses its dates and contributors. Keyed new-path -> historical path.
#
# docs/index.md became docs/about.md when the splash page took over `/`.
RENAMES = {
    "docs/about.md": "docs/index.md",
}

def git(*args: str, cwd: Path) -> str:
    r = subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8"
    )
    if r.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed:\n{r.stderr}")
    return r.stdout


NO_HISTORY = """
No commit history found in {root}

Dates and per-page contributors are BOTH derived from `git log`. A repository
created with `git init` has nothing to read, so every page would lose its
"Last update" stamp and its contributor avatars.

Create the repo by CLONING the original instead, so history is preserved:

    git clone <original-repo-url> gee-community-catalog

In CI, also set `fetch-depth: 0` on actions/checkout — a shallow clone makes
every page look as though it were created at the shallow boundary.

See README.md -> "Repository history is required".
"""


def require_history(repo_root: Path) -> None:
    """Fail early and legibly rather than emitting a cryptic git error."""
    r = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=repo_root, capture_output=True, text=True
    )
    if r.returncode != 0:
        sys.exit(NO_HISTORY.format(root=repo_root.resolve()))


def load_token(token_file: str | None) -> str | None:
    if token_file:
        p = Path(token_file)
        if p.exists():
            data = json.loads(p.read_text(encoding="utf-8"))
            for key in ("GH_TOKEN", "GITHUB_TOKEN", "token"):
                if data.get(key):
                    return data[key]
    return os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")


def api_get(url: str, token: str | None) -> object | None:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "build-committers",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    try:
        with urllib.request.urlopen(
            urllib.request.Request(url, headers=headers), timeout=30
        ) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        print(f"    ! HTTP {e.code} for {url.split('?')[0]}", file=sys.stderr)
        return None
    except Exception as e:  # noqa: BLE001 - network flakiness shouldn't abort the build
        print(f"    ! {type(e).__name__}: {e}", file=sys.stderr)
        return None


def resolve_email(repo: str, email: str, token: str | None) -> dict | None:
    """One API call: ask for a single commit by this author, read the identity.

    This is the whole trick. `git-committers` asks "who touched this page?" for
    every page; we ask "who is this email?" once per distinct email.
    """
    url = f"{API}/repos/{repo}/commits?per_page=1&author={urllib.parse.quote(email)}"
    data = api_get(url, token)
    if not data or not isinstance(data, list):
        return None
    author = data[0].get("author")
    commit_author = data[0].get("commit", {}).get("author", {})
    if not author:  # commit email not linked to any GitHub account
        return None
    return {
        "login": author["login"],
        "name": commit_author.get("name") or author["login"],
        "url": author["html_url"],
        "avatar": author["avatar_url"],
    }


def page_authorship(repo_root: Path, git_path: str, since: str | None) -> dict:
    """path -> {email: commit_count}, from one git log pass."""
    rng = [f"{since}..HEAD"] if since else []
    raw = git(
        "log", *rng, "--format=%x00%ae", "--name-only", "--", git_path, cwd=repo_root
    )
    pages: dict[str, Counter] = {}
    for commit in raw.split("\x00")[1:]:
        email, _, files = commit.partition("\n")
        email = email.strip().lower()
        for f in filter(None, (ln.strip() for ln in files.splitlines())):
            if f.endswith(".md"):
                pages.setdefault(f, Counter())[email] += 1
    return pages


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root", default="../..")
    ap.add_argument("--git-path", default="docs")
    ap.add_argument("--repo", default="samapriya/awesome-gee-community-datasets")
    ap.add_argument("--token-file", default="gh_token.json")
    ap.add_argument("--rebuild", action="store_true", help="ignore the cache")
    ap.add_argument("--out", default=CACHE)
    args = ap.parse_args()

    t0 = time.perf_counter()
    repo_root = Path(args.repo_root).resolve()
    require_history(repo_root)
    out = Path(args.out)

    cache = {"_meta": {}, "authors": {}, "pages": {}}
    if out.exists() and not args.rebuild:
        cache = json.loads(out.read_text(encoding="utf-8"))
        cache.setdefault("_meta", {})
        cache.setdefault("authors", {})
        cache.setdefault("pages", {})

    since = cache["_meta"].get("last_commit") if not args.rebuild else None
    if since:
        # A rewritten/force-pushed history would make the stored SHA unreachable.
        check = subprocess.run(
            ["git", "cat-file", "-e", f"{since}^{{commit}}"],
            cwd=repo_root, capture_output=True,
        )
        if check.returncode != 0:
            print(f"cached commit {since[:9]} not found — full rebuild")
            since = None

    head = git("rev-parse", "HEAD", cwd=repo_root).strip()
    if since == head:
        print(f"up to date at {head[:9]} — nothing to do (0 API calls)")
        print(f"\npages: {len(cache['pages'])}, authors: {len(cache['authors'])}")
        print(f"elapsed: {time.perf_counter() - t0:.2f}s")
        return 0

    mode = "full rebuild" if not since else f"incremental since {since[:9]}"
    print(f"{mode} -> HEAD {head[:9]}")

    delta = page_authorship(repo_root, args.git_path, since)
    print(f"  pages touched: {len(delta)}")

    # Merge commit counts into the cache.
    for path, counts in delta.items():
        merged = Counter(cache["pages"].get(path, {}).get("counts", {}))
        merged.update(counts)
        cache["pages"].setdefault(path, {})["counts"] = dict(merged)

    # Resolve only emails we have never seen. This is the only API cost.
    known = cache["authors"]
    unseen = {e for c in delta.values() for e in c} - set(known) - set(
        cache["_meta"].get("unresolved", [])
    )
    print(f"  distinct new emails needing resolution: {len(unseen)}")

    token = load_token(args.token_file)
    if unseen and not token:
        print("  ! no token — skipping resolution (set GH_TOKEN or --token-file)")
    unresolved = set(cache["_meta"].get("unresolved", []))
    calls = 0
    for email in sorted(unseen):
        if not token:
            break
        who = resolve_email(args.repo, email, token)
        calls += 1
        if who:
            known[email] = who
            print(f"    {email[:38]:<38} -> @{who['login']}")
        else:
            unresolved.add(email)  # never retry a permanently unlinkable email
            print(f"    {email[:38]:<38} -> (no GitHub account)")

    # Materialise per-page committer lists, most commits first.
    pages_out = {}
    for path, info in cache["pages"].items():
        ranked = sorted(info.get("counts", {}).items(), key=lambda kv: -kv[1])
        people = [known[e] for e, _ in ranked if e in known]
        if people:
            pages_out[path] = people
        info["committers"] = [p["login"] for p in people]

    cache["_meta"] = {
        "last_commit": head,
        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "unresolved": sorted(unresolved),
        "api_calls_this_run": calls,
    }
    cache["committers_by_page"] = pages_out

    out.write_text(json.dumps(cache, indent=1), encoding="utf-8")
    dt = time.perf_counter() - t0
    print(
        f"\nwrote {out}  |  {len(pages_out)} pages, {len(known)} authors, "
        f"{calls} API calls, {dt:.2f}s"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

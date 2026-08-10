"""Restore "Last update" dates and contributor avatars under Zensical.

Zensical has no equivalent to `mkdocs-git-revision-date-localized-plugin` or
`mkdocs-git-committers-plugin-2` (backlog #17/#18, both open and unlabelled
since Nov 2025). But it *ships the entire footer renderer* —
`zensical/templates/partials/source-file.html` is included on every page by
`partials/content.html`. It is simply never fed.

Two of its inputs come from page front matter and work with no override at all:

    page.meta.git_revision_date_localized  -> "Last update"
    page.meta.git_creation_date_localized  -> "Created"

The third (`committers`) is a context variable that nothing in Zensical
populates. `overrides/partials/source-file.html` adds two lines so it falls back
to `page.meta.committers`, then reuses Zensical's own macro unchanged.

This script stamps all three into front matter from git history.

Run it as a PRE-BUILD CI STEP against the working copy. Do not commit the
result: the stamps are derived data, and committing them would change the very
mtimes they describe.

    python stamp_git_metadata.py --docs docs --repo-root .
    zensical build

Dates need nothing but git. Avatars need a GitHub token:

    GH_TOKEN=... python stamp_git_metadata.py --committers

Performance note: this walks git history ONCE (not once per file, which is what
makes `git-committers` take ~160s and hit 403s on this repo) and resolves
authors with one paginated commit crawl instead of one request per page.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_committers import require_history  # noqa: E402

FRONT_MATTER_KEYS = (
    "git_revision_date_localized",
    "git_creation_date_localized",
    "committers",
)
MAX_AVATARS_SHOWN = 4  # Zensical's macro slices [:4] and renders "+N" past that


# Pages renamed as part of the migration. A single `git log --name-only` pass
# does not follow renames, so without this map the renamed file looks brand new
# and loses its dates and contributors. Keyed new-path -> historical path.
#
# docs/index.md became docs/about.md when the splash page took over `/`.
RENAMES = {
    "docs/about.md": "docs/index.md",
}

def git(*args: str, cwd: Path) -> str:
    out = subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8"
    )
    if out.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed:\n{out.stderr}")
    return out.stdout


def history(repo_root: Path, docs_rel: str) -> tuple[dict, dict, dict]:
    """One pass over git log -> (last_date, first_date, emails per file).

    Requires full history: set `fetch-depth: 0` on actions/checkout, otherwise
    every file looks like it was created at the shallow boundary.
    """
    raw = git(
        "log", "--format=%x00%aI%x1f%ae%x1f%an", "--name-only", "--", docs_rel,
        cwd=repo_root,
    )
    last: dict[str, str] = {}
    first: dict[str, str] = {}
    authors: dict[str, dict[str, str]] = defaultdict(dict)

    # git log is newest-first, so the first date seen for a path is its last
    # modification and the last one seen is its creation.
    for commit in raw.split("\x00")[1:]:
        head, _, files = commit.partition("\n")
        date, email, name = head.split("\x1f")
        for f in filter(None, (ln.strip() for ln in files.splitlines())):
            last.setdefault(f, date[:10])
            first[f] = date[:10]
            authors[f].setdefault(email.lower(), name)
    return last, first, authors


def github_author_map(repo: str, token: str) -> dict[str, dict]:
    """email -> {login, name, url, avatar}, from one paginated commit crawl.

    `git-committers` issues a request per page and exhausts the rate limit on a
    390-file repo. Crawling the commit list instead costs ~1 request per 100
    commits and yields the same email->profile mapping.
    """
    mapping: dict[str, dict] = {}
    for page in range(1, 40):  # 40 * 100 commits is ample for this repo
        url = f"https://api.github.com/repos/{repo}/commits?per_page=100&page={page}"
        req = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "User-Agent": "stamp-git-metadata",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                batch = json.load(r)
        except urllib.error.HTTPError as e:
            print(f"  github: HTTP {e.code} on page {page}; stopping crawl", file=sys.stderr)
            break
        if not batch:
            break
        for c in batch:
            author, commit = c.get("author"), c.get("commit", {}).get("author", {})
            email = (commit.get("email") or "").lower()
            if not email or not author:
                continue  # unmatched email, e.g. a local-only git identity
            mapping.setdefault(
                email,
                {
                    "login": author["login"],
                    "name": commit.get("name") or author["login"],
                    "url": author["html_url"],
                    "avatar": author["avatar_url"],
                },
            )
        print(f"  github: page {page}, {len(mapping)} authors resolved", file=sys.stderr)
    return mapping


def yaml_block(fields: dict) -> str:
    lines = ["---"]
    for k, v in fields.items():
        if k == "committers":
            lines.append("committers:")
            for c in v:
                lines.append(f"  - login: {c['login']}")
                lines.append(f"    name: {json.dumps(c['name'])}")
                lines.append(f"    url: {c['url']}")
                lines.append(f"    avatar: {c['avatar']}")
        else:
            lines.append(f"{k}: {v}")
    return "\n".join(lines) + "\n---\n\n"


def split_front_matter(text: str) -> tuple[list[str], str]:
    """Return (preserved front-matter lines, body).

    Existing front matter is kept — only our own keys are replaced — so pages
    like `docs/publications/index_showcase.md` do not lose `template:`.
    """
    if not text.startswith("---\n"):
        return [], text
    end = text.find("\n---", 4)
    if end == -1:
        return [], text
    existing, body = text[4:end], text[end + 4 :].lstrip("\n")
    kept, skipping = [], False
    for line in existing.splitlines():
        if line and not line[0].isspace():
            skipping = line.split(":", 1)[0].strip() in FRONT_MATTER_KEYS
        if not skipping:
            kept.append(line)
    return kept, body


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--docs", default="docs", help="directory to stamp")
    ap.add_argument("--repo-root", default=".")
    ap.add_argument(
        "--git-path",
        default="docs",
        help="path of the docs tree INSIDE the git repo. Differs from --docs "
        "only when stamping a copy (as the trial does); in CI they are the same.",
    )
    ap.add_argument("--repo", default="samapriya/awesome-gee-community-datasets")
    ap.add_argument("--committers", action="store_true", help="also stamp per-page avatars")
    ap.add_argument("--committers-cache", default="page_committers.json")
    args = ap.parse_args()

    repo_root = Path(args.repo_root).resolve()
    require_history(repo_root)
    docs = Path(args.docs).resolve()

    print(f"reading git history for {args.git_path}/ ...")
    last, first, authors = history(repo_root, args.git_path)
    print(f"  {len(last)} files with history")

    # Per-page committers come from the cache built by build_committers.py,
    # which resolves identities incrementally and costs 0 API calls in steady
    # state. Nothing here touches the network.
    by_page: dict[str, list] = {}
    if args.committers:
        cache = Path(args.committers_cache)
        if not cache.exists():
            sys.exit(
                f"{cache} not found — run:\n"
                f"  python build_committers.py --token-file gh_token.json"
            )
        data = json.loads(cache.read_text(encoding="utf-8"))
        by_page = data.get("committers_by_page", {})
        meta = data.get("_meta", {})
        print(
            f"committers cache: {len(by_page)} pages, "
            f"{len(data.get('authors', {}))} authors, built at {meta.get('last_commit', '?')[:9]}"
        )

    stamped = missing = 0
    for md in sorted(docs.rglob("*.md")):
        rel = f"{args.git_path}/{md.relative_to(docs).as_posix()}"
        rel = RENAMES.get(rel, rel)  # inherit history across the migration rename
        if rel not in last:
            missing += 1  # never committed, e.g. generated or brand new
            continue

        fields = {"git_revision_date_localized": last[rel]}
        if first.get(rel):
            fields["git_creation_date_localized"] = first[rel]

        if args.committers and by_page.get(rel):
            fields["committers"] = by_page[rel]

        kept, body = split_front_matter(md.read_text(encoding="utf-8"))
        block = yaml_block(fields)
        if kept:
            block = block[:-5] + "\n".join(kept) + "\n---\n\n"
        md.write_text(block + body, encoding="utf-8")
        stamped += 1

    print(f"\nstamped {stamped} pages; {missing} skipped (no git history)")
    if args.committers:
        print(f"max {MAX_AVATARS_SHOWN} avatars shown per page, rest collapse to +N")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

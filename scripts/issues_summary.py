"""Build issues-summary.json (site-wide issue/PR contributors) and cache avatars.

Output format is unchanged. All network access goes through gh_api, which adds
timeouts and retries.
"""
import hashlib
import json
import os
import time

import requests

from gh_api import API, api_session, get, paginate, plain_session

token = os.environ["GITHUB_TOKEN"]
owner, repo = os.environ["REPO"].split("/")

AVATAR_DIR = "assets/avatars"
GHOST = {  # what GitHub shows for a deleted account
    "login": "ghost",
    "avatar_url": "https://avatars.githubusercontent.com/u/10137?v=4",
    "html_url": "https://github.com/ghost",
}

api = api_session(token)


def camel_case(name):
    if not name:
        return None
    return " ".join(w.capitalize() for w in name.split())


def fetch_user(stub):
    """Full profile for a user; falls back to the data already on the issue/PR.

    The fallback means one deleted, renamed or otherwise unfetchable account
    cannot take down the whole summary. Only the display name is lost.
    """
    try:
        return get(api, f"{API}/users/{stub['login']}").json()
    except requests.RequestException as exc:
        print(f"  WARNING: could not fetch profile for {stub['login']} ({exc}); using issue data")
        return stub


def new_user(stub, first_date):
    profile = fetch_user(stub)
    return {
        "github_login": stub["login"],
        "display_name": camel_case(profile.get("name")) or stub["login"],
        "avatar_url": profile["avatar_url"],
        "profile_url": profile["html_url"],
        "total_contributions": 0,
        "open_issues": 0,
        "closed_issues": 0,
        "open_prs": 0,
        "merged_prs": 0,
        "closed_prs": 0,
        # Per-year counts for the contribution chart in contributors.html.
        # Precomputed here so the page does not have to call api.github.com
        # live (unauthenticated, 60 requests/hour/IP).
        "years": {},
        "last_contribution_date": first_date,
    }


def record(users, item, bucket):
    stub = item.get("user") or GHOST
    login = stub["login"]
    if login not in users:
        users[login] = new_user(stub, item["created_at"])
    u = users[login]
    u["total_contributions"] += 1
    u[bucket] += 1
    year = item["created_at"][:4]
    u["years"][year] = u["years"].get(year, 0) + 1
    if item["created_at"] > u["last_contribution_date"]:
        u["last_contribution_date"] = item["created_at"]


def _avatar_filename(login, avatar_url):
    url_hash = hashlib.md5(avatar_url.encode()).hexdigest()[:8]
    return f"{login}_{url_hash}.png"


def download_avatars(contributors):
    os.makedirs(AVATAR_DIR, exist_ok=True)
    plain = plain_session()
    for user in contributors:
        login = user.get("github_login", "unknown")
        avatar_url = user.get("avatar_url", "")
        if not avatar_url:
            user["avatar_local"] = ""
            continue

        local_path = os.path.join(AVATAR_DIR, _avatar_filename(login, avatar_url))
        if not os.path.exists(local_path):
            try:
                resp = plain.get(avatar_url.split("?")[0] + "?size=128", timeout=10)
                resp.raise_for_status()
                with open(local_path, "wb") as f:
                    f.write(resp.content)
                print(f"  Downloaded avatar: {os.path.basename(local_path)}")
                time.sleep(0.05)
            except Exception as exc:
                print(f"  WARNING: could not download avatar for {login}: {exc}")
                user["avatar_local"] = ""
                continue
        user["avatar_local"] = local_path
    return contributors


def main():
    base = f"/repos/{owner}/{repo}"
    # The issues endpoint also returns PRs; drop them, PRs are fetched separately.
    issues = [i for i in paginate(api, f"{base}/issues", {"state": "all"}) if "pull_request" not in i]
    prs = list(paginate(api, f"{base}/pulls", {"state": "all"}))

    users = {}
    for issue in issues:
        record(users, issue, "open_issues" if issue["state"] == "open" else "closed_issues")
    for pr in prs:
        if pr["state"] == "open":
            bucket = "open_prs"
        elif pr["merged_at"]:
            bucket = "merged_prs"
        else:
            bucket = "closed_prs"
        record(users, pr, bucket)

    contributors = sorted(users.values(), key=lambda x: x["total_contributions"], reverse=True)
    contributors = download_avatars(contributors)

    with open("issues-summary.json", "w") as f:
        json.dump(contributors, f, indent=2)

    print(f"Wrote {len(contributors)} contributors")
    print(f"Total Issues: {len(issues)}")
    print(f"Total PRs: {len(prs)}")
    print(f"Total Contributions: {sum(u['total_contributions'] for u in users.values())}")


if __name__ == "__main__":
    main()

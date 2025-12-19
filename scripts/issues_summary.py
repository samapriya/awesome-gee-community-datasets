import os
import requests
import json

token = os.environ["GITHUB_TOKEN"]
owner, repo = os.environ["REPO"].split("/")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

def camel_case(name):
    if not name:
        return None
    return " ".join(w.capitalize() for w in name.split())

def fetch_all_issues():
    """Fetch all issues (excluding PRs)"""
    issues = []
    page = 1

    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/issues"
        params = {"state": "all", "per_page": 100, "page": page}
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()

        data = r.json()
        if not data:
            break

        issues.extend(i for i in data if "pull_request" not in i)
        page += 1

    return issues

def fetch_all_prs():
    """Fetch all pull requests"""
    prs = []
    page = 1

    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        params = {"state": "all", "per_page": 100, "page": page}
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()

        data = r.json()
        if not data:
            break

        prs.extend(data)
        page += 1

    return prs

def fetch_user(login):
    r = requests.get(f"https://api.github.com/users/{login}", headers=headers)
    r.raise_for_status()
    return r.json()

# Fetch both issues and PRs
issues = fetch_all_issues()
prs = fetch_all_prs()

users = {}

# Process issues
for issue in issues:
    login = issue["user"]["login"]

    if login not in users:
        profile = fetch_user(login)
        users[login] = {
            "github_login": login,
            "display_name": camel_case(profile.get("name")) or login,
            "avatar_url": profile["avatar_url"],
            "profile_url": profile["html_url"],
            "total_contributions": 0,
            "open_issues": 0,
            "closed_issues": 0,
            "open_prs": 0,
            "merged_prs": 0,
            "closed_prs": 0,
            "last_contribution_date": issue["created_at"]
        }

    u = users[login]
    u["total_contributions"] += 1
    u["open_issues" if issue["state"] == "open" else "closed_issues"] += 1

    if issue["created_at"] > u["last_contribution_date"]:
        u["last_contribution_date"] = issue["created_at"]

# Process PRs
for pr in prs:
    login = pr["user"]["login"]

    if login not in users:
        profile = fetch_user(login)
        users[login] = {
            "github_login": login,
            "display_name": camel_case(profile.get("name")) or login,
            "avatar_url": profile["avatar_url"],
            "profile_url": profile["html_url"],
            "total_contributions": 0,
            "open_issues": 0,
            "closed_issues": 0,
            "open_prs": 0,
            "merged_prs": 0,
            "closed_prs": 0,
            "last_contribution_date": pr["created_at"]
        }

    u = users[login]
    u["total_contributions"] += 1

    # Categorize PR state
    if pr["state"] == "open":
        u["open_prs"] += 1
    elif pr["merged_at"]:
        u["merged_prs"] += 1
    else:
        u["closed_prs"] += 1

    if pr["created_at"] > u["last_contribution_date"]:
        u["last_contribution_date"] = pr["created_at"]

output = sorted(
    users.values(),
    key=lambda x: x["total_contributions"],
    reverse=True
)

with open("issues-summary.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Wrote {len(output)} contributors")
print(f"Total Issues: {len(issues)}")
print(f"Total PRs: {len(prs)}")
print(f"Total Contributions: {sum(u['total_contributions'] for u in users.values())}")

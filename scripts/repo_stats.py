import json
import os
from datetime import datetime

import requests

token = os.environ["GITHUB_TOKEN"]
owner, repo = os.environ["REPO"].split("/")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

def fetch_repo_stats():
    url = f"https://api.github.com/repos/{owner}/{repo}"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()

def fetch_pr_stats():
    """Fetch PR statistics"""
    open_prs = 0
    merged_prs = 0
    closed_prs = 0
    page = 1

    while True:
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        params = {"state": "all", "per_page": 100, "page": page}
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()

        data = r.json()
        if not data:
            break

        for pr in data:
            if pr["state"] == "open":
                open_prs += 1
            elif pr.get("merged_at"):
                merged_prs += 1
            else:
                closed_prs += 1

        page += 1

    return {
        "open_prs": open_prs,
        "merged_prs": merged_prs,
        "closed_prs": closed_prs,
        "total_prs": open_prs + merged_prs + closed_prs
    }

repo_data = fetch_repo_stats()
pr_stats = fetch_pr_stats()

output = {
    "repository": f"{owner}/{repo}",
    "total_stars": repo_data["stargazers_count"],
    "total_forks": repo_data["forks_count"],
    "total_watchers": repo_data["watchers_count"],
    "open_issues": repo_data["open_issues_count"],
    "open_prs": pr_stats["open_prs"],
    "merged_prs": pr_stats["merged_prs"],
    "closed_prs": pr_stats["closed_prs"],
    "total_prs": pr_stats["total_prs"],
    "created_at": repo_data["created_at"],
    "updated_at": repo_data["updated_at"],
    "pushed_at": repo_data["pushed_at"],
    "description": repo_data.get("description"),
    "language": repo_data.get("language"),
    "fetched_at": datetime.utcnow().isoformat() + "Z"
}

with open("repo-stats.json", "w") as f:
    json.dump(output, f, indent=2)

print(f"Repository Stats for {owner}/{repo}:")
print(f"  Total Stars: {output['total_stars']}")
print(f"  Total Forks: {output['total_forks']}")
print(f"  Total Watchers: {output['total_watchers']}")
print(f"  Open Issues: {output['open_issues']}")
print(f"  Open PRs: {output['open_prs']}")
print(f"  Merged PRs: {output['merged_prs']}")
print(f"  Total PRs: {output['total_prs']}")
print(f"\nWrote stats to repo-stats.json")

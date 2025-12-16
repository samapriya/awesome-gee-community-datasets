import os
import requests
import json
from datetime import datetime

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

repo_data = fetch_repo_stats()

output = {
    "repository": f"{owner}/{repo}",
    "total_stars": repo_data["stargazers_count"],
    "total_forks": repo_data["forks_count"],
    "total_watchers": repo_data["watchers_count"],
    "open_issues": repo_data["open_issues_count"],
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
print(f"\nWrote stats to repo-stats.json")

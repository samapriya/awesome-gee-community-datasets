"""Build repo-stats.json. Output format is unchanged; requests now retry (see gh_api)."""
import json
import os
from datetime import datetime, timezone

from gh_api import API, api_session, get, paginate

token = os.environ["GITHUB_TOKEN"]
owner, repo = os.environ["REPO"].split("/")

api = api_session(token)


def fetch_pr_stats():
    counts = {"open_prs": 0, "merged_prs": 0, "closed_prs": 0}
    for pr in paginate(api, f"/repos/{owner}/{repo}/pulls", {"state": "all"}):
        if pr["state"] == "open":
            counts["open_prs"] += 1
        elif pr.get("merged_at"):
            counts["merged_prs"] += 1
        else:
            counts["closed_prs"] += 1
    counts["total_prs"] = sum(counts.values())
    return counts


def main():
    repo_data = get(api, f"{API}/repos/{owner}/{repo}").json()
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
        # same format as before; datetime.utcnow() is deprecated since 3.12
        "fetched_at": datetime.now(timezone.utc).replace(tzinfo=None).isoformat() + "Z",
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
    print("\nWrote stats to repo-stats.json")


if __name__ == "__main__":
    main()

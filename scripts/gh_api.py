"""Shared GitHub API helpers for issues_summary.py and repo_stats.py.

Every request gets a timeout and automatic retries with backoff, so a single
dropped connection ("RemoteDisconnected") or a 5xx no longer fails the run.
"""
import os
import time

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# GitHub Actions sets GITHUB_API_URL; the default covers local runs.
API = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
TIMEOUT = 30


def _retrying_session():
    retry = Retry(
        total=6,
        backoff_factor=1.5,  # 0s, 3s, 6s, 12s, 24s, 48s
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
        respect_retry_after_header=True,
        raise_on_status=False,
    )
    s = requests.Session()
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.mount("http://", HTTPAdapter(max_retries=retry))
    return s


def api_session(token):
    """Session for api.github.com (carries the token)."""
    s = _retrying_session()
    s.headers.update({
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    return s


def plain_session():
    """Session WITHOUT the token, for other hosts (avatar downloads)."""
    return _retrying_session()


def get(session, url, **kwargs):
    """GET that also waits out a GitHub rate limit (403/429) before giving up."""
    kwargs.setdefault("timeout", TIMEOUT)
    for _ in range(3):
        r = session.get(url, **kwargs)
        limited = r.status_code in (403, 429) and (
            "retry-after" in r.headers or r.headers.get("x-ratelimit-remaining") == "0"
        )
        if not limited:
            break
        if "retry-after" in r.headers:
            wait = int(r.headers["retry-after"])
        else:
            wait = int(r.headers.get("x-ratelimit-reset", 0)) - int(time.time())
        wait = max(1, wait) + 1
        if wait > 300:  # not worth holding a runner for; fail with a clear message
            break
        print(f"  rate limited, waiting {wait}s")
        time.sleep(wait)
    r.raise_for_status()
    return r


def paginate(session, path, params=None, per_page=100):
    """Yield every item from a paginated list endpoint."""
    page = 1
    while True:
        q = dict(params or {}, per_page=per_page, page=page)
        data = get(session, f"{API}{path}", params=q).json()
        yield from data
        if len(data) < per_page:
            return
        page += 1

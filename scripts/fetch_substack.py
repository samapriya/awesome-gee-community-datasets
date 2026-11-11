#!/usr/bin/env python3
"""Refresh the post list in docs/substack_blogs.md from the Substack RSS feed.

Standard library only. Tries the RSS2JSON API first (Substack often blocks
GitHub-hosted runner IPs), then the feed directly. If both fail the markdown
file is left untouched and the script exits non-zero.
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

FEED_URL = "https://datacommons.substack.com/feed"
FILENAME = "docs/substack_blogs.md"
START_MARKER = "<!-- START_MARKER -->"
END_MARKER = "<!-- END_MARKER -->"
NUM_ENTRIES = 20
USER_AGENT = "Mozilla/5.0 (compatible; awesome-gee-community-catalog feed fetcher)"


def http_get(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/rss+xml, application/xml, text/xml, application/json, */*",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def via_rss2json():
    api_key = os.environ.get("RSS2JSON_API_KEY")
    if not api_key:
        print("RSS2JSON_API_KEY not set, skipping RSS2JSON")
        return []
    query = urllib.parse.urlencode({"rss_url": FEED_URL, "api_key": api_key, "count": NUM_ENTRIES})
    data = json.loads(http_get(f"https://api.rss2json.com/v1/api.json?{query}"))
    if data.get("status") != "ok":
        raise RuntimeError(f"RSS2JSON error: {data.get('message', 'unknown')}")
    return [(i.get("title", ""), i.get("link", "")) for i in data.get("items", [])]


def parse_rss(xml_bytes):
    root = ET.fromstring(xml_bytes)
    return [(item.findtext("title") or "", item.findtext("link") or "") for item in root.iter("item")]


def via_direct():
    return parse_rss(http_get(FEED_URL))


def fetch_posts():
    for name, method in (("RSS2JSON", via_rss2json), ("direct feed", via_direct)):
        try:
            posts = [(t.strip(), l.strip()) for t, l in method()]
            posts = [(t, l) for t, l in posts if t and l][:NUM_ENTRIES]
        except Exception as exc:
            # str(exc) never contains the API key: urllib errors don't echo the URL
            print(f"{name} failed: {type(exc).__name__}: {exc}")
            continue
        if posts:
            print(f"Fetched {len(posts)} posts via {name}")
            return posts
        print(f"{name} returned no posts")
    return []


def update_markdown(posts):
    if os.path.exists(FILENAME):
        with open(FILENAME, encoding="utf-8") as f:
            content = f.read()
    else:
        os.makedirs(os.path.dirname(FILENAME), exist_ok=True)
        content = f"# Substack Blogs\n\n{START_MARKER}\n\n{END_MARKER}\n"

    original = content
    # One-time cleanup: the old workflow appended one of these every day.
    content = re.sub(r"^<!-- Updated: .*? -->\n?", "", content, flags=re.M)

    if START_MARKER not in content or END_MARKER not in content:
        content = content.rstrip("\n") + f"\n\n{START_MARKER}\n\n{END_MARKER}\n"
    start = content.find(START_MARKER) + len(START_MARKER)
    end = content.find(END_MARKER)

    section = "\n".join(f"* [{title}]({link})" for title, link in posts)
    content = content[:start] + "\n" + section + "\n" + content[end:]

    if content == original:
        print("post list unchanged")
        return
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {FILENAME}")


def main():
    posts = fetch_posts()
    if not posts:
        sys.exit("::error::could not fetch the Substack feed by any method; leaving the page untouched")
    update_markdown(posts)


if __name__ == "__main__":
    main()

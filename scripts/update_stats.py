#!/usr/bin/env python3
"""Refresh the stats list in docs/stats.md from the stats gist. Standard library only."""
import json
import sys
import time
import urllib.request

JSON_URL = "https://gist.githubusercontent.com/samapriya/c604537511cb7ef3b46376ee5aff22c4/raw"
FILENAME = "docs/stats.md"
START_MARKER = "<!-- START_MARKER -->"
END_MARKER = "<!-- END_MARKER -->"


def fetch_json(url, attempts=4):
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.load(resp)
        except Exception as exc:  # network blips, truncated JSON
            print(f"attempt {attempt}/{attempts} failed: {exc}")
            if attempt == attempts:
                raise
            time.sleep(5 * attempt)


def main():
    data = fetch_json(JSON_URL)
    if not isinstance(data, dict) or not data:
        sys.exit("::error::stats gist did not return a non-empty JSON object; leaving docs/stats.md untouched")

    with open(FILENAME, encoding="utf-8") as f:
        content = f.read()

    start = content.find(START_MARKER)
    end = content.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        sys.exit(f"::error file={FILENAME}::START/END markers not found; refusing to rewrite the file")
    start += len(START_MARKER)

    body = "".join(f"* **{key}**: {value}\n" for key, value in data.items())
    updated = content[:start] + "\n" + body + content[end:]

    if updated == content:
        print("stats unchanged")
        return
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"Updated {FILENAME} with {len(data)} stats")


if __name__ == "__main__":
    main()

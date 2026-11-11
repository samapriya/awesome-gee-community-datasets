#!/usr/bin/env python3
"""Build community_datasets.jsonl and community_datasets.csv from community_datasets.json.

Standard library only. Output is byte-compatible with the old inline workflow script.
"""
import csv
import json
import sys

SRC = "community_datasets.json"
FIELDS = ["id", "provider", "title", "type", "tags", "sample_code", "license",
          "license_text", "docs_page", "thematic_group", "thumbnail"]
# CSV column -> JSON key, where they differ
SOURCE_KEY = {"docs_page": "docs"}


def main():
    with open(SRC, encoding="utf-8") as f:
        data = json.load(f)

    rows, errors = [], []
    for i, entry in enumerate(data):
        row = []
        for field in FIELDS:
            if field == "license_text":
                row.append(entry.get("license_text", "NA") if entry.get("license") == "custom" else "NA")
                continue
            key = SOURCE_KEY.get(field, field)
            if key not in entry:
                errors.append(f"entry {i} ({entry.get('id', '?')}): missing '{key}'")
                continue
            row.append(entry[key])
        rows.append(row)

    if errors:
        for e in errors:
            print(f"::error file={SRC}::{e}")
        sys.exit(1)

    with open("community_datasets.jsonl", "w", encoding="utf-8") as f:
        for entry in data:
            f.write(json.dumps(entry) + "\n")

    with open("community_datasets.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",", lineterminator="\n")
        writer.writerow(FIELDS)
        writer.writerows(rows)

    print(f"Wrote {len(data)} datasets to community_datasets.jsonl and community_datasets.csv")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Small local JSONL search helper for the crawled Relativity KB."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHUNKS = ROOT / "data" / "jsonl" / "chunks.jsonl"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Regex or plain text query.")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--collection", choices=["user", "developer"])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pattern = re.compile(args.query, re.IGNORECASE)
    count = 0
    with CHUNKS.open("r", encoding="utf-8") as handle:
        for line in handle:
            item = json.loads(line)
            if args.collection and item["collection"] != args.collection:
                continue
            match = pattern.search(item["text"])
            if not match:
                continue
            snippet_start = max(0, match.start() - 140)
            snippet_end = min(len(item["text"]), match.end() + 260)
            snippet = item["text"][snippet_start:snippet_end].replace("\n", " ")
            print(f"{item['title']}\n{item['url']}\n{snippet}\n")
            count += 1
            if count >= args.limit:
                break
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

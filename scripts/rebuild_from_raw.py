#!/usr/bin/env python3
"""Rebuild Markdown and JSONL outputs from already crawled raw HTML files."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from crawl_relativity import DATA_DIR, ROOT, PageParser, append_jsonl, chunk_markdown_by_headings, now_iso, write_text


PAGES_JSONL = DATA_DIR / "jsonl" / "pages.jsonl"
CHUNKS_JSONL = DATA_DIR / "jsonl" / "chunks.jsonl"


def load_existing_records() -> dict[str, dict]:
    records: dict[str, dict] = {}
    if not PAGES_JSONL.exists():
        return records
    with PAGES_JSONL.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            item = json.loads(line)
            records[item["id"]] = item
    return records


def reset_jsonl() -> None:
    for path in [PAGES_JSONL, CHUNKS_JSONL]:
        if path.exists():
            path.unlink()


def rebuild() -> int:
    records = load_existing_records()
    reset_jsonl()
    rebuilt = 0

    for raw_path in sorted((DATA_DIR / "raw_html").glob("*/*.html")):
        collection = raw_path.parent.name
        page_id = raw_path.stem
        existing = records.get(page_id, {})
        url = existing.get("url")
        if not url:
            print(f"Skipping {raw_path}: URL missing from existing pages.jsonl")
            continue

        body = raw_path.read_bytes()
        html_text = body.decode("utf-8", errors="replace")
        parser = PageParser(url)
        parser.feed(html_text)

        markdown_path = DATA_DIR / "markdown" / collection / f"{page_id}.md"
        content_sha = hashlib.sha256(body).hexdigest()
        fetched_at = existing.get("fetched_at", now_iso())
        markdown = (
            f"---\n"
            f"title: {json.dumps(parser.title, ensure_ascii=False)}\n"
            f"url: {url}\n"
            f"collection: {collection}\n"
            f"fetched_at: {fetched_at}\n"
            f"sha256: {content_sha}\n"
            f"---\n\n"
            f"{parser.markdown}"
        )
        write_text(markdown_path, markdown)

        page_record = {
            "id": page_id,
            "collection": collection,
            "title": parser.title,
            "url": url,
            "raw_html_path": str(raw_path.relative_to(ROOT)).replace("\\", "/"),
            "markdown_path": str(markdown_path.relative_to(ROOT)).replace("\\", "/"),
            "headings": parser.headings,
            "text": parser.plain_text,
            "sha256": content_sha,
            "fetched_at": fetched_at,
        }
        append_jsonl(PAGES_JSONL, page_record)

        for chunk in chunk_markdown_by_headings(markdown, parser.title):
            append_jsonl(
                CHUNKS_JSONL,
                {
                    "chunk_id": f"{page_id}::{chunk['section_slug']}::{chunk['chunk_index']:04d}",
                    "page_id": page_id,
                    "collection": collection,
                    "page_title": parser.title,
                    "title": parser.title,
                    "section_title": chunk["section_title"],
                    "heading_level": chunk["heading_level"],
                    "heading_path": chunk["heading_path"],
                    "part": chunk["part"],
                    "part_count": chunk["part_count"],
                    "url": url,
                    "text": chunk["text"],
                },
            )

        rebuilt += 1
        if rebuilt % 100 == 0:
            print(f"Rebuilt {rebuilt} pages...")

    print(f"Rebuilt {rebuilt} pages from raw HTML.")
    return 0


if __name__ == "__main__":
    raise SystemExit(rebuild())

#!/usr/bin/env python3
"""
Crawl Relativity Server 2025 documentation into raw HTML, Markdown, and JSONL.

The crawler intentionally uses only Python's standard library so it can run in a
fresh Windows workstation without installing dependencies.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
USER_AGENT = "RelativityKnowledgeBaseCrawler/1.0 (+local research archive)"


@dataclass(frozen=True)
class Source:
    collection: str
    seed: str
    allowed_prefix: str


@dataclass
class HeadingNode:
    level: int
    title: str
    content: list[str]
    children: list["HeadingNode"]


SOURCES = [
    Source(
        collection="user",
        seed="https://help.relativity.com/Server2025/Content/Relativity/Data_Grid/Monitoring_Data_Grid.htm",
        allowed_prefix="https://help.relativity.com/Server2025/Content/",
    ),
    Source(
        collection="developer",
        seed="https://platform.relativity.com/Server2025/Content/Relativity_Platform/index.htm",
        allowed_prefix="https://platform.relativity.com/Server2025/Content/",
    ),
]


SKIP_EXTENSIONS = {
    ".7z",
    ".bmp",
    ".css",
    ".csv",
    ".doc",
    ".docx",
    ".eot",
    ".exe",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".js",
    ".mp4",
    ".pdf",
    ".png",
    ".ppt",
    ".pptx",
    ".svg",
    ".ttf",
    ".txt",
    ".woff",
    ".woff2",
    ".xls",
    ".xlsx",
    ".zip",
}


class PageParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.links: list[str] = []
        self.title_parts: list[str] = []
        self.markdown_parts: list[str] = []
        self.text_parts: list[str] = []
        self.headings: list[str] = []
        self._skip_depth = 0
        self._tag_stack: list[str] = []
        self._current_href: str | None = None
        self._in_title = False
        self._in_pre = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k.lower(): v or "" for k, v in attrs}
        tag = tag.lower()

        if tag in {"script", "style", "noscript", "svg"}:
            self._skip_depth += 1
            return

        if tag == "title":
            self._in_title = True

        if tag == "a":
            href = attrs_dict.get("href")
            if href:
                self.links.append(urljoin(self.base_url, href))
                self._current_href = href

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "pre", "br", "tr"}:
            self._newline()

        if tag == "li":
            self._append_md("- ")
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag[1])
            self._append_md("#" * level + " ")
        elif tag == "pre":
            self._in_pre = True
            self._append_md("```text\n")

        self._tag_stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self._skip_depth and tag in {"script", "style", "noscript", "svg"}:
            self._skip_depth -= 1
            return

        if tag == "title":
            self._in_title = False
        elif tag == "a":
            self._current_href = None
        elif tag == "pre":
            self._append_md("\n```")
            self._in_pre = False

        if tag in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "pre", "tr", "div", "section"}:
            self._newline()

        for idx in range(len(self._tag_stack) - 1, -1, -1):
            if self._tag_stack[idx] == tag:
                del self._tag_stack[idx]
                break

    def handle_data(self, data: str) -> None:
        if self._skip_depth:
            return

        value = html.unescape(data)
        if not value.strip():
            if self._in_pre:
                self._append_md(value)
            return

        if self._in_title:
            self.title_parts.append(value.strip())

        normalized = value if self._in_pre else re.sub(r"\s+", " ", value).strip()
        if not normalized:
            return

        if self._tag_stack and self._tag_stack[-1] in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(normalized)

        self.text_parts.append(normalized)
        self._append_md(normalized)
        if not self._in_pre:
            self._append_md(" ")

    def _append_md(self, value: str) -> None:
        self.markdown_parts.append(value)

    def _newline(self) -> None:
        if self.markdown_parts and not self.markdown_parts[-1].endswith("\n"):
            self.markdown_parts.append("\n")
        if self.markdown_parts and not "".join(self.markdown_parts[-3:]).endswith("\n\n"):
            self.markdown_parts.append("\n")

    @property
    def title(self) -> str:
        title = " ".join(part for part in self.title_parts if part).strip()
        if title:
            return re.sub(r"\s+", " ", title)
        return self.headings[0] if self.headings else self.base_url

    @property
    def markdown(self) -> str:
        text = "".join(self.markdown_parts)
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = strip_boilerplate(text)
        return text.strip() + "\n"

    @property
    def plain_text(self) -> str:
        text = "\n".join(part.strip() for part in self.text_parts if part.strip())
        text = re.sub(r"\n{3,}", "\n\n", text)
        return strip_boilerplate(text).strip()


def strip_boilerplate(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    drop_exact = {
        "Skip To Main Content",
        "Account",
        "Settings",
        "Logout",
        "Feedback",
        "placeholder",
        "Account Settings Logout",
        "Coveo Search Page",
        "Version:",
        "RelativityOne",
        "Server 2025",
        "Server 2024",
        ">>",
        "☰",
        "â˜°",
        "Name (optional): Email (optional): Message:",
        "Name (Optional): Email (Optional): Message (Required):",
    }
    truncate_at = {
        "On this page",
        "Why was this not helpful?",
        "Name (optional):",
        "Name (Optional):",
        "IncludedTopics",
    }
    kept: list[str] = []
    for idx, line in enumerate(lines):
        if " Skip To Main Content" in line:
            line = line.split(" Skip To Main Content", 1)[0].rstrip()

        compact = re.sub(r"\s+", " ", line).strip()
        compact_unbulleted = compact[2:].strip() if compact.startswith("- ") else compact
        compact_plain = compact_unbulleted.lstrip("#").strip()
        remaining = "\n".join(lines[idx:])
        if compact_plain in truncate_at:
            break
        if compact_plain.startswith("For more information on using the Feedback form"):
            break
        if compact_plain == "Install Relativity" and "231 South LaSalle Street" in remaining:
            break
        if compact_plain == "Additional Resources" and "Privacy and Cookies" in remaining:
            break
        if compact_plain in drop_exact:
            continue
        if compact_plain.startswith("Version: RelativityOne"):
            continue
        if re.fullmatch(r"relativity[a-z0-9]{8,}", compact_plain):
            continue
        if compact_plain.endswith("/CoveoSearch.htm") or compact_plain.endswith("\\CoveoSearch.htm"):
            continue
        if compact_plain.startswith("https://relativity") and "coveo.com/rest/search" in compact_plain:
            continue
        if compact_plain.startswith("xx") and len(compact_plain) > 20:
            continue
        kept.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip()


def normalize_url(url: str) -> str:
    url, _fragment = urldefrag(url)
    parsed = urlparse(url)
    path = re.sub(r"/+", "/", parsed.path)
    return parsed._replace(path=path, query="").geturl()


def is_allowed_doc_url(url: str, source: Source) -> bool:
    normalized = normalize_url(url)
    if not normalized.startswith(source.allowed_prefix):
        return False
    path = urlparse(normalized).path.lower()
    suffix = Path(path).suffix
    if suffix and suffix in SKIP_EXTENSIONS:
        return False
    if suffix and suffix not in {".htm", ".html"}:
        return False
    return True


def page_id(collection: str, url: str) -> str:
    parsed = urlparse(url)
    slug = parsed.path.strip("/").replace("/", "__")
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", slug)
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"{collection}__{slug}__{digest}"


def fetch(url: str, timeout: int) -> tuple[bytes, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*"})
    with urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get_content_charset() or "utf-8"
        return response.read(), content_type


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def append_jsonl(path: Path, item: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")


def reset_outputs() -> None:
    for file_path in [
        DATA_DIR / "jsonl" / "pages.jsonl",
        DATA_DIR / "jsonl" / "chunks.jsonl",
        DATA_DIR / "manifests" / "crawl_errors.jsonl",
    ]:
        if file_path.exists():
            file_path.unlink()


def slugify(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return slug[:80] or "section"


def strip_front_matter(markdown: str) -> str:
    if markdown.startswith("---\n"):
        end = markdown.find("\n---\n", 4)
        if end != -1:
            return markdown[end + 5 :].strip()
    return markdown.strip()


def markdown_to_plain_text(markdown: str) -> str:
    text = strip_front_matter(markdown)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"```[a-zA-Z0-9_-]*\n", "", text)
    text = text.replace("```", "")
    text = re.sub(r"^\s*[-*]\s+", "", text, flags=re.MULTILINE)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def parse_heading_tree(markdown: str, page_title: str) -> HeadingNode:
    root = HeadingNode(level=0, title=page_title, content=[], children=[])
    stack = [root]
    in_code = False

    for raw_line in strip_front_matter(markdown).splitlines():
        line = raw_line.rstrip()
        if line.startswith("```"):
            in_code = not in_code

        heading = None if in_code else re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            level = len(heading.group(1))
            title = heading.group(2).strip()
            while stack and stack[-1].level >= level:
                stack.pop()
            node = HeadingNode(level=level, title=title, content=[], children=[])
            stack[-1].children.append(node)
            stack.append(node)
            continue

        # The scraper often emits a duplicate page title immediately before H1.
        if stack[-1] is root and line.strip() == page_title and not root.content:
            continue
        stack[-1].content.append(line)

    return root


def render_node(node: HeadingNode, include_children: bool = True) -> str:
    parts: list[str] = []
    if node.level:
        parts.append(f"{'#' * node.level} {node.title}".strip())
    content = "\n".join(node.content).strip()
    if content:
        parts.append(content)
    if include_children:
        for child in node.children:
            child_text = render_node(child, include_children=True)
            if child_text:
                parts.append(child_text)
    return re.sub(r"\n{3,}", "\n\n", "\n\n".join(parts)).strip()


def split_markdown_by_paragraphs(text: str, max_chars: int) -> list[str]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0

    for paragraph in paragraphs:
        if len(paragraph) > max_chars:
            if current:
                chunks.append("\n\n".join(current).strip())
                current = []
                current_len = 0

            line_chunk: list[str] = []
            line_len = 0
            for line in paragraph.splitlines():
                if len(line) > max_chars:
                    if line_chunk:
                        chunks.append("\n".join(line_chunk).strip())
                        line_chunk = []
                        line_len = 0
                    for start in range(0, len(line), max_chars):
                        chunks.append(line[start : start + max_chars].strip())
                    continue
                if line_chunk and line_len + len(line) + 1 > max_chars:
                    chunks.append("\n".join(line_chunk).strip())
                    line_chunk = []
                    line_len = 0
                line_chunk.append(line)
                line_len += len(line) + 1
            if line_chunk:
                chunks.append("\n".join(line_chunk).strip())
            continue

        if current and current_len + len(paragraph) + 2 > max_chars:
            chunks.append("\n\n".join(current).strip())
            current = []
            current_len = 0
        current.append(paragraph)
        current_len += len(paragraph) + 2

    if current:
        chunks.append("\n\n".join(current).strip())
    return chunks


def chunk_node(node: HeadingNode, path: list[str], max_chars: int) -> list[dict]:
    text = render_node(node, include_children=True)
    if not text:
        return []

    if len(text) <= max_chars or not node.children:
        parts = [text] if len(text) <= max_chars else split_markdown_by_paragraphs(text, max_chars)
        total = len(parts)
        return [
            {
                "heading_level": node.level,
                "heading_path": path,
                "section_title": node.title,
                "text": part,
                "part": idx + 1,
                "part_count": total,
            }
            for idx, part in enumerate(parts)
            if part
        ]

    chunks: list[dict] = []
    intro = render_node(HeadingNode(node.level, node.title, node.content, []), include_children=False)
    if intro:
        chunks.extend(chunk_node(HeadingNode(node.level, node.title, node.content, []), path, max_chars))
    for child in node.children:
        chunks.extend(chunk_node(child, path + [child.title], max_chars))
    return chunks


def chunk_markdown_by_headings(markdown: str, page_title: str, max_chars: int = 8000) -> list[dict]:
    root = parse_heading_tree(markdown, page_title)
    chunks: list[dict] = []

    if root.content and "\n".join(root.content).strip():
        preface = "\n".join(root.content).strip()
        parts = split_markdown_by_paragraphs(preface, max_chars)
        for idx, part in enumerate(parts):
            chunks.append(
                {
                    "heading_level": 0,
                    "heading_path": [page_title],
                    "section_title": page_title,
                    "text": part,
                    "part": idx + 1,
                    "part_count": len(parts),
                }
            )

    for child in root.children:
        if child.level == 1 and child.children:
            intro = render_node(HeadingNode(child.level, child.title, child.content, []), include_children=False)
            if intro:
                chunks.extend(chunk_node(HeadingNode(child.level, child.title, child.content, []), [child.title], max_chars))
            for grandchild in child.children:
                chunks.extend(chunk_node(grandchild, [child.title, grandchild.title], max_chars))
        else:
            chunks.extend(chunk_node(child, [child.title], max_chars))

    if not chunks:
        text = markdown_to_plain_text(markdown)
        if text:
            chunks.append(
                {
                    "heading_level": 0,
                    "heading_path": [page_title],
                    "section_title": page_title,
                    "text": text,
                    "part": 1,
                    "part_count": 1,
                }
            )

    bounded_chunks: list[dict] = []
    for chunk in chunks:
        if len(chunk["text"]) <= max_chars:
            bounded_chunks.append(chunk)
            continue

        parts = split_markdown_by_paragraphs(chunk["text"], max_chars)
        total = len(parts)
        for idx, part in enumerate(parts):
            if not part:
                continue
            bounded_chunks.append(
                {
                    **chunk,
                    "text": part,
                    "part": idx + 1,
                    "part_count": total,
                }
            )

    for index, chunk in enumerate(bounded_chunks):
        chunk["chunk_index"] = index
        chunk["section_slug"] = slugify(" ".join(chunk["heading_path"]))
    return bounded_chunks


def crawl_source(source: Source, args: argparse.Namespace, seen: set[str], stats: dict) -> None:
    queue: deque[str] = deque([normalize_url(source.seed)])
    queued = set(queue)

    while queue:
        if args.max_pages and stats["fetched"] >= args.max_pages:
            return

        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        pid = page_id(source.collection, url)
        markdown_path = DATA_DIR / "markdown" / source.collection / f"{pid}.md"
        raw_path = DATA_DIR / "raw_html" / source.collection / f"{pid}.html"
        if args.resume and markdown_path.exists():
            stats["skipped_existing"] += 1
            continue

        try:
            body, charset = fetch(url, args.timeout)
            html_text = body.decode(charset, errors="replace")
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            stats["errors"] += 1
            append_jsonl(
                DATA_DIR / "manifests" / "crawl_errors.jsonl",
                {
                    "collection": source.collection,
                    "url": url,
                    "error": repr(exc),
                    "fetched_at": now_iso(),
                },
            )
            continue

        parser = PageParser(url)
        parser.feed(html_text)

        for link in parser.links:
            normalized = normalize_url(link)
            if normalized not in seen and normalized not in queued and is_allowed_doc_url(normalized, source):
                queue.append(normalized)
                queued.add(normalized)

        raw_path.parent.mkdir(parents=True, exist_ok=True)
        raw_path.write_bytes(body)

        content_sha = hashlib.sha256(body).hexdigest()
        markdown = (
            f"---\n"
            f"title: {json.dumps(parser.title, ensure_ascii=False)}\n"
            f"url: {url}\n"
            f"collection: {source.collection}\n"
            f"fetched_at: {now_iso()}\n"
            f"sha256: {content_sha}\n"
            f"---\n\n"
            f"{parser.markdown}"
        )
        write_text(markdown_path, markdown)

        page_record = {
            "id": pid,
            "collection": source.collection,
            "title": parser.title,
            "url": url,
            "raw_html_path": str(raw_path.relative_to(ROOT)).replace("\\", "/"),
            "markdown_path": str(markdown_path.relative_to(ROOT)).replace("\\", "/"),
            "headings": parser.headings,
            "text": parser.plain_text,
            "sha256": content_sha,
            "fetched_at": now_iso(),
        }
        append_jsonl(DATA_DIR / "jsonl" / "pages.jsonl", page_record)

        for chunk in chunk_markdown_by_headings(markdown, parser.title):
            append_jsonl(
                DATA_DIR / "jsonl" / "chunks.jsonl",
                {
                    "chunk_id": f"{pid}::{chunk['section_slug']}::{chunk['chunk_index']:04d}",
                    "page_id": pid,
                    "collection": source.collection,
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

        stats["fetched"] += 1
        stats["queued"] = len(queue)
        print(f"[{stats['fetched']:05d}] {source.collection}: {parser.title} <{url}>")
        time.sleep(args.delay)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def write_manifest(args: argparse.Namespace, stats: dict) -> None:
    manifest = {
        "created_at": now_iso(),
        "sources": [source.__dict__ for source in SOURCES],
        "args": vars(args),
        "stats": stats,
    }
    write_text(DATA_DIR / "manifests" / "crawl_manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-pages", type=int, default=0, help="Stop after this many fetched pages. Default: no limit.")
    parser.add_argument("--delay", type=float, default=0.25, help="Delay between requests in seconds.")
    parser.add_argument("--timeout", type=int, default=30, help="HTTP timeout in seconds.")
    parser.add_argument("--resume", action="store_true", help="Keep existing outputs and skip pages already written.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.resume:
        reset_outputs()

    stats = {"fetched": 0, "errors": 0, "queued": 0, "skipped_existing": 0}
    seen: set[str] = set()
    for source in SOURCES:
        crawl_source(source, args, seen, stats)
    write_manifest(args, stats)
    print(json.dumps(stats, ensure_ascii=False, indent=2))
    return 0 if stats["errors"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

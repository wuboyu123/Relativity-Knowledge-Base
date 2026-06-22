# Relativity Server 2025 Knowledge Base

This repository is set up to mirror and normalize Relativity Server 2025 documentation for local search and future RAG workflows.

## Sources

- User docs: `https://help.relativity.com/Server2025/Content/`
- Developer docs: `https://platform.relativity.com/Server2025/Content/`

## Crawl

Run:

```powershell
python .\scripts\crawl_relativity.py
```

Useful options:

```powershell
python .\scripts\crawl_relativity.py --max-pages 50
python .\scripts\crawl_relativity.py --delay 0.5
python .\scripts\crawl_relativity.py --resume
```

## Output Layout

- `data/raw_html/` - source HTML, kept for audit/re-processing.
- `data/markdown/` - cleaned Markdown, ideal for `rg` or reading directly.
- `data/jsonl/pages.jsonl` - one JSON object per page with metadata and full text.
- `data/jsonl/chunks.jsonl` - chunked records suitable for embedding/RAG.
- `data/manifests/crawl_manifest.json` - crawl stats and source configuration.

## Grep Examples

```powershell
rg -n "Data Grid" .\data\markdown
rg -n "Object Manager" .\data\markdown\developer
rg -n "workspace" .\data\jsonl\chunks.jsonl
```

## RAG Notes

Use `data/jsonl/chunks.jsonl` as the embedding input. Each chunk keeps:

- `chunk_id`
- `page_id`
- `collection`
- `title`
- `url`
- `text`

That gives enough metadata to cite the original Relativity page after retrieval.

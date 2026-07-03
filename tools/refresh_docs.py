"""Refresh the bundled iSolarCloud documentation knowledge base.

Fetches the official developer docs from the iSolarCloud OpenAPI doc portal and
rewrites `src/mcp_isolarcloud/knowledge/`. No credentials or login are required —
the portal doc API is public (see tools/_isc_client.py for the request scheme).
Documents are fetched by their manage_id and de-duplicated across projects.

Usage:  python tools/refresh_docs.py      (requires: cryptography, markdownify)
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from pathlib import Path

from markdownify import markdownify

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _isc_client import call, fetch_tree  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "src" / "mcp_isolarcloud" / "knowledge"


def slugify(name: str) -> str:
    return (re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "doc")[:80]


def to_md(html: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", markdownify(html or "", heading_style="ATX", bullets="-")).strip()


def main() -> None:
    docs_dir = OUT / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    for old in docs_dir.glob("*.md"):
        old.unlink()

    manage_ids = {n["manage_id"] for n in fetch_tree() if n.get("document_type") == 3 and n.get("manage_id")}

    docs: list[dict] = []
    seen: dict[str, str] = {}
    print(f"{len(manage_ids)} documents to fetch")
    for mid in sorted(manage_ids):
        d = call("queryApiDocumentDetailForUser", {"id": mid}).get("result_data", {}).get("document")
        if not d:
            continue
        name = d.get("document_name") or f"doc-{mid}"
        body = to_md(d.get("markdown_doc_en_us") or d.get("markdown_doc") or "")
        api = {
            k: d[k]
            for k in ("api_path", "api_method", "api_desc", "request_example", "response_example_sec")
            if d.get(k)
        }
        if not body and not api:
            continue
        chash = hashlib.sha1((body + json.dumps(api, sort_keys=True)).encode()).hexdigest()
        if chash in seen:
            continue
        slug = slugify(name)
        base, n = slug, 2
        while any(x["slug"] == slug for x in docs):
            slug, n = f"{base}-{n}", n + 1
        seen[chash] = slug
        md = f"# {name}\n\n"
        if api.get("api_path"):
            md += f"`{api.get('api_method', 'POST')} {api['api_path']}`\n\n{to_md(api.get('api_desc', ''))}\n\n"
        md += body
        if api.get("request_example"):
            md += f"\n\n## Request example\n\n```json\n{api['request_example']}\n```"
        if api.get("response_example_sec"):
            md += f"\n\n## Response example\n\n```json\n{api['response_example_sec']}\n```"
        (docs_dir / f"{slug}.md").write_text(md.strip() + "\n", encoding="utf-8")
        docs.append({"slug": slug, "manage_id": mid, "title": name, "type": "api" if api.get("api_path") else "guide"})
        time.sleep(0.2)

    (OUT / "documents.json").write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(docs)} documents to {docs_dir}")


if __name__ == "__main__":
    main()

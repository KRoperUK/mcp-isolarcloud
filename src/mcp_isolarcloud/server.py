"""MCP server exposing the Sungrow iSolarCloud OpenAPI documentation.

Serves the official developer docs (scraped into the bundled knowledge base) as
searchable tools + resources, plus a small set of how-to "skill" prompts. Run it
with `uvx mcp-isolarcloud` (stdio) — no network or credentials required; the docs
are shipped with the package.
"""

from __future__ import annotations

import json
from functools import lru_cache
from importlib import resources

from fastmcp import FastMCP

mcp = FastMCP(
    name="iSolarCloud Docs",
    instructions=(
        "Reference for the Sungrow iSolarCloud OpenAPI. Use `search_docs` to find "
        "relevant pages, `read_doc` to read one, and `list_docs` to browse. The "
        "`control_parameters` page (Appendix 10) is the authoritative source for "
        "device dispatch/control parameter codes, units and value encodings."
    ),
)


@lru_cache(maxsize=1)
def _index() -> list[dict]:
    data = resources.files("mcp_isolarcloud.knowledge").joinpath("documents.json").read_text(encoding="utf-8")
    return json.loads(data)


@lru_cache(maxsize=256)
def _read(slug: str) -> str | None:
    try:
        return resources.files("mcp_isolarcloud.knowledge.docs").joinpath(f"{slug}.md").read_text(encoding="utf-8")
    except (FileNotFoundError, ModuleNotFoundError):
        return None


@mcp.tool
def list_docs() -> list[dict]:
    """List every available iSolarCloud documentation page (slug, title, type)."""
    return [{"slug": d["slug"], "title": d["title"], "type": d["type"]} for d in _index()]


@mcp.tool
def read_doc(slug: str) -> str:
    """Return the full markdown of one documentation page by its slug (see `list_docs`)."""
    body = _read(slug)
    if body is None:
        available = ", ".join(d["slug"] for d in _index())
        return f"No document '{slug}'. Available slugs: {available}"
    return body


@mcp.tool
def search_docs(query: str, limit: int = 8) -> list[dict]:
    """Search the docs by keyword; returns ranked pages with a matching snippet.

    Args:
        query: words to search for (case-insensitive).
        limit: maximum number of results.
    """
    terms = [t for t in query.lower().split() if t]
    results = []
    for d in _index():
        body = _read(d["slug"]) or ""
        title = d["title"].lower()
        low = body.lower()
        # Title matches are weighted heavily so the most on-topic page ranks first.
        score = sum(10 * title.count(t) + low.count(t) for t in terms)
        if not score:
            continue
        # First line containing any term, as a snippet.
        snippet = ""
        for line in body.splitlines():
            low = line.lower()
            if any(t in low for t in terms) and line.strip():
                snippet = line.strip()[:200]
                break
        results.append({"slug": d["slug"], "title": d["title"], "score": score, "snippet": snippet})
    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:limit]


@mcp.resource("isolarcloud://docs/{slug}")
def doc_resource(slug: str) -> str:
    """Expose each documentation page as an MCP resource."""
    return _read(slug) or f"No document '{slug}'."


@mcp.prompt
def find_control_parameter(what: str) -> str:
    """Skill: locate the control/dispatch parameter for a device action and its encoding."""
    return (
        f"I want to control a Sungrow device: {what}. Use `read_doc('appendix-10-control-parameter-definitions')` "
        "to find the matching param_code, its device type, and the exact value encoding (note that ratios/SOC are "
        "often sent as tenths, e.g. 700-1000 for 70-100%, and power is in watts). Then explain how to set it via "
        "the update-parameters API."
    )


@mcp.prompt
def api_call_walkthrough(endpoint: str) -> str:
    """Skill: walk through how to call a specific iSolarCloud API endpoint."""
    return (
        f"Explain how to call the iSolarCloud endpoint '{endpoint}'. First `search_docs('{endpoint}')`, then "
        "`read_doc` the matching page. Cover the request parameters, the encryption/auth requirements, and give a "
        "concrete request/response example from the docs."
    )


def main() -> None:
    """Console entry point (stdio transport)."""
    mcp.run()


if __name__ == "__main__":
    main()

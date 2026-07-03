# mcp-isolarcloud

An [MCP](https://modelcontextprotocol.io) server that serves the **Sungrow iSolarCloud OpenAPI documentation** — the official developer docs, control-parameter reference, device-type dictionary, error codes and measuring-point tables — as searchable tools, resources and how-to "skill" prompts.

The full documentation set is **bundled with the package**, so the server needs no network access or credentials at runtime.

## Why

Building against the iSolarCloud API (e.g. the [`sungrow-isolarcloud`](https://github.com/KRoperUK/pysolarcloud) client or the [Home Assistant integration](https://github.com/KRoperUK/sungrow-hass)) means constantly cross-referencing the developer portal — whose docs live behind a JavaScript app. This server puts them one tool call away for any MCP-capable assistant, including the authoritative **Appendix 10: Control Parameter Definitions** (param codes, units and value encodings — e.g. SOC is sent as tenths of a percent, power in watts).

## Run it

With [`uv`](https://docs.astral.sh/uv/) (recommended — no install step):

```bash
uvx mcp-isolarcloud
```

Or add it to an MCP client (Claude Desktop / Claude Code / etc.):

```json
{
  "mcpServers": {
    "isolarcloud": {
      "command": "uvx",
      "args": ["mcp-isolarcloud"]
    }
  }
}
```

For Claude Code: `claude mcp add isolarcloud -- uvx mcp-isolarcloud`

## What it exposes

**Tools**
- `list_docs()` — every documentation page (slug, title, type)
- `read_doc(slug)` — the full markdown of one page
- `search_docs(query, limit=8)` — keyword search, title-weighted, with snippets

**Resources**
- `isolarcloud://docs/{slug}` — each page as an MCP resource

**Prompts (skills)**
- `find_control_parameter(what)` — locate a dispatch/control parameter and its value encoding
- `api_call_walkthrough(endpoint)` — walk through calling a specific API endpoint

## Updating the docs

The bundled docs are refreshed from the portal with:

```bash
pip install cryptography markdownify
python tools/refresh_docs.py
```

The portal's doc API is public (no login); `refresh_docs.py` reproduces its request-encryption scheme using the public keys embedded in the portal's own web app.

## Development

```bash
uv venv && uv pip install -e '.[dev]'
ruff check src/ tests/
pytest
```

## License

MIT

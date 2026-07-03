"""Tests for the iSolarCloud docs MCP server."""

from mcp_isolarcloud import server


def test_docs_are_bundled():
    docs = server._index()
    assert len(docs) >= 20
    slugs = {d["slug"] for d in docs}
    assert "appendix-10-control-parameter-definitions" in slugs


def test_list_docs_shape():
    for d in server.list_docs():
        assert set(d) == {"slug", "title", "type"}


def test_read_doc_returns_markdown():
    body = server.read_doc("appendix-10-control-parameter-definitions")
    assert body.startswith("# ")
    # The authoritative control-parameter encodings are present.
    assert "Charging/Discharging Power" in body
    assert "700 to 1000" in body  # SOC upper limit is tenths of a percent


def test_read_doc_unknown_slug_lists_available():
    out = server.read_doc("does-not-exist")
    assert "No document" in out


def test_search_ranks_relevant_doc_first():
    results = server.search_docs("control parameter definitions")
    assert results
    assert results[0]["slug"] == "appendix-10-control-parameter-definitions"
    assert results[0]["score"] > 0


def test_search_no_match_is_empty():
    assert server.search_docs("zzzznotarealterm") == []

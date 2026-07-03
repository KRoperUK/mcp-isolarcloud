"""Generate openapi.json + openapi.yaml for the iSolarCloud OpenAPI.

Fetches every documented endpoint (path, method, request params, response fields,
examples) from the developer portal and writes a deterministic OpenAPI 3.1 spec
to the repo root. Run in CI to verify the committed spec is up to date:

    python tools/build_openapi.py && git diff --exit-code openapi.json openapi.yaml
"""

from __future__ import annotations

import contextlib
import json
import sys
import time
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _isc_client import call, fetch_tree  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def _infer_type(example) -> str:
    s = str(example if example is not None else "").strip()
    if s.lower() in ("true", "false"):
        return "boolean"
    for cast, name in ((int, "integer"), (float, "number")):
        try:
            cast(s)
            return name
        except ValueError:
            continue
    return "string"


def _request_schema(params: list[dict]) -> dict:
    props: dict = {}
    required: list[str] = []
    for p in params:
        name = p.get("parameter_name")
        if not name or "." in name:
            continue
        prop = {"type": _infer_type(p.get("parameter_value")), "description": (p.get("parameter_desc") or "").strip()}
        if p.get("parameter_value") not in (None, ""):
            prop["example"] = p["parameter_value"]
        props[name] = prop
        if p.get("is_necessary") == 1:
            required.append(name)
    schema: dict = {"type": "object", "properties": props}
    if required:
        schema["required"] = required
    return schema


def _response_schema(params: list[dict]) -> dict:
    root: dict = {"type": "object", "properties": {}}
    for p in params:
        name = p.get("parameter_name")
        if not name:
            continue
        node = root
        parts = name.split(".")
        for i, part in enumerate(parts):
            props = node.setdefault("properties", {})
            if i == len(parts) - 1:
                props.setdefault(
                    part,
                    {
                        "type": _infer_type(p.get("parameter_value")),
                        "description": (p.get("parameter_desc") or "").strip(),
                    },
                )
            else:
                child = props.get(part)
                if not child or child.get("type") != "object":
                    child = props[part] = {"type": "object", "properties": {}}
                node = child
    return root


def build_spec() -> dict:
    endpoints: dict[str, int] = {}
    for n in fetch_tree():
        if n.get("api_path") and n.get("manage_id"):
            endpoints.setdefault(n["api_path"], n["manage_id"])

    paths: dict = {}
    total = len(endpoints)
    print(f"{total} unique endpoints", flush=True)
    for i, (path, mid) in enumerate(sorted(endpoints.items()), 1):
        d = call("queryApiDocumentDetailForUser", {"id": mid}).get("result_data", {}).get("document")
        if not d:
            continue
        method = "post" if str(d.get("api_method")) in ("2", "POST", "post") else "get"
        op: dict = {
            "summary": (d.get("document_name") or path.rsplit("/", 1)[-1]).strip(),
            "description": (d.get("api_desc") or "").strip(),
            "operationId": path.rsplit("/", 1)[-1],
            "responses": {
                "200": {
                    "description": "Success",
                    "content": {
                        "application/json": {"schema": _response_schema(d.get("api_details_list_response") or [])}
                    },
                }
            },
        }
        req = _request_schema(d.get("api_details_list_request") or [])
        if req["properties"]:
            content: dict = {"schema": req}
            with contextlib.suppress(json.JSONDecodeError, TypeError):
                content["example"] = json.loads(d.get("request_example") or "")
            op["requestBody"] = {"required": True, "content": {"application/json": content}}
        paths[path] = {method: op}
        print(f"  [{i}/{total}] {method.upper()} {path}", flush=True)
        time.sleep(0.12)

    return {
        "openapi": "3.1.0",
        "info": {
            "title": "Sungrow iSolarCloud OpenAPI",
            "version": "1.0.0",
            "description": (
                "Unofficial OpenAPI description of the Sungrow iSolarCloud OpenAPI, generated from the official "
                "developer-portal documentation (https://developer-api.isolarcloud.com). All requests are POST with a "
                "JSON body that also carries `appkey` and `lang`; authentication uses `x-access-key` + a Bearer token. "
                "Not affiliated with or endorsed by Sungrow."
            ),
        },
        "servers": [
            {"url": "https://gateway.isolarcloud.eu", "description": "Europe"},
            {"url": "https://gateway.isolarcloud.com", "description": "International"},
            {"url": "https://gateway.isolarcloud.com.hk", "description": "China"},
            {"url": "https://augateway.isolarcloud.com", "description": "Australia"},
        ],
        "paths": dict(sorted(paths.items())),
    }


def main() -> None:
    spec = build_spec()
    (ROOT / "openapi.json").write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "openapi.yaml").write_text(
        yaml.safe_dump(spec, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8"
    )
    print(f"\nWrote openapi.json/.yaml with {len(spec['paths'])} paths")


if __name__ == "__main__":
    main()

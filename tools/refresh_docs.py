"""Refresh the bundled iSolarCloud documentation knowledge base.

Fetches the official developer docs from the iSolarCloud OpenAPI doc portal and
rewrites `src/mcp_isolarcloud/knowledge/`. No credentials or login are required —
the portal doc API is public, gated only by a request-encryption scheme whose
public keys are embedded in the portal's own web app (reproduced below).

Usage:  python tools/refresh_docs.py      (requires: cryptography, markdownify)

The scheme: body = hex(AES-128-ECB/Pkcs7(k, JSON)); k = "web"+13 hex chars;
x-random-secret-key = base64(RSA-PKCS1v15(pubkey, k)); the response is hex,
decrypted with the same k. Documents are fetched by their manage_id and
de-duplicated across projects.
"""

from __future__ import annotations

import base64
import hashlib
import json
import re
import secrets
import time
import urllib.request
from pathlib import Path

from cryptography.hazmat.primitives import padding as sympad
from cryptography.hazmat.primitives.asymmetric import padding as apad
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import load_der_public_key
from markdownify import markdownify

# Public values published in the iSolarCloud developer-portal web app.
PUB_URLSAFE = (
    "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC99_yC4U4ZfiINho1JfyqQ3kyCF7T3spyDHOM7dfnKgL8lYvLt6_9WsQN7J1"
    "EzBs5Uy0Rq426mbFqINIOfQRQ-ccYoRWoiVJK9JdukW_wqhxrscFFypjyxwS4hRwvuCey9pvugS5HafoF1aq3_TvJOzOtY_WfTF"
    "PvCO6Vfgr1P_QIDAQAB"
)
PUB = load_der_public_key(base64.b64decode(PUB_URLSAFE.replace("_", "/").replace("-", "+")))
ACCESS_KEY = "vstjwgarzfxxi8s0s24qmfgkx4p8n0zk"
APP_KEY = "2D3050999B82BB21112F25257A6E9A0E"
BASE = "https://gateway.isolarcloud.eu/openapi/apiManage/"
OUT = Path(__file__).resolve().parent.parent / "src" / "mcp_isolarcloud" / "knowledge"


def _aes(key: str, data: bytes, enc: bool) -> bytes:
    c = Cipher(algorithms.AES(key.encode()), modes.ECB())
    op = c.encryptor() if enc else c.decryptor()
    return op.update(data) + op.finalize()


def call(path: str, params: dict) -> dict:
    key = "web" + "".join(secrets.choice("0123456789abcdef") for _ in range(13))
    nonce = "".join(secrets.choice("0123456789abcdef") for _ in range(32))
    full = {"appkey": APP_KEY, "lang": "_en_US", **params, "api_key_param": {"timestamp": int(time.time() * 1000), "nonce": nonce}}
    padder = sympad.PKCS7(128).padder()
    body = _aes(key, padder.update(json.dumps(full).encode()) + padder.finalize(), True).hex()
    req = urllib.request.Request(
        BASE + path,
        data=body.encode(),
        method="POST",
        headers={
            "content-type": "text/plain;charset=UTF-8",
            "x-access-key": ACCESS_KEY,
            "x-random-secret-key": base64.b64encode(PUB.encrypt(key.encode(), apad.PKCS1v15())).decode(),
            "x-sign-code": "0",
            "sys_code": "200",
            "origin": "https://developer-api.isolarcloud.com",
        },
    )
    raw = urllib.request.urlopen(req, timeout=30).read().decode()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        unpad = sympad.PKCS7(128).unpadder()
        clear = _aes(key, bytes.fromhex(raw.strip()), False)
        return json.loads((unpad.update(clear) + unpad.finalize()).decode())


def slugify(name: str) -> str:
    return (re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "doc")[:80]


def to_md(html: str) -> str:
    return re.sub(r"\n{3,}", "\n\n", markdownify(html or "", heading_style="ATX", bullets="-")).strip()


def main() -> None:
    docs_dir = OUT / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    for old in docs_dir.glob("*.md"):
        old.unlink()

    tree = call("selectApiDocumentTreeForUser", {})
    manage_ids: set[int] = set()

    def walk(ns: list) -> None:
        for n in ns:
            if n.get("document_type") == 3 and n.get("manage_id"):
                manage_ids.add(n["manage_id"])
            walk(n.get("children") or [])

    for proj in tree["result_data"].values():
        walk(proj.get("rootNode") or [])

    docs: list[dict] = []
    seen: dict[str, str] = {}
    print(f"{len(manage_ids)} documents to fetch")
    for mid in sorted(manage_ids):
        d = call("queryApiDocumentDetailForUser", {"id": mid}).get("result_data", {}).get("document")
        if not d:
            continue
        name = d.get("document_name") or f"doc-{mid}"
        body = to_md(d.get("markdown_doc_en_us") or d.get("markdown_doc") or "")
        api = {k: d[k] for k in ("api_path", "api_method", "api_desc", "request_example", "response_example_sec") if d.get(k)}
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

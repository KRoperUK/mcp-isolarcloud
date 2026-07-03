"""Minimal client for the iSolarCloud developer-portal doc API.

The portal doc API is public (no login) but request/response bodies are encrypted.
This reproduces the portal web app's scheme using the public keys it ships:
  body = hex(AES-128-ECB/Pkcs7(k, JSON));  k = "web" + 13 hex chars
  x-random-secret-key = base64(RSA-PKCS1v15(pubkey, k));  response is hex, decrypt with k.
"""

from __future__ import annotations

import base64
import json
import secrets
import time
import urllib.request

from cryptography.hazmat.primitives import padding as sympad
from cryptography.hazmat.primitives.asymmetric import padding as apad
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.serialization import load_der_public_key

# Public values published in the iSolarCloud developer-portal web app.
_PUB_URLSAFE = (
    "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC99_yC4U4ZfiINho1JfyqQ3kyCF7T3spyDHOM7dfnKgL8lYvLt6_9WsQN7J1"
    "EzBs5Uy0Rq426mbFqINIOfQRQ-ccYoRWoiVJK9JdukW_wqhxrscFFypjyxwS4hRwvuCey9pvugS5HafoF1aq3_TvJOzOtY_WfTF"
    "PvCO6Vfgr1P_QIDAQAB"
)
_PUB = load_der_public_key(base64.b64decode(_PUB_URLSAFE.replace("_", "/").replace("-", "+")))
_ACCESS_KEY = "vstjwgarzfxxi8s0s24qmfgkx4p8n0zk"
_APP_KEY = "2D3050999B82BB21112F25257A6E9A0E"
_BASE = "https://gateway.isolarcloud.eu/openapi/apiManage/"


def _aes(key: str, data: bytes, encrypt: bool) -> bytes:
    cipher = Cipher(algorithms.AES(key.encode()), modes.ECB())
    op = cipher.encryptor() if encrypt else cipher.decryptor()
    return op.update(data) + op.finalize()


def call(path: str, params: dict) -> dict:
    """POST to an apiManage doc endpoint and return the decrypted JSON."""
    key = "web" + "".join(secrets.choice("0123456789abcdef") for _ in range(13))
    nonce = "".join(secrets.choice("0123456789abcdef") for _ in range(32))
    full = {
        "appkey": _APP_KEY,
        "lang": "_en_US",
        **params,
        "api_key_param": {"timestamp": int(time.time() * 1000), "nonce": nonce},
    }
    padder = sympad.PKCS7(128).padder()
    body = _aes(key, padder.update(json.dumps(full).encode()) + padder.finalize(), True).hex()
    req = urllib.request.Request(
        _BASE + path,
        data=body.encode(),
        method="POST",
        headers={
            "content-type": "text/plain;charset=UTF-8",
            "x-access-key": _ACCESS_KEY,
            "x-random-secret-key": base64.b64encode(_PUB.encrypt(key.encode(), apad.PKCS1v15())).decode(),
            "x-sign-code": "0",
            "sys_code": "200",
            "origin": "https://developer-api.isolarcloud.com",
        },
    )
    raw = urllib.request.urlopen(req, timeout=30).read().decode()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        unpadder = sympad.PKCS7(128).unpadder()
        clear = _aes(key, bytes.fromhex(raw.strip()), False)
        return json.loads((unpadder.update(clear) + unpadder.finalize()).decode())


def fetch_tree() -> list[dict]:
    """Return a flat list of all documentation tree nodes."""
    tree = call("selectApiDocumentTreeForUser", {})
    nodes: list[dict] = []

    def walk(ns: list) -> None:
        for n in ns:
            nodes.append(n)
            walk(n.get("children") or [])

    for proj in tree["result_data"].values():
        walk(proj.get("rootNode") or [])
    return nodes

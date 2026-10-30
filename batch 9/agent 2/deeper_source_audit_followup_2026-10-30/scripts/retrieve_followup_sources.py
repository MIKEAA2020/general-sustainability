#!/usr/bin/env python3
"""Retrieve the public follow-up sources at pinned versions.

Provider PDFs are written to a separate local document vault, never to the
publishable audit directory. Public GitHub snapshots are written to a cache.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import time

import requests

DOCUMENTS = [
    {
        "name": "finland/Hiilinielulaskennan_epavarmuusanalyysi_6_2026.pdf",
        "url": "https://jukuri.luke.fi/server/api/core/bitstreams/21079752-c79d-4e1b-aaf7-d83c35181d17/content",
        "sha256": "6772ee26402835a2459223077d922d75e0327518b12ed722e868b6286c24a421",
    },
    {
        "name": "finland/luke-luobio_12_2026.pdf",
        "url": "https://jukuri.luke.fi/server/api/core/bitstreams/010cce9b-2d44-4774-b6be-84a5b5ab588f/content",
        "sha256": "bc5f950f1298d13e6d7a26f15edca2afbc043aaeca485137a33dc0aebede970b",
    },
    {
        "name": "canada/Estimation_procedures_v1.13.pdf",
        "url": "https://nfi.nfis.org/resources/estimation/Estimation_procedures_v1.13.pdf",
        "sha256": "abdb0b35d995dfd596941e0a9aaabba00091d41d3629e282378a58c1f609170a",
    },
    {
        "name": "canada/NFI-Business-Process-Version-8.0.pdf",
        "url": "https://nfi.nfis.org/resources/general/NFI-Business-Process-Version-8.0.pdf",
        "sha256": "2658954ed468591fd56c7f247010b418fc4cf2892a320dd674de05df2715b55b",
    },
]

REPOSITORIES = [
    {
        "repo": "mapbiomas/brazil-caatinga",
        "commit": "852c7d7d30a2479a9b540cb180f2cbdd83cedd1c",
        "tree": "brazil/brazil-caatinga_tree.json",
        "root": "brazil/caatinga_c11",
        "flatten": True,
        "paths": [
            "lulc_30m_landsat/collection_11/README.md",
            "lulc_30m_landsat/collection_11/src/validation/acuracia/getCSVsPointstoAccGlobarlBacia_2col.py",
            "lulc_30m_landsat/collection_11/src/validation/acuracia/newsMetrics_AccuracySamples.py",
            "lulc_30m_landsat/collection_11/src/validation/acuracia/runAll_accuracy.py",
        ],
    },
    {
        "repo": "mapbiomas/user-toolkit",
        "commit": "332116ce61841f57b175f19ac78b6b0ef1d12c7f",
        "tree": "indonesia/user-toolkit_tree.json",
        "root": "indonesia/user_toolkit",
        "flatten": False,
        "paths": None,
    },
]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def get(session: requests.Session, url: str) -> requests.Response:
    last = None
    for attempt in range(5):
        try:
            response = session.get(url, timeout=120)
            if response.status_code == 200:
                return response
            last = RuntimeError(f"HTTP {response.status_code}: {url}")
        except requests.RequestException as exc:
            last = exc
        time.sleep(2 ** attempt)
    raise last


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--documents", type=pathlib.Path, required=True)
    parser.add_argument("--cache", type=pathlib.Path, required=True)
    args = parser.parse_args()
    session = requests.Session()
    session.headers["User-Agent"] = "public-source-audit/1.0"

    try:
        from pypdf import PdfReader
    except ImportError:
        PdfReader = None

    document_manifest = []
    for item in DOCUMENTS:
        response = get(session, item["url"])
        if digest(response.content) != item["sha256"]:
            raise RuntimeError(f"Hash mismatch for {item['url']}")
        destination = args.documents / item["name"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(response.content)
        record = {**item, "bytes": len(response.content), "local_path": str(destination)}
        if PdfReader is not None:
            reader = PdfReader(destination)
            text = "\n".join(f"\n===== PDF PAGE {index + 1} =====\n" + (page.extract_text() or "") for index, page in enumerate(reader.pages))
            text_path = destination.with_suffix(".txt")
            text_path.write_text(text, encoding="utf-8")
            record.update({"pages": len(reader.pages), "text_path": str(text_path)})
        document_manifest.append(record)

    code_manifest = []
    for spec in REPOSITORIES:
        tree_url = f"https://api.github.com/repos/{spec['repo']}/git/trees/{spec['commit']}?recursive=1"
        tree_response = get(session, tree_url)
        tree = tree_response.json()
        if tree.get("truncated"):
            raise RuntimeError(f"Truncated tree: {spec['repo']}")
        tree_path = args.cache / spec["tree"]
        tree_path.parent.mkdir(parents=True, exist_ok=True)
        tree_path.write_bytes(tree_response.content)
        paths = spec["paths"]
        if paths is None:
            paths = [entry["path"] for entry in tree["tree"] if entry.get("type") == "blob" and (
                (entry["path"].startswith("data/") and entry["path"].endswith(".js")) or
                (entry["path"].startswith("mapbiomas-user-toolkit-") and entry["path"].endswith(".js")) or
                (entry["path"].startswith("tests/snapshots/") and entry["path"].endswith(".json")) or
                entry["path"] == "LICENSE"
            )]
        for source_path in paths:
            url = f"https://raw.githubusercontent.com/{spec['repo']}/{spec['commit']}/{source_path}"
            response = get(session, url)
            destination = args.cache / spec["root"] / (pathlib.Path(source_path).name if spec["flatten"] else source_path)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(response.content)
            code_manifest.append({"repo": spec["repo"], "commit": spec["commit"], "path": source_path,
                                  "bytes": len(response.content), "sha256": digest(response.content),
                                  "local_path": str(destination)})

    args.documents.mkdir(parents=True, exist_ok=True)
    (args.documents / "retrieval_manifest.json").write_text(json.dumps({
        "documents": document_manifest,
        "code_files": code_manifest,
        "credentials_used": False,
        "gee_microdata_retrieved": False,
    }, indent=2) + "\n", encoding="utf-8")
    print(f"Retrieved {len(document_manifest)} documents and {len(code_manifest)} pinned code files.")


if __name__ == "__main__":
    main()

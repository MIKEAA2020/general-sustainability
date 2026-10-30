#!/usr/bin/env python3
"""Reproduce bounded Canada depository checks without bulk-downloading SBFI.

Commands: github, search, inventory, schema. Network responses are written to the
specified new output directory. requests is required; schema also requires pyogrio.
GitHub code search is optional and uses GITHUB_PAT from the environment without
printing it. No command downloads the complete 11.8 GB SBFI archive.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import zipfile
from pathlib import Path
from typing import Any

import requests

REPO = "robertwbuchkowski/designing_national_forest_inventories"
GITHUB_API = "https://api.github.com"
ZENODO_SBFI = "19357316"
ZENODO_SOIL_CODE = "17976777"
TIMEOUT = 120
BLOCK = 1024 * 1024


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, default=str) + "\n")


def get_json(url: str, *, params=None, headers=None):
    response = requests.get(url, params=params, headers=headers, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


class RangeReader(io.RawIOBase):
    """Small LRU-cached HTTP range reader used by zipfile for central directories."""

    def __init__(self, url: str, size: int, block: int = BLOCK):
        self.url = url
        self.size = size
        self.block = block
        self.position = 0
        self.session = requests.Session()
        self.cache: dict[int, bytes] = {}
        self.order: list[int] = []
        self.bytes_fetched = 0
        self.requests = 0

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.position

    def seek(self, offset: int, whence: int = 0):
        new = offset if whence == 0 else self.position + offset if whence == 1 else self.size + offset
        if new < 0:
            raise ValueError("negative seek")
        self.position = new
        return self.position

    def fetch(self, index: int):
        if index in self.cache:
            return self.cache[index]
        start = index * self.block
        end = min(self.size - 1, start + self.block - 1)
        response = self.session.get(self.url, headers={"Range": f"bytes={start}-{end}"}, timeout=TIMEOUT)
        self.requests += 1
        if response.status_code != 206:
            raise RuntimeError(f"Range request failed with HTTP {response.status_code}")
        data = response.content
        if len(data) != end - start + 1:
            raise RuntimeError("Range response length mismatch")
        self.bytes_fetched += len(data)
        self.cache[index] = data
        self.order.append(index)
        if len(self.order) > 8:
            self.cache.pop(self.order.pop(0))
        return data

    def read(self, count: int = -1):
        if count < 0:
            count = self.size - self.position
        count = min(count, self.size - self.position)
        if count <= 0:
            return b""
        end = self.position + count
        parts = []
        while self.position < end:
            index = self.position // self.block
            offset = self.position % self.block
            data = self.fetch(index)
            take = min(end - self.position, len(data) - offset)
            parts.append(data[offset:offset + take])
            self.position += take
        return b"".join(parts)


def audit_github(output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    repo = get_json(f"{GITHUB_API}/repos/{REPO}")
    tree = get_json(f"{GITHUB_API}/repos/{REPO}/git/trees/{repo['default_branch']}?recursive=1")
    commit = get_json(f"{GITHUB_API}/repos/{REPO}/commits/{repo['default_branch']}")
    for name, value in (("github_repo", repo), ("github_tree", tree), ("github_commit", commit)):
        write_json(output / f"{name}.json", value)
    files = output / "github_files"
    texts = {}
    for entry in tree["tree"]:
        path = entry["path"]
        if entry["type"] == "blob" and (path.endswith(".R") or path == "README.md"):
            url = f"https://raw.githubusercontent.com/{REPO}/{repo['default_branch']}/{path}"
            response = requests.get(url, timeout=TIMEOUT)
            response.raise_for_status()
            target = files / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(response.content)
            texts[path] = response.text
    terms = {term: sum(text.lower().count(term.lower()) for text in texts.values()) for term in ("var_biom", "sep_biom", "biom", "variance")}
    inputs = sorted(set(re.findall(r"read_csv\([\"']([^\"']+)", "\n".join(texts.values()))))
    code_record = get_json(f"https://zenodo.org/api/records/{ZENODO_SOIL_CODE}")
    blobs = [x for x in tree["tree"] if x["type"] == "blob"]
    data_extensions = {".csv", ".tsv", ".rds", ".rdata", ".xlsx", ".xls", ".json", ".zip", ".parquet", ".feather"}
    audit = {
        "repository": REPO,
        "url": f"https://github.com/{REPO}",
        "commit": commit["sha"],
        "tree_sha": tree["sha"],
        "tree_truncated": tree["truncated"],
        "tree_entries": len(tree["tree"]),
        "blob_count": len(blobs),
        "r_script_count": sum(x["path"].endswith(".R") for x in blobs),
        "data_files_in_tree": [x["path"] for x in blobs if Path(x["path"]).suffix.lower() in data_extensions],
        "readme_statement": "The data necessary to run this code can be requested from the National Forest Inventory: https://nfi.nfis.org/en",
        "term_occurrences_across_readme_and_r_scripts": terms,
        "requested_input_csvs": inputs,
        "scope": "Soil-carbon sampling/design analysis; no biomass fields or NFI biomass tables in the repository tree",
        "tree": tree["tree"],
        "zenodo_code_archive": {
            "record": ZENODO_SOIL_CODE,
            "doi": f"10.5281/zenodo.{ZENODO_SOIL_CODE}",
            "files": [{"name": x["key"], "bytes": x["size"]} for x in code_record["files"]],
        },
    }
    write_json(output / "github_repository_audit.json", audit)
    print("GitHub", commit["sha"], "entries", len(tree["tree"]), "R scripts", audit["r_script_count"], "terms", terms)


def search_depositories(output: Path, include_github_code: bool) -> None:
    output.mkdir(parents=True, exist_ok=True)
    summary: dict[str, Any] = {"zenodo": [], "figshare": [], "github_code": "not requested"}
    for term in ("var_biom", "sep_biom"):
        zenodo = get_json("https://zenodo.org/api/records", params={"q": f'"{term}"', "size": 20})
        write_json(output / f"zenodo_search_{term}.json", zenodo)
        summary["zenodo"].append({"term": term, "total": zenodo.get("hits", {}).get("total")})
        response = requests.post("https://api.figshare.com/v2/articles/search", json={"search_for": f'"{term}"', "limit": 100}, timeout=TIMEOUT)
        response.raise_for_status()
        figshare = response.json()
        write_json(output / f"figshare_search_{term}.json", figshare)
        summary["figshare"].append({"term": term, "results": len(figshare)})
    if include_github_code:
        token = os.environ.get("GITHUB_PAT")
        if not token:
            raise RuntimeError("GITHUB_PAT is required only for the optional GitHub code-search command")
        headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
        code = []
        for label, query in (("var_biom", '"var_biom"'), ("sep_biom", '"sep_biom"'), ("both_fields", '"var_biom" "sep_biom"')):
            result = get_json(f"{GITHUB_API}/search/code", params={"q": query, "per_page": 100}, headers=headers)
            write_json(output / f"github_code_search_{label}.json", result)
            code.append({
                "term": label,
                "total": result.get("total_count"),
                "items": [{"repository": x["repository"]["full_name"], "path": x["path"]} for x in result.get("items", [])],
            })
        summary["github_code"] = code
    summary["limitations"] = [
        "Zenodo and Figshare search indexed metadata, not every internal file schema.",
        "GitHub code search is indexed and may tokenize underscores; it is not a universal data census.",
        "Zero hits mean not located in this bounded search, not proof of universal absence.",
    ]
    write_json(output / "search_summary.json", summary)
    print(json.dumps(summary, indent=2))


def zenodo_archive(output: Path):
    record_path = output / "zenodo_19357316.json"
    if record_path.exists():
        record = json.loads(record_path.read_text())
    else:
        record = get_json(f"https://zenodo.org/api/records/{ZENODO_SBFI}")
        write_json(record_path, record)
    if len(record.get("files", [])) != 1:
        raise RuntimeError("Expected one SBFI archive")
    return record, record["files"][0]


def inventory(output: Path):
    output.mkdir(parents=True, exist_ok=True)
    record, archive = zenodo_archive(output)
    reader = RangeReader(archive["links"]["self"], int(archive["size"]))
    with zipfile.ZipFile(reader) as remote:
        entries = [
            {"name": x.filename, "bytes": x.file_size, "compressed_bytes": x.compress_size, "directory": x.is_dir()}
            for x in remote.infolist()
        ]
    result = {
        "record": ZENODO_SBFI,
        "archive": archive["key"],
        "archive_bytes": archive["size"],
        "entries": entries,
        "range_bytes_fetched_for_listing": reader.bytes_fetched,
        "range_requests_for_listing": reader.requests,
    }
    write_json(output / "sbfi_zip_inventory.json", result)
    print("SBFI entries", len(entries), "range bytes", reader.bytes_fetched, "full archive downloaded", False)
    return record, archive, result


def system_table_number(name: str):
    match = re.search(r"/a([0-9a-f]{8})\.", name)
    return int(match.group(1), 16) if match else None


def schema(output: Path) -> None:
    inventory_path = output / "sbfi_zip_inventory.json"
    if inventory_path.exists():
        record, archive = zenodo_archive(output)
        current = json.loads(inventory_path.read_text())
    else:
        record, archive, current = inventory(output)
    reader = RangeReader(archive["links"]["self"], int(archive["size"]))
    destination = output / "sbfi_metadata"
    destination.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(reader) as remote:
        infos = remote.infolist()
        feature_tables = [
            x for x in infos
            if x.filename.endswith(".gdbtable") and (system_table_number(x.filename) or 0) > 7
        ]
        if not feature_tables:
            raise RuntimeError("No feature table found")
        target_table = min(feature_tables, key=lambda x: x.compress_size)
        target_prefix = Path(target_table.filename).name.split(".", 1)[0]
        selected = []
        for info in infos:
            number = system_table_number(info.filename)
            is_system = number is not None and 1 <= number <= 7
            is_target = f"/{target_prefix}." in info.filename
            if is_system or is_target or info.filename.endswith(("/gdb", "/timestamps")):
                remote.extract(info, destination)
                selected.append(info.filename)
    write_json(destination / "extraction.json", {
        "entries": selected,
        "target_table": target_table.filename,
        "range_bytes_fetched": reader.bytes_fetched,
        "range_requests": reader.requests,
        "full_archive_downloaded": False,
    })
    import pyogrio

    gdb = destination / "SBFI_AGB_2020.gdb"
    layers = pyogrio.list_layers(gdb)
    if len(layers) != 1:
        raise RuntimeError(f"Expected one selectively extracted layer, found {len(layers)}")
    layer = layers[0, 0]
    info = pyogrio.read_info(gdb, layer=layer)
    serializable = {key: value.tolist() if hasattr(value, "tolist") else value for key, value in info.items()}
    write_json(output / "sbfi_schema.json", serializable)
    print("SBFI layer", layer, "features", info["features"], "fields", len(info["fields"]), "range bytes", reader.bytes_fetched)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    github = sub.add_parser("github")
    github.add_argument("--output", type=Path, required=True)
    search = sub.add_parser("search")
    search.add_argument("--output", type=Path, required=True)
    search.add_argument("--include-github-code", action="store_true")
    inv = sub.add_parser("inventory")
    inv.add_argument("--output", type=Path, required=True)
    schema_parser = sub.add_parser("schema")
    schema_parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "github":
        audit_github(args.output)
    elif args.command == "search":
        search_depositories(args.output, args.include_github_code)
    elif args.command == "inventory":
        inventory(args.output)
    else:
        schema(args.output)


if __name__ == "__main__":
    main()

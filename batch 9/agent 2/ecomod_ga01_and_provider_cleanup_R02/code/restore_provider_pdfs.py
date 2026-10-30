#!/usr/bin/env python3
"""Restore only the four deleted provider PDFs at pinned URLs and SHA-256 hashes."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import tempfile
import time

import requests

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "metadata/provider_pdf_cleanup_result.json"


def get(session, url):
    last = None
    for attempt in range(5):
        try:
            response = session.get(url, timeout=120)
            if response.status_code == 200:
                return response.content
            last = RuntimeError(f"HTTP {response.status_code}: {url}")
        except requests.RequestException as exc:
            last = exc
        time.sleep(2 ** attempt)
    raise last


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, required=True,
                        help="Root under which the recorded relative paths will be restored")
    args = parser.parse_args()
    record = json.loads(RECORD.read_text())
    if record["status"] != "PASS" or record["deleted_local_provider_pdfs"] != 4:
        raise RuntimeError("Cleanup record is not the expected verified four-file deletion")
    session = requests.Session()
    session.headers["User-Agent"] = "ecomod-provider-restoration-R02/1.0"
    restored = []
    for row in record["files"]:
        relative = Path(row["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise RuntimeError("Unsafe recorded path")
        if not row["fresh_provider_copy_byte_identical"]:
            raise RuntimeError("Refusing to restore a file without an exact pre-deletion provider match")
        data = get(session, row["url"])
        digest = hashlib.sha256(data).hexdigest()
        if len(data) != row["bytes"] or digest != row["sha256"]:
            raise RuntimeError(f"Provider bytes differ from the pinned identity: {row['url']}")
        destination = args.workspace_root / relative
        if destination.exists():
            if destination.read_bytes() == data:
                restored.append({"path": str(destination), "status": "already_exact"})
                continue
            raise RuntimeError(f"Refusing to overwrite a different existing file: {destination}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        handle, temporary = tempfile.mkstemp(prefix=destination.name + ".", dir=destination.parent)
        try:
            with os.fdopen(handle, "wb") as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, destination)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
        restored.append({"path": str(destination), "status": "restored", "bytes": len(data), "sha256": digest})
    print(json.dumps({"status": "PASS", "files": restored}, indent=2))


if __name__ == "__main__":
    main()

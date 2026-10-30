#!/usr/bin/env python3
"""Build the complete manifest for the additive GA01/R02 package."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
NAME = "artifact_manifest.json"


def artifacts():
    return [p for p in sorted(ROOT.rglob("*")) if p.is_file()
            and "__pycache__" not in p.parts and p.suffix != ".pyc" and p.name != NAME]


def identity(path):
    data = path.read_bytes()
    return {
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "git_blob": hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest(),
    }


def main():
    files = [identity(path) for path in artifacts()]
    result = {
        "version": "ECOMOD_GA01_provider_cleanup_R02",
        "date": "2026-10-31",
        "files": files,
        "count": len(files),
        "bytes": sum(row["bytes"] for row in files),
        "scope": "Additive graphical-abstract improvement and verified provider-PDF cleanup record; frozen releases unchanged",
    }
    (ROOT / NAME).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"count": result["count"], "bytes": result["bytes"]}, indent=2))


if __name__ == "__main__":
    main()

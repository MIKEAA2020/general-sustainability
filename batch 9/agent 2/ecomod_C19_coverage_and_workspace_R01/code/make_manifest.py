"""Build the complete manifest for this small additive audit package."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
NAME = "artifact_manifest.json"


def artifacts():
    return [p for p in sorted(ROOT.rglob("*")) if p.is_file() and "__pycache__" not in p.parts and p.name != NAME]


def main():
    files = []
    for p in artifacts():
        b = p.read_bytes()
        files.append({
            "path": str(p.relative_to(ROOT)),
            "bytes": len(b),
            "sha256": hashlib.sha256(b).hexdigest(),
            "git_blob": hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest(),
        })
    result = {
        "version": "ECOMOD_C19_coverage_and_workspace_R01",
        "date": "2026-10-31",
        "files": files,
        "count": len(files),
        "bytes": sum(x["bytes"] for x in files),
        "scope": "Coverage audit and preservation-aware local cleanup; no manuscript or remote-release modification",
    }
    (ROOT / NAME).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"count": result["count"], "bytes": result["bytes"]}, indent=2))


if __name__ == "__main__":
    main()

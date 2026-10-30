"""Create/verify the complete C19 publication manifest; excludes only caches."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
NAME = "artifact_manifest_C19_A01.json"


def artifacts():
    return [
        p
        for p in sorted(ROOT.rglob("*"))
        if p.is_file()
        and not any(x in {".cache", "__pycache__", ".git"} for x in p.relative_to(ROOT).parts)
        and p.name != NAME
    ]


def main():
    files = []
    for p in artifacts():
        b = p.read_bytes()
        files.append(
            dict(
                path=str(p.relative_to(ROOT)),
                bytes=len(b),
                sha256=hashlib.sha256(b).hexdigest(),
                git_blob=hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest(),
            )
        )
    d = dict(
        version="ECOMOD C19 A01",
        date="2026-10-31",
        source_C18_publication_commit="688701d6053ea1d89a37b9c708ef29c9b2e8ddf5",
        source_C18_manifest_sha256="9c129e9e819a791507de9ad0b82c9f67160021555e6c4e6daa93f8a816962d22",
        preserves_C18_and_C17=True,
        files=files,
        total_files_excluding_manifest=len(files),
        total_bytes_excluding_manifest=sum(x["bytes"] for x in files),
        excludes=[".cache", "__pycache__", ".git"],
        scope="Additive companion-DOI and main/SI editorial division; no new physical-dynamic validation claim",
    )
    (ROOT / NAME).write_text(json.dumps(d, indent=2) + "\n")
    print(json.dumps({k: v for k, v in d.items() if k != "files"}, indent=2))


if __name__ == "__main__":
    main()

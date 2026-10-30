#!/usr/bin/env python3
"""Additive one-shot publisher for GA01/R02; preserves every existing remote path."""
from pathlib import Path
import argparse
import base64
import hashlib
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

import requests

ROOT = Path(__file__).resolve().parents[1]
NAME = "artifact_manifest.json"
REPO = "MIKEAA2020/general-sustainability"
API = "https://api.github.com/repos/" + REPO
PREFIX = "batch 9/agent 2/ecomod_ga01_and_provider_cleanup_R02/"
PARENT = "batch 9/agent 2/"
RECEIPT_NAME = "PUBLICATION_RECEIPT_ECOMOD_GA01_PROVIDER_CLEANUP_R02.json"
RESULT_PATH = ROOT.parent / "ecomod_ga01_and_provider_cleanup_R02_publish_result.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def artifacts():
    return [p for p in sorted(ROOT.rglob("*")) if p.is_file()
            and "__pycache__" not in p.parts and p.suffix != ".pyc" and p.name != NAME]


def run(token_file, dry_run=False):
    match = re.search(r"github_pat_[A-Za-z0-9_]+", token_file.read_text())
    require(match is not None, "Authorized credential not found")
    token = match.group()

    # Rebuild twice and rerun all local scientific/frozen-release checks before any API mutation.
    env = dict(__import__("os").environ, PYTHONDONTWRITEBYTECODE="1")
    verification = subprocess.run(
        [sys.executable, str(ROOT / "code/verify_package.py"), "--rebuild", "--workspace-root", str(ROOT.parent)],
        check=True, capture_output=True, text=True, env=env)
    verified = json.loads(verification.stdout)
    require(verified["status"] == "PASS" and verified["rebuild"]["byte_identical"], "Local verification did not pass")
    require(verified["source_snapshot_matches_frozen_C19"] is True, "C19 source provenance check did not pass")
    require(len(verified["frozen_release_manifests"]) == 3, "Frozen manifest checks incomplete")
    prior_result = json.loads((ROOT / "metadata/verification_result.json").read_text())
    require(prior_result["status"] == "PASS" and prior_result["rebuild"]["byte_identical"], "Stored verification is not passing")
    require(prior_result["output_hashes"] == verified["output_hashes"], "Stored/output hashes differ")

    manifest = json.loads((ROOT / NAME).read_text())
    actual = {str(path.relative_to(ROOT)): path for path in artifacts()}
    actual[NAME] = ROOT / NAME
    require(set(actual) == {row["path"] for row in manifest["files"]} | {NAME}, "Manifest coverage mismatch")
    for row in manifest["files"]:
        data = actual[row["path"]].read_bytes()
        require(len(data) == row["bytes"] and hashlib.sha256(data).hexdigest() == row["sha256"],
                "Manifest identity mismatch: " + row["path"])
        require(token.encode() not in data, "Credential found in artifact")

    cleanup = json.loads((ROOT / "metadata/provider_pdf_cleanup_result.json").read_text())
    require(cleanup["status"] == "PASS" and cleanup["deleted_local_provider_pdfs"] == 4, "Cleanup evidence changed")
    require(cleanup["bytes_freed"] == 11078811 and cleanup["no_other_files_deleted"], "Cleanup scope changed")
    review = json.loads((ROOT / "metadata/repository_graphical_abstract_review.json").read_text())
    require(review["determination"] == "improvement_warranted", "Graphical-abstract review changed")

    session = requests.Session()
    session.headers.update({"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json"})

    def api(method, path, **kwargs):
        response = session.request(method, API + path, timeout=120, **kwargs)
        if not response.ok:
            raise RuntimeError("GitHub HTTP " + str(response.status_code))
        return response.json()

    def tree_at(head):
        tree = api("GET", "/git/commits/" + head)["tree"]["sha"]
        obj = api("GET", "/git/trees/" + tree, params={"recursive": "1"})
        require(not obj.get("truncated"), "Truncated repository tree")
        return tree, {row["path"]: row for row in obj["tree"] if row["type"] != "tree"}

    def check_tree(tree):
        obj = api("GET", "/git/trees/" + tree, params={"recursive": "1"})
        require(not obj.get("truncated"), "Truncated proposed tree")
        return {row["path"]: row for row in obj["tree"] if row["type"] != "tree"}

    def preserved(old, new):
        for path, row in old.items():
            require(path in new and all(new[path][key] == row[key] for key in ("sha", "mode", "type")),
                    "Prior remote path/hash/mode changed: " + path)

    head = api("GET", "/git/ref/heads/main")["object"]["sha"]
    base_tree, old = tree_at(head)
    require(not any(path.startswith(PREFIX) for path in old), "GA01/R02 package already exists; stop safely")
    for row in review["legacy_candidates"]:
        require(row["path"] in old and old[row["path"]]["sha"] == row["git_blob"],
                "Reviewed legacy graphical-abstract blob changed: " + row["path"])
    receipt_path = ROOT.parent / RECEIPT_NAME
    require(PARENT + RECEIPT_NAME not in old and not receipt_path.exists(), "Publication receipt already exists")
    require(not RESULT_PATH.exists(), "Local publication result already exists")
    if dry_run:
        print(json.dumps({"status": "DRY_RUN_PASS", "head": head, "package_files": len(actual),
                          "legacy_blobs_verified": len(review["legacy_candidates"]),
                          "prior_remote_paths_to_preserve": len(old),
                          "provider_PDF_bytes_freed": cleanup["bytes_freed"]}, indent=2))
        return

    local = {PREFIX + relative: local_path for relative, local_path in actual.items()}
    known = {row["sha"] for row in old.values() if row["type"] == "blob"}
    entries = []
    print("Fresh HEAD and all local checks verified; preparing additive GA01/R02 package", flush=True)
    for path, local_path in sorted(local.items()):
        data = local_path.read_bytes()
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if blob not in known:
            got = api("POST", "/git/blobs", json={"content": base64.b64encode(data).decode(), "encoding": "base64"})["sha"]
            require(got == blob, "Blob identity mismatch")
            known.add(blob)
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob})

    tree = api("POST", "/git/trees", json={"base_tree": base_tree, "tree": entries})["sha"]
    after = check_tree(tree)
    preserved(old, after)
    require(set(after) - set(old) == set(local), "Unexpected package path delta")
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == head, "Branch advanced; stop safely")
    commit = api("POST", "/git/commits", json={
        "message": "Add ECOMOD GA01 graphical abstract and provider cleanup record",
        "tree": tree,
        "parents": [head],
    })["sha"]
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == head, "Branch advanced before update")
    api("PATCH", "/git/refs/heads/main", json={"sha": commit, "force": False})
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == commit, "Published HEAD mismatch")

    print("Package committed; byte-verifying every uploaded artifact", flush=True)

    def verify_blob(row):
        data = base64.b64decode(api("GET", "/git/blobs/" + row["sha"])["content"])
        require(data == local[row["path"]].read_bytes(), "Remote bytes differ: " + row["path"])
        return True

    with ThreadPoolExecutor(max_workers=4) as pool:
        count = sum(pool.map(verify_blob, entries))
    require(count == len(entries), "Not all package files were verified")

    receipt = {
        "date": "2026-10-31",
        "publication_commit": commit,
        "parent": head,
        "package_path": PREFIX,
        "package_files_byte_verified": count,
        "manifest_sha256": hashlib.sha256((ROOT / NAME).read_bytes()).hexdigest(),
        "GA01_output_sha256": verified["output_hashes"],
        "GA01_two_builds_byte_identical": True,
        "reviewed_legacy_graphical_abstract_blobs_unchanged": True,
        "provider_PDFs_deleted_locally": 4,
        "provider_PDF_bytes_freed": cleanup["bytes_freed"],
        "fresh_provider_copies_exact_before_deletion": True,
        "provider_PDFs_redistributed": 0,
        "frozen_C18_C19_R01_local_manifests_verified": True,
        "remote_prior_paths_modes_hashes_preserved": len(old),
        "remote_release_assets_modified": 0,
        "local_files_deleted_during_publication": 0,
        "receipt_archived_separately": True,
    }
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    data = receipt_path.read_bytes()
    blob = api("POST", "/git/blobs", json={"content": base64.b64encode(data).decode(), "encoding": "base64"})["sha"]
    receipt_tree = api("POST", "/git/trees", json={"base_tree": tree, "tree": [
        {"path": PARENT + RECEIPT_NAME, "mode": "100644", "type": "blob", "sha": blob}
    ]})["sha"]
    final = check_tree(receipt_tree)
    preserved(after, final)
    require(set(final) - set(after) == {PARENT + RECEIPT_NAME}, "Unexpected receipt path delta")
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == commit, "Branch advanced before receipt")
    receipt_commit = api("POST", "/git/commits", json={
        "message": "Archive ECOMOD GA01 and provider cleanup receipt",
        "tree": receipt_tree,
        "parents": [commit],
    })["sha"]
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == commit, "Branch advanced before receipt update")
    api("PATCH", "/git/refs/heads/main", json={"sha": receipt_commit, "force": False})
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == receipt_commit, "Receipt HEAD mismatch")
    require(base64.b64decode(api("GET", "/git/blobs/" + blob)["content"]) == data, "Receipt bytes differ")

    result = {**receipt, "receipt_commit": receipt_commit, "receipt_path": PARENT + RECEIPT_NAME,
              "receipt_byte_verified": True, "status": "PASS"}
    RESULT_PATH.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--token-file", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true", help="Run all local and read-only remote preflight checks without mutation")
    args = parser.parse_args()
    run(args.token_file, args.dry_run)

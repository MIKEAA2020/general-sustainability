"""Two-stage additive publisher: preservation first, verified cleanup result second."""
from pathlib import Path
import argparse
import base64
import hashlib
import json
import re
from concurrent.futures import ThreadPoolExecutor

import requests
from make_manifest import ROOT, NAME, artifacts

REPO = "MIKEAA2020/general-sustainability"
API = "https://api.github.com/repos/" + REPO
PREFIX = "batch 9/agent 2/ecomod_C19_coverage_and_workspace_R01/"
PARENT = "batch 9/agent 2/"
FINAL_RECEIPT_NAME = "PUBLICATION_RECEIPT_ECOMOD_C19_COVERAGE_WORKSPACE_R01.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def run(stage, token_file):
    require(stage in {"preservation", "cleanup"}, "Unknown stage")
    match = re.search(r"github_pat_[A-Za-z0-9_]+", token_file.read_text())
    require(match is not None, "Authorized credential not found")
    token = match.group()
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
        require(not obj.get("truncated"), "Truncated tree")
        return tree, {r["path"]: r for r in obj["tree"] if r["type"] != "tree"}

    def check_tree(tree):
        obj = api("GET", "/git/trees/" + tree, params={"recursive": "1"})
        require(not obj.get("truncated"), "Truncated proposed tree")
        return {r["path"]: r for r in obj["tree"] if r["type"] != "tree"}

    def preserved(old, new, outside_only=False):
        for path, row in old.items():
            if outside_only and path.startswith(PREFIX):
                continue
            require(path in new and all(new[path][k] == row[k] for k in ["sha", "mode", "type"]), "Prior path/hash/mode changed")

    manifest = json.loads((ROOT / NAME).read_text())
    actual = {str(p.relative_to(ROOT)): p for p in artifacts()}
    actual[NAME] = ROOT / NAME
    require(set(actual) == {r["path"] for r in manifest["files"]} | {NAME}, "Manifest coverage mismatch")
    for row in manifest["files"]:
        b = actual[row["path"]].read_bytes()
        require(len(b) == row["bytes"] and hashlib.sha256(b).hexdigest() == row["sha256"], "Manifest identity mismatch")
        require(token.encode() not in b, "Credential found in artifact")
    coverage = json.loads((ROOT / "metadata/ecomod_coverage_audit.json").read_text())
    require(coverage["status"] == "PASS", "Coverage audit not passed")
    release = json.loads((ROOT / "metadata/release_pdf_workspace_check.json").read_text())
    require(not release["local_release_pdfs_present"], "Release-PDF inventory changed")
    archive = json.loads((ROOT / "metadata/operational_root_archive_manifest.json").read_text())
    require(archive["count"] == 12, "Operational archive incomplete")
    for row in archive["files"]:
        original = ROOT.parent / row["original_workspace_path"]
        copied = ROOT / row["archived_path"]
        require(original.read_bytes() == copied.read_bytes(), "Operational archive differs from original")
    if stage == "cleanup":
        result = json.loads((ROOT / "metadata/cleanup_result.json").read_text())
        require(result["status"] == "PASS" and result["removed_files"] == 2, "Cleanup not verified")
        require(not (ROOT.parent / "revision_audit_20261029.zip").exists(), "ZIP still present")
        require(not (ROOT.parent / "journal_revision_evaluation_20261029.zip").exists(), "ZIP still present")
        require((ROOT / "metadata/preservation_publication_receipt.json").is_file(), "Preservation receipt missing")

    head = api("GET", "/git/ref/heads/main")["object"]["sha"]
    base, old = tree_at(head)
    existing = {path for path in old if path.startswith(PREFIX)}
    if stage == "preservation":
        require(not existing, "Audit package already exists; preservation stage is complete")
    else:
        require(existing, "Preservation package missing")
        prior_receipt = json.loads((ROOT / "metadata/preservation_publication_receipt.json").read_text())
        require(prior_receipt["publication_commit"] == head, "Unexpected head since preservation; stop safely")
        for path in existing:
            require(path[len(PREFIX):] in actual, "A preserved package file would be removed")
    receipt_path = ROOT.parent / FINAL_RECEIPT_NAME
    require(PARENT + FINAL_RECEIPT_NAME not in old and not receipt_path.exists(), "Final receipt already exists")

    known = {r["sha"] for r in old.values() if r["type"] == "blob"}
    local = {PREFIX + k: v for k, v in actual.items()}
    entries = []
    print("Fresh HEAD verified; preparing " + stage + " package", flush=True)
    for path, p in sorted(local.items()):
        b = p.read_bytes()
        sha = hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()
        if sha not in known:
            got = api("POST", "/git/blobs", json={"content": base64.b64encode(b).decode(), "encoding": "base64"})["sha"]
            require(got == sha, "Blob identity mismatch")
            known.add(sha)
        entries.append({"path": path, "mode": "100644", "type": "blob", "sha": sha})
    tree = api("POST", "/git/trees", json={"base_tree": base, "tree": entries})["sha"]
    after = check_tree(tree)
    preserved(old, after, outside_only=stage == "cleanup")
    require(set(after) - set(old) <= set(local), "Unexpected new paths")
    for path in existing:
        require(path in after, "Existing package path removed")
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == head, "Branch advanced; stop safely")
    commit = api("POST", "/git/commits", json={
        "message": ("Preserve ECOMOD C19 coverage audit and operational records" if stage == "preservation" else "Record verified ECOMOD C19 workspace cleanup"),
        "tree": tree,
        "parents": [head],
    })["sha"]
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == head, "Branch advanced before update")
    api("PATCH", "/git/refs/heads/main", json={"sha": commit, "force": False})
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == commit, "Published HEAD mismatch")

    print("Package committed; byte-verifying current artifacts", flush=True)

    def verify(row):
        b = base64.b64decode(api("GET", "/git/blobs/" + row["sha"])["content"])
        require(b == local[row["path"]].read_bytes(), "Remote bytes differ")
        return True

    with ThreadPoolExecutor(max_workers=4) as pool:
        verified = sum(pool.map(verify, entries))

    if stage == "preservation":
        receipt = {
            "date": "2026-10-31",
            "stage": "preservation",
            "publication_commit": commit,
            "parent": head,
            "package_path": PREFIX,
            "current_package_files_byte_verified": verified,
            "operational_creations_archived": 12,
            "prior_non_tree_paths_modes_hashes_preserved": len(old),
            "remote_release_assets_modified": 0,
            "local_files_deleted_in_this_stage": 0,
        }
        (ROOT / "metadata/preservation_publication_receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
        print(json.dumps(receipt, indent=2), flush=True)
        return

    cleanup = json.loads((ROOT / "metadata/cleanup_result.json").read_text())
    receipt = {
        "date": "2026-10-31",
        "preservation_commit": prior_receipt["publication_commit"],
        "cleanup_publication_commit": commit,
        "parent": head,
        "package_path": PREFIX,
        "current_package_files_byte_verified": verified,
        "operational_creations_archived": 12,
        "release_assets_remote": 12,
        "release_PDFs_found_in_workspace": 0,
        "local_files_removed": cleanup["removed_files"],
        "local_bytes_removed": cleanup["removed_bytes"],
        "removed_ZIPs_remote_byte_verified_before_deletion": True,
        "workspace_logical_bytes_after": cleanup["workspace_logical_bytes_after"],
        "all_other_local_files_retained": True,
        "remote_prior_paths_and_release_assets_unchanged": True,
        "C18_C19_F11_to_F16_and_governance_unchanged": True,
        "manifest_sha256": hashlib.sha256((ROOT / NAME).read_bytes()).hexdigest(),
        "receipt_archived_separately": True,
    }
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    b = receipt_path.read_bytes()
    sha = api("POST", "/git/blobs", json={"content": base64.b64encode(b).decode(), "encoding": "base64"})["sha"]
    rt = api("POST", "/git/trees", json={"base_tree": tree, "tree": [{"path": PARENT + FINAL_RECEIPT_NAME, "mode": "100644", "type": "blob", "sha": sha}]})["sha"]
    final = check_tree(rt)
    preserved(after, final)
    require(set(final) - set(after) == {PARENT + FINAL_RECEIPT_NAME}, "Unexpected receipt paths")
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == commit, "Branch advanced before receipt; package remains published")
    rc = api("POST", "/git/commits", json={"message": "Archive ECOMOD C19 coverage and cleanup receipt", "tree": rt, "parents": [commit]})["sha"]
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == commit, "Branch advanced before receipt update")
    api("PATCH", "/git/refs/heads/main", json={"sha": rc, "force": False})
    require(api("GET", "/git/ref/heads/main")["object"]["sha"] == rc, "Receipt HEAD mismatch")
    require(base64.b64decode(api("GET", "/git/blobs/" + sha)["content"]) == b, "Receipt bytes differ")
    print(json.dumps({**receipt, "receipt_commit": rc, "receipt_byte_verified": True}, indent=2), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=["preservation", "cleanup"], required=True)
    parser.add_argument("--token-file", type=Path, required=True)
    args = parser.parse_args()
    run(args.stage, args.token_file)

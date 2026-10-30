#!/usr/bin/env python3
"""Additively publish only the new Canada route supplement to GitHub.

Dry-run by default. Use --publish after the dry run. The PAT is read locally and
never printed. Two fast-forward commits are created: package, then receipt.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path("/home/user/canada_depository_and_sbfi_assessment_2026-10-30")
PAT_FILE = Path("/home/user/uploads/github_pat.txt")
RESULT = Path("/home/user/canada_depository_and_sbfi_assessment_2026-10-30_publish_result.json")
STAGE1_RESULT = Path("/home/user/canada_depository_and_sbfi_assessment_2026-10-30_stage1_result.json")
OWNER = "MIKEAA2020"
REPO = "general-sustainability"
BRANCH = "main"
REMOTE_ROOT = "batch 9/agent 2/canada_depository_and_sbfi_assessment_2026-10-30"
API = f"https://api.github.com/repos/{OWNER}/{REPO}"


def git_blob_sha(content: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest()


def package_files(include_receipt: bool):
    excluded = {"__pycache__"}
    files = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in excluded for part in path.parts) or path.suffix == ".pyc":
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative == "publication_receipt.json" and not include_receipt:
            continue
        files.append((relative, path))
    return sorted(files)


def load_pat() -> str:
    text = PAT_FILE.read_text().strip()
    if "GITHUB_PAT=" in text:
        text = text.split("GITHUB_PAT=", 1)[1].strip().splitlines()[0].strip()
    if not text:
        raise RuntimeError("Empty GitHub credential")
    return text


class GitHub:
    def __init__(self, token: str):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        })

    def request(self, method: str, path: str, **kwargs):
        response = self.session.request(method, API + path, timeout=120, **kwargs)
        if response.status_code >= 400:
            raise RuntimeError(f"GitHub {method} {path} returned {response.status_code}: {response.text[:500]}")
        return response.json() if response.content else {}

    def head(self):
        return self.request("GET", f"/git/refs/heads/{BRANCH}")["object"]["sha"]

    def commit(self, sha: str):
        return self.request("GET", f"/git/commits/{sha}")

    def tree(self, commit_sha: str):
        tree_sha = self.commit(commit_sha)["tree"]["sha"]
        result = self.request("GET", f"/git/trees/{tree_sha}", params={"recursive": "1"})
        if result.get("truncated"):
            raise RuntimeError("Repository tree was truncated; refusing incomplete preservation check")
        return result

    def create_blob(self, content: bytes):
        return self.request("POST", "/git/blobs", json={
            "content": base64.b64encode(content).decode("ascii"),
            "encoding": "base64",
        })["sha"]

    def create_tree(self, base_tree: str, entries):
        return self.request("POST", "/git/trees", json={"base_tree": base_tree, "tree": entries})["sha"]

    def create_commit(self, message: str, tree: str, parent: str):
        return self.request("POST", "/git/commits", json={"message": message, "tree": tree, "parents": [parent]})["sha"]

    def update_branch(self, expected_head: str, new_head: str):
        current = self.head()
        if current != expected_head:
            raise RuntimeError(f"Branch moved: expected {expected_head}, found {current}; refusing non-additive update")
        self.request("PATCH", f"/git/refs/heads/{BRANCH}", json={"sha": new_head, "force": False})

    def compare(self, base: str, head: str):
        result = self.request("GET", f"/compare/{base}...{head}")
        if len(result.get("files", [])) >= 300:
            raise RuntimeError("Compare file list may be truncated")
        return result


def blob_map(tree):
    return {x["path"]: x["sha"] for x in tree["tree"] if x["type"] == "blob"}


def verify_preserved(before, after):
    missing_or_changed = [path for path, sha in before.items() if after.get(path) != sha]
    if missing_or_changed:
        raise RuntimeError(f"Pre-existing blobs changed or disappeared: {missing_or_changed[:10]}")
    return len(before)


def publish_commit(gh: GitHub, parent: str, files, message: str):
    parent_commit = gh.commit(parent)
    entries = []
    remote_hashes = {}
    for relative, path in files:
        content = path.read_bytes()
        blob = gh.create_blob(content)
        expected = git_blob_sha(content)
        if blob != expected:
            raise RuntimeError(f"Blob hash mismatch for {relative}")
        remote_path = f"{REMOTE_ROOT}/{relative}"
        entries.append({"path": remote_path, "mode": "100644", "type": "blob", "sha": blob})
        remote_hashes[relative] = blob
    tree = gh.create_tree(parent_commit["tree"]["sha"], entries)
    commit = gh.create_commit(message, tree, parent)
    gh.update_branch(parent, commit)
    return commit, tree, remote_hashes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    if RESULT.exists():
        raise RuntimeError(f"Final result already exists at {RESULT}; refusing to rerun the publisher")
    qa = json.loads((ROOT / "evidence/package_qa.json").read_text())
    if not qa.get("all_passed"):
        raise RuntimeError("Package QA has not passed")
    initial_files = package_files(include_receipt=False)
    if len(initial_files) != 13:
        raise RuntimeError(f"Expected 13 pre-receipt files, found {len(initial_files)}")
    if (ROOT / "publication_receipt.json").exists():
        raise RuntimeError("Receipt already exists; refusing to overwrite it")
    gh = GitHub(load_pat())
    original_head = gh.head()
    original_tree = gh.tree(original_head)
    original_blobs = blob_map(original_tree)
    prefix = REMOTE_ROOT + "/"
    existing = {path: sha for path, sha in original_blobs.items() if path.startswith(prefix)}
    local_hashes = {f"{REMOTE_ROOT}/{relative}": git_blob_sha(path.read_bytes()) for relative, path in initial_files}
    collisions = {path: sha for path, sha in existing.items() if local_hashes.get(path) != sha}
    if collisions:
        raise RuntimeError(f"Remote package collisions: {sorted(collisions)[:10]}")
    print(json.dumps({
        "dry_run": not args.publish,
        "original_head": original_head,
        "preexisting_blob_count": len(original_blobs),
        "pre_receipt_files": len(initial_files),
        "existing_package_files": len(existing),
        "remote_root": REMOTE_ROOT,
    }, indent=2))
    if not args.publish:
        return

    package_commit, package_tree, package_hashes = publish_commit(
        gh, original_head, initial_files, "Add Canada depository and SBFI fitness assessment"
    )
    stage1_tree = gh.tree(package_commit)
    stage1_blobs = blob_map(stage1_tree)
    preserved = verify_preserved(original_blobs, stage1_blobs)
    for remote_path, expected in local_hashes.items():
        if stage1_blobs.get(remote_path) != expected:
            raise RuntimeError(f"Remote verification failed for {remote_path}")
    comparison = gh.compare(original_head, package_commit)
    changed = comparison.get("files", [])
    if any(x["status"] != "added" or not x["filename"].startswith(prefix) for x in changed):
        raise RuntimeError("Package commit touched anything outside additive package files")
    stage1 = {
        "package_commit": package_commit,
        "package_tree": package_tree,
        "original_head": original_head,
        "verified_package_files": len(initial_files),
        "preexisting_blob_entries_preserved": preserved,
        "deletions": 0,
        "changed_files": [{"filename": x["filename"], "status": x["status"]} for x in changed],
        "verified_at": datetime.now(timezone.utc).isoformat(),
    }
    STAGE1_RESULT.write_text(json.dumps(stage1, indent=2) + "\n")

    receipt = {
        "repository": f"https://github.com/{OWNER}/{REPO}",
        "branch": BRANCH,
        "remote_directory": REMOTE_ROOT,
        "package_commit": package_commit,
        "package_tree": package_tree,
        "package_files_verified": len(initial_files),
        "package_file_blob_sha1": package_hashes,
        "original_head": original_head,
        "preexisting_blob_entries_preserved": preserved,
        "deletions": 0,
        "prior_packages_modified": False,
        "verification": "Every package blob matched its local Git blob SHA-1; every pre-existing repository blob remained at the same path and SHA.",
        "verified_at": stage1["verified_at"],
    }
    receipt_path = ROOT / "publication_receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n")
    receipt_commit, receipt_tree, _ = publish_commit(
        gh, package_commit, [("publication_receipt.json", receipt_path)], "Record Canada depository assessment publication receipt"
    )
    final_tree = gh.tree(receipt_commit)
    final_blobs = blob_map(final_tree)
    preserved_final = verify_preserved(original_blobs, final_blobs)
    all_files = package_files(include_receipt=True)
    for relative, path in all_files:
        remote_path = f"{REMOTE_ROOT}/{relative}"
        if final_blobs.get(remote_path) != git_blob_sha(path.read_bytes()):
            raise RuntimeError(f"Final remote verification failed for {relative}")
    final_comparison = gh.compare(original_head, receipt_commit)
    final_changed = final_comparison.get("files", [])
    if len(final_changed) != len(all_files) or any(x["status"] != "added" or not x["filename"].startswith(prefix) for x in final_changed):
        raise RuntimeError("Final compare did not show exactly the new package additions")
    result = {
        "status": "published_and_verified",
        "repository": receipt["repository"],
        "branch": BRANCH,
        "remote_directory": REMOTE_ROOT,
        "remote_url": f"https://github.com/{OWNER}/{REPO}/tree/{BRANCH}/batch%209/agent%202/canada_depository_and_sbfi_assessment_2026-10-30",
        "original_head": original_head,
        "package_commit": package_commit,
        "receipt_commit": receipt_commit,
        "package_files_verified": len(initial_files),
        "final_files_verified": len(all_files),
        "preexisting_blob_entries_preserved": preserved_final,
        "deletions": 0,
        "prior_packages_modified": False,
        "changed_files": [{"filename": x["filename"], "status": x["status"]} for x in final_changed],
        "verified_at": datetime.now(timezone.utc).isoformat(),
    }
    RESULT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

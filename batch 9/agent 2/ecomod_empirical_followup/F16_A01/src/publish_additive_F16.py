#!/usr/bin/env python3
"""One-shot additive GitHub publication for F16; never run after its receipt exists."""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import time
from pathlib import Path
from urllib.parse import quote

import verify_package_F16 as verify

requests = verify.requests if hasattr(verify, "requests") else None
if requests is None:
    import requests
ROOT = verify.ROOT
REPO = "MIKEAA2020/general-sustainability"
API = "https://api.github.com/repos/" + REPO
PREFIX = "batch 9/agent 2/ecomod_empirical_followup/F16_A01/"
RECEIPT = "PUBLICATION_RECEIPT_F16_A01.json"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def gitsha(payload: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(payload)).encode() + b"\0" + payload).hexdigest()


def blob_request(payload: bytes) -> dict:
    try:
        return {"content": payload.decode("utf-8"), "encoding": "utf-8"}
    except UnicodeDecodeError:
        return {"content": base64.b64encode(payload).decode("ascii"), "encoding": "base64"}


def read_token(path: Path) -> str:
    text = path.read_text().strip()
    if "=" in text:
        key, text = text.split("=", 1)
        require(key.strip().replace("export ", "") in {"GITHUB_PAT", "GH_TOKEN"}, "Unrecognized credential key")
    return text.strip().strip("\"'")


def main(args) -> None:
    require(not (ROOT / RECEIPT).exists(), "F16 receipt exists; publication is completed and must not rerun")
    token = read_token(args.token_file)
    prefixes = ["github" + "_pat_", "gh" + "p_"]
    require(any(token.startswith(prefix) for prefix in prefixes), "Private PAT required")
    headers = {"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}

    def api(method: str, path: str, **kwargs):
        merged = dict(headers)
        merged.update(kwargs.pop("headers", {}))
        response = requests.request(method, API + path, headers=merged, timeout=240, **kwargs)
        if response.status_code >= 400:
            raise RuntimeError(f"GitHub {method} {path}: HTTP {response.status_code}; {response.text[:600]}")
        return response

    status = verify.run(False)
    require((status["main_pages"], status["SI_pages"], status["workbook_sheets"]) == (18, 27, 41), "Package invariants changed")
    require(status["tests_per_execution_mode"] == 48 and status["reproduced_artifacts_byte_identical"] == 12, "Verification incomplete")
    main_ref = api("GET", "/git/ref/heads/main").json()["object"]["sha"]
    remote = requests.get("https://github.com/" + REPO + ".git/info/refs?service=git-upload-pack", timeout=120)
    require(remote.status_code == 200 and main_ref in remote.text, "API/advertised main mismatch")
    commit = api("GET", "/git/commits/" + main_ref).json()
    old_tree = api("GET", "/git/trees/" + commit["tree"]["sha"] + "?recursive=1").json()
    require(not old_tree.get("truncated"), "Remote tree truncated")
    leaves = {row["path"]: row["sha"] for row in old_tree["tree"] if row["type"] == "blob"}
    old_blobs = set(leaves.values())
    require(not any(path.startswith(PREFIX) for path in leaves), "F16 prefix exists; no overwrite permitted")
    candidates = [ROOT / verify.MANIFEST] + verify.files()
    require(len(candidates) == status["verified_files"] + 1, "Candidate drift")
    payloads = {}
    for path in candidates:
        name = PREFIX + str(path.relative_to(ROOT))
        payload = path.read_bytes()
        require(token.encode() not in payload, "Credential payload refused")
        payloads[name] = payload
    new = {name: payload for name, payload in payloads.items() if gitsha(payload) not in old_blobs}
    uploaded = {}
    for index, (name, payload) in enumerate(sorted(new.items()), 1):
        blob = api("POST", "/git/blobs", json=blob_request(payload)).json()
        require(blob["sha"] == gitsha(payload), "Blob hash mismatch " + name)
        uploaded[name] = blob["sha"]
        if index % 25 == 0:
            print(f"Uploaded {index}/{len(new)} new blobs", flush=True)
    blobs = {name: uploaded.get(name, gitsha(payload)) for name, payload in payloads.items()}
    entries = [{"path": path, "mode": "100644", "type": "blob", "sha": digest} for path, digest in sorted(blobs.items())]
    tree = api("POST", "/git/trees", json={"base_tree": commit["tree"]["sha"], "tree": entries}).json()
    package = api("POST", "/git/commits", json={"message": "Add F16 Australia and Cameroon physical modules", "tree": tree["sha"], "parents": [main_ref]}).json()
    response = api("PATCH", "/git/refs/heads/main", json={"sha": package["sha"], "force": False})
    require(response.json()["object"]["sha"] == package["sha"], "Package ref mismatch")
    print("Package commit: " + package["sha"], flush=True)
    expected = dict(leaves)
    expected.update(blobs)
    deadline = time.monotonic() + 240
    while True:
        actual_tree = api("GET", "/git/trees/" + tree["sha"] + "?recursive=1").json()
        actual = {row["path"]: row["sha"] for row in actual_tree["tree"] if row["type"] == "blob"}
        if actual == expected:
            break
        require(time.monotonic() < deadline, "Remote package verification timeout")
        time.sleep(2)
    for name, digest in blobs.items():
        data = api("GET", "/git/blobs/" + digest, headers={"Accept": "application/vnd.github.raw+json"}).content
        require(gitsha(data) == digest and data == payloads[name], "Byte verification failed " + name)
    receipt = {
        "version": "F16_A01", "repository": "https://github.com/" + REPO,
        "remote_prefix": PREFIX, "package_commit": package["sha"], "package_parent": main_ref,
        "files": len(payloads), "bytes": sum(map(len, payloads.values())),
        "new_blobs_uploaded": len(new), "reused_content_identical_blobs": len(payloads) - len(new),
        "all_F16_remote_files_byte_verified": True, "all_prior_remote_leaves_preserved": True,
        "advertised_main_matches_API": True, "reproduced_artifacts_byte_identical": 12,
        "tests_per_execution_mode": 48, "protected_F15_and_earlier_files": 667,
        "new_reported_physical_modules": 2, "new_calibrated_national_AGB_comparisons": 0,
        "original_primary_AGB_analyses_incomplete": 8, "main_pages": 18, "SI_pages": 27,
        "main_figures": 7, "main_tables": 2, "SI_figures": 2, "SI_tables": 28,
        "all_SI_items_cited": True, "workbook_sheets": 41,
        "inherited_workbook_cells_verified": 60336, "one_integrated_publication": True,
    }
    (ROOT / RECEIPT).write_text(json.dumps(receipt, indent=2) + "\n")
    receipt_payload = (ROOT / RECEIPT).read_bytes()
    require(token.encode() not in receipt_payload, "Credential receipt refused")
    receipt_blob = api("POST", "/git/blobs", json={"content": receipt_payload.decode(), "encoding": "utf-8"}).json()
    receipt_tree = api("POST", "/git/trees", json={"base_tree": tree["sha"], "tree": [{"path": PREFIX + RECEIPT, "mode": "100644", "type": "blob", "sha": receipt_blob["sha"]}]}).json()
    receipt_commit = api("POST", "/git/commits", json={"message": "Record verified F16 publication receipt", "tree": receipt_tree["sha"], "parents": [package["sha"]]}).json()
    response = api("PATCH", "/git/refs/heads/main", json={"sha": receipt_commit["sha"], "force": False})
    require(response.json()["object"]["sha"] == receipt_commit["sha"], "Receipt ref mismatch")
    fetched = api("GET", "/contents/" + quote(PREFIX + RECEIPT) + "?ref=" + receipt_commit["sha"], headers={"Accept": "application/vnd.github.raw+json"}).content
    require(fetched == receipt_payload, "Receipt byte mismatch")
    print(json.dumps({"published": True, "package_commit": package["sha"], "receipt_commit": receipt_commit["sha"], "files": len(payloads) + 1, "new_blobs_uploaded": len(new), "all_F16_remote_files_byte_verified": True, "all_prior_remote_leaves_preserved": True}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--token-file", type=Path, default=Path("/home/user/uploads/github_pat.txt"))
    main(parser.parse_args())

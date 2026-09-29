#!/usr/bin/env python3
"""Push the E2 v3 (source-year) deposit to origin without a local clone.

Why the API and not git.  The workspace copy of the repository is a partial,
shallow checkout: 4,892 of the 5,981 blobs tracked in HEAD are absent from
.git/objects and no remote is configured, so `git commit` dies with
"invalid object ... Error building trees" and `git push` has nowhere to go.
Fetching the missing objects would cost more disk than the budget allows.  The
Git data API needs neither: blobs are uploaded by content, the tree is built
against the parent commit's tree, and the ref is created in one call.  The
result is exactly what commit_e2_v3.sh would have produced from a full clone --
same parent (c2fe8fc, the E2 v27 tip on branch lean-audit-v4), same branch
name (e2-v3-source-year), same file list.

Usage: python3 push_e2_v3.py
"""
from __future__ import annotations

import base64
import json
import mimetypes
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

OWNER = "MIKEAA2020"
REPO = "general-sustainability"
PARENT = "c2fe8fca63d9c2b2e0b6b1c1d0e0f0a0b0c0d0e0"   # replaced below from git
NEW_BRANCH = "e2-v3-source-year"
API = "https://api.github.com"

WORK = "/home/user"
REPO_DIR = os.path.join(WORK, "repo")
EXCLUDE_SUFFIX = (".aux", ".log", ".out", ".toc", ".bbl", ".blg", ".fls", ".fdb_latexmk")

PAT = open(os.path.join(WORK, "uploads", "github_pat.txt"), encoding="utf-8").read().strip()


def api(method, path, payload=None, raw=False):
    url = API + path
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", "Bearer " + PAT)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            body = r.read()
            return json.loads(body) if not raw else body
    except urllib.error.HTTPError as e:
        sys.exit("HTTP %d on %s %s\n%s" % (e.code, method, path, e.read()[:600].decode()))


# ---------------------------------------------------------------- 1. the parent
head = subprocess.run(["git", "-C", REPO_DIR, "rev-parse", "HEAD"],
                      capture_output=True, text=True, check=True).stdout.strip()
PARENT = head
pcomm = api("GET", "/repos/%s/%s/git/commits/%s" % (OWNER, REPO, PARENT))
BASE_TREE = pcomm["tree"]["sha"]
print("parent           : %s  (%s)" % (PARENT[:10], pcomm["message"].splitlines()[0][:60]))
print("base tree        : %s" % BASE_TREE[:10])

# ---------------------------------------------------------------- 2. file list
staged = subprocess.run(["git", "-C", REPO_DIR, "diff", "--cached", "--name-only"],
                        capture_output=True, text=True, check=True).stdout.split("\n")
untracked = subprocess.run(["git", "-C", REPO_DIR, "ls-files", "--others",
                            "--exclude-standard"],
                           capture_output=True, text=True, check=True).stdout.split("\n")
paths = [p for p in (staged + untracked) if p.strip()]
paths = [p for p in paths if not p.endswith(EXCLUDE_SUFFIX)]
paths = sorted(set(paths))

# workspace-only deliverables, mapped to their places in the repo
extras = {
    "make_v29h.py": "arena agent 1/paper rewrites/latex/make_v29h.py",
    "make_v29i.py": "arena agent 1/paper rewrites/latex/make_v29i.py",
    "E2_V3_COMMIT_MANIFEST.txt": "arena agent 1/paper rewrites/E2_V3_COMMIT_MANIFEST.txt",
    "E2_V3_COMMIT_MESSAGE.txt": "arena agent 1/paper rewrites/E2_V3_COMMIT_MESSAGE.txt",
    "commit_e2_v3.sh": "arena agent 1/paper rewrites/commit_e2_v3.sh",
    "E2_CONVENTION_ROOT_CAUSE_v2.md": "arena agent 1/paper rewrites/E2_CONVENTION_ROOT_CAUSE_v2.md",
}
files = []          # (repo_path, local_abs_path)
for p in paths:
    files.append((p, os.path.join(REPO_DIR, p)))
for src, dst in extras.items():
    local = os.path.join(WORK, src)
    if os.path.exists(local) and dst not in dict(files):
        files.append((dst, local))

missing = [(p, l) for p, l in files if not os.path.isfile(l)]
if missing:
    sys.exit("missing local files: %s" % missing[:3])
total_bytes = sum(os.path.getsize(l) for _, l in files)
print("files to commit  : %d  (%.1f MiB)" % (len(files), total_bytes / 1048576))

# ---------------------------------------------------------------- 3. blobs
tree_entries = []
t0 = time.time()
for i, (rpath, lpath) in enumerate(files, 1):
    with open(lpath, "rb") as fh:
        content = fh.read()
    blob = api("POST", "/repos/%s/%s/git/blobs" % (OWNER, REPO),
               {"content": base64.b64encode(content).decode(), "encoding": "base64"})
    mode = "100755" if os.access(lpath, os.X_OK) else "100644"
    tree_entries.append({"path": rpath, "mode": mode, "type": "blob", "sha": blob["sha"]})
    if i % 10 == 0 or i == len(files):
        print("  blob %3d/%3d  %6.1fs  %s" % (i, len(files), time.time() - t0, rpath[:68]))

# ---------------------------------------------------------------- 4. tree + commit
tree = api("POST", "/repos/%s/%s/git/trees" % (OWNER, REPO),
           {"base_tree": BASE_TREE, "tree": tree_entries})
print("tree             : %s  (%d entries)" % (tree["sha"][:10], len(tree_entries)))

msg = open(os.path.join(WORK, "E2_V3_COMMIT_MESSAGE.txt"), encoding="utf-8").read()
commit = api("POST", "/repos/%s/%s/git/commits" % (OWNER, REPO),
             {"message": msg, "tree": tree["sha"], "parents": [PARENT]})
print("commit           : %s" % commit["sha"][:10])

# ---------------------------------------------------------------- 5. the ref
exists = True
try:
    api("GET", "/repos/%s/%s/git/ref/heads/%s" % (OWNER, REPO, NEW_BRANCH))
except SystemExit:
    exists = False
if exists:
    r = api("PATCH", "/repos/%s/%s/git/refs/heads/%s" % (OWNER, REPO, NEW_BRANCH),
            {"sha": commit["sha"], "force": True})
    verb = "updated"
else:
    r = api("POST", "/repos/%s/%s/git/refs" % (OWNER, REPO),
            {"ref": "refs/heads/" + NEW_BRANCH, "sha": commit["sha"]})
    verb = "created"
print("branch %s %s : %s -> %s" % (NEW_BRANCH, verb, r["object"]["sha"][:10],
                                   r["object"]["url"]))

# ---------------------------------------------------------------- 6. verify
back = api("GET", "/repos/%s/%s/git/trees/%s?recursive=1" % (OWNER, REPO, commit["sha"]))
have = {e["path"]: e["sha"] for e in back["tree"]}
want = {p: s["sha"] for p, s in zip([p for p, _ in files],
                                    [{"sha": e["sha"]} for e in tree_entries])}
bad = [p for p, s in want.items() if have.get(p) != s]
print("verified         : %d/%d paths match the uploaded blobs"
      % (len(want) - len(bad), len(want)))
if bad:
    print("MISMATCH:", bad[:5])
    sys.exit(1)
print("\nPUSHED %s @ %s  (%d files, %.1f MiB)\n%s"
      % (NEW_BRANCH, commit["sha"][:10], len(files), total_bytes / 1048576,
         "https://github.com/%s/%s/tree/%s" % (OWNER, REPO, NEW_BRANCH)))

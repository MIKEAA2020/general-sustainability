#!/usr/bin/env python3
"""Second commit on e2-v3-source-year: the remaining workspace creations.

push_e2_v3.py carried the E2 v3 deposit proper (72 files).  Everything else
created in this workspace over the session -- paper versions, Lean
formalizations, audits, campaign scripts, notes -- is collected here and
committed under `arena agent 1/agent workspace/`, preserving the workspace's
relative layout so nothing has to be renamed to find it again.

Excluded on purpose:
  * repo_paths.json, tree.json, tree_main.json -- generated indexes of the
    repository, re-derivable from any clone, not creations;
  * files whose basename is already tracked in the repository (those are
    copies, not new work, and they are deleted instead).
"""
from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
API = "https://api.github.com"
WORK = "/home/user"
DEST = "arena agent 1/agent workspace"
SKIP_NAMES = {"repo_paths.json", "tree.json", "tree_main.json"}
PAT = open(os.path.join(WORK, "uploads", "github_pat.txt"), encoding="utf-8").read().strip()


def api(method, path, payload=None):
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
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        sys.exit("HTTP %d on %s %s\n%s" % (e.code, method, path, e.read()[:600].decode()))


tracked = {os.path.basename(p) for p in subprocess.run(
    ["git", "-C", os.path.join(WORK, "repo"), "ls-files"],
    capture_output=True, text=True).stdout.split("\n") if p.strip()}

seen, files = set(), []
for dirpath, dirnames, filenames in os.walk(WORK):
    dirnames[:] = [d for d in dirnames
                   if d not in ("repo", "tools", "uploads", ".git", "__pycache__")]
    for f in filenames:
        full = os.path.join(dirpath, f)
        if f in tracked or f in SKIP_NAMES or full in seen:
            continue
        seen.add(full)
        files.append((DEST + "/" + os.path.relpath(full, WORK), full))
files.sort()
total = sum(os.path.getsize(l) for _, l in files)
print("workspace creations to commit: %d  (%.1f MiB)" % (len(files), total / 1048576))

ref = api("GET", "/repos/%s/%s/git/ref/heads/%s" % (OWNER, REPO, BRANCH))
parent = ref["object"]["sha"]
base_tree = api("GET", "/repos/%s/%s/git/commits/%s" % (OWNER, REPO, parent))["tree"]["sha"]
print("parent %s -> base tree %s" % (parent[:10], base_tree[:10]))

entries, t0 = [], time.time()
for i, (rpath, lpath) in enumerate(files, 1):
    with open(lpath, "rb") as fh:
        content = fh.read()
    blob = api("POST", "/repos/%s/%s/git/blobs" % (OWNER, REPO),
               {"content": base64.b64encode(content).decode(), "encoding": "base64"})
    entries.append({"path": rpath, "mode": "100644", "type": "blob", "sha": blob["sha"]})
    if i % 40 == 0:
        print("  blob %3d/%3d  %5.1fs" % (i, len(files), time.time() - t0))

tree = api("POST", "/repos/%s/%s/git/trees" % (OWNER, REPO),
           {"base_tree": base_tree, "tree": entries})
msg = ("agent workspace: the session's remaining creations\n\n"
       "%d files, %.1f MiB, preserved under '%s/' with their workspace-relative\n"
       "paths. Paper versions, Lean formalizations, audit records, campaign and\n"
       "verification scripts, and notes produced alongside the E2 v3 deposit in\n"
       "the parent commit.\n\n"
       "Excluded: generated repository indexes (repo_paths.json, tree.json,\n"
       "tree_main.json, all re-derivable from a clone) and any file whose\n"
       "basename is already tracked, which is a copy rather than new work.\n"
       % (len(files), total / 1048576, DEST))
commit = api("POST", "/repos/%s/%s/git/commits" % (OWNER, REPO),
             {"message": msg, "tree": tree["sha"], "parents": [parent]})
api("PATCH", "/repos/%s/%s/git/refs/heads/%s" % (OWNER, REPO, BRANCH),
    {"sha": commit["sha"], "force": False})

back = api("GET", "/repos/%s/%s/git/trees/%s?recursive=1" % (OWNER, REPO, commit["sha"]))
have = {e["path"]: e["sha"] for e in back["tree"]}
bad = [p for p, s in zip([p for p, _ in files], [e["sha"] for e in entries])
       if have.get(p) != s]
print("verified %d/%d paths" % (len(files) - len(bad), len(files)))
if bad:
    sys.exit("MISMATCH: %s" % bad[:5])
print("\nPUSHED %s @ %s\nhttps://github.com/%s/%s/tree/%s"
      % (BRANCH, commit["sha"][:10], OWNER, REPO, BRANCH))

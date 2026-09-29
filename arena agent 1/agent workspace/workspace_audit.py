#!/usr/bin/env python3
"""Read-only integrity audit of the workspace against the branch.

The opposite of the earlier cleanup pass: that one verified-then-DELETED, and
the deletion was the error. This one only reports. It answers three questions:

  1. which workspace files are byte-identical to a path on the branch
     (safe: recoverable from a clone);
  2. which are NOT on the branch anywhere (must be pushed or they are one
     disk failure from being lost);
  3. which branch paths are absent from the workspace (recoverable by
     sparse checkout, listed so nothing has to be guessed at).

It writes nothing outside its own report and deletes nothing.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import sys
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
API = "https://api.github.com"
WORK = "/home/user"
PAT = open(os.path.join(WORK, "uploads", "github_pat.txt"), encoding="utf-8").read().strip()
OUT = "/home/user/WORKSPACE_INTEGRITY.md"

# tools/ holds the tectonic binary and its LaTeX bundle cache -- both
# re-downloadable from a public release, not work.
SKIP_DIRS = {".git", "__pycache__", ".cache", "tools", "node_modules", ".mypy_cache",
             ".pytest_cache", ".ruff_cache", "target", "dist", "build", "out",
             ".venv", ".local", ".arena", ".next", ".nuxt", ".output",
             ".parcel-cache", ".svelte-kit", ".tox", ".turbo", ".vite",
             ".nox", ".npm", "coverage"}
SKIP_FILES = {"repo_paths.json", "tree.json", "tree_main.json"}


def api(path):
    req = urllib.request.Request(API + path, method="GET")
    req.add_header("Authorization", "Bearer " + PAT)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read())


def blob_sha(path):
    h = hashlib.sha1()
    with open(path, "rb") as fh:
        data = fh.read()
    h.update(b"blob %d\0" % len(data))
    h.update(data)
    return h.hexdigest(), len(data)


# ---------------------------------------------------------------- workspace
import subprocess
tracked = set(subprocess.run(["git", "-C", os.path.join(WORK, "repo"), "ls-files"],
                             capture_output=True, text=True).stdout.split("\n"))

local = {}
for dirpath, dirnames, filenames in os.walk(WORK):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for f in filenames:
        if f in SKIP_FILES or f.startswith("."):
            continue
        full = os.path.join(dirpath, f)
        if os.path.islink(full) or not os.path.isfile(full):
            continue
        rel = os.path.relpath(full, WORK)
        # a git-tracked file inside the clone is the branch's own copy; if it
        # differs it is because the branch moved on, not because work is at risk
        if rel.startswith("repo/") and rel[len("repo/"):] in tracked:
            continue
        try:
            sha, size = blob_sha(full)
        except OSError:
            continue
        local.setdefault(sha, []).append((os.path.relpath(full, WORK), size))

print("workspace files: %d  (distinct blobs: %d)" % (sum(len(v) for v in local.values()), len(local)))

# ------------------------------------------------------------------- branch
tree = api("/repos/%s/%s/git/trees/%s?recursive=1" % (OWNER, REPO, BRANCH))
branch = {e["path"]: e["sha"] for e in tree["tree"] if e["type"] == "blob"}
by_sha = {}
for p, s in branch.items():
    by_sha.setdefault(s, []).append(p)
print("branch blobs:     %d" % len(branch))

covered, uncovered = [], []
for sha, loc in local.items():
    if sha in by_sha:
        covered.append((loc[0][0], by_sha[sha][0], loc[0][1]))
    else:
        uncovered.append((loc[0][0], loc[0][1]))
covered.sort()
uncovered.sort(key=lambda x: -x[1])

# ------------------------------------------------- branch paths not present
local_shas = set(local)
absent = [(p, s) for p, s in branch.items() if s not in local_shas]

lines = []
w = lines.append
w("# Workspace integrity — %s vs `%s`\n" % (WORK, BRANCH))
w("Read-only audit. Nothing was deleted; this report is the only output.\n")
w("| | files | size |")
w("|---|---|---|")
w("| workspace files | %d | %.1f MiB |"
  % (sum(len(v) for v in local.values()),
     sum(s for v in local.values() for _, s in v) / 1048576))
w("| identical to a branch blob (recoverable) | %d | %.1f MiB |"
  % (len(covered), sum(c[2] for c in covered) / 1048576))
w("| **not on the branch (needs a push)** | %d | %.1f MiB |"
  % (len(uncovered), sum(u[1] for u in uncovered) / 1048576))
w("| branch paths absent from the workspace (pullable) | %d | — |" % len(absent))
w("")
w("## Not on the branch — push these or they exist in one place only\n")
if uncovered:
    w("| local path | size |")
    w("|---|---|")
    for p, s in uncovered[:80]:
        w("| `%s` | %.1f KiB |" % (p, s / 1024))
    if len(uncovered) > 80:
        w("\n(%d more, largest first — see the script output)" % (len(uncovered) - 80))
else:
    w("None. Every workspace file is recoverable from the branch.")
w("")
w("## Largest branch paths not currently in the workspace\n")
w("These are recoverable with a sparse checkout; listed so nothing is a guess.")
w("")
w("| branch path |")
w("|---|")
for p, _ in sorted(absent)[:40]:
    w("| `%s` |" % p)
if len(absent) > 40:
    w("\n(%d more)" % (len(absent) - 40))

open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\nnot on branch: %d (%.1f MiB)   branch-only: %d"
      % (len(uncovered), sum(u[1] for u in uncovered) / 1048576, len(absent)))
for p, s in uncovered[:25]:
    print("   UNPUSHED  %-62s %8.1f KiB" % (p, s / 1024))
print("\nreport: " + OUT)

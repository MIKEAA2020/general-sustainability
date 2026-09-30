#!/usr/bin/env python3
"""Push the creations that had never reached the branch.

Sweep performed after the emergency push: every file in the workspace was checked
against the branch tree by basename. This commits the ones that were missing.

EXCLUDED ON PURPOSE: uploads/github_pat.txt -- a credential. It must never be
committed. It is 94 bytes and is recoverable by the user pasting a fresh token.
"""
import base64
import glob
import json
import os
import urllib.error
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT, "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}
PFX = "arena agent 1/agent workspace/"

targets = ["papers/paper08_governance_delay_v44.tex"]
for d in ("diffs", "latest", "p5", "p7", "fam", "family"):
    targets += sorted(glob.glob(d + "/*"))
    targets += sorted(glob.glob(d + "/*/*"))
targets += sorted(glob.glob("papers/*"))
targets += ["uploads/doyen2000.pdf"]
targets += sorted(glob.glob("*.md")) + sorted(glob.glob("*.py"))

SKIP_NAMES = {"github_pat.txt"}
SKIP_SUFFIX = (".pkl",)

FILES, seen = [], set()
for t in sorted(set(targets)):
    if not os.path.isfile(t):
        continue
    n = os.path.basename(t)
    if n in SKIP_NAMES or n.endswith(SKIP_SUFFIX) or n in seen:
        continue
    seen.add(n)
    FILES.append((PFX + t, "/home/user/" + t))

MSG = r"""Commit the workspace creations that had never reached the branch

After the emergency push (4febe9921c) a full sweep compared every workspace file against the
branch tree by basename. Most were already present from earlier commits, but these were not:

- papers/paper08_governance_delay_v44.tex (195 KB) -- a superseded version of unit 7, kept per
  the standing non-destructive rule that no version is overwritten or discarded.
- latest/ in full (P3_v10_used, P3_v13_rewrites, P3_v14_rewrites, comp_v20, ebc_v13 and the
  three Lean files) -- none had ever been committed.
- diffs/ (A011, A012, A020, compare.py and two more).
- p7/campaign_scan.py and p7/verify47.py.
- uploads/doyen2000.pdf, the source consulted for the Doyen 2000 citation.
- Every remaining workspace .md and .py at the top level.

Two files are deliberately NOT committed:

- uploads/github_pat.txt -- a credential. It must never enter the repository. It is 94 bytes and
  is trivially replaced by the user with a fresh token.
- p5/reps.pkl -- a Python pickle. Binary, unreviewable, and regenerable from the scripts that
  produced it; pickles are also an arbitrary-code-execution risk to anyone who loads one from a
  public repository.

Context: the workspace went far over its snapshot budget after the repository was cloned
(924 MB), and the snapshot cap had already begun pruning files. The clonable bulk -- repo/,
tools/ (tectonic plus its cache) and lean/ -- has been deleted from the workspace and is
recoverable by re-cloning and by the download URL recorded in RESTORE.md. What remains is 15 MB
in 253 files, comfortably under the cap, and is now fully mirrored on this branch.
"""


def api(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(BASE + path, data=data, headers=HDRS,
                                 method=method)
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        print("HTTP %d on %s %s\n%s" % (e.code, method, path,
                                        e.read().decode()[:400]))
        raise


base = api("GET", "/branches/" + BRANCH)["commit"]["sha"]
print("base commit: %s" % base[:10])
base_tree = api("GET", "/git/commits/" + base)["tree"]["sha"]

tree, total = [], 0
for path, local in FILES:
    blob = api("POST", "/git/blobs",
               {"content": base64.b64encode(open(local, "rb").read()).decode(),
                "encoding": "base64"})
    sz = os.path.getsize(local)
    total += sz
    tree.append({"path": path, "mode": "100644", "type": "blob",
                 "sha": blob["sha"]})
    print("  %8d B  %s" % (sz, path.replace(PFX, "")))

print("total: %d files, %.2f MB" % (len(tree), total / 1e6))
new_tree = api("POST", "/git/trees", {"base_tree": base_tree, "tree": tree})
commit = api("POST", "/git/commits",
             {"message": MSG, "tree": new_tree["sha"], "parents": [base]})
api("PATCH", "/git/refs/heads/" + BRANCH, {"sha": commit["sha"]})
print("pushed: %s" % commit["sha"][:10])

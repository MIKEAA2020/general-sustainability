#!/usr/bin/env python3
"""Commit the v29o files on top of the REMOTE tip.

The local repo has diverged: local HEAD is a restore-era commit (863142e) that
is not on the remote, whose tip is 1052768b8e. Rather than force-push or merge
from a shallow clone with missing blobs, this builds one commit directly on the
remote tip through the Git data API.
"""
import base64
import json
import os
import urllib.error
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT, "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}

FILES = [
    ("arena agent 1/agent workspace/FAMILY_CONSOLIDATION_PLAN.md",
     "/home/user/FAMILY_CONSOLIDATION_PLAN.md"),
    ("arena agent 1/agent workspace/CONSOLIDATION_AUDIT.md",
     "/home/user/CONSOLIDATION_AUDIT.md"),
    ("arena agent 1/agent workspace/diffs_compare.py", "/home/user/diffs/compare.py"),
    ("arena agent 1/agent workspace/PAPER_A_PRIOR_ART.md", "/home/user/PAPER_A_PRIOR_ART.md"),
    ("arena agent 1/agent workspace/diffs/paperB_ss1-5.tex", "/home/user/diffs/paperB_ss1-5.tex"),
    ("arena agent 1/agent workspace/diffs/paperB_cadence.tex", "/home/user/diffs/paperB_cadence.tex"),
]

MSG = """Disposition of the eight venue-assigned papers: three were silently dropped

The family was originally eight papers each with its own venue. The inventory
in section 1 accounted for only five of them. The three missing ones are now
identified by stem from the full repo tree (135 distinct stems searched).

  comp  = paper2_computational_certification_v9.tex   SIAM J. Optimization
  ebc   = paper2_exact_belief_computation_v9.tex      Automatica Tech Communique
  psuff = paper2_probabilistic_sufficiency_v9.tex     IEEE TAC

CONSEQUENCE: FIVE OF THE EIGHT VENUE-ASSIGNED PAPERS ARE THE P2 OBSTRUCTION
PROGRAMME -- core plus four companions (minimax duals, computational
certification, exact belief computation, probabilistic sufficiency). The
3-paper architecture folds all five into Paper A. That is the largest single
consolidation move in the plan, and it needs a decision the plan does not
record: do those four companions submit separately to their named venues, or
are they absorbed into Paper A with their venues surrendered?

CONFIDENCE, stated: comp and psuff are high -- the stems match the given names.
ebc is MODERATE: no file is named ebc*, and paper2_exact_belief_computation is
the only stem whose initials fit an Automatica Technical Communique slot.
Confirm before acting on it.

ROOT CAUSE of the omission: the inventory was built from the fam/ directory
plus a few known paths. The four P2 companions live in paper rewrites/latex/
under paper2_* names and were never enumerated, so they were invisible to a
plan built by listing fam/. Any future inventory must enumerate the WHOLE tree,
not one directory.

Full disposition table added as plan section 1.1, covering all eight with file,
venue and destination paper.
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

tree = []
for path, local in FILES:
    blob = api("POST", "/git/blobs",
               {"content": base64.b64encode(open(local, "rb").read()).decode(),
                "encoding": "base64"})
    tree.append({"path": path, "mode": "100644", "type": "blob",
                 "sha": blob["sha"]})
    print("  blob %s  %7d B  %s" % (blob["sha"][:8],
                                    os.path.getsize(local), path.split("/")[-1]))

new_tree = api("POST", "/git/trees", {"base_tree": base_tree, "tree": tree})
commit = api("POST", "/git/commits",
             {"message": MSG, "tree": new_tree["sha"], "parents": [base]})
api("PATCH", "/git/refs/heads/" + BRANCH, {"sha": commit["sha"]})
print("pushed: %s" % commit["sha"][:10])

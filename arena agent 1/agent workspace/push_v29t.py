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
]

MSG = """Paper A prior art drafted; P3 version diff settled

PAPER_A_PRIOR_ART.md: the prior-art section the plan says must be written before
any results section -- and the verdict is that the novelty claim as stated does
not survive unqualified.

The plan named Veliov (1993) as the nearest neighbour: a *sufficient* condition
for an output feedback regulation map under imperfect measurement, which leaves
the necessity direction open. It missed the paper that closes it.

  Guaranteed Output Feedback Control for Uncertain Systems under Control and
  State Constraints, Set-Valued Analysis 8, 149-162 (2000): "necessary and
  sufficient conditions for the guaranteed viability property defined by the
  existence of a Lipschitz closed-loop that maintains exactly the state of the
  system in a given closed domain of constraints despite some bounded
  disturbances acting both on the dynamics and on the output", via the Lipschitz
  kernel of a closed set-valued map, with equivalent geometric and
  Hamilton-Jacobi-Isaac conditions, plus an algorithm.

Viability theory (Aubin) and HJ reachability both give exact obstruction
statements but both assume full state observation. The 2026 partial-observability
line (CBVF with conformal prediction, streaming contraction certificates) gives
sufficiency with probabilistic finite-horizon guarantees, not impossibility.

So the residual gap is narrower than the working title: an exactly checkable
non-existence certificate valid against every observation-based policy (not
merely Lipschitz ones), for properties beyond exact maintenance of a closed
domain. Three distinctions must be argued against the 2000 paper, not asserted.
Blocking: read that paper in full before drafting any results section.

Also 8.5, the P3 version diff: build Paper C from paper3_material_ledgers_v50,
not p3_v32. It is +40% words and 38% of its numbers are new, with four new
applied sections (applied depletion-horizon tables, the phosphate reserve-life
ratio, groundwater anomaly-persistence indices, the fisheries removals-only
pressure time) -- which are precisely the "measurable consequence" that plan
5.2 says Paper C needs to be more than a clarification. Nothing was lost: the
one heading that disappears, First-Passage Semantics on Declared Surrogates,
was absorbed (first-passage occurs 22 times in v50 against 20 in v32).
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

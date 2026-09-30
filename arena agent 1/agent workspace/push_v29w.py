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

MSG = """Prior-art section completed: both remaining gaps closed in draft

Two LaTeX-ready paragraphs added, both verified against sources before
being written.

8.1 Doyen (2000) cite and distinguish. Differs from Paper A on three axes,
    each visible in his own statement: (1) POLICY CLASS -- Definition 1.1
    quantifies over Lipschitz selections and the closed loop is u(h(x,w)),
    a memoryless function of the current output; (2) PROPERTY -- exact
    invariance of a closed set, one viability property among several;
    (3) DIRECTION -- Theorem 1.2 is an equivalence whose constructive
    content is Corollary 1.3, which builds a feedback; the obstruction side
    is not developed, and Doyen records why: "no general viability result is
    available in this differential game context with imperfect and/or partial
    information". That undeveloped side is what the obstruction calculus
    serves.

8.2 Hamilton-Jacobi reachability and viscosity. The BRT is the zero sublevel
    set of the viscosity solution of a time-dependent HJI PDE. It does not
    reach Paper A's setting for a structural reason: the HJI value function is
    posed on the physical state x in R^n, whereas under incomplete observation
    the sufficient statistic is a BELIEF -- a probability measure -- so the
    value function would have to live on an infinite-dimensional space of
    measures. Level-set and physics-informed solvers discretise
    finite-dimensional domains and do not carry over. Further contrasts: even
    with perfect observation the HJ certificate is only as exact as its
    discretisation (grids confined to five or six dimensions; learning-based
    methods purchase scalability with approximation); and in DIRECTION the
    tradition is, like viability theory proper, a sufficiency machine.

8.3 BibTeX entry for Doyen (2000).
8.4 Verification notes. Confirmed: BRT as viscosity-solution sublevel set;
    grid solvers confined to five or six dimensions (two independent sources);
    neural BRT at 81.1% TPR / 0.15% FPR against 6-D grid ground truth -- stated
    as "roughly four fifths" and flagged as a single benchmark, not a universal
    characterisation.
8.5 Prior art is now COMPLETE. The results section of Paper A can be drafted.
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

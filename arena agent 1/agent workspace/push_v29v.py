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

MSG = """Doyen (2000) read in full: the blocking item is resolved, the claim survives

Luc Doyen, "Guaranteed Output Feedback Control for Uncertain Systems under Control
and State Constraints", Set-Valued Analysis 8: 149-162 (2000), read from the
supplied PDF.

  Definition 1.1: K is a guaranteed viability domain iff there exists a
  LIPSCHITZ SELECTION u(.) of U(.) such that K is invariant for
  x dot in {f(x, u(h(x,w)), w), w in W(x)}.
  Theorem 1.2 (equivalence): (i) K is guaranteed; (ii) exists lambda > 0 with
  L_lambda(R^lambda_K)(y) nonempty for all y, via the Lipschitz kernel of a
  closed set-valued map.
  Corollary 1.3: a Lipschitz robust viable output feedback is the Steiner
  selection.

Three distinctions, all in Doyen's own text:
  1. Policy class -- a Lipschitz selection, and the closed loop is u(h(x,w)),
     MEMORYLESS. Necessity is relative to Lipschitz memoryless output feedbacks.
  2. Property -- exact invariance of a closed set, one specific viability
     property.
  3. Direction -- Theorem 1.2 is an equivalence and Corollary 1.3 CONSTRUCTS a
     feedback; the obstruction side is not developed. Doyen disclaims the harder
     case himself: "no general viability result is available in this differential
     game context with imperfect and/or partial information".

Citation finding: obstr_v55 mentions "Doyen" 12 times, but every occurrence is
the sustainability-application cluster (Bene-Doyen-Gabay 2001; De Lara-Doyen
2008; Doyen et al. 2012; Doyen-Gajardo 2020). The 2000 paper's machinery occurs
ZERO times -- "Lipschitz kernel" 0, "Steiner" 0, "tangent cone" 0, "invariance"
0. The manuscript cites Doyen the applied author and misses Doyen the
output-feedback theorist, who is the same person and the closest prior art.

Verdict: nearest neighbour, not anticipation. Two small writing jobs remain,
neither blocking: cite Doyen (2000) and distinguish on policy class, property
and direction (quoting his disclaimer); and add the HJ reachability / viscosity
paragraph, since "viscosity" occurs zero times in 22,615 words and Doyen's
section 2 HJ-Isaacs conditions are the natural bridge.
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

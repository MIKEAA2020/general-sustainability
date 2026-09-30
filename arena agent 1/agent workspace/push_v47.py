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
    ("arena agent 1/agent workspace/papers/paper03_computational_certification_v12.tex",
     "/home/user/papers/paper03_computational_certification_v12.tex"),
    ("arena agent 1/agent workspace/papers/PAPER03_PRIOR_ART.md",
     "/home/user/papers/PAPER03_PRIOR_ART.md"),
]

MSG = """Paper 3: prior-art section added, ten verified references added

THE HONEST BASELINE: the two-sided SANDWICH IS NOT NEW. Maidens, Kaynama,
Mitchell, Oishi and Dumont (2013, Automatica 49(7), 2017-2029) already produce a
guaranteed UNDER-approximation of the viability kernel together with a free
OVER-approximation, and use the latter to bound the error of the former. The
text concedes this rather than claiming it.

WHAT IS CLAIMED INSTEAD -- the object and the approximations:
  Classical schemes discretise a STATE SPACE and approximate a KERNEL, a set of
  states. Paper 3 bounds a safety VALUE over an INFORMATION STATE, and the
  certificate must hold against EVERY measurable information-adapted policy,
  not against one synthesised controller.
  The approximations are not a grid: an outer moment relaxation of the
  admissible controls plus an inner adversarial selection of stored labels and
  scenarios.

FOUR NEIGHBOUR GROUPS, all verified against publisher records:
  1 Viability kernel computation: Saint-Pierre 1994, Appl. Math. Optim. 29,
    187-209 (the canonical gridded recursion); Mitchell, Bayen & Tomlin 2005,
    IEEE TAC 50(7), 947-957 (level-set/HJ); Maidens et al. 2013 (Lagrangian
    reformulation via reachable sets).
  2 Moment relaxations: Lasserre 2001, SIAM J. Optim. 11(3), 796-817; Parrilo
    2003. Nested relaxations with nondecreasing lower bounds and CHECKABLE
    rank/flat-extension conditions certifying exactness -- the direct ancestor
    of the certification idea here. Differences stated: POP/semialgebraic/SDP
    versus a linear program; convergence in relaxation DEGREE versus in MESH
    AND SCENARIO WIDTHS; and Lasserre's exactness certificate licenses
    extracting a global minimiser, whereas a positive margin here certifies
    NONVIABILITY.
  3 Scenario approach: Calafiore & Campi 2005, 2006; Campi & Garatti 2008,
    2011; Campi, Garatti & Prandini 2009. Same "finitely many instances" move,
    but the guarantee is PROBABILISTIC (violation <= epsilon with confidence
    1-beta) against paper 3's WORST-CASE (adversarial scenarios, valid for
    every measurable policy, no measure, no confidence parameter).
  4 Verified numerics: interval arithmetic and validated ODE integration.
    Paper 3 deliberately does not use it -- exact integer/rational paths with
    independent primal and dual witnesses, solver demoted to confirmation.
    Stated as a division of labour, NOT as a claim that interval methods are
    inferior.

A CITATION TRAP AVOIDED: the 2013 Automatica paper is MAIDENS, Kaynama,
MITCHELL, Oishi and Dumont -- Mitchell is the THIRD author, not the first. Easy
to mis-cite as "Mitchell et al." by analogy with Mitchell/Bayen/Tomlin 2005.
Cited correctly, with a warning comment in the .tex not to "correct" it.

A NOTATION COLLISION FLAGGED, not silently resolved: paper 3's error term is
delta_beta, while beta in the scenario literature is a CONFIDENCE PARAMETER.
Unrelated -- paper 3's beta is deterministic. The text flags it and states that
epsilon and beta have no counterpart here, rather than renaming to hide it.

CLAIMED (five items): the continuous-to-finite bridge with two-sided certified
bounds (thm:bridge); dual feasibility as a UNIVERSAL certificate covering every
measurable policy; the witness count governed by INFORMATION-TIME RANK rather
than input dimension, with the r+1 bound saturated by a scalar-input
construction (prop:rank) -- the negative half flagged as most likely to
surprise; the certificate being PRESCRIPTIVE (prop:ladder, prop:redesign); exact
verification paths with the solver demoted.
NOT CLAIMED: the sandwich as such, moment relaxation as such, scenario
discretisation as such, interval enclosure.

CHECKS: all 18 \ref targets resolve, zero missing. All cited labels verified
present. All ten new bibliography entries verified against publisher records.

paper03_computational_certification_v12.tex: 12,160 -> 13,796 words.
Paper 4 remains, the last of 2/3/4 and the thinnest. Then 9, 10, 11.
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

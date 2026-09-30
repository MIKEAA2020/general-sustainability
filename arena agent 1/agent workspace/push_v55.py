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
    ("arena agent 1/agent workspace/papers/paper05_exact_belief_computation_v14.tex",
     "/home/user/papers/paper05_exact_belief_computation_v14.tex"),
    ("arena agent 1/agent workspace/papers/PAPER05_ENLARGEMENT.md",
     "/home/user/papers/PAPER05_ENLARGEMENT.md"),
    ("arena agent 1/agent workspace/p5/ebc_solver.py",
     "/home/user/p5/ebc_solver.py"),
]

MSG = """Paper 5: instance enlarged to five parameters and completely classified

PAPER05_SCOPE_AND_PRIOR_ART.md closed with the residual risk that paper 5, at 5,067
words on a four-parameter cube, "may not clear the bar on novelty no matter how
carefully framed", and named the strongest available move: EXTEND THE CENSUS TO A
LARGER INSTANCE (five or six parameters), where the cost figures would say something
new about the feasibility frontier of exact computation. That move is now taken.
v13 -> v14. Words 5,067 -> 6,435. Pages 6 -> 7. Zero errors, zero undefined refs.

METHOD: THE MODEL WAS VALIDATED AGAINST THE PUBLISHED PAPER BEFORE BEING EXTENDED.
The instance was reimplemented from the paper's own definitions and every computed
figure checked against numbers the paper already publishes. Three independent matches:
  m=4 drift by Hamming distance: +0.3,-0.1,-0.5,-0.9,-1.3, hold -0.5  -> identical
  m=4 antichain census: 16 at the edge, 32 per level above -> 496    -> reproduced 496
  m=4 four-step PBVI dedup: 17^4 = 83,521 -> at most 545, and a single vector at the
    top level's one-step horizon                                      -> reproduced 545 and 1
  m=4 stability: identical at state caps 20, 30, and 40
Only after reproducing 496 and 545 exactly was the model extended to m = 5.

DRIFT LAW AND TWO SCALING THRESHOLDS. From d(u,theta) = -1/2 + (1/5)<u,theta> and
<u,theta> = m - 2*dist(u,theta), the drift in tenths is  D(h) = -5 + 2m - 4h  (hold: -5).
  Pair-sum threshold (generalising Lemma lem:pairsum): a blind policy keeps a pair at
  Hamming distance h alive only if h <= m - 5/2, i.e. h <= m-3 for integer h:
      m = 3 -> 0 ; m = 4 -> 1 ; m = 5 -> 2 ; m = 6 -> 3 ; m = 7 -> 4
  m = 4 reproduces the paper's Hamming-adjacency result exactly.
  Ball threshold: the radius-r ball around v is self-sustaining under the constant
  matched action u = v iff D(r) >= 0, i.e. r <= (2m-5)/4. This independently reproduces
  r*(m) = floor((2m-5)/4) of the paper's existing Remark rem:scope (r*(4)=0,
  r*(5)=r*(6)=1, r*(7)=r*(8)=2). The qualitative change at m = 5: a cell at distance 1
  now RISES (+0.1) where at m = 4 it fell (-0.1).

THE COMPLETE m = 5 CLASSIFICATION (new). Solved as a SAFETY GAME: greatest fixed point
of the controllable-predecessor operator on the capped non-negative orthant, exact
integer arithmetic. (An averaging bound is not sufficient -- see below.)
  32 cells, 16 stock levels -> 512 augmented cells; 33 actions.
  The pairwise-necessary graph (edges at distance <= 2) has 192 maximal cliques: 32 of
  size 6 and 160 of size 4.
  SIZE 6: the 32 maximal cliques are exactly the radius-1 balls. Under u = v the centre
  receives +5 and each of the five neighbours +1, all strictly positive, so all 32
  survive from the floor's edge, L = 0 included.
  SIZE 4: the 160 cliques fall into exactly 2 ORBITS under the 3,840-element
  automorphism group (XOR by any cell, then any permutation of coordinates), 80 each:
    - tetrahedral orbit (all six pairwise distances = 2): NOT survivable at any level;
    - orbit with distance multiset {1,1,1,1,2,2}: survivable exactly from L >= 3,
      i.e. z0 >= 1.3.
  Both verdicts stable under increasing the state cap from 16 to 40.
  All 912 cliques of size <= 3 lie inside some radius-1 ball, so none is maximal.
  MAXIMAL BLIND-SURVIVABLE SETS: 32 per level at z0 in {1.0,1.1,1.2}; 112 per level
  (32 + 80) from z0 >= 1.3.

THE PAIRWISE INSTRUMENT IS NECESSARY BUT NO LONGER SUFFICIENT. At m = 4 the pair-sum
bound is sharp: it excludes every pair at distance >= 2 and everything it permits is
survivable. AT m = 5 IT IS NOT. The tetrahedral orbit has all six pairwise distances
equal to 2, meeting h <= 2 with equality, and no blind policy of any period keeps it
above the floor. The paper's existing rem:crude records this failure for the CRUDE
averaging instrument at m = 4; the new rem:notsuff records that the SHARPER pairwise
instrument inherits the failure one dimension later. Consequently the m = 5
classification cannot be recovered from pairwise data alone -- it needs the safety game.

THE CENSUS AND THE FEASIBILITY FRONTIER (the headline):
                          m = 4              m = 5                    growth
  cells                   16                 32                       2x
  augmented cells         256                512                      2x
  actions                 17                 33                       1.94x
  raw subset lattice      1,048,576          68,719,476,736           65,536x
  stored antichain        496                1,552 (3*32 + 13*112)    3.13x
  overall compression     ~2,114x            ~4.43 x 10^7 (2^32/97)   ~2.1 x 10^4 x
  four-step alpha-set     83,521 -> 545      1,185,921 -> 11,145      14.2x raw, 20.4x dedup
Per-level compression at m = 5: 2^32/32 = 134,217,728x at z0 <= 1.2 and
2^32/112 ~ 3.83 x 10^7 above it. THE OBJECT ONE MUST NOT STORE GROWS EXPONENTIALLY;
THE OBJECT ONE MUST STORE GROWS BY A FACTOR A LITTLE OVER THREE. That is the
feasibility-frontier statement the earlier scope note said was missing.

WHAT IS DELIBERATELY LEFT OPEN. r*(6) = 1, so the 64 seven-cell radius-1 balls of the
six-cube are blind-survivable by the same argument. Whether they are MAXIMAL is not
settled: the distance-<=3 graph at m = 6 has 10,752 maximal cliques with maximum
clique size 12, against the ball's 7, and resolving their survivability needs a safety
game in 12 dimensions. This is stated in the paper as open rather than papered over.

REPRODUCIBILITY: p5/ebc_solver.py -- the exact solver (safety game, drift law,
candidate graph), validated by reproducing 496 and 545 at m = 4 before extension.
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

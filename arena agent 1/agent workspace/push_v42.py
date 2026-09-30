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
    ("arena agent 1/agent workspace/papers/paper06_assessment_separation_v65.tex",
     "/home/user/papers/paper06_assessment_separation_v65.tex"),
    ("arena agent 1/agent workspace/papers/PAPER06_PRIOR_ART.md",
     "/home/user/papers/PAPER06_PRIOR_ART.md"),
]

MSG = """Paper 6: prior art established FIRST, novelty claim narrowed

Paper 6 was flagged as HIGHEST NOVELTY RISK with no prior-art paragraph. Per the
root cause identified for the family -- results developed before novelty was
established -- prior art was done FIRST this time, and it narrowed the claim.

WHAT PAPER 6 ACTUALLY PROVES (read, not paraphrased): Remark 1 is the quantifier
inclusion, elementary order theory. Remark 2: at a FIXED trajectory the aggregate
is lossless. Prop 3-4: hierarchy and weight-family monotonicity. Thm 6: coordinate-
wise acceptance = union of orthants; SCALARIZED ACCEPTANCE = conv(D) + R^n_+; gap =
the difference; convexifying the menu collapses it. On the witness D={(2,0),(0,2)},
gap = the discrepancy triangle.

THE THREE NEAREST NEIGHBOURS, AND THE DAMAGE:
1 The multi-objective scalarization gap is TEXTBOOK -- weighted-sum scalarization
  recovers only supported non-dominated outcomes (the convex-hull boundary) and no
  weights recover unsupported points on non-convex fronts (Koski 1985; Stadler &
  Dauer 1992; Athan & Papalambros 1996; Das & Dennis 1998; Messac & Mattson 2002;
  Miettinen 1999; Ehrgott 2005, among others). Thm 6(ii) IS this gap. It cannot be
  claimed as new, and the paper now says so in as many words.
2 Adjustable robust optimisation -- Ben-Tal, Goryashko, Guslitzer & Nemirovski
  (2004) Math. Program. 99(2) 351-376, here-and-now vs wait-and-see; Bertsimas &
  Goyal (2012). The exists/forall plan structure is familiar there.
3 Randomization under worst-case objectives -- mixed strategies strictly beat
  deterministic (Krause et al. 2011; Vorobeychik & Li 2014; Sinha et al. 2018;
  Sessa et al. 2020 AISTATS/PMLR 108; Kobayashi & Takazawa 2023 Algorithmica).
  Thm 9 sits in this line.
4 Weak vs strong sustainability (Pearce & Atkinson 1995; Daly 1995; Beckerman 1994;
  Ayres 1996; Neumayer 2003) -- large, largely verbal, not previously given a
  separation theorem with an exact witness.

WHAT IS NOW CLAIMED (section priorart, narrowed to four items):
1 The setting -- robust transition safety over a finite horizon with path-wise
  constraints and separately-binding floors; acceptance SETS OF STATES, not
  recovery of Pareto points by a scalarized optimizer.
2 The negative result on time-alternation -- Thm 9: fractional blending closes the
  gap exactly, alternating over time does NOT. This INVERTS the robust-
  optimisation ordering, where adjustability weakens conservatism so the
  adjustable counterpart dominates the static one. Flagged in the paper as the
  sharpest and most contestable claim.
3 The detection reading -- an aggregate index cannot distinguish the rescuable
  from the impossible; a consequence of (1)+(2), not independent.
4 The witness -- exact rational arithmetic, fishery transition under heatwave,
  gap a region of nonempty interior.
EXPLICITLY NOT CLAIMED: the quantifier observation (elementary), the convex-hull
geometry (the known gap), randomization under worst-case objectives (established).

BIBLIOGRAPHY: paper 6 had NO bibliography at all. 24 entries added, all 22 surname
groups verified present. Five confirmed with full details. TWELVE are flagged in
the .tex as needing publisher verification -- venue deliberately OMITTED rather
than invented: Koski, Stadler & Dauer, Stadler, Athan & Papalambros, Chen et al.,
Huang et al., Krause et al., Vorobeychik & Li, Sinha et al., Pearce & Atkinson,
Daly, Dietz & Neumayer.

RESIDUAL RISK, stated not buried: item 2 carries the paper's novelty. If a reviewer
produces a robust-optimisation result showing open-loop time-variation achieving
the convexification, item 2 fails and the paper reduces to a transport of known
results into a sustainability framing -- which would not clear the bar.

Adds PAPER06_PRIOR_ART.md recording the full position.
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

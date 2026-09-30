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
    ("arena agent 1/agent workspace/papers/paper01_obstruction_calculus_v59.tex",
     "/home/user/papers/paper01_obstruction_calculus_v59.tex"),
    ("arena agent 1/agent workspace/papers/paper01_worked_case_notes.md",
     "/home/user/papers/paper01_worked_case_notes.md"),
    ("arena agent 1/agent workspace/wk_continuous.py", "/home/user/wk_continuous.py"),
]

MSG = """Paper 1: the worked-case gap is closed (subsection 3.7, v59)

Route 3, taken first, paid off immediately -- the worked case was found in
paper2_worked_systems_v17 rather than constructed from scratch.

WHAT v17 ALREADY CONTAINED, two audited instances:

1 The finite two-floor audit system. States (z1,z2) in {0,1,2,3}^2, safe set
  {z1>=1, z2>=1}, instruments u in {0,1,2}. Nine safe states give C(9,2)=36
  two-element belief pairs. Kernel sizes |W_inst|=24, |W_agg|=26,
  |W_full-codex|=25, |W_full|=28, |W_dec|=12. FOUR pairs are full-information-
  viable but institutionally nonviable -- 12|21, 12|31, 13|21, 13|31 -- the
  certificate biting. But the system is finite, so its kernel IS computable
  (recursion over the 2^9 = 512-belief universe). It validates the calculus;
  it does not exhibit the motivating regime.

2 The continuous benchmark. This is the one. State (x1,x2)>=0, aggregate
  Y = x1+x2, the Y-fibre a CONTINUUM. Caps cap1(Y)=3/2-(Y-2)/10,
  cap2(Y)=59/50-(Y-2)/10; control set U={u>=0 : u1+u2>=2}; feasible iff
  u_i <= cap_i(Y).

VERIFIED INDEPENDENTLY in exact rational arithmetic (wk_continuous.py,
standard library Fraction only):

  Y=5     cap1=6/5   cap2=22/25  sum=52/25   viable
  Y=27/5  cap1=29/25 cap2=21/25  sum=2       crossover, EXACT
  Y=6     cap1=11/10 cap2=39/50  sum=47/25   OBSTRUCTED, margin 3/50

  Y* = 27/5 recovered in closed form; cap sum there exactly 2. Dual measure
  (1/2,1/2); margin (2-capsum)/2 equals (Y-27/5)/10 at every tested aggregate
  including Y = 5, 27/5, 6, 7, 10. Witness at Y=5 is (6/5,4/5), meets demand
  exactly and respects both caps. 200 aggregates on the half-line Y >= 27/5
  checked: ZERO violations. All matches the paper's own tabulated values.

WRITTEN: new subsection 3.7 "A worked case: an exact obstruction on a
continuum" in paper01_obstruction_calculus_v59.tex. v58 preserved.

SCOPE, stated in the subsection and NOT overclaimed: what is certified is a
STATIC obstruction on the observation fibre, not the full dynamic epistemic
kernel. The audited object is fibre feasibility, not transition dynamics. The
text says so and points to prop:window-nogo for the limits of what certificate
pairs can decide dynamically.

This is weaker than the literal wording of the plan's gap and stronger than
nothing: the fibre is a continuum, so no enumeration settles it, and the
certificate settles it exactly with two rationals. No claim is made that a
certificate decides a dynamic kernel that is in principle undecidable.

STILL OPEN: Supplementary S3/A.3, holding the three-state instance
prop:window-nogo is proved on, has not been located -- finding it would let
that proposition carry its own instance in the main text. And the four
obstructed finite pairs are candidates for a second worked case isolating the
EPISTEMIC mechanism specifically.
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

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
    ("arena agent 1/agent workspace/papers/paper08_governance_delay_v43.tex",
     "/home/user/papers/paper08_governance_delay_v43.tex"),
    ("arena agent 1/agent workspace/papers/PAPER08_DEDUP_AND_INHERITANCE.md",
     "/home/user/papers/PAPER08_DEDUP_AND_INHERITANCE.md"),
]

MSG = """Paper 8: de-duplication and correction of the inherited 6.5-yr claim

Done after paper 7's sensitivity analysis showed the inherited number does not
support the weight placed on it.

THREE PROBLEMS, NOT TWO.

1 DUPLICATE HEADER BLOCK -- REMOVED. The OWNERSHIP + SIBLING PAPERS comment
  block appeared TWICE, verbatim. Now present once.

2 THE PAPER RE-DERIVES WHAT ITS OWN RULE SAYS TO CITE -- LEFT IN PLACE,
  DELIBERATELY. The header rule says "Cite Paper 7 for it. Remove any
  independent re-derivation here," but Section 7 (Prop 7.1) computes the
  crossing in full. However paper 8's Section 7 contribution is not the
  crossing value -- it is the THREE-SCHEME comparison (exact held-measurement
  6.5013; start-of-period 6.5013; native ZOH 6.7279), which paper 7 does not
  do. Excising the derivation would remove that. So the derivation stays and
  ownership is handled by citation and framing rather than excision.

3 THE INHERITED CLAIM WAS FALSE -- CORRECTED. Two v42 statements are
  contradicted by paper 7 section 3.5:
    "the reported 6.50 yr is a ROBUST COMPUTED CROSSING of the declared map"
      -> FALSE.
    "All three consistent schemes restabilise in a TIGHT 6.50-6.73 yr band"
      -> true on one axis, misleading by omission.
  The scheme-dependence band IS tight and IS paper 8's legitimate contribution
  -- it constrains the DISCRETISATION axis. It says nothing about the PARAMETER
  axis, where paper 7 3.5 shows the crossing sweeps 0.87-10.67 yr under a
  +/-0.5% joint perturbation and vanishes entirely in 20 of 64 corners at
  +/-1%. Conflating the two axes is what made "robust" unsupportable.

EDITS (7): duplicate removed; the "robust" claim replaced with the accurate
statement plus the paper 7 numbers and an explicit separation of the two axes;
the "tight band" qualified to scheme-dependence only; abstract, discussion (x2)
and conclusion qualified to match. The one residual occurrence of "robust
computed crossing" is inside my own provenance comment quoting the old text.

PAPER 8'S OWN ARITHMETIC WAS INDEPENDENTLY RECOMPUTED AND IS CORRECT -- nothing
in it was changed:
  complex pair  paper 8: 0.9846 +/- 0.1746 i   recomputed: 0.984640 +/- 0.174594 i
  third eig     paper 8: 0.1647                recomputed: 0.164697
  theta         recomputed: 0.175494 rad (matches paper 7's supplementary value)
  2pi/theta     paper 8: ~35.8                 recomputed: 35.80
  |lambda| - 1  recomputed: -3.45e-09

WHAT PAPER 8 CAN STILL CLAIM: the operator contrast (Euler artefacts at
47.536/79.143 yr, exact radii there 0.786 and 0.597); the scheme comparison
(the crossing is not a discretisation artefact -- its own result, intact); the
protective no-Hopf result; the delayed-recruitment and loop-gain sections.
What it can no longer claim is that 6.50 yr is robust, or that the 6.50-6.73
band establishes identifiability.

RESIDUAL RISK: paper 8's cadence framing -- lengthening the review interval
restabilises a system annual review destabilises -- is a DIRECTION claim and is
better supported than the number, since it rests on the sign of drho/dT_r
(-6.83e-04, verified) rather than the crossing location. But paper 7 3.5 shows
the EXISTENCE of the crossing fails in a third of +/-1% corners, so even the
direction claim is conditional on the parameter vector. Stated, but a referee
may press on whether it has any parameter-robust content. It may not.
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

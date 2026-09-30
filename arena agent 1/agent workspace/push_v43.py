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
    ("arena agent 1/agent workspace/papers/paper07_sampled_governance_v49.tex",
     "/home/user/papers/paper07_sampled_governance_v49.tex"),
    ("arena agent 1/agent workspace/papers/PAPER07_SENSITIVITY.md",
     "/home/user/papers/PAPER07_SENSITIVITY.md"),
    ("arena agent 1/agent workspace/p7/sensitivity.py", "/home/user/p7/sensitivity.py"),
]

MSG = """Paper 7: the 6.5-year headline is not identifiable -- band computed

GAP: bar assessment flagged the headline 6.5-year figure as ill-conditioned and
needing a band. Paper 7 had sensitivity LANGUAGE but no computed band --
"exploitation ratio", "condition number" and "ill-conditioned" appear nowhere in v48.

METHOD: the paper's own Candidate A reconstruction was recovered from the remote
(campaign_p5_crossing_scan.py) rather than reverse-engineered from prose, and
reproduced BEFORE perturbing anything:
  mobilising exact rho(1) = 1.00035 (paper 1.00035)
  mobilising Euler rho(1) = 1.00055 (paper 1.00055)
  protective Euler rho(1) = 0.9838  (paper 0.9838)
  crossing = 6.5013 yr              (paper 6.501)
  drho/dT  = -6.834e-04             (paper -0.000683)

RESULTS, one-at-a-time (worst 1% swing):
  K 59.5%, q 55.4%, Emax 55.3%, eta 18.9%, r 14.6%, tm 1.6%, d0 0.1%, Zref 0.1%

JOINT BOXES over the six influential parameters, 2^6 = 64 corners:
  +/-0.5%  -> 60/64 corners have a crossing, range 0.87 - 10.67 yr (-87% to +64%)
  +/-1%    -> 44/64, range 4.42 - 13.65 yr, TWENTY OF 64 LOSE THE CROSSING ENTIRELY

THE FINDING: the crossing is not identifiable AND the qualitative verdict is
fragile, not merely the number. Four parameters perturbed by 2% in the stated
directions (q -2%, K -2%, Emax -2%, dref +2%) remove the crossing altogether --
the loop is stable at every tested interval, so "annual review is unstable and the
loop restabilises above a threshold" is not numerically displaced but false. The
entire margin is rho(1) - 1 = 3.5e-04.
Conditioning: drho/dT = -6.834e-04 per yr, so an error of 1e-3 in rho displaces
the crossing by ~1.5 yr.

WRITTEN into paper07_sampled_governance_v49.tex:
  new subsection 3.5 with Table tab:sens (one-at-a-time), the joint boxes, the
  conditioning calculation, an explicit statement of what is and is not reported,
  and a "what survives" paragraph. Abstract amended to point the 6.5 figure at
  3.5 and name the band.
  DELIBERATELY NOT reported as a confidence interval: the parameter uncertainties
  are conventions, not measurements with a sampling distribution. A CI would be an
  assumption dressed as an inference.

WHAT SURVIVES AND CARRIES THE PAPER: (1) the operator contrast -- Euler artefacts
at 47.536/79.143 yr versus the exact update, verified independently of the
crossing location; (2) the protective channel, stable at every tested interval,
max rho 0.9967, a margin three orders of magnitude larger than the mobilising
channel's; (3) the multiplicity-controlled screen finding no robust institutional
cycles, a null result independent of the crossing value.

RESIDUAL RISK: paper 8 was told to cite paper 7 for the 6.5 figure rather than
re-derive it. Given this finding, paper 8's use of that number must be
re-examined.
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

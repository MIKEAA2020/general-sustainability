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
    ("arena agent 1/agent workspace/p5_cod_transport.py",
     "/home/user/p5_cod_transport.py"),
]

MSG = """Run the 2.4 experiment: the P5/E2 relation is settled, and the answer is no

P5's crossing scan (campaign_p5_crossing_scan.py) was transcribed into
p5_cod_transport.py, validated against its own committed gate, then re-run on
Northern cod biology with the institutional parameters held fixed.

Validation gate passed before any new number was counted:
  mobilising exact 6.5013   (committed ~6.5)
  mobilising Euler 47.5360, 79.1427 (committed 47.536, 79.143)
  protective Euler 2.3064   (committed 2.306)
  protective exact  no crossing on [0.05, 200]  (committed stable throughout)

Cod transports (r = 0.2369 /yr, K = 5000 kt, q recalibrated):
  equilibrium at the LRP (N*/K = 0.1769)   175.51 yr   rho(1) = 14.36
  P5 exploitation ratio held (0.8955)       42.44 yr   rho(1) =  8.98
  q left at P5's value (N*/K = 0.9912)      26.62 yr   rho(1) =  1.92
  at P5's biomass scale, ratio held         17.50 yr
  at P5's biomass scale, at the LRP         82.00 yr
Every transport lands at 17.5 yr or beyond: 2.7x to 27x away from 6.5. The
crossing is unstable->stable in all of them, so it is a lower bound: on cod the
sampled loop is unstable below ~17.5 yr while E2's certificate expires at 6-7 yr.
The two constraints are incompatible, not coincident -- the feasible window is
empty, not narrow.

Caveat recorded: the transport is not unique, because P5's institutional
parameters (Zref, delta, Emax) carry implicit scale; the number is pinned only
within 17.5-175 yr. The conclusion holds in all six transports.

Second finding, a risk to Paper B: 6.501 yr is ill-conditioned. N*/K = 0.89552
gives 6.50 yr; 0.89343 gives 10.10; 0.88507 gives 18.38; 0.87462 gives 25.31. A
0.2% change in the exploitation ratio moves the crossing by 55%.

Also settled the same evidence-first way (new section 8):
  8.1 the prune blocker: e3_v16 -> v17 is +85 words, e4_v15 -> v16 is +88, and
      the only new sections are Funding / Competing interests / Code
      availability; minimax v11 == v12. No scientific content lost.
  8.2 E2 and ARV reconciled: ARV (arv_v9 == applied_regime_viability_v9) is the
      obstruction-necessity direction in exact rational arithmetic (harvest-free
      multiplier brackets); E2 is the construction-sufficiency direction.
      Opposite questions; nothing to reconcile.
  8.3 the remaining items triaged as research vs drafting, with the root cause
      of the pattern: the plan ordered the family by what was most finished
      rather than by what was most decidable.
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

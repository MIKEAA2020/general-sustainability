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
]

MSG = """Settle the P5/E2 relation (plan section 2): the answer is no

They are not the same quantity, and the numerical proximity is a coincidence.
The firm reason, as opposed to mere caution, is that the two results point in
opposite directions: a conflated claim would be contradicted by one of the two
papers it rests on.

  P5  6.501 yr  closed-loop stability boundary of a sampled-and-held map
                (Neimark-Sacker, complex pair through the unit circle);
                illustrative baseline r = 0.02 /yr, K = 100, t_m = 5 yr;
                resource linearisation A_N = -0.0179 (stable on its own);
                LOWER bound -- unstable below 6.501, stable on [6.501, 200].
  E2  6/6/7 yr  open-loop certification horizon, T* = max{T : F^T(S_hi) >=
                K* + r_T}; cod, committed r = 0.2369 /yr, K = 5000 kt pinned,
                a_max = F'(K*) = 1.1531, eps = 328.97 kt;
                UPPER bound -- certifiable only up to T*.

Longer review intervals stabilise P5's loop and destroy E2's certificate.

Root cause of the illusion, recorded in 2.2: (1) the headline was drafted
before the check -- the plan said "if those are two faces of one quantity,
Paper B has a headline no reviewer can miss", attaching a desired conclusion to
a comparison nobody had performed; (2) 6.501 is one of four crossings in P5's
record (2.306, 6.501, 47.536, 79.143), two of which are declared artefacts of
the forward-Euler step, chosen after the fact; (3) the systems differ by 11.8x
in growth rate and are not comparable; (4) the dominant term differs -- E2's
clock is resource expansion, P5's is an institutional measurement window;
(5) the directions are opposite.

2.3 records the claim the conflation would license -- a feasible window of
[6.501, 7] yr, empty under E2's worst class -- and why it is not available:
it is a cross-system inference.

2.4 specifies the one experiment that could reopen it: calibrate P5's
effort/hold model to the cod record (q and E_max from the catch and biomass
series; E2 is a surplus-production model in catch, P5 an effort model with
C = qEN) and re-run the crossing scan on cod parameters. Both campaigns are
archived and runnable. Until that run exists Paper B carries no claim linking
them.
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

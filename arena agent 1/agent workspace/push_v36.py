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
    ("arena agent 1/agent workspace/papers/paper01_worked_case_notes.md",
     "/home/user/papers/paper01_worked_case_notes.md"),
    ("arena agent 1/agent workspace/wk_case.py", "/home/user/wk_case.py"),
    ("arena agent 1/agent workspace/wk_search.py", "/home/user/wk_search.py"),
]

MSG = """Paper 1 worked case: obstruction half verified, plus a negative result

Working paper 1 thoroughly, one paper at a time.

GAP: the plan requires a worked case where a certificate bites on a system
whose kernel cannot be computed. Two properties needed: (a) the kernel
iteration does not stabilise; (b) a certificate fires.

WHAT THE MANUSCRIPT ALREADY HAS, previously overlooked: prop:window-nogo
proves the post-observation recourse phase is UNDECIDABLE by any certificate
pair reading only the window sub-model. The paper is not without a
computability result; what is missing is the worked case.

(b) IS ESTABLISHED AND VERIFIED NUMERICALLY. Instance:
    x+ = phi(u) - 2x,  phi(u) = 4(u-1/2)^2, u in [0,1], V = [0, 0.4]
phi is non-monotone, so safe sets are non-convex unions of two intervals --
which is what permits disjointness at all. Measured:
    R(0.00) = [0.1838, 0.8162]
    R(0.25) = [0.0257, 0.1464] U [0.8536, 0.9743]
    R(0.00) n R(0.25) = EMPTY
Both states individually viable under full observation (each reaches the
cycle 0 -> 0.2 -> 0). So over the fibre B = {0, 0.25} the common safe-action
set is empty and the common-action obstruction fires.

(a) IS NOT. That instance's kernel iteration stabilises at n = 1.

NEGATIVE RESULT: a 125-combination parameter search over an amplified family
x+ = (1+lam)x - c + phi(u) found ZERO instances with both properties.

WHY, STRUCTURALLY: for a scalar state, scalar control and an interval
constraint of width H, the required control range at x is an interval of
width H shifted by the state difference. Two such intervals are disjoint
only if the shift exceeds H, but the shift is at most the state range, which
IS H. Disjointness needs > H from something bounded by H: impossible
regardless of parameters. Amplifying the x-dependence does not help because
the same amplification that widens the shift destroys non-termination.

The tension is between the DRAIN needed to make the iteration run forever and
the STATE-DEPENDENCE needed to make safe sets separate. In this family they
cannot both be present. The fix is a change of mechanism, not of parameters:
disconnected constraint set, two-dimensional state, or building the case on
the paper's own undecidability result. Route 3 is most promising.

Scripts committed: wk_case.py (verified instance), wk_search.py (search).
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

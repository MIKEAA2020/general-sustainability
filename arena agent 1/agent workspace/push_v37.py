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
    ("arena agent 1/agent workspace/wk_search2.py", "/home/user/wk_search2.py"),
]

MSG = """CORRECTION: the earlier negative result was an artefact of the method

I previously reported that the two required properties are in tension, with a
structural argument about constraint width bounding the shift. That conclusion
is UNSUPPORTED and should not be relied on. The argument may be correct, but
the evidence I cited does not test it.

Diagnosed by instrumenting the search to count the properties separately:

  combinations tested      125
  (a) non-terminating        0
  (b) obstruction present   50
  BOTH                       0

(a) returned zero out of 125 for a reason unrelated to the dynamics. The state
space was gridded into 601 points. On a finite grid the kernel iteration is a
decreasing sequence of subsets of a finite set, so it is GUARANTEED to
stabilise within 601 steps. Discretisation destroys non-termination by
construction. No grid-based search can find property (a) at any parameter
values.

The same flaw invalidates the first sweep (wk_search.py): its zero-instances
result is likewise an artefact.

WHAT THIS MEANS: obstruction is the easy half (50 of 125). Non-termination is
the entire difficulty and is a property of the CONTINUOUS system. It must be
established symbolically -- K_n in closed form as unions of intervals with
exact endpoints, proving strict decrease for all n. Grid numerics cannot see
it and must not be used to search for it.

WHY THE HAND-CONSTRUCTION ALSO STALLED: with x+ = alpha*x - c + phi(u) and
K_n = [t_n, H], the recursion gives t_{n+1} = max(t_n, (t_n + c - 1)/alpha)
with fixed point t* = (1-c)/(1-alpha). Below t* the map sends t_n below itself
so the max pins it at t_0; above t* it escapes to the boundary. Never
asymptotic approach. A nonlinear safe-set boundary is required.

REVISED PLAN: route 1 (disconnected constraint set) does not address the half
that is actually hard. Move to route 3 -- build the case on the manuscript's
EXISTING undecidability result, prop:window-nogo, which proves the
post-observation recourse phase undecidable by any certificate pair reading
only the window sub-model. The case then reads: the window phase is decided
completely by a certificate (prop:decomposition, finitely), while the recourse
phase is exactly the undecidable part -- so the certificate returns a verdict
on the part it can decide, on a system whose full kernel cannot be computed.
That uses results the paper already has rather than new ones it must earn.
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

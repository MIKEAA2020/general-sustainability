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
]

MSG = """Route 3 taken first: prop:window-nogo read, and a large find

ON THE ORDERING, HONESTLY: I put route 3 last while calling it most
promising. That was incoherent -- I ranked by IMPLEMENTATION EFFORT (route 1
was a small edit to a script I already had) while labelling by PROBABILITY OF
SUCCESS. The two orderings disagreed and I did not notice. Underneath it I
was treating "use the result the paper already has" as a fallback and
"construct something new" as the real work. Route 3 is first from here.

THE TWO RESULTS, READ PROPERLY.

prop:decomposition [exact two-phase decomposition]: B0 is viable iff (i) some
declared blind control keeps every branch in V through step K, and (ii) some
declared blind control satisfying (i) lands every branch in RViab(V) at the
reveal. Over classes where window certificates are complete, these are
equivalent: both certificates silent; clause (i) holds; and B0 is either
viable or its nonviability is exactly the post-observation recourse mode.

prop:window-nogo [no window-measurable pair is complete]: a pair is
window-measurable when its verdicts depend only on the window sub-model --
initial belief, branch transitions within the window, floors, observation
schedule. NO window-measurable pair is complete. The proof IS a worked case:
"the three-state instance of Supplementary S3/A.3 and its variant agree on
all window data, the certificates are silent in both, and yet one is
nonviable (x4 exits under every post-reveal action) while the other is viable
(x4 is maintained)."

TWO CONSEQUENCES: (1) the paper is not short of a worked instance, it is
short of one FRAMED as the answer to the gap. (2) The gap is narrower than
"the kernel cannot be computed". What is proven is that the window phase is
decidable by certificates while the recourse phase is decidable by no
window-measurable pair -- so a certificate returns a verdict on the part it
can decide, on a system whose full viability question cannot be settled
window-measurably.

LARGE FIND: paper2_worked_systems, versions 1 through 17, in
paper rewrites/latex/. v17 is 10,374 words across 17 sections (master
monotonicity theorem; master table; policy classes; decentralized
observation; review timing on the hidden-regime grid; monitoring adequacy;
regime uncertainty; continuous benchmark; static duality; certainty-
equivalence drift audit; multiple floors; robustness margins; design rules;
verification methods) with a companion verification script of 63,080 chars.
This is worked-case material with an executable harness, and NONE of it is in
paper01. It is the natural source for, or home of, the case paper 1 lacks.

NEXT: read v17 against the gap; check whether its master table already holds
an instance where a certificate fires while the kernel is not
window-measurably decidable. Also still to locate: Supplementary S3/A.3,
which holds the three-state instance prop:window-nogo is proved on.
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

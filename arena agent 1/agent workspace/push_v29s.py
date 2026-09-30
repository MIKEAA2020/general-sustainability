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
    ("arena agent 1/agent workspace/diffs_compare.py", "/home/user/diffs/compare.py"),
]

MSG = """A011/A012/A020 against P5 and P4: the supplement gains content

Screen (diffs/compare.py): every number of three or more significant digits was
extracted from each module and from the paper it would fold into, then matched.

  A011 periodic review  5,692 w  vs P5  17 of 22 numbers shared (77%)
  A012 delay dynamics   8,006 w  vs P4  57 of 76 numbers shared (75%)
  A020 two channels     2,295 w  vs P4  21 of 23 numbers shared (91%)

A012 is the clear keep: the numbers absent from P4 are unambiguously registry
data -- persistence bisection tau in [148.125, 148.438] yr, crossings 17.568 and
18.362 yr at the out-of-range eta = 10, orbit folds near 5.574-5.575 and 5.587
yr, a second branch at 3.7849 and 150.12 yr, a real Floquet multiplier running
1.0514 at tau = 5.584 to 0.998983 at tau = 5.587, supercritical amplitude onset
with exponent 0.59, and 360-380 yr cycles in the lower regime. It is titled "A
Registered Family of Renewable-Resource Models", i.e. exactly supplement
material.

A011 keeps three case studies absent from P5 (Bangkok pumping after 1999,
Peruvian anchoveta 1950-2019, Icelandic cod CV 0.387 -> 0.143 post
implementation) and four methodology sections with no counterpart heading
(RAM spectral screen, power and detectability, prospective identification
designs, governance-event panels).

A020 is 91% subsumed; its only absent numbers are a SHA-256 fragment and one
frequency.

Limits recorded in the plan: an absent number does not prove absence, and the
section test failed outright because P5 is IMRaD (14 headings) while A011 is a
structured module (23 headings) -- they share only "conclusion". So A012 is safe
to fold in on this evidence, A011 needs one human read, A020 is a judgement
call. Consequence for the prune: revised_articles/ is supplement feedstock, not
prunable duplicates.
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

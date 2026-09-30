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
    ("arena agent 1/agent workspace/PAPER_A_PRIOR_ART.md", "/home/user/PAPER_A_PRIOR_ART.md"),
]

MSG = """Paper A prior art: revised after checking the manuscript

The first version of PAPER_A_PRIOR_ART.md was drafted from the plan's summary plus
an external search, without first reading obstr_v55's own prior-art treatment. That
is the same failure mode catalogued in plan 2.2 for the P5/E2 headline -- a
conclusion drafted before the check -- and it produced an overstated verdict. The
manuscript is not prior-art-naive:

  - It poses the split correctly: "Under incomplete observation the sufficiency
    direction has a canonical answer in Veliov's output-feedback regulation
    condition... The complementary direction -- certifying that no
    observation-based policy is viable --" is the paper's object.
  - It cites Aubin (1991), Aubin-Bayen-Saint-Pierre (2011), Saint-Pierre (1994),
    Aubin-Frankowska (1990), Frankowska (1989), Veliov (1993), Quincampoix-Veliov
    (1994), Cardaliaguet-Quincampoix-Saint-Pierre (2007), and Aubin (2001) on the
    failure side.
  - It makes the recommended distinction in its own words: "Veliov's condition
    tells us when output feedback can work; the obstruction calculus tells us when
    it cannot."
  - It distinguishes on checkability: one obstruction object "is a finite,
    checkable test" while two drift certificates "are not finite objects".
  - Section 5, "The Sufficiency Landscape", records the sufficiency results the
    obstruction calculus is defined against.

Two gaps remain, and the priority flips:

  1. HJ reachability / viscosity is entirely absent -- "viscosity" occurs ZERO
     times in 22,615 words, despite being the plan's first-named prior-art area.
     This is now the more urgent gap, and needs no paywalled source: add a
     paragraph contrasting the obstruction certificate with the
     BRT-as-viscosity-sublevel-set construction, on the observation assumption
     and the belief-state dimensionality barrier.
  2. Set-Valued Analysis 8, 149-162 (2000) is uncited. It gives necessary AND
     sufficient conditions, but only for a Lipschitz closed-loop maintaining the
     state exactly -- narrower than P2's "every policy" framing, and likely from
     the same school P2 already engages. Still required, but a
     citation-and-distinguish job.

Blocking step is now writing the viscosity paragraph, not obtaining the 2000 paper.
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

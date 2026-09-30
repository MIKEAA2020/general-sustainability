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
    ("arena agent 1/agent workspace/fam/e2/"
     "paperE2_cod_intervention_v29.tex",
     "/home/user/fam/e2/paperE2_cod_intervention_v29.tex"),
    ("arena agent 1/agent workspace/fam/e2/"
     "paperE2_cod_intervention_v29.pdf",
     "/home/user/fam/e2/paperE2_cod_intervention_v29.pdf"),
    ("arena agent 1/agent workspace/v29_battery.py", "/home/user/v29_battery.py"),
    ("arena agent 1/agent workspace/sabotage_v29.py", "/home/user/sabotage_v29.py"),
    ("arena agent 1/agent workspace/make_v29o.py", "/home/user/make_v29o.py"),
]

MSG = """Say what the two intervals are evidence for; register every abstract number

The profile range [67.9, 95.2] and the bootstrap interval [-89.4, 125.7] for
the same quantity differ by a factor of eight, and only the bootstrap crosses
zero. Both were carried in the abstract without saying why they disagree, which
one supports the paper's claim, or that the tight one is not a precision
statement.

- abstract: the profile range is presented as an identification result (pinned
  to within 27 kt while K is not identified from above) and explicitly not as a
  precision one; the bootstrap is the resampling dispersion of the estimate.
- 3.10: the disagreement is explained. The profile interval is F-based and
  holds the fit inside the 95% likelihood cut with r reprofiled; the bootstrap
  resamples and refits both parameters. The gap has two separable causes: the
  7.4% of replicates whose refit places K below the reference point, and
  small-sample dispersion with 24 transitions. It is not an artefact of the
  degenerate refits: the bootstrap is wider at both ends, 35 kt above the
  profile ceiling and 74 kt below its floor.
- battery: R25i/R25j pin the body's own bootstrap sentences, which were
  unpinned (a mutation corrupting them in 3.10 passed). R26 registers all 29
  abstract numeric tokens: 19 quantities recomputed from the archive and 10
  structural tokens, so a number added to the abstract without provenance
  fails the battery. 412 checks, 0 failed.
- sabotage: 136 mutations, 0 holes (5 new, including a fabricated abstract
  number and a reversed precision disclaimer).

Note: the paper source and compiled PDF were not in the repository before this
commit - only the checking scripts were. Both are now archived here.
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

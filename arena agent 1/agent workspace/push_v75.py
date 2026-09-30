#!/usr/bin/env python3
"""Emergency push: all workspace creations, before deleting clonable bulk.

Pushes the authoritative unit heads, every record .md, and every tool/script .py
in papers/ and p5/. Deliberately does NOT push the ~8 MB of superseded .tex
versions in papers/ -- those are already on the branch from earlier commits.
"""
import base64
import glob
import json
import os
import urllib.error
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT, "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}
PFX = "arena agent 1/agent workspace/"

HEADS = [
    "papers/paper01_obstruction_calculus_v63.tex",
    "papers/paper02_probabilistic_sufficiency_v12.tex",
    "papers/paper03_computational_certification_v16.tex",
    "papers/paper04_minimax_dual_certificates_v16.tex",
    "papers/paper05_exact_belief_computation_v16.tex",
    "papers/paper06_assessment_separation_v67.tex",
    "papers/paper07_sampled_governance_v50.tex",
    "papers/paper08_governance_delay_v46.tex",
    "papers/paper09_cod_certification_v32.tex",
    "papers/paper10_depletion_ledgers_v53.tex",
    "papers/paper11_forecasting_baselines_v64.tex",
    "papers/paper09b_arv_certification_v2.tex",
    "papers/paper10b_edwards_aquifer_v1.tex",
    "papers/paper11b_edwards_forecast_v2.tex",
    "papers/paper11c_worked_systems_audit_v2.tex",
]

targets = list(HEADS)
targets += sorted(glob.glob("papers/*.md"))
targets += sorted(glob.glob("papers/*.py"))
targets += sorted(glob.glob("p5/*.py"))
targets += sorted(glob.glob("push_v7*.py"))

FILES, seen = [], set()
for t in targets:
    if t in seen or not os.path.exists(t):
        continue
    seen.add(t)
    FILES.append((PFX + t, "/home/user/" + t))

MSG = r"""Emergency push of all workspace creations, before deleting clonable bulk

The workspace went far over the snapshot budget: cloning the repository added 924 MB, and the
snapshot cap has already begun pruning files (repo fell from 6,407 files to 2,416 on its own).
This commit secures everything that is NOT recoverable by cloning before the clonable bulk is
deleted.

Contents:

- The fifteen authoritative unit-source .tex files: the eleven heads of the ratified
  architecture plus the three merged-in companions (paper09b, paper10b, paper11b) and the
  container-derived unit 1, paper01_obstruction_calculus_v63.tex.
- Every record .md in papers/: SUBMISSION_ARCHITECTURE, PRIOR_ART_PASS,
  PHASE0_MERGE_VERIFICATION, and the rest.
- Every tool .py in papers/ and p5/: the merge machinery (mergelib, build, merge_*), the split
  machinery (split_parts, split_paper01_unit1), and the Phase 0 scanner.
- The push scripts v70-v75.

Deliberately NOT pushed here: the roughly 8 MB of superseded .tex versions in papers/, already
on the branch from earlier commits.

Deleted immediately after this commit, all recoverable: repo/ (the clone itself), tools/
(tectonic 26 MB plus its 44 MB cache, re-downloadable from the URL documented in RESTORE.md),
and lean/ (present in the repository).

Nothing here is a content change to any paper. This is a preservation commit.
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

tree, total = [], 0
for path, local in FILES:
    blob = api("POST", "/git/blobs",
               {"content": base64.b64encode(open(local, "rb").read()).decode(),
                "encoding": "base64"})
    sz = os.path.getsize(local)
    total += sz
    tree.append({"path": path, "mode": "100644", "type": "blob",
                 "sha": blob["sha"]})
    print("  %8d B  %s" % (sz, path.replace(PFX, "")))

print("total: %d files, %.1f MB" % (len(tree), total / 1e6))
new_tree = api("POST", "/git/trees", {"base_tree": base_tree, "tree": tree})
commit = api("POST", "/git/commits",
             {"message": MSG, "tree": new_tree["sha"], "parents": [base]})
api("PATCH", "/git/refs/heads/" + BRANCH, {"sha": commit["sha"]})
print("pushed: %s" % commit["sha"][:10])

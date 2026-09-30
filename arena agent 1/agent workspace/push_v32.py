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
    ("arena agent 1/agent workspace/papers/paper01_obstruction_calculus_v58.tex", "/home/user/papers/paper01_obstruction_calculus_v58.tex"),
    ("arena agent 1/agent workspace/papers/paper02_probabilistic_sufficiency_v10.tex", "/home/user/papers/paper02_probabilistic_sufficiency_v10.tex"),
    ("arena agent 1/agent workspace/papers/paper03_computational_certification_v10.tex", "/home/user/papers/paper03_computational_certification_v10.tex"),
    ("arena agent 1/agent workspace/papers/paper04_minimax_dual_certificates_v12.tex", "/home/user/papers/paper04_minimax_dual_certificates_v12.tex"),
    ("arena agent 1/agent workspace/papers/paper05_exact_belief_computation_v10.tex", "/home/user/papers/paper05_exact_belief_computation_v10.tex"),
    ("arena agent 1/agent workspace/papers/paper06_assessment_separation_v64.tex", "/home/user/papers/paper06_assessment_separation_v64.tex"),
    ("arena agent 1/agent workspace/papers/paper07_sampled_governance_v48.tex", "/home/user/papers/paper07_sampled_governance_v48.tex"),
    ("arena agent 1/agent workspace/papers/paper08_governance_delay_v42.tex", "/home/user/papers/paper08_governance_delay_v42.tex"),
    ("arena agent 1/agent workspace/papers/paper09_cod_certification_v30.tex", "/home/user/papers/paper09_cod_certification_v30.tex"),
    ("arena agent 1/agent workspace/papers/paper10_depletion_ledgers_v51.tex", "/home/user/papers/paper10_depletion_ledgers_v51.tex"),
    ("arena agent 1/agent workspace/papers/paper11_forecasting_baselines_v61.tex", "/home/user/papers/paper11_forecasting_baselines_v61.tex"),
    ("arena agent 1/agent workspace/papers/PAPERS_MANIFEST.md", "/home/user/papers/PAPERS_MANIFEST.md"),
]

MSG = """Editorial pass on the eleven papers

Cross-citations, 6.5-year ownership, and merge bridges.

  Cross-citations: every one of the eleven files now carries a sibling block
  naming its companions, with the directive that the selector principle, the
  epistemic kernel and the observation structure are defined in paper 1 and
  CITED by papers 2-5 rather than re-derived.

  6.5-year ownership assigned: paper 7 computes it on the sampled map and owns
  it; paper 8 carries an instruction to cite paper 7 and remove any independent
  re-derivation. The instruction is a note, not yet a text edit -- the duplicate
  passage in paper 8 still has to be removed by hand.

  Merge bridges written: papers 9, 10 and 11 now open with a "How the parts
  fit together" paragraph and their parts are promoted to \part{} units with
  labels. Paper 9 uses the E2/ARV reconciliation, which was already written;
  papers 10 and 11 are new prose.

STILL OUTSTANDING, not mechanically finishable:
  1 Framework de-duplication across papers 1-5. The sibling blocks state the
    rule; the actual excision of repeated setup from papers 2-5 is editorial
    judgement and has NOT been done. Each still derives the shared framework.
  2 Bibliography merging for papers 9, 10, 11. Each carries two or three
    separate reference lists. A duplicate-long-line diagnostic returned ZERO
    for all three, meaning the lists are not literal duplicates and must be
    merged by content, not by string match.
  3 The duplicate 6.5-year passage in paper 8 is flagged but not removed.

ROOT CAUSE of the failure this pass corrected: the divider written into the
merged files used %% inside a Python percent-format string, which collapses to
a single %, so the bridge-insertion regex silently matched nothing. Caught only
because the script reported zero words for three files instead of writing them.
A silent no-match is the failure mode to guard against: a script that edits
should always report what it changed.
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

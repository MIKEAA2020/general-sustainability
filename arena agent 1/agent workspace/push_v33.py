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

MSG = """Correct two errors in the manifest pushed in the previous commit

The previous commit's manifest section 5 contained two of my errors, both now
corrected.

  1. It claimed a duplicate-long-line diagnostic returned zero for papers 9,
     10 and 11. It did not. The first run reported zero only because the
     bridge-insertion regex failed to match and the script skipped those files
     before counting. The real counts, now that bridges are inserted: 87
     duplicated long lines in paper 9, 45 in paper 10, 113 in paper 11. These
     are the shared preamble and repeated reference entries.
  2. Its text was mangled in transit: back-quoted spans inside a shell
     double-quoted string were consumed by bash command substitution before
     the file was written, so a sentence about the part-units lost its
     content. Rewritten without back-quotes.

Everything else in the previous commit stands: cross-citation sibling blocks in
all eleven files, 6.5-year ownership assigned to paper 7 with a cite-instruction
in paper 8, and merge bridges in papers 9, 10 and 11.

Still outstanding and not mechanically finishable: framework de-duplication
across papers 1-5 (editorial judgement), bibliography merging for 9/10/11
(must be merged by content, not string match), and hand-removal of the
duplicate 6.5-year passage in paper 8.
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

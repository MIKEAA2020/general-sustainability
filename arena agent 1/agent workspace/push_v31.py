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

MSG = """Eleven papers assembled by content-and-merits partition, as new versions

Partition made on content and merits ONLY -- venue, length and submission
strategy excluded as considerations. Nothing overwritten; every file is a new
version with a provenance header naming its source.

  1 paper01_obstruction_calculus_v58          22,257 w  (obstr_v57)
  2 paper02_probabilistic_sufficiency_v10     11,804 w  (psuff_v9)
  3 paper03_computational_certification_v10    9,924 w  (comp_v9)
  4 paper04_minimax_dual_certificates_v12      6,107 w  (minimax_v11)
  5 paper05_exact_belief_computation_v10       3,420 w  (ebc_v9)
  6 paper06_assessment_separation_v64         27,934 w  (P1_v63)
  7 paper07_sampled_governance_v48            18,259 w  (p5_v47)
  8 paper08_governance_delay_v42              27,339 w  (p4_v41)
  9 paper09_cod_certification_v30             22,276 w  (E2_v29 + ARV_v9)
 10 paper10_depletion_ledgers_v51             42,982 w  (P3_v50 + E4_v16)
 11 paper11_forecasting_baselines_v61         39,499 w  (E1_v60 + E3_v17 + ws_v17)

TOTAL 231,801 words.

HONEST STATUS, recorded in PAPERS_MANIFEST.md: this is STRUCTURAL ASSEMBLY,
not editorial integration. Papers 1-8 are single-source and substantively
complete. Papers 9, 10 and 11 are CONCATENATIONS behind \clearpage dividers,
not merged arguments. Outstanding: (1) shared-framework de-duplication across
papers 1-5 -- the setup must be derived once in paper 1 and cited by 2-5;
(2) sibling cross-citations, currently absent throughout; (3) the 6.5-year
crossing is duplicated in papers 7 and 8 -- paper 7 owns it, paper 8 must cite;
(4) merge editing for 9/10/11, of which only 9 has written reconciliation prose;
(5) bibliography merging for 9/10/11, which carry two or three reference lists.

ROOT CAUSE of the mis-partition: the earlier inventory was built by listing
fam/. The P2 companions live in paper rewrites/latex/ under paper2_* names and
were never enumerated, so three of eight venue-assigned papers were dropped.
An inventory built from one directory is not an inventory of the family.

Why the count moved 3 -> 8 -> 10 -> 11: each move was an evidence correction.
8 -> 10 because a CONTENT overlap test replaced a section-title test and showed
the five P2 papers near-disjoint, invalidating two merges justified by thinness
rather than duplication. 10 -> 11 because removing venue considerations left
the P5/P4 merge unsupported: a hybrid sampled map against a delay differential
equation, with almost disjoint result sets.

RECURRING FAILURE MODE, named: three times a conclusion was reached before the
evidence was checked -- the prior-art verdict, the drift onto papers outside
the named family, and the two merges later invalidated. Remedy each time: read
the artifact, measure, then conclude.

CORRECTION I OWE: I twice answered "have you drifted" defensively, explaining
that the plan assigned P5 to Paper B, rather than acknowledging that six of the
eight named papers had received no work. That was exculpatory, not accurate.

CONFIDENCE: comp and psuff high; ebc MODERATE (no file named ebc*) -- paper 5
rests on it and should be confirmed first.
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

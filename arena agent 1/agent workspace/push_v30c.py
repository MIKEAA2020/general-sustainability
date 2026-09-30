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
    ("arena agent 1/agent workspace/diffs/paperB_ss1-5.tex", "/home/user/diffs/paperB_ss1-5.tex"),
    ("arena agent 1/agent workspace/diffs/paperB_cadence.tex", "/home/user/diffs/paperB_cadence.tex"),
    ("arena agent 1/agent workspace/FAMILY_PAPER_COUNT.md", "/home/user/FAMILY_PAPER_COUNT.md"),
]

MSG = """Recommendation: 8 papers, with the evidence it rests on

The question reduces to something sharper than "how many". preprints.org is a
STAGING venue with no length limit, so posting more preprints buys nothing on
its own. Each preprint should map to exactly one journal submission. So the
real question is how many journal articles the content merits, decided by one
test per candidate: does it pose one answerable question, stand on its own,
and survive separation without being weakened?

EVIDENCE FIRST -- the four P2 companions are NOT absorbed into obstr_v57.
Checked by section-title overlap:
  psuff    11,804 w  13 sections  0/13 overlap with obstr
  comp      9,924 w  14 sections  0/14
  minimax   6,107 w  12 sections  1/12
  ebc       3,420 w  11 sections  0/11
Their objects are distinct -- measure duals and envelopes; adjoint safety rows
and a continuous-to-finite theorem; a support identity and exact sufficiency;
a pairwise-Hamming classification and antichain census. A programme with
several papers in it, not one paper with four drafts.

THE EIGHT:
  1 Obstruction certificates          obstr + minimax   ~28.7k  Automatica
  2 Computation of certificates       comp + ebc        ~13.3k  SIAM J Opt
  3 Exact probabilistic sufficiency   psuff             ~11.8k  IEEE TAC
  4 Quantifier-order separation       P1                ~30.6k  Math OR
  5 The decision clock                P5 + P4           ~45.6k  preprints
  6 Certified horizons on a record    E2 + ARV          ~23.5k  CJFAS
  7 What depletion numbers certify    P3 + E4           ~45.0k  Ecol Econ
  8 Forecasting baselines and null    E1 + E3 + ws      ~41.0k  Int J Forecast
Total roughly 240,000 words.

WHY THESE MERGES. Five P2 papers become three: minimax folds into obstr (dual
certificates are part of the certificate theory; 6.1k is thin alone) and ebc
folds into comp (both computational; 3.4k is a section, not an article).
psuff stays alone -- exact sufficiency is a different question from
obstruction and is a full paper.

P1 STANDS ALONE, reversing the current plan. At 30,600 words the separation
result is a full article; the plan files it as "Supplement S1" of Paper A,
burying 30k words of real result inside someone else's paper.

P5 + P4 MERGE BECAUSE THEY SHARE A RESULT. Both report the 6.5-year crossing
-- P5 as the exact map's single crossing, P4 as the mobilising rule
restabilising above 6.5 yr through a Neimark-Sacker crossing. Split, each
would cite the other for the same number, the worst outcome. This is the one
merge the content demands rather than merely permits.

E2 + ARV merge: two directions on one record, already reconciled, ARV too thin
alone at 7,256 w. Measurement splits by question, not length.

PREPRINTS.ORG: post all eight, each with a DOI. Do not split for length.
RESOLVE OVERLAP BEFORE POSTING -- the main risk. The shared framework
(selector principle, epistemic kernel, observation structures) must be derived
ONCE in paper 1 and cited by 2 and 3; re-deriving it three times is what makes
a programme look like salami-slicing. Cross-cite explicitly.

CAVEATS: companion separation was checked by section-title overlap, which is
crude -- it establishes they are not absorbed but does not rule out
content-level duplication; papers 1-3 need a proper content diff. ebc
identification remains moderate confidence. Word counts for E1/E3/E4/ws are
inferred from file sizes, not counted. The economics material (ecomod_v37,
manuscript_ECOMOD_v37, paper3_JIE_submission, JIE_cover_letter) is in none of
the eight -- if live, it is a ninth.
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

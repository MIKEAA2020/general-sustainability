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

MSG = """REVISED: the count is 10, not 8 -- content-overlap test run

The section 1 check used section-title overlap and proved the P2 companions
are not absorbed into obstr. It did not test content. That test is now run:
sentences of eight or more words extracted from all five P2 manuscripts and
intersected.

  obstr <-> psuff    0 shared   0.0%
  obstr <-> comp     0 shared   0.0%
  obstr <-> ebc      0 shared   0.0%
  obstr <-> minimax  1 shared   0.7%
  minimax <-> psuff  2 shared   1.5%
  psuff <-> comp     4 shared   1.9%
  psuff <-> ebc      3 shared   3.4%
  comp <-> ebc       4 shared   4.5%
  minimax <-> comp / ebc  1 / 0  0.7% / 0.0%

Sentence counts: obstr 557, psuff 248, comp 216, minimax 137, ebc 89.

THE FIVE ARE ESSENTIALLY DISJOINT IN CONTENT. This reverses the two merges.
minimax -> obstr was justified by thinness, not duplication; with no
duplication to remove, folding it in buries an independent result, and 6,107
words is a legitimate Mathematics of OR research article. ebc -> comp
likewise: 3,420 words is about right for an Automatica Technical Communique,
the short format it was already assigned.

The revised count matches the original venue assignment, which gave the five
P2 papers five separate venues.

THE REVISED TEN:
  1 Obstruction certificates            obstr          22,615  Automatica
  2 Exact probabilistic sufficiency     psuff          11,804  IEEE TAC
  3 Computational certification         comp            9,924  SIAM J Opt
  4 Minimax dual certificates           minimax         6,107  Math OR
  5 Exact belief computation            ebc             3,420  Automatica TC
  6 Quantifier-order separation         P1            ~30,600  Math OR
  7 The decision clock                  P5 + P4       ~45,600  preprints
  8 Certified horizons on a record      E2 + ARV      ~23,500  CJFAS
  9 What depletion numbers certify      P3 + E4       ~45,000  Ecol Econ
 10 Forecasting baselines and the null  E1 + E3 + ws  ~41,000  Int J Forecast

PAPER 7 SURVIVES AS A MERGE because P5 and P4 share an actual RESULT -- both
report the 6.5-year crossing. That is content overlap, not thinness, and
splitting would make each cite the other for the same number. It is the one
merge the evidence supports. Papers 1-5 stand apart because the overlap test
found nothing to remove by merging.

PREPRINTS.ORG: ten preprints, ten DOIs, ten submissions. The salami-slicing
risk is smaller than it looks precisely BECAUSE overlap is near zero -- but
the corollary is that each paper must cite its siblings for the shared
framework rather than re-derive it. With five disjoint P2 papers, a reader of
paper 3 needs one line telling them the selector principle and epistemic
kernel are defined in paper 1.

REMAINING CAVEATS: the test is sentence-level on shared strings and would miss
paraphrase-level duplication -- strong evidence of disjointness, not proof.
ebc identification remains moderate confidence. Word counts for P1/E1/E3/E4/ws
are inferred from file size, not counted. The economics material is in none of
the ten; if live, an eleventh.
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

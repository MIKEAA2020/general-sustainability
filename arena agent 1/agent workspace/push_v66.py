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
    ("arena agent 1/agent workspace/papers/SUBMISSION_ARCHITECTURE_DRAFT.md",
     "/home/user/papers/SUBMISSION_ARCHITECTURE_DRAFT.md"),
    ("arena agent 1/agent workspace/papers/paper03_computational_certification_v16.tex",
     "/home/user/papers/paper03_computational_certification_v16.tex"),
    ("arena agent 1/agent workspace/papers/paper10_depletion_ledgers_v53.tex",
     "/home/user/papers/paper10_depletion_ledgers_v53.tex"),
    ("arena agent 1/agent workspace/p5/phase0_scan.py",
     "/home/user/p5/phase0_scan.py"),
]

MSG = r"""Draft submission architecture derived from the recorded venue strategy; scanner context-check

SUBMISSION_ARCHITECTURE_DRAFT.md supersedes my seven-way merge partition. SIX OF MY SEVEN
MERGES WERE WRONG, and the reason is diagnostic: I grouped by CONTENT AFFINITY ("do these
support a broader claim together?") when the driver should have been SUBMISSION UNIT ("which
papers constitute one journal submission?"). The recorded strategy -- FAMILY_CONSOLIDATION_PLAN
section 1.1 and FAMILY_PAPER_COUNT's revised ten -- already answers that question and answers
it differently.

THE DRAFT: 11 units, each = one claim = one venue.
  1 paper01  Obstruction calculus            Automatica Regular        23,428 w  21 thm
  2 paper02  Probabilistic sufficiency       IEEE TAC Full             13,632 w  18 thm
  3 paper03  Computational certification     SIAM J. Optimization      13,629 w   7 thm
  4 paper04  Minimax dual certificates       Mathematics of OR          8,566 w  13 thm
  5 paper05  Exact belief computation        Automatica Tech Comm       6,435 w   9 thm
  6 paper06  Quantifier-order separation     Math OR / SIOPT           29,071 w   0 thm
  7 paper07+paper08  The decision clock      preprints first           47,923 w  16 thm
  8 paper09+paper09b Certified horizons      CJFAS                     23,766 w  14 thm
  9 paper10+paper10b Depletion numbers       Ecological Economics      44,338 w   0 thm
 10 paper11+paper11b Forecasting and the null Int. J. Forecasting      30,401 w   0 thm
 11 paper11c Exact audits of worked systems  Systems & Control Letters 11,123 w  14 thm

FOLD-OR-SEPARATE. UNITS 1-5: SEPARATE. This reverses my 1+2 and 3+4 merges and the plan's
minimax->obstr and ebc->comp. The dispositive evidence already exists: a sentence-level overlap
test found the five P2 manuscripts ESSENTIALLY DISJOINT (obstr<->psuff/comp/ebc 0.0%;
obstr<->minimax 0.7%; comp<->ebc 4.5%). With no duplication to remove, folding removes nothing
and buries an independent result. THE CRUCIAL POINT: the "below bar" verdicts on 2, 3, 4, 5 are
PRIOR-ART verdicts, and FOLDING CANNOT FIX THEM. Measured prior-art sections: unit 1 has 951
words of real prose; units 7a/7b 518/652; 8a/8b 608/647; 9a/9b 531/590; 10a/10b/10c 532/438/405
-- but units 2, 3, 4, 5 and 6 have STUBS. Folding paper02 into paper01 produces a larger paper
THAT STILL HAS NO PRIOR-ART SECTION. The block is removable by writing ~600-950 words per
paper, which is what the others already have. Cost of folding would be four venues surrendered
to purchase nothing.
UNIT 6: separate, but its prior art is a RESEARCH task -- the bar assessment flags it as
highest novelty risk because the separation result sits close to known robust-optimisation and
MCDM separation results. Units 2-5 need a writing job; unit 6 needs the literature searched.
UNIT 7: MERGE. P5 and P4 share an actual RESULT -- both report the 6.5-year crossing. The
recorded strategy says explicitly "this is the one merge the evidence supports." It is the only
one of my seven that survives.
UNITS 8, 9, 10: MERGE. Each folds a thin member that shares a RECORD, SYSTEM or QUESTION with
its host: ARV is a second direction on the same cod record; E4 a second withdrawal system under
the same depletion question; E3 a second system under the same retention rule. Thinness plus
shared object -- the right reason.
UNIT 11: CONTESTED. The recorded strategy CONTRADICTS ITSELF: FAMILY_CONSOLIDATION_PLAN
section 1.1 assigns ws to Systems & Control Letters; FAMILY_PAPER_COUNT's revised ten folds ws
into unit 10 at Int. J. Forecasting. Content favours S&CL decisively -- paper11c is "Exact
Audits of Worked Systems for the OBSTRUCTION CALCULUS", 14 theorems, 405 words of real prior
art, 11,123 words (not thin). Recommendation: stands alone at S&CL, making eleven.

WHAT MY SEVEN-WAY PARTITION COST: 1+2 wrong (lost TAC, did not fix the prior-art gap it was
meant to fix); 3+4 wrong (same); 5+11c wrong (lost a Tech Communique, misplaced 11c out of the
forecasting unit); 6+10 wrong (buried a standalone 29k-word result, separated 10 from 10b);
8+7 CORRECT; 9+9b+10b wrong (misplaced 10b into the cod unit); 11+11b incomplete (should also
take 11c). Four venues surrendered, three papers misplaced, and the folding was aimed at a
prior-art gap that folding is structurally incapable of closing.

THE FOLD RULE THIS YIELDS. Fold when the member shares a result, record, system or question
with the host, or is too thin to stand alone at any venue it was assigned. Separate when the
member poses its own question, carries its own result, and is at a legitimate length for a
venue it was assigned. NEVER FOLD TO FIX A MISSING PRIOR-ART SECTION.

SCANNER CONTEXT-CHECK, AS DIRECTED. A string match is a CANDIDATE, not a finding. Each
stale-provenance signature now carries an excusing context; if the paper states the current
value AND the caveat beside the stale one, the hit is reclassified as a disclosed caveat and
reported as a POSITIVE signal. Self-disclosure is now detected and reported ("build has not
been re-run", "should be re-confirmed before submission"). Effect on the 15 source heads: 10
hits reclassified as disclosed, 4 remaining actionable. The scanner also caught a real
asymmetry the raw match missed -- unit 3's provenance sentence stated the run pin but not the
current pin, unlike its siblings.

paper03 v16 (new version, source untouched): completes that sentence to "pinned to Lean~4 in
lean-toolchain (currently v4.34.1); the checks were run under v4.14.0", consistent with units
1, 4 and 5. 13 pp, 0 errors.

TWO POINTS OPEN FOR RATIFICATION: (1) unit 11 -- stand alone at S&CL (eleven units) or fold
into unit 10 per the revised ten; the recorded strategy says both. (2) units 2-5 -- the
recommendation is separate-and-write-prior-art, four prior-art sections, four more
submissions; folding is coherent if the preference is fewer stronger papers, but it must be
paired with writing the prior art anyway or the merged paper inherits the gap.
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

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
    ("arena agent 1/agent workspace/papers/SUBMISSION_ARCHITECTURE.md",
     "/home/user/papers/SUBMISSION_ARCHITECTURE.md"),
]

MSG = r"""Re-derive the architecture with COHERENCE as the driver; withdraw the cost-of-folding column

THE CORRECTION ACCEPTED. With preprints.org as the primary target, TWO COLUMNS OF THE
RATIFIED DRAFT ARE VOID: (a) VENUE -- informational only, not decisive; (b) COST OF FOLDING --
if preprints are the target, folding loses no submission, so "loses a TAC submission" and
"loses a SIOPT submission" measure nothing. The stated reason for separating units 2-5 -- "four
venues surrendered to purchase nothing" -- WAS WRONG UNDER THE ACTUAL GOAL. I was still
reasoning as if each paper needed its own journal slot. The JMCDA concern is likewise void:
with preprints as the target there is no competing journal submission to conflict with.

RE-DERIVED WITH COHERENCE AS THE SOLE DRIVER. Fold when the member shares a result, record,
system or question with the host, or is too thin to be a coherent standalone piece. Separate
when the member poses its own question, carries its own result, and is coherent on its own
terms. Never fold to fix a missing prior-art section. The venue column is retained as
informational only; nothing changes if a venue is retargeted.

ELEVEN UNITS, WITH ONE STRUCTURAL CHANGE FROM THE VENUE-DRIVEN DRAFT:
  1  paper01                     Obstruction calculus            23,428 w  21 thm
  2  paper02                     Probabilistic sufficiency       13,632 w  18 thm
  3  paper03                     Computational certification     13,629 w   7 thm
  4  paper04                     Minimax dual certificates        8,566 w  13 thm
  5  paper05                     Exact belief computation         6,435 w   9 thm
  6  paper06                     Quantifier-order separation     29,071 w   0 thm
  7  paper07 + paper08           The decision clock              47,923 w  16 thm
  8  paper09 + paper09b + paper10b  Certification on real records 33,092 w 14 thm
  9  paper10                     Depletion arithmetic            35,012 w   0 thm
 10  paper11 + paper11b          Forecasting and the null        30,401 w   0 thm
 11  paper11c                    Exact audits of worked systems  11,123 w  14 thm

THE ONE CHANGE: paper10b MOVES FROM UNIT 9 TO UNIT 8. Under the recorded venue strategy it sat
with paper10 (P3, ledgers) at Ecological Economics. Under coherence it belongs with unit 8:
(a) its central result IS unit 8's claim -- "every positive-pumping certified kernel is empty
beyond three years, an optimistic bound on a defect the out-of-sample audit exceeds" is the
HORIZON result on a second system; (b) its machinery is unit 8's -- robust viability kernels
under a retention protocol frozen before any score, exactly paper09b's (ARV) apparatus; with
paper10 it shares only a DOMAIN (groundwater), not a method or a question; (c) paper10 does not
need it -- the standing direction on P3 was that "the four applied sections are the ingredient
that lifts it from typology to measurable consequence", so P3 carries its own application (three
public-data indicators classified at their exact status, plus the registered domain templates);
(d) unit 8 gains breadth it otherwise lacks -- as {09,09b} it is cod-only, and with paper10b it
is exact viability certification on TWO real systems with no hydrology, biology or institutional
history in common. Option A (recorded): unit8 23,766 w cod only, unit9 44,338 w. Option B
(coherence): unit8 33,092 w cod+Edwards, unit9 35,012 w.

WHAT DID NOT CHANGE, WITH THE REASONS REPLACED. UNITS 1-5 STILL SEPARATE, but not for the
reason I gave. Two venue-independent grounds now carry it: (1) DON'T BURY INDEPENDENT RESULTS --
the five are essentially disjoint, sentence-level overlap 0.0% (obstr<->psuff/comp/ebc), 0.7%
(obstr<->minimax), 4.5% (comp<->ebc); folding removes nothing and buries five independent
results. (2) FOLDING CANNOT PRODUCE A PRIOR-ART SECTION -- units 2,3,4,5 have stub prior-art
sections (0 words) against 405-951 for the others. UNITS 7, 8, 10 STILL FOLD on shared result
(7: the 6.5-yr crossing), shared machinery and question (8), shared rule and question (10),
each with a thin member (9,637 w and 9,326 w). None of this depended on venue.

GUARDING AGAINST FOLDING DRIFT, AS DIRECTED. Removing venue pressure removes the main argument
AGAINST folding, so the drift risk is real. Three checks hold the line: (a) DISJOINTNESS BLOCKS
THE BIG FOLD -- the obvious temptation is one large obstruction-programme paper from units 1-5;
the overlap test forbids it, since there is no duplication for a merge to remove and the only
effect would be to bury four independent results. (b) THINNESS IS NOT ALONE SUFFICIENT -- units
4 (8,566 w) and 5 (6,435 w) are thinnest but each poses and answers one question completely;
thinness justifies folding only when the member also shares a result, record, system or question
with a host, and neither does. (c) A BURIED RESULT IS A DEFECT UNDER ANY TARGET -- unit 6 at
29,071 w was folded into unit 9 in my earlier seven-way partition, burying a standalone result
with its own claim inside a paper about ledgers; wrong whether the output is a preprint or a
journal article.

PRIOR ART REMAINS THE GATING TASK. Measured: unit 1 951 w of prior art, 7a/7b 518/652,
8a/8b/8c 608/647/590, 9 531, 10a/10b 532/438, 11 405 -- and units 2,3,4,5,6 have ZERO. A
preprint without prior art is incomplete scholarship whether or not it is peer-reviewed. It
must be treated as a NOVELTY TEST, not a drafting exercise: no one has checked whether these
results survive the literature, because until now there was no prior-art section to check them
against. Attrition plan: reposition the claim; combine with a sibling (permissible -- the
prohibition is specifically on folding TO FIX A PRIOR-ART GAP, not on folding for a new
reason); or drop. Unit 5 likeliest casualty (thinnest), unit 3 least likely (comparator now
explicit).

ONE OPEN QUESTION: IS PREPRINTS.ORG THE FINAL TARGET OR THE FIRST STEP? The record
(FAMILY_PAPER_COUNT section 0) treats it as STAGING, one preprint mapping to one eventual
journal submission; the current direction treats it as primary. Compatible if the reading is
"primary near-term target, journals later." The answer determines only whether the venue column
is retained as provisional or dropped entirely -- THE PARTITION IS THE SAME EITHER WAY, since
it is now coherence-driven.
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

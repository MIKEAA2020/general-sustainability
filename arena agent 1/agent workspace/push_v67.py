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

MSG = r"""Ratify the submission architecture: eleven units, with the prior-art inference verified

RATIFIED 2026-09-30. Eleven units, each one claim, derived from the recorded venue strategy
and grouped by CLAIM rather than content affinity.

VENUE IS SECONDARY AND THIS IS NOW STATED IN THE DOCUMENT. The target is preprints.org, with
one preprint mapping to one eventual journal submission. The venue column records the intended
destination; it is not the reason any unit is constituted. The partition stands on the claim
structure and the fold rule, both venue-independent. Nothing in the partition changes if a
venue is retargeted.

AMENDMENT 1: UNIT 11 STANDS ALONE AT SYSTEMS & CONTROL LETTERS. paper11c is
obstruction-calculus machinery -- 14 theorems, 405 words of real prior art, 11,123 words, not
thin. Folding it into unit 10 would put calculus machinery in front of Int. J. Forecasting
referees. Venue match outweighs unit count: eleven units, not ten.

AMENDMENT 2: THE PRIOR-ART INFERENCE WAS VERIFIED, NOT ASSUMED -- AND THE PUSHBACK WAS
RIGHT ON 2 OF 4. The partition rested on an inference: that the bar assessment's "blocked" /
"below bar" verdicts on units 2-5 are PRIOR-ART-ONLY. Checked against the actual wording:
  unit 2 psuff:  "none states a prior-art position" -- prior art ONLY. Stub.
  unit 4 minimax:"none states a prior-art position" -- prior art ONLY. Stub.
  unit 3 comp:   prior art PLUS "five formal results for a computational paper, WITH NO
                 COMPARATOR FOR ITS COMPLEXITY CLAIMS" -- beyond prior art, BUT NOW CLOSED:
                 Saint-Pierre (1994) is engaged in the body (L1416) and the rank result gives
                 a real comparator -- a Helly-type "at most m+1 states suffice" bound is valid
                 for convex common-action sets and FALSE for a common blind control function,
                 the correct dimension being information-time rank. Grew 10,077 -> 13,629 w,
                 5 -> 7 theorems.
  unit 5 ebc:    prior art PLUS "against substantial methodological development this does not
                 clear AT THIS LENGTH", requiring "a scope decision: expand beyond the cube
                 instance, or fold into paper 3" -- beyond prior art, BUT THE SCOPE DECISION
                 WAS TAKEN: task 58 expanded m=4 -> m=5, census 16x2^32 = 68,719,476,736 ->
                 1,552, with raw growth 65,536x against stored growth 3.13x. Grew 3,578 ->
                 6,435 w, 9 theorems. Remaining question is whether 6,435 w clears for a
                 Technical Communique; it is the thinnest of the five.
CONSEQUENCE: the separate-and-write-prior-art recommendation SURVIVES, because the decisive
argument was never venue-count but this -- FOLDING CANNOT PRODUCE A PRIOR-ART SECTION. That
argument is untouched by the verification. But the ratification carries one correction: THE
PRIOR ART FOR UNITS 2-5 MUST BE TREATED AS A NOVELTY TEST, NOT A DRAFTING EXERCISE. No one has
checked whether these results survive the literature, because until now there was no
prior-art section to check them against. Attrition must be budgeted for.

ATTRITION PLAN, RECORDED. If a unit's result does not survive its novelty test, options in
order: reposition the claim to what the evidence supports; combine with a sibling FOR THE NEW
REASON (a collapsed novelty claim genuinely changes the fold calculus -- the earlier ruling
only excluded folding TO FIX A PRIOR-ART GAP, not folding for any other reason); or drop.
Unit 5 is the most likely casualty, being thinnest; unit 3 the least likely, its comparator
now being explicit.

OPEN ITEM, NEEDS A HUMAN ANSWER: unit 1's venue and a possible live JMCDA special-issue
submission. Ratification flagged that a JMCDA special-issue submission for Paper 1 may exist
from earlier in the project, which would conflict with the Automatica assignment. CHECKED: NO
TRACE. "JMCDA", "special issue" and "Special Issue" return ZERO matches across every .md in
the workspace and across paper01_obstruction_calculus_v61.tex. Either the submission predates
the workspace record, was recorded only in conversation, or does not exist as a live artifact.
Under the ratification's own rule -- the live submission's venue takes priority over the
architecture's assignment -- this is the only unresolved item in the architecture, and it
cannot be settled from the workspace.
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

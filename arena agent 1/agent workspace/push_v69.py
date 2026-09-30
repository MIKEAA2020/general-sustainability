#!/usr/bin/env python3
"""Commit the target-settled architecture on top of the REMOTE tip.

Builds one commit directly on the remote tip through the Git data API,
because the local clone is shallow and has diverged from the remote.
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

MSG = r"""Settle the target: preprints.org is FINAL, not staging; drop the venue column entirely

THE OPEN QUESTION IS CLOSED. PREPRINTS.ORG IS THE FINAL TARGET. Journal submission is a
possible secondary prospect only, and is never allowed to shape the partition. The venue column
is DROPPED rather than retained as provisional -- a provisional column reopens the question
"would this fold more neatly at journal X" every time the partition is revisited, and with the
target settled that question has no standing. The partition is unchanged: it is derived from
coherence, and coherence does not depend on where a paper is posted.

WHAT FINAL-TARGET CHANGES ABOUT THE BAR -- a real change, not bookkeeping. Under a journal
target three functions are discharged FOR the paper by referees: error detection, scope
moderation, prior-art screening. Under preprints.org as the final destination NONE OF THEM ARE.

  (a) SCREENING IS SHALLOW BY DESIGN. Preprints.org screens for "basic scientific content,
      author background, and compliance with ethical standards", in under one business day
      (preprints.org/about). It will not detect a false lemma, a mis-stated interval, or a
      missing prior-art section.
  (b) THERE IS NO REVISION ROUND. Screening is a pass/fail gate, not a referee loop. What is
      posted is what stands.
  (c) IT CANNOT BE TAKEN BACK. Authors must acknowledge that "preprints cannot be completely
      removed once online" (preprints.org submission guidance). A published defect is permanent
      and carries a DOI.

CONSEQUENCE: THE THREE PENDING PASSES ARE NOT PREPARATION FOR A GATE THAT WILL CHECK THEM --
THEY ARE THE ONLY GATE THERE IS. Phase 0 (soundness), the prior-art novelty test, and the claim
audit move from advisory to LOAD-BEARING. And because publication is irreversible, ORDER
MATTERS: a unit should not be posted before it has passed its own passes. This strengthens
rather than relaxes the case for the pending work, and it is the opposite of the drift risk --
removing a referee does not remove the standard, it removes the safety net.

UPSIDE WORTH BANKING. Preprints.org assigns a DOI and posts under CC BY 4.0, so every unit --
and every supplementary file -- is permanently citable and dated. This is what makes the
standing NO-CONTENT-LOST rule satisfiable: material displaced to supplementary is citable, not
orphaned. The rule is preserved by the target rather than threatened by it.

NEW PRE-POSTING CHECKLIST, to be verified against the platform itself before the first unit
goes up. None of it changes the partition.

  1. AI-USE DISCLOSURE. Preprints.org is run by MDPI, whose house policy requires generative-AI
     use to be disclosed in an Acknowledgments statement and described in detail in Methods,
     with grammar and formatting exempt (MDPI announcement 5687; COPE-aligned). That policy is
     documented for MDPI JOURNALS; whether it is applied to the preprint platform has NOT been
     verified. It bears squarely on this family, developed with AI assistance. VERIFY BEFORE
     POSTING AND DEFAULT TO DISCLOSURE IF UNCERTAIN -- over-disclosure carries no penalty,
     under-disclosure is treated as an ethics breach.
  2. RESEARCH DATA MUST BE AVAILABLE at submission. Each unit needs a data/code availability
     statement. The Lean-checked units already name their toolchain pins, which is most of one.
  3. CONSENT TO THE NO-WITHDRAWAL POLICY. Co-authors must agree to CC BY 4.0 posting and to the
     fact that the preprint cannot be removed once online. Sole-authored or not, that
     irreversibility deserves a conscious decision per unit, taken AFTER its passes.

Unchanged and still standing: eleven coherence-driven units; the paper10b -> unit 8 move; the
disjointness and prior-art grounds for keeping units 1-5 apart; the three anti-folding-drift
checks; prior art as the gating task with attrition budgeted.
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

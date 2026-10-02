#!/usr/bin/env python3
"""Commit: structural proof audit of theory units 1-6 and 11."""
import base64
import json
import os
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT, "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}
PFX = "arena agent 1/agent workspace/"

FILES = ["papers/PROOF_AUDIT.md",
         "papers/proof_audit.py",
         "papers/proof_audit2.py"]

MSG = r"""Structural proof audit of the theory units (remaining-work item b)

Units 1-6 and 11 are theorem papers, so no numeric check discharges them. Two instruments were
built; the first is superseded by the second and both are committed, with the error recorded.

INSTRUMENT ERROR (the tenth of its class). proof_audit.py counted only \begin{proof}
environments and reported units 1 and 7 as having ZERO proofs against 21 and 16 claims. That
reading is wrong. Both units write proofs inline as \emph{Proof.} / \emph{Proof sketch.}
paragraphs with no environment at all: unit 1 has 20 such markers, unit 7 has 19. Trusting the
count would have produced a badly false report -- "37 theorems with no proofs" -- out of a
stylistic difference. Caught by reading the file. Two further false-positive modes in the
corrected instrument: deferred proofs (proof placed after the next claim environment) and
embedded proofs (argument inside the statement body). Neither is a defect.

FINDING A (narrow). Of 112 claim environments in the family, exactly one has no evidence of
proof of any convention: unit 1's selector principle, calc-prop:selector, L609-L630, followed
only by a subsection heading before the next claim at L666. It matters out of proportion
because section 1.2 Contributions states "Five obstruction mechanisms are developed, each with
a complete proof", and the selector principle is one of the five. Its complete proof exists in
the v51 supplement and is not in v63.

Eight claims were flagged; five were cleared by context-checking and three (all unit 4) are a
house style for computed results -- worked instance or verification script rather than a formal
proof -- which is not a defect. Recorded individually.

FINDING B (systemic, 75 pointers, 4 units). Units 1, 6, 7 and 9 repeatedly cite their own
supplementary sections S1...S17 and NO SUCH DOCUMENT EXISTS FOR ANY OF THEM. Unit 1: 17
pointers. Unit 6: 3. Unit 7: 44. Unit 9: 11.

Unit 1 is a REGRESSION, not an unkept promise. paper2_obstruction_calculus_v40..v51
_Automatica_routes_supplementary.tex all exist on the branch (v51 is 85,563 B). v52 and every
later version has no supplementary file, and the in-text pointers survived the deletion. Units
6, 7 and 9 never had one: checked across 7,240 branch paths.

Unit 1's supplement is RECOVERABLE, and it fits exactly. v51 main text and v63 contain identical
sets of 21 claims compared by (environment type, statement name) -- zero added, zero dropped.
The v51 supplement has S1. Complete proofs (L28-799) containing thm:finite-horizon, thm:exit and
the Complete proof of the selector principle (L443), plus S4. Additional figures holding
Figure~S1 (fig_p2_ladder.png) and Figure~S2 (fig_p2_obstruction_tree.png) -- precisely the two
supplementary figures v63 cites. 19 of its 25 labels match v63 once the calc- prefix is
stripped; the 6 that do not are its own internal figures, table and appendix heading. The only
adaptation needed is a mechanical label rewrite.

This is severe under the ratified target. Under preprints no one performs error detection, scope
moderation or prior-art screening but us; there is no revision round and publication is
irreversible. A reader who checks the finite-horizon completeness theorem finds "Proof sketch",
then a pointer to S1, then nothing. Forty-four such pointers in unit 7 make the paper
unverifiable exactly where it invites verification.

NOTHING HAS BEEN EDITED. Remediation is a pending decision recorded in section 7 of the audit:
recover unit 1's supplement mechanically; for units 6, 7 and 9 (58 pointers, no source material)
either strip and fold the load-bearing content in, write the supplements where comp/ supports
reconstruction, or do not post. The third option is incompatible with an irreversible first
posting, so it is recorded only for completeness.

Limitations: structural only -- this checks that a proof is evidenced, not that it is correct;
no theorem has been verified by reading its argument. Units 6, 9 and 10 number results inline
rather than in claim environments, so their results are absent from the claim totals. Pointer
matching is regex-based, so 75 is a lower bound. Compilation remains unverified.
"""


def api(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(BASE + path, data=data, headers=HDRS, method=method)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


base = api("GET", "/branches/" + BRANCH)["commit"]["sha"]
print("base commit: %s" % base[:10])
base_tree = api("GET", "/git/commits/" + base)["tree"]["sha"]

tree = []
for f in FILES:
    blob = api("POST", "/git/blobs",
               {"content": base64.b64encode(open(f, "rb").read()).decode(),
                "encoding": "base64"})
    tree.append({"path": PFX + f, "mode": "100644", "type": "blob",
                 "sha": blob["sha"]})
    print("  %8d B  %s" % (os.path.getsize(f), f))

new_tree = api("POST", "/git/trees", {"base_tree": base_tree, "tree": tree})
commit = api("POST", "/git/commits",
             {"message": MSG, "tree": new_tree["sha"], "parents": [base]})
api("PATCH", "/git/refs/heads/" + BRANCH, {"sha": commit["sha"]})
print("pushed: %s" % commit["sha"][:10])

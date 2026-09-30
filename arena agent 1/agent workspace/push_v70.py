#!/usr/bin/env python3
"""Commit the prior-art pass results and the architecture corrections."""
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
    ("arena agent 1/agent workspace/papers/PRIOR_ART_PASS.md",
     "/home/user/papers/PRIOR_ART_PASS.md"),
    ("arena agent 1/agent workspace/papers/SUBMISSION_ARCHITECTURE.md",
     "/home/user/papers/SUBMISSION_ARCHITECTURE.md"),
]

MSG = r"""Prior-art pass on units 2-6: all five survive; correct two false measurements in the architecture

THE MEASUREMENT THAT MOTIVATED THIS PASS WAS WRONG. The architecture recorded 0 words of
prior art for units 2-6. Direct measurement of the source heads refutes it entirely:

  unit 2  1,493 w    unit 3  1,680 w    unit 4  1,321 w    unit 5  709 w    unit 6  921 w
  (previously recorded as 0, 0, 0, 0, 0)

Every unit has a real Related work section. TWO CONSEQUENCES:
  1. THE GROUND "FOLDING CANNOT PRODUCE A PRIOR-ART SECTION" IS STRUCK from the case for
     keeping units 1-5 separate. There was no missing section to produce. That ground is
     marked STRUCK in the architecture; the separation now rests on disjointness alone
     (0.0% sentence overlap obstr<->psuff/comp/ebc), which is sufficient on its own.
  2. THIS WAS NEVER A DRAFTING EXERCISE. Prior art existed and had not been checked against
     the literature -- which is the novelty test as originally specified. Units 2-6 were
     therefore tested, not written.

NOVELTY TEST RESULTS (full record in PRIOR_ART_PASS.md):

  unit 2  PASSES   No additions.
  unit 3  PASSES   No additions.
  unit 4  PASSES   Optional: surface Caratheodory/Helly attribution in the related work.
  unit 5  SURVIVES Two real gaps.
  unit 6  SURVIVES Two real gaps.

NO UNIT WAS REPOSITIONED, COMBINED, OR DROPPED. THE ATTRITION BUDGET WAS NOT DRAWN ON.

UNITS 2, 3, 4 HAD ALREADY ANTICIPATED THE CLASSICAL OBJECTIONS. Unit 4 concedes the
discriminating-kernel collision in its own words -- "that is a real collision with prior art
and is conceded here rather than argued around" -- cites Sion 1958 and disclaims originating
the minimax equality, and credits Caratheodory (R^k) and Helly 1923 for the k+1 support bound
and its tightness in the body. Unit 3 engages Saint-Pierre 1994, the level-set and Lagrangian
routes, the moment-SOS programme (Lasserre 2001, Parrilo 2003) with three concrete
differences, the scenario approach (Calafiore and Campi; Campi and Garatti) as probabilistic
versus worst-case, and shows the Helly-type bound FALSE for a common blind control function.
Unit 2 positions itself item by item against Veliov 1993 and Luc Doyen 2000, and pre-empts
both distributionally robust POMDPs (Nakao, Jiang and Shen 2021) and safe RL shielding
(Alshiekh et al. 2018). Both objections I went looking for were already answered in source.

UNIT 6 GAPS. (a) KUHN'S THEOREM IS ABSENT -- grep: "Kuhn" 0, "perfect recall" 0, "behavior" 0.
Theorem 9 says blending over plans works but alternation over time does not; in game theory
these are mixed and behavioural strategies, equivalent under perfect recall by Kuhn 1953. The
contradiction is superficial -- Kuhn equates distributions over paths under expected payoff,
while this constraint is path-wise -- but the paper never says so, and Main and Randour (Games
and Economic Behavior 2024, arXiv:2201.10825) show Kuhn crumbles under finite memory, which is
this paper's setting and SUPPORTS Theorem 9. (b) WEI, N. AND ZHANG, P. 2024, "Adjustability in
robust linear optimization", Math. Program. 208(1-2), 581-628, DOI 10.1007/s10107-023-02049-w,
verified via Crossref, gives a necessary and sufficient theorem-of-the-alternatives condition
for adjustability to be zero -- the same quantifier question from the opposite face. The paper
attributes that characterization to Bertsimas and Goyal 2012, which is about affine policies.

UNIT 5 GAPS. (a) The antichain ALGORITHMS literature is uncited -- De Wulf, Doyen, Henzinger
and Raskin (CAV 2006, LNCS 4144, 17-30) proved the exponential compression in general form in
2006, and Doyen's programme covers games of imperfect information where "the set of winning
belief states is downward-closed... we only store the maximal elements", which is unit 5's
instrument verbatim. (b) HARPER'S THEOREM governs the m=5 result -- "the maximal sets are the
32 radius-one balls" is a Hamming-ball extremal statement and hypercube vertex isoperimetry
governs exactly that, yet neither Harper nor any isoperimetric result is cited. (c) The
abstract ("it scales further than the relaxing instinct expects") is looser than the body
("this paper proves no new theorem about antichains... a computation on one instance").

TWO CROSS-CUTTING STRUCTURAL FINDINGS. Two source heads are \part-structured CONTAINERS each
holding TWO architecture units: paper06_v66 = unit 6 (Part I, 25,443 w) + unit 9 (Part II,
33,267 w, 91.6% sentence-identical to paper10_v53); paper05_v15 = unit 5 (Part I, 6,297 w) +
unit 11 (Part II, 11,142 w, 67.4% sentence-identical to paper11c_v2). In both cases the parts
share 0 sentences with each other. BOTH MUST BE SPLIT before any merge is re-run or any
unit-level edit is applied, or unit 9 and unit 11 content will be silently carried into
units 6 and 5.

ALSO CORRECTED: the "screening is shallow" line. It invited the reading that the standard is
lower under preprints.org. It is not. Restated as a claim about WHO checks rather than HOW
MUCH checking is owed: the objective remains valid, accurate, correct science, no erroneous
mathematics and no erroneous prose; because no one else will catch those defects, we are the
only ones who can.
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

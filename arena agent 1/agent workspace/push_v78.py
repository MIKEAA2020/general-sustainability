#!/usr/bin/env python3
"""Commit: extend the prior-art pass to units 7-11; fix unit 5's constrained-POMDP gap."""
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

FILES = ["papers/paper05_exact_belief_computation_v16.tex",
         "papers/PRIOR_ART_PASS.md"]

MSG = r"""Unit 5: cite the constrained/chance-constrained POMDP literature; begin the units 7-11 pass

The ratified prior-art pass covered units 2-6. Units 7-11 had never been tested. Measuring them
first: per-paper related-work sections run 398-638 words (unit 7: 508; unit 8: 606/638/586
across its three merged papers; unit 9: 509; unit 10: 526/424; unit 11: 398), against 709-1,680
for units 2-6. Read, they are substantive rather than stubs -- each names its founding
literature and states what it adds. Unit 9 cites Brunner and Rechberger (2016) and Sterner and
Elser (2002) and says the contribution "is therefore not a new way to close a balance but a
typing discipline that rules out a class of aggregations"; unit 11 cites Aubin (1991), the
ARCH-COMP benchmark literature, and Farkas, Helly and max-plus algebra, stating "none of these
is contributed here".

Re-reading unit 5 against its own central object surfaced a gap the first pass missed. Unit 5
computes V_k(b), "the maximal probability of remaining safe for k steps" -- precisely the
objective of the constrained and chance-constrained POMDP literature. It cited the POMDP
ALGORITHMS literature (Lovejoy 1991; Pineau, Gordon and Thrun 2003; Shani, Pineau and Kaplow
2013 -- all on point-based value iteration) but NOTHING on constrained formulations; "constrained"
appeared zero times in the file. So the paper engaged the literature on how to compute
belief-space values approximately and not the literature on the objective it computes.

FIXED. New subsection "Constrained and chance-constrained POMDPs" (label scale-cpomdp), before
"Mechanized verification". Names Altman (1999) for constrained MDPs; Poupart et al. (2015),
Undurti and How (2010) and Santana et al. (2016) for constrained POMDPs; Ono et al. (2015) for
chance-constrained dynamic programming. Separates on three axes: those formulations OPTIMISE
OVER POLICIES subject to a constraint, whereas V_k(b) is the value FUNCTION studied as an
object; their constraint is a FEASIBILITY THRESHOLD, whereas the result here is the
probability's SHAPE (the piecewise-linear alpha-vector support and the antichain structure); and
every one of those methods is APPROXIMATE, whereas nothing here is. Closes by stating the
question is not new and the paper does not claim it is.

All five citations Crossref-verified before insertion, per the standing rule that none enters a
source file unverified:

  Altman, E., 1999. Constrained Markov Decision Processes. Chapman & Hall/CRC.
      doi:10.1201/9781315140223 (2021 CRC reprint; Crossref indexes the reprint, not the
      original, and the entry cites 1999 carrying the reprint DOI)
  Poupart, Malhotra, Pei, Kim, Goh and Bowling, 2015. AAAI 29(1). doi:10.1609/aaai.v29i1.9655
  Santana, Thiebaux and Williams, 2016. AAAI 30(1). doi:10.1609/aaai.v30i1.10423
  Undurti and How, 2010. ICRA 2010, 3966-3973. doi:10.1109/robot.2010.5509743
  Ono, Pavone, Kuwata and Balaram, 2015. Autonomous Robots 39, 555-571.
      doi:10.1007/s10514-015-9467-7

UNIT 5 SURVIVES. Its contributions -- exact rational arithmetic, the support identity, the
antichain structure of the alpha-vectors, the exhaustive classification -- are untouched by this
literature, which is uniformly approximate. No repositioning, and the attrition budget is still
not drawn on.

Verified after the edit: braces +0; document/abstract/enumerate/itemize balanced; no dangling
\ref; all five in-text citations resolve to bibliography entries; 7,580 -> 8,101 words.

Compilation remains unverified -- no LaTeX toolchain obtainable this session.

Next: the units 7-11 sweep itself. Section 7.1 of PRIOR_ART_PASS.md came from re-reading unit 5,
not from that sweep, which has only reached the measurement stage recorded above.
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

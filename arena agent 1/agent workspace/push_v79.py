#!/usr/bin/env python3
"""Commit: prior-art sweep of units 9 and 11 -- gaps found and fixed."""
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

FILES = ["papers/paper10_depletion_ledgers_v53.tex",
         "papers/paper11c_worked_systems_audit_v2.tex",
         "papers/PRIOR_ART_PASS.md"]

MSG = r"""Prior-art sweep: units 9 and 11 tested, gaps found and fixed

Two more units of the 7-11 sweep, run as a novelty test.

UNIT 9 (paper10_depletion_ledgers_v53) otherwise covers its ground well. A bibliography check
found Tilton (2), Redner, Daly, Neumayer, Munda (2), Ekins, Hubbert (2), Bartlett, Sterner and
Brunner (2) all cited -- reserve-life criticism, first-passage processes, ecological economics,
noncompensatory aggregation, MFA and stoichiometry.

But its third objective is to "formalize weak and strong sustainability not as irreconcilable
ethical doctrines, but as two distinct operating regimes", and its Weak Sustainability Regime
bullet describes exactly the substitutability assumption Solow and Hartwick formalized -- while
citing only Daly (1990), Neumayer (2013) and Ekins (2003). "Solow" and "Hartwick" appeared zero
times. The weak-sustainability criterion (a non-declining consumption path sustained by investing
resource rents in reproducible capital) is the canonical origin of precisely the regime the bullet
defines.

Fixed by adding the origin at the claim site and distinguishing rather than merely naming: the
ledger "does not dispute that criterion; it makes its precondition checkable, since whether
material loops close at the rate of throughput is a property of the incidence structure that the
aggregate criterion presupposes and does not itself test."

Crossref-verified: Solow, R.M. (1974), Review of Economic Studies 41, 29-45, doi:10.2307/2296370.
Hartwick's 1977 American Economic Review original is NOT indexed by Crossref; the entry cites the
original and carries the DOI of the verified 2017 Routledge reprint (The Economics of
Sustainability, 63-65, doi:10.4324/9781315240084-4). That discrepancy is recorded rather than
smoothed over.

Unit 9 SURVIVES: the typed ledger, the three certification layers, the no-nonnegative-weighting
theorem, the double-counting rules and the reclassification of three public indicators are all
untouched by Solow-Hartwick, which the paper now uses as the frame it makes checkable rather than
as a competitor.

UNIT 11 (paper11c_worked_systems_audit_v2) had the thinnest prior art at 398 words. It cited
Aubin (1991) for viability theory's founding move, the ARCH-COMP benchmark literature, and the
classical instruments (Farkas, Helly, max-plus), and handled its own positioning honestly --
disclaiming superiority over interval arithmetic as "a statement about the verification pipeline
and not a claim of superiority over validated or interval-arithmetic approaches".

But several audits tabulate viability kernels -- "kernel sizes 24, 26, 25, and 28 of 36 belief
pairs" -- and the literature on COMPUTING viability kernels was entirely uncited.

Fixed with a new paragraph, "Computing viability kernels", naming Saint-Pierre's
backward-reaching-set algorithm with its convergence property (Saint-Pierre, 1994) and the
support-vector approximation of kernels and resilience values (Deffuant, Chapel and Martin,
2007). Separates on two axes: those methods address FULLY OBSERVED dynamics in continuous or
large discrete spaces, where exact computation is infeasible and the honest goal is a guaranteed
approximation, whereas these audits are exact in rational arithmetic with no approximation error
to bound; and their objects are kernels over states, not the observation-constrained kernels over
BELIEF PAIRS tabulated here. Closes by naming what does transfer -- the question of which states
admit a constraint-satisfying control, and the finding that the answer is not monotone in the
observation structure, which is a statement about the observation layer those methods do not
model.

Crossref-verified: Saint-Pierre, P. (1994), Applied Mathematics & Optimization 29, 187-209,
doi:10.1007/bf01204182. Deffuant, G., Chapel, L. and Martin, S. (2007), IEEE Transactions on
Automatic Control 52(5), 933-937, doi:10.1109/tac.2007.895881.

Unit 11 SURVIVES: it is an audit paper, and its contribution is the exact tabulation, which is
precisely what the approximated methods cannot supply.

Verified after both edits: braces +0 in both files; environments balanced; no dangling \ref; all
four new citations resolve to bibliography entries. Unit 9 32,782 words; unit 11 11,730 -> 12,003.

SWEEP STATUS: units 5 (revisited), 9 and 11 tested; one gap in each, all three fixed. No unit
repositioned, combined or dropped -- the attrition budget is still undrawn after two passes.
Units 7, 8 and 10 remain, measured but not yet tested. Compilation still unverified.
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

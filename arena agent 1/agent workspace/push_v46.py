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
    ("arena agent 1/agent workspace/papers/paper02_probabilistic_sufficiency_v12.tex",
     "/home/user/papers/paper02_probabilistic_sufficiency_v12.tex"),
    ("arena agent 1/agent workspace/papers/PAPER02_PRIOR_ART.md",
     "/home/user/papers/PAPER02_PRIOR_ART.md"),
]

MSG = """Paper 2: prior-art section added; three verified references added

MEASURED FIRST. The bar verdict "prior art: no" for paper 2 was measured on the
stale v10, so it was re-measured on v11 -- and it HOLDS:
  paper 1  6,197 ref chars, 38 years, 72 author-initials, PRIOR-ART SECTION yes
  paper 2  2,729 ref chars, 12 years, 21 author-initials, PRIOR-ART SECTION no
  paper 3  2,908 ref chars, 15 years, 23 author-initials, PRIOR-ART SECTION no
  paper 4  2,194 ref chars, 10 years, 10 author-initials, PRIOR-ART SECTION no
Papers 2/3/4 have bibliographies but no positioned argument.

THE FOUR REFERENCES NAMED IN THE EARLIER TODO: all VERIFIED against publisher
records before use, and all three missing ones were ABSENT from the
bibliography:
  Veliov, V.M., 1993. Sufficient conditions for viability under imperfect
    measurement. Set-Valued Analysis 1, 305-317. DOI 10.1007/BF01027640.
    Gives a SUFFICIENT condition for an output feedback regulation map.
  Luc Doyen, 2000. Guaranteed output feedback control for uncertain systems
    under control and state constraints. Set-Valued Analysis 8, 149-162.
    NECESSARY AND SUFFICIENT -- but only over LIPSCHITZ MEMORYLESS closed
    loops u(h(x,w)), for EXACT maintenance of a closed domain.
  Cardaliaguet, Quincampoix & Saint-Pierre, 2007. Differential games through
    viability theory. Advances in Dynamic Game Theory, Ann. ISDG 9, 3-35.
  Austrom 1965 was already present.

A TRAP AVOIDED. The bibliography already contained a "Doyen" -- LAURENT Doyen,
co-author with Chatterjee and Henzinger (2009) on qualitative POMDPs. That is a
DIFFERENT PERSON from LUC Doyen, the viability theorist of the 2000 paper. Both
are now cited and the text distinguishes them explicitly with a parenthetical
warning. Merging them would have been a visible error.

THE POSITION, which the two viability neighbours delimit precisely:
  vs Veliov (1993): his condition is sufficient only, so its failure is
    inconclusive. Paper 2's is necessary as well, so failure is informative.
  vs Luc Doyen (2000): he ALREADY HAS necessary and sufficient, so exactness
    alone is not the delta. The delta is twofold: (i) his loops are Lipschitz
    and memoryless, the recursion here admits HISTORY-DEPENDENT policies with
    the feedback/blind distinction strict (rem:feedback-strict); (ii) his
    criterion is exact maintenance of a closed domain, the safety value here is
    QUANTITATIVE with the deficit bound 1 - V_k(b) >= min b(x).

CLAIMED (five items): exact sufficiency (thm:support); history-dependent
policies with the repaired reading machine-checked; the quantitative deficit
(prop:deficit); the alpha-vector structural identification as Sperner-bounded
antichains (prop:antichain), class lattice (thm:lattice) and parametric closed
forms; Lean 4 machine-checking with the Sperner bound of prop:antichain(iii)
CITED NOT FORMALIZED.
NOT CLAIMED: belief-state reduction (Astrom), alpha-vector representation as
such (Smallwood & Sondik), qualitative complexity landscape (Chatterjee,
Laurent Doyen & Henzinger), hardness results (Papadimitriou & Tsitsiklis;
Lovejoy).

CHECKS: all 38 \ref targets resolve, 46 labels defined, zero missing. Every
cited label verified to exist.

paper02_probabilistic_sufficiency_v12.tex: 12,753 -> 14,155 words.
Papers 3 and 4 remain; paper 4 is the thinnest and the higher risk.
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

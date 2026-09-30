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
    ("arena agent 1/agent workspace/papers/paper10_depletion_ledgers_v52.tex",
     "/home/user/papers/paper10_depletion_ledgers_v52.tex"),
    ("arena agent 1/agent workspace/papers/paper10b_edwards_aquifer_v1.tex",
     "/home/user/papers/paper10b_edwards_aquifer_v1.tex"),
    ("arena agent 1/agent workspace/papers/PAPER10_SPLIT_AND_PRIOR_ART.md",
     "/home/user/papers/PAPER10_SPLIT_AND_PRIOR_ART.md"),
]

MSG = """Paper 10: split into two papers; Part II recovered from dead text; prior art added

SYSTEMIC DISCOVERY. Scanning the whole set for the paper-9 failure mode found it
twice more:
    paper09_cod_certification_v30.tex        2 docs  (fixed last turn)
    paper10_depletion_ledgers_v51.tex        2 docs  (fixed here)
    paper11_forecasting_baselines_v61.tex    3 docs  (STILL OUTSTANDING)
Papers 1-8 are clean. In every case the \part merge marker (E2/Arv, E4, E3/Ws)
sits in the GAP BETWEEN DOCUMENTS -- outside any document -- which is why the
merge never worked.

PAPER 10'S DEFECT. v51 was two complete LaTeX documents and did NOT COMPILE AT
ALL.
    Part I : \documentclass @ 1686,  \end{document} @ 235852, 34258 words,
             "Typed Flux Ledgers and Depletion Arithmetic"
    Part II: \documentclass @ 236809, \end{document} @ 299278, 8530 words,
             "Governance operators and viability kernels of the Edwards
              Aquifer: a J-17 test"
COMPILE PROOF (tectonic, figures stubbed):
    v51 (merged)  NO PDF,      0 bytes
    v52 (Part I)  55 pages, 393179 bytes
    v1  (Part II) 17 pages, 131022 bytes
Both new files: ZERO undefined references, ZERO LaTeX errors.

WHY SPLIT, ON CONTENT AND MERIT. Zero overlap on every distinctive term:
                          Part I    Part II
    ledger/typed/compartment 135/35/79    0/0/0
    stoichiometric/phosphate   15/19      0/0
    flux/conservation          89/66      1/3
    Edwards/J-17/pumping        0/0/0    22/14/70
    trigger/governance op       1/0       36/4
Part I never mentions Edwards; Part II never mentions ledgers. Part I is a
general typed stock-flow accounting framework (moieties, conservation,
componentwise deficits, depletion arithmetic across groundwater, phosphate and
fisheries). Part II is a single-aquifer empirical viability-kernel study.

PRIOR ART, PART I (v52). New \subsection*{1.4 Related work}.
  1 Material/substance flow analysis (NEW): Brunner & Rechberger 2016, Handbook
    of Material Flow Analysis, 2nd ed., CRC Press. What is added is TYPING --
    conserved moieties tracked independently and never summed across types, so
    the central negative result (compensatory scalar aggregation masks critical
    physical deficits) is a PROHIBITION ON A STEP MFA ROUTINELY PERFORMS. Not a
    new way to close a balance; a typing discipline.
  2 Ecological stoichiometry (NEW): Sterner & Elser 2002, Princeton UP. The
    moiety bookkeeping and stoichiometric conservation are the same idea carried
    into depletion accounting; Redfield-type ratios are the canonical instance.
  3 Reserve-life / R:P / "time to depletion" (NEW): Hubbert 1956, Drilling and
    Production Practice, API, 1-57; Bartlett 2000, Math. Geol. 32(1), 1-17.
    Positioning: the confusion is not a property of one badly-behaved indicator
    but a SYMPTOM OF LEAVING THE INDICATOR UNTYPED.
  5 Two-cell aquifer modelling (NEW): Augeraud-Veron & Pereau 2022 -- a one-cell
    bathtub model allocates too much water to extraction at the expense of
    groundwater-dependent ecosystems. Direct antecedent of the two-pool gap.

PRIOR ART, PART II (v1). New \subsection{Related work}.
  1 THE REGULATORY OBJECT. Verified against EAA and EARIP documents: the J-17
    index well is the official regulatory trigger for Critical Period
    Management, and the paper's 660-ft level IS THE REAL STAGE I TRIGGER
    (J-17 < 660 ft MSL -> 20% withdrawal reduction, San Antonio Pool, 40% at
    Stage IV; Uvalde Pool staged separately on J-27; permitted withdrawals
    capped at 572,000 ac-ft/yr). The results therefore read directly as a
    statement about the instrument in force.
  2 Viability applied to groundwater (NEW): Pereau, Pryet & Rambonilaza 2019,
    Ecol. Econ. 161, 109-120; Pereau, Mouysset & Doyen 2018, Environ. Resour.
    Econ. 71(2), 319-336; Oubraham & Zaccour 2018 survey. What is added is the
    ROBUST element and the geometry of the trigger -- kernels against a
    persistent drought-floor recharge, and the negative finding that nothing is
    retained at 660 ft because the rules are invisible to the kernel of their
    own trigger. A different question from the one that literature asks.
  3 SAFE YIELD: A CONSPICUOUS OMISSION, NOW ENGAGED. The term "safe yield"
    appears ZERO times in this manuscript, yet the safe-yield critique is the
    classical groundwater-sustainability literature most directly analogous to
    its central finding. Now cited: Sophocleous 1997, Ground Water 35(4), 561;
    Alley, Reilly & Franke 1999, USGS Circular 1186; Sophocleous 2000,
    J. Hydrology 235, 27-43; Alley & Leake 2004, Ground Water 42(1), 12-16;
    Devlin & Sophocleous 2005, Hydrogeol. J. 13, 549-554. The paper's finding
    -- a positive attractor-to-threshold margin defeats every non-negative
    pumping rule, so 660 ft is protected by wet years rather than by policy --
    is identified as THE ROBUST-VIABILITY ANALOGUE OF THE SAFE-YIELD CRITIQUE.

VERIFICATION: both files have exactly 1 \documentclass, 1 \begin{document},
1 \end{document} after stripping comments. All \ref targets resolve. Compiled:
55pp and 17pp, zero errors, zero undefined references. The single "not found"
log line in each is the benign pdftexcmds info message about \pdfdraftmode.
Stub figures created only under /tmp/p10; none written into /home/user/papers.

TOOL NOTE: tectonic lost its exec bit again mid-session (Permission denied);
re-chmod +x fixed it. Second occurrence.

NEXT: paper11_forecasting_baselines_v61.tex is THREE concatenated documents --
Northern cod forecasting (20048 w), Edwards Aquifer forecasting (8819 w), and
Exact Audits of Worked Systems for the Obstruction Calculus (10374 w, \part{Ws}).
'ws' is a separate unit in the authoritative eight-paper scope.
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

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
    ("arena agent 1/agent workspace/papers/paper11_forecasting_baselines_v62.tex",
     "/home/user/papers/paper11_forecasting_baselines_v62.tex"),
    ("arena agent 1/agent workspace/papers/paper11b_edwards_forecast_v1.tex",
     "/home/user/papers/paper11b_edwards_forecast_v1.tex"),
    ("arena agent 1/agent workspace/papers/paper11c_worked_systems_audit_v1.tex",
     "/home/user/papers/paper11c_worked_systems_audit_v1.tex"),
    ("arena agent 1/agent workspace/papers/PAPER11_SPLIT_AND_PRIOR_ART.md",
     "/home/user/papers/PAPER11_SPLIT_AND_PRIOR_ART.md"),
]

MSG = """Paper 11: split into THREE papers; 74 pages recovered from dead text; prior art added

THE DEFECT. v61 was THREE complete LaTeX documents concatenated -- 3x
\\documentclass, 3x \\begin{document}, 3x \\end{document}. \\part{E3} and \\part{Ws}
sat in the GAPS BETWEEN DOCUMENTS, outside any document, so nothing past the
first \\end{document} compiled and Parts II and III (141k chars, 19200 words)
were DEAD TEXT.
    D1 139352 chars, 20048 w -- Does a surplus-production ladder improve
                                forecasts of Northern cod?
    D2  64194 chars,  8819 w -- Does a one-pool water-balance model improve
                                forecasts of Edwards Aquifer head?
    D3  74770 chars, 10374 w -- Exact Audits of Worked Systems for the
                                Obstruction Calculus
COMPILE PROOF (tectonic, figures stubbed):
    v61 (merged)     NO PDF,      0 bytes
    v62 (cod)        41 pages, 240533 bytes
    v1  (Edwards)    21 pages, 134496 bytes
    v1  (Ws)         12 pages, 200939 bytes
All three: ZERO undefined references, ZERO LaTeX errors.

WHY THREE -- THE DECISIVE EVIDENCE. Unlike papers 9 and 10, whose halves had
ZERO cross-reference, D1 and D2 explicitly cite each other as separate
companion papers, each with its own Zenodo DOI:
  D2: "A companion study under separate review applies the same scored design to
      a marine fishery stock (Northern cod, NAFO 2J3KL)... The two systems'
      scores are never pooled, and no retention verdict is transferred between
      them."
  D1: "The same scored design is applied to a groundwater system, the Edwards
      Aquifer, Texas, in Abaee (2026...). The two systems' series are not
      pooled, and no retention outcome is transferred between them."
The author already treats these as separate papers; the concatenation was purely
an assembly artefact. D3 shares no vocabulary with either (forecast 1, scored 0,
ladder 1, Northern cod 0, Edwards 0; versus obstruction 24, witness 12, audit
81). It is 'ws' -- a separate unit in the authoritative eight-paper scope.

PRIOR ART, D1 (v62). Core finding: NO surplus-production module is retained
against last-value persistence on either specification. Cross-domain anchor
(NEW): the M-competitions -- Makridakis, Spiliotis & Assimakopoulos 2018, IJF
34(4), 802-808; 2018, PLoS ONE 13(3), e0194889; 2020, IJF 36(1), 54-74. In M4
all six pure ML methods performed poorly, none better than the combination
benchmark and only one better than Naive2. THE SCOPE DIFFERENCE IS STATED, NOT
CLAIMED AWAY: M4 aggregates 100,000 series and 61 methods; this is one stock
under two specifications. Also positioned against the collapse/non-recovery
literature (Myers, Hutchings & Barrowman 1997; Hutchings 2005) -- that
literature establishes the empirical fact, this paper measures what it does to
FORECAST SKILL from a fixed origin. Explicit non-claim: the predictand is
retrospectively reconstructed with catch supplied along the horizon, so this is
a CONDITIONAL HINDCAST, NOT AN OPERATIONAL FORECAST EVALUATION.

PRIOR ART, D2 (v1). Positioned against groundwater-level forecasting
(Daliakopoulos, Coulibaly & Tsanis 2005; Adamowski & Chan 2011) with the
departure stated: the contribution is NOT a new forecasting model but a LOCKED
EVALUATION DESIGN applied to a familiar model family, the negative result being
the finding -- ladder, baselines and rule fixed before any score was read, and a
protocol clause declines the best one-step forecaster (M2m). THE MECHANISM IS
NAMED: annual recharge is near-white (r(R_t,R_{t-1}) = 0.17) while the head
increment is strongly coupled to contemporaneous recharge (r(dH,R) = 0.74), so a
model that persists last year's recharge persists a quantity with almost no
memory; given realised fluxes the same map nowcasts well (7.55 ft), separating a
forecasting failure from a structural one. Added Hyndman & Koehler 2006 and
Makridakis & Hibon 2000.

PRIOR ART, D3 (v1) -- THE LARGEST GAP IN THE SET. This half's bibliography had
SIX SURNAMES TOTAL -- Abaee, Baccelli, Cohen, Olsder, Quadrat, Wiley -- four of
which are one book. It cited NO viability theory and NO verification
literature. Six verified entries added:
  Aubin 1991, Viability Theory -- the founding framing, previously absent.
  ARCH-COMP (Althoff et al. 2020; Geretti et al. 2020; EPiC Series in Computing
    vol. 74) -- the verification community's annual friendly competition applying
    tools to fixed benchmark problems. This paper's worked-systems family plays
    the analogous role for the obstruction calculus. The difference is stated:
    ARCH benchmarks are reachability problems solved by reachability tools;
    these are information-constrained viability problems under partial
    observation, tabulating survivable belief-pair counts, kernel sizes under
    policy-class restrictions, and minimal witness-set sizes. No reachability
    tool computes these.
  Farkas 1902 (the duality certificate); Helly 1923 (tightness of the sparse
    witness); Baccelli, Cohen, Olsder & Quadrat 1992 (max-plus, already cited,
    now contextualised).

ERROR CAUGHT: a first draft of D1's section referenced \\ref{sec:power} -- a
label I INVENTED, which does not exist in the document. Detected by the
\\ref-vs-\\label check and replaced with plain text before compiling. Had it
shipped it would have produced a ?? in the PDF.

VERIFICATION: all three files have exactly 1 \\documentclass, 1
\\begin{document}, 1 \\end{document} after stripping comments. All \\ref targets
resolve (2, 0 and 29 refs). Compiled: 41, 21 and 12 pages; zero errors, zero
undefined references. Stub figures created only under /tmp/p11; none written
into /home/user/papers.

This closes the systemic multi-document defect: papers 9, 10 and 11 all split;
papers 1-8 verified clean.
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

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
    ("arena agent 1/agent workspace/papers/paper09_cod_certification_v31.tex",
     "/home/user/papers/paper09_cod_certification_v31.tex"),
    ("arena agent 1/agent workspace/papers/paper09b_arv_certification_v1.tex",
     "/home/user/papers/paper09b_arv_certification_v1.tex"),
    ("arena agent 1/agent workspace/papers/PAPER09_SPLIT_AND_PRIOR_ART.md",
     "/home/user/papers/PAPER09_SPLIT_AND_PRIOR_ART.md"),
]

MSG = """Paper 9: split into two papers; Part II recovered from dead text; prior art added

THE DEFECT. v30 was TWO complete LaTeX documents concatenated, and it did NOT
COMPILE AT ALL.
  Part I  (E2) : \documentclass[11pt]{article} @ char 2790, \end{document} @ 116595
  Part II (Arv): \documentclass[10pt,twocolumn]{article} @ 116643, \end{document} @ 162724
  - \part{E2} and a \paragraph sat at chars 1036-2400, BEFORE the first
    \documentclass -> FATAL "Missing \begin{document}".
  - \part{Arv} sat at char 116612, AFTER the first \end{document} (116595)
    -> LaTeX ignores everything past it. 46,127 chars and 38 labels were DEAD
    TEXT, including ALL 14 labelled results of the merged file.
COMPILE PROOF (tectonic, figures stubbed):
    v30 (merged)  NO PDF, 0 bytes
    v31 (Part I)  35 pages, 203967 bytes
    v1  (Part II)  8 pages, 165922 bytes
Both new files compile with ZERO errors and ZERO undefined references.

WHY SPLIT, ON CONTENT AND MERIT (the user's criterion: "is the work unified
enough to merit a single paper?"). It is not.
                        Part I (E2)   Part II (Arv)
    Schaefer                11              0
    LRP (Part I's object)   87              0
    surplus production       3              0
    exact rational           1             10
    harvest-free             1             17
    breach                   2             27
    labelled results         0             14 (ALL of them)
    mentions of other part   2              0
  Different method: Part I fits Schaefer 1983-2007 in floating point (N=20000
  trajectories, B=2000 bootstrap refits); Part II uses NO FITTED MODEL AT ALL,
  exact rational arithmetic. No shared formalism. Overlapping bibliography is
  DATA SOURCES ONLY (Regular 2025; Schijns 2021), not scholarship. Part II never
  cites Part I. CORROBORATION: 'arv' is a separate unit in the authoritative
  eight-paper scope, and Part II IS arv.
  The framing paragraph's one claimed link (harvest-free contractions evidence
  non-stationarity, hence the constructive bound is regime-dependent) is
  MOTIVATIONAL, NOT LOGICAL -- Part I establishes regime-dependence on its own.
Neither half needed preamble surgery; both were already complete standalone
documents. v30 is preserved untouched.

PRIOR ART, PART I (v31). New \subsection{Related work}.
  1 Viability in fisheries: Aubin 1991; Bene, Doyen & Gabay 2001; Martinet,
    Thebaud & Doyen 2007; Doyen et al. 2012; Krawczyk & Pharo 2013; Krawczyk
    et al. 2013.
  2 Robust viability kernel (NEW): Regnier & De Lara 2015, Environ. Model.
    Assess. 20, 687-698. Their definition is the object Part I computes and
    their "uncertainty shrinks the kernel" finding is what Part I is built
    around. What is new is HOW it is obtained: descending set iteration there
    versus a COLLAPSE TO ALGEBRA here -- two constants C* = g(LRP) - |e| = 91.59
    kt and g_max - |e| = 215.2 kt reproduce the kernel table in closed form, and
    every rule's protection margin is exactly C* minus its catch.
  3 Harvest control rules / MSE (NEW): Butterworth 2007, ICES J. Mar. Sci. 64,
    613-617; Punt et al. 2016, Fish Fish. 17, 303-334. The delta is stated
    without rhetoric: an MSE verdict is CONDITIONAL on the operating model and
    the simulated ensemble; the no-dominance verdict here falls out of an
    IDENTITY and holds for every rule in the class, including rules never
    simulated. THE NARROWING IS CONCEDED -- MSE handles multiple objectives,
    implementation error and observation error at once, which the scalar
    reduction gives up.

PRIOR ART, PART II (v1). New \section{Related work}.
  THE TENSION, NAMED RATHER THAN BURIED. Part II certifies collapse steps as
  HARVEST-FREE contractions, which looks like it contradicts:
    Hutchings & Myers 1994, CJFAS 51, 2126-2146 -- collapse attributable SOLELY
      to overexploitation;
    Myers & Cadigan 1995, CJFAS 52, 1274-1285 -- did NOT support the natural-
      mortality hypothesis; overfishing sufficient to cause the collapse;
    Myers, Hutchings & Barrowman 1997, Ecol. Appl. 7(1), 91-106 -- rejected
      juvenile mortality being unrelated to fishing mortality.
  Resolution stated precisely: those papers ask about the HISTORICAL CAUSE;
  Part II asks about the ARITHMETIC OF THE RECORD -- was the step a contraction
  even at zero removals. Both hold; removals on a contractionary productivity
  term make things worse, which prop:moratorium says outright.
  WHERE A REAL TENSION REMAINS AND IS NOT RESOLVED: Myers & Cadigan specifically
  declined elevated natural mortality as the explanation. Read as evidence of a
  productivity collapse, the harvest-free contractions sit against that finding,
  and THIS PAPER DOES NOT ADJUDICATE IT -- the certificates are statements about
  transitions as recorded and identify no biological mechanism.
  THE SERIES-DISCREPANCY CONCERN IS MET, NOT ASSUMED AWAY: Myers et al. 1997
  documented VPA-vs-survey divergence from the early 1980s. prop:survey checks
  the raw survey: certified factor 21797/2127417 over 1989-1994, falling 2.6x
  FURTHER than the assessment series. Robust to series choice, stronger in the
  raw survey. Also added Aubin 1991 (Part II's bibliography lacked it);
  Hutchings & Myers 1994 was already present.

VERIFICATION: both files have exactly 1 \documentclass, 1 \begin{document},
1 \end{document}, 1 \maketitle after stripping comments. All \ref targets
resolve (Part I 0/23; Part II 16/38). Compiled: 35pp and 8pp, zero errors, zero
undefined references. Stub figures were used only under /tmp for the compile
check; none was written into /home/user/papers.

CAUTION ON ONE EARLIER COUNT: a first recount reported Part I as having 2
\begin{document} and 3 \end{document}. That was a FALSE POSITIVE -- the
provenance comment I had just added mentions those control sequences. Recounting
with comments stripped gave 1/1/1/1. Same failure family as the retracted
paper-6 'sorry' grep.

Papers 10 and 11 remain.
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

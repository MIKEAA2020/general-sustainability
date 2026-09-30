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
    ("arena agent 1/agent workspace/papers/PAPERS_RESTRUCTURED.md",
     "/home/user/papers/PAPERS_RESTRUCTURED.md"),
]

MSG = r"""Add PAPERS_RESTRUCTURED.md: manifest of the fifteen-to-seven restructure

Records the final structure, the correction to the earlier eight-way plan, the evidence
behind placing paper 10b with 9+9b rather than 6+10, the two results that only exist
because of the merges, and the merge-machinery failure modes.

THE SEVEN (all compile with tectonic at 0 errors, 0 undefined references):
  1 paper01_obstruction_calculus_v62.tex          1+2        35 pp  38,565 w
      The set-valued and probabilistic readings are the SAME OBJECT AT TWO RESOLUTIONS.
  2 paper03_computational_certification_v15.tex   3+4        24 pp  23,411 w
      OBSTRUCTION CERTIFICATES ARE SMALL -- sized by the decision variables, not the
      uncertainty.
  3 paper05_exact_belief_computation_v15.tex      5+11c      21 pp  18,963 w
      EXACTNESS IS THE INSTRUMENT, NOT THE LIMITATION -- it scales, and it bites.
  4 paper06_assessment_separation_v66.tex         6+10      122 pp  65,390 w
      Aggregation is a REPRESENTATION ERROR WITH A GEOMETRIC SIGNATURE, not a doctrine.
  5 paper08_governance_delay_v46.tex              8+7        90 pp  49,255 w
      Institutional latency decides stability -- and THE REPRESENTATION CHANGES THE
      ANSWER.
  6 paper09_cod_certification_v32.tex             9+9b+10b   68 pp  34,451 w
      CERTIFICATION HAS A HORIZON, set by the fitted map, not by the method.
  7 paper11_forecasting_baselines_v64.tex         11+11b     64 pp  31,100 w
      PROCESS-BASED MODELS ARE NOT SELF-JUSTIFYING.
261,135 words. Every merge is a NEW VERSION; no source overwritten; all prior versions
remain on disk. No content lost or condensed: each Part body reproduced verbatim INCLUDING
ITS ORIGINAL ABSTRACT, and every merged file is larger than the sum of its parts.

CORRECTION TO THE EARLIER PLAN. The eight-way partition proposed earlier listed a "paper
12" THAT DOES NOT EXIST and OMITTED PAPER 10b (Edwards Aquifer viability kernels). The
real corpus is fifteen papers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 9b, 10, 10b, 11, 11b, 11c. The
corrected partition is SEVEN papers, not eight, and -- with 10b placed by evidence rather
than convenience -- NO PAPER IN THE CORPUS NOW DRAWS ITS CONCLUSION FROM A SINGLE SYSTEM.

HOW 10b WAS PLACED (the one judgement call asked for). It joins 9 + 9b, not 6 + 10.
Viability kernels: 9+9b yes, 6+10 no, 10b 12 mentions (66 "kernel"). Retention protocol
frozen before scoring: 9+9b yes, 6+10 no, 10b 24 mentions of "retention". Ledger /
aggregation theory: 9+9b no, 6+10 yes, 10b ZERO. The structural reason is stronger: paper
9b applies the viability machinery to a real assessment record (Northern cod) and paper 10b
performs THE SAME MOVE ON A DIFFERENT SYSTEM -- the two-system replication the audit
identified as missing. Paper 10b also names its own limit ("the scored comparison on one
measured system"); merging removes that limit rather than leaving it standing.

TWO RESULTS THAT ONLY EXIST BECAUSE OF THE MERGES. (1) CERTIFICATION HAS A HORIZON: paper
9's certified layer is finite (six years under the two harsher floors, seven under the
informative one) because the map is expansive at the reference point; paper 10b's every
positive-pumping certified kernel is empty beyond three years, "an optimistic bound on a
defect the out-of-sample audit exceeds." Two systems, unrelated hydrologies, the same shape
of limitation. Neither paper could state this; together it is the paper's thesis. (2) THE
REPRESENTATION CHANGES THE ANSWER: paper 7's operator contrast and paper 8's
discretisation artefact are one phenomenon seen from two formalisations, yielding the
discipline the field is missing -- a stability claim about a reviewed resource is not
interpretable until the decision clock is declared, and the operator axis and the parameter
axis are different axes.

MERGE MACHINERY. All merges run through p5/mergelib.py with per-merge configs and a
build.py harness that stubs missing figures so tectonic can run. Eight distinct failure
modes found and fixed centrally. The one worth carrying forward: EVERY STRUCTURAL SEARCH
IN THIS CORPUS MUST BE COMMENT-AWARE -- provenance headers literally mention the commands
they describe ("It contained 2x \documentclass, 2x \begin{document} ..."). This bug
appeared in FIVE DIFFERENT FORMS, most recently inside merge_preamble, where a plain rfind
matched inside a comment and injected a package block mid-comment, turning the comment's
continuation lines into live LaTeX. Others: \newtheorem and \usepackage must be
de-duplicated BY NAME, not by literal line; declarations blocks carry \ref while defining
no \label, so namespacing must be given the part's label set explicitly; reference lists
are sometimes wrapped in size groups whose delimiters survive an alphabetical sort as
unbalanced braces, and a cleanup rule added to fix that silently ate the closing brace of
\end{document}.

WHAT REMAINS. The merges create the room for broader claims; they do not write them. THE
CLAIM-CLOSING PASS ACROSS ALL SEVEN IS STILL OUTSTANDING -- per the user, next prompt.
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

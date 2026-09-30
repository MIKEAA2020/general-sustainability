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
    ("arena agent 1/agent workspace/papers/paper09_cod_certification_v32.tex",
     "/home/user/papers/paper09_cod_certification_v32.tex"),
    ("arena agent 1/agent workspace/papers/PAPER_MERGE_09_9B_10B.md",
     "/home/user/papers/PAPER_MERGE_09_9B_10B.md"),
    ("arena agent 1/agent workspace/p5/merge_09_9b_10b.py",
     "/home/user/p5/merge_09_9b_10b.py"),
    ("arena agent 1/agent workspace/p5/mergelib.py",
     "/home/user/p5/mergelib.py"),
]

MSG = r"""Merge paper 9 + 9b + 10b: certification, not simulation, on two real systems

THE PLACEMENT DECISION, AND WHY (asked to judge on merits). Two options were on the table
for paper 10b (Edwards Aquifer): join 9+9b, or join 6+10. IT JOINS 9 + 9b. The evidence is
textual and decisive: viability kernels -- 9+9b yes, 6+10 no, 10b 12 mentions (66 "kernel");
retention protocol frozen before scoring -- 9+9b yes, 6+10 no, 10b 24 mentions of
"retention"; ledger/aggregation theory -- 9+9b no, 6+10 yes, 10b ZERO. 10b is a
viability-kernel study under a frozen retention protocol: that is 9b's machinery, not paper
10's. Placing it with 6+10 would have put a viability-kernel paper inside an
aggregation-theory paper on the strength of both being about groundwater accounting. The
stronger reason is structural. Paper 9b opens: "The viability machinery of the obstruction
calculus has been developed and validated on deliberately small exact instances. This paper
applies it to a real assessment record -- the Northern cod stock." Paper 10b performs THE
SAME MOVE ON A DIFFERENT SYSTEM: robust viability kernels of the Edwards Aquifer J-17
record. So 9b and 10b are one operation on two different real systems -- exactly the
two-system replication the task-59 audit identified as missing across the corpus. Paper 10b
also names its own limitation in its conclusion: "the scored comparison on one measured
system." Merging removes that limitation rather than leaving it standing.

THE UNIFYING FINDING. The three parts certify rather than simulate, on two real assessment
records with no hydrology, no biology and no institutional history in common. The finding
they establish jointly and none establishes alone: CERTIFICATION HAS A HORIZON, AND THE
HORIZON IS SET BY THE FITTED MAP, NOT BY THE METHOD. Part I (paper 9): the map is expansive
at the reference point for every admissible carrying capacity K >= 2K*, so the certified
layer has a finite horizon -- six years under the two harsher floors, seven under the
informative one. Part III (paper 10b): every positive-pumping certified kernel is empty
beyond three years, "an optimistic bound on a defect the out-of-sample audit exceeds." The
two numbers differ by a factor of two and come from unrelated systems, which is why the
recurrence is a finding rather than a property of one fit. A CERTIFIED VERDICT IS VALID
OVER A STATED HORIZON, AND QUOTING IT WITHOUT THAT HORIZON IS QUOTING A DIFFERENT CLAIM --
a discipline simulation does not impose, since a simulation shows a trajectory of some
length and leaves the reader to supply the horizon.

WHAT WAS PRODUCED. paper09_cod_certification_v32.tex, a NEW VERSION; no source modified.
    paper 9  (harvest-protection budget)  29 pp   16,710 words
    paper 9b (regime viability, cod)     ~14 pp    7,056 words
    paper 10b(Edwards viability kernels) ~20 pp    9,326 words
    merged v32                           68 pp   34,451 words
Structure: combined title and abstract; Part I (harvest--protection budget); Part II
(regime viability); Part III (Edwards governance operators); cross-system conclusion;
merged references (50 entries); merged declarations. 83 labels, 0 dangling. Compiled with
tectonic: 68 pages, 0 errors, 0 undefined references.

NOTHING LOST. All three Part bodies reproduced in full and verbatim, each opening with its
own original abstract. Word count EXCEEDS the sum of the parts (34,451 vs 33,092) because
the new front matter, TOC, Part heads and cross-system conclusion are additive. Page count
is the sum of the parts plus the new front matter.

THE GENERAL CLAIM NOW STATED: reference points and management rules are usually defended by
simulation; here the defence is CERTIFICATION -- and the difference is not stylistic. A
simulation shows what happened on the runs that were tried; a certification states WHY,
locates the verdict in a constant, and makes explicit the horizon over which the verdict
holds. Three supporting claims, each stated because each is easy to overstate. (1) The
verdict becomes STRUCTURAL: paper 9's no-dominance verdict is structural, not empirical --
because C* = g(LRP) - |e| = 91.59 kt and any rule's protection margin is exactly C* minus
its catch there, harvest and protection are ONE BUDGET, so a reactive rule cannot out-supply
a flat cap it matches in protection. (2) THE PROTOCOL IS WHAT MAKES A NEGATIVE RESULT
INFORMATIVE: all three parts fix the criterion before any score and all three report
negative results; Part III reports its reactive rules as retained only NOMINALLY together
with the reason (the hybrid criterion's wet-year margin is exactly what the robust class
excludes), and Part II reports which steps do NOT certify. (3) Two design consequences
generalise: where a threshold is protected by the weather rather than by policy, no rule in
the scored family can be credited with protecting it (the 660-ft line is protected by wet
years -- a geometric property of scoring triggers against their own level); and a positive
attractor-to-threshold margin defeats every non-negative pumping rule. Scope is stated once:
each part names its own resolution limit (Part III cannot resolve the marginal caps,
P = 0.41-0.65; Part II certifies some steps and not others). The general claim is not that
certification resolves more than simulation, but that CERTIFICATION STATES WHAT IT RESOLVES
AND OVER WHAT HORIZON.

TWO NEW BUGS (both fixed in mergelib.py). (1) THE COMMENT BUG, FIFTH APPEARANCE, IN
merge_preamble. This function located the insertion point with a plain
rfind('\begin{document}'), which is NOT comment-aware. Paper 9's provenance header literally
says "It contained 2x \documentclass, 2x \begin{document} ...", so the search matched
INSIDE THE COMMENT and injected the package block mid-comment -- turning the comment's
continuation lines into live LaTeX and producing two spurious \begin{document}. Fixed by
using the comment-aware find_real(), with an append-at-end fallback for the normal case
(where split_body() has already removed the real one). This is the same root cause as the
original bug in the 11+11b merge, now found in FIVE FORMS: provenance headers mention the
structural commands they describe, and EVERY structural search in this corpus must be
comment-aware. (2) "Option clash for package geometry": paper 9 and paper 10b both load
geometry with DIFFERENT OPTIONS, so the literal-line comparison did not treat them as
duplicates and both were included. Fixed by de-duplicating \usepackage BY PACKAGE NAME
(skipping a line only when every package it loads is already present, so multi-package lines
with a new member survive) -- the same principle already applied to \newtheorem.

VERIFICATION. Compiled with tectonic: 68 pages, 0 errors, 0 undefined references. Content
checked by PDF text extraction for all three Part markers, all three original abstracts, and
the signature quantities of each part (91.59 kt, 215.2 kt, 615.72 ft, the 660-ft threshold).
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

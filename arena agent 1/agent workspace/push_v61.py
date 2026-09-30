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
    ("arena agent 1/agent workspace/papers/paper05_exact_belief_computation_v15.tex",
     "/home/user/papers/paper05_exact_belief_computation_v15.tex"),
    ("arena agent 1/agent workspace/papers/PAPER_MERGE_05_11C.md",
     "/home/user/papers/PAPER_MERGE_05_11C.md"),
    ("arena agent 1/agent workspace/p5/merge_05_11c.py",
     "/home/user/p5/merge_05_11c.py"),
    ("arena agent 1/agent workspace/p5/mergelib.py",
     "/home/user/p5/mergelib.py"),
]

MSG = """Merge paper 5 + paper 11c: exactness is not the limitation

WHY THIS MERGE. Both papers are exact-arithmetic papers, and each supplies the thing the
other lacks.
  PART I (paper 5, computation at scale): takes the exact discipline into the
    curse-of-dimensionality regime and shows it survives -- 1,048,576 subset evaluations
    collapse to 496 sets, and at five parameters 68,719,476,736 collapse to 1,552.
  PART II (paper 11c, exact audits): applies one exact audit framework to a family of
    worked systems and shows exactness is what produces the counter-intuitive verdicts --
    a review-timing identity that is NON-STRICT, a monitoring target on which NO COARSEST
    ADEQUATE PARTITION EXISTS, and two middle cells that are simply incomparable.
A method that scales is not thereby shown to produce surprising verdicts, and a collection
of surprising exact examples is not thereby shown to survive dimensionality. Together they
close both objections normally raised against exact methods: that they are confined to
toys, and that they are a stylistic preference rather than a source of results.

WHAT WAS PRODUCED. paper05_exact_belief_computation_v15.tex, a NEW VERSION; neither source
modified.
    paper 5 (at scale)  13 pp    6,435 words
    paper 11c (audits)  ~8 pp   11,123 words
    merged v15          21 pp   18,963 words
Structure: combined title and abstract; Part I; Part II; cross-part conclusion; merged
references (26 entries); merged declarations. 75 labels, 47 cross-references, 0 dangling.

NOTHING LOST. Both Part bodies reproduced in full and verbatim, each opening with its own
original abstract. Word count EXCEEDS the sum of the parts (18,963 vs 17,558).

THE GENERAL CLAIM NOW STATED: EXACTNESS IS THE INSTRUMENT, NOT THE LIMITATION -- with the
two supports kept separate because they fail independently. EXACTNESS SCALES, because the
stored object is an antichain and the argued instrument is a pairwise bound: a change of
what is enumerated, not a constant-factor saving. EXACTNESS BITES, because the verdicts are
statements about boundaries, non-existence and incomparability -- exactly the kind a
floating-point treatment smooths into a wrong answer. Part I also reports where the
instrument runs out: at five parameters THE PAIRWISE BOUND STOPS BEING SUFFICIENT. That is
the honest form of a scaling claim. What is deliberately not claimed is stated plainly:
these examples do not constitute a general taxonomy of viability failures; they supply
exact counterexamples, finite censuses and reproducible benchmarks that separate mechanisms
often conflated in qualitative discussion. The operational output is restated because it is
the transferable part: boundary-inclusive reviews; fibre splits over threshold tuning;
certainly-safe reporting under aggregation; structural repair of bias rather than
compensation for it; and protocol design before instrument tuning -- DESIGN THE OBSERVATION
BEFORE TUNING THE ESTIMATOR, because in both regimes the information structure, not the
estimation quality, determines what is achievable.

NEW BUG: MULTIPLE SIZE-GROUPS IN ONE REFERENCE LIST. The 1+2 merge fixed an unbalanced
{\footnotesize ... } by stripping the wrapper at the block ends. That was insufficient
here: paper 5's reference list contains SEVERAL such groups, and the entry splitter cannot
break across a delimiter (there is no ". " to key on), so the opener and closer stayed
glued to whichever entries happened to be first and last in each group. An alphabetical
sort then scattered them, producing "! Too many }'s." Fixed by dropping size-group
delimiter LINES (a line that is exactly {, }, {\cmd}, or {\cmd) before splitting entries.
This is strictly more general than the block-end strip and supersedes it. A SIDE EFFECT
WORTH NOTING: the merged reference count went from 24 to 26. Two entries had been invisible
to the earlier de-duplication because they were glued to brace wrappers and so failed to
normalise to distinct keys. Recovering them is a reminder that a reference-merge bug does
not only break the build -- it can silently drop citations.

VERIFICATION. Compiled with tectonic: 21 pages, 0 errors, 0 undefined references. Content
checked by PDF text extraction for both Part markers, both original abstracts, and each
part's signature objects (1,048,576 -> 496; 68,719,476,736; the 16 maximal singletons; the
93-cell grid; "no coarsest"; 7 of 15; Y* = 27/5).
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

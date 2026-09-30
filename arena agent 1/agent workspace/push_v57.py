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
    ("arena agent 1/agent workspace/papers/paper11_forecasting_baselines_v64.tex",
     "/home/user/papers/paper11_forecasting_baselines_v64.tex"),
    ("arena agent 1/agent workspace/papers/PAPER_MERGE_11_11b.md",
     "/home/user/papers/PAPER_MERGE_11_11b.md"),
    ("arena agent 1/agent workspace/p5/merge_11_11b.py",
     "/home/user/p5/merge_11_11b.py"),
]

MSG = """Merge paper 11 + paper 11b into one two-system forecasting paper

WHY THIS MERGE. The bar is BROAD CONCLUSIONS AND FUNDAMENTAL UNDERSTANDING. Nine of
the fifteen papers drew their conclusions from a single system each, which caps how
broad any of them can be. Papers 11 (Northern cod) and 11b (Edwards Aquifer) were the
strongest candidate for a fix, on evidence:
  - Structurally parallel: identical LaTeX preamble and the same section architecture
    (Introduction, Related work, Data/Specification, Forecast Models, Evaluation
    Design, Results, Discussion, Conclusions), differing only in the system.
  - ONE METHOD, TWO SYSTEMS: both score deliberately simple process-based models
    against naive benchmarks under a retention rule frozen before any score.
  - 11b already claimed the replication: its "Transferable lesson" paragraph stated the
    finding "replicates in the companion Northern cod forecast study". The merge makes
    that replication INTERNAL to the paper rather than a citation to a sibling.
Vocabulary overlap is 33.0% -- unremarkable, and not the deciding criterion. The
deciding criterion is that TOGETHER THEY SUPPORT A CLAIM NEITHER SUPPORTS ALONE: a
finding on one system is a demonstration; the same finding on two systems from
different domains is a replication.

WHAT WAS PRODUCED. paper11_forecasting_baselines_v64.tex, a NEW VERSION; neither
source was modified.
    paper 11 (cod)       41 pp   20,764 words
    paper 11b (Edwards)  22 pp    9,637 words
    merged v64           64 pp   31,100 words
Structure: combined title and abstract stating the two-system design and the general
claim; Part I (full Northern cod study); Part II (full Edwards study); a cross-system
conclusion; merged references (36 entries, union, de-duplicated); merged declarations.

NOTHING LOST. Both Part bodies are reproduced in full, uncondensed. BOTH ORIGINAL
ABSTRACTS ARE PRESERVED -- an early version of the merge script stripped them as
duplicate front matter; that was caught by checking the rendered PDF for the phrase
"Five surplus-production modules", which had vanished. The script was corrected so
each Part opens with its own original abstract, with the combined abstract at the head
of the document. Page count is the sum of the parts plus TOC and cross-system
conclusion, which is the arithmetic check that nothing was dropped.

THE GENERAL CLAIM NOW STATED BY THE PAPER: "A model that persists a near-white driver
has no claim to beat persistence, whatever its mechanistic fidelity," with two general
consequences -- a negative result is informative only against a protocol fixed in
advance; and the failure is DIAGNOSTIC, locating the defect in the driver's spectrum
rather than only reporting a loss. The two systems supply different mechanisms (a
weakly autocorrelated surplus in the fishery; a near-white annual recharge, r = 0.17,
in the aquifer) against the same test, and that invariance is the point.

BUGS HIT DURING THE MERGE, AND THE LESSON:
  1 \end{document} x3: each source body carried its own, and so did the declarations
    block.
  2 Duplicate titles/abstracts: both bodies contained \title/\author/\maketitle.
  3 THE COMMENT BUG, AGAIN. Paper 11's provenance header MENTIONS \documentclass and
    \begin{document} ("v61 was THREE complete LaTeX documents concatenated (3x
    \documentclass, 3x \begin{document})"). A naive s.find() split INSIDE THAT COMMENT,
    putting the real preamble into the body and producing "LaTeX Error: Environment
    abstract undefined". Fixed with a comment-aware find_real() that skips matches
    preceded by % on the same line. THIS IS THE THIRD TIME THIS CLASS OF BUG HAS
    APPEARED IN THIS CORPUS; it must be assumed present in any structural operation
    on these files.
  4 Namespace collisions: the two papers shared 8 labels (conclusions, discussion,
    evaluation-design, forecast-models, introduction, priorart, references, results).
    Resolved by prefixing Part I labels with cod- and Part II labels with edw-,
    rewriting both \label and \ref/\eqref consistently.
  5 re.sub replacement escaping: '\eqref{...}' in a replacement string raises
    "bad escape \e"; replacements must be passed as lambdas.

VERIFICATION. Compiled with tectonic: 64 pages, 0 errors, 0 undefined references.
Rendered content checked by PDF text extraction for both Part markers, both systems'
signature quantities (884.6 kt, r = 0.17, 16.80 vs 21.11, 97% power), both original
abstracts, and the cross-system conclusion.
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

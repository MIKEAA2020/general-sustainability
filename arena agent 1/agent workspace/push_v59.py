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
    ("arena agent 1/agent workspace/papers/paper01_obstruction_calculus_v62.tex",
     "/home/user/papers/paper01_obstruction_calculus_v62.tex"),
    ("arena agent 1/agent workspace/papers/PAPER_MERGE_01_02.md",
     "/home/user/papers/PAPER_MERGE_01_02.md"),
    ("arena agent 1/agent workspace/p5/mergelib.py",
     "/home/user/p5/mergelib.py"),
    ("arena agent 1/agent workspace/p5/merge_01_02.py",
     "/home/user/p5/merge_01_02.py"),
]

MSG = """Merge paper 1 + paper 2: the obstruction calculus in two readings

WHY THIS MERGE. Paper 2 is explicitly a companion rather than an independent
contribution. Its own conclusion opens: "The belief-state safety value carries the
obstruction calculus into the probabilistic setting without loss of exactness." Its
abstract opens: "The obstruction calculus characterizes nonviability through
certificates on information states; the probabilistic side asks what the certificates
imply when the information state is a distribution." Two papers, ONE INSTRUMENT, TWO
READINGS. Separately each supports half of a claim:
  PART I (paper 1, information states): sound sufficient conditions for nonviability,
    finitely checkable in the common-action, fibre-certification and finite-horizon forms.
  PART II (paper 2, distributions): the belief-state safety value V_k(b), carried
    entirely in exact rational arithmetic.
Merged, they establish that the two readings are THE SAME OBJECT AT TWO RESOLUTIONS, not
competing approximations: the value-one level of the belief recursion COINCIDES with the
viable-set recursion, and the alpha-vectors are EXACTLY the indicators of the maximal
jointly survivable subsets of the support -- an antichain, Sperner-bounded. That
agreement is a theorem relating the two parts, and neither part can state it.

WHAT WAS PRODUCED. paper01_obstruction_calculus_v62.tex, a NEW VERSION; neither source
modified.
    paper 1 (calculus)            ~23 pp   23,428 words
    paper 2 (probabilistic)       ~12 pp   13,632 words
    merged v62                     35 pp   38,565 words
Structure: combined title and abstract; Part I (obstruction calculus, full body of paper
1); Part II (probabilistic sufficiency, full body of paper 2); cross-part conclusion;
merged references (30 entries, union, de-duplicated); merged declarations.

NOTHING LOST. Both Part bodies reproduced in full, verbatim. BOTH ORIGINAL ABSTRACTS
PRESERVED, each opening its Part. Word count EXCEEDS the sum of the parts (38,565 vs
37,060): the new front matter, TOC, Part heads and cross-part conclusion are additive.
124 labels, 71 cross-references, 0 dangling.

THE GENERAL CLAIM NOW STATED: nonviability under incomplete observation is certifiable in
exact arithmetic in both the set-valued and the probabilistic reading, and the two are
the same object at two resolutions. The cross-part conclusion argues that the direction
the literature has treated systematically is SUFFICIENCY (Veliov's output-feedback
regulation condition, the estimation-tube reduction), while the complementary direction
-- certifying that NO policy is viable -- has received less. That asymmetry matters
practically, because a negative verdict is what licenses a redesign: it is the difference
between "no policy we tried worked" and "no policy can work, and here is the finite object
that proves it." Both parts supply finite, checkable, exact witnesses for that negative
direction. What does NOT transfer is stated explicitly: the taxonomy is nonexhaustive,
the certificates are sound SUFFICIENT conditions for nonviability rather than necessary
ones, and the agreement between the two readings is proved under stated structural
hypotheses (finite models, deterministic kernels and observation maps, rational input
data). The design consequence is stated generally: every mechanism empties a specific
response correspondence and licenses a specific DESIGN response -- enlarge the command
set, add a separating observation, shorten the review interval, refine the index, correct
a known bias -- and Part II attaches a PRICE to each. The general lesson: THE OBSERVATION
LAYER, NOT THE FORECAST LAYER, SETS THE VALUE.

THREE NEW BUGS FOUND (all now fixed in mergelib.py):
  1 \proposition already defined. Both papers declare theorem environments. The preamble
    union compared lines LITERALLY, so paper 2's \newtheorem{proposition}{...} was copied
    across despite paper 1 already defining it. Fixed by de-duplicating \newtheorem BY
    ENVIRONMENT NAME, not by line.
  2 Dangling refs from declarations. Paper 1's Code-availability line carries
    \ref{tab:coverage} and \ref{fig:coverage}. Only the BODIES were namespaced, so these
    two refs stayed unprefixed and dangled. First fix attempt (namespacing the
    declarations block with its own labels) did nothing, because declarations blocks
    define NO LABELS -- namespace() only rewrote refs whose targets were defined in the
    same block. Real fix: pass the part's label set as a known= argument so refs are
    rewritten even where no label exists locally.
  3 Unbalanced {\footnotesize ... }. Paper 1 wraps its whole reference list in a size
    group. Splitting entries and sorting them alphabetically scattered the opener and the
    closer into different entries, producing "! Too many }'s." at the end of the
    document. Fixed by stripping the group wrapper in split_entries() BEFORE the split.

VERIFICATION. Compiled with tectonic: 35 pages, 0 errors, 0 undefined references.
Rendered content checked by PDF text extraction for both Part markers, both original
abstracts, and the signature objects of each part (common-action obstruction,
antichain/Sperner, the belief-state safety value, the 36 timing combinations). Two
apparent misses -- "Part II -- Probabilistic sufficiency" and "Six mechanisms" -- were
both traced to extraction artifacts (the ff ligature rendering as a single glyph, and
paper 1's own wording "Five mechanisms ... with a sixth"), not to missing content.
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

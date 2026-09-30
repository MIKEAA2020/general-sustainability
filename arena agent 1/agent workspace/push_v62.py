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
    ("arena agent 1/agent workspace/papers/paper06_assessment_separation_v66.tex",
     "/home/user/papers/paper06_assessment_separation_v66.tex"),
    ("arena agent 1/agent workspace/papers/PAPER_MERGE_06_10.md",
     "/home/user/papers/PAPER_MERGE_06_10.md"),
    ("arena agent 1/agent workspace/p5/merge_06_10.py",
     "/home/user/p5/merge_06_10.py"),
    ("arena agent 1/agent workspace/p5/mergelib.py",
     "/home/user/p5/mergelib.py"),
    ("arena agent 1/agent workspace/p5/build.py",
     "/home/user/p5/build.py"),
]

MSG = """Merge paper 6 + paper 10: aggregation is a claim, not a presentation

WHY THIS MERGE. Both papers close on THE SAME GENERAL CLAIM, reached from different
directions:
  6:  "...not of either tradition ... an index can be sound at the level of accounting
       and still over-certify at the level of assessment ... per-floor reporting is not a
       presentation preference but a detection requirement."
  10: "For ecological-economics measurement, that is the closing statement: NOT RIVAL
       DOCTRINES BUT TWO READINGS OF ONE LEDGER, AND THE VECTOR READING IS WHAT CARRIES
       THE CERTIFICATE."
As with papers 7 and 8, two papers asserting one sweeping conclusion from one direction
each. The directions are genuinely complementary rather than redundant:
  PART I (paper 6) gives the GEOMETRIC reason: the compensatory and noncompensatory
    readings are related by a QUANTIFIER COMMUTATION THAT CAN FAIL ON AN OPEN REGION of
    state space; for any finite menu the acceptance gap is exactly the part of the convex
    hull of the required margins that NO SINGLE PLAN DOMINATES.
  PART II (paper 10) gives the CONSERVATION reason: in a typed stock--flow ledger the
    moieties are not commensurable, conservation is proved from the incidence structure
    rather than assumed, and substitution is located WITHIN the ledger as either a
    recycled flux or a drawdown on a second compartment -- different entries with
    different statuses.
Part I says the gap is real and geometric; Part II says the coordinate-wise reading is the
one that carries the certificate.

WHAT WAS PRODUCED. paper06_assessment_separation_v66.tex, a NEW VERSION; neither source
modified.
    paper 6 (assessment separation)  60 pp   29,071 words
    paper 10 (typed ledgers)         62 pp   34,903 words
    merged v66                      122 pp   65,390 words
Structure: combined title and abstract; Part I; Part II; cross-part conclusion; merged
references (153 entries, union, de-duplicated); merged declarations. 129 labels, 0
dangling. Compiled with tectonic: 122 pages, 0 errors, 0 LaTeX undefined-reference
warnings.

NOTHING LOST. Both Part bodies reproduced in full and verbatim, each opening with its own
original abstract. Word count EXCEEDS the sum of the parts (65,390 vs 63,974) because the
new front matter, TOC, Part heads and cross-part conclusion are additive. Page count is
the sum of the parts plus the new front matter.

THE GENERAL CLAIM NOW STATED: aggregating incommensurable quantities is not a doctrine to
be weighed against its alternative but a REPRESENTATION ERROR WITH A GEOMETRIC SIGNATURE,
and the error is structural rather than a knife-edge. Three points are made explicitly
because each is easy to overstate. (1) NOT A NORMATIVE POSITION: Part I's theorem
establishes NO RANKING OF DOCTRINES -- the structural character of the separation is a
property of the finite deterministic menu, not of either the weak- or the
strong-sustainability tradition. Neither part claims aggregation is never permissible; the
claim is that where separately-binding floors matter the aggregate cannot be the instrument
that detects their violation. (2) THE GAP HAS INTERIOR: the commutation fails on an OPEN
REGION, and on the explicit rational datum every nonnegative weighting licenses some
transition, no transition is licensed by all, and no transition satisfies the floors
path-wise. This is the difference between a caution and a theorem, and it is why per-floor
reporting is a DETECTION REQUIREMENT. (3) THE MECHANISM IS IDENTIFIED, NOT ASSUMED: it is
NOT scalarization blindness -- at fixed trajectories the full-cone aggregate is lossless.
It is the POLICY DEPENDENCE of the aggregate-feasible transition: the aggregate says
THERE EXISTS A WEIGHT, the floors say FOR ALL COORDINATES, and the quantifiers do not
commute once the plan may depend on the weight. The implication for composite indices is
stated as one about USE rather than construction: the arithmetic can be impeccable and the
inference drawn from it unsupported. Part II makes the same point from the other side by
unpacking "depletion time" into three mutually non-interchangeable quantities and
classifying three widely cited public-data indicators at their exact status.

TWO NEW BUGS (both fixed in mergelib.py). (1) \end{document} INSIDE THE REFERENCES BLOCK:
paper 10 has no Declarations-style heading after its References -- its declarations sit
BEFORE them -- so split_body() returned no declarations block and the whole tail, including
\end{document}, became "references"; it was then split into entries and sorted into the
middle of the merged bibliography. Fixed by stripping \end{document} from the references
blocks before merging. (2) THE TRAILING-} STRIP ATE A COMMAND'S CLOSING BRACE: the
per-entry cleanup removes a trailing } to clean up size-group wrappers, and applied to an
entry ending in \end{document} it produced the malformed \end{document, giving
"! Paragraph ended before \end was complete." Fixed by not stripping a trailing } that
closes a \begin{...}/\end{...} command. This second bug is the interesting one: A CLEANUP
RULE INTRODUCED TO FIX ONE PROBLEM SILENTLY CORRUPTED AN UNRELATED COMMAND. The fix is a
guard, not a broader strip.

VERIFICATION. Compiled with tectonic: 122 pages, 0 errors, 0 LaTeX undefined-reference
warnings. Content checked by PDF text extraction for both Part markers, both original
abstracts, and each part's signature objects. The undef=21 figure reported by the harness
is the WORD "undefined" occurring in prose (e.g. "undefined output functional"), not a
dangling reference: the log contains ZERO LaTeX "Reference/Citation ... undefined"
warnings.
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

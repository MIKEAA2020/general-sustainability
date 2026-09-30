#!/usr/bin/env python3
"""Commit the non-destructive split of the two \\part-structured container sources."""
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
    ("arena agent 1/agent workspace/papers/paper05_exact_belief_computation_v16.tex",
     "/home/user/papers/paper05_exact_belief_computation_v16.tex"),
    ("arena agent 1/agent workspace/papers/paper06_assessment_separation_v67.tex",
     "/home/user/papers/paper06_assessment_separation_v67.tex"),
    ("arena agent 1/agent workspace/papers/split_parts.py",
     "/home/user/papers/split_parts.py"),
    ("arena agent 1/agent workspace/papers/PRIOR_ART_PASS.md",
     "/home/user/papers/PRIOR_ART_PASS.md"),
]

MSG = r"""Split the two \part-structured containers; units 5 and 6 now have standalone sources

NON-DESTRUCTIVE. Both containers are left byte-identical (138,034 and 458,404 chars, verified
after the run). New numbered versions are written alongside them.

  paper05_exact_belief_computation_v15.tex  (container)
      Part I  -> paper05_exact_belief_computation_v16.tex   UNIT 5   5,654 w
  paper06_assessment_separation_v66.tex     (container)
      Part I  -> paper06_assessment_separation_v67.tex      UNIT 6  24,799 w

WHY. The containers each hold TWO architecture units that share ZERO sentences with each other:
  paper06_v66 = unit 6 (Part I, 25,443 w) + unit 9  (Part II, 33,267 w, 91.6% identical to
                paper10_v53)
  paper05_v15 = unit 5 (Part I,  6,297 w) + unit 11 (Part II, 11,142 w, 67.4% identical to
                paper11c_v2)
Left unsplit, any merge or unit-level edit would silently carry unit 9 / unit 11 content into
unit 6 / unit 5. The split removes that hazard permanently and unblocks both the pending
citation fixes and the re-merge of units 7-10.

TWO CANDIDATE SPLITS WERE DISCARDED AS REDUNDANT. paper11c...v3 and paper10...v54 (the
container-derived Part IIs) overlap their pre-existing standalone files by only 67.4% and
91.6%, so the containers hold EARLIER states. paper11c_v2 and paper10_v53 therefore remain
authoritative for units 11 and 9, and the derived copies were deleted rather than committed,
to prevent ambiguity about which file is the unit source.

ASYMMETRIES THAT A BLIND SPLIT WOULD HAVE BROKEN. The two containers are not structured alike:
  - paper05: Part I has its own \title / \maketitle / \begin{abstract}. Retaining the umbrella
    block as well emitted TWO \maketitle and printed the title block twice. Fixed by starting
    Part I at its \part and injecting the umbrella \title.
  - paper06: Part I has its own abstract but NO \maketitle -- in the container the umbrella's
    \maketitle covers both parts. Fixed by starting at its \part and injecting \title plus
    \maketitle.
  - paper10's Part II emits its abstract as \section*{Abstract}, not \begin{abstract}, so a
    count-based check would have mis-read it.

VERIFICATION PERFORMED. No LaTeX toolchain is available in this session (apt requires root; the
tectonic binary could not be fetched), so compilation was not possible. Static verification was
done instead, and is recorded as a residual risk:
  - 1 \documentclass, 1 \begin{document}, 1 \end{document}, 1 \part per file;
  - all environments balanced (enumerate, itemize, abstract, figure, table, center, document);
  - NO CROSS-PART MACRO DEPENDENCY -- every \newcommand / \def / \newtheorem /
    \DeclareMathOperator defined in only one part was checked against the other; none is used
    across the boundary;
  - no dangling \ref after stripping comments (a \ref{priorart} inside a %% comment is a false
    positive, not a defect);
  - word counts consistent with the measured part sizes.
The preambles are copied verbatim from sources known to compile, so package availability is
unchanged; the unverified step is compilation itself, which should be done before any split is
merged or posted.

KNOWN COSMETIC ISSUE, NOT TAKEN. Both splits carry the umbrella title, which names both parts
(e.g. "computation at scale and the audits that bind the obstruction calculus to its worked
systems"). Narrowing the titles is a content decision and is left for the author.

Also updates PRIOR_ART_PASS.md section 3.1 with the split record.
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

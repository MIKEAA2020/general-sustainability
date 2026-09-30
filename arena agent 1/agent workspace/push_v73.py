#!/usr/bin/env python3
"""Commit: apply unit 5's three prior-art fixes (antichain algorithms, Harper, scope)."""
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
    ("arena agent 1/agent workspace/papers/PRIOR_ART_PASS.md",
     "/home/user/papers/PRIOR_ART_PASS.md"),
]

MSG = r"""Apply unit 5's three prior-art fixes: antichain algorithms, Harper, scope tightening

To paper05_exact_belief_computation_v16.tex (unit 5, 6,068 -> 6,710 w).

1. NEW SUBSECTION "Antichain algorithms in formal verification". The prior-art pass found the
   antichain ALGORITHMS literature entirely uncited -- the paper cited only antichain COUNTING
   (Sperner, Kleitman, Stanley, Engel). That literature uses antichains as a compact DATA
   STRUCTURE: for downward-closed sets, storing only maximal elements can be exponentially more
   succinct, and De Wulf, Doyen, Henzinger and Raskin (2006) PROVED the separation in general
   form -- they exhibit families of automata on which the subset construction is exponential
   while the antichain algorithm is polynomial. The same representation is used for games of
   imperfect information, where winning belief states are downward closed -- which is unit 5's
   instrument almost verbatim.

   Added: De Wulf, Doyen, Henzinger and Raskin (2006); Doyen and Raskin (2009); De Wulf,
   Doyen, Maquet and Raskin (2008); Filiot, Jin and Raskin (2009, 2011). The subsection states
   plainly that "the compression itself should not be read as a new result", then distinguishes
   three axes: those algorithms compute FIXED POINTS whereas there is none here; those settings
   are QUALITATIVE (a winning region) whereas V_k(b) is a QUANTITATIVE worst-case probability
   whose stored antichain is the identifying structure of its alpha-vectors; and the compression
   figures are MEASURED COSTS of exhaustive exact classification at this size, not a claimed
   asymptotic improvement. The paper's five claimed contributions are unaffected.

2. HARPER (1966). The m=5 result -- "the maximal sets are the 32 radius-one balls" -- is a
   Hamming-ball extremal statement, and hypercube vertex isoperimetry governs exactly that, yet
   neither Harper nor any isoperimetric result was cited. On inspection the paper's result turns
   out to be INDEPENDENT of isoperimetry, and the source now says why: the balls arise RADIALLY.
   The constant matched action u = 1 gives a cell at Hamming distance k the drift -1/2 + (m-2k)/5,
   which depends on the cell only through k, so the set on which it is nonnegative is a Hamming
   ball of radius r*(m) = floor((2m-5)/4) AUTOMATICALLY. Nothing is minimised. The coincidence
   with the isoperimetric extremal sets is structural rather than consequential, and no result
   of the paper depends on Harper's theorem. Stating the relation is the point; leaving a reader
   to wonder whether the result is an uncredited corollary is not.

3. SCOPE TIGHTENING. The split removed the umbrella abstract, and with it both overclaiming
   phrases -- verified: "scales further" and "relaxing instinct" occur 0 times in v16 and once
   each in the container. One residual survived in the Introduction: "the answer is affirmative"
   to a general question about the curse of dimensionality, qualified only two sentences later.
   Changed to "ON THE INSTANCE STUDIED HERE the answer is affirmative", aligning the
   Introduction with the related work's own discipline ("this paper proves no new theorem about
   antichains... a computation on one instance").

Six bibliography entries added in the paper's flat hand-formatted style, anchored on the
alphabetically-following entries: De Wulf 2006, De Wulf 2008 and Doyen & Raskin after Baccelli;
Filiot 2009 and Filiot 2011 after Farkas; Harper after Geretti.

ALL SIX NEW CITATIONS CROSSREF-VERIFIED BEFORE INSERTION (no citation enters a source file
unverified -- see the fabricated-DOI correction recorded in the previous commit):
  De Wulf, Doyen, Henzinger, Raskin 2006  CAV, LNCS 4144, 17-30    10.1007/11817963_5
  De Wulf, Doyen, Maquet, Raskin 2008     TACAS, LNCS 4963, 63-77  10.1007/978-3-540-78800-3_6
  Doyen and Raskin 2009                   LMCS 5(1)                10.2168/lmcs-5(1:5)2009
  Filiot, Jin and Raskin 2009             CAV, LNCS 5643, 263-277  (publisher record)
  Filiot, Jin and Raskin 2011             FMSD 39, 261-296         (Springer record)
  Harper 1966                             JCT 1, 385-393           10.1016/s0021-9800(66)80059-5

VERIFIED AFTER EDIT: all eight checked citations resolve (De Wulf 2006, De Wulf 2008, Doyen
2009, Filiot 2009, Filiot 2011, Harper 1966, Sperner 1927, Kleitman 1969); braces balanced in
every inserted passage and file-wide (546/546); one \begin{document} and one \end{document}.

COMPILATION IS STILL UNVERIFIED -- no LaTeX toolchain available (apt needs root; tectonic fetch
blocked). Recorded as residual risk in PRIOR_ART_PASS.md section 3.1.

Units 2-6 prior-art pass is now COMPLETE: units 2, 3, 4 passed with no additions; units 5 and 6
survived with six added citations between them. No unit repositioned, combined or dropped; the
attrition budget was not drawn on.
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

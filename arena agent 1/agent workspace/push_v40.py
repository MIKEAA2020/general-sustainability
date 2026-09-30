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
    ("arena agent 1/agent workspace/papers/paper02_probabilistic_sufficiency_v11.tex",
     "/home/user/papers/paper02_probabilistic_sufficiency_v11.tex"),
    ("arena agent 1/agent workspace/papers/paper03_computational_certification_v11.tex",
     "/home/user/papers/paper03_computational_certification_v11.tex"),
    ("arena agent 1/agent workspace/papers/paper05_exact_belief_computation_v11.tex",
     "/home/user/papers/paper05_exact_belief_computation_v11.tex"),
    ("arena agent 1/agent workspace/papers/VERSION_CURRENCY.md",
     "/home/user/papers/VERSION_CURRENCY.md"),
]

MSG = """Correction: three papers were built from stale sources; re-assembled

The user caught that paper 2 was assembled from
paper2_probabilistic_sufficiency_v9.tex while v14 existed. The check was then
generalised to all eleven. THREE of the five P2-group papers were built from
stale sources.

  paper02 psuff   v9 -> v14    5 versions behind   +641 words
  paper03 comp    v9 -> v20   11 versions behind  +1967 words
  paper05 ebc     v9 -> v13    4 versions behind   +540 words

Re-assembled as v11 of each; the v10 files are retained. NO label was dropped
in any lineage, so each new version is a content superset of the old.

VERIFIED NOT DRIFTED: paper01 (source fam/obstr_v57.tex -- the rewrites
lineage stops at v56, so v57 is ahead of it); paper04 (fam/minimax_v11.tex
and paper rewrites/latex/minimax_dual_certificates_v12.tex are IDENTICAL,
6107 words, same labels); paper07, paper09, paper10, paper11.

WHAT THE STALE VERSIONS WERE MISSING -- not cosmetic. The psuff v9 -> v14 gap
included (1) a mathematical correction: v14 distinguishes the feedback
viable-set recursion W^fb_k from the blind recursion W_k, with
rem:feedback-strict noting the inclusion is strict in general; v10 conflated
them. (2) A repaired proof: v10's converse for the value-one characterisation
read "with deterministic observations the realized observation path is fixed
by the declared sequence" -- a hand-wave -- replaced in v14 by a proper
induction on k. (3) The completed mechanized layer.

THE MECHANIZED LAYER -- the largest omission. Three current sources carry a
Lean 4 claim; TEN of my eleven papers carried no Lean mention at all.
  comp_v20: the Farkas core underlying the exact primal-dual witnesses is
    PROVED in Lean 4 (54 modules, 60 build jobs, no axioms, no admitted
    gaps); the soundness direction -- the one the certificates use -- from the
    ordered-field interface alone. The converse is not proved there, and is
    not used.
  ebc_v13: sections hamming-deadline formalized, no axioms, no admitted gaps,
    no CAS oracle, derived from the ordered-field interface alone.
  psuff_v14: support identity, freeze count and its frozen value, and
    rationality of the alpha-vectors, machine-checked. One bound remains cited
    rather than formalized: the Sperner bound of prop:antichain (iii).
Papers 2, 3 and 5 now carry these claims.

OPEN, AND THE BIGGEST SINGLE FINDING: paper 1's central results are already
machine-checked and the paper does not say so.
lean/Formalizations/P1_Obstruction.lean is 29,054 chars, 58 theorem/lemma/def,
0 axioms, 0 sorry, importing only Formalizations.Prelude. It declares post,
possible, commonAdm, beliefSafe, preOp, Wk, preOp_mono, Wk_antitone,
Wk_descending, SafeUnderPi, finite_horizon_sound, tree_sound,
finite_horizon_complete, Blocked, blocked_iff, commonSafe.
Mapping onto paper 1's labels:
  finite_horizon_sound / finite_horizon_complete -> thm:finite-horizon
  commonSafe, Blocked, blocked_iff              -> thm:common-action
  Wk_antitone, Wk_descending                    -> def:kernel
  preOp_mono                                    -> prop:monotone
Minimax_Dual.lean (13,427 chars, 26 declarations, 0 axioms, 0 sorry) sits
under paper 4, which also does not mention it.

NOT YET DONE, DELIBERATELY: I have not added these claims to papers 1 and 4.
Doing so requires first confirming the modules build and that each named
declaration means what the mapping assumes. Writing the claim before the check
is exactly the failure that produced the retracted "tension" argument.

CAVEAT NEEDING RESOLUTION: P1_AssessmentSeparation_v5.lean (paper 6) is
160,246 chars and 246 declarations with 0 axioms but 1 sorry -- an admitted
gap. Paper 6 mentions Lean once; if that mention asserts "no admitted gaps"
it is false as it stands and must be corrected before submission.

Adds papers/VERSION_CURRENCY.md recording all of the above.
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

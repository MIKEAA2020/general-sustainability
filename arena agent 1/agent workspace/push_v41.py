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
    ("arena agent 1/agent workspace/papers/paper01_obstruction_calculus_v60.tex",
     "/home/user/papers/paper01_obstruction_calculus_v60.tex"),
    ("arena agent 1/agent workspace/papers/paper04_minimax_dual_certificates_v13.tex",
     "/home/user/papers/paper04_minimax_dual_certificates_v13.tex"),
    ("arena agent 1/agent workspace/papers/VERSION_CURRENCY.md",
     "/home/user/papers/VERSION_CURRENCY.md"),
]

MSG = """Lean layer VERIFIED by building it, then written into papers 1 and 4

Every mechanized claim below was CHECKED BEFORE being written into any paper.

METHOD: Lean 4.14.0 installed via elan; the lean/ project fetched from the
remote (lakefile.toml plus 67 modules) and built.

RESULT 1 -- THE PROJECT BUILDS. `lake build`: 60/60 jobs, exit 0. This matches
the "54 modules, 60 build jobs" figure the sources claim.

RESULT 2 -- NO ADMITTED GAPS, established three independent ways.
  (a) #print axioms on the named declarations -- the only reliable test, since
      in Lean an unfinished proof surfaces as the axiom sorryAx in the footprint
      of every declaration depending on it:
        finite_horizon_sound     -> none
        finite_horizon_complete  -> Classical.choice
        tree_sound               -> none
        blocked_iff              -> propext, Classical.choice, Quot.sound
        Wk_antitone, Wk_descending, preOp_mono, commonSafe -> none
      sorryAx appears nowhere. Those three are Lean's standard classical axioms.
  (b) Comment-stripped source scan over all of Formalizations/: ZERO sorry,
      admit, or axiom declarations. The only modifier present is noncomputable
      (20 occurrences), which marks a definition as using classical choice and
      is not a gap.
  (c) At scale: 170 declarations of P1_AssessmentSeparation_v5 checked --
      sorryAx count 0; only propext, Quot.sound, Classical.choice appear.

RESULT 3 -- SCALE: 1,237 theorem/lemma declarations across 61 modules,
including 199 in P1_AssessmentSeparation_v5, 33 in P1_Obstruction, 21 in
Minimax_Dual.

RESULT 4 -- FIDELITY. The formalization's source of record is obstr_v53; paper
1 descends from obstr_v57. v53 has 73 labels, paper01 has 74, and the ONLY
difference is worked-case, added this session. Nothing dropped, and
thm:finite-horizon, def:kernel, thm:common-action, prop:monotone,
thm:static-complete, prop:selector are present in both. So the formalization
does apply to paper 1 as it stands.

SCOPE LIMITS, recorded in the papers rather than omitted:
  1 The continuous-time results are NOT formalized. The header of
    P1_Obstruction.lean says the Dini-derivative arguments, exit certificates
    and timing bounds "live in an analysis setting outside a dependency-free
    Lean layer." Formalized is the discrete core: Section 3.1 (finite systems,
    backward recursion over beliefs), the Section 7 one-step characterization,
    the Section 3.2 common-action obstruction in discrete/infinite-horizon
    form, the Section 4.1 certification theory, the Farkas robustness margin,
    the hidden-mode conflict example, and kernel monotonicity.
  2 Completeness is with respect to policy TREES, not stationary policies:
    finite_horizon_complete returns a PolicyTree, a history-dependent object.
    Where a paper asserts a stationary policy suffices, that rests on the hand
    proof.

WRITTEN:
  paper01_obstruction_calculus_v60.tex -- new subsection 3.8 "Mechanized
    verification of the discrete core": the declaration-to-result table, the
    axiom evidence, and both scope limits.
  paper04_minimax_dual_certificates_v13.tex -- new section "Mechanized
    verification" (inserted before References; that paper has no Conclusion).

RETRACTION. Last commit I reported that P1_AssessmentSeparation_v5.lean
(paper 6) had 1 sorry and an admitted gap, and said paper 6's Lean mention
might be false. That was a FALSE POSITIVE and is retracted. The single grep hit
is line 108 of the file -- a COMMENT reading "Every theorem is fully proved;
there are no `sorry`s and no extra axioms." A grep hit is not evidence; the
claim was made from an unexamined grep, the same failure family as the
retracted "tension" argument. Paper 6's module is clean, per check (c) above.
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

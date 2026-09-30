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
    ("arena agent 1/agent workspace/papers/paper01_obstruction_calculus_v61.tex",
     "/home/user/papers/paper01_obstruction_calculus_v61.tex"),
    ("arena agent 1/agent workspace/papers/paper03_computational_certification_v13.tex",
     "/home/user/papers/paper03_computational_certification_v13.tex"),
    ("arena agent 1/agent workspace/papers/paper04_minimax_dual_certificates_v15.tex",
     "/home/user/papers/paper04_minimax_dual_certificates_v15.tex"),
    ("arena agent 1/agent workspace/papers/paper05_exact_belief_computation_v13.tex",
     "/home/user/papers/paper05_exact_belief_computation_v13.tex"),
    ("arena agent 1/agent workspace/papers/paper09b_arv_certification_v2.tex",
     "/home/user/papers/paper09b_arv_certification_v2.tex"),
    ("arena agent 1/agent workspace/papers/paper11_forecasting_baselines_v63.tex",
     "/home/user/papers/paper11_forecasting_baselines_v63.tex"),
    ("arena agent 1/agent workspace/papers/paper11c_worked_systems_audit_v2.tex",
     "/home/user/papers/paper11c_worked_systems_audit_v2.tex"),
    ("arena agent 1/agent workspace/papers/LEAN_AUDIT_2026-09-30.md",
     "/home/user/papers/LEAN_AUDIT_2026-09-30.md"),
]

MSG = """Lean statement audit across all papers: two stale claims fixed, three under-claims added

METHOD AND ITS LIMITS. A toolchain was deliberately NOT installed -- doing so
previously (.elan, hundreds of MB) breached the ~128 MB workspace snapshot cap.
The audit is therefore STATIC: every claim checked against the Lean source in
/home/user/lean with comments stripped.
  Verifiable here: sorry/admit/axiom/constant absence; declaration counts;
    presence of named declarations; module counts; toolchain pin.
  NOT verifiable here: that the project still BUILDS, and the axiom footprints
    (#print axioms). Both need a working toolchain.

STATE OF THE LEAN TREE:
    64 .lean files; 60 under Formalizations/; 44 distinct logical modules
    (excluding _vN); 1603 declarations
    sorry = 0, admit = 0, axiom = 0, constant = 0
    lean-toolchain pin: leanprover/lean4:v4.34.1
A first scan flagged 12 axiom/constant hits in 7 files. ALL 12 are the ENGLISH
WORD "constant" in prose and doc-comments ("/-- Membership in K is constant on
every observation fibre. -/", "disturbance constant implies...", "constant
expected drift"). None is a Lean declaration. The layer is genuinely gap-free.

CLAIM BY CLAIM:
  paper 1: P1_Obstruction has 58 declarations -- CORRECT (33 theorems + 25 defs;
           excl. 1 structure, 3 inductive). Convention now stated explicitly.
  paper 1: all 9 named declarations (finite_horizon_sound, finite_horizon_complete,
           Wk_antitone, Wk_descending, commonSafe, Blocked, blocked_iff,
           preOp_mono, tree_sound) -- ALL PRESENT.
  paper 3: "54 modules" -- STALE, corrected to 60.
  paper 4: Minimax_Dual has 21 theorems and lemmas -- CORRECT (21 theorems + 3 defs).
  paper 5: EBC has 16 modules, 134 declarations -- CORRECT (16 files; 134 theorems;
           174 total incl. 38 defs + 2 inductives). Paper's wording "134 theorem
           and lemma declarations" is exact.
  papers 1/4/5: "Lean 4 v4.14.0" -- STALE, pin is now v4.34.1.
  papers 1/4/5: "60 build jobs pass" -- UNVERIFIABLE NOW, dated from v4.14.0 run.

CHANGES. Version bumps: paper01 v60->v61, paper03 v12->v13, paper04 v14->v15,
paper05 v12->v13, paper09b v1->v2, paper11 v62->v63, paper11c v1->v2.
  1 Removed the stale v4.14.0 from the body of papers 1, 4, 5.
  2 Added a Verification provenance paragraph to papers 1, 3, 4, 5: the pin is
    v4.34.1; checks were run under v4.14.0; source invariants re-verified
    2026-09-30; THE BUILD HAS NOT BEEN RE-RUN SINCE THE PIN MOVED, so build-job
    figures are dated.
  3 Paper 1: made the "58" convention explicit (33 theorems + 25 definitions).
  4 Papers 3 and 5: "54 modules" -> "60 modules under Formalizations/".

UNDER-CLAIMS FOUND AND CORRECTED. Three papers had Lean modules in the tree but
never mentioned them -- not errors, but leaving evidence on the table:
  paper 9b (ARV): Formalizations.ARV, 2 files, 28 theorems -- bracket_upper_form1/2,
    bracket_sandwich_form1/2, bracket_upper_lt_one_iff, bracket_subunitary_form1/2,
    bracket_subunitary_of_upper_form1/2 + omax primitives. Added a Mechanized
    verification section: this DIRECTLY FORMALIZES lem:bracket, the harvest-free
    multiplier bracket.
  paper 11c (WS): Formalizations.WS, 2 files, 5 theorems -- master_monotone,
    monotone_action_axis. Added a subsection: formalizes prop:master.
  paper 11 (E1): Formalizations.E1, 5 theorems -- ladder_telescope, ladder_bound_upper,
    ladder_bound_lower, ladder_bracket, ladder_ascent. Note added.
In each case the scope limit is stated: the bracket algebra / monotonicity
theorem / ladder inequality is proved, while upstream extraction, enumeration and
estimation are script computations and are NOT proved. Paper 11c states the
arrangement exactly: "the theorem that organises the table is proved, while the
entries in the table are computed."

PAPERS WITH NO LEAN CLAIM. Papers 2 and 6 make Lean claims with no version or
count -- checked, no stale numbers. Papers 7, 8, 9 (Part I), 10, 10b, 11b make
NO Lean claim -- correct, no Lean module corresponds to them. No false claim
introduced.

COMPILE VERIFICATION: all seven changed files compiled with tectonic -- 21, 13,
8, 6, 8, 12 and 41 pages; ZERO undefined references, ZERO errors.
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

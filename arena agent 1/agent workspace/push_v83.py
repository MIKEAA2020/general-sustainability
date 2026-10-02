#!/usr/bin/env python3
"""Commit: Phase 1 remaining work items 1-3 (relocatable v3 chain + elevation re-run)."""
import base64
import json
import os
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT, "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}

# (local path under /home/user, path on branch)
# note: the computation lives at repo ROOT, not under "arena agent 1/agent workspace/"
FILES = [
    ("/home/user/papers/PHASE1_CLAIM_AUDIT.md",
     "arena agent 1/agent workspace/papers/PHASE1_CLAIM_AUDIT.md"),
    ("/home/user/comp/wave_e_cod/src/campaign_e2_elevation_v3.py",
     "wave_e_cod/src/campaign_e2_elevation_v3.py"),
    ("/home/user/comp/wave_e_cod/src/campaign_e2_depensation_v3.py",
     "wave_e_cod/src/campaign_e2_depensation_v3.py"),
    ("/home/user/comp/wave_e_cod/src/campaign_e2_fox_form_v3.py",
     "wave_e_cod/src/campaign_e2_fox_form_v3.py"),
    ("/home/user/comp/wave_e_cod/src/campaign_e2_allee_declared_v3.py",
     "wave_e_cod/src/campaign_e2_allee_declared_v3.py"),
    ("/home/user/comp/fix_repo_paths.py",
     "wave_e_cod/fix_repo_paths.py"),
]

MSG = r"""Phase 1 remaining work items 1-3: relocatable v3 chain, elevation campaign re-run

Closes three of the five open items in PHASE1_CLAIM_AUDIT.md section 7. Item 4 (proof review
of units 1-6 and 11) is closed separately in PROOF_AUDIT.md; item 5 (compile) remains blocked.

ITEM 1 -- relocatable paths. Three scripts hardcoded REPO = Path("/home/user/repo") and derived
COD = REPO/"wave_e_cod"/"src" and REPO/"wave_e_cod"/"results"/... from it:
campaign_e2_allee_declared_v3.py (L46), campaign_e2_depensation_v3.py (L40),
campaign_e2_fox_form_v3.py (L38). Since the scripts live in <repo>/wave_e_cod/src/, they now use
Path(__file__).resolve().parents[2], which resolves to the same root. Verified after the change
that REPO, COD and results/ still point at real directories and that intervention_results_v3.json
is still reachable. The /home/user/repo symlink is no longer needed by the chain.

campaign_srcyear.py (L41) hardcodes Path("/home/user/git_repo") but is the superseded v2-era
ancestor of campaign_e2_elevation_v3.py, is imported by no v3 script (the only match is a comment
in run_intervention_v3.py L54), and is left as a historical artifact. Recorded, not fixed.

ITEM 2 -- self-containment. campaign_e2_elevation_v3.py loaded the v2 artifact
REPO/"wave_e_cod"/"results"/"intervention_results.json" into a local `committed`. That file is
absent from the tree, which is why the campaign could not previously be run at all. Justified by
AST, not grep: the binding had exactly one node, a Store at L171, and ZERO Load nodes anywhere in
the module. Every residual-derived field it supplied is recomputed from the source-year data
immediately below and written back onto fit (train_residual_sd, min, max, _q05, _q10, and
e_min/e_q05/e_q10). The load was dead weight that also made the campaign unrunnable. The now-
unused "import json" is left alone because campaign_e2_fox_form_v3.py has the same situation.

ITEM 3 -- elevation campaign re-run. The campaign now runs start to finish (exit 0, ALL LAYERS
COMPLETE). Re-derived from execution rather than from committed files:

    UC_min (residual_min)   -328.97   delta 0.0000
    UC_q05 (residual_q05)   -287.36   delta 0.0000
    UC_q10 (residual_q10)    -80.87   delta 0.0000
    residual mean            -10.88   delta 0.0000

Also reproduced in the same run: residual SD 114.91, residual max 206.55, lag-1 ACF 0.554, q10
constructive bound 91.59. The script's self-checks assert these and would have aborted otherwise.

STRONGER THAN EQUALITY AT DISPLAY PRECISION: all six output artefacts were regenerated and
compared byte-for-byte against the committed copies in wave_e_cod/src/results_srcyear_v3/ --
residuals, k_grid, stochastic, finite_floors, stochastic_constructive and bootstrap CSVs are all
IDENTICAL. The campaign reproduces the committed artefacts exactly, so the earlier caveat that UC
and the residual mean were "exact but not re-derived" no longer applies. (The CSVs are therefore
not re-committed: they are unchanged.)

Two related runs re-executed to confirm the path edits broke nothing: run_intervention_v3.py
(exit 0; reproduces the BAU UC_q05 T=inf kernel 2219.65 and the UC_q10 constructive bound 91.59),
and the three modified campaigns themselves (all exit 0). run_intervention_v3.py never hardcoded
a path.

Compilation remains unverified -- no LaTeX engine is available and all checks are static.
"""


def api(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(BASE + path, data=data, headers=HDRS, method=method)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


base = api("GET", "/branches/" + BRANCH)["commit"]["sha"]
print("base commit: %s" % base[:10])
base_tree = api("GET", "/git/commits/" + base)["tree"]["sha"]

tree = []
for local, branch_path in FILES:
    if not os.path.exists(local):
        print("  MISSING  %s" % local)
        continue
    blob = api("POST", "/git/blobs",
               {"content": base64.b64encode(open(local, "rb").read()).decode(),
                "encoding": "base64"})
    tree.append({"path": branch_path, "mode": "100644", "type": "blob",
                 "sha": blob["sha"]})
    print("  %8d B  %s" % (os.path.getsize(local), branch_path))

new_tree = api("POST", "/git/trees", {"base_tree": base_tree, "tree": tree})
commit = api("POST", "/git/commits",
             {"message": MSG, "tree": new_tree["sha"], "parents": [base]})
api("PATCH", "/git/refs/heads/" + BRANCH, {"sha": commit["sha"]})
print("pushed: %s" % commit["sha"][:10])

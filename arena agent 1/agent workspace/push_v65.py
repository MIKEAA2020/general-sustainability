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
    ("arena agent 1/agent workspace/papers/paper10_depletion_ledgers_v53.tex",
     "/home/user/papers/paper10_depletion_ledgers_v53.tex"),
    ("arena agent 1/agent workspace/p5/phase0_scan.py",
     "/home/user/p5/phase0_scan.py"),
]

MSG = r"""Phase 0, first fix landed at source: paper10 imports 6.5-yr without its band

SETTLED FIRST: ARE THE MERGES SCRIPTED? Yes, entirely. mergelib.py plus one config per
merge (merge_01_02, merge_03_04, merge_05_11c, merge_06_10, merge_08_07,
merge_09_9b_10b, merge_11_11b) and build.py for verification. A re-merge is 0.084 s.
Therefore option C is strictly better than A: fix at source, hold the merges provisional,
re-merge once at the end. No merge was manual, so re-merging costs nothing.

PHASE 0 SWEEP (systematic, not enumerative). A scanner, p5/phase0_scan.py, looks for
DEFECT CLASSES rather than a fixed list, across all 44 .tex files: stale provenance,
convention contamination, unverifiable claims, abstract selection, unsourced numbers,
mis-cited prior art, bare point estimates. On the 15 pre-merge source heads it returned 10
findings. Checking each against its context:

SEVEN OF THE TEN ARE FALSE POSITIVES, AND THIS IS THE IMPORTANT RESULT. All seven are the
Lean toolchain pin. Every one of papers 1, 3, 4 and 5 already states BOTH the current pin
(v4.34.1) AND the run pin (v4.14.0), followed by an explicit disclosure: "The build has not
been re-run since the toolchain pin moved, so the build-job figures below date from the
v4.14.0 run and should be re-confirmed before submission." That is correct, honest,
self-disclosing provenance -- not a defect. The scanner matched the string without reading
the sentence around it. Editing these would have REMOVED an honest caveat and made the
papers worse. A defect list built by pattern-matching produces false positives, and acting
on them is its own failure mode.

PAPER A AT SOURCE IS CLEAN ON SOUNDNESS. Two further points, both checked directly:
(a) Paper A's novelty question is RESOLVED, not pending. Doyen (2000), Set-Valued Analysis
8: 149-162, is already integrated at paper01 v61 lines 261-305: the guaranteed viability
domain, the Lipschitz selection, the Steiner synthesis, and the three distinctions
(checkable certificate; holds against EVERY observation-based policy, not merely Lipschitz
memoryless selections; applies beyond exact maintenance of a closed domain). "viscosity"
now occurs 3 times. Both writing jobs named in PAPER_A_PRIOR_ART.md section 7 are DONE.
(b) The E2 hybrid-basis numbers (-460.03, -318.76, -114.85, 134.96) are NOT present in
paper09 v31/v32, paper09b, or fam/e2/paperE2_cod_intervention_v29. The correct v3 numbers
are. That systematic convention error has already been purged from the paper sources; it
survives only in superseded_v2 scripts under repo/wave_e_cod/src, which are marked
"must not be cited".

THE ONE GENUINE FINDING, NOW FIXED AT SOURCE. paper10_depletion_ledgers_v52 imports the
6.5-year crossing from the companion paper WITHOUT its sensitivity band, at the single
site where it says "The companion analysis supplies the one numerical fact about governance
timing that this paper may use without re-deriving it". It then reasons from that number.
Fix (paper10 v53, new version, source untouched): the qualification is inherited with the
number -- the crossing is reproducible across discretisation schemes (6.50-6.73 yr) but is
not identifiable in the parameters, sweeping 0.87-10.67 yr under a half-percent joint
perturbation and vanishing entirely in twenty of sixty-four corners under one percent --
and the text now states explicitly that this is not a number on which a margin in this
paper may be conditioned, and that none is. Nothing removed; the fix adds qualification
only. Compiles: 56 pages, 0 errors.

NOT YET RESOLVED, AND BLOCKING THE SEQUENCE. Paper A's planned composition is obstr +
minimax + P1 separation (PAPER_A_PRIOR_ART.md: "Core: obstr_v55; folds in P1's separation
result, minimax_dual_certificates, certificate_duality"). That is papers 1, 4 and 6. My
merges produced 1+2, 3+4 and 6+10 -- which cuts ACROSS the intended submission
architecture. The merge structure was derived from a content-affinity criterion ("do two
papers together support a broader claim"), but the driver should be "which papers form one
journal submission". Since the merges are held provisional and re-merging is free, this is
cheap to correct -- but it needs the target architecture settled first, not after.
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

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
    ("arena agent 1/agent workspace/FAMILY_CONSOLIDATION_PLAN.md",
     "/home/user/FAMILY_CONSOLIDATION_PLAN.md"),
    ("arena agent 1/agent workspace/CONSOLIDATION_AUDIT.md",
     "/home/user/CONSOLIDATION_AUDIT.md"),
    ("arena agent 1/agent workspace/diffs_compare.py", "/home/user/diffs/compare.py"),
    ("arena agent 1/agent workspace/PAPER_A_PRIOR_ART.md", "/home/user/PAPER_A_PRIOR_ART.md"),
    ("arena agent 1/agent workspace/PAPER_B_BUILD.md", "/home/user/PAPER_B_BUILD.md"),
]

MSG = """Paper B unblocked: build document (long-open item 42)

Paper A is closed. The prior-art gate is cleared: Doyen (2000) was read in
full, the claim survives, both prior-art paragraphs are integrated into
obstr_v57.tex, and the narrowed residual claim is stated in section 1.3.

Finding on inspection before writing anything new: the manuscript already
states its results. Section 1.2 Contributions enumerates all six obstruction
mechanisms and sections 3-10 develop them, with 30+ labelled theorems,
propositions and corollaries. They were drafted in parallel with the prior-art
work rather than gated by it, so no new mathematics was needed to unblock.
What the prior art actually gates is the NOVELTY CLAIM, and that is what
changed: the residual contribution is now stated as a certificate that holds
against EVERY observation-based policy -- not merely Lipschitz memoryless
selections -- for properties beyond exact maintenance of a closed domain.
Plan section 3 item 1 also corrected: it still carried the withdrawn verdict.

PAPER_B_BUILD.md is the build document for the long-open item 42.

  Source map: P5 p5_v47.tex 18,259 w; P4 p4_v41.tex 27,339 w; E2
  paperE2_cod_intervention_v29.tex 16,176 w. ARV (arv_v9, one file under two
  names) has NO file in the workspace -- not a blocker, because its
  reconciliation with E2 is already archived in plan section 8.2, which is
  all Paper B needs.

  Headline: "What decides whether management stabilises or destabilises a
  renewable resource is not biology alone but the decision clock."

  THE TWO RESULTS CONFLICT, and the conflict is the result -- stronger than
  agreement would have been. E2's certificate expires at T* = 6-7 yr; P5's
  sampled loop on cod biology is unstable below 17.5-175 yr. On one system no
  review interval is both stable and certifiable: the window is empty by a
  factor of at least 2.5.

  BOTH CAVEATS TRAVEL WITH IT, neither demoted to a footnote:
   (1) the transport is not unique -- six calibrations pin the crossing only
       within 17.5-175 yr; the conclusion holds in all six, the number does
       not;
   (2) 6.501 yr is ill-conditioned -- a 0.2% change in N*/K moves the
       crossing by 55% (6.50 / 10.10 / 18.38 / 25.31). Do not lead with it
       without a sensitivity band.

  E2/ARV: one paragraph, both directions named, NO numbers reconciled because
  there is nothing to reconcile -- obstruction/necessity in exact rational
  arithmetic versus construction/sufficiency in floating point. The useful
  link runs the other way: ARV's harvest-free collapse certificates are
  evidence for E2's regime-dependence (171 kt post-moratorium, 0 +/- 8 kt
  modern).

  Null result promoted: 42 stocks, multiplicity-controlled, no robust
  institutional cycles; 32 cross-sector systems, no unconfounded oscillator.
  Currently framed as a limitation; it belongs in the abstract.

  Included: 11-section outline, three-figure plan (E2's graphical abstract is
  the model and already exists with its data JSON and generator), and the
  open items -- cadence table needs a real survey (research), figures 2 and 3
  to be drawn, and the 6.501 sensitivity decision with P5 still unresolved.

  Must NOT be said: the conflated claim putting the constraints intersecting
  in [6.501, 7] yr. It is a cross-system inference between systems whose
  growth rates differ by 11.8x.
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

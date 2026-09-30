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
    ("arena agent 1/agent workspace/papers/paper05_exact_belief_computation_v12.tex",
     "/home/user/papers/paper05_exact_belief_computation_v12.tex"),
    ("arena agent 1/agent workspace/papers/PAPER05_SCOPE_AND_PRIOR_ART.md",
     "/home/user/papers/PAPER05_SCOPE_AND_PRIOR_ART.md"),
    ("arena agent 1/agent workspace/papers/PAPERS_MANIFEST.md",
     "/home/user/papers/PAPERS_MANIFEST.md"),
]

MSG = """Paper 5: ebc confirmed, scope decision resolved, prior art added

1 ebc IDENTIFICATION -- CONFIRMED, upgraded moderate -> high. Sixteen Lean
  modules named EBC_* exist in lean/Formalizations/, namespace
  Formalizations.EBC, carrying 134 theorem/lemma declarations with ZERO
  sorry/admit: EBC_Hamming, EBC_Bands, EBC_Ladder, EBC_ExactBelief,
  EBC_Deadline, EBC_Pairs, EBC_Dynamics, EBC_Classification and successive
  versions. The module names map onto paper 5's own section labels (hamming,
  bands, ladder, pbvi, deadline). EBC = Exact Belief Computation. Manifest
  confidence line updated.

2 SCOPE DECISION -- EXPAND, DO NOT FOLD INTO PAPER 3. Decided on evidence:
  paper 3 CITES paper 5 as "the exact-computation companion" in both body text
  and bibliography, so folding would make paper 3 cite itself. Folding would
  also join two different mathematical cores (continuous-to-finite bridge vs
  exact enumeration at scale) -- the failure the manifest itself names -- would
  bury paper 5's own 16-module formalization, and is ruled out by the standing
  constraint that none of the eight venue-assigned papers may be silently
  dropped. Length is not a constraint, so thinness argues for development, not
  merger.

3 THE ORPHANED "SCALE II" -- RESOLVED. Paper 5 is titled "at Scale II" and
  calls itself a companion to the belief-state safety-value theory, but no
  Scale I appeared among the eleven. It is
  paper rewrites/latex/paper2_belief_state_v2.tex, "Belief-State Safety Values
  for Viability under Incomplete Observation" -- which is paper 2 of this set
  in its EARLIER form: 32.6% of its sentences appear verbatim in
  paper02_probabilistic_sufficiency_v11, and both develop V_k(b) and the
  support identity. The companion relation therefore points inward at paper 2.
  Now stated explicitly in the text.

4 PAPERS 2 AND 5 ARE NOT DUPLICATES. Sentence overlap 4.3% (5 of 117), all
  five boilerplate (cross-cite comments, AI declaration, author statement, one
  bibliography line). Complementary: paper 2 uses the antichain structure
  THEORETICALLY (alpha-vectors as indicators of maximal jointly survivable
  subsets, Sperner-bounded, prop:antichain); paper 5 performs the
  computational CENSUS at scale.

5 PRIOR ART ADDED. Concedes Sperner (1927), Dedekind's problem, Kleitman's
  asymptotic count, and Hamming adjacency as classical, and states in as many
  words that THIS PAPER PROVES NO NEW THEOREM ABOUT ANTICHAINS -- the census
  (1,048,576 -> 496) is an output of a computation on one instance. Positions
  PBVI (Pineau/Gordon/Thrun 2003; Shani/Pineau/Kaplow 2013) with the
  distinction being exact rational arithmetic rather than the point-set idea.
  Claim narrowed to four items.

6 MECHANIZED VERIFICATION ADDED. 16 EBC modules, 134 declarations, project
  builds 60/60 under Lean 4.14.0, no sorryAx, no sorry/admit/axiom anywhere in
  the layer. HONEST SCOPE NOTE included: the enumeration itself, including the
  census, is performed by the deposited scripts and is NOT formalized.

7 BIBLIOGRAPHY: seven works added. Chatterjee/Doyen/Henzinger copied verbatim
  from paper 2's bibliography for consistency across the set. Four flagged as
  needing publisher verification: Sperner 1927, Kleitman 1969, Pineau et al.
  2003, Shani et al. 2013.

paper05_exact_belief_computation_v12.tex: 4,241 -> 5,474 words.

RESIDUAL RISK, stated: paper 5 remains the thinnest of the eleven. It is honest
about being a companion, its claim is narrowed, and it carries a
134-declaration formalization -- but a companion whose combinatorics is
classical and whose scale is a four-parameter cube may not clear the novelty
bar however carefully framed. The strongest available move, NOT taken here,
would be to extend the census to a larger instance (five or six parameters),
where the cost figures would say something new about the feasibility frontier
of exact computation. That is research, not editing.
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

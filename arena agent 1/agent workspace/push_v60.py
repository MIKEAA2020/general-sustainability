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
    ("arena agent 1/agent workspace/papers/paper03_computational_certification_v15.tex",
     "/home/user/papers/paper03_computational_certification_v15.tex"),
    ("arena agent 1/agent workspace/papers/PAPER_MERGE_03_04.md",
     "/home/user/papers/PAPER_MERGE_03_04.md"),
    ("arena agent 1/agent workspace/p5/merge_03_04.py",
     "/home/user/p5/merge_03_04.py"),
]

MSG = """Merge paper 3 + paper 4: obstruction certificates are small

WHY THIS MERGE. The two papers are explicitly cross-referenced as reaching THE SAME
FINDING IN DIFFERENT LANGUAGES. Paper 4's conclusion states it directly: "A companion
paper reaches an analogous conclusion for a different pipeline: there the count is the
information--time product rather than the input dimension (Abaee, 2026, computational
certification). The two are the same finding in different languages, and the recurrence
is the point -- OBSTRUCTION CERTIFICATES ARE SMALL OBJECTS WHOSE SIZE IS SET BY THE
DECISION VARIABLES, NOT BY THE UNCERTAINTY." That is a general, fundamental claim
currently split across two papers, each of which can only assert its own half and cite
the other for the other half. Merged, the recurrence stops being an observation about a
sibling and becomes the paper's own result, evidenced by two independent pipelines.
  PART I (paper 3, computational): an outer moment approximation of all measurable
    information-adapted controls plus an inner adversarial approximation yields a finite
    LP whose optimum is a certified lower bound on the continuous-time safety value;
    whenever a positive certificate exists one can be chosen with at most r+1 safety
    rows, r an information--time rank.
  PART II (paper 4, duality): the obstruction is not a failed search but the existence
    of a measure witness, supported on at most k+1 points (k the control dimension),
    tight.
Part I says the certificate CAN BE COMPUTED; Part II says what it IS.

WHAT WAS PRODUCED. paper03_computational_certification_v15.tex, a NEW VERSION; neither
source modified.
    paper 3 (computational)  13 pp   13,626 words
    paper 4 (measure dual)    8 pp    8,566 words
    merged v15               24 pp   23,411 words
Structure: combined title and abstract; Part I; Part II; cross-part conclusion; merged
references (44 entries, union, de-duplicated); merged declarations. 50 labels, 28
cross-references, 0 dangling.

NOTHING LOST. Both Part bodies reproduced in full and verbatim, each opening with its own
original abstract. Word count EXCEEDS the sum of the parts (23,411 vs 22,192) because
the new front matter, TOC, Part heads and cross-part conclusion are additive.

THE GENERAL CLAIM NOW STATED: obstruction certificates are small objects whose size is
set by the decision variables, not by the uncertainty -- with the negative half made
explicit, because a bound is only substantive if it can fail. The natural Helly-type
alternative -- at most m+1 compatible states suffice to witness nonviability -- is valid
for convex common-action sets in R^m and FALSE for a common blind control function: for
every q there is a system with SCALAR input and q+1 indistinguishable modes in which
every proper subbelief is viable while the full belief is not, so every certificate must
involve all q+1 modes. The correct dimension counts independent temporal and
informational control decisions, not inputs. Where the equivalence fails is stated
plainly: the measure characterisation requires convexity, and a two-action instance
exhibits a strict minimax gap in which no measure certifies. The two recoveries are
given as what they are -- Farkas infeasibility certificates and Isaacs minimax drift
conditions are not rival frameworks but specialisations of one duality -- so that what
the unification LICENSES is the transfer of checkability: a certificate verifiable
without re-running the search, whose size is known in advance, and which localises the
failure it reports.

VERIFICATION. Compiled with tectonic: 24 pages, 0 errors, 0 undefined references.
Content checked by PDF text extraction for both Part markers, both original abstracts,
and each part's signature objects (the r+1 safety rows, the q+1-mode rank instance, the
k+1 tight measure bound, Farkas and Isaacs recovery, the minimax gap). The one apparent
miss, "Information--time rank", was traced to a dash-variant artifact (en-dash in the TOC
versus em-dash in the probe), not missing content.

NOTE ON THE MERGE MACHINERY. This merge reused mergelib.py, factored out of the 11+11b
and 8+7 merges. No new failure modes appeared, which is the point of factoring it: the
three bugs found during the 1+2 merge (\newtheorem collision, declarations-block refs,
the {\footnotesize ... } reference group) are now fixed once, centrally.
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

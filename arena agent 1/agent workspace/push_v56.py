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
    ("arena agent 1/agent workspace/papers/paper03_computational_certification_v14.tex",
     "/home/user/papers/paper03_computational_certification_v14.tex"),
    ("arena agent 1/agent workspace/papers/paper04_minimax_dual_certificates_v16.tex",
     "/home/user/papers/paper04_minimax_dual_certificates_v16.tex"),
    ("arena agent 1/agent workspace/papers/paper11b_edwards_forecast_v2.tex",
     "/home/user/papers/paper11b_edwards_forecast_v2.tex"),
]

MSG = """Papers 3, 4, 11b: elevate the general claims each paper already contained

Bar refinement: papers should reach BROAD CONCLUSIONS and advance fundamental
understanding. Three papers already contained a general claim but did not lead with
it, or had nowhere to state it. Fixed as new versions; nothing removed or condensed.

PAPER 4 (v15 -> v16): ADDED A CONCLUSION SECTION. The paper had NO conclusion at all --
it ended with a scope delimitation ("Claimed / Not claimed") and went straight to
References. Added a real Conclusion organised around five points, each grounded in a
result the paper actually establishes:
  - What the obstruction is dual to: the common safe-action set is empty precisely when
    an adversarial probability measure on the active boundary-disturbance bundle drives
    expected inward drift strictly negative against every control (Theorem thm:dual).
    So nonviability is not merely a failed search; it has a WITNESS, and the witness is
    a measure. Same movement as LP going from "the solver found nothing" to "here is a
    dual ray".
  - What governs the size of the witness: supported on at most k+1 points, k the CONTROL
    dimension, and the bound is TIGHT (Proposition prop:sparse). Neither state dimension,
    nor disturbance cardinality, nor discretisation resolution appears in it. Complexity
    of certifying nonviability is set by how many independent controls the agent has, not
    by how large the world is.
  - What the two recoveries establish: polyhedral recovers the l1-normalised Farkas
    multiplier, game case recovers the Isaacs condition (Proposition prop:recover). The
    measure form is not a third thing alongside them but the common generalisation from
    which both drop out.
  - What the boundary result delimits: the convexity boundary is located exactly with an
    explicit gap instance (Proposition prop:gap). Knowing when a certificate CANNOT exist
    is as much the contribution as knowing what it looks like where it does.
  - Scope restated once, unchanged in substance.
Cross-references paper 3's analogous finding, making the shared moral explicit:
OBSTRUCTION CERTIFICATES ARE SMALL OBJECTS WHOSE SIZE IS SET BY THE DECISION AND
INFORMATION STRUCTURE, NOT BY THE SIZE OF THE WORLD.

PAPER 3 (v13 -> v14): RESTRUCTURED THE CONCLUSION SO THE GENERAL CLAIM LEADS. The claim
"certificate size must be understood in the information-time product rather than the
input dimension" was the THIRD item of a three-item list. It now opens the conclusion as
a standalone principle, developed over a full paragraph: the certificate scales with the
product of how much the controller can learn and over how long a horizon it must act; it
does NOT scale with input dimension. A high-dimensional system about which little can be
learned over a short horizon is cheap to certify; a low-dimensional system observed
richly over a long horizon is expensive. DIMENSIONALITY IS THE WRONG AXIS, and pipelines
organised around reducing it optimise the wrong quantity. Then states the same finding
reached independently in the measure-dual companion (tight k+1 bound). Everything
previously in the conclusion -- the three requirements, the bridge theorem, the
three-branch instance, the campaign, the reference library, the open completeness
question, and all three extension directions (stochastic/conic, decentralised and
infinite-horizon, cross-tool comparison study) -- is PRESERVED VERBATIM, reorganised
under explicit headings: What that claim rests on / What the instance shows / What
remains open.

PAPER 11b (v1 -> v2): MOVED AND SHARPENED THE TRANSFERABLE LESSON TO LEAD. It previously
appeared as the fourth paragraph. The conclusion now opens with the general finding:
process-based models are not self-justifying. A one-pool water balance is more mechanistic
than last-value persistence, and that added mechanism is widely treated as a reason to
prefer it; it is not, it is a CLAIM testable against a naive benchmark. The value of a
process model is bounded by the predictability of the driver it persists: where the model's
causal content is carrying a driver forward and that driver is near white, the structure
adds parameters without adding signal, and persisting it is overhead rather than insight.
A MODEL THAT PERSISTS A NEAR-WHITE DRIVER HAS NO CLAIM TO BEAT PERSISTENCE, WHATEVER ITS
MECHANISTIC FIDELITY. Two general consequences: a negative result is informative only
against a protocol fixed in advance; and the failure is DIAGNOSTIC, locating the defect in
the driver's spectrum rather than only reporting a loss. The J-17 findings follow as "the
demonstration", with an explicit note that the basin demonstrates rather than constitutes
the claim. The old lesson paragraph is retained as a one-place statement of the
replication. Practical reading and Generalizability boundary preserved verbatim.

COMPILE: paper03 v14 13pp / paper04 v16 8pp / paper11b v2 22pp -- all zero errors, zero
undefined references. All new content verified present by PDF text extraction.
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

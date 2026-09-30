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
    ("arena agent 1/agent workspace/papers/paper04_minimax_dual_certificates_v14.tex",
     "/home/user/papers/paper04_minimax_dual_certificates_v14.tex"),
    ("arena agent 1/agent workspace/papers/PAPER04_PRIOR_ART.md",
     "/home/user/papers/PAPER04_PRIOR_ART.md"),
]

MSG = """Paper 4: prior-art section added, seven verified references added

THE HONEST BASELINE: this paper's obstruction IS THE EMPTINESS OF THE
DISCRIMINATING KERNEL. The discriminating kernel (Aubin 1991; Aubin & Catte
2002; Cardaliaguet, Quincampoix & Saint-Pierre 1994, 2007) is the largest
closed discriminating domain -- Victor's victory domain -- characterised as the
largest/smallest/UNIQUE MINIMAX (bilateral) fixed point of an adequate map.
thm:dual is, in that vocabulary, a certificate for that kernel being empty.
This collision is CONCEDED in the text, not argued around.

WHAT SURVIVES (four items):
  1 The certificate is a MEASURE, not a SET. That programme returns a subset
    of state space via a set iteration; thm:dual returns a finitely supported
    probability measure. Membership in a kernel becomes existence of a
    checkable dual object.
  2 The support bound and its tightness. prop:sparse: at most k+1 points, k
    the CONTROL dimension -- the witness count scales with the INSTRUMENT
    space, not the state space. Nothing in the fixed-point characterisation
    yields a finite witness of this kind.
  3 The convexity boundary sits exactly where the kernel programme puts it,
    from the other side. CQS 1994 Proposition 2.3: under convexity the
    discriminating kernel IS convex. prop:gap here is the complementary
    NEGATIVE. Together: convexity is simultaneously what makes kernels convex
    and what makes measure duality sound.
  4 One-sided and observation-constrained. The kernel programme computes a
    victory domain in BOTH directions; this certifies only the negative. That
    narrowing is what buys items 1 and 2, and is stated as a narrowing.

FIVE NEIGHBOUR GROUPS, all verified against publisher records:
  1 Discriminating-kernel programme: Aubin 1991, Viability Theory (Birkhauser);
    Aubin 2001, SIAM J. Control Optim. 40(3), 853-881; Aubin & Catte 2002,
    Set-Valued Anal. 10, 379-416; CQS 1994, RAIRO/M2AN 28(4), 441-461 (the
    ALGORITHM paper, source of Prop 2.3); CQS 2007, Advances in Dynamic Game
    Theory, Ann. ISDG 9, 3-35.
  2 Farkas / LP duality: Farkas 1902 (already cited). Finite and static
    versus measures over a boundary-disturbance bundle and the emptiness of a
    set of SIMULTANEOUSLY safe actions. The polyhedral recovery is a
    consistency check, not the generalisation.
  3 Isaacs / HJI: Isaacs 1965 (already cited). A value as a function of state
    under full observation versus a one-directional refutation; the adversarial
    DISTRIBUTION is what carries the singleton case.
  4 Differential games under incomplete information ON THE SPACE OF MEASURES:
    Cardaliaguet & Quincampoix 2008, Int. Game Theory Rev. 10(1), 1-16. THE
    SINGLE CLOSEST NEIGHBOUR, AND NOT IN THE ROADMAP -- found during this
    pass. Players know only a distribution on the initial state; value exists
    via HJI uniqueness on the space of measures. That is an analytic EXISTENCE
    result in an infinite-dimensional setting; this paper gives a FINITE
    CERTIFICATE, k+1 points, exactly checkable. Existence-and-uniqueness
    yields no finite witness, and nothing here establishes a value.
  5 Minimax equality: Sion 1958, Pacific J. Math. 8(1), 171-176. thm:dual's
    equality in the convex case is arguably an instance of this classical
    circle and NO origination of the equality is claimed. What Sion does not
    supply is the SPARSE WITNESS and its tightness. Symmetrically, prop:gap is
    consistent with it: minimax equality is what fails when convexity drops.

TWO CITATION TRAPS HANDLED:
  Aubin and CATTE -- accented, not "Catte". Verified against the Springer
  record, with a warning comment in the .tex not to strip the accent.
  A DROPPED CLAIM. The inherited roadmap note attributed to Aubin (2001) "the
  complement of the kernel -- Poincare's shadow". THAT COULD NOT BE VERIFIED
  AND IS NOT ASSERTED. Aubin 2001 is cited only for the verified
  kernel/capture-basin fixed-point characterisation. An unverified attribution
  is worse than a missing one.

CHECKS: all 12 \ref targets resolve, zero missing. All cited labels verified
present. Braces balanced in the inserted block. All seven new bibliography
entries verified against publisher records.

paper04_minimax_dual_certificates_v14.tex: 6,508 -> 8,397 words (+29%), the
largest relative gain of the 2/3/4 group -- paper 4 was the thinnest of the
eleven. Residual risk is now different in kind: not "no prior art" but whether
the measure form plus the tight k+1 bound plus the located convexity boundary
are enough for a top journal, which is an editorial judgement rather than a
checkable one. Papers 9, 10, 11 remain.
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

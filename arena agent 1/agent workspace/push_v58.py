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
    ("arena agent 1/agent workspace/papers/paper08_governance_delay_v46.tex",
     "/home/user/papers/paper08_governance_delay_v46.tex"),
    ("arena agent 1/agent workspace/papers/PAPER_MERGE_08_07.md",
     "/home/user/papers/PAPER_MERGE_08_07.md"),
    ("arena agent 1/agent workspace/p5/merge_08_07.py",
     "/home/user/p5/merge_08_07.py"),
]

MSG = """Merge paper 8 + paper 7 into one two-regime paper on governance latency

WHY THIS MERGE. Neither paper could make the claim it was making. BOTH CLOSE WITH THE
SAME SWEEPING SENTENCE:
  7: "What decides whether management stabilises or destabilises a renewable resource
     is therefore not biology alone but the DECISION CLOCK."
  8: "INSTITUTIONAL FORM AND TIMING, not ecological lag, decide whether governance
     stabilises or destabilises the stock."
Two papers, ONE GENERAL CLAIM, one delay regime each. The original partition note
separated them deliberately -- "separated from Paper 7 because the mathematics
differs" -- a real reason, but a reason to keep two TREATMENTS, not two papers.
Merged, they support a claim neither supports alone:
  PART I (continuous channel, paper 8): delay as a lag in the control loop. Establishes
    that the effect of latency is RULE-SIGNED AND NON-MONOTONE -- intermediate delay
    stabilises under the mobilising rule (two subcritical Hopf crossings) and is stable
    at every delay under the protective rule (no-Hopf theorem). "Delay destabilises" is
    false as a generality.
  PART II (sampled channel, paper 7): delay as a review clock. Establishes that the
    OPERATOR is not innocent -- the exact sample-and-hold map crosses once near 6.5 yr
    while one-step approximations report artefact crossings, and the protective channel
    is stable at every interval.
Together these separate the PHENOMENON (latency in the institutional loop matters, and
rule-dependently) from the REPRESENTATION (whose choice changes the computed answer).
That separation is the general result, and neither part can state it.

EVIDENCE THE ENTANGLEMENT WAS REAL. Colliding labels: 6 (conclusion, discussion,
introduction, limitations, references, related). Paper 8 cites paper 7's Section 3.5 in
LIVE TEXT for the identifiability band; paper 7 does not cite back. The 6.5-yr number
appears 36 times in paper 7 and 22 times in paper 8 -- the same result computed in one
paper and quoted in the other. That cross-paper dependency is now internal.

WHAT WAS PRODUCED. paper08_governance_delay_v46.tex, a NEW VERSION; neither source
modified.
    paper 8 (continuous)  46 pp   27,377 words
    paper 7 (sampled)     41 pp   19,333 words
    merged v46            90 pp   49,255 words
Structure: combined title and abstract; Part I (continuous, full body of paper 8);
Part II (sampled, full body of paper 7); cross-regime conclusion; merged references
(85 entries, union, de-duplicated); merged declarations.

NOTHING LOST. Both Part bodies reproduced in full, verbatim, uncondensed. BOTH ORIGINAL
ABSTRACTS PRESERVED, each opening its own Part (same defect caught and fixed in the
11+11b merge; the fix carried forward here from the start). Word count EXCEEDS the sum
of the parts (49,255 vs 46,710) because the new front matter, TOC, Part heads and
cross-regime conclusion are additive. The cross-citation "(Abaee, 2026, Sampled
Governance, Section 3.5)" is LEFT VERBATIM in Part I; it now points at a sibling that is
also Part II of the same document. Known cosmetic artifact, left deliberately --
rewriting it would alter source content, and NO CONTENT MAY BE LOST OR CHANGED BY A MERGE.

THE GENERAL CLAIM NOW STATED: whether management stabilises or destabilises a renewable
resource is decided by the latency of the institution, not the ecology alone -- and
jointly by how long the institution takes and in what form that delay is represented.
What does NOT transfer is stated first, because it is the more useful result: a stability
claim about a reviewed resource is NOT INTERPRETABLE UNTIL THE DECISION CLOCK IS
DECLARED, and THE OPERATOR AXIS AND THE PARAMETER AXIS ARE DIFFERENT AXES -- stability
across discretisation schemes (6.50-6.73 yr) says nothing about identifiability in the
parameters (0.87-10.67 yr, vanishing in 20 of 64 corners). Three things do transfer:
rule sign governs the effect of latency; faster assessment is not always safer;
periodicity alone cannot diagnose governance feedback (42-stock screen, 32-system search).

BUG HIT: NESTED BRACES IN \author. strip_front removed \author{...} with the regex
\{[^\}]*\}, which is NOT brace-balanced. Paper 8's author block contains nested braces
(\textsuperscript{1}, \href{..}{..}), so the match terminated at the first } and left
the affiliation tail as stray markup, producing "! LaTeX Error: There's no line here to
end." on a bare \\[0.35em] at line 148. Fixed with strip_cmd() / _match_brace(), which
do BALANCED-brace matching and skip matches inside comments. This is the same
non-nesting-class trap that produced the comment bug; the corpus has nested braces in
front matter and any structural operation must assume so.

VERIFICATION. Compiled with tectonic: 90 pages, 0 errors, 0 undefined references.
Rendered content checked by PDF text extraction for both Part markers, both original
abstracts, both systems' signature quantities (3.7 yr, 148.6-149.5, 6.5013,
0.87-10.67, the 42-stock screen and 32-system search), the section 3.5 sensitivity
heading, and the cross-regime conclusion.
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

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
]

MSG = """Prior art integrated into the manuscript: obstr_v56.tex

Both paragraphs are now IN the manuscript, not merely drafted beside it.

  Output: diffs/obstr_v56.tex (v55 untouched and preserved alongside).
  Location: the prior-art paragraph of section 2 Framework, beginning
  "The viability-theory background is Aubin (1991)".
  Doyen paragraph inserted after the Veliov / Quincampoix-Veliov /
  Cardaliaguet-Quincampoix-Saint-Pierre sentence, so it sits between the
  sufficiency direction and the "On the failure side" sentence: Veliov
  supplies sufficiency, Doyen supplies synthesis under partial observation,
  and the obstruction calculus takes up the side Doyen leaves open.
  HJ paragraph inserted after the barrier-certificate sentence, keeping the
  two verification traditions adjacent.
  Six bibliography entries added in correct alphabetical position. Reference
  block audited: 35 entries, sorted. The two apparent inversions are the
  manuscript's pre-existing Astrom-before-Abaee convention and a trailing
  funding/data-availability block caught by the audit filter.
  Net change: +801 words.

HOUSE-STYLE FINDING, load-bearing for any future manuscript edit:
obstr_v55.tex contains ZERO citation macros, no bibliography call and no
thebibliography environment. Citations are LITERAL author-year prose --
"(Aubin, 1991)", "Aubin and Frankowska (1990)" -- with double-backtick /
double-quote for quoted phrases, and the References section is a hand-written
alphabetized block inside a footnotesize group after the References
subsection. Inline math uses backslash-paren delimiters.
The draft prose in 8.1 and 8.2 was written with natbib commands (citep, citet,
citeyear) and would NOT have compiled; it was converted on insertion. Any
future prose for this manuscript must use the literal convention.

CAVEATS on added bibliography entries: Doyen (2000) is exact, taken from the
PDF header. Crandall-Ishii-Lions (1992), Mitchell-Bayen-Tomlin (2005) and
Margellos-Lygeros (2011) are recorded with journal, volume, issue and pages.
Bansal-Chen-Herbert-Tomlin (2017) and Bansal-Tomlin (2021) are given with
conference and year but PAGE NUMBERS OMITTED DELIBERATELY, because they could
not be confirmed and a wrong page number is worse than an absent one. All six
should be spot-checked against publisher records before submission.

Prior-art treatment is complete and integrated. Results section can be drafted.
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

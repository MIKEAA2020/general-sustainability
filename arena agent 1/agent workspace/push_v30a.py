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
    ("arena agent 1/agent workspace/diffs/paperB_ss1-5.tex", "/home/user/diffs/paperB_ss1-5.tex"),
    ("arena agent 1/agent workspace/diffs/paperB_cadence.tex", "/home/user/diffs/paperB_cadence.tex"),
]

MSG = """Paper B: sections 1-5 drafted from P5/P4/E2, plus the cadence survey

SECTIONS 1-5 (diffs/paperB_ss1-5.tex), built from the three source papers'
actual content rather than recollection:

  1 Introduction -- the decision clock; the two mechanisms; the three lines of
    evidence; and an explicit statement of what the paper does NOT claim.
  2 The decision clock: two mechanisms -- 2.1 review interval and
    sample-and-hold stability (two exact properties: forward invariance of the
    sampled state space, rapid-review consistency over finite horizons only;
    stability boundaries move or vanish when the operator is changed; the
    exact map crosses once near 6.5 yr while one-step approximations report
    artefact crossings and the protective channel is stable throughout);
    2.2 response delay (mobilising rule: two subcritical Hopf crossings
    interval-certified near 3.7 and 150 yr bound a window in which the lag
    itself stabilises the loop; protective rule: loop gain below one at the
    calibrated point, exponentially stable at every delay, a no-Hopf theorem,
    with the apparent 2.3-yr threshold a discretisation artefact; five-regime
    attractor topology with two folds certified at collocation level and a
    basin-boundary transition identified but not verified); 2.3 one idea, not
    two -- both enter the same loop at the same place, both set how stale the
    control is when applied.
  3 Evidence I: 42 stocks -- the null promoted to a result. Periodicity alone
    cannot diagnose governance feedback; a well-governed and a badly-governed
    stock can both be spectrally quiet.
  4 Evidence II: 32 cross-sector systems -- same design logic, same positive
    content.
  5 The cod certification -- the three constants (C* = 91.59 kt,
    g_max - |e| = 215.2 kt, a_max = F'(K*) = 1.1531); no-dominance as an
    identity; the finite horizon of six years under the two harsher floors and
    seven under the informative one; and the decisive property that NO catch
    reduction extends it -- it is the same for every admissible catch,
    including none at all. Carrying capacity not identified from above, stated
    plainly.

  Both caveats carried in the draft: the 6.5 yr figure is ill-conditioned
  (a two-hundredth-part change in the exploitation ratio moves it by more
  than half) and reads as a sensitivity band, not a point.

CADENCE SURVEY (diffs/paperB_cadence.tex), four bodies:

  IWC aboriginal subsistence whaling -- strike limits in SIX-YEAR BLOCKS,
    tested by SLAs simulated over 100 yr; established 2018, renewed 2024,
    due 2030. THE CADENCE ITSELF IS THE FINDING: until the 2018 reform the
    limits required a vote every TWO years. An institution deliberately moved
    its own decision clock, by making rollover automatic subject to three
    stated tests. First successful use 2024.
  NOAA -- management track assessments twice a year; each stock has its own
    cycle, some annual, most Mid-Atlantic/New England stocks two years,
    Hawaii three; research/benchmark tracks about every five years for
    important stocks like red snapper and up to A DECADE for others; ~500
    stocks managed, ~200 assessed per year; marine mammals annual if
    strategic, three-yearly if not.
  ICES -- ANNUAL advice, but the methodology behind it benchmarked every
    THREE TO FIVE YEARS, ~20 stocks per year, ACOM agreeing the programme a
    year ahead. Two clocks doing different jobs.
  MSC -- certification five years with ANNUAL surveillance; chain of custody
    three years with 12/18-month audits.

  Table sets each cadence against the 6-7 yr certified horizon: NOAA and ICES
  advice well inside; NOAA benchmark and MSC inside with little margin;
  IWC AT THE BOUNDARY; NOAA's decade-long gaps BEYOND.

  Scope stated plainly, applying the section 2.2 lesson: the table is a
  SURVEY OF CADENCES, not a set of certifications. The 6-7 yr horizon is a
  property of one stock under one protocol and does not transfer by
  inspection. What the comparison shows is that the question is live, not
  hypothetical.

  Gaps listed as open, not assumed: the tuna RFMOs, the EU CFP (annual TACs
  against multiannual plans), DFO Canada, and the Australian/New Zealand
  harvest-strategy frameworks.

House style honoured: all three sources use ZERO citation macros, the same
literal author-year convention as the obstruction manuscript. The draft
deliberately contains almost no external citations rather than invented ones;
Paper B's bibliography should be assembled by MERGING the three source
reference lists, not by writing new entries.
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

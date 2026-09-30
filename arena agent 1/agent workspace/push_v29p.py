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
    ("arena agent 1/agent workspace/fam/e2/graphical_abstract_e2.png",
     "/home/user/fam/e2/graphical_abstract_e2.png"),
    ("arena agent 1/agent workspace/fam/e2/graphical_abstract_e2_data.json",
     "/home/user/fam/e2/graphical_abstract_e2_data.json"),
    ("arena agent 1/agent workspace/make_graphical_abstract_e2.py",
     "/home/user/make_graphical_abstract_e2.py"),
    ("arena agent 1/agent workspace/check_ga_layout.py", "/home/user/check_ga_layout.py"),
    ("arena agent 1/agent workspace/audit_families.py", "/home/user/audit_families.py"),
    ("arena agent 1/agent workspace/audit_signatures.py", "/home/user/audit_signatures.py"),
    ("arena agent 1/agent workspace/CONSOLIDATION_AUDIT.md",
     "/home/user/CONSOLIDATION_AUDIT.md"),
    ("arena agent 1/agent workspace/FAMILY_CONSOLIDATION_PLAN.md",
     "/home/user/FAMILY_CONSOLIDATION_PLAN.md"),
]

MSG = """Graphical abstract, and an audit of what the consolidation would lose

Graphical abstract (fam/e2/graphical_abstract_e2.png, 2880x1639):
three panels built from the archived result files rather than by hand --
(1) K has no upper limit: the profile fit improves monotonically to the grid
edge at 50,000 kt, yet C* moves only 67.9 -> 95.2 kt over that 33-fold range;
(2) the certified horizon is 6/6/7 years for every catch <= 150 kt, including
zero; (3) the erosion margin grows geometrically at F'(K*) = 1.1531, so from
T = 4 one year of the decision clock costs more than any catch cut tested.
Every plotted value is re-derived from the archive and re-checked in the
battery (R27a-R27h), so the figure cannot drift from the manuscript.
check_ga_layout.py verifies the rendered geometry numerically -- text extents,
out-of-bounds artists, overlapping pairs -- because the figure cannot be
eyeballed during the build.

Consolidation audit (CONSOLIDATION_AUDIT.md): of the 16 concrete items in the
plan, 1 is closed. The audit found
  - the P1 slot names the wrong file: fam/arv_v9.tex and
    applied_regime_viability_v9.tex are the same manuscript (same title, both
    7,256 words), so the plan's P1 row duplicated the ARV row and left the real
    separation paper, paper1_assessment_separation_v63 (194 KiB, 42 sections),
    unmapped and headed for the archive;
  - five leads lag their families, one badly: p3_v32 (26,027 words) vs
    paper3_material_ledgers_v50 (36,387 words), a 40% expansion;
  - 17 revised_articles/A0xx modules (618 KiB) plus a 582 KiB theory manuscript
    mapped to no paper, several topically identical to P5/P4/P3;
  - the "other ~330 .tex files" to prune is really ~430 files in 79 families.
Recommendations for supplement delegation are per paper, and reuse the
supplements the family already has (paper3_supplementary_v18, 72 KiB;
paper2_obstruction_calculus_v29_supplementary, 48 KiB; companionA/B).
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

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
    ("arena agent 1/agent workspace/papers/MULTIDOC_SCAN.md",
     "/home/user/papers/MULTIDOC_SCAN.md"),
]

MSG = """Set-wide multi-document scan: all 11 papers now compile

Records the systemic defect found while remediating papers 9, 10 and 11, and
the final state of the set.

WHAT WAS FOUND. A scan of all LaTeX files found THREE merged files that were
actually multiple complete documents concatenated. In every case the \part
merge marker sat in the GAP BETWEEN DOCUMENTS -- outside any document -- which
is why the merge never worked:
    paper09_cod_certification_v30.tex        2 docs
    paper10_depletion_ledgers_v51.tex        2 docs
    paper11_forecasting_baselines_v61.tex    3 docs
Papers 1-8 were clean throughout.

WHY IT MATTERED. LaTeX stops at the first \end{document}. Every document after
that was SILENTLY DEAD TEXT -- no error, no warning, just missing pages. None
of v30, v51 or v61 compiled at all. In v30 and v51 there was a further fatal
cause: content (\part, \paragraph) sat BEFORE the first \documentclass, giving
"Missing \begin{document}".

AFTER THE SPLIT -- 7 papers, 189 pages recovered from 0:
    paper09_cod_certification_v31      35 pp  203967 B
    paper09b_arv_certification_v1       8 pp  165922 B
    paper10_depletion_ledgers_v52      55 pp  393179 B
    paper10b_edwards_aquifer_v1        17 pp  131022 B
    paper11_forecasting_baselines_v62  41 pp  240533 B
    paper11b_edwards_forecast_v1       21 pp  134496 B
    paper11c_worked_systems_audit_v1   12 pp  200939 B
All compile with ZERO errors and ZERO undefined references.

SPLIT CRITERION USED (the user's: "merge or split, depending on contents and
merit... is the work unified enough to merit a single paper?").
  Papers 9 and 10: split on ZERO vocabulary overlap and ZERO cross-reference.
    Paper 10's halves: ledger 135/0, Edwards 0/22, pumping 0/70. Shared a
    study system but no method, formalism, result set or literature.
  Paper 11: split into three on DIFFERENT evidence -- D1 and D2 DO share a
    method and DO cross-cite. Split anyway because the author already treats
    them as separate companion papers under separate review, each with its own
    Zenodo DOI, stating explicitly that scores are never pooled and no
    retention verdict is transferred. D3 ('ws') shares no vocabulary with
    either and is a separate unit in the authoritative eight-paper scope.

CURRENT SET STATE: 26 current-version files, ALL clean -- 1 \documentclass,
1 \begin{document}, 1 \end{document}, all \ref resolved. Three archived
originals (v30, v51, v61) intentionally preserved as multi-doc.

ROOT CAUSE. The 2026-09-29 partition assembled merged papers by NAIVE
CONCATENATION of complete LaTeX source files, leaving each file's
\documentclass, preamble, \begin{document}, \maketitle and \end{document} in
place and placing the \part markers outside all documents. No compile check was
run at assembly time.

RECOMMENDATION recorded in the file: compile-verify any future merge
immediately, and strip comments before grepping for control sequences -- a raw
grep over a file whose provenance header mentions them gives a FALSE POSITIVE.
That error was made once here and caught.
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

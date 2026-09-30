#!/usr/bin/env python3
"""Commit: restore unit 1, verify merges, close Phase 0, Phase 1 stale-value first pass."""
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
    ("arena agent 1/agent workspace/papers/paper01_obstruction_calculus_v63.tex",
     "/home/user/papers/paper01_obstruction_calculus_v63.tex"),
    ("arena agent 1/agent workspace/papers/split_paper01_unit1.py",
     "/home/user/papers/split_paper01_unit1.py"),
    ("arena agent 1/agent workspace/papers/PHASE0_MERGE_VERIFICATION.md",
     "/home/user/papers/PHASE0_MERGE_VERIFICATION.md"),
]

MSG = r"""Restore unit 1, verify merges, close Phase 0, run Phase 1 stale-value first pass

Four things, in dependency order.

1. RESTORED THE COMPUTATION. /home/user/repo was empty; RESTORE.md documents the deposit, and
   cloning branch e2-v3-source-year succeeded (6,407 files, 924 MB). wave_e_cod is readable,
   including src/superseded_v2, the v3 campaigns and the three verification scripts. Phase 1 is
   no longer gated on access.

2. FOUND AND FIXED A LOST SPLIT. The unit 1 / unit 2 split recorded from an earlier pass had
   never persisted: paper01_obstruction_calculus_v63.tex did not exist, and the head of paper01
   was v62 -- the container holding BOTH units (Part I 20,038 w, Part II 14,195 w) produced by
   merge_01_02.py from paper01_v61 + paper02_v12. Under the 11-unit architecture unit 1 was
   therefore still folded into unit 2.

   Fixed non-destructively with split_paper01_unit1.py. New paper01_obstruction_calculus_v63.tex
   (21,582 w): preamble re-scoped to unit 1, the \part* wrapper removed, Part I's own \maketitle
   and abstract retained, shared bibliography reproduced in full (an extra uncited entry is
   harmless, a missing one is not). The container v62 is untouched. Unit 2 remains
   paper02_probabilistic_sufficiency_v12.tex (13,380 w), unchanged.

   Verified by reading back: braces +0; document/abstract/enumerate/itemize/tabular/figure/table
   all balanced; 0 \part; exactly 1 \maketitle and 1 \title; labels=75 refs=34 dangling=0;
   99.92% of Part I 8-grams carried, the 18 missing being the removed \part* wrapper and its
   label/toc lines. The container's Part II was also diffed against paper02_v12: bibliography
   consolidation and label renaming only, so keeping v12 loses nothing.

3. PHASE 0 IS CLOSED. The residual "6.5 yr without its band" was a false alarm from a literal
   number check. paper07_v50 states the band in its ABSTRACT in prose -- "reported as a band,
   not a threshold: under a half-percent joint perturbation of the model parameters it ranges
   from under one year to nearly eleven" -- which a check for the numerals 0.87/10.67 scored as
   missing. paper08_v46 carries it in the lead, the body, the perturbation table and the close.
   The third finding, attributed to unit 10, does not exist: no file in unit 10 mentions a
   6.5-yr figure at all. No fix is owed on any of the three.

   The three merge units were also confirmed ALREADY MERGED and complete. v46, v32 and v64 are
   respectively the outputs of merge_08_07, merge_09_9b_10b and merge_11_11b. Markup-stripped
   8-gram coverage of sources in outputs is 91.7-98.6%, and the residual is concentrated in
   label renumbering (fig:cod -> prefixed, lem:bracket -> arv-lem:bracket), bibliography
   consolidation and merged declarations -- exactly the regions a merge must change. An earlier
   sentence-level diff reporting 104/87/54 sentences "not carried" was a splitting artifact:
   sentence breaks on [.!?] fracture LaTeX decimals and captions glued to markup.

4. PHASE 1 FIRST PASS -- SUPERSEDED-VALUE AUDIT, CLEAN. superseded_v2/README.md records that the
   v2 basis is a hybrid (parameters fitted under source-year, disturbance classes measured under
   destination-year), "not a convention", and must not be cited. The v2 -> v3 migration covers
   TEN quantities, not the four previously tracked: UC_min, UC_q05, UC_q10, residual SD, residual
   mean, residual max, lag-1 acf, vacuous classes, q05 BAU kernel at T=inf, constructive bound.

   All eleven unit heads scanned with digit-boundary regexes, each hit classified as live claim
   or documented migration by whether the v3 value appears alongside.

   RESULT: 0 live superseded-v2 claims. 2 documented-migration mentions, both in unit 8, which
   also cites three authoritative v3 values (-80.87, 0.554, 91.59). The stale-number residual is
   closed with evidence.

FIVE MEASUREMENT ARTIFACTS this pass, all the same failure mode -- literal matching without
semantic context: prior-art word counts; the fabricated Main & Randour DOI; the G.illcond numeral
check; "2 of 3" matching inside "12 of 36 pairs"; and v2 values appearing in v3 files where they
are the left column of a migration table. Every automated check in this workspace is a candidate
generator, never a verdict; each of these was caught by reading the hit in context before acting.

COMPILATION REMAINS UNVERIFIED -- no LaTeX toolchain obtainable this session (apt needs root,
tectonic release fetch returns a 9-byte non-gzip file). All checks above are static.
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

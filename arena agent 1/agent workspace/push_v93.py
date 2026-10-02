#!/usr/bin/env python3
"""Gate the merges: stop repairing output the pipeline regenerates.

Paper08's reference list was rebuilt by hand on 2026-10-01 -- 5 glued lines
split, 26 detached tails reattached to their heads, 5 duplicate entries removed,
the list re-sorted, the Supplementary material section lifted out of the middle
of the bibliography. All of it correct, and all of it temporary: a clean
re-merge of the same two sources reproduced every artifact.

So this commit does not touch the .tex. It fixes the layer above.

Diagnosis (empirical, not inferred):

  Sources are clean.  paper08 v45: 36 reference entries, 0 orphan tails.
                      paper07 v50: 37 entries, 0 orphan tails.
  The merge shreds them.  merge_08_07.py's split_entries() turns v45 into
                      30 entries / 14 orphans and v50 into 59 / 12.
  A clean re-merge reproduces the damage.  85 "entries", 26 orphan tails,
                      2 Declarations blocks, 2 Supplementary material passages,
                      the paper4_supplementary pointer. Every artifact.

Mechanism:

  split_entries() breaks on
      (?<=\.)\s+(?=[A-ZÄÖÅ][\w'{}\"~^- ]{1,30}?, )
  i.e. a period, whitespace, then "Word, ". That is exactly the shape of a
  book's publisher line, so "Introduction to Interval Analysis.\nSIAM,
  Philadelphia." becomes two "entries". It also misses real seams where the
  preceding token is a DOI or a bare page number, which is what glues one
  reference's tail to the next author's head.

  merge_refs() then sorts by re.sub(r'[^a-z]','',e.lower())[:24] -- the first
  24 alphanumeric characters. A detached tail sorts by PUBLISHER ("academicpress")
  while its head sorts by AUTHOR, which is why orphan tails sat alphabetically
  by journal while heads sat alphabetically by author. That is the mechanism,
  and it is generated here, not in the sources.

  Separately, every merge appends one Declarations block per source
  ("for d in (decl_a, decl_b)"), so merging N papers yields N Declarations
  blocks -- 2 in paper01/03/05/08/09v30, 3 in paper09 v32 and paper11 v61.
  Likewise one Supplementary material passage per source. The merges
  concatenate; they do not integrate.

One defect is NOT the script's: the paper4_supplementary_v8.md pointer is
present in paper08 v42, v43, v44 and v45 -- it predates every merge and is
inherited. It is still cross-unit contamination (unit 4's supplement inside
unit 7) and still wrong, but the fix belongs in v45, not in mergelib.

What this commit adds:

  phase0_scan.py -- classes H-L, the structural gate:
      H  more than one Declarations block
      I  more than one supplementary-material passage
      J  cross-unit paperNN_* file reference
      K  split bibliography entry (detached tail / glued / journal opener)
      L  duplicate bibliography key
    plus merge_gate(), gate_text() and report_gate() so a merge can check the
    document it just assembled. `phase0_scan.py --gate` exits non-zero.

  mergelib.py, merge_08_07.py -- call the gate before writing. If any fatal
    class fires the merge prints the findings and exits 1 WITHOUT writing the
    output, so a broken artifact is never emitted.

Calibration note: L.dup-ref-key is deliberately non-fatal. paper11 carries four
genuinely different Abaee 2026 works and paper08 carries two different DFO 2024
documents; those need a/b/c letters, not deduplication. Making that fatal
produced 176 failures, almost all false. Fatal set is H, I, J, K and L.dup-ref
(exact duplicates only), which gives 32 across the corpus.
"""
import base64
import json
import os
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT,
        "Accept": "application/vnd.github+json", "User-Agent": "e2-push"}

GOOD = "arena agent 1/agent workspace/p5/"
P5 = "/home/user/p5"

LOCAL = {
    "phase0_scan.py": P5 + "/phase0_scan.py",
    "mergelib.py": P5 + "/mergelib.py",
    "merge_08_07.py": P5 + "/merge_08_07.py",
}

MSG = __doc__.strip()


def api(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(BASE + path, data=data, headers=HDRS,
                                 method=method)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


base = api("GET", "/branches/" + BRANCH)["commit"]["sha"]
print("base commit: %s" % base[:10])
base_tree = api("GET", "/git/commits/" + base)["tree"]["sha"]

tree = []
for rel, local in sorted(LOCAL.items()):
    blob = api("POST", "/git/blobs",
               {"content": base64.b64encode(open(local, "rb").read()).decode(),
                "encoding": "base64"})
    tree.append({"path": GOOD + rel, "mode": "100644", "type": "blob",
                 "sha": blob["sha"]})
    print("  %8d B  +%s" % (os.path.getsize(local), GOOD + rel))

new_tree = api("POST", "/git/trees", {"base_tree": base_tree, "tree": tree})
commit = api("POST", "/git/commits",
             {"message": MSG, "tree": new_tree["sha"], "parents": [base]})
api("PATCH", "/git/refs/heads/" + BRANCH, {"sha": commit["sha"]})
print("pushed: %s" % commit["sha"][:10])

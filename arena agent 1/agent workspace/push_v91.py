#!/usr/bin/env python3
"""Record the cross-paper duplication audit covering all 55 pairs of units.

No paper text is changed: the scan found no substantive duplication between any
pair of papers.
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

GOOD = "arena agent 1/agent workspace/papers/"
PAPERS = "/home/user/papers"

LOCAL = {
    "PAIRWISE_DUP_AUDIT.md": PAPERS + "/PAIRWISE_DUP_AUDIT.md",
    "pairwise_dup.py": PAPERS + "/pairwise_dup.py",
}

MSG = r"""Record cross-paper duplication audit: all 55 pairs, no substantive duplication

The framework audit compared paper 1 against papers 2-5 only, leaving papers 6-11 and the
merged concatenations untested -- which is where duplication was most likely, since those
files were assembled from several sources. This covers every pair.

Result: 18 shared passages of 45+ words across all 55 pairs, and NOT ONE is body content.
Every shared passage falls into three categories, each of which every paper must carry on
its own:

  - shared bibliography entries (sibling citations such as "Abaee, 2026, An obstruction
    calculus..." in papers 1, 2, 4, 5, 11c; Baez 2023 and Fischer-Kowalski 2011 in papers
    6 and 10; Edwards Aquifer Authority and Water Data for Texas entries in papers 9 and 11).
    A reader of one paper cannot be sent to another for a citation.

  - declarations back-matter (papers 1 and 2, 129 words). Verified by inspection: paper01
    lines 2117-2131 and paper02 lines 1795-1806 are each file's own Declarations block.

  - the Lean verification provenance paragraph (papers 1, 4 and 5, 111-139 words). Three
    papers independently make mechanization claims; each reader needs the statement in the
    paper they are reading. It also carries the caveat that the build has not been re-run
    since the toolchain pin moved, which would be lost to two of the three papers if the
    paragraph were centralised.

No shared derivation, no repeated theorem, no duplicated argument, no repeated results
section anywhere in the eleven units.

This completes the de-duplication picture alongside the earlier audits: framework setup is
not duplicated (papers 2-5 cite paper 1); cross-paper body content is not duplicated;
within-paper duplicate bibliography entries were reduced (18 of 19 removed, the 19th left
because Brown 2012 in paper08 has Carpenter 2011 glued to it); and the one within-paper
duplicated block (paper11's CRediT statement repeated under the Funding heading) was
removed.

Still open and awaiting a decision, neither being de-duplication:
  - paper09's three AI declarations sit in three declarations blocks whose other content
    differs, so each belongs to its source paper; recommendation is to retain.
  - paper08's reference list needs repair (Carpenter 2011 glued to Brown 2012, an orphan
    "World Bank, Washington, DC." fragment, and a fragment glued to Astrom 1997).

Limitation, as with the framework audit: this tests verbatim overlap. A paraphrased
restatement would not be detected. Detecting that means reading the papers against one
another in full -- far more invasive than "de-duplicate only what is obvious" warrants.

Adds PAIRWISE_DUP_AUDIT.md and pairwise_dup.py. No paper text modified.
"""


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
    if not os.path.exists(local):
        print("  MISSING  %s" % local)
        continue
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

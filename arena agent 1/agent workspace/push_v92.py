#!/usr/bin/env python3
"""Reconstruct paper08's damaged reference list.

The list had been mangled by a mechanical failure: every entry was split into
(authors + title) and (journal + volume + pages + DOI / publisher), the two
halves were sorted separately -- heads by author, tails by journal name -- and
then merged back in that wrong order. That is why orphan tails sat
alphabetically by journal while heads sat alphabetically by author, and why
some lines carried the end of one reference and the start of the next.

Repairs, all mechanical or verified against the publisher:

  - split five glued lines (a stray Hocherman tail in front of Hutchinson 1948;
    Karlsson & Gilek's Ambio tail in front of Kuang 1993; Shertzer 2007 and
    Walters 1996; Brown 2012 and Carpenter 2011; a stray "Theoretical Ecology"
    fragment in front of Astrom 1997)
  - reattached 26 detached tails to their heads
  - removed five duplicate entries that had entered twice, once with a tail and
    once without (Adamson, Karlsson, Shertzer, Brown, Astrom)
  - removed six orphan fragments duplicating tails already reattached
  - folded four entries that were stranded in a second block after the
    Supplementary material prose back into the alphabetical list; Aiello 1990,
    Beretka 2020 and Carpenter 2011 exist nowhere else and are cited in the
    text, so they were moved rather than deleted
  - supplied five missing publishers (Springer, New York for Diekmann 1995,
    Guckenheimer & Holmes 1983 and Hale & Verduyn Lunel 1993; Cambridge
    University Press, Cambridge for Ostrom 1990 and Stuart & Humphries 1996)
  - moved the Supplementary material section out of the middle of the
    bibliography, where it split the list in two
  - sorted the list alphabetically

Two corrections caught by checking against the publisher rather than trusting
recall, both of which would have put a wrong journal on a cited work:

  - McManus et al. 2016 is ICES J. Mar. Sci. 73, 227-238, not Cadigan 2016;
    Cadigan 2016 is Can. J. Fish. Aquat. Sci. 73, 296-308.
  - Rose & Walters 2019 is Fisheries Research 219, 105314 (their "second
    opinion" on Northern cod); Marine Policy 109, 103695 is Sumaila et al.
    2019 on fisheries subsidies. The two had been crossed.

Result: 76 entries, no orphan tails, no glued lines, one alphabetical list.
Compiles clean with tectonic 0.15.0: PDF builds, 0 undefined references.

Adds PAPER08_REF_RECONSTRUCTION.md (the audit write-up), the repaired .tex, and
the four scripts used: recon_paper08.py (maps the damage), rebuild_paper08_refs.py
(reattaches tails), consolidate_paper08_refs.py (removes duplicates and folds the
stranded block back in), finalise_paper08_refs.py (moves the Supplementary
material section and sorts).

Not touched, and flagged for a decision:
  - paper08 carries two different Supplementary material passages. The
    \subsection{} one points at paper4_supplementary_v8.md and describes the
    A025 fold computation and MPF material; the \textbf{} one after the closing
    rule describes a different S1-S10 set (statement inventory, epistemic-layer
    results, case-screening records). They describe different supplements.
  - the file still has two \section*{Declarations} blocks, the second
    anonymized ("Anonymized for review.").
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
    "paper08_governance_delay_v46.tex": PAPERS + "/paper08_governance_delay_v46.tex",
    "recon_paper08.py": PAPERS + "/recon_paper08.py",
    "rebuild_paper08_refs.py": PAPERS + "/rebuild_paper08_refs.py",
    "consolidate_paper08_refs.py": PAPERS + "/consolidate_paper08_refs.py",
    "finalise_paper08_refs.py": PAPERS + "/finalise_paper08_refs.py",
    "PAPER08_REF_RECONSTRUCTION.md": PAPERS + "/PAPER08_REF_RECONSTRUCTION.md",
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

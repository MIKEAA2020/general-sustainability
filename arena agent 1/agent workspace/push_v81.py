#!/usr/bin/env python3
"""Commit: CORRECTION to the proof audit -- supplements 6/7/9 DO exist."""
import base64
import json
import os
import urllib.request

OWNER, REPO, BRANCH = "MIKEAA2020", "general-sustainability", "e2-v3-source-year"
PAT = open("/home/user/uploads/github_pat.txt").read().strip()
BASE = "https://api.github.com/repos/%s/%s" % (OWNER, REPO)
HDRS = {"Authorization": "Bearer " + PAT, "Accept": "application/vnd.github+json",
        "User-Agent": "e2-push"}
PFX = "arena agent 1/agent workspace/"

FILES = ["papers/PROOF_AUDIT.md"]

MSG = r"""Proof audit: RETRACT the "supplements do not exist" finding -- they do

An earlier reading of this audit reported that units 6, 7 and 9 carried 75 pointers to
supplementary sections that do not exist. That is WRONG and is retracted here. The supplements
exist. They are filed under the OLD paper numbering (paper1-paper5), which a search scoped to
the NEW unit filenames (paper06, paper08, paper10) could not see. A content search for "S13.3" --
a section only unit 7 cites -- located them immediately.

WHAT EXISTS:
  unit 1 -> paper2_obstruction_calculus_v51_Automatica_routes_supplementary.tex   85,563 B
  unit 6 -> paper1_supplementary_v12.md                                           36,553 B
  unit 7 -> paper5_supplementary_v19_NatSustain.md                                77,327 B
  unit 9 -> paper3_supplementary_v18.tex (also .md)                               73,881 B

Corroboration that each is the right file, not a lookalike: unit 9's supplement "Accompanies"
line is character-identical to paper10_v53's \title, and its unusual cited sections S5.4 and S17
are present. Unit 7's supplement carries exactly the thirteen sections the main text cites,
including S13.1, S13.2 and S13.3. Unit 1's v51 main and v63 main contain IDENTICAL sets of 21
claims by (type, name) -- zero added, zero dropped -- so the v51 supplement still fits.

CORRECTED TALLY: 74 of 75 supplement pointers resolve. Exactly ONE does not.

THE ONE DEAD POINTER. Unit 7 L1207 cites "Supplementary S9.5" for the registered compute-core
Hopf pair 3.666149 / 150.358477 yr. The supplement has S9.1 and S9.2 but no S9.5. Checked across
every available version (v14-v20): S9.5 occurs ZERO times in all of them, and neither "compute
core" nor those values appear anywhere in v19. That content has never been written. One pointer,
not 44.

UNIT 7 MUST USE v19, NOT v20. v20 is headed "Blinded review copy... Accompanies blinded main
v47" and substitutes "citation blinded for review" and [repository] for real citations and paths.
The v19-v20 diff is 27 lines, all blinding. Unit 7's main is the UNBLINDED v46, so v19 is the
match.

STALENESS. Only unit 1 is demonstrably stale: its main advanced from v51 to v63 and no supplement
was produced after v51 -- a content search for "Complete proof of the selector principle" returns
v47-v51 and nothing later. 12 versions behind. Version numbers are NOT comparable across lineages
(unit 9's main is v53 while its supplement is v18), so the other rows rest on content checks.

Two section citations resolve as bolded body text rather than headings -- unit 7's S2.3 and unit
9's S2.1 -- so a heading-only scan falsely reports them missing. Both counted as resolved.

UNCHANGED FROM THE FIRST AUDIT: Finding A stands. Of 112 claim environments, exactly one has no
evidence of proof of any convention: unit 1's selector principle (calc-prop:selector, L609-L630),
while section 1.2 Contributions claims "each with a complete proof". Five of the eight flags were
instrument artifacts (deferred proofs, embedded proofs, unmarked prose proofs) and three are unit
4's house style for computed results.

ERROR LOG. The retracted finding came from a filename regex scoped to new unit names. Filename
matching proves nothing when the naming scheme may differ. A null result from a scoped search is
not evidence of absence -- all 166 supplement-like files were one listing away. Note the direction:
a too-narrow search INFLATED the defect count from 1 to 75, the same direction as earlier errors
of this class.

Remediation (section 7, nothing edited yet): recover unit 1's v51 supplement with a figure
numbering fix so its S4 figures render S1/S2/S3; attach v19 for unit 7; resolve or remove S9.5;
attach the unit 6 and 9 supplements and update unit 6's stale "Accompanies" title.
"""


def api(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(BASE + path, data=data, headers=HDRS, method=method)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


base = api("GET", "/branches/" + BRANCH)["commit"]["sha"]
print("base commit: %s" % base[:10])
base_tree = api("GET", "/git/commits/" + base)["tree"]["sha"]

tree = []
for f in FILES:
    blob = api("POST", "/git/blobs",
               {"content": base64.b64encode(open(f, "rb").read()).decode(),
                "encoding": "base64"})
    tree.append({"path": PFX + f, "mode": "100644", "type": "blob",
                 "sha": blob["sha"]})
    print("  %8d B  %s" % (os.path.getsize(f), f))

new_tree = api("POST", "/git/trees", {"base_tree": base_tree, "tree": tree})
commit = api("POST", "/git/commits",
             {"message": MSG, "tree": new_tree["sha"], "parents": [base]})
api("PATCH", "/git/refs/heads/" + BRANCH, {"sha": commit["sha"]})
print("pushed: %s" % commit["sha"][:10])

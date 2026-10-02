#!/usr/bin/env python3
"""Commit: attach the four recovered supplements (units 1, 6, 7, 9)."""
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

FILES = ["papers/PROOF_AUDIT.md",
         "papers/paper01_obstruction_calculus_v63_supplementary.tex",
         "papers/paper06_assessment_separation_v67_supplementary.md",
         "papers/paper08_governance_delay_v46_supplementary.md",
         "papers/paper10_depletion_ledgers_v53_supplementary.tex",
         "papers/supprec/build_unit1_supp.py",
         "papers/supprec/build_supp_679.py"]

MSG = r"""Attach the four recovered supplementary files (units 1, 6, 7, 9)

Recovers and attaches every supplement the family's units point at, following the correction
pushed in 80f36d5a5f. Four files, four units, 74 of 75 supplement pointers now resolve.

UNIT 1 -- paper01_obstruction_calculus_v63_supplementary.tex (85,852 B)
Recovered from paper2_obstruction_calculus_v51_Automatica_routes_supplementary.tex, the newest
supplement that exists; the main text advanced v51 -> v63 with none produced after v51. It still
fits: v51 main and v63 main carry identical 21-claim sets by (type, name). Only three changes:
retitled to v63's \title; the \author line dropped (v63 has none); and \renewcommand{\thefigure}
{S\arabic{figure}} inserted immediately before S4 so the "Additional figures" render S1/S2/S3 and
match the main text's Figure~S1 (obstruction ladder) and Figure~S2 (obstruction tree). The fibre
figure earlier in the document keeps ordinary numbering, so it does not consume an S-slot -- this
is why the reset sits before S4 rather than in the preamble. Carries S1. Complete proofs,
including the complete proof of the selector principle, which is the one claim in the family with
no proof of any convention in its main text while section 1.2 claims "each with a complete proof".

UNIT 7 -- paper08_governance_delay_v46_supplementary.md (77,346 B)
Uses v19, the UNBLINDED supplement, not v20. v20 is headed "Blinded review copy... Accompanies
blinded main v47" and substitutes "citation blinded for review" and [repository] for real
citations and paths; the v19-v20 diff is 27 lines, all blinding. Unit 7's main is the unblinded
v46, so v19 is the match.

UNITS 6 AND 9 -- paper06_assessment_separation_v67_supplementary.md (36,555 B) and
paper10_depletion_ledgers_v53_supplementary.tex (73,881 B)
Both carried superseded "Accompanies" titles. Unit 6's still read "Aggregate Indices and
Transition Safety..." though the main text is now "Aggregation is a claim, not a presentation...";
updated in both the H1 and the Accompanies line. Unit 9's title now states it is supplementary
material. Unit 9 needed no attribution change: its Accompanies line was already character-identical
to the main text's \title, and it carries author and ORCID.

VERIFIED on all four: braces balanced, no dangling \ref, environments balanced, and the two .tex
files standalone (documentclass -> \begin{document} -> \end{document}). Two instrument slips were
caught in the verification itself: the standalone test initially read the file CONTENT instead of
the FILENAME, so it never ran and reported "n/a" for the .tex files; fixed and re-run.

ONE ITEM LEFT OPEN -- unit 7, Supplementary S9.5. Unit 7 L1207 attributes the registered
compute-core Hopf pair 3.666149 / 150.358477 yr to "the recovered compute core (Supplementary
S9.5)". S9.5 has never existed: checked v14-v20, zero occurrences in all of them, and neither
"compute core" nor those values appear anywhere in v19. This is not fabricable here -- writing it
needs the compute-core artifact, and removing the parenthetical removes a claim attribution, which
is a content decision for the author. It is left as-is and flagged rather than patched, so the
dangling pointer stays visible instead of being papered over.

Compilation remains unverified; no TeX engine is available and all checks are static.
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

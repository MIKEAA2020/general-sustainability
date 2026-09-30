#!/usr/bin/env python3
"""Commit: fix the split bibliographies, and apply unit 6's two prior-art citations."""
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
    ("arena agent 1/agent workspace/papers/paper06_assessment_separation_v67.tex",
     "/home/user/papers/paper06_assessment_separation_v67.tex"),
    ("arena agent 1/agent workspace/papers/paper05_exact_belief_computation_v16.tex",
     "/home/user/papers/paper05_exact_belief_computation_v16.tex"),
    ("arena agent 1/agent workspace/papers/split_parts.py",
     "/home/user/papers/split_parts.py"),
    ("arena agent 1/agent workspace/papers/PRIOR_ART_PASS.md",
     "/home/user/papers/PRIOR_ART_PASS.md"),
]

MSG = r"""Repair the split bibliographies; apply unit 6's two prior-art citations (Kuhn, Wei-Zhang)

THE FIRST SPLIT SILENTLY DROPPED THE ENTIRE REFERENCE LIST. Both containers keep ONE shared
bibliography at the very end of the document, inside Part II's character range, even though it
serves both parts. The split therefore produced files with no bibliography at all.

This was nearly missed, and for an instructive reason: THESE PAPERS USE NO \cite COMMANDS.
Citations are literal inline text ("(Ben-Tal, Goryashko, Guslitzer and Nemirovski, 2004)").
A missing list produces no ? marker and no LaTeX warning -- it is invisible until the end of
the document, and fatal for publication.

TWO FURTHER SOURCE DEFECTS SURFACED WHILE EXTRACTING IT:

  (a) paper06's list is FRAGMENTED. It runs A..V, is interrupted by a \section{Supplementary
      material}, then resumes with a SECOND \label{references} block -- a duplicate label that
      would raise "multiply defined" in LaTeX. A "stop at the next heading" rule truncates it:
      86 of 109 entries, leaving Sion 1958, Saint-Pierre 1994, Schaefer 1954, Solow 1974,
      Roy 1996 and Vincke 1992 all unresolved.
  (b) A shape-based filter on "Surname, X." is ALSO too strict. It drops institutional authors
      with no comma ("DFO. (2016).", "World Bank. (2011)."), lowercase nobiliary prefixes
      ("von Neumann, J. (1928)."), and LaTeX accents ("Schar, S., Pohl, E., and Geldermann,
      J. (2025)."). All four are cited by Part I and all were verified present in the source.

 RESOLUTION: capture from the References heading to the Declarations section, then keep the
 heading plus every paragraph matching "Surname, X." OR containing a parenthesised year --
 bibliography entries essentially always carry a year, supplementary prose mostly does not.

                                container    first split    final split
   paper05 -> unit 5 bib entries      22          0              22
   paper06 -> unit 6 bib entries     109       0 -> 86 -> 108   109
   unit 6 unresolved citations         -         15          0 real (2 regex false positives)
   \label{references}                  2 (dup)     -             1
   supplementary sections leaked        -          -             0

UNIT 6 CITATION FIXES APPLIED to paper06_assessment_separation_v67.tex.

  1. WEI, N. AND ZHANG, P. (2024), "Adjustability in robust linear optimization", Math.
     Program. 208(1-2), 581-628, DOI 10.1007/s10107-023-02049-w. Added to the "Adjustable and
     randomized robust optimization" subsection, replacing the mis-attribution to Bertsimas and
     Goyal (2012) -- a paper about affine policies that does not give the zero-adjustability
     condition. Wei and Zhang give a necessary and sufficient theorem-of-the-alternatives for
     adjustability to be zero, which is this paper's quantifier question from the opposite face.
     Distinction stated on three axes: objective value vs feasibility; polyhedral uncertainty
     sets vs the present setting; characterising when the commutation CLOSES vs exhibiting when
     it FAILS with nonempty interior.
  2. KUHN'S THEOREM, 343-word paragraph. States the objection in the reader's own terms and
     answers it: mixed and behavioural strategies are realization-equivalent under perfect
     recall (Kuhn 1953), which on its face contradicts Theorem 9. It does not, because Kuhn's
     equivalence is an equality of DISTRIBUTIONS OVER PATHS under an EXPECTED criterion, while
     the certified constraint is PATH-WISE. Convexification must occur WITHIN a step;
     alternation varies ACROSS steps, so it never convexifies. MAIN AND RANDOUR (2024) added
     as reinforcement from the other side: Kuhn's equivalence FAILS OUTRIGHT under finite
     memory, which is this paper's setting, so the classical theorem does not apply even before
     the worst-case criterion is imposed.

Three bibliography entries added in each paper's own flat hand-formatted style, anchored on the
alphabetically-following entries: Kuhn after Krause; Main after Lygeros; Wei after von Neumann.

VERIFIED AFTER EDIT: all six checked citations resolve (Kuhn 1953, Main 2024, Wei 2024,
Krause 2011, Kobayashi 2023, Sion 1958); braces balanced in every inserted passage and in the
whole file (1824/1824); one \begin{document} and one \end{document}. Unit 6 is now 27,325 w
(24,799 w before the fixes).

PROCESS NOTE RECORDED IN THE SOURCE FILE. Main and Randour was first recorded as Games and
Economic Behavior with DOI 10.1016/j.geb.2024.05.004. THAT DOI WAS FABRICATED -- inferred from
a PII prefix that was misread -- and the journal was wrong. Both were corrected by Crossref
lookup before insertion (Information and Computation 301, 105229, DOI 10.1016/j.ic.2024.105229).
Under a no-withdrawal target an invented DOI would have been permanent, so no citation goes
into a source file unverified. All three new citations were Crossref-verified: Kuhn (Contributions
to the Theory of Games AM-28 Vol. II, 193-216, DOI 10.1515/9781400881970-012), Main and Randour,
Wei and Zhang.

COMPILATION IS STILL UNVERIFIED -- no LaTeX toolchain is available in this session (apt needs
root; the tectonic binary could not be fetched). This is recorded as residual risk.
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

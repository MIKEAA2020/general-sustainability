#!/usr/bin/env python3
"""Build paper2 v26 from v25.

v26 = v25 + three literature-grounding citations (all non-decorative):
  - Nagumo (1942): the manuscript names "Nagumo's theorem" without a
    reference-list entry; added at its formal invocation in Section 2.2.
  - Kurzhanski & Valyi (1997): the set-membership information set B_t of
    Section 2.3 is the guaranteed-estimation object; grounded directly.
  - Smallwood & Sondik (1973): Section 3.5's belief recursion is the
    set-membership analogue of the POMDP belief-state recursion, and the
    paper already contrasts with probabilistic formulations (Section 6.5).
All three entries are cited in the text (no orphans).  No statement,
hypothesis, equation, numbering, or figure is changed.  The corrected
figures (timing, CE trap, obstruction tree) are separate assets regenerated
by make_figures_p2_v26.py and are picked up at compile time.
"""
import re

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v25.tex"
DST = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v26.tex"

with open(SRC, encoding="utf-8") as f:
    s = f.read()

CITATIONS = [
    ("We assume the standard set-membership semantics, so that",
     "We assume the standard set-membership semantics (Kurzhanski and V\\'alyi, 1997), so that"),
    ("by Nagumo's theorem in its robust form",
     "by Nagumo's theorem (Nagumo, 1942) in its robust form"),
    ("backward recursion over beliefs is sound and complete on any finite horizon",
     "backward recursion over beliefs --- the set-membership analogue of the belief-state recursion of partially observable Markov processes (Smallwood and Sondik, 1973) --- is sound and complete on any finite horizon"),
]

REFS = [
    ("Maghenem, M., Sanfelice, R.G.: Characterizations of safety in hybrid",
     "Kurzhanski, A.B., V\\'alyi, I.: Ellipsoidal Calculus for Estimation and\nControl. Birkh\\\"auser, Boston (1997)\n\nMaghenem, M., Sanfelice, R.G.: Characterizations of safety in hybrid"),
    ("Prajna, S., Jadbabaie, A.: Safety verification of hybrid systems using",
     "Nagumo, M.: \\'Uber die Lage der Integralkurven gew\\'ohnlicher\nDifferentialgleichungen. Proc. Phys.-Math. Soc. Japan 24, 551--559\n(1942)\n\nPrajna, S., Jadbabaie, A.: Safety verification of hybrid systems using"),
    ("Sontag, E.D.: Mathematical Control Theory: Deterministic Finite",
     "Smallwood, R.D., Sondik, E.J.: The optimal control of partially\nobservable Markov processes over a finite horizon. Oper. Res. 21(5),\n1071--1088 (1973)\n\nSontag, E.D.: Mathematical Control Theory: Deterministic Finite"),
]

def sub_ws(old, new, tag):
    global s
    pat = re.compile(r"\s+".join(map(re.escape, old.split())))
    m = list(pat.finditer(s))
    assert len(m) == 1, f"{tag}: expected 1 match, found {len(m)}"
    s = s[:m[0].start()] + new + s[m[0].end():]

for old, new in CITATIONS:
    sub_ws(old, new, "citation")

for old, new in REFS:
    # reference anchors are single-line and exact; use plain count+replace
    assert s.count(old) == 1, f"ref anchor not unique: {old[:40]}"
    s = s.replace(old, new)

with open(DST, "w", encoding="utf-8") as f:
    f.write(s)

print("wrote", DST, len(s), "bytes")

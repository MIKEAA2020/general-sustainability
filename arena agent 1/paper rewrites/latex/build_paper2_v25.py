#!/usr/bin/env python3
"""Build paper2 v25 from v24: a faithful prose humanization.

Reads the landmark register (Aubin & Catte 2002, Set-Valued Analysis;
Prajna-Jadbabaie-Pappas 2007, IEEE TAC) and smooths the genuinely stilted
sentences of the manuscript into the same active, first-person, concrete
voice.  Every edit is PROSE-ONLY: the old and new strings contain no
backslashes, dollar signs, ampersands, or percent signs, so no mathematics,
label, citation, or reference can be touched.  All statements, hypotheses,
equations, numbering, figures, and the abstract are preserved verbatim.
"""
import re, sys

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v24.tex"
DST = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v25.tex"

with open(SRC, encoding="utf-8") as f:
    s = f.read()

EDITS = [
    # ---- Section 1.1: the problem ----
    ("The question has a natural split.",
     "The question splits naturally."),
    ("For sustainability problems the constraint set is a set of floors --- stock levels, service thresholds, safety margins --- and viability is the formal counterpart of the requirement that a development path be maintained rather than merely optimized",
     "For sustainability problems the constraints are floors --- stock levels, service thresholds, safety margins --- and viability is the formal counterpart of maintaining a development path rather than merely optimizing it"),
    ("Viability theory characterizes the states of a constrained control system from which there exists at least one control keeping every future state within a constraint set",
     "Viability theory characterizes the states of a constrained control system from which at least one control can keep every future state within a constraint set"),
    ("This paper addresses that side: under an incomplete observation structure, it develops instruments for certifying that no observation-based policy is viable --- establishing infeasibility for reasons of information rather than of dynamics.",
     "This paper addresses that side: for an incomplete observation structure, it develops instruments that certify that no observation-based policy is viable --- that the infeasibility is due to the information structure, not to the dynamics."),
    ("Incompleteness of observation is therefore a structural feature of the certification problem, not merely a practical limitation; the sufficiency literature and the obstruction calculus of this paper address the same underlying indeterminacy rather than competing ones.",
     "Incomplete observation is therefore structural to the certification problem, not merely a practical limitation; the sufficiency literature and the obstruction calculus of this paper address the same underlying indeterminacy rather than competing ones."),
    ("An obstruction certificate --- a checkable witness that no observation-based policy exists, finite in the polyhedral and finite-fibre cases --- is an argument that a prescribed class of observation-based policies fails, not because a particular policy is bad, but because the information structure leaves no room for any policy.",
     "An obstruction certificate is a checkable witness that no observation-based policy exists --- finite in the polyhedral and finite-fibre cases --- and the argument it makes is that a prescribed class of observation-based policies fails not because a particular policy is bad, but because the information structure leaves no room for any policy."),
    # ---- Section 1.3: related work ----
    ("The viability theory background is Aubin (1991) and Aubin, Bayen, and Saint-Pierre (2011); approximation of kernels is due to Saint-Pierre (1994).",
     "The viability-theory background is Aubin (1991) and Aubin, Bayen, and Saint-Pierre (2011); the approximation of kernels is due to Saint-Pierre (1994)."),
    ("the elementary facts on which they rest (quantifier commutation; Dini comparison) are classical.",
     "the elementary facts on which they rest (quantifier commutation and Dini comparison) are classical."),
    # ---- Section 1.4: organization ----
    ("Section 5 reviews the sufficiency landscape, which this paper does not re-derive, with citations.",
     "Section 5 reviews the sufficiency landscape, cited rather than re-derived."),
    # ---- Section 3.1: exit certificate ----
    ("In management terms: when the dynamics themselves force exit before any control can react, no monitoring design can rescue viability, and the certification problem is closed without any observation-theoretic reasoning.",
     "Put in management terms, when the dynamics themselves force exit before any control can react, no monitoring design can rescue viability, and the certification problem is closed without observation-theoretic reasoning."),
    # ---- Section 3.2: epistemic emptiness ----
    ("In ecological terms, this is the situation in which each stock, considered on its own, is manageable; the failure arises because the indicator cannot tell the manager which stock is present.",
     "In ecological terms, each stock is manageable on its own; the failure arises because the indicator cannot tell the manager which stock is present."),
    # ---- Section 4.1: fibre criterion ----
    ("For a manager operating under partial ecological information, this is the question of whether an indicator reading alone can ever settle that the system is, or is not, on the safe side of a specified floor.",
     "For a manager operating under partial ecological information, the question is whether an indicator reading alone can ever settle whether the system is on the safe side of a specified floor."),
    # ---- Section 7: conclusion ----
    ("Viability under perfect measurement has, under standard finite-dimensional regularity assumptions, a mature kernel, tangency, and approximation theory.",
     "Under standard finite-dimensional regularity assumptions, viability under perfect measurement has a mature kernel, tangency, and approximation theory."),
    ("This paper supplies the missing instrument: the obstruction calculus develops sound, computationally interpretable certificates for nonviability --- sufficient conditions for nonviability, equivalently necessary conditions for viability.",
     "This paper supplies the missing instrument: the obstruction calculus develops sound, computationally interpretable certificates for nonviability --- that is, sufficient conditions for nonviability, equivalently necessary conditions for viability."),
    # ---- Appendix A ----
    ("The following bounded constructions complement the obstruction theorems of Sections 3--4. They are stated in full with their scope remarks.",
     "The bounded constructions below complement the obstruction theorems of Sections 3--4. They are stated in full, together with their scope remarks."),
]

for i, (old, new) in enumerate(EDITS):
    assert "\\" not in old and "$" not in old and "&" not in old and "%" not in old, f"edit {i}: old not prose-only"
    assert "\\" not in new and "$" not in new and "&" not in new and "%" not in new, f"edit {i}: new not prose-only"
    pat = re.compile(r"\s+".join(map(re.escape, old.split())))
    matches = list(pat.finditer(s))
    assert len(matches) == 1, f"edit {i}: expected 1 match, found {len(matches)}: {old[:70]}"
    m = matches[0]
    s = s[:m.start()] + new + s[m.end():]

with open(DST, "w", encoding="utf-8") as f:
    f.write(s)

print("wrote", DST, len(s), "bytes")

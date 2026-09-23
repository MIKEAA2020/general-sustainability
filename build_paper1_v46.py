#!/usr/bin/env python3
"""
v46 — alignment, tone, and delegation pass for paper 1.

1. Abstract: one added sentence (benchmark, exact verification, unit
   anchoring, translation guide); still under the 265-word limit.
2. Tone/hedge pass (the three in-text hits of the scan, plus one):
   - 4.12 opening "We emphasize what the instantiation is and is not..."
     rewritten as a single formal scope sentence (deduplicated with the
     data-anchor qualifications, which are tightened separately);
   - "Three caveats keep the claim honest" -> "Three qualifications apply",
     with the duplicated scope clause removed;
   - run-in "What the reader should see." -> "The dashboard reading.";
   - run-in "What the abstraction buys a modeller." -> "The case for the
     abstraction."
3. Proposition (rescue threshold) numbered as Proposition 10 (next in the
   paper-wide sequence after Proposition 9); the contribution list reference
   updated accordingly.
4. Delegation: Section 5.2's per-literature exegesis (commensurability
   foundation, maximin formulations, compensability mapping) moved to a new
   Supplementary section S10; the main text keeps the condensed positioning
   with all citations intact and a pointer to S10. The Supplementary Material
   pointer is extended accordingly.

No theorem, reference, or figure content is lost (audit: all v29 sections,
manual theorem numbers, and references retained — the only reference-form
changes are the standing rule's replacement of the 2026a/b/c shorthand with
full titles and DOIs). v45 is left untouched.
"""

LATEX = "/home/user/arena agent 1/paper rewrites/latex"
SRC = f"{LATEX}/paper1_assessment_separation_v45.tex"
DST = f"{LATEX}/paper1_assessment_separation_v46.tex"

OLD_HEADER = "% Amin Abaee. Revision v45 (layout and accessibility pass: wider text block, paragraph breaks, Fig. 4 annotation fix, terminology translation table 5.3, benchmark units anchored to DFO 2016 Northern cod LRP; master deposit DOI 10.6084/m9.figshare.33764023). Compiles with tectonic, pdflatex, or xelatex."
NEW_HEADER = "% Amin Abaee. Revision v46 (alignment pass: abstract extended to the benchmark and translation guide, tone formalized, rescue-threshold result numbered Proposition 10, positioning exegesis delegated to Supplementary S10; master deposit DOI 10.6084/m9.figshare.33764023). Compiles with tectonic, pdflatex, or xelatex."

ABSTRACT_ADD = """A resource-transition benchmark realizes the datum as a fishery
transition --- pulse, sustained-yield, and reserve-financed staged plans
under a heatwave disturbance --- with every value verified in exact
rational arithmetic and units anchored to a regulated biomass limit; a
terminology guide maps the results onto decision-analysis,
control-theoretic, and environmental vocabulary.

"""

SCOPE_OLD = """We emphasize what the instantiation is and is
not: it is an exact rational re-reading of the witness datum in the
domestic language of a Schaefer (1954) production model --- every number
below is verified symbolically by the deposited benchmark script, twenty-four
checks reproducing the figures quoted here --- and the certified tubes are
shown to be conservative for the nonlinear realization by an exact
inequality; it is not a calibrated case study of a specific fishery, and no
empirical claim is made."""
SCOPE_NEW = """The instantiation is an exact rational re-reading of the witness
datum in the domestic language of a Schaefer (1954) production model:
every number below is re-derivable from the deposited benchmark script,
which verifies it in exact rational arithmetic, and the certified tubes
are conservative for the nonlinear realization by an exact inequality. It
is not a fitted case study, and no empirical claim is made."""
SCOPE_NEW = """The instantiation is an exact rational re-reading of the witness
datum in the domestic language of a Schaefer (1954) production model:
every number below is re-derivable from the deposited benchmark script,
which verifies it in exact rational arithmetic, and the certified tubes
are conservative for the nonlinear realization by an exact inequality. It
is not a fitted case study, and no empirical claim is made."""

CAVEATS_OLD = """Three caveats keep the claim honest. This is an anchoring of units, not a
fitted case study: no parameter of the rational witness is estimated from
data. The paper's theorems therefore say nothing predictive about this or any
other stock."""
CAVEATS_NEW = """Three qualifications apply. The anchoring fixes units only: no
parameter of the rational witness is estimated from data, and the
theorems say nothing predictive about this or any other stock."""

DELEGATE_OLD = """The foundation statement that values may be only
weakly comparable --- and that this incommensurability is constitutive
of ecological economics --- is due to Martinez-Alier, Munda, and O'Neill
(1998). Our operators give one formal model of the distinction that
paper draws between strong and weak commensurability. The
characterization of which sustainability criteria admit indicator
representations, and the role of maximin and MSY-type reasoning in
making strong sustainability operational, are developed in Martinet
(2011), Cairns and Martinet (2014), and Doyen and Gajardo (2020). The
latter in particular shows that the multicriteria maximin value is the
solution of a static Pareto problem over the viability kernel, which is
the strongest formal statement in the literature of the position ---
strong sustainability as constraint viability rather than optimality ---
that the typed operator formalizes here.

Static scalarization
limitations are established: weighted sums cannot reach nonconvex parts
of Pareto fronts (Das and Dennis, 1997), a mechanism of frontier
geometry under a single optimization, different from the
action-quantifier mechanism of this paper. Compensability analysis is
established in multi-criteria decision analysis, including the explicit
mapping of compensatory aggregation to weak sustainability and
outranking methods to strong sustainability (Cinelli, Coles, and Kirwan,
2014; Sch\\\"ar, Pohl, and Geldermann, 2025). Scalarization-dependent
optimal policies are a staple of multi-objective optimization."""
DELEGATE_NEW = """Static scalarization limitations --- weighted sums that cannot
reach nonconvex parts of Pareto fronts (Das and Dennis, 1997) --- act
through frontier geometry under a single optimization, a mechanism
distinct from the action-quantifier mechanism established here. The
per-literature details --- the commensurability foundation
(Martinez-Alier, Munda, and O'Neill, 1998), the maximin and indicator
formulations of strong sustainability (Martinet, 2011; Cairns and
Martinet, 2014; Doyen and Gajardo, 2020), and the compensability mapping
in multi-criteria decision analysis (Cinelli, Coles, and Kirwan, 2014;
Sch\\\"ar, Pohl, and Geldermann, 2025) --- are collected in the
Supplementary Material (S10)."""


def replace_once(text, old, new, what):
    n = text.count(old)
    assert n == 1, f"{what}: expected exactly 1 occurrence, found {n}"
    return text.replace(old, new)


def main():
    t = open(SRC, encoding="utf-8").read()

    t = replace_once(t, OLD_HEADER, NEW_HEADER, "header comment")

    t = replace_once(
        t,
        "impossible.\n\n\\end{abstract}",
        "impossible.\n\n" + ABSTRACT_ADD + "\\end{abstract}",
        "abstract addition")

    t = replace_once(t,
        "\\noindent\\textbf{What the abstraction buys a modeller.}",
        "\\noindent\\textbf{The case for the abstraction.}",
        "1.1 run-in")
    t = replace_once(t, SCOPE_OLD, SCOPE_NEW, "4.12 scope sentence")
    t = replace_once(t, "\\textbf{What the reader should see.}",
                     "\\textbf{The dashboard reading.}", "dashboard run-in")
    t = replace_once(t, CAVEATS_OLD, CAVEATS_NEW, "data-anchor qualifications")

    t = replace_once(t, "\\textbf{Proposition (rescue threshold).}",
                     "\\textbf{Proposition 10 (rescue threshold).}",
                     "proposition 10 numbering")
    t = replace_once(t,
        "with the error-bound remark (Proposition, Section 5.6)",
        "with the error-bound remark (Proposition 10, Section 5.6)",
        "contribution proposition ref")

    t = replace_once(t, DELEGATE_OLD, DELEGATE_NEW, "5.2 delegation")
    t = replace_once(t,
        "the itemized data requirements for empirical application (S9).",
        "the itemized data requirements for empirical application (S9), and the per-literature positioning notes (S10).",
        "supplementary pointer")

    assert "Proposition 10 (rescue threshold)" in t
    assert "S10" in t and "The dashboard reading." in t
    assert "keep the claim honest" not in t and "What the reader should" not in t
    assert "buys a modeller" not in t and "We emphasize what the instantiation" not in t

    open(DST, "w", encoding="utf-8").write(t)
    print(f"wrote {DST} ({len(t)} bytes)")


if __name__ == "__main__":
    main()

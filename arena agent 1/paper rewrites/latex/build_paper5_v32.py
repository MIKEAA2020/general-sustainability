#!/usr/bin/env python3
"""Build paper5 v32 from v31: remnants/redundancy sweep, no-loss verification,
light readability, accessible abstract, flow (user-directed 2026-09-11, 5 tasks).

Every substitution asserts exactly one match. Scope:
- Task 4: abstract rewritten (4 paras, same claims, plain language).
- Task 1: 6 cuts (Lemma-2.2 restatement para; 2.7 rounding clause; 3.8 survival
  sentence; 3.4 artefact sentence; 3.4 archived-input sentences compressed;
  Conclusion summary list compressed). Every cut preserves all facts elsewhere.
- Tasks 3+5: 8 light touches (dual-name fix; fivefold framing; 2.2/2.4/3.4
  clarifications; App-B S6 pointer; Stuart&Humphries citation + References).
- Task 2: proofs verified full (3.1, 2.1, 2.2, S2.3, S3.2, S3.4 intact; 3.2 via
  cited frameworks + new citation). NOT touched: all proofs, S4.2, S4.4, S4.5,
  S4.7, App B body, Box 1, Tables 2-4, supp v9.
"""
import os

SRC = "/home/user/paper5_v31/paper5_sampled_governance_v31.tex"
DST = "/home/user/paper5_v32/paper5_sampled_governance_v32.tex"

r = lambda s: s

SUBS = [
("VER-header",
r'''% Periodic Review as Sampled Governance (paper 5, revision v31): author-blocked items (A3/A5/A8-A11) resolution revision with line numbers for review.''',
r'''% Periodic Review as Sampled Governance (paper 5, revision v32): redundancy sweep, accessible abstract, and readability revision with line numbers for review.'''),

# ---- Task 4: abstract ----
("ABS-p1",
r'''Fisheries governance is periodic: assessments are compiled at fixed
cadences, decisions taken at review points, and controls held until the
next review. Real institutions therefore operate a sampled-control loop
--- observation and update occur at discrete review times --- an
architecture we call \emph{sample-and-hold governance}. The formal
literature instead represents institutional response as a
continuous-time delay or an annual discrete step on a surplus-production
model; neither matches the operating object, and substituting either can
move or delete stability boundaries.''',
r'''Fisheries are managed on a schedule: scientists assess fish
stocks at fixed intervals, decisions are taken at review points, and
the resulting catch limits stay in force until the next review.
Management therefore works as a sampled loop --- it observes and acts
at discrete review times, holding each decision between reviews --- an
architecture we call \emph{sample-and-hold governance}. The standard
models of management response pretend otherwise: they treat
institutional reaction as a smooth continuous delay, or squeeze
the months between decisions into a single annual step. Neither matches
how real institutions operate, and swapping in either shortcut can move
or erase the boundaries between stable and unstable management.'''),

("ABS-p2",
r'''We analyse a logistic stock under held effort between reviews, with a
filtered deficit signal carrying institutional memory and a projected
Euler update resetting effort at each review. The sampled state space is
forward invariant by induction; the rapid-review limit is a
finite-horizon consistency statement, not a stability claim. The
logistic hold map's equilibrium multipliers cross the unit circle at a
review interval near 6.5 yr (a Neimark--Sacker-type crossing);
thresholds reported by first-order discretisation are command-step
artefacts. The archived stage-structured response regions are
provisional (their generating computation was never attached) and not
robust to the catchability scale the stage record never specifies: at
\(q = 0.1\) every class's annual-review verdict flips, making that
comparison uninformative rather than a non-reproduction. The
sample-and-hold map and the continuous-delay equation are distinct
operators; stability does not transfer in general between them.''',
r'''We model a fish stock harvested under effort held fixed between
reviews, with an institutional memory tracking perceived decline. Two
exact properties anchor the analysis: the model's state stays within
its valid set from one review to the next, and reviewing ever more
frequently approaches a continuous controller only over finite time
spans --- frequent review is not, by itself, a stability guarantee.
Computing stability review-interval by review-interval, the equilibrium
loses and regains stability at a review interval near 6.5 years;
thresholds reported by cruder one-step approximations are artefacts of
the approximation, not properties of the review schedule. The older
stage-structured calculations, whose generating code was never archived,
are reported as provisional records --- and they hinge on a catchability
scale those records never specify, at whose alternative every verdict
flips, so that comparison is uninformative rather than a refutation.
The lesson is architectural: periodically reviewed and continuously
delayed versions of the same feedback loop are different mathematical
objects, and stability results do not carry over between them.'''),

("ABS-p3",
r'''A multiplicity-controlled Lomb--Scargle screen of 42 annually assessed
stocks finds no target-band discoveries; a structured search across more
than thirty systems returns zero eligible cases. The northern cod case
yields a descriptive split: the crash interpretation is
formulation-dependent, post-collapse dynamics expose an identification
problem the mortality-allocation comparison does not resolve, and a
phase-line obstruction shows why no fixed scalar autonomous model
reproduces the observed reversals.''',
r'''On the empirical side, a spectral screen of 42 annually assessed
fish stocks --- testing for the 4- and 8-year cycles the model predicts,
with false discoveries controlled --- finds no robust cases; a structured
search across more than thirty resource systems finds no case meeting
the criteria for an unconfounded institutional oscillator. The northern
cod collapse contributes a descriptive split instead of a mechanism:
whether the crash was natural or fishing mortality depends on the
modelling formulation, the post-collapse record poses an identification
problem that mortality-allocation comparison cannot resolve, and a
mathematical obstruction explains why no simple fixed-rule model
reproduces the observed ups and downs.'''),

("ABS-p4",
r'''The cadence and form of periodic review, not ecological lag alone,
determine whether governance stabilises or destabilises a harvested
stock; the review interval is a local spectral design parameter.''',
r'''What decides whether management stabilises or destabilises a
fishery is therefore not biology alone but the review schedule itself
--- how often, and in what form, decisions are revisited. The review
interval is a design choice with stability consequences, and any claim
about institutional feedback must say which decision architecture it was
computed on.'''),

# ---- Task 1: cuts ----
("CUT-lemma22-restate",
r'''Case (i) subtracts a fixed term; case (ii)
subtracts a term proportional to stock. In each case the smaller
positive root of the modified production function moves rightward; at
the production maximum the two positive equilibria coalesce, and beyond
it they disappear. An effective threshold is not automatically a shifted
structural parameter, and the coalescence/disappearance case is part of
the statement.

\emph{Proof.} The constitutive production''',
r'''\emph{Proof.} The constitutive production'''),

("CUT-27-rounding",
r'''reopening of 26 June 2024 with a total allowable catch of 18 kt). The
displayed values are rounded values from the assessment table, and the
survival column''',
r'''reopening of 26 June 2024 with a total allowable catch of 18 kt). The
survival column'''),

("CUT-38-survival",
r'''101.05, 30.55 kt), and the survival column
\(\exp(-M)\) is a transformation of the reported instantaneous mortality
estimate, not an independently observed survival series. The
interpretation''',
r'''101.05, 30.55 kt). The
interpretation'''),

("CUT-34-artefact-sent",
r'''at \(\approx 6.5\) yr under the exact update, with the same restabilising direction. The 47.536
yr crossing and its \(-1\) multiplier at 79.143 yr are command-step
artefacts, not a review-cadence property (Section 4.1). For an institution implementing''',
r'''at \(\approx 6.5\) yr under the exact update, with the same restabilising direction. For an institution implementing'''),

("CUT-34-archived-inputs",
r'''bands): the command step is not a small distortion. On the archived
stage-structured review map, annual review is stable at every tested
response value, and the archived record places the anchovy-class window
at \(T_r\approx 3\)--\(4\) yr and the sprat-class window at
\(T_r\approx 6\)--\(12\) yr, reporting robustness to 30\% multiplicative
assessment error. These are archived, unreproduced statements (Section
3.3): the generating computation is not available, and the pre-registered reconstruction below does not reproduce the multi-year windows; they are
claims about the archived map, not results of the reconstructed object,
and neither transfers to the other operator.''',
r'''bands): the command step is not a small distortion. The stage-map
inputs to this evaluation are the archived, unreproduced records of
Section 3.3 --- annual stability, the anchovy-class 3--4 yr and
sprat-class 6--12 yr windows, and robustness to 30\% multiplicative
assessment error --- read at that section's status, not as results of
the reconstructed object.'''),

("CUT-conclusion-list",
r'''Until those
designs are executed, the summary of the empirical layer is the one
stated here --- a well-posed mechanism, an exploratory computational
record, a selected-cohort screen with limited power, a zero-count case
search that is not disconfirmation, and one case whose positive content
is a descriptive split.''',
r'''Until those
designs are executed, the empirical layer stands as stated here: a
well-posed mechanism, an exploratory computational record, limited
screen power, a case search that does not disconfirm, and one
descriptive split.'''),

# ---- Tasks 3+5: light touches ----
("T1-dual-name",
r'''control-theoretic update law --- and the two names are used
interchangeably throughout this article.''',
r'''control-theoretic update law --- and the article body uses
\emph{sample-and-hold} (with \emph{sampled} for its maps and loops)
throughout.'''),

("T2-fivefold",
r'''falsification discipline. The paper's constructive content is the
prospective programme''',
r'''falsification discipline. These five are retrospective; the paper's
constructive content is the prospective programme'''),

("T3-22-boundary",
r'''core that boundary calculation is reported in Section 3.4.''',
r'''core the multiplier-based boundary calculation is reported in Section 3.4.'''),

("T4-24-criterion",
r'''selected by a separate annual-review eligibility criterion.''',
r'''selected by an annual-review eligibility criterion defined for this analysis.'''),

("T5-34-both-records",
r'''statement consistent with both.''',
r'''statement consistent with both records.'''),

("T6-appB-S6",
r'''full instrument detail and the unreproduced pipeline register are in the
Supplementary material.''',
r'''full instrument detail and the unreproduced pipeline register are in the
Supplementary material (S6).'''),

("T7-32-stuart",
r'''\(C^1\)-consistency of the sampled map with projection inactive locally,
the multipliers satisfy \(\mu_j(T_r) = 1 + T_r\lambda_j(A) + O(T_r^2)\),
so local stability persists''',
r'''\(C^1\)-consistency of the sampled map with projection inactive locally,
the multipliers satisfy \(\mu_j(T_r) = 1 + T_r\lambda_j(A) + O(T_r^2)\)
(Stuart and Humphries, 1996), so local stability persists'''),

("ABS-p1-pretend",
r'''models of management response pretend otherwise: they treat''',
r'''models of management response assume otherwise: they treat'''),

("ABS-p2-flipfix",
r'''scale those records never specify, at whose alternative every verdict
flips, so that comparison is uninformative rather than a refutation.''',
r'''scale those records never specify; at an alternative scale every
verdict flips, so that comparison is uninformative rather than a
refutation.'''),

("T8-refs-stuart",
r'''Statistics Canada. Tables 38-10-0167-01 and 38-10-0168-01, CANSIM
database. Statistics Canada, Ottawa.

Tam, J. C.''',
r'''Statistics Canada. Tables 38-10-0167-01 and 38-10-0168-01, CANSIM
database. Statistics Canada, Ottawa.

Stuart, A. M., and Humphries, A. R. 1996. Dynamical Systems and
Numerical Analysis. Cambridge University Press, Cambridge.

Tam, J. C.'''),
]

def main():
    src = open(SRC).read()
    for name, old, new in SUBS:
        n = src.count(old)
        assert n == 1, f"{name}: {n} matches (expected 1)"
        src = src.replace(old, new)
        print(f"ok {name}")
    # post-checks: proofs intact; no new staleness
    assert src.count("emph{Proof.}") == 3, "proof count changed"
    assert "Proposition 3.1" in src and "Proposition 2.1" in src and "Lemma 2.2" in src
    assert "used\ninterchangeably" not in src
    assert "that boundary calculation is reported" not in src
    assert "consistent with both records" in src
    assert "Supplementary material (S6)" in src
    assert src.count("Stuart") == 2, "Stuart cite+ref"
    assert "ups and downs" in src and "decision architecture it was" in src
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "w").write(src)
    print("wrote", DST, len(src))

if __name__ == "__main__":
    main()

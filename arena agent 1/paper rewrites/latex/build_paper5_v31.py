#!/usr/bin/env python3
"""Build paper5 v31 from v30: A3/A5/A8-A11 author-blocked items resolved.

Every substitution asserts exactly one match. Scope (user-directed 2026-09-11):
A3 (Table-3 full vector + S2.1 interiority + code pins @24c980cd), A5 (S3.3
decomposition paragraph + S9.2 pointer), A8/A9 (no-ops, closed), A10 audited
compression (S4.1-para-1, S4.3, S3.7 hedge; Box-1/S3.6 audited no-cut) +
notation Table 4, A11 (S2.4 first-use note + S3.5 battery sentence + S9.1).
NOT touched: S4.2, S4.4, S4.5, S4.7, App B, title/abstract, S3.4/S3.8.
"""
import sys

SRC = "/home/user/paper5_v30/paper5_sampled_governance_v30.tex"
DST = "/home/user/paper5_v31/paper5_sampled_governance_v31.tex"
PIN = "24c980cd"

r = lambda s: s

SUBS = [
("VER-header",
r'''% Periodic Review as Sampled Governance (paper 5, revision v30): screen verification and battery repair revision with line numbers for review.''',
r'''% Periodic Review as Sampled Governance (paper 5, revision v31): author-blocked items (A3/A5/A8-A11) resolution revision with line numbers for review.'''),

# ---- A3 ----
("A3-S2.1-interiority",
r'''the nonsmooth regions of \(\Phi_k\) and \(\Pi_{[0,E_{\max}]}\); the
equilibrium coordinates are not listed here (Appendix A).''',
r'''the nonsmooth regions of \(\Phi_k\) and \(\Pi_{[0,E_{\max}]}\):
\(\Phi_k(0) = \delta\) gives the equilibrium deficit \(s^* = 0\)
uniquely, with softplus slope \(sp_k'(0) = 1/2\), and \(E^* = 2.09\)
lies in the interior \((0, E_{\max})\); the coordinates
\((89.55188, \delta, 2.08962)\) are listed in Table 3 of Appendix A.'''),

("A3-S3.4-listed",
r'''--- and on the unlisted parameter vector (Table 3).''',
r'''--- and on the parameter vector listed in Table 3.'''),

("A3-AppA-first",
r'''Two further consolidated records. First, the members of the
logistic-core parameter vector that the text does not list (\(r\), \(K\),
\(E_{\max}\), \(\delta_0\), \(Z_{\rm ref}\), \(\Delta_{\rm ref}\),
\(\tau_m\); \(\delta = \log 2/10\) is stated in Section 2.1), the linearised fixed point \((N^*, E^*, Z^*)\)
and its interiority to the nonsmooth regions of \(\Phi_k\) and
\(\Pi_{[0,E_{\max}]}\), the monodromy's numerical construction, and the
continuous eigenvalue \(\lambda\) and crossing angle \(\theta\) of
Section 3.4's records are part of the computational record;
Table 3 collects the parameter values stated in the text.''',
r'''Two further consolidated records. First, the logistic-core parameter
vector (\(r\), \(K\), \(E_{\max}\), \(\delta_0\), \(Z_{\rm ref}\),
\(\Delta_{\rm ref}\), \(\tau_m\); \(\delta = \log 2/10\) is stated in
Section 2.1) and the linearised fixed point \((N^*, E^*, Z^*)\) with its
interiority to the nonsmooth regions of \(\Phi_k\) and
\(\Pi_{[0,E_{\max}]}\) are printed in Table 3, with the code constants
block pinned per row; the monodromy's numerical construction and the
continuous eigenvalue \(\lambda\) and crossing angle \(\theta\) of
Section 3.4's records remain part of the computational record.'''),

("A3-T3-caption",
r'''\textbf{Table 3.} Parameter values stated in this manuscript for the
logistic hold-map core and the stage-structured reconstruction. No value
here is newly computed; values not stated in the text remain in the computational record (this
appendix).''',
r'''\textbf{Table 3.} Parameter values for the
logistic hold-map core and the stage-structured reconstruction. No value
here is newly computed; the baseline-core vector is printed here, with
the code constants block pinned per row, and values not stated remain in
the computational record (this appendix).'''),

("A3-T3-vector",
r'''Logistic hold-map core & \(r\), \(K\), \(E_{\max}\), \(\delta_0\),
\(Z_{\rm ref}\), \(\Delta_{\rm ref}\), \(\tau_m\) & not
listed here & computational record (this
appendix) \\''',
r'''Logistic hold-map core & growth rate \(r\) (yr\(^{-1}\)) & 0.02
(validation argument) & This table; constants block
\texttt{droop\_test.py} L49--58 @ PIN \\'''.replace("PIN", PIN) + "\n" +
r'''Logistic hold-map core & carrying capacity \(K\) & 100 & This table;
constants block \texttt{droop\_test.py} L49--58 @ PIN \\'''.replace("PIN", PIN) + "\n" +
r'''Logistic hold-map core & effort ceiling \(E_{\max}\) & 30 & This
table; constants block \texttt{droop\_test.py} L49--58 @ PIN \\'''.replace("PIN", PIN) + "\n" +
r'''Logistic hold-map core & effort-law gain \(\delta_0\) & 0.01 & This
table; constants block \texttt{droop\_test.py} L49--58 @ PIN \\'''.replace("PIN", PIN) + "\n" +
r'''Logistic hold-map core & reference deficit \(Z_{\rm ref}\) & 1 & This
table; constants block \texttt{droop\_test.py} L49--58 @ PIN \\'''.replace("PIN", PIN) + "\n" +
r'''Logistic hold-map core & reference scale \(\Delta_{\rm ref}\) & 1 &
This table; constants block \texttt{droop\_test.py} L49--58 @ PIN \\'''.replace("PIN", PIN) + "\n" +
r'''Logistic hold-map core & memory timescale \(\tau_m\) (yr) & 5 & This
table; constants block \texttt{droop\_test.py} L49--58 @ PIN \\'''.replace("PIN", PIN)),

("A3-T3-fixedpoint",
r'''Logistic hold-map core & linearised fixed point \((N^*, E^*, Z^*)\);
interiority to the nonsmooth regions of \(\Phi_k\) and \(\Pi\) & not
listed here & computational record (this
appendix) \\''',
r'''Logistic hold-map core & linearised fixed point \((N^*, E^*, Z^*)\);
interiority & \((89.55188, \delta, 2.08962)\); \(E^* \in (0,
E_{\max})\), \(\Phi_k(0) = \delta\), \(sp_k'(0) = 1/2\) & This table;
equilibrium routine \texttt{base\_equilibrium},
\texttt{droop\_test.py} L86--93 @ PIN \\'''.replace("PIN", PIN)),

# ---- A5 ----
("A5-S3.3-decomp-para",
r'''Multiplicative assessment-error experiments preserve''',
r'''A \(\tau_0\) decomposition separates, within the delayed-recruitment
operator, cohort-driven from institutional-delay-induced crossings: at
\(g = 5\) yr and \(\eta = 0.914\) the raw \(r\)-window [0.0076, 0.3705]
narrows to the institutional-only [0.2660, 0.3285], and fish-range
crossings from 12 to 8, under \(\tau_0\)-stable classification by
nonlinear ground truth. The separation is within one operator; it does
not isolate the cross-operator effect compared in Section 4.1. The
\(g = 5\) middle band overlaps slow cod-class growth rates but remains
confounded with cohort resonance --- a different operator from Section
3.7's four-state loop. Full windows, the twelve-cell decomposition grid,
and the middle-band table are tabulated in Supplementary S9.2.

Multiplicative assessment-error experiments preserve'''),

# ---- A10 ----
("A10-S4.1-compress",
r'''The same feedback loop --- surplus production,
an institutional deficit signal, an effort law --- carries an archived,
unreproduced instability record near 3--4 yr of review under the
stage-structured map (a different ecological plant, Section 2.3; the
archived windows' provisional status and the reconstruction's comparison
with them are stated in Sections 3.3 and 3.4; the plant--operator
confound is stated alongside --- the operator effect is not claimed to be
isolated by this comparison), convergence over a 1--20 yr grid under the
cod-class parameterisation of that same map, and instability at annual
review with a complex unit-circle crossing near 6.5 yr under the exact update --- the Euler-reported crossing near 47.5 yr being a
command-step artefact relative to the exact update --- under the logistic hold map. The stage-map
layer of that record has its own stated limitation: the stage
map fixes no catchability, the reconstruction imports the hold-map
core's \(q = 0.001\), and at the sensitivity case \(q = 0.1\) every
verdict of the Section 3.4 comparison flips --- every class unstable at
annual review (\(\rho(1) \ge 1.29\)), the slow-stock class unstable
across the entire grid (\(\rho(50) = 7.8\)) --- so the archived-window
comparison is uninformative at the unspecified scale rather than a
non-reproduction (Section 3.4's Reading).''',
r'''The same feedback loop --- surplus production,
an institutional deficit signal, an effort law --- carries an archived,
unreproduced instability record near 3--4 yr of review under the
stage-structured map, convergence over a 1--20 yr grid under that map's
cod-class parameterisation, and instability at annual review with a
complex crossing near 6.5 yr under the exact logistic hold map (full
records, the Euler command-step artefact, and the \(q\)-sensitivity
caveat in Section 3.4 and its Reading; the plant--operator confound is
stated alongside and the operator effect is not claimed isolated).'''),

("A10-S4.3-compress",
r'''The cod case contributes a descriptive partition, not a mechanism. The
crash-window mortality is formulation-dependent because the NCAM M-shift
allocation is that --- an allocation of unobserved deaths
conditional on model structure (Cadigan, 2016). The post-collapse record
is not resolved by either mortality-allocation formulation because no
single fixed-regime model reproduces the repeated reversals of the
post-moratorium record (the phase-line obstruction, applied as a
model-class diagnostic under Section 3.8's two conditions), and the
post-2015 production stall documented by Rose (2026) shows the second
window persisting under independent reconstructions. The obstruction
mathematics is likewise bounded: it concerns exact trajectories of the
fixed-parameter, fixed-removals autonomous class and is not a rejection
under measurement error, process noise, age structure, migration,
time-varying mortality, or state-space observation models. What the case
supplies is a falsification benchmark: a well-documented
collapse-and-stall record against which prospective designs can be
powered and scored.''',
r'''The cod case contributes a descriptive partition, not a mechanism:
crash-window mortality is formulation-dependent (Section 3.8), and the
post-collapse record is not resolved by either mortality-allocation
formulation, with the post-2015 production stall persisting under
independent reconstructions (Rose, 2026). The obstruction mathematics
applies within the scope stated in Sections 3.8 and 4.7(vii). What the
case supplies is a falsification benchmark: a well-documented
collapse-and-stall record against which prospective designs can be
powered and scored.'''),

("A10-S3.7-hedge",
r'''The visible-record pattern --- long series repeatedly
associated with climate variability, cohort effects, infrastructure
changes, or emergency interventions --- suggests, without establishing,
a selection mechanism in which systems receive intensive monitoring
after complex crises. The retrospective search cannot distinguish that
hypothesis from the null of coincidental association, and no causal
identification of selection bias is claimed.''',
r'''The visible-record pattern --- long series repeatedly associated
with climate variability, cohort effects, infrastructure changes, or
emergency interventions --- suggests, without establishing, a selection
mechanism in which systems receive intensive monitoring after complex
crises; no causal identification of selection bias is claimed.'''),

("A10-notation-pointer",
r'''leaving \(M\) to natural mortality
alone.''',
r'''leaving \(M\) to natural mortality
alone. Symbols are tabulated with their definition sites in Table 4 of
Appendix A.'''),

("A10-Table4",
r'''\end{longtable}

\subsection{Appendix B. Distributive constraints where reproducible}''',
r'''\end{longtable}

\textbf{Table 4.} Notation: every symbol with its definition site. No
row introduces a symbol; rows without a site would be gaps, and all
rows resolve.

\begin{longtable}[]{@{}
  >{\raggedright\arraybackslash}p{(\columnwidth - 4\tabcolsep) * \real{0.2500}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 4\tabcolsep) * \real{0.4500}}
  >{\raggedright\arraybackslash}p{(\columnwidth - 4\tabcolsep) * \real{0.3000}}@{}}
\toprule\noalign{}
\begin{minipage}[b]{\linewidth}\raggedright
Symbol
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Meaning
\end{minipage} & \begin{minipage}[b]{\linewidth}\raggedright
Defined at
\end{minipage} \\
\midrule\noalign{}
\endhead
\bottomrule\noalign{}
\endlastfoot
\(N\) & resource stock & Section 2.1 \\
\(Z\) & institutional deficit signal & Section 2.1 \\
\(E\) & extraction effort & Section 2.1 \\
\(\mathcal P_{T_r}\) & review Poincar\'e map (sampled flow at review
instants) & Section 2.1 \\
\(D\mathcal P_{T_r}(X^*)\) & monodromy matrix (Jacobian at the fixed
point) & Section 2.1 \\
\(\Pi\) & projection onto \([0,E_{\max}]\) & Section 2.1 \\
\(\Phi\), \(\Phi_k\) & signal map; softplus realisation (shift
\(\delta\), sharpness \(k\)) & Section 2.1 \\
\(\delta\); \(\delta_0\) & equilibrium memory level \(\log 2/10\);
effort-law gain (unrelated) & Section 2.1 \\
\(F_B\); \(F_B^{\rm prot}\) & extractive effort law; protective
comparator & Section 2.1 \\
\(\mathcal A_n\); \(\mathcal O\) & assessment operator; observation
operator & Section 2.1 \\
\(S(\cdot)\); \(S\) & surplus production (control sections); spawning
stock biomass (cod sections, Table 2) & Section 2.1; Sections 2.7, 3.8 \\
\(g\) & maturation delay (delayed-recruitment parameterisation) &
Section 3.3 \\
\(C_E\), \(C_Z\) & linearised protective gains & Section 3.4 (Abaee,
2026, equation~(3)) \\
\(A\), \(J\), \(Z\), \(E\) & four-state loop: adults, juveniles, memory
signal, held effort & Section 3.7 \\
\(\mathfrak s\), \(K\), \(C(t)\), \(M\), \(F\) & cod case: unstable
threshold, unexploited capacity, removals, natural mortality, fishing
mortality & Sections 2.7, 3.8; Table 2 \\
\end{longtable}

\subsection{Appendix B. Distributive constraints where reproducible}'''),

# ---- A11 ----
("A11-S2.4-note",
r'''\texttt{ram\_crosssection.py}, \texttt{verify\_bh.py}) are deposited with
the article.''',
r'''\texttt{ram\_crosssection.py}, \texttt{verify\_bh.py}) are deposited with
the article. The screen is a restricted result: its weight is limited to
the refutation stated in Section 4.2, and its null verdict survives the
eleven-variant sensitivity battery of Supplementary S9.1.'''),

("A11-S3.5-battery",
r'''periodicity itself diagnoses an institutional feedback is unsupported by
this cohort.''',
r'''periodicity itself diagnoses an institutional feedback is unsupported by
this cohort. That null verdict is robust: an eleven-variant sensitivity
battery --- ARMA(1,1), trend-stationary-no-detrend, circular block
bootstrap at three block lengths, Hodrick--Prescott-cycle and
first-difference pretreatments, and piecewise-AR(1) regime surrogates at
three break dates, each at the published 200-replicate, seed-7
resolution --- returns the BH-adjusted zero count in every variant
(smallest nominal \(p\) 0.0100, Hodrick--Prescott variant; details and
the resolution bound in Supplementary S9.1).'''),
]

def main():
    import os
    src = open(SRC).read()
    for name, old, new in SUBS:
        n = src.count(old)
        assert n == 1, f"{name}: {n} matches (expected 1)"
        src = src.replace(old, new)
        print(f"ok {name}")
    # post-checks: A3 pointer dissolved; no stale unlisted-vector refs
    assert "are not listed here (Appendix A)" not in src
    assert "on the unlisted parameter vector" not in src
    assert "that the text does not list" not in src
    assert src.count("not\nlisted here") == 0, "residual Table-3 grouped row"
    assert "Table 4" in src and "S9.1" in src and "S9.2" in src
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "w").write(src)
    print("wrote", DST, len(src))

if __name__ == "__main__":
    main()

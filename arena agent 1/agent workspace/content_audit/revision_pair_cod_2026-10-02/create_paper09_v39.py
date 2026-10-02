#!/usr/bin/env python3
"""Submission-facing versioned correction: exact local boundary, epsilon thresholds and scoped robustness."""
from pathlib import Path
src=Path('/home/user/papers/paper09_cod_certification_v38.tex');dst=src.with_name('paper09_cod_certification_v39.tex');s=src.read_text()
def change(old,new):
 global s
 assert s.count(old)==1,(old[:100],s.count(old))
 s=s.replace(old,new)
change('''informative one --- because the map is expansive at the reference point for every admissible carrying
capacity.''','''informative one --- because the map is expansive at the reference point for every
declared admissible carrying capacity $K\\ge2K^*$.''')
change('''The sensitivity itself is a result: 387 of 2,000 joint parameter refits
lose the positive cod LRP budget under the registered fixed floor''','''The sensitivity itself is a result: the local fixed-floor boundary
$r_{\\rm crit}(K;C)=(C+80.87)/[884.6(1-884.6/K)]$ locates loss of LRP
self-viability, and 387 of 2,000 joint parameter refits lose the positive
cod LRP budget under the registered fixed floor''')
change('''conclusion; three of four listed conventions reverse it.

Refitting \\(r\\) alone''','''conclusion; three of four listed conventions reverse it.

\\begin{proposition}[Exact local failure boundary under a fixed floor]
\\label{prop:budget-failure-boundary}
Let $L=K^*>0$, $K>L$, $r>0$, and let a policy take catch $C(L)=C\\ge0$
at the LRP under a persistent one-step floor $q\\le0$. The LRP is
self-viable for one step precisely when
\\[
C^*(r,K;q)-C=rL(1-L/K)+q-C\\ge0
\\quad\\Longleftrightarrow\\quad
r\\ge r_{\\mathrm{crit}}(K;C,q)
=\\frac{C-q}{L(1-L/K)}.
\\]
Under the registered fixed $q=-80.86977895$ kt and $L=884.6$ kt,
$r_{\\mathrm{crit}}(5000;0)\\simeq0.11107$ and
$r_{\\mathrm{crit}}(5000;5)\\simeq0.11794$.
A model below this boundary sends the LRP below the safe set in one step
for any rule with the stated catch at $L$; the condition alone does not
classify a kernel starting at higher stock levels.
\\end{proposition}
\\begin{proof}
Evaluate the Schaefer map $F(L)=L+rL(1-L/K)-C+q$ and rearrange
$F(L)\\ge L$; its coefficient of $r$ is strictly positive because
$K>L$. The converse is the same identity.
\\end{proof}

Refitting \\(r\\) alone''')
change('''\\subsection{4. Discussion}\\label{budget-discussion}

\\noindent\\textbf{Certification as a conditional decision aid.}''','''\\subsection{4. Discussion}\\label{budget-discussion}

\\noindent\\textbf{Robustness and limits.}
Proposition~\\ref{prop:budget-failure-boundary} identifies an exact local
failure region for the fixed registered q10 floor, not a state-global
failure theorem. For example, a zero-budget $(K,r)=(5000,0.11107)$ model
has a one-step SSE ratio about $1.24560$ relative to the registered fit;
it lies inside an \\emph{approximate conditional} two-parameter Gaussian
$95\\%$ $F$-cut (ratio $1.31303$). A $95\\%$ Bayesian
highest-posterior-density \\emph{credible} region constructed with a
stated Gaussian likelihood and uniform bounded priors also intersects
the fixed-floor negative-budget region. These are different, assumption-
dependent regions; a Bayesian credible region is not a confidence set,
and neither construction establishes physical-model coverage. Recomputing
q10 at every candidate fitted map changes these local classifications;
it is a coherent alternative sensitivity but not an independently
validated future process shock. Detailed cuts, prior sensitivity and
reproduction code are retained in the linked audit record below.

On the aquifer, retrospective adaptive-conformal and block-bootstrap
ensemble intervals show method- and learning-rate-dependent empirical
one-step coverage; some adaptive intervals are infinite. Neither such
coverage nor an observed maximum furnishes a uniform multi-year
additive defect bound. The 2J3KL assessment literature describes distinct
survey and tagging data streams, but does not identify independent
additive catch, SSB-observation, process and Schaefer-discrepancy channels
on the registered fit window. A physical robust-within-class claim would
require a new, independently validated joint state-space decomposition,
a justified class of maps and shocks, and a nonvacuous all-model recursion.
The conditional model-class and error diagnostics are documented in the
reproducibility record
\\url{https://github.com/MIKEAA2020/general-sustainability/blob/e5452c07c6536213c7051178bac5acf7a46b8b4d/arena%20agent%201/agent%20workspace/CONDITIONAL_MODEL_CLASS_AND_ERROR_SCOPE_2026-10-02.md};
see also Regular et al. (2025), DFO Canadian Science Advisory Secretariat
Research Document 2025/048 for the catch-bound and survey-model scope.

\\noindent\\textbf{Certification as a conditional decision aid.}''')
change('''$\\varepsilon=21.8105683$ ft as an alternative hypothetical bound makes
each of those sets empty by $T=3$. These are computed conditional on a''','''$\\varepsilon=21.8105683$ ft as an alternative hypothetical bound makes
each of those sets empty by $T=3$. A numerical bisection of the same
direct recursion finds the following \\emph{suprema} of imposed uniform
additive-error magnitudes with nonempty kernels, at the 618-ft threshold,
710-ft ceiling and UC-min recharge:
\\begin{center}
\\begin{tabular}{lrr}
\\toprule
Policy & $T=3$ (ft) & $T=4$ (ft)\\\\
\\midrule
BAU & 16.01 & 9.91\\\\
Flat 90\\% & 16.82 & 10.71\\\\
Stage I & 16.71 & 10.94\\\\
Cascade & 17.23 & 11.60\\\\
\\bottomrule
\\end{tabular}
\\end{center}
The $(T=3)$ values place the observed out-of-sample maximum
(21.81 ft) beyond all four nonempty-kernel limits; the training
maximum (15.41 ft) exceeds all $(T=4)$ limits. These are bisection
outputs for an \\emph{assumed sure bound} in a fitted finite-state-domain
recursion, not calibrated error quantiles, interval-arithmetic rounding
certificates or physical-coverage statements. The full error-versus-boundary
curve and source-specific numerical checks are in the linked record.
These are computed conditional on a''')
change('''yr\\(^{-1}\\) --- an analytic limit whose bootstrap \\(90\\%\\) interval is
  \\([0, 121.1]\\) kt''','''yr\\(^{-1}\\) --- an analytic limit whose \\emph{raw signed} fixed-$K$
  bootstrap \\(90\\%\\) percentile interval is \\([-69.3,121.1]\\) kt
  (the clipped reporting interval is \\([0,121.1]\\) kt)''')
change('''  Under the informative 10th-percentile productivity class,
  moratorium-level''','''  Under the registered source-year, linear-quantile 10th-percentile
  productivity class, moratorium-level''')
change('''  No non-BAU policy dominates BAU, and the mechanism is the clause-(H1)
  reading at the 5th-percentile''','''  Under the registered linear-quantile classes, no non-BAU policy
  dominates BAU, and the mechanism is the clause-(H1)
  reading at the 5th-percentile''')
change('''  The results are convention-dependent in the residual convention only
  in the sense that the source-year convention sets the constructive
  bound at 91.59 kt, brings the 60-kt rules onto the reference point
  itself (their \\(T=\\infty\\) boundary is \\(884.6\\) kt, against 900.3 kt
  under the registered convention), lengthens the certified horizon (to \\(T=6\\) under the two
  harsher floors and \\(T=7\\) under the informative one), and reduces
  the vacuous family to one class; every parameter and every certificate
  direction is otherwise stable.''','''  The source-year fit, catch-year alignment, residual-quantile estimator
  and floor-construction rule are consequential modelling choices:
  an internally refitted destination-year alignment lowers $C^*$
  from 91.59 to 51.95 kt, and three alternative q05 conventions make
  the perpetual q05 class vacuous. The exact local failure boundary
  locates this sensitivity in parameter space; no numeric verdict
  transfers unqualified across these model and class choices.''')
change('''\\emph{Definitional note A (identity).} Only the perpetual-worst floor is
vacuous''','''\\emph{Definitional note A (identity).} Under the registered source-year,
linear-quantile classes, only the perpetual-worst floor is vacuous''')
change('''\\emph{Definitional note B (rule-level).} The no-dominance outcome of
finding (2)''','''\\emph{Definitional note B (rule-level).} Under those same declared
classes, the no-dominance outcome of finding (2)''')
assert not dst.exists() or dst.read_text()==s, f'Existing {dst} differs; refusing overwrite'
if not dst.exists():dst.write_text(s)
print('VERIFIED',dst,len(s))

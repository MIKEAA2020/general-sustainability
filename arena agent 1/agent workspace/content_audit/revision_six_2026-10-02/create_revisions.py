#!/usr/bin/env python3
"""Construct six immutable next-version TeX sources from adjudicated predecessors."""
from pathlib import Path
import re
R=Path('/home/user/papers')
VERS={'02':('probabilistic_sufficiency',14,15),'03':('computational_certification',18,19),'04':('minimax_dual_certificates',18,19),'05':('exact_belief_computation',18,19),'06':('assessment_separation',69,70),'09':('cod_certification',34,35)}
S={k:(R/f'paper{k}_{stem}_v{old}.tex').read_text() for k,(stem,old,new) in VERS.items()}
def rep(k,a,b,n=1):
    assert S[k].count(a)==n,(k,S[k].count(a),a[:130]); S[k]=S[k].replace(a,b)
def section(k,a,b):
    assert a in S[k],(k,a); S[k]=S[k].replace(a,b,1)
# 02: unified nominal/robust/policy scope and actual class-dependent result.
rep('02','the maximal worst-case probability of keeping the state','the maximal nominal probability, under the declared observation and transition law, of keeping the state')
rep('02','the recursion\nmaximises over actions but \\emph{minimises} over the disturbance, so the object is a\nworst-case safety probability rather than an expected total reward. Consequently the\npiecewise-linear representation survives but its identifying structure does not: here the\n$\\alpha$-vectors are exactly the indicators of the maximal jointly survivable subsets of the\nsupport, an antichain (Proposition~\\ref{prop:antichain}), rather than the\nreward-derived vectors of the expected-criterion theory.',
'''the nominal recursion maximises over actions and takes the specified transition--observation expectation; it does not minimise over disturbances. A separate rectangular robust recursion is defined in Section~\\ref{dr}. General stochastic finite-horizon safety values have the usual policy-tree $\\alpha$-vectors. Only in the deterministic, declared-policy-class limit do their entries reduce to survival indicators; retaining maximal survivor subsets as an antichain is justified there (Proposition~\\ref{prop:antichain}), not for every stochastic POMDP.''')
rep('02','a second probe cuts the misread probability from\n\\(1/10\\) to \\(7/250\\)', 'a three-reading majority reduces the error from\n\\(1/10\\) for one reading to \\(7/250\\) (two extra blind steps)')
rep('02','an\nexact probe-count bound \\(p_{\\mathrm{wrong}}(n) \\le (4\\varepsilon(1 -\n\\varepsilon))^{n/2}\\)', 'a sufficient probe-count bound \\(p_{\\mathrm{wrong}}(n) \\le (4\\varepsilon(1 -\n\\varepsilon))^{n/2}\\)')
rep('02','In particular \\(V^{\\Pi_{\\mathrm{hold}}}_{k}(b_{0}) = 1\\) exactly on\n\\(z_{0} \\ge 1 + T_{\\mathrm{obs}}\\), recovering the declared-class\ndeterministic verdict as the value-one level;', 'For \\(k\\ge1\\), the value-one region is exactly\n\\(z_{0} \\ge 1 + \\min(k,T_{\\mathrm{obs}})\\); for \\(k=0\\) it is \\(z_0\\ge1\\).\nThe displayed expression is restricted to the certified grid \\(z_0\\ge1\\);\nfor \\(z_0<1\\) initial safety fails and the value is zero. At and after\nrevelation the value-one boundary is \\(1+T_{\\mathrm{obs}}\\);')
rep('02','--- an exact computable infinite-horizon value. On the delayed instance', '--- a well-defined infinite-horizon value, but finiteness of the lattice by itself gives no computable bound on the index of the last strict drop for a nonstationary policy class. A finite stationary game with an effective fixed-point operator admits a separate stopping algorithm. On the delayed instance')
rep('02','consequently every certified table at\n\\(T_{\\mathrm{obs}} \\le 3\\), \\(k \\le 4\\) already records the\nfull-horizon value.', 'consequently the columns with \\(k\\ge T_{\\mathrm{obs}}\\) in the\ncertified table record the full-horizon hold-class value; columns before revelation do not.')
rep('02','the hold-class value has jump\ndiscontinuities exactly at \\(z_{0} = 1 + \\min(k, T_{\\mathrm{obs}})\\) --- a\njump of exactly \\(\\tfrac{1}{2}\\), from \\(\\tfrac{1}{2}\\) to \\(1\\)', 'for \\(k\\ge1\\) the hold-class value has two global jump\nloci: \\(z_0=1\\) (from \\(0\\) to \\(\\max(w,1-w)\\)), and\n\\(z_{0} = 1 + \\min(k, T_{\\mathrm{obs}})\\) (from\n\\(\\max(w,1-w)\\) to \\(1\\)); the certified grid excludes the region \\(z_0<1\\),\nand at the symmetric prior both jumps have size \\(1/2\\)')
rep('02','the\nflat free-probe threshold \\(21/10\\) bound it from below and above.', 'the flat free-probe threshold \\(21/10\\) are separate lower-cost comparators: neither upper-bounds the pinned threshold at every displayed deadline. The grid counts \\(5,4,3,2,1\\) form a staircase, not a continuous linear kernel-size law.')
rep('02','The min-mass\nbound is the case \\(p_{x} \\equiv 1\\) (deterministic readings, no\ncommon action)', 'The deterministic min-mass lower bound instead requires that every admissible policy loses at least one positive-prior-mass initial branch (which may depend on the policy). The condition \\(p_x\\equiv1\\) would make the weighted deficit equal to one, not to the smallest prior mass')
rep('02','Let \\(\\mathcal{D}_{\\rho}\\) be as above and define', '''For this operator require a continuation \\(\\tau(b,a,y)\\) at \\emph{every} outcome on which contamination may concentrate. If an outcome is nominally null, either remove it from the contaminating support or supply an explicit off-support continuation via a joint transition--observation model. Fixing nominal posteriors while varying only outcome probabilities defines a rectangular stress operator; it is not automatically the Bayesian update of one coherent perturbed joint law.\\par
Let \\(\\mathcal{D}_{\\rho}\\) be as above and define''')
rep('02','Chatterjee, Doyen, and Henzinger (2009)', 'Chatterjee, Doyen, and Henzinger (2010)')
S['02']=S['02'].replace('Chatterjee, Doyen and Henzinger, 2009','Chatterjee, Doyen and Henzinger, 2010')
# bibliographic year and coordinates change only at matching entry; do not touch unrelated 2009 papers
S['02']=re.sub(r'(Chatterjee, K\., Doyen, L\., Henzinger, T\.A\., )2009\.',r'\g<1>2010.',S['02'])
# 03: held policies need all-time envelopes; distinguish demonstrated pair sufficiency from necessity.
rep('03','the pairs past \\(\\approx 0.245\\) and \\(\\approx\n0.397\\), singletons never', 'the displayed pair schedules reach their respective position ceilings at\n\\(\\approx 0.245\\) and \\(\\approx 0.397\\), while all-control\npair nonviability beyond those values is not established; singletons remain viable in the stated model')
rep('03','so such a policy is continuously safe exactly when its block\nmoments satisfy the unrelaxed rows: an exact reduction precisely when the\nrow bounds are exact, \\(\\bar{e}_a = 0\\);', 'so such a policy satisfies the \\emph{sampled} rows exactly when their\nblock moments satisfy the corresponding unrelaxed grid rows. Continuous-time\nsafety further requires a valid all-time between-grid enclosure (or an\nindependent exact extremum test on each block); \\(\\bar e_a=0\\)\nonly removes the averaging error and does not supply this missing test;')
rep('03','and positivity is non-monotone on\nboth sides.', 'while the computed levels here are monotone; changes of label set,\nscenario approximation and error budgets preclude inferring a general\npositivity-monotonicity theorem from refinement of the control mesh alone.')
rep('03','\\(T=\\tfrac65\\): program dimensions,','\\(T=\\tfrac65\\): program dimensions,') if False else None
# avoid the false converse for pair ceilings in the proposition and its surroundings
rep('03','the pair delay thresholds --- where the peak reaches\n2 --- are', 'the selected-schedule pair ceiling roots --- where that schedule\'s critical-position peak reaches\n2 --- are')
rep('03','For every \\(\\tau\\) at or below its threshold the\ncritical position stays \\(\\le 2\\) with the velocity rows strict;', 'For each pair, the displayed schedule is safe up to its stated root\nprovided its remaining facets and the fixed terminal horizon are checked;\nthis is a sufficient schedule, not an all-control impossibility proof beyond the root;')
rep('03','the two-mode cells\n\\(\\{1,2\\}\\) and \\(\\{2,3\\}\\) are viable to', 'the two-mode cells\n\\(\\{1,2\\}\\) and \\(\\{2,3\\}\\) admit the displayed schedules to')
rep('03','the\naudited delay hierarchy is exactly the cell-refinement family:', 'the instance provides a cell-refinement family with an exact triple obstruction and constructive pair lower bounds:')
rep('03','(the full seven-facet scan exactly at rational\nsurrogates below each threshold', '(the full seven-facet scan exactly at rational\nsurrogates below each selected-schedule root') if False else None
S['03']=S['03'].replace('pair delay thresholds','selected-schedule pair ceiling roots').replace('pair thresholds','pair schedule roots')
# preserve reference-library/solver distinction; supplementary unchanged in mathematics
rep('03','The complete proofs and verification record cited in the bridge theorem\naccompany this article as\n\\texttt{paper03\\_computational\\_certification\\_v18\\_supplementary.tex}\n(with a matching PDF). The companion\'s mathematical text has not been\nrewritten here; its source-year identity is recorded in the preservation\nreview.', 'The bridge hypotheses, proof details and rational verification record are\nin \\texttt{paper03\\_computational\\_certification\\_v19\\_supplementary.tex}.\nThe finite \\texttt{viacert} reference package uses only the Python standard library;\nthe distinct continuous-program optimization campaign uses SciPy/HiGHS.')
# 04: Helly proof with an actual minimax argument on the selected family.
a=S['04'].index('\\begin{proof}',S['04'].index('\\label{prop:sparse}'))
b=S['04'].index('\\end{proof}',a)+len('\\end{proof}')
S['04']=S['04'][:a]+r'''\begin{proof}
Work in $\operatorname{aff}U$, of dimension $d\le k$. Each label
$i=(x,j,d_0)$ defines the closed convex subset
$H_i=\{u\in U:\psi_i(u)\ge0\}$. The complete intersection is empty.
Compactness of $U$ gives a finite subfamily with empty intersection:
otherwise the closed sets $H_i$ would have the finite intersection
property in $U$. Helly's theorem in $\operatorname{aff}U$ then selects
at most $d+1$ of these sets whose intersection is already empty.
For the selected finite rows, $u\mapsto\min_i\psi_i(u)$ is continuous,
attains its maximum on compact $U$, and that maximum is strictly
negative. Finite minimax (affinity in $u$, linearity in simplex weights)
therefore gives weights $\lambda_i\ge0$, $\sum_i\lambda_i=1$,
with $\max_{u\in U}\sum_i\lambda_i\psi_i(u)<0$.
This is the desired certificate supported on at most $d+1$ labels.
The support bound is existential, not a worst-case search bound;
a collection of affine rows need not arise from an arbitrary prescribed
plant. In the plane the three constraints $u_1\ge1$, $u_2\ge1$,
$u_1+u_2\le1$ have pairwise nonempty intersections but empty total
intersection, showing the sharp row count in dimension two.
\end{proof}'''+S['04'][b:]
rep('04','and no adversarial measure certifies.', 'and no negative averaged measure exists although any strictly negative averaged measure, when present, still soundly rules out all actions without convexity. This counterexample loses completeness, not certificate soundness.')
rep('04','$U = \\{u \\ge 0:\\ u_{1} + u_{2} \\ge 2\\}$ (a demand floor; no capacity\nconstraint is imposed).', '$U = \\{u\\in[0,2]^2:\\ u_{1} + u_{2} \\ge 2\\}$ (a demand floor with\nnonbinding coordinate capacities for the printed witnesses). The capped\nset is compact and convex, as required by the static dual theorem.')
rep('04','so the fibre is viable exactly when','so the fibre admits a common first-order tangent action exactly when')
rep('04','aggregate fibres with $Y \\le \\tfrac{27}{5}$ are\nviable and those with $Y > \\tfrac{27}{5}$ are obstructed', 'aggregate fibres with $Y \\le \\tfrac{27}{5}$ admit a common\nfirst-order floor-tangent action and those with $Y > \\tfrac{27}{5}$\ndo not. This pointwise fibre test is not a proof of controlled invariance\nof the evolving fibre or of a global viability kernel')
# replace finite-sequence general setup/theorem/proof with action-dependent review theorem
start=S['04'].index('\\section{The general finite-sequence envelope}')
end=S['04'].index('\\begin{remark}[the recourse certificate',start)
S['04']=S['04'][:start]+r'''\section{A finite-sequence envelope with action-dependent reviews}

The review tree may depend on earlier actions: a stock observation after
control generally does. Let $\Omega$ be a finite set of complete exogenous
scenarios (including initial hidden parameters and all disturbances), with
a \emph{single} rational joint probability law $\mu$ on $\Omega$.
No independence or product structure is needed. There are $K$ action
stages with finite action sets $A_k$ and a bounded rational pathwise
functional $G(\omega,a_{1:K})$. Before stage one the controller observes
a cell of a partition $\mathcal P_1$ of $\Omega$. At each history
$h=(C,a_{1:k})$, the next observation partitions $C$ into disjoint
subcells $\mathcal C_{k+1}(h)$; the partition is allowed to depend on
the action prefix. Only cells of positive $\mu$-mass are used for
conditional expectations. Histories, rather than scenarios known to
the analyst, determine the available action.

\begin{theorem}[consistent finite review envelope]\label{thm:general}
Put $N_K(C,a_{1:K-1})=
\max_{a\in A_K}\sum_{\omega\in C}\mu(\omega\mid C)
G(\omega,a_{1:K-1},a)$ and, for $k<K$, set
\[
N_k(C,a_{1:k-1})=\max_{a\in A_k}
\sum_{C'\in\mathcal C_{k+1}(C,a_{1:k-1}a)}
\frac{\mu(C')}{\mu(C)}N_{k+1}(C',a_{1:k-1}a).
\]
Then $\sup_{\pi\,\mathrm{adapted}}E_\mu G^\pi
=\sum_{C\in\mathcal P_1}\mu(C)N_1(C)$, omitting null initial cells.
The maximum is attained. All values are rational. For every fixed
policy the conditional-expectation process along its induced review
filtration is a martingale. If a second information design refines every
reachable observation partition under the same action prefix, its
optimized value cannot decrease. If the root value is negative, every
admissible policy has a strictly negative $G$ on a set of positive
$\mu$-measure. If $G$ is a weighted sum of genuine safety-facet
margins with nonnegative weights, such a realization violates at least
one facet; an arbitrary payoff lacks that physical implication.
\end{theorem}
\begin{proof}
At a terminal cell the action is common across all compatible scenarios:
taking $\max_a$ \emph{after} its conditional average gives $N_K$;
scenario-wise optimization here would improperly reveal hidden data.
At an earlier cell the current action is likewise common. Conditional
probabilities of its disjoint successor cells are $\mu(C')/\mu(C)$,
with the same joint law throughout the tree. Backward induction gives
the displayed conditional optimum at every positive-mass node; finite
maxima permit a compatible maximizing action at each history. Summing
at the root proves the identity. Conditional expectations of the same
terminal random variable along the filtration of a \emph{fixed} policy
satisfy the tower law and form a martingale; the optimized envelope
need not itself be a martingale. A refinement embeds every old adapted
policy into the larger class, proving monotonicity. Finally
$E_\mu G^\pi<0$ rules out $G^\pi\ge0$ almost surely. For a
nonnegative weighted sum of facet margins, strict negativity implies
at least one constituent facet margin is negative on that scenario.
\end{proof}

\noindent\textbf{Fixed-prior versus adversarial coupling.} The theorem
conditions on one joint law. An adversary allowed to choose among
consistent couplings asks for $\inf_{\mu\in\mathfrak M}\sup_\pi
E_\mu G^\pi$, a different optimization; a root result for one $\mu$
proves no equality for that robust value. The two-window example takes
$\Omega=\{\pm1\}^3$ (the hidden $s$ and $d_1,d_2$), a uniform product
law for that particular calculation, a blind first cell, and a second
review cell keyed by the \emph{action-dependent} observation $z_1$.
The final review cell need not be a singleton. This is precisely the
information pattern addressed by the theorem.

'''+S['04'][end:]
rep('04','--- all $3^{4} = 81$ policy trees over the reachable $z_1$ cells ---', '--- 81, 9 or 81 reachable second-stage policies conditional on the\nfirst action $u_1=-2,0,2$ (171 reachable policy trees in all) ---')
rep('04','The one-step adversarial priors couple to the product measure on\n$(d_1, d_2)$', 'The declared uniform law on $(s,d_1,d_2)$ is a consistent joint law')
rep('04','so the bridge lemma applies verbatim.', 'with the expectation taken under the declared joint law; the pathwise\npayoff is $G(s,d_1,d_2;u_1,u_2)=2-|z_2|$.')
rep('04','The instance of the previous section is the $K = 2$ case of a general\nstatement.', 'The action-dependent review pattern is a special case of the theorem below.') if False else None
# 05: all-dimension finite-slack theorem; precise work and bibliography
mark='\\begin{corollary}[the cube\'s pairs are Hamming-adjacent]'
assert mark in S['05']
new=r'''\begin{theorem}[global drift criterion for blind viability]
\label{scale-thm:global-drift}
Let $S$ be any nonempty finite set of hidden cells and let $U$ be a
finite rational action set with state-independent per-step drift
$d(u,\theta)$. The following are equivalent:
(i) some blind action sequence preserves every cell of $S$ forever
from some common \emph{finite} starting stock;
(ii) a probability vector $p$ on $U$ satisfies
$\sum_u p(u)d(u,\theta)\ge0$ for every $\theta\in S$;
(iii) a finite periodic blind word survives forever from a sufficiently
large finite starting stock. For the cube model in this paper these are
also equivalent to the exact minimax criterion
\[
\max_{y\in[-1,1]^m}\min_{\theta\in S}\theta\cdot y\ge\frac52
\quad\Longleftrightarrow\quad
\min_{q\in\Delta(S)}\left\|\sum_{\theta\in S}q_\theta\theta\right\|_1
\ge\frac52.
\]
The criterion decides existence from \emph{some} finite initial stock,
not viability from a prescribed stock or after observations.
\end{theorem}
\begin{proof}
For (i)$\Rightarrow$(ii), the finite simplex of empirical frequencies
of actions is compact. Choose a convergent subsequence of these
frequencies. For each cell the cumulative drift is bounded below by
$1-z_0$; after division by elapsed time its subsequential limit is
nonnegative. The limit frequencies thus satisfy all the inequalities.
For (ii)$\Rightarrow$(iii), the feasible polytope has rational data
and has a rational point $p'$. Multiplying by a common denominator
turns $p'$ into a finite action word. Its total drift in each cell is
nonnegative. The largest finite within-word drawdown over the finitely
many cells is finite: starting at least that far above the floor makes
every cycle safe, regardless of the ordering of the word. Periodicity
implies (i). In the cube, the convex hull of its sign-vector actions
(and the hold) is $[-1,1]^m$; averaging drifts gives
$-1/2+\theta\cdot y/5$. The two displayed expressions are equal by
finite-dimensional convex minimax because
$\max_{y\in[-1,1]^m}y\cdot v=\|v\|_1$. All quantifiers are over the
specified finite blind-action model, not an adaptive policy class.
\end{proof}

'''
S['05']=S['05'].replace(mark,new+mark,1)
rep('05','\\(16 \\times 2^{32} = 68{,}719{,}476{,}736\\) raw subsets collapse to \\(1{,}552\\) stored sets. The raw lattice grows \\(65{,}536\\times\\) against a \\(3.13\\times\\) growth in the stored object, improving compression by four orders of magnitude;', '\\(16 \\times 2^{32} = 68{,}719{,}476{,}736\\) \\emph{possible} (level, subset) combinations are represented by \\(1{,}552\\) maximal sets. This is a representation ratio against a hypothetical power-set baseline, not the number of subsets evaluated or a runtime speedup;')
rep('05','so that \\(16 \\times 2^{32}', 'so that \\(16 \\times 2^{32}') if False else None
rep('05','All eight radii and the sign pattern', 'All six radii at \\(m=3,\\ldots,8\\) and the sign pattern')
rep('05','with the asymptotic count \\(2^{\\binom{n}{\\lfloor n/2\\rfloor}(1+o(1))}\\) due to Kleitman\n(1966)', 'with the asymptotic count \\(2^{\\binom{n}{\\lfloor n/2\\rfloor}(1+o(1))}\\) associated with the Dedekind-number literature\n(Kleitman, 1969)')
rep('05','The\nhistorical \\(134\\) counted only lines opening with \\texttt{theorem}:','A source count limited to lines opening with \\texttt{theorem}')
rep('05','The prior provisional\n\\(135\\) report was also an incomplete static count; the\nreproducible source census supersedes it.', 'This count concerns declaration headers, not proof coverage of the paper.')
rep('05','and the simulation is now redundant --- the','and the simulation supplements the analytic result --- the') if False else None
rep('05','For the deadline the simulation is now redundant --- the\nthreshold is proved --- and is retained as an independent cross-check.', 'For the deadline the threshold follows analytically; the finite run checks\nonly its sampled instances.')
rep('05','Where this text previously attributed a result to simulation', 'The analytic result')
S['05']=S['05'].replace('Chatterjee, Doyen and Henzinger, 2009','Chatterjee, Doyen and Henzinger, 2010')
S['05']=re.sub(r'(Chatterjee, K\., Doyen, L\., Henzinger, T\.A\., )2009\.',r'\g<1>2010.',S['05'])
S['05']=S['05'].replace('(MFCS 2009). LNCS, vol. 5734, pp. 635--646.', '(MFCS 2010). LNCS, vol. 6281, pp. 258--269.')
# 06: exact synchronization lemma and remove reversed implications.
mark='\\textbf{Theorem 6 (finite-menu geometric characterization).}'
assert mark in S['06']
S['06']=S['06'].replace(mark,r'''\textbf{Path-to-margin synchronization lemma.} Let the componentwise
within-path required margins of plan $a$ be
$d_{a,i}=\max_{t\in[0,1]}r_{a,i}(t)$ for continuous deficit paths
$r_{a,i}$. For any fixed $w\ge0$, the scalarized path requirement is
$m_a(w)=\max_t\sum_iw_i r_{a,i}(t)$ and always satisfies
$m_a(w)\le w\cdot d_a$. Equality holds if and only if a single time
attains $d_{a,i}$ simultaneously for every coordinate with $w_i>0$.
Indeed, every summand is at most its own maximum. At a maximizer of
the continuous scalarized path, equality of the nonnegative weighted
sum of these inequalities forces equality in every positive-weight
coordinate. Thus the margin-vector geometry below describes the
$w\cdot d_a$ protocol exactly; it is conservative for a protocol that
scalarizes first and only then takes its within-path maximum. Neither
interpretation may be substituted for the other without synchronization.

'''+mark,1)
rep('06','\u201cejected at every weighting\u201d','rejected at every weighting') if False else None
# targeted locally inspect specific text before replacement of tabular cell
for a,b in [('rejected at every weighting','accepted for every weighting under the scalarized protocol; typed rejection is a separate question'),('passes every weighting but no plan passes every floor','passes each weighting with an available plan, but no plan passes every floor')]:
    S['06']=S['06'].replace(a,b)
rep('06','(\\sqrt{2},\\sqrt{2})', '(\\varphi,\\varphi)', n=1)
rep('06','cubic master root','root \\(\\sqrt{6\\sqrt{3}-9}\\)')
rep('06','\u201cdiscrete time-sharing does not\u201d','discrete time-sharing does not') if False else None
# add a principle that separately identifies fixed-weight false acceptance
anchor='\\textbf{Theorem 6 (finite-menu geometric characterization).}'
S['06']=S['06'].replace(anchor,r'''\textbf{Fixed-weight countermechanism.} The quantifier gap is not
necessary for false acceptance. At $s_1=s_2=6/5$ with resource
$x=1/2$, the fixed weight $w=(1,1)$ accepts a primitive menu plan
because its scalar margin meets $s_1+s_2=12/5\ge2$; no primitive plan
meets both typed floors. Enlarging the weight family to the full cone
makes the scalarized protocol stricter than any one nonempty subfamily,
but does not turn this point into a typed-safe one. This assertion is
about the stated action-indexed path/margin protocol, not an identity
between different-time scalarized and componentwise minima.

'''+anchor,1)
# 09: challenge F4 and method horizon; retain numeric historical table as method output
rep('09','the horizon is set by the fitted map, not by the method.', 'the horizon depends jointly on the fitted map, the declared defect, the\ninitial-state ceiling and the particular certificate conversion; it is not\na universal expiration date for an observed stock.')
rep('09','The certified kernel at\nhorizon T is the nominal kernel of \\(K^{\\ast}\\) + r\\_T, with r\\_T as in\nCalculation 2.1.', 'For a constant-pumping affine closed loop satisfying (F4), the\nthreshold-erosion construction at horizon T uses the nominal kernel\nof \\(K^{\\ast}\\) + r\\_T, with r\\_T as in Calculation 2.1. For a\nstate-triggered rule this construction is conditional on an independently\nverified closed-loop cross-trigger modulus as specified below.')
start=S['09'].index('Two properties of the certified layer must be stated before the results,')
end=S['09'].index('\\subsection{3. Results}',start)
S['09']=S['09'][:start]+r'''A cross-trigger comparison is required for feedback. For the scalar
closed loop $f_P(H)=aH+b-\gamma P(H)$, the exact difference identity is
\[
f_P(H)-f_P(\widetilde H)=a(H-\widetilde H)
-\gamma[P(H)-P(\widetilde H)].
\]
Constant pumping makes the bracket vanish, but a trigger may introduce
a jump. On a declared head domain $D$ define the local oscillation
$\omega_P(r;D)=\sup\{|P(x)-P(y)|:x,y\in D,|x-y|\le r\}$.
If model error per step is bounded by $\varepsilon$ and both nominal
and perturbed paths stay in $D$, the inductive radius
\[
R_0=0,\qquad R_{t+1}=|a|R_t+\gamma\omega_P(R_t;D)+\varepsilon
\]
is a valid trajectory-error bound by the triangle inequality. For
constant pumping $\omega_P=0$ and the printed geometric $r_T$ follows.
For a threshold rule the oscillation may not tend to zero with $r$;
using $r_T$ without proving that trajectories remain in one affine
regime is unjustified. A same-regime calculation is valid conditionally
when every nominal and perturbed trajectory is separated from each
trigger by the requisite radius at every time. Neither the trigger
entry of a \emph{raised safe threshold} nor identical within-regime
slopes proves that separation. The historical feedback values below
are therefore conditional stress-test outputs of the originally
specified conversion, not newly established uniform closed-loop
certificates. No physical-error guarantee follows when the declared
training defect is exceeded out of sample.

'''+S['09'][end:]
rep('09','Because the audit correctly flagged', 'Because the model requires') if 'Because the audit correctly flagged' in S['09'] else None
rep('09','because the audit correctly flagged the earlier account as imprecise', 'because the conversion requires an explicit operator domain') if 'because the audit correctly flagged the earlier account as imprecise' in S['09'] else None
rep('09','\\(C_{\\mathrm{vac}} = 215.2\\)\nkt). Every declared reactive', '\\(C^* = 91.59\\)\nkt) for the indicated admissible band. The class-specific vacuity\nlimits are about \\(8.73\\) kt (q05) and \\(215.22\\) kt (q10)\nusing the printed \\(g_{\\max}=296.09\\) kt; the worst class has no\nnonnegative constant-catch vacuity limit. Every declared reactive')
rep('09','from T = 3 at BAU through T \\ensuremath{\\approx} 6 at\nflat-50\\% to T \\ensuremath{\\approx} 6--11 for zero pumping', 'from T = 3 at BAU to a ceiling-dependent longer horizon for flat-50\\%\nand zero pumping')
rep('09','so the 710-ft ceiling gives 12.7 years', 'so the 710-ft ceiling gives 12.7 years') if False else None
# Reconcile spurious figure/header, and method-dependent interpretation
rep('09','Schaefer, M.B., 1954. Some aspects of the dynamics of populations important to the\nmanagement of the commercial marine fisheries. \\emph{Bulletin of the Inter-American\nTropical Tuna Commission}, 1(2), 27--56. Reprinted in \\emph{Bulletin of Mathematical\nBiology}, 53, 253--279, 1991, doi:10.1007/bf02464432.\n\nWorst, \\(T=1\\)', 'Worst, \\(T=1\\)')
# preserve existing table data until regenerated; do not replace an unverified 1074.8 with another guess
# write only now that all assertions passed
for k,(stem,old,new) in VERS.items():
    path=R/f'paper{k}_{stem}_v{new}.tex'
    assert not path.exists(),path
    path.write_text(S[k])
    print(k,path,len(S[k]),'bytes')

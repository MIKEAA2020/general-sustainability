#!/usr/bin/env python3
from pathlib import Path
p=Path('/home/user/papers')
s=(p/'paper03_computational_certification_v19.tex').read_text()
def repl(a,b):
 global s
 assert s.count(a)==1,(s.count(a),a[:100]);s=s.replace(a,b)
repl('the displayed pair schedules reach their respective position ceilings at\n\\(\\approx 0.245\\) and \\(\\approx 0.397\\), while all-control\npair nonviability beyond those values is not established; singletons remain viable in the stated model', 'exact two-label duals certify pair impossibility past \\(\\tau_{12}=\\tau_{13}=(15-\\sqrt{183})/6\\) and \\(\\tau_{23}=(10-\\sqrt{58})/6\\), while the explicit paired schedules attain equality and all smaller delays at \\(T=6/5\\); singletons remain viable in the stated model')
repl('For each pair, the displayed schedule is safe up to its stated root\nprovided its remaining facets and the fixed terminal horizon are checked;\nthis is a sufficient schedule, not an all-control impossibility proof beyond the root; the verification script verifies the full seven-facet scan exactly at rational\nsurrogates below each threshold (\\(\\tau = \\tfrac6{25}\\) and\n\\(\\tau = \\tfrac{39}{100}\\)); those checks alone do not\ncover every real delay below the respective ceiling roots.', 'At the declared horizon \\(T=6/5\\) these are \\emph{exact all-control delay thresholds} for the two-branch beliefs: a single selected schedule is safe at equality and all smaller delays, and the dual below excludes every measurable common-blind/post-revelation policy at every larger delay. The all-time seven-facet proof is given below; finite checks at rational surrogate delays are not used to fill a continuum gap.')
# locate after proof of shared-authority proposition
anchor='\\end{proof}\n\nThe prescriptive reading follows directly.'
assert s.count(anchor)==1
thm=r'''\end{proof}

\begin{theorem}[exact two-branch obstruction at the fixed horizon]
\label{thm:pair-duals}
For the plant and observation protocol of Section~\ref{instance} at
$T=6/5$, the beliefs $\{1,2\},\{1,3\},\{2,3\}$ admit a safe
measurable observation-adapted controller precisely when, respectively,
$\tau\le(15-\sqrt{183})/6$, $\tau\le(15-\sqrt{183})/6$, and
$\tau\le(10-\sqrt{58})/6$. No assumption of blockwise-constant
control is needed for the impossibility direction.
\end{theorem}
\begin{proof}
Write the pair as $B=\{i,j\}$, and let $t=2/5$ for a pair
containing branch 1 and $t=3/5$ for $\{2,3\}$. Give the critical
position facets the normalized weights $(3/8,5/8)$ for $(1,2)$ or
$(1,3)$, and $(1/2,1/2)$ for $(2,3)$. The pooled unit-normal vector
$v=\lambda_i n_i+\lambda_j n_j$ is respectively $(0,1/2)$,
$(0,-1/2)$, or $(-3/5,0)$, and its support on the hexagonal $U$ is
$h_U(v)=t$ (direct evaluation at its six vertices). Each individual
normal has support one. Choose the two facet labels at the common time
$s_*=\tau+q$, $q=1-t\tau>0$. Their row threshold is
$\beta=16/25-s_*$; the exact continuous dual is
\[
\Gamma_B(\tau;s_*)
=-t\int_0^\tau(s_*-s)\,ds
-\int_\tau^{s_*}(s_*-s)\,ds-\beta
=-\frac7{50}+(1-t)\tau-\frac{t(1-t)}2\tau^2.
\]
This integration minimizes over \emph{every} measurable common
blind control and every independently chosen measurable post-revelation
control; hence $\Gamma_B>0$ is an all-control nonviability
certificate. It is strictly increasing for $0\le\tau<1/t$ and
its first zero is exactly the displayed root. For each root
$s_*=1+(1-t)\tau<6/5$ (the rational brackets
$0.2453<\tau_{12}<0.2454$ and
$0.3973<\tau_{23}<0.3974$ verify this). Thus for any delay just above
each root, still with $s_*\le T$, the dual is strictly positive.
A controller that observes no later than $\tau$ can always ignore
premature information; therefore feasibility is monotone decreasing
with the delay. For an arbitrary delay beyond the root choose an
intermediate delay with positive dual and $s_*\le T$; its obstruction
transfers to the later delay.

For the converse, at the root use the constant blind controls of
Proposition~\ref{prop:ladder}: $w=(-2/5,-4/5)$ (or its reflection) or
$w=(1,0)$, followed on branch $j$ by $u=-n_j$ for
$q=1-t\tau$ and then $u=0$ until $T$. The critical position is
nondecreasing until the projected velocity becomes zero at $s_*$,
where it equals $2$ by the quadratic identity above, and then remains
constant. For every other position facet $i\ne j$, $n_i\cdot n_j<0$
and $h_U(n_i)=1$, so at every $0\le s\le6/5$,
\[
n_i\cdot p_j(s)\le (34/25+s)n_i\cdot n_j+s^2/2
\le18/25<2.
\]
Each velocity coordinate is affine on each of the three control legs.
Its largest absolute value therefore occurs at the endpoints of those
legs. At the blind endpoint it is $n_j+\tau w$; at the end of braking
it is $\tau(w+t n_j)$; initially it is $n_j$. Substituting the three
specified $w$ and the two rational upper root bounds above shows every
coordinate at each junction has magnitude at most $1$ (at most $4/5$
for $\{2,3\}$), strictly below $6/5$. These bounds verify all seven
facets continuously, including the final hold leg. Finally, an earlier
revelation may be ignored until the certified root; the same schedule
is then admissible and safe. This establishes the closed-endpoint
thresholds, not just isolated rational viability samples.
\end{proof}

The prescriptive reading follows directly.'''
s=s.replace(anchor,thm)
# remove remaining contradictory label re generic schedule roots where theorem now proves exact
s=s.replace('selected-schedule pair ceiling roots', 'exact pair obstruction thresholds')
s=s.replace('the selected-schedule pair ceiling roots', 'the exact pair obstruction thresholds')
s=s.replace('the two-mode cells\n\\(\\{1,2\\}\\) and \\(\\{2,3\\}\\) admit the displayed schedules to', 'the two-mode cells\n\\(\\{1,2\\}\\) and \\(\\{2,3\\}\\) have exact all-control thresholds')
s=s.replace('an exact triple obstruction and constructive pair lower bounds:', 'an exact triple obstruction and exact two-label pair duals:')
s=s.replace('pair schedule roots', 'pair thresholds')
s=s.replace('paper03\\_computational\\_certification\\_v19\\_supplementary.tex','paper03\\_computational\\_certification\\_v20\\_supplementary.tex')
out=p/'paper03_computational_certification_v20.tex';assert not out.exists();out.write_text(s)
supp=p/'paper03_computational_certification_v20_supplementary.tex';assert not supp.exists();supp.write_bytes((p/'paper03_computational_certification_v19_supplementary.tex').read_bytes())
print(out,len(s),'supplement unchanged copied')

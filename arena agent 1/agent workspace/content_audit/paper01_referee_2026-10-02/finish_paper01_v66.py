#!/usr/bin/env python3
"""Downstream semantics and finite-fibre corrections, from the v66 first pass."""
from pathlib import Path
R=Path('/home/user/paper 2 family/01_obstruction');p=R/'paper01_obstruction_calculus_v66.tex';A=p.read_text()
def ch(old,new,label):
 global A
 n=A.count(old);assert n==1,(label,n,old[:100]);A=A.replace(old,new)
start=A.index('\\textbf{A two-patch protection audit.}')
end=A.index('\n\n\\begin{table}[t]',start)
A=A[:start]+r'''\textbf{A two-patch protection audit.} At each step one of two
patches \(z_i\in\{0,1,2,3\}\) receives protection \(u\in\{1,2\}\).
The transition is \(z_i^+=\min\{3,z_i+1-2\mathbf 1[u\ne i]\}\):
the protected patch gains one unit up to the cap, while the other
loses one net unit (recruitment of one less a loss of two).
The floor is \(z_i\ge1\) and the observed reading is
\(y=z_1+z_2\). In this finite discrete model the exact one-step
test is Theorem~\ref{calc-thm:onestep}, not the continuous-time boundary
tangency condition of Theorem~\ref{calc-thm:common-action}.
The actual current y-fibres have verdicts in
Table~\ref{calc-tab:patch}. The y=4 fibre is especially instructive:
all three states are safe and individually viable under full
information, so y=4 is a certainly-safe \emph{reading}, yet the fibre
is not viable. Action 1 fails at (3,1), sending it to (3,0);
action 2 fails at (1,3), sending it to (0,3). The y=3 fibre
has the analogous action conflict. The y=2 singleton (1,1) is
nonviable even with full information: it is a dynamic, not an epistemic,
failure. The viable y=5 fibre has a history-dependent witness: play
\(u=1\) while the reading remains 5, reaching the known singleton (3,1)
when it first becomes 4; thereafter alternate 2,1 to cycle (3,1)
and (2,2). The y=6 singleton reaches y=5 under \(u=1\) and uses the same
continuation. Certainly-safe readings are y>=4, whereas viable
\emph{full initial fibres} have y>=5. These exact recursion results
concern the declared finite model, not a calibrated resource system.'''+A[end:]
start=A.index('\\begin{table}[t]',A.index('\\textbf{A two-patch protection audit.}'))
end=A.index('\\end{table}',start)+len('\\end{table}')
A=A[:start]+r'''\begin{table}[t]
\centering
\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lcll@{}}
\toprule
actual current fibre & \(y\) & verdict & certificate / witness \\
\midrule
\(\{(1,1)\}\) & 2 & nonviable & full-information one-step failure \\
\(\{(1,2),(2,1)\}\) & 3 & nonviable & no common safe first action \\
\(\{(1,3),(2,2),(3,1)\}\) & 4 & nonviable & no common safe first action \\
\(\{(2,3),(3,2)\}\) & 5 & viable & \(u=1\) until y=4, then 2,1 cyclically \\
\(\{(3,3)\}\) & 6 & viable & \(u=1\), then y=5 witness \\
\bottomrule\end{tabular}}
\caption{The five actual safe-state fibres of the aggregate reading
\(y=z_1+z_2\). The one-step discrete obstruction is
Theorem~\ref{calc-thm:onestep}; the y=2 singleton fails even with full
information. The y=4 reading certifies current safety but cannot
support one common safe action. The viable rows admit the stated
history-dependent policies.}
\label{calc-tab:patch}
\end{table}'''+A[end:]
# Do not apply a continuous differential theorem directly to a discrete-time toy.
ch('The hidden-regime instance of Section 9 is this check \\emph{for its explicitly declared whole-window hold class}:','The hidden-regime instance of Section 9 is a \\emph{discrete analogue} of this check for its declared whole-window hold class, not an application of the continuous drift theorem:','timing check discrete')
ch('This is an application of\nTheorem~\\ref{calc-thm:delayed} to the \\emph{restricted} implementable\nclass, not an assertion that its (H3.2) holds under arbitrary blind\nswitching:','This is an exact \\emph{discrete hold-class} calculation from the\nfinite recursion, not a verification of the continuous Theorem~\\ref{calc-thm:delayed}:','case study discrete')
ch('certified only by the hold-class timing bound (Theorem~\\ref{calc-thm:delayed} with this institutional restriction).','classified by the discrete hold-class survival threshold and exact finite recursion (not by the continuous Theorem~\\ref{calc-thm:delayed}).','coverage caption')
ch('the delay-free setting makes the timing bound of Theorem~\\ref{calc-thm:delayed} sharp,','the continuous timing bound of Theorem~\\ref{calc-thm:delayed} is sufficient under its strengthened adverse-realization hypothesis, not generally sharp;','sharp')
ch('Theorem~\\ref{calc-thm:delayed} gives the minimal monitoring frequency in\nclosed form:','Theorem~\\ref{calc-thm:delayed} gives a conditional sufficient bound on\nmonitoring timing in the continuous model, not a general minimum frequency:','monitoring')
ch('Let \\(B_0\\) be an initial information set. Suppose the following','Let \\(B_0\\) be an initial post-observation information cell whose\nmembers share a current reading. Suppose the following','Thm3 initial cell')
ch('Let \\(\\mathcal{V}\\) be compact with \\(C^{1}\\) constraint functions \\(q_{j}\\), \\(f\\) continuous with \\(D\\) compact-valued and of closed graph, \\(U(x) \\equiv U\\), and suppose the observation is \\emph{static}:','Let \\(B_0\\) be a post-observation cell with one initial reading. Let \\(\\mathcal{V}\\) be compact with \\(C^{1}\\) constraint functions \\(q_{j}\\), \\(f\\) continuous with \\(D\\) compact-valued and of closed graph, \\(U(x) \\equiv U\\), and suppose the observation is \\emph{static}:','Thm7 cell')
ch('Five mechanisms are established --- two finitely checkable, two\nclosed-form conditional, one minimal --- with a sixth under a\npolicy-class restriction.','The paper separates dynamic exit, epistemic action and timing\nobstructions, static certification limits, and failure of a declared\npolicy class; these are distinct kinds of result, not one list of\nnonviability conditions.','abstract taxonomy')
ch('post-observation recourse phase\nundecidable by any certificate pair that reads only the window sub-model.','post-observation recourse verdict not determined by the window sub-model\nalone.','abstract undecidable')
ch('Five obstruction mechanisms are developed, each with a complete proof,\nand a sixth is exhibited under a policy-class restriction:','The following certificates, classification criteria, exact algorithms and\npolicy-class cautions play different roles:','contribution count')
ch("policy-specific failure: a controller that uses the observation map's\npolicy-specific failure: a controller that uses the observation map's","policy-specific failure: a controller that uses the observation map's",'duplicate CE')
ch('a calibrated case study with a coverage audit','a symbolic case study with a coverage audit','lead calibration')
ch('the calibrated delayed-hidden-regime','the symbolic delayed-hidden-regime','lead 2 calibration')
ch('\\subsection{9. A Calibrated Case Study and a Coverage Audit}','\\subsection{9. A Symbolic Case Study and a Coverage Audit}','section title calibration')
ch('a calibrated case study and a coverage audit reproduce','a symbolic case study and a coverage audit reproduce','conclusion calibration')
ch('specification. Four elements complete the picture:','specification. The principal further elements are:','conclusion count 1')
ch('A fourth completion is structural:','A separate structural result concerns','conclusion count 2')
ch('post-observation recourse phase undecidable by any window-measurable certificate','post-observation recourse verdict not determined by any window-only certificate','conclusion undecidable')
# Clear downstream claims whose original premises were removed or changed.
ch('''With displayed proofs and explicit witnesses, the certificates identify
five mechanisms by which an observation structure can make robust
viability impossible, plus one through which a single uncorrected policy
empties the kernel: the disturbance can enforce exit in finite time
against every control; a constant observation can merge states with
incompatible admissible controls (Proposition~\\ref{calc-prop:emptiness}'s admissibility form);
the compatible states can demand incompatible actions at a single
information state; the information can arrive after the enforced exit;
and the observation fibres can cross the safe-set boundary, defeating
every exact certifier --- with the uncorrected certainty-equivalence controller as the
sixth, policy-specific, mechanism.''','''The results must be separated by claim type. The exit certificate is
dynamic and defeats every control; the common-action and conditional
delayed-information certificates concern failure of a shared response;
Proposition~\\ref{calc-prop:emptiness} is a nonconvex state-dependent
\\emph{safety} instance with a nonempty common admissible set. The fibre
criterion limits exact observation-only verdicts rather than viability,
and the certainty-equivalence example defeats one uncorrected policy,
not every observation-based policy. The finite recursion is an exact
algorithm in its specified finite class.''','conclusion classification')
ch('''\\paragraph{Scope, stated plainly.} What is certified is a \\emph{static} obstruction on the
observation fibre, not the full dynamic epistemic kernel: the audited object is fibre
feasibility, and no claim is made here about the kernel of the transition system induced by
these caps. The distinction matters and should not be blurred. The instance shows a
certificate returning an exact verdict on a continuum, which is the property the calculus
needs; it does not show, and does not claim to show, a certificate deciding a dynamic kernel
that is in principle undecidable. For the limits of what certificate pairs can decide in the
dynamic two-phase model, see Proposition~\\ref{calc-prop:window-nogo}.''','''\\paragraph{Scope.} This is a static two-variable LP: the caps depend only on
\\(Y\\), so every point of the same continuum fibre imposes the \\emph{same}
two inequalities. Its exact rational certificate checks this LP and
illustrates a shared-action failure, but the continuum does not add a
nontrivial finite-witness or Helly problem here. No dynamic epistemic
kernel is decided. Window-only data do not determine the post-reveal
recourse verdict of Proposition~\\ref{calc-prop:window-nogo}; this is
not a computability-undecidability claim.''','LP scope')
ch('\\subsubsection{3.8 A worked case: an exact obstruction on a continuum}','\\subsubsection{3.8 A worked case: a static aggregate LP with a rational dual}','LP title')
ch('''The calculus is motivated by the regime in which the epistemic kernel cannot be computed.
It is therefore worth exhibiting an instance in which a certificate returns an exact verdict
on a set of states that no finite procedure could enumerate. This subsection gives one,
verified in exact rational arithmetic.''','''This subsection gives a simple static aggregate-allocation LP verified
in exact rational arithmetic. Because its constraints depend only on
\\(Y\\), it does not demonstrate a nontrivial state-varying-fibre
Helly witness or an infinite-dimensional dynamic calculation.''','LP intro')
ch('''\\paragraph{What this establishes.} The \\(Y=6\\) fibre is a continuum of states, and the
question "is there an allocation meeting both floors from every state in this fibre?" is not
a question a finite enumeration could settle: there is no finite object to enumerate. The
certificate settles it exactly, with a rational witness and a rational margin, and by the
same argument settles it for \\emph{every} \\(Y\\ge\\tfrac{27}{5}\\) simultaneously. That is the
regime the obstruction calculus is built for, and this is the instance that shows it
operating there.''','''\\paragraph{What this establishes.} The two aggregate caps yield a
finite LP, which the rational witness and margin decide for every
\\(Y\\ge\\tfrac{27}{5}\\). This result does not rely on enumerating the
individual points in a fibre.''','LP claim')
ch('\\emph{every} observation-based policy --- not merely against Lipschitz memoryless selections of the current output','\\emph{every} observation-based policy in the declared class under its realization and blind-record hypotheses --- not merely against Lipschitz memoryless selections of the current output','lit scope')
ch('''The audit is reproduced by the script \\texttt{paper2\\_coverage\\_audit.py}, publicly available at \\url{https://github.com/MIKEAA2020/general-sustainability} (folder \\texttt{arena agent 1/paper rewrites/latex}), which regenerates Table~\\ref{calc-tab:coverage} and Figure~\\ref{calc-fig:coverage} verbatim.''','''The archived \\texttt{paper2\\_coverage\\_audit.py} reproduces the
finite-grid classification; this discrete calculation is not a proof of
the continuous Theorem~\\ref{calc-thm:delayed}.''','coverage archive wording')
ch('orange = nonviable \\emph{only in the audited hold class}, certified there by the timing bound.','orange = nonviable \\emph{only in the audited hold class}, established by the discrete hold-class survival calculation.','figure orange')
ch('the remaining 12 --- those with \\(z_{0}\\ge2\\) and integer \\(T_{\\mathrm{obs}}>z_{0}-1\\) --- by the hold-class timing bound;','the remaining 12 --- those with \\(z_{0}\\ge2\\) and integer \\(T_{\\mathrm{obs}}>z_{0}-1\\) --- by the discrete hold-class survival calculation;','coverage 12')
ch('the restricted timing calculation covers','the exact discrete hold-class calculation covers','coverage partition')
ch('''the certificate reduces to the finite check that every candidate control enforces exit before \\(T_{\\mathrm{obs}}\\), each worst-case exit time computed by branchwise integration or by the recursion of Section 3.1.''','''the strengthened certificate requires, for each candidate, an
admissible adverse solution with the closed-strip derivative condition
through first boundary contact; finite enumeration of controls alone
does not establish that continuous-time realization.''','checkability')
ch('condition (3) is the timing bound: inverted, it is the design requirement that the first informative observation precede the enforced exit time.','condition (3) is a sufficient timing condition for this obstruction; evading it does not itself establish viability.','timing converse')
ch('A belief \\(B \\subseteq \\mathcal{V}\\) is one-step viable under \\(\\mathcal{I}\\)','A post-observation cell \\(B \\subseteq \\mathcal{V}\\) is one-step viable under \\(\\mathcal{I}\\)','one-step domain')
ch('the discrete reading of Theorem~\\ref{calc-thm:common-action}.','a separate finite/discrete analogue of the continuous Theorem~\\ref{calc-thm:common-action}.','one-step distinction')
ch('certified by the common-action certificate (Theorem~\\ref{calc-thm:common-action}); \\(\\ast\\) nonviable','certified by the finite one-step common-action test (Theorem~\\ref{calc-thm:onestep}); \\(\\ast\\) nonviable','coverage common')
ch('red = nonviable under either class, certified by the common-action certificate;','red = nonviable under either class, diagnosed by the discrete one-step test;','coverage fig common')
ch('30 are certified by the common-action certificate','30 are classified by the finite one-step test','coverage total 30')
ch('The common-action certificate covers \\(z_0<2\\);','The finite one-step test covers \\(z_0<2\\);','coverage partition common')
p.write_text(A)
s=R/'paper01_obstruction_calculus_v66_supplementary.tex';T=s.read_text();old='Let \\(B_0\\) be an initial information set. Suppose the following';assert T.count(old)==1;T=T.replace(old,'Let \\(B_0\\) be an initial post-observation information cell whose\nmembers share a current reading. Suppose the following')
old='a review interval longer than the\nworst-case exit time is an information structure in which the exit is inevitable.'
assert T.count(old)==1;T=T.replace(old,'under the theorem\'s closed-strip drift and genuine-trajectory hypotheses, a blind window\nlonger than the certified bound forces a violation; outside those\nhypotheses no such claim is established.')
s.write_text(T)
print('FINISHED v66 source heads',len(A),len(T))

#!/usr/bin/env python3
"""Draft v66 from immutable v65. Checks textual anchors; no proof-referee claims."""
from pathlib import Path
R=Path('/home/user'); base=R/'paper 2 family/01_obstruction'
A=(base/'paper01_obstruction_calculus_v65.tex').read_text();S=(base/'paper01_obstruction_calculus_v65_supplementary.tex').read_text()
def change(text,old,new,label):
 n=text.count(old)
 assert n==1,(label,n,old[:100])
 return text.replace(old,new)
# Theorem 3: quantifier and actual through-boundary drift, retaining the adversarial
# forall policy/exist scenario order rather than demanding drift on every trajectory.
h1='''(H3.1) No informative observation arrives before time
\\(T_{\\mathrm{obs}} > 0\\) --- formally, there are branches that are
\\textbf{observation-equivalent on \\([0, T_{\\mathrm{obs}})\\)}: they
produce identical observation records throughout that interval, so the
policy cannot distinguish them before \\(T_{\\mathrm{obs}}\\); between
observations the information set evolves by the set-membership semantics
of Section 2.3.'''
h1new='''(H3.1) Fix a blind interval \\([0,T_{\\mathrm{obs}})\\) with
\\(T_{\\mathrm{obs}}>0\\). For each implementable control history in the
declared class, \\emph{every} compatible realization while safe produces
the same observation record on this interval (up to its first exit).
Thus no branch-dependent observation can change the policy's control
before exit; the set-membership information state may evolve, but the
common record contains no branch-discriminating signal.'''
h2='''There exist a constraint function \\(q\\) of class \\(C^1\\) (the class of Theorem~\\ref{calc-thm:exit}'s proof, Section 3.5) with \\(\\mathcal{V} \\subseteq \\{ q \\ge 0 \\}\\)
and a constant \\(\\varepsilon > 0\\) such that, \\textbf{for every implementable blind-window control in the fixed class} ---
each of its controls is measurable on \\([0, T_{\\mathrm{obs}})\\) and admissible at
every compatible state throughout the blind window, \\(u(t) \\in U^B(B_t)\\)
with \\(B_t\\) the set-membership belief propagated under \\(u(\\cdot)\\) ---
which is the full class realizable before the first informative
observation \\emph{only in the unrestricted case}; a declared hold class
is a proper subclass --- there are a compatible initial state \\(x^* \\in B_0\\) attaining
\\(q(x^*) = \\inf_{x \\in B_0} q(x)\\) (with \\(B_0\\) compact and \\(q\\) lower
semicontinuous; otherwise replace the infimum by \\(\\inf q + \\delta\\) for
an arbitrary \\(\\delta\\)-minimizer, let \\(\\delta \\downarrow 0\\), and read
the timing bound with \\(\\inf q + \\delta\\)) and an admissible disturbance
realization such that, along the realized trajectory from \\(x^*\\) under
that open-loop control, the record remains compatible and
\\[D^+ q(x(t); f(x(t), u(t), d(t))) \\;\\le\\; -\\varepsilon \\qquad \\text{while } q(x(t)) > 0, \\tag{2}\\]'''
h2new='''There are \\(q\\) of class \\(C^1\\), defined on a neighbourhood of
the relevant trajectories, with \\(\\mathcal V\\subseteq\\{q\\ge0\\}\\),
and \\(\\varepsilon>0\\). Let \\(B_0\\subseteq\\mathcal V\\) be compact,
and fix \\(a>\\max_{B_0}q\\ge0\\).
\\textbf{For every implementable blind-window control} \\(u(\\cdot)\\) in the
declared class, measurable and common to all compatible states while
there is no informative observation, there exist a minimizer
\\(x_u\\in B_0\\) of \\(q\\) and an admissible disturbance realization
with an absolutely continuous solution from \\(x_u\\). This solution
exists through any first contact with \\(q=0\\) until either it reaches
\\(q<0\\) or \\(T_{\\mathrm{obs}}\\), and follows the common record
of (H3.1) until exit. For almost every pre-exit time in the closed strip
\\(0\\le q(x(t))\\le a\\), \\emph{including boundary contact},
its actual derivative obeys
\\[\\frac{d}{dt}q(x(t))=\\nabla q(x(t))\\cdot f(x(t),u(t),d(t))
\\;\\le\\;-\\varepsilon. \\tag{2}\\]
The realization is chosen \\emph{after} \\(u\\), not before it. This
condition is on a genuine admissible trajectory of the original system,
not solely on a convexified disturbance inclusion; no exit is assumed
in the hypothesis. It may fail even when a positive-side drift estimate
holds.'''
# main exact text; supplement has its own rendering of the same statement.
A=change(A,h1,h1new,'main H3.1')
start=A.index('(H3.2) Fix the policy class being certified:')
end=A.index('\n\n(H3.3)',start)
A=A[:start]+'(H3.2) Fix the policy class being certified: by default all implementable measurable blind-window controls; a declared whole-window hold class yields only class-relative nonviability. '+h2new+A[end:]
sh1='''(H3.1) No informative observation arrives before time
\\(T_{\\mathrm{obs}} > 0\\) --- formally, there are branches that are
\\textbf{observation-equivalent on \\([0, T_{\\mathrm{obs}})\\)}: they
produce identical observation records throughout that interval, so the
policy cannot distinguish them before \\(T_{\\mathrm{obs}}\\); between
observations the information set evolves by the set-membership semantics
of Section 2.3.'''
S=change(S,sh1,h1new,'supp H3.1')
start=S.index('(H3.2) Fix the class being certified:')
end=S.index('\n\n(H3.3)',start)
old=S[start:end]
new=h2new.replace('of class \\(C^1\\), defined','of class \\(C^1\\), defined')
S=change(S,old,'(H3.2) Fix the class being certified: by default all implementable measurable blind-window controls; a declared whole-window hold class yields only class-relative nonviability. '+new,'supp H3.2')
proof='''\\emph{Proof sketch.} By (H3.1) the policy's actions on \\([0, T_{\\mathrm{obs}})\\) form one fixed open-loop control; if it is ever inadmissible at a compatible state the policy fails outright, otherwise (H3.2), applied to this implementable control, supplies a compatible state \\(x^*\\) with \\(q(x^*) = \\inf_{B_0} q\\) and an admissible disturbance realizing the drift (2); integrating (2) gives \\(q(x(t)) \\le \\inf_{B_0} q - \\varepsilon t\\), so the violation \\(q < 0\\) occurs by time \\(\\inf_{B_0} q / \\varepsilon\\), which (3) places strictly before \\(T_{\\mathrm{obs}}\\) --- before any informative observation, so the policy cannot react in time.'''
proofnew='''\\emph{Proof.} Fix a policy in the declared class. Hypothesis (H3.1)
gives it a common blind control \\(u\\); an action inadmissible on a
compatible branch already fails. Otherwise (H3.2) supplies a compatible
minimizer and a genuine adverse trajectory. Put
\\(h(t)=q(x(t))\\), \\(h(0)=m=\\min_{B_0}q\\ge0\\), and
\\(t_*=m/\\varepsilon<T_{\\mathrm{obs}}\\). Suppose there is no strict
violation by some \\(t_1\\in(t_*,T_{\\mathrm{obs}})\\). As long as
\\(0\\le h\\le a\\), (2) gives \\(h(t)\\le m-\\varepsilon t\\).
The trajectory cannot first leave this strip through \\(h=a\\) because
its derivative is strictly negative there almost everywhere; at a
contact \\(h=0\\) it cannot remain nonnegative through \\(t_1\\)
for the same reason. Hence nonviolation through \\(t_1\\) would give
\\(0\\le h(t_1)\\le m-\\varepsilon t_1<0\\), a contradiction.
This includes \\(m=0\\): negative drift is required at the boundary,
not a vacuous condition on \\(h>0\\). The realization continues through
first contact by (H3.2), so some \\(t<t_1<T_{\\mathrm{obs}}\\) has
\\(q(x(t))<0\\), contrary to safety. The policy was arbitrary; the
quantifier is \\(\\forall\\pi\\,\\exists(x_u,d_u)\\), not a demand that
every trajectory drift downward.'''
A=change(A,proof,proofnew,'main Thm3 proof')
start=S.index('\\emph{Proof.} Fix any observation-based policy \\emph{in the fixed\nclass}.',S.index('\\begin{theorem}[delayed-information obstruction]'))
end=S.index('\n\n',S.index('\\(B_0\\notin\\mathrm{ERViab}_{\\mathcal I}(\\mathcal V)\\).',start))
S=S[:start]+proofnew.replace('\\emph{Proof.}','\\emph{Proof.}')+ '\nOnly an unrestricted blind-control class licenses the conclusion for the\nfull observation-based kernel; a declared hold class does not.'+S[end:]
# Theorem 7: separate the B0 open-loop statement from the all-V invariance test.
old='''necessary for a constant control to keep \\(\\mathcal{V}\\) invariant and sufficient under the standard regularity assumptions (Aubin, 1991; Frankowska, 1989). A time-varying open-loop control may be viable when no constant control is; the open-loop reduction, not the constant-control condition, is the exact characterization in the static class.'''
new='''a sufficient test (under the tangent-cone and solution-existence regularity of the robust Nagumo theorem) for invariance of \\(\\mathcal V\\) from \\emph{every} initial state. Under an appropriate constraint qualification the condition is also necessary for invariance of \\(\\mathcal V\\) as a whole, but it is \\emph{not necessary} for viability from a specified proper subset \\(B_0\\). A time-varying open-loop control may be viable when no constant control is; the open-loop reduction, not a global boundary test, characterizes viability from \\(B_0\\) in the static class.'''
A=change(A,old,new,'main Thm7 statement')
start=A.index('\\emph{Proof.} A static observation makes the record constant',A.index('\\begin{theorem}[static-observation reduction'))
end=A.index('\\hfill\\(\\square\\)',start)+len('\\hfill\\(\\square\\)')
A=A[:start]+'''\\emph{Proof.} A static observation makes the record constant;
for a fixed initial prior belief a record-based policy can therefore be
represented by a time-only control on each initial observation cell.
For a post-observation belief \\(B_0\\) with one reading, this is one
open-loop control, and the equivalence follows in both directions.
Under the standard tangent-cone and existence hypotheses, the displayed
boundary test suffices for invariance of all \\(\\mathcal V\\) with a
constant control. It says nothing necessary about a smaller \\(B_0\\):
for example \\(\\mathcal V=[0,2]\\), \\(\\dot x=x-1\\),
\\(B_0=\\{1\\}\\) has a stationary viable trajectory although the
velocity is outward at both ends of \\(\\mathcal V\\). \\hfill\\(\\square\\)'''+A[end:]
A=change(A,'within the constant-control subclass the boundary condition of Theorem~\\ref{calc-thm:common-action} is necessary and sufficient.','within the constant-control subclass the global boundary condition is a sufficient test for invariance of all \\(\\mathcal V\\), not a necessary test for viability from a specified \\(B_0\\).','Thm7 downstream')
# Define a common ambient belief domain while distinguishing a prior from an actual cell.
old='''Admissible initial
beliefs are the compact information sets \\(B_0 \\subseteq X\\) generated
by the observation structure --- the observation fibres \\(O^{-1}(y)\\),
\\(y \\in O(X)\\), in the constructions of Sections 3.2--3.3 and 3.6. The existential (non-robust) counterpart'''
new='''The common ambient domain for this kernel, for every sensor, is
\\(\\mathfrak B=\\{B\\subseteq X:B\\neq\\varnothing\\}\\); compactness is
assumed separately where a theorem needs it. A general \\(B_0\\) is a
\\emph{prior} before the initial observation; the initial reading
\\(y_0=O(x_0)\\) is available before the first action. The resulting
current information cell is \\(B_{0,y}=B_0\\cap O^{-1}(y)\\), and
subsequent beliefs similarly lie in one current observation cell.
Only such a post-observation cell shares one action \\(u\\in U^B(B)\\).
For a prior spanning readings, the policy may choose separate actions
for different \\(y\\), so the common-action theorems are applied to its
nonempty cells, not to the unsplit prior. Full fibres are the initial
cells when \\(B_0=X\\); histories can yield strict subsets. Observation
measurability alone does not imply compact fibres; the domain does not
silently impose this property. The existential (non-robust) counterpart'''
A=change(A,old,new,'Def1 belief domain')
A=change(A,'''\\(B_0\\) --- admissible initial beliefs are the compact information sets
the observation structure generates, the observation fibres
\\(O^{-1}(y)\\), \\(y \\in O(X)\\), in the constructions.''','''\\(B_0\\) --- a prior in the common ambient domain
\\(\\mathfrak B\\) which is split by the initial observation into
nonempty post-observation cells \\(B_{0,y}=B_0\\cap O^{-1}(y)\\).''','notation belief domain')
A=change(A,'If \\(B\\in\\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V})\\) and \\(\\pi\\) is a\npolicy witnessing viability on \\(B\\), then at every review time the','If \\(B\\in\\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V})\\) is a \\emph{post-observation information cell} and \\(\\pi\\) is a\npolicy witnessing viability on \\(B\\), then at every review time the','Prop1 selector domain')
A=change(A,'in continuous\ntime the converse is the backward-recursion completion noted in\nSection 6.5.','in continuous time no general finite backward-recursion converse is\nclaimed (Section 6.5).','selector converse')
# finite recursion remains on post-observation cells; prior kernel is its y-cell lift.
A=change(A,'For a belief \\(B\\subseteq X\\),\nan action \\(a\\), and an observation \\(y\\), the post-belief is','For a post-observation belief \\(B\\subseteq X\\) contained in one\ncurrent observation cell, an action \\(a\\), and a successor observation\n\\(y\\), the post-belief is','recursion precondition')
A=change(A,'An initial belief \\(B_0\\) admits an observation-based policy that keeps\nevery compatible trajectory in \\(\\mathcal V\\) for \\(N\\) steps if and only\nif \\(B_0\\in\\mathcal W_N\\).','An initial \\emph{post-observation cell} \\(B_0\\) admits an observation-based\npolicy keeping every compatible trajectory in \\(\\mathcal V\\) for\n\\(N\\) steps if and only if \\(B_0\\in\\mathcal W_N\\). For a prior\n\\(P\\in\\mathfrak B\\) before the initial reading, the verdict is\n\\(P\\in\\mathrm{ERViab}_{\\mathcal I,N}\\) if and only if every\nnonempty cell \\(P\\cap O^{-1}(y)\\) belongs to \\(\\mathcal W_N\\).','finite Thm main')
S=change(S,'An initial belief \\(B_0\\) admits an observation-based policy that keeps\nevery compatible trajectory in \\(\\mathcal V\\) for \\(N\\) steps if and only\nif \\(B_0\\in\\mathcal W_N\\).','An initial post-observation cell \\(B_0\\) admits an observation-based\npolicy that keeps every compatible trajectory in \\(\\mathcal V\\) for\n\\(N\\) steps if and only if \\(B_0\\in\\mathcal W_N\\). A prior\n\\(P\\) is viable if and only if every nonempty initial observation cell\n\\(P\\cap O^{-1}(y)\\) belongs to \\(\\mathcal W_N\\).','finite Thm supp')
S=change(S,'\\emph{Proof.} \\((\\Rightarrow)\\) Induction on \\(N\\).','\\emph{Proof.} The initial observation partitions a prior into\ndisjoint cells; one policy may choose independently on each cell. It\ntherefore suffices to prove the post-observation statement.\n\\((\\Rightarrow)\\) Induction on \\(N\\).','finite proof supp')
# Refinement compares kernels on the common prior domain; actual cells vary with sensor.
for label,txt in [('Prop8 refinement',A),('Prop8 supp refinement',S)]:
 old=r'\mathrm{ERViab}^{\mathcal{I}_2} \subseteq \mathrm{ERViab}^{\mathcal{I}_1}.\]'
 new=old+'\nThis refinement inclusion compares kernels on the \\emph{same domain of prior beliefs}; it is not a literal inclusion of differently typed already-observed fibres.'
 if label=='Prop8 refinement':A=change(txt,old,new,label)
 else:S=change(txt,old,new,label)
# Minimal nonconvex example is a safety obstruction, not empty common U.
A=change(A,'admissibility (Proposition~\\ref{calc-prop:emptiness}) & \\(U^B(B)=\\varnothing\\) & enlarge the command set','state-dependent admissibility example (Proposition~\\ref{calc-prop:emptiness}) & \\(U^B(B)=\\{0\\}\\), but \\(\\mathcal R_{\\mathcal V}^B(B)=\\varnothing\\) & enlarge the common safe-command set','Table1 Prop5')
A=change(A,'The six mechanisms form a nonexhaustive taxonomy of information-theoretic failure.','The entries below distinguish dynamic, epistemic, classification, and policy-specific mechanisms; they are not all information-theoretic nonviability certificates.','Table1 intro')
A=change(A,'The first six are sound sufficient conditions for nonviability; the last is the exact finite-horizon characterization.','The exit and common-action/timing rows concern nonviability in their stated systems or classes; the fibre row concerns verdicts and the certainty-equivalence row one uncorrected controller. The last row is the exact finite-horizon characterization.','Table1 caption')
A=change(A,'The construction is the minimal instance of Theorem~\\ref{calc-thm:common-action}\'s admissibility mechanism','The construction is the minimal instance of Theorem~\\ref{calc-thm:common-action}\'s safety obstruction, with a nonconvex state-dependent admissibility set','Prop5 description')
# The minimal example U(S) is nonconvex, and controller relaxation changes the result.
A=change(A,'Set \\(U(S) = \\{0, S\\}\\), \\(\\mathcal{V} = [1,2]\\), and the constant observation','Set the \\emph{unrelaxed, nonconvex} \\(U(S) = \\{0, S\\}\\), \\(\\mathcal{V} = [1,2]\\), and the constant observation','Prop5 nonconvex')
A=change(A,'The construction is the minimal instance of Theorem~\\ref{calc-thm:common-action}\'s safety obstruction, with a nonconvex state-dependent admissibility set --- with a constant control set in the same plant the fibre is epistemically viable','The construction is the minimal instance of Theorem~\\ref{calc-thm:common-action}\'s safety obstruction, with a nonconvex state-dependent admissibility set --- with a constant control set in the same plant the fibre is epistemically viable','Prop5 description check') if False else A
# Show the modelling distinction without claiming the disturbance-only relaxation convexifies U.
A=change(A,'the complete isolation of the mechanism is given in the Supplementary Material (S1).','the complete isolation of the mechanism is given in the Supplementary Material (S1). Convexifying the \\emph{controller} sets to \\(\\operatorname{co}U(S)=[0,S]\\) is a different problem: then \\(u\\equiv1\\) is common and keeps every state in \\([1,2]\\); no such controller convexification is used in the original construction.','Prop5 scope')

assert 'while } q(x(t)) > 0' not in A[A.index('\\begin{theorem}[delayed-information obstruction]'):A.index('\\end{theorem}',A.index('\\begin{theorem}[delayed-information obstruction]'))]
(base/'paper01_obstruction_calculus_v66.tex').write_text(A)
(base/'paper01_obstruction_calculus_v66_supplementary.tex').write_text(S)
print('CREATED v66 first-pass main',len(A),'supp',len(S))

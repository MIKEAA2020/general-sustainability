#!/usr/bin/env python3
"""Build new, explicitly unrefereed Paper01 v68 TeX from pinned v67 sources.
Does not edit historical v65/v66/v67 files or assert independent mathematical review.
Run from any directory. Every replacement checks its exact anchor count.
"""
from pathlib import Path
from hashlib import sha256
R=Path(__file__).resolve().parents[2]
D=R/'paper 2 family/01_obstruction'
A0=D/'paper01_obstruction_calculus_v67.tex'
S0=D/'paper01_obstruction_calculus_v67_supplementary.tex'
A1=D/'paper01_obstruction_calculus_v68.tex'
S1=D/'paper01_obstruction_calculus_v68_supplementary.tex'
assert sha256(A0.read_bytes()).hexdigest()=='4f5cc909e9035319e7056d9d9b8d64f60285d9a68bcf801cf5b8154aff9fad39'
assert sha256(S0.read_bytes()).hexdigest()=='99819f72de9c85570ab2daa2f8610ca5c1e8fb703d0a5be8c593b08f2022ce62'
a=A0.read_text();s=S0.read_text();notes=[]
def rep(text,old,new,label):
    assert text.count(old)==1,(label,text.count(old))
    notes.append(label)
    return text.replace(old,new,1)
def block(text,start,end,new,label):
    assert text.count(start)==1,(label,'start',text.count(start))
    i=text.index(start);j=text.find(end,i+len(start));assert j>i,(label,'end not found after start')
    notes.append(label)
    return text[:i]+new+text[j:]

# MAIN SOURCE
# Maintain exact existing title, author and symbolic/example data. Do not add an audit memo to submission prose.
a=rep(a,'\\maketitle\n','\\maketitle\n'+r'\begin{center}\small\emph{Unrefereed author preprint; independent mathematical review pending.}\end{center}'+'\n','main front unrefereed status')
a=rep(a,'finitely\ncheckable in the common-action, fibre-certification, and finite-horizon forms',
      'finitely\ncheckable for declared polyhedral common-action and finite-system classes; the fibre criterion addresses static certification rather than policy nonviability', 'abstract distinct scopes')
a=rep(a,'exit certificate under an Isaacs-type drift condition, an',
      'exit certificate conditional on an Isaacs-type drift bound and a compatible original-system adverse trajectory, an','abstract original path scope')
a=rep(a,'states with incompatible admissible controls, a delayed-information',
      'states whose only common admissible control is unsafe, a delayed-information','abstract admissibility example')
a=rep(a,'sound beyond the\ndeclaration with an unbounded implementable-class gap',
      'with a separate unbounded gap relative to a narrower whole-window hold class','abstract polytope scope')
a=rep(a,'The present v66 edits have','These statements have','remove internal version prose')
a=rep(a,r'\paragraph{No admitted gaps.}',r'\paragraph{Checked Lean declarations and their limits.}','Lean fragment heading')
a=rep(a,'figs_p2/fig_p2_coverage_v67.png','figs_p2/fig_p2_coverage_v68.png','versioned figure path')
# Preserve source provenance in the new v68 draft, but do not silently redefine RViab.
a=rep(a, r'\(B_0 \in \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V}) \Rightarrow B_0 \subseteq \mathrm{RViab}(\mathcal{V})\).',
      r'\(B_0 \in \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V}) \Rightarrow B_0 \subseteq \mathrm{RViab}(\mathcal{V})\) only when observation-based nonanticipative strategies admit a full-information state-feedback realization with the same timing and disturbance quantifiers. Without that comparison theorem, the inclusion is into the full-history robust viability set, which need not have been identified with the state-feedback kernel.', 'hierarchy condition')
a=rep(a,r'&\;\subseteq\; \mathrm{RViab}(\mathcal{V}) \;\subseteq\; \mathrm{Viab}(\mathcal{V}),',
      r'&\;\subseteq\; \mathrm{RViab}^{\mathrm{hist}}(\mathcal{V}),', 'hierarchy display')
a=rep(a,'where \\(\\mathrm{IRViab}_{\\mathcal{J}}(\\mathcal{V})\\) is the institutionally restricted kernel of Section 6.4.',
      'where \\(\\mathrm{IRViab}_{\\mathcal{J}}(\\mathcal{V})\\) is the institutionally restricted kernel of Section 6.4 and \\(\\mathrm{RViab}^{\\mathrm{hist}}\\) permits nonanticipative full-information histories. The relation to the state-feedback \\(\\mathrm{RViab}\\) and nondisturbed \\(\\mathrm{Viab}\\) requires matching admissibility, solution and policy classes; no equality is inferred here.', 'hierarchy notation')
a=rep(a,'Consistency check: when the observation \\(O\\) is injective the record determines the state, so the epistemic and robust kernels agree, \\(\\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V}) = \\mathrm{RViab}(\\mathcal{V})\\),',
      'When the observation \\(O\\) is injective, the record determines the state, but equality with a state-feedback robust kernel requires an additional policy-class reduction; under such a reduction the corresponding kernels agree,','injective kernel scope')
# Gradients are necessary for contingent tangency, not sufficient without a constraint qualification.
a=block(a,r'(i) \emph{Local reading.}',r'(ii) \emph{Kernel reading.}',r'''(i) \emph{Local reading.} For the finite \(C^1\) representation \(\mathcal V=\{q_j\ge0\}\), every contingent tangent velocity satisfies the active-gradient inequalities. The reverse inclusion, and hence a sufficient Nagumo reading of \(\mathcal R_{\mathcal V}\), requires a representation regularity condition, for example the Mangasarian--Fromovitz constraint qualification at the relevant boundary points, together with the usual solution and measurable-selection assumptions. Without such a qualification the gradient inequalities are necessary but not sufficient for tangency: \(q(x)=x^3\), \(\mathcal V=[0,\infty)\), and velocity \(-1\) at \(x=0\) satisfy \(\nabla q(0)\cdot(-1)=0\) yet exit immediately. By contrast, a \emph{strictly negative} derivative at an active constraint along an admissible original-system path gives a local obstruction without a constraint qualification. These two directions must not be conflated.
''' ,'gradient/tangent correction')
# A closed-loop dynamics statement is a theorem under an original-path hypothesis, not an LSC shortcut.
a=block(a,r'(H2.3) \textbf{Closed-loop existence of the local adverse selection',r'Then, under hypotheses (H2.1)--(H2.3),',r'''(H2.3) \textbf{Original-system adverse trajectory (safety case).} For each \(a\in U^B(B)\) in the safety case there exist \(x_a\in B\cap\partial\mathcal V\), an active constraint \(j_a\), numbers \(c_a,\tau_a>0\), and an admissible original-system Carath\'eodory pair \((x_a(\cdot),d_a(\cdot))\) from \(x_a\) under the held action \(a\), compatible with the same pre-review observation record, such that \(d_a(t)\in D(x_a(t))\) almost everywhere and
\[q_{j_a}(x_a(t))\le -c_a t<0\qquad(0<t<\tau_a).\]
No lower semicontinuity inheritance for a thresholded disturbance correspondence, measurable feedback \(d(x)\), or convexified-to-original transfer is presumed. Existence and non-vacuity of compatible paths are part of the hypothesis.

''','main H2.3 explicit')
a=block(a,r'\emph{Proof sketch.} If the selected action is inadmissible at some compatible state',r'For polyhedral data the emptiness certificate',r'''\emph{Proof.} Fix a policy and its held first command \(a\). If \(a\notin U^B(B)\), it is inadmissible at a compatible state. Otherwise \(a\in U^B(B)\); emptiness of the common active-gradient response set implies some compatible boundary state has an active constraint with a strictly negative drift for this action. Hypothesis (H2.3) supplies an \emph{actual} compatible original-system path from such a state with \(q_{j_a}(x_a(t))<0\) at arbitrarily small positive times, hence before the next review. The policy therefore fails. This proof is conditional on (H2.3) and the declared held-action class, not a statement about an unrestricted switching policy.

''','main Thm2 proof')
a=block(a,r'the margin \(\mu_0\) is exactly the',r'Second, verified approximate data suffice:',r'''the scale-invariant ratio \(\mu_0/\|\mu\|_1\) is a guaranteed perturbation tolerance for this fixed multiplier. Scaling to \(\|\mu\|_1=1\) does not maximize it; optimizing over admissible multiplier directions is a separate problem. ''','normalized multiplier correction')
a=rep(a,'then feasibility of some\n\\(u \\in U\\) would imply',
      'then, provided \\(\\hat\\mu\\ge0\\) and the row-error bounds are valid, feasibility of some\n\\(u \\in U\\) would imply','approximate Farkas nonnegative')
a=block(a,r'\textbf{The tube-safety form.}',r'\begin{proposition}[uniform margin',r'''\textbf{The tube-safety form.} For a post-observation cell \(B\) and a policy required to hold one command over \([0,\Delta]\), let
\[\mathcal A_{\mathrm{tube}}(B,\Delta)=\{a\in U^B(B):\ \text{every compatible original-system held trajectory exists, remains action-admissible and stays in }\mathcal V\text{ on }[0,\Delta]\}.\]
The quantifier includes all compatible initial states, admissible disturbances and solutions. If a path cannot be continued for the required interval, the model must specify whether this counts as failure rather than treating an empty solution set as safe. Empty tube safety rules out a viable \emph{first action in the declared hold class}; no conclusion follows for unrestricted within-review switching. Instantaneous gradient tests imply this tube obstruction only under the original-system path premise (H2.3).

''','typed main tube')
a=rep(a,'Under the closed-loop existence convention of\nTheorem~\\ref{calc-thm:common-action}, the tube-safe action set is then empty',
      'Assume in addition that each such candidate action has an admissible original-system exiting path as in (H2.3), for its chosen boundary state. Then the tube-safe action set is empty', 'margin path premise')
a=block(a,r'\emph{Proof sketch.} For fixed \(a \in U^B(B)\), continuity of the drift',r'\begin{proposition}[obstruction ladder]',r'''\emph{Proof.} For each fixed \(a\), the assumed original-system exiting path has \(q_j(x_a(t))<0\) for every sufficiently small \(t>0\). Thus every positive \(\Delta\) contains an unsafe point, although the permissible exit interval may depend on \(a\). No uniform lower bound on those intervals is needed. The last implication concerns only policies that must hold the command over that review.

''','main Prop2 proof')
a=rep(a,'Under the standing regularity assumptions and the closed-loop existence\nconvention of Theorem~\\ref{calc-thm:common-action},',
      'For the declared positive-duration hold class, assuming (H2.3) at every relevant failed active-gradient test and original-system solutions through the review,','main ladder assumptions')
a=rep(a,r'\emph{Proof sketch.} The inclusion \(\mathcal{R}_{\mathcal{V}}(x) \subseteq U(x)\) gives the second nesting. For the first, an action outside \(\mathcal{R}_{\mathcal{V}}^B(B)\) violates \(\nabla q_j(x) \cdot f(x, a, d) \ge 0\) at some active boundary state, and the corresponding trajectory leaves \(\mathcal{V}\) in arbitrarily small time, so the action is not tube-safe.',
      r'\emph{Proof.} The second inclusion follows from \(\mathcal R_{\mathcal V}(x)\subseteq U(x)\). For the first, a command outside \(\mathcal R_{\mathcal V}^B(B)\) but inside \(U^B(B)\) fails an active-gradient test; (H2.3) supplies an admissible original-system path that exits before every positive review time. A command outside \(U^B(B)\) is already excluded by the tube definition. The final emptiness implication applies only to policies obliged to hold the first command for this same \(\Delta\); finite-step predecessor sets are not identified with continuous tubes without a sampled-transition model.', 'main ladder proof')
# Mechanical LP order; independent disturbance sets are a load-bearing condition.
a=rep(a,r'\(\max_{w \in W_{j}} F E_{j} A^{\ell} w\)',r'\(h_{W_j}(E_j^{\top}(A_j^{k-1-t})^{\top}F_r^{\top})\)', 'LP matrix order')
a=rep(a,'feasibility of the\nhorizon-\\(K\'\\) system is monotone',
      'this row assumes independent per-step disturbances \\(w_{j,t}\\in W_j\\) and floor row \\(F_r\\) for branch \\(j\\), step \\(k\\), and disturbance time \\(t\\). For coupled disturbance scenarios the joint support must be used instead. Feasibility of the\nhorizon-\\(K\'\\) system is monotone','LP quantified rows')
# v65/v66 theorem 3 now has through-boundary continuation; do not weaken it to contact alone.
a=rep(a,r'\(\sigma^*_{\Pi}(B_0)\le\inf_{x\in B_0}q(x)/\varepsilon\)',
      r'\(\sigma^*_{\Pi}(B_0)\le\inf_{x\in B_0}q(x)/\varepsilon\)', 'timing retained')
a=rep(a,'The realization continues through\nfirst contact by (H3.2),',
      'The realized minimizer path continues through first contact by (H3.2); contact alone would not imply nonviability for the closed safe set. The theorem need not detect a failure caused only by a non-minimizer branch.','timing minimizer scope')
# Helly is at most m+1 DISTINCT states; repeated padding of the old display was valid.
a=rep(a,'there\nexist '+r'\(x_1,\dots,x_{m+1}\in B\) with'+'\n'+r'\(\bigcap_{i=1}^{m+1}\mathcal R_{\mathcal V}(x_i)=\varnothing\).',
      r'there exist \(1\le\ell\le m+1\) distinct states \(x_1,\dots,x_\ell\in B\) with \(\bigcap_{i=1}^{\ell}\mathcal R_{\mathcal V}(x_i)=\varnothing\).', 'Helly at-most distinct')
# Honest theoretical recourse rather than asserting function-space minimization computable.
a=rep(a,'the infimum runs over admissible disturbance realizations (for affine dynamics each bracket is computable in closed form by variation of constants).',
      'the infimum runs over admissible exogenous disturbance scenarios. Variation of constants evaluates a bracket for a fixed scenario; it does not by itself compute the scenario infimum. An admissible scenario with a strictly negative bracket (an upper bound on the infimum) already supplies a failure witness, whereas a negative lower bound alone does not.', 'recourse computational scope')
# J3 exit certificate: distinguish control classes and original paths.
a=block(a,r'(H5.2) \textbf{Closed-loop existence of the adverse realization.',r'Then, under hypotheses (H5.1)--(H5.2),',r'''(H5.2) \textbf{Original-system adverse realization for the declared control class.} For every admissible control history in the stated class and every \(x_0\in\mathcal S_a\), there exists a compatible absolutely continuous original-system trajectory \(x(\cdot)\) and measurable disturbance \(d(\cdot)\), with \(d(t)\in D(x(t))\) and \(\dot x=f(x,u(t),d(t))\) almost everywhere. It is defined beyond \(q(x_0)/\varepsilon\) unless it has already reached \(q<0\), and while \(0\le q(x(t))\le a\) before exit it satisfies \(\frac{d}{dt}q(x(t))\le-\varepsilon\) almost everywhere. The trajectory continues through first contact long enough to decide strict exit. This is a substantive hypothesis about the \emph{original} game, not a consequence of ambient lower semicontinuity or closed graph of \(D\) alone. For an open-loop control one admissible path may depend on the selected control; disturbance-reactive or merely measurable closed-loop policies require their own compatible-solution premise.

''','main H5.2 original path')
a=block(a,r'Then, under hypotheses (H5.1)--(H5.2),',r'\begin{remark}[comparison-function form]',r'''Then, under (H5.1)--(H5.2), for every control in the \emph{declared} class and \(x_0\in\mathcal S_a\) an admissible original-system trajectory strictly violates \(q\ge0\) before every time strictly greater than \(q(x_0)/\varepsilon\). The infimum of strict-violation times is at most \(q(x_0)/\varepsilon\le a/\varepsilon\); a strict violation \emph{at} that bound is not asserted. Since \(\mathcal V\subseteq\{q\ge0\}\), the trajectory defeats viability in this class. At \(q=0\) a state may still be safe.
\end{theorem}

\emph{Proof.} Fix a control and the compatible pair of (H5.2). Let \(h(t)=q(x(t))\), \(t_0=h(0)/\varepsilon\). If the pair stays safe through a time \(t_1>t_0\) before its guaranteed continuation ends, it cannot first cross upward through \(h=a\), and on the still-safe portion \(0\le h\le a\) integration gives \(0\le h(t_1)\le h(0)-\varepsilon t_1<0\), a contradiction. Therefore it strictly exits before any such \(t_1\); a single strict violation so obtained precedes every later deadline. The argument never integrates the drift condition on a path after it has left its stated strip. Existence of the compatible original pair, not a closed-graph selection slogan or an unproved relaxation transfer, is the load-bearing premise.

''','main exit statement proof')
a=block(a,r'\begin{remark}[comparison-function form]',r'\subsubsection{3.6 Epistemic emptiness',r'''\begin{remark}[comparison-function form]\label{calc-rem:comparison}
If a state-dependent decline bound \(\dot q\le-\alpha(q)\), \(\alpha:(0,a]\to(0,\infty)\), holds along a compatible adverse original trajectory while \(q>0\), and \(\int_0^{q(x_0)}ds/\alpha(s)<\infty\), comparison bounds the time of \emph{first boundary contact}. It does not alone give strict exit from the closed set \(\{q\ge0\}\): the solution of \(\dot q=-\sqrt q\) from \(q(0)=1\) reaches zero at time two and can stay there. Strict exit requires a compatible continuation with negative drift at or through contact while the path remains safe. A value assigned to \(\alpha(0)\) without such a continuation is not a substitute for this hypothesis.
\end{remark}

The condition (4) has a control-before-disturbance, pointwise reading. A sound pathwise certificate still requires (H5.2) in the original system for the declared policy class. In particular, an open-loop adverse solution is not automatically a solution against a controller observing the current disturbance; a common admissible disturbance \(d^*\) with \(\sup_{u\in U(x)}\nabla q(x)\cdot f(x,u,d^*)\le-\varepsilon\) throughout the strip and compatible closed-loop solutions is one sufficient additional condition for such a disturbance-reactive class. A pointwise minimax interchange, even where justified, does not supply one state-uniform \(d^*\). The certificate is information-independent in its drift inequality, \emph{not} unconditional in solution existence or policy class. A state-dependent barrier may be used with output feedback; only an explicitly observation-only barrier subclass must be fibre-constant.

''','main comparison and policy scope')
# Original-source LP: check robust rows in main and supplement together.
a=rep(a,'Infeasibility at horizon \\(K\\) is certified by Farkas multipliers:',
      'When the per-step scenario choices are independent, infeasibility at horizon \\(K\\) is certified by Farkas multipliers:', 'LP independence statement')
# Condition both phases on the same blind control and correctly typed reveal.
a=block(a,r'\begin{proposition}[exact two-phase decomposition]',r'\begin{proposition}[no window-measurable pair is complete]',r'''\begin{proposition}[two-phase decomposition under a typed reveal]\label{calc-prop:decomposition}
Fix a declared blind-window policy class and an exact post-reveal information model. A post-observation cell \(B_0\) is viable for the two-phase game if and only if \emph{one and the same} blind control keeps every compatible branch in \(\mathcal V\) through step \(K\) and places every possible terminal information state in the kernel for the stated post-reveal policy class. Under full physical-state revelation this is the corresponding full-information \emph{state} kernel; if only a branch label is learned and within-branch uncertainty remains, it is the appropriate post-reveal \emph{belief} kernel. Neither case follows from a window-only failure test without these continuation hypotheses.
\end{proposition}

\emph{Proof.} Restrict a viable policy to its blind part and then to each possible revealed information state: the same blind part must be safe and every continuation must be viable. Conversely, join a blind witness to the appropriate viable continuation after each distinguishable terminal record, provided the declared strategy class permits this nonanticipative pasting and the posteriors use the same admissible disturbance histories. This equivalence is a two-phase policy decomposition, not a finite dual certificate for arbitrary continuous observations.

''','main two-phase revelation')
a=rep(a,'the three-state instance of Supplementary S3/A.3','the four-state (three safe-state) instance of Supplementary S3/A.3','main A3 state count')
a=rep(a,'Both computations are machine-verified in exact rational arithmetic',
      'The two finite transition tables can be checked by exhaustive recursion','main example verification scope')
# Separate typed finite recursion, continuous held response and static classification.
a=block(a,r'\paragraph{The selector.}',r'\paragraph{Monitoring adequacy',r'''\paragraph{Typed selectors.} For the finite-system recursion of Theorem~\ref{calc-thm:finite-horizon}, with \(B\subseteq\mathcal V\), write
\[\Gamma_N^{\mathrm{fin}}(B)=\{a\in U^B(B):\mathrm{Post}(B,a,y)\in\mathcal W_{N-1}\ \text{for every possible }y\}.\]
This is a discrete predecessor. The continuous one-review held response is \(\Gamma_\Delta^{\mathrm{hold}}(B)=\mathcal A_{\mathrm{tube}}(B,\Delta)\) with trajectory-wise safety and admissibility as defined above. An infinite-horizon held predecessor additionally asks that every exact post-review belief lie in a specified held-policy viability set. It is not Theorem 1's finite-system recursion until a sampled-transition embedding, information and disturbance rectangularity, and policy implementability are supplied.

\paragraph{Scope of witnesses.} An original-system boundary-exit path (under its path hypotheses), an admissible Farkas infeasibility witness, or a negative exogenous recourse scenario proves only the nonviability assertion in its declared model and policy class. A crossing observation fibre proves failure of an \emph{exact static certifier}, not policy nonviability. The biased-reading example tests one uncorrected policy, not all output-feedback policies. These mechanisms must not be combined into one untyped dual pair.

\paragraph{Exact and open cases.} The finite-state finite-horizon predecessor is exact under its stated observation/strategy semantics. A particular polytope LP has its own feasibility--Farkas alternative, not a global continuous epistemic-kernel duality. Static observation permits an open-loop policy reduction in Theorem~\ref{calc-thm:static-complete}; it does not by itself produce a finite obstruction witness for every nonviable belief. The grid of Remark~\ref{calc-rem:coverage} classifies its declared whole-window hold instance only. For a general continuous recursive class, the converse ``every nonviable belief has a witness from this finite checkable certificate family'' remains Open Problem~\ref{calc-op:dynamic}. An abstract transfinite predecessor identity is not a finite checkable certificate.

''','typed selector duality')
a=rep(a,'the three-state instance of Supplementary S3/A.3','the four-state instance of Supplementary S3/A.3','A3 residual count in main') if 'the three-state instance of Supplementary S3/A.3' in a else a
# The notation section must agree with the new typed held-action definition.
a=block(a,r'The tube-safe action set at review length',r'The first informative observation',r'''The tube-safe action set at review length \(\Delta\) is the set \(\mathcal A_{\mathrm{tube}}(B,\Delta)\) of commands \(a\in U^B(B)\) for which \emph{every} compatible admissible original-system held-action trajectory exists, remains in \(\mathcal V\), and obeys \(a\in U(x(t))\) throughout \([0,\Delta]\). The last condition matters when admissible controls depend on state; initial common admissibility does not imply trajectory-wise admissibility. Statements about its emptiness apply only to a policy class required to hold the first action for that \(\Delta\).
''','notation tube typing')
# The new theoretical status cannot be hidden by later unconditional language.
a=rep(a,'\nThe certificates of Section 3 are stated mechanism by mechanism. This section records',
      '\nThe certificates of Section 3 are stated mechanism by mechanism. This section records','no-op section anchor')
# Supplement front matter and concordance (environment counters are independent).
s=rep(s,'Notation and numbering follow the main text.',r'''Notation follows the main article, but theorem, proposition, remark, table and figure numbering is independent in this document. A selected concordance is: article Theorems 1/2/3/5 correspond to supplementary Theorems 1/2/3/4; article Theorem 4 has its indexed LP proof in S2; article Propositions 2/3 correspond to supplementary Propositions 1/2; article Proposition 6 has its recourse proof in S1; article Proposition 9 has its two-phase argument in S1. The main article\'s Section 3.8 aggregate LP has no matching supplementary theorem. After any repagination these location descriptions must be checked against both final PDFs.''','supp independent numbering and scoped crosswalk')
# Preserve existing model statements but eliminate the invalid selection implication.
s=block(s,r'(H2.3) \textbf{Closed-loop existence of the local adverse selection',r'Then, under hypotheses (H2.1)--(H2.3),',r'''(H2.3) \textbf{Compatible original-system adverse path.} In the safety case, for every candidate held \(a\in U^B(B)\) there exist a compatible boundary state \(x_a\), an active constraint \(j_a\), constants \(c_a,\tau_a>0\), and an admissible original-system Carath\'eodory pair under \(a\), with \(d_a(t)\in D(x_a(t))\) and \(q_{j_a}(x_a(t))\le-c_a t<0\) for \(0<t<\tau_a\) before any informative observation. This premise is about a realized path and does not follow merely from the closed graph or ambient lower semicontinuity of \(D\); a convexified-inclusion trajectory is not substituted for an original path.

''','supp H2.3 aligned')
s=block(s,r'\textbf{Safety case.} Otherwise \(a \in U^B(B)\).',r'\begin{proposition}[uniform margin',r'''\textbf{Safety case.} Otherwise \(a\in U^B(B)\). Since the active-gradient response equals \(U(x)\) at interior points, its empty common intersection implies that this particular command fails an active boundary inequality at a compatible state. Hypothesis (H2.3) provides a \emph{realized original-system} path from such a state whose corresponding active constraint becomes strictly negative at arbitrarily small positive times, before the next review. Thus this policy fails on one admissible compatible path. The policy was arbitrary within the required hold class; no claim is made for within-review switching or for relaxed-only paths. \ensuremath{\square}

''','supp Thm2 proof')
s=rep(s,'Under the closed-loop existence convention of\nTheorem~\\ref{thm:common-action}, the tube-safe action set is then empty',
      'Assume for each candidate command the original-system adverse path (H2.3) at the relevant state. Then the tube-safe action set is empty','supp uniform margin hypothesis')
s=block(s,r'\emph{Proof.} Fix \(a\in U^B(B)\) and the triple',r'\begin{proposition}[obstruction ladder]',r'''\emph{Proof.} Fix a candidate held command \(a\). By the assumed compatible original-system path, its active floor becomes negative on some interval \((0,\tau_a)\). Every \(\Delta>0\) contains a time in that interval, so \(a\notin\mathcal A_{\mathrm{tube}}(B,\Delta)\); no lower bound on \(\tau_a\) uniform in \(a\) is needed. Exhausting the common candidate set proves the assertion only for the class obliged to hold for that review. \ensuremath{\square}

''','supp uniform margin proof')
s=rep(s,'Under the standing regularity assumptions and the closed-loop existence\nconvention of Theorem~\\ref{thm:common-action},',
      'For the declared held-action review class, with original-system exiting paths (H2.3) whenever an active-gradient test fails,','supp ladder hypotheses')
s=block(s,r'\emph{Proof.} The second inclusion is by definition, since',r'\begin{theorem}[delayed-information obstruction]',r'''\emph{Proof.} The second inclusion follows from \(\mathcal R_{\mathcal V}(x)\subseteq U(x)\). For the first, if \(a\in U^B(B)\) fails an active-gradient inequality at a compatible boundary state, (H2.3) gives an admissible original-system path with \(q_j(x(t))<0\) arbitrarily soon; hence it cannot be tube-safe. A constant \(d\in D(x_0)\) need not remain admissible as \(x(t)\) moves when \(D\) depends on state. Emptiness of the held-command tube rules out a policy \emph{required} to hold that same command for this review; it does not rule out a time-varying input signal. The discrete \(\mathcal A_N\) is not included in the continuous tube without a defined sampled-transition bridge. \ensuremath{\square}

''','supp ladder proof admissible path')
# The delayed theorem already has a valid through-contact path. Qualify the recorded limit.
s=rep(s,'This includes \\(m=0\\): negative drift is required at the boundary,',
      'This includes \\(m=0\\): contact alone would not violate the closed constraint; negative drift while still safe is required at the boundary,','supp delayed contact')
# Replace supplement exit theorem and its spurious measurable-selection proof.
s=block(s,r'(H5.2) \textbf{Closed-loop existence of the adverse realization.',r'\begin{proposition}[epistemic emptiness by admissibility',r'''(H5.2) \textbf{Compatible original-system adverse pair.} For each admissible control history in the declared class and each initial state in \(\mathcal S_a\), assume an absolutely continuous original-system state and measurable disturbance exist, with \(d(t)\in D(x(t))\), \(\dot x=f(x,u(t),d(t))\) almost everywhere, and \(\dot q(x(t))\le-\varepsilon\) almost everywhere while \(0\le q(x(t))\le a\) before exit. This pair continues through first boundary contact until strict exit or beyond \(q(x_0)/\varepsilon\). Ambient lower semicontinuity and closed graph alone are not claimed to supply this path; a convexified path alone does not witness the original game.

Then the infimum of strict-violation times along such a path is at most \(q(x_0)/\varepsilon\). For every later deadline a strict violation occurs before that deadline, so the declared control class is nonviable from \(\mathcal S_a\); strict exit \emph{at} the bound is not asserted. Theorem 4 is independent of an observation argument but conditional on (H5.2) and its chosen policy class.
\end{theorem}

\emph{Proof.} Fix the control and original pair. If it stayed in \(q\ge0\) through any \(t_1>q(x_0)/\varepsilon\) before the assured continuation ends, it could not exit the strip upward through \(q=a\). Integrating only on the safe part of the closed strip gives \(0\le q(x(t_1))\le q(x_0)-\varepsilon t_1<0\), a contradiction. Thus a strict violation occurs before every later deadline. No use is made of a thresholded-correspondence LSC inheritance or an unproved closed-loop selection. \ensuremath{\square}

''','supp exit original path')
s=rep(s,'the infimum runs over admissible disturbance realizations',
      'the infimum runs over exogenous admissible scenarios; the bracket for a fixed scenario is given by variation of constants, whereas minimizing it over all scenarios is a separate problem. A single admissible scenario with a negative bracket is a sufficient computational witness. The infimum runs over admissible disturbance realizations','supp recourse scope') if 'the infimum runs over admissible disturbance realizations' in s else s
# Editorial and exact-reference coordination.
assert s.count('Proposition prop:helly')==2
s=s.replace('Proposition prop:helly','Proposition 4 of the main article');notes.append('both raw Helly labels')
s=rep(s,r'\(\mathcal{A}_N(B)\subseteq\mathcal{A}_{\mathrm{tube}}(B,\Delta)\subseteq\mathcal{R}_{\mathcal{V}}^B(B)\subseteq U^B(B)\)',
      r'\(\mathcal{A}_{\mathrm{tube}}(B,\Delta)\subseteq\mathcal{R}_{\mathcal{V}}^B(B)\subseteq U^B(B)\); the discrete \(\mathcal A_N\) is a separately typed predecessor','supp ladder discussion types')
s=rep(s,r'\(U^B(B)\supseteq\mathcal{R}_{\mathcal{V}}^B(B)\supseteq\mathcal{A}_{\mathrm{tube}}(B,\Delta)\supseteq\mathcal{A}_N(B)\)',
      r'\(U^B(B)\supseteq\mathcal{R}_{\mathcal{V}}^B(B)\supseteq\mathcal{A}_{\mathrm{tube}}(B,\Delta)\); the discrete \(\mathcal A_N\) needs a sampled model bridge','supp figure caption typing')
s=rep(s,'and the three-state computations below.','and the four-state computations below.','supp example computations')
s=rep(s,'A three-state system shows','A four-state system (three safe states) shows','supp A3 count')
s=rep(s,'\nwith equality only at \\(S_i = C_i/2\\), and the constraint set is the box \\([C_1/2, \\bar S_1] \\times [C_2/2, \\bar S_2]\\).',
      '\nwith equality only at \\(S_i = C_i/2\\), and the constraint set is the compact box \\([C_1/2, \\bar S_1] \\times [C_2/2, \\bar S_2]\\) with fixed finite \\(\\bar S_i>C_i/2\\). The admissible harvests in this construction are time-constant \\(h_i\\ge h_{\\min,i}\\).','supp A2 compact constant scope')
s=block(s,'But\n'+r'convergence to \(p^*\) is impossible:',r'Therefore no trajectory remains admissible',r'''But a singleton \(\omega\)-limit set of an autonomous smooth flow is invariant only if its point is an equilibrium. Since \(f(p^*)\ne0\), no nonempty invariant subset of \(\{p^*\}\) exists. For any time-constant harvest strictly exceeding the minimum in at least one coordinate, \(\dot W\le-\sum_i(h_i-h_{\min,i})<0\) gives the contradiction directly from the lower bound on \(W\). The argument for the minimum-harvest equality case is the compact invariant-set contradiction just proved. A separate proof is needed for any time-varying harvest class.
''','supp A2 invariant-set proof')
s=rep(s,'the three-state instance of Supplementary S3/A.3','the four-state instance of Supplementary S3/A.3','supp A3 reference') if 'the three-state instance of Supplementary S3/A.3' in s else s

# Reconcile the main §2.4 principle with the separation of static verdicts.
a=rep(a,'Each\nobstruction certificate of Sections 3 and 4 is a checkable sufficient\ncondition under which one of these response correspondences is empty:',
      'Each dynamic nonviability certificate of Section 3 is a sufficient condition under its declared policy and original-path hypotheses for failure of a response correspondence. Section 4 instead concerns static verdicts and a specified uncorrected feedback law. The dynamic correspondences include:','main selector static vs dynamic')
# A general finite dual witness is not supplied merely by static observation.
a=rep(a,'the belief-space restatement below, or prove a separation showing that none exists in a natural class.',
      'the belief-space restatement below, or prove a separation showing that none exists in a natural class. Abstract transfinite fixed-point recursions do not alone provide a finite, checkable family of original-system obstruction certificates.', 'main open problem effectivity')
# Directly exhibit the universally quantified robust LP row.
a=rep(a,'\n\emph{Proof sketch.} Unrolling the affine dynamics makes each branch state',
      '\n\emph{Proof sketch.} For branch \\(j\\), horizon step \\(k\\), floor row \\(r\\), and independent disturbances \\(w_{j,t}\\in W_j\\), the robust inequality is\n\\[\\sum_{t=0}^{k-1}F_r A_j^{k-1-t}B_j u_t\\le g_r-F_r A_j^k x_{j,0}-\\sum_{t=0}^{k-1}h_{W_j}\\!\\left(E_j^{\\top}(A_j^{k-1-t})^{\\top}F_r^{\\top}\\right).\\]\nUnrolling the affine dynamics makes each branch state', 'main LP displayed row')
# Supplement figure/concordance and original-source LP typo repaired consistently.
s=rep(s,'S1 collects the complete proofs of the main text\'s statements',
      'S1 collects selected proofs and worked certificates of the main text\'s statements','supp front proof placement')
s=rep(s,'\\section*{S1. Complete proofs}',r'\section*{S1. Certificates and detailed proofs}', 'supp S1 title scope')
s=rep(s,'\\section*{S2. The Sufficiency Landscape}',r'\section*{S2. Sufficiency landscape and further proof details}', 'supp S2 title scope') if r'\section*{S2. The Sufficiency Landscape}' in s else s
s=block(s,r'The robust floor row \(F_{i} x_{j,k} \le g_{i}\)',r'where \(h_{W_{j}}\) is the support function',r'''For every branch \(j\), step \(k\), and floor row \(r\), the robust inequality \(F_r x_{j,k}\le g_r\) for all \emph{independently selectable} disturbances \(w_{j,t}\in W_j\) is equivalent to
\[\sum_{t=0}^{k-1}F_r A_j^{k-1-t}B_j u_t
\le g_r-F_r A_j^k x_{j,0}-\sum_{t=0}^{k-1}h_{W_j}\!\left(E_j^{\top}(A_j^{k-1-t})^{\top}F_r^{\top}\right).\]
The row index \(r\) is not the disturbance-time index \(t\). With coupled disturbance paths, the sum of independent support values must be replaced by the support of the joint admissible path set.
''','supp LP floor/time corrected')
# Two-phase necessity and sufficiency require the exact reveal model and a single blind control.
s=block(s,r'\noindent\textbf{Complete proof of the exact two-phase decomposition',r'\rule{0.5\linewidth}{0.5pt}',r'''\noindent\textbf{Two-phase policy decomposition (main article, Section 7).} A viable policy restricts to one blind control that keeps \emph{every} compatible trajectory safe through the window. For each possible terminal observation, its continuation must be viable from that terminal information state. Under full physical-state revelation the terminal condition is membership of each terminal state in the matched full-information state kernel; under branch-only revelation with residual within-branch uncertainty, it is membership of each branch-conditional \emph{belief} in the post-reveal epistemic kernel. Conversely, if one blind command sequence satisfies both window safety and the relevant terminal condition, and the declared policy class admits nonanticipative pasting of the terminal strategies, concatenate those continuations to obtain a viable policy. This is not a claim that silence of an incomplete window certificate proves viability or that branch revelation automatically reveals the physical state.
''','supp two-phase typed proof')
# Copy of ambient prior domain and conditional continuous selector.
s=block(s,'Admissible initial\nbeliefs are the compact information sets',r'The existential (non-robust) counterpart',r'''The common ambient prior domain is \(\mathfrak B=\{B\subseteq X:B\ne\varnothing\}\), matching the main article. The initial observation splits a prior \(P\) into nonempty post-observation cells \(P\cap O^{-1}(y)\). A singleton prior remains singleton under a constant observation, and compactness is imposed separately in statements that need it. ''','supp ambient belief domain')
s=rep(s,'in continuous\ntime the converse is the backward-recursion completion noted in\nSection 6.5.',
      'in continuous time a converse for unrestricted policies is not established by the finite recursion, and remains open under the stated class and observation assumptions (main article, Section 7).','supp selector continuous converse')
s=block(s,r'\begin{remark}[comparison-function form]',r'\begin{example}[hidden-mode conflict]',r'''\begin{remark}[comparison-function form]\label{rem:comparison}
Suppose a compatible original-system adverse path satisfies \(\dot q\le-\alpha(q)\) while \(q>0\), with \(\alpha(s)>0\) on \((0,a]\). A finite comparison integral \(\int_0^{q(x_0)}ds/\alpha(s)\) bounds \emph{first contact}, not necessarily strict exit from the closed safe set. For example \(\dot q=-\sqrt q\), \(q(0)=1\), reaches zero at time two and may remain there. Strict exit additionally needs compatible continuation with adverse drift at or through boundary contact; a formal value \(\alpha(0)>0\) without such a path is insufficient.
\end{remark}

''','supp comparison contact')
# Barrier certificates may depend on physical state even with output-based feedback.
s=block(s,r'\emph{Barrier certificates.}',r'\emph{Estimation-tube reduction.}',r'''\emph{Barrier certificates.} A state-dependent barrier need not be constant on an observation fibre merely because the controller is output-based. What fails in this two-state instance is the existence of a \emph{common safe action} satisfying the incompatible floor inequalities at both states; a search restricted to observation-only barriers may be inconclusive about more general barrier methods. Any theorem transferring a particular barrier construction or estimation-space value to this model requires matching its primary-source hypotheses. No general nonexistence of a state-dependent barrier is inferred solely from a fibre-constancy argument.

''','supp barrier fibre scope')
s=block(s,r'\textbf{(c) Observer-and-buffer transfer.}',r'\textbf{(d) The linear substitution alternative.}',r'''\textbf{(c) Observer-and-buffer transfer.} A full-information feedback \(k(x)\) and an observer estimate \(\hat x\) alone do not prove invariance. If a specified compact set \(K_\zeta\) has been proved invariant under every \emph{admissible} input perturbation \(u=k(x)+v\) with \(\|v\|\le\rho\), then using \(k(\hat x)+\delta u\) inherits that guarantee whenever
\[L_k\|\hat x(t)-x(t)\|+\|\delta u(t)\|\le\rho\]
for all relevant times and the implemented command remains admissible. An exponentially decaying observer bound may imply this inequality from a sufficiently small initial error, but the robust-input radius \(\rho\), the admissibility condition and the invariant set must be established for the particular plant; no universal erosion coefficient or no-loss theorem is asserted here.

''','supp observer buffer conditional')
s=rep(s,'For the finite linear\nmodel in which a resource-typed system must meet a demand vector through specified substitution pathways, exactly one of the following holds',
      'Let \\(a\\in\\mathbb R^k_{\\ge0}\\) be pathways with constraints \\(Ra\\le x\\), \\(Ea\\le e\\), and \\(Qa\\ge s^{\\mathrm{req}}\\), where \\(R\\in\\mathbb R^{n\\times k}\\), \\(E\\in\\mathbb R^{m\\times k}\\), \\(Q\\in\\mathbb R^{p\\times k}\\), and \\(x,e,s^{\\mathrm{req}}\\) have matching dimensions. For this specified finite linear model, exactly one of the following holds', 'supp S2d model dimensions')
s=rep(s,'\nThe mechanism is a \\emph{failure of one policy to use the observation\nmap\'s structure}',
      '\nThe mechanism is a \\emph{failure of one policy to use the observation\nmap\'s structure}', 'no-op bias anchor')
s=rep(s,'\\(g\\) strictly\nincreasing on \\([S_{\\min}, S^* + b]\\)',
      '\\(g\\) continuous and strictly\nincreasing on \\([S_{\\min}, S^* + b]\\)', 'supp bias continuous')
s=block(s,'The phenomenon is the viability-theoretic analogue\nof Witsenhausen\'s counterexample',r'The remark is\npolicy-specific;' if False else 'The remark is\npolicy-specific;',
      'No analogy to signalling or nonclassical information is required for this known-bias example. ', 'supp bias remove Witsenhausen')

# Final whole-document consistency: no generic held-policy or compact-posterior shortcut.
a=block(a,r'\textbf{Conventions.} Throughout, the plant evolves in continuous time',r'An \textbf{observation structure}',r'''\textbf{Conventions.} The plant evolves in continuous time; sampling and hold are hypotheses only of those statements that explicitly declare a review and a held first command. A continuous record may be available between reviews, and a time-varying control is permitted when the declared policy class includes it. The observation record is generated by \(O\); error, hidden-parameter and delay variants need their own information model. A policy may use the full nonanticipative observation record. Representing it solely by the set-valued belief \(B_t\) is justified when the exact belief is a sufficient statistic and a measurable policy selector exists for the stated strategy class, not by the definition of a record alone. In a blind window, observation-equivalent branches share the same control, but this does not require that control to be constant unless a hold is declared. Disturbance information order is statement-specific: the common-action and delayed witnesses respond to a candidate policy; the oracle-recourse witness uses one exogenous scenario admissible against all policies. An action outside \(U(x)\) on a compatible state is failure; strict floor violation means \(q<0\).

''','main global convention timing')
a=rep(a,'We assume the standard set-membership semantics (Kurzhanski and V\\\'alyi, 1997), so that \\(B_t\\) contains every state\nconsistent with the observations and the applied controls.',
      'Under the stated set-membership semantics (Kurzhanski and V\\\'alyi, 1997), \\(B_t\\) contains every state consistent with the observations and applied controls. A one-step exact update equals reachable states intersected with the reading cell only if admissible original paths can be restricted and glued, disturbances are rectangular and memoryless across the step, and the surviving paths can be extended as required. Otherwise that formula is an outer approximation, not the exact posterior. Closed observation cells and compact reachable sets are separate prerequisites for compact posteriors; measurability of a viable belief-policy selector is another separate prerequisite.', 'main exact posterior conditions')
a=rep(a,'a policy is\n\\textbf{observation-based} if \\(u(t)\\) depends on the record only\nthrough \\(B_t\\); this is a special case of record-based policies, and\nthe two coincide when the belief is a sufficient statistic for the\ndecision problem, which holds in the delay-free set-membership semantics used\nthroughout.',
      'a policy is \\textbf{belief-based} if \\(u(t)\\) depends on the record only through \\(B_t\\). This is a special case of record-based policies; their equivalence requires exact sufficient-state semantics and measurable selection, and is not assumed merely because observations are delay-free.', 'main belief policy equivalence') if 'a policy is\n\\textbf{observation-based}' in a else a
# Lower down the prior-domain section reiterates a false unconditional equivalence.
a=rep(a,'The thesis is now precise:\n\\textbf{the epistemic kernel is the greatest recursively viable collection of information states in the sense of the estimation-space reduction cited in Section 5;',
      'Under exact rectangular belief dynamics and a strategy class admitting nonanticipative concatenation, the epistemic kernel is a recursively viable family of information states. Without those hypotheses, this is an organizational description rather than an exact greatest-fixed-point theorem. In every class,','main thesis fixed-point qualification')
a=rep(a,'the belief-space restatement below','a suitably defined belief-space restatement below','main open problem qualifier1')
a=block(a,r'The belief-space restatement is:',r'\end{openproblem}',r'''With exact original-system reachability, disturbance rectangularity, compatible extension/gluing and implementable measurable belief policies, a belief-space viability kernel gives the matching policy statement; a generic set-valued reachability recursion need not equal the original policy kernel. Compact reachability and closed observation cells must be supplied if that kernel is formulated on compact beliefs. These conditions are not asserted for every measurable observation map in this paper.
''','main open problem conditional belief')
a=rep(a,'Supplementary S1.\n\n\\begin{example}[decaying LP',
      'Supplementary S2.\n\n\\begin{example}[decaying LP', 'main LP proof correct supplement S2')
a=rep(a,'a comparison-function form\nsharpens the exit-time bound','a comparison-function form bounds first boundary contact under its path assumptions','main intro comparison scope')
a=rep(a,'the selector principle consolidates the certificates as dual witnesses of one correspondence, with the monitoring-adequacy converse and the design rules (Section 8)',
      'typed selector correspondences distinguish finite recursion, held continuous review and static verdicts, with conditional design rules (Section 8)', 'main conclusion typed selectors')
a=rep(a,'the certificates are complete in the one-step and static-observation classes, with the residual dynamic gap stated as an open problem (Section 7)',
      'finite one-step recursion is exact and static observation admits an open-loop policy reduction, without a general finite witness for nonviability; the dynamic finite-certificate gap remains open (Section 7)', 'main conclusion static scope')
a=rep(a,'A separate structural result concerns over polytope-declared\nblind-window classes',
      'A separate structural result concerns polytope-declared blind-window classes:','main conclusion grammar')
a=rep(a,'the timing certificate is exactly computable as a linear\nprogram, sound beyond the declaration with an unbounded implementable-class gap',
      'the specified affine timing-feasibility problem is exactly computable as a linear program, while its relaxation of a different implementable hold class can have an unbounded survival gap', 'main conclusion LP scope')
a=rep(a,'the partition form of the fibre criterion (Proposition~\\ref{calc-prop:fibre})',
      'a discrete common-action test distinct from the static-verdict fibre criterion of Proposition~\\ref{calc-prop:fibre}', 'main monitoring distinction')
a=rep(a,'\\textbf{Bias.} Remark~\\ref{calc-rem:ce-trap} shows that the loss need not be in the\nmeasurement: a biased indicator with an uncorrected\ncertainty-equivalence policy empties the epistemic kernel of a system\nwhose perfect-information kernel is nonempty.',
      '\\textbf{Bias.} Remark~\\ref{calc-rem:ce-trap} shows that a known biased indicator causes one uncorrected certainty-equivalence policy to fail on a system with a viable corrected policy; it does not empty the kernel of all output-feedback policies.', 'main bias kernel correction')
a=rep(a,'The certificates of Section 3 are stated mechanism by mechanism. This section records',
      'The certificates of Section 3 are stated mechanism by mechanism. This section records','no-op final anchor')
a=rep(a,'\\textbf{Aggregation.} Proposition~\\ref{calc-prop:fibre}',
      r'''\textbf{Sensor regularity.} The manuscript does not posit one universal numerical sensor \(h,\rho\). A proposed sensor regularity condition (R3) is model-specific: thresholded readings and tolerance-band readings can both fail closed-posterior/outer-limit or approximation obligations under their respective exact conventions. For any claimed regular-observation lemma, one must verify uniform joint approximation of reachable states, admissible actions, readings and exact posteriors, rather than infer posterior regularity from continuity of the raw sensor alone. These caveats do not themselves establish a failure for every sensor model.

\textbf{Aggregation.} Proposition~\ref{calc-prop:fibre}''','main R3 scope')
# Avoid a false first-exit equality in the threshold supplement.
s=rep(s,'\\(B_{0}\\) contains no fibre-induced\ninitial belief, while beliefs that are singletons (exact prior\nknowledge) are not admissible initial states of this observation\nstructure.',
      '\\(B_{0}\\) contains no full-fibre initial belief. A singleton prior under the same constant observation remains singleton and can be viable under state-specific control; the example therefore proves emptiness only on the explicitly full-fibre initial-belief domain, not the common ambient prior domain.', 'supp singleton prior correction') if '\\(B_{0}\\) contains no fibre-induced' in s else s
s=rep(s,'while beliefs that are singletons (exact prior\nknowledge) are not admissible initial states of this observation\nstructure.',
      'while a singleton prior under the same constant sensor can be viable and must not be excluded from the common ambient belief domain. The empty-kernel statement is restricted to full-fibre starting beliefs.', 'supp singleton prior scope') if 'while beliefs that are singletons (exact prior' in s else s
s=rep(s,'The main article\\\'s Section 3.8','The main article\'s Section 3.8','supp apostrophe literal')
s=rep(s,'article Proposition 9 has its two-phase argument in S1.',
      'article Proposition 9 has its two-phase argument in S2.', 'supp concordance proof location')
s=rep(s,'the complete proofs of the Section 3 certificates (S1),',
      'selected Section 3 certificate proofs (S1 and S2),','supp front proof types')
s=rep(s,'Therefore no trajectory remains admissible for all time: the kernel is\nempty, and since the box is compact and the vector field smooth, every\ntrajectory violates the constraint in finite time.',
      'Therefore, in the declared constant-harvest class, no trajectory remains in the compact box for all time: its restricted kernel is empty, and every such trajectory violates a constraint in finite time.', 'supp A2 restricted kernel')
s=rep(s,'The reduction returns the verdict exactly, but as a black box:',
      'Where the cited estimation-space reduction applies with matching policy and admissibility hypotheses, it returns the verdict; without those hypotheses the reduction is not a separate proof. In that setting, the value alone does not isolate the cause:','supp estimation literature conditional')
s=rep(s,'The hypothesis (2) is the set-membership form of the drift condition,\nquantified over open-loop controls on the blind window --- a condition\non the data of the problem, not on the policies:',
      'The hypothesis (2) is a pathwise condition for each control in the declared blind-window class, not an automatically checkable condition on a pointwise minimax expression:', 'supp delayed discussion path qualification') if 'The hypothesis (2) is the set-membership form' in s else s

a=rep(a,'A policy is\n\\textbf{observation-based} if \\(u(t)\\) depends on the record only\nthrough \\(B_t\\); this is a special case of record-based policies, and\nthe two coincide when the belief is a sufficient statistic for the\ndecision problem, which holds in the delay-free set-membership semantics used\nthroughout.',
      'A policy is \\textbf{observation-based} when it is a measurable nonanticipative function of the available record. A \\textbf{belief-based} policy factors through \\(B_t\\), and is a special case. Replacing arbitrary record policies by belief policies requires exact sufficient-statistic semantics and an implementable measurable selector; it is not guaranteed merely by delay-free measurement.', 'main record vs belief policy')
a=rep(a,'mechanism by mechanism, the information states outside it.}',
      'mechanism by mechanism, some information states outside it under their stated hypotheses.', 'main thesis stray brace')
a=rep(a,'The four correspondences of this section are one skeleton.',
      'The continuous response correspondences and separately typed discrete predecessor provide one organizing skeleton, not an unrestricted completeness theorem.', 'main skeleton typing')
s=rep(s,'After any repagination these location descriptions must be checked against both final PDFs.',
      'These article-to-supplement location descriptions should be checked against final paginated proofs. This is an unrefereed author draft; the continuous original-path premises and sensor-specific regularity are not certified by the finite formalization.', 'supp unrefereed disclosure')
s=rep(s,'There exists a system with\n\\(\\mathrm{Viab}(\\mathcal{V}; U, \\pi_{\\mathrm{perf}}) = \\mathcal{V} \\neq \\varnothing\\)\nsuch that, for a non-injective observation map \\(O\\), every admissible\ninitial information state --- the observation fibres',
      'There exists a system with\n\\(\\mathrm{Viab}(\\mathcal{V}; U, \\pi_{\\mathrm{perf}}) = \\mathcal{V} \\neq \\varnothing\\)\nsuch that, for a non-injective observation map \\(O\\), every \\emph{full-fibre} initial information state --- the observation fibres', 'supp prop1 prior domain')
a=rep(a,'such that, for a non-injective observation map \\(O\\), every admissible\ninitial information state --- the observation fibres',
      'such that, for a non-injective observation map \\(O\\), every \\emph{full-fibre} initial information state --- the observation fibres', 'main prop1 prior domain')
a=rep(a,'finite-time exit certificate is\ndynamic and defeats every control;',
      'finite-time exit certificate is dynamic and defeats every control \\emph{in its stated class under the original-system adverse-path premise};','main conclusion exit condition') if 'finite-time exit certificate is\ndynamic and defeats every control;' in a else a

a=rep(a,'Consider the \\emph{two-phase model}: a window of \\(K\\) blind\nsteps followed by exact branch revelation and branch-adapted continuation, with declared\nblind class \\(\\Pi_{B}\\) and full-information kernel \\(\\mathrm{RViab}(\\mathcal{V})\\)\navailable after the reveal.',
      'Consider a \\emph{two-phase model}: a window of \\(K\\) blind steps with declared blind class \\(\\Pi_B\\), followed by a specified reveal. Full physical-state revelation permits a matched full-information state kernel; revealing only a branch label may leave a nontrivial belief and requires the matching post-reveal belief kernel.', 'main two phase setup revelation scope')
a=rep(a,'Completeness fails only when information accrues, where the residual modes are post-observation recourse and timing --- the hidden-mode example and the timing bound of Section 3.3.',
      'A finite obstruction-witness theorem is not supplied for the general static continuous class; when information accrues, post-observation recourse and timing add distinct modes.', 'main static exactness scope')
s=rep(s,'\\item \\emph{Recursive obstruction} --- in the finite-horizon setting the\n\\(N\\)-step common safe-action sets \\(\\mathcal{A}_N(B)\\) of Section 3.1 complete the ladder\n',
      '\\item \\emph{Recursive obstruction} --- in the finite-system setting the \\(N\\)-step action predecessor of Section 3.1 is separate from the continuous-action ladder. The continuous inclusions are\n', 'supp A_N separate text')
# Avoid claiming a compiled PDF was checked: only the TeX source and pre-existing asset have been checked.
s=rep(s,'These article-to-supplement location descriptions should be checked against final paginated proofs.',
      'These article-to-supplement locations are source-level only and require checking against compiled paginated proofs.', 'supp no PDF source crosswalk')

a=rep(a,'fibre criterion addresses static certification rather than policy nonviability and analytic drift-and-timing conditions elsewhere.',
      'fibre criterion instead addresses static certification; analytic drift and timing tests have additional original-path premises.', 'abstract grammar and scope')
a=rep(a,'Two certification-theoretic completions are established:',
      'Two class-typed exact statements are established:', 'abstract completion scope')
a=rep(a,'Theorem~\\ref{calc-thm:exit}\'s adversarial-realization step presupposes both the closed-graph regularity of Section 2.1 and the closed-loop existence hypothesis (H5.2) --- \\(D\\) lower semicontinuous or constant, or the convexified reading; without these the certificate remains a heuristic.',
      'Theorem~\\ref{calc-thm:exit} is sound under its compatible original-system adverse-path hypothesis (H5.2). Neither a closed graph for \\(D\\) nor lower semicontinuity of ambient \\(D\\) alone proves that hypothesis; a convexified-inclusion trajectory is not an original-system witness. When the path premise is unverified, the theorem does not certify the model in question.', 'main remaining exit limitation')
a=rep(a,'The results are finite-dimensional and time-invariant; the continuous timing bound',
      'The base examples are finite-dimensional; the recourse certificate separately allows bounded measurable time-dependent coefficients for a fixed exogenous scenario. The continuous timing bound', 'main time varying scope')
a=rep(a,'it develops instruments that certify that no observation-based policy is viable --- that the infeasibility is due to the information structure, not to the dynamics.',
      'it develops conditional instruments for proving nonviability, separating information failures from dynamics-only exit and from static-verdict limits.', 'main introductory mechanism scope')
a=block(a,'The phenomenon is the viability-theoretic analogue\nof Witsenhausen\'s counterexample', 'The remark is\npolicy-specific;', 'No signalling or nonclassical-information analogy is needed for this known-bias policy example. ', 'main remove Witsenhausen analogy')

A1.write_text(a)
S1.write_text(s)
print('BUILT',A1.relative_to(R),S1.relative_to(R),'edits',len(notes))
print('\n'.join(notes))

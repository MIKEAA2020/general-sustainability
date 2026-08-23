# Independent External Review Response
## *Correcting the Mathematics and Prioritizing Development of a General Theory of Sustainability*

**Reviewed material:** the external review packet; the current master manuscript; Article 001 (`topdown.txt`); Article 002 (`general_theory.txt`); Article 011 V2 (`paper3_empirical.txt`); Article 012 (`paper2_dynamics.txt`); and Article 013 (`paper1_accounting.txt`).  
**Review date:** 16 August 2026

---

## Executive judgment

The programme contains a valuable and unusually disciplined distinction between (i) typed accounting and physical admissibility, (ii) trajectory safety and viability, (iii) information-limited implementation, (iv) recovery, and (v) architecture transformation. Its strongest publishable mathematical core is **Article 002**, provided its scope labels remain strict. The master manuscript is strongest as an architectural/perspective paper rather than as a claim to a completed general law.

The principal risk is not lack of ideas; it is conflation of several different quantifier structures:

\[
\exists\text{ trajectory},\qquad
\exists\pi\ \forall d,\qquad
\forall\text{ selections},\qquad
\exists\text{ state-contingent local prescription},\qquad
\Pr(\cdot)\ge 1-\epsilon.
\]

These are not interchangeable. Several Article 001 claims must be corrected or demoted because they move between them without enough assumptions. The corrective strategy should be **surgical rather than subtractive**: make Article 002 the canonical formal source; retain corrected Article 001 results as named restricted modules; preserve numerical and empirical material at its stated status; and do not promote Operator II or general composition beyond a restricted theorem target.

### Overall recommendation

1. **Freeze one formal vocabulary and audit every use of “robust,” “invariant,” “viable,” “institutional,” and “epistemic.”** This is the first priority.
2. **Use Article 002 as the canonical theorem corpus.** It already contains the most careful restricted construction of sampled, information-state, RFDE, hybrid, reduction, and accounting results.
3. **Correct Article 001 before citing it as a theorem source.** Several claims survive in restricted form; several institutional claims should become templates or conditional theorems.
4. **Publish the master as an architecture paper, not a theorem compendium.** It should point to technical sources and carry an explicit claim-status register.
5. **Develop one restricted Operator II theorem and one restricted composition theorem before claiming a general transformation/composition theory.**

---

## 1. Standing conventions used in this response

Let \(X\) be a state space, \(K\subseteq X\) a closed safe set, \(U(x)\) an action correspondence, \(D(x)\) a disturbance correspondence, and \(f(x,u,d)\) a vector field or declared transition law. A policy is denoted by \(\pi\), and a disturbance signal or nonanticipating disturbance strategy by \(d\) or \(\delta\).

The following distinctions are used throughout:

- **Controlled/existential viability:** \(\exists\pi\) (or \(\exists u(\cdot)\)) maintains safety when no adverse disturbance quantifier is present.
- **Robust/discriminating viability:** one policy works against every declared disturbance:
  \[
  \exists\pi\in\mathbb P\ \forall\delta\in\Delta:
  x^{\pi,\delta}(t)\in K.
  \]
- **Strong invariance:** every solution of a fixed closed-loop dynamics/inclusion remains in \(K\). This is stronger than existence of one viable solution of a set-valued inclusion.
- **Epistemic viability:** the state of the control problem is an information state/belief, not the unobserved physical state, unless an estimator theorem establishes otherwise.
- **Chance safety:** a probability law, filtration, and risk level are supplied. It is not a robust claim with probability notation added afterwards.

Every corrected theorem below should state which of these is being concluded.

---

## 2. Canonical notation and viability hierarchy

### 2.1 Recommended notation

Use one notation set across the master and technical sources.

| Object | Recommended notation | Avoid |
|---|---|---|
| Architecture | \(\mathfrak A_q\) | \(\mathcal A\) when \(\mathcal A\) also denotes assessment/action |
| State space | \(\mathsf X_q\) | \(X\) for both a stock and a state space |
| Physical safe set induced by a specification | \(\mathsf K_{q,\Omega}\) | \(K\) when \(K\) also denotes sink burden |
| Typed constraint registry | \(\mathscr C_\Omega\) | \(\mathcal V\) for both values and viability set |
| Observation map | \(\mathsf O_q\) | \(\mathcal O\) for a service readout |
| Assessment/filter | \(\mathsf A_q\) | \(A\) when \(A\) is an active material pool |
| Service readout | \(\mathsf S_{\rm svc}\) | \(\mathcal O\) |
| Constitutive/model class | \(\mathfrak M_q\) | \(\mathcal V\) |
| Carrying capacity | \(C_{\rm cap}\) or \(\bar x\) | \(K\) |
| Sink burden/load state | \(L\) or \(z_{\rm sink}\) | \(K\) |
| Information-state space | \(\mathsf B_q\) | the same symbol as \(\mathsf X_q\) |

For the master, keep \(\Omega\) for the frozen sustainability specification and \(\mathbf J_\Omega=(P,F,N,R,E)\) for the typed verdict. The fifth component should be called **epistemic/implementability status**, not a fifth geometric constraint set.

### 2.2 Canonical operators

For a fixed architecture and a fixed safe set \(\mathsf K\), write:

\[
\operatorname{CViab}^{T}(\mathsf K;\mathbb P)
=
\{x_0\in\mathsf K:\exists\pi\in\mathbb P,\ x^{\pi}(t)\in\mathsf K\ \forall t\in T\},
\]

\[
\operatorname{RViab}^{T}(\mathsf K;\mathbb P,\Delta)
=
\{x_0\in\mathsf K:\exists\pi\in\mathbb P\ \forall\delta\in\Delta,
 x^{\pi,\delta}(t)\in\mathsf K\ \forall t\in T\},
\]

\[
\operatorname{Safe}^{T}(\pi;\mathsf K,\Delta)
=
\{x_0\in\mathsf K:\forall\delta\in\Delta,
 x^{\pi,\delta}(t)\in\mathsf K\ \forall t\in T\}.
\]

For information states \(b\in\mathsf B_q\), use a separate object:

\[
\operatorname{EViab}^{T}(\mathsf K;\mathbb P^{\rm obs},\Delta)
\subseteq\mathsf B_q.
\]

For an institution \(\mathfrak I\), write the institution in the policy/action argument rather than introducing a new untyped kernel:

\[
\operatorname{RViab}^{T}(\mathsf K;\mathbb P^{\mathfrak I}_{\rm impl},\Delta).
\]

For chance safety, use a distinct operator such as

\[
\operatorname{ChViab}^{T,1-\epsilon}(\mathsf K;
\mathbb P,\mathbb P_{\!d}),
\]

where \(\mathbb P_{\!d}\) is an explicit law on disturbances, observation errors, and any model randomization. Do not put \(\delta\in\Delta\) inside a probability statement unless a probability law over \(\Delta\) is explicitly declared.

Capture/recovery should retain all of its indices:

\[
\operatorname{Capt}^{H}_{\mathbb P,\Delta}(C;E),
\]

where \(C\) is the target, \(E\) the authorized emergency envelope, and \(H\) the recovery horizon.

### 2.3 Which inclusions are literal?

The literal inclusion

\[
\operatorname{RViab}^{T}(\mathsf K;\mathbb P,\Delta)
\subseteq
\operatorname{CViab}^{T}(\mathsf K;\mathbb P)
\]

holds only after the no-disturbance controlled problem is aligned with the robust problem. Similarly, if \(\mathbb P_1\subseteq\mathbb P_2\) on the **same information state space**, then the corresponding robust kernels are ordered by inclusion.

By contrast, \(\operatorname{EViab}\) lives in a belief/information space. It is not literally a subset of a physical-state kernel until a common prior space, belief-to-physical projection, or information-refinement map has been declared. Chance and robust kernels also have no automatic inclusion without a relationship between the support/law of uncertainty and the robust disturbance class.

---

# 3. Live mathematical error docket

## Article 001

### A1 — Robust tangency versus strong invariance

**Primary verdict:** `FALSE_AS_STATED` — the diagnosis is correct.

**Corrected statement.** Let \(K\subset\mathbb R^n\) be closed. A sufficient full-state robust-invariance statement is:

\[
\exists k:K\to U\quad\text{such that}\quad
\forall x\in K\ \forall d\in D(x),
\quad f(x,k(x),d)\in T_K(x),
\]

and the **same** feedback \(k\) yields a well-posed closed-loop system for every admissible measurable disturbance signal. Under the regularity below, every such closed-loop trajectory remains in \(K\). Hence \(K\subseteq\operatorname{RViab}(K)\).

The quantifier order is essential:

\[
\exists k\ \forall d \quad\text{is required, not}\quad \forall d\ \exists k_d.
\]

For a differential game, formulate the result as a discriminating-kernel/robust controlled-invariance result with a nonanticipative controller policy and a declared controller–disturbance information pattern.

**Minimal assumptions.** A clean sufficient package is: \(K\) closed; \(D(x)\) nonempty compact; \(f\) continuous and locally Lipschitz in \(x\), uniformly on relevant \((u,d)\); a continuous or locally Lipschitz feedback \(k\) with \(k(x)\in U(x)\); and existence/uniqueness of the Carathéodory solution for every admissible \(d(\cdot)\). A more general differential-inclusion formulation is possible, but then one must cite a **strong-invariance** theorem and verify its hypotheses, rather than a weak viability theorem.

**Proof sketch.** Fix any admissible \(d(\cdot)\). The closed-loop vector field \(x\mapsto f(x,k(x),d(t))\) satisfies the tangent condition on \(K\) at every time. A strong Nagumo/forward-invariance theorem then keeps its unique solution in \(K\). Since the argument used no property special to the selected disturbance signal, it holds for every \(d(\cdot)\), with the same \(k\).

**Counterexamples when weakened.**

1. If one has only \(F(x)\cap T_K(x)\neq\varnothing\), then one has weak viability, not strong invariance. Take \(K=[0,\infty)\) and \(F(0)=\{-1,+1\}\). The direction \(+1\) is viable, while the solution using \(-1\) exits immediately.
2. If the quantifiers are reversed, let \(K=[0,\infty)\), \(U=D=\{-1,+1\}\), and \(\dot x=ud\). At \(x=0\), for every \(d\) there is a safe choice \(u=d\), but no one action is safe for both disturbances.

**Recommended source status:** Conditional theorem after correction; retain the definition of robust viability. Do not use the current proof to establish a robust/discriminating kernel.

**Downstream consequences.** This correction applies to Article 001 Theorems 4.5, 5.1, 13.2, and 16.1 wherever a weak viability theorem is used to claim one policy protects against every disturbance. It also affects the master’s use of “robust viability” as an Operator I foundation.

**Literature.** Aubin, *Viability Theory*; Aubin, Bayen & Saint-Pierre, *Viability Theory: New Directions*; Blanchini, “Set invariance in control,” *Automatica* 35 (1999), 1747–1767, DOI: [10.1016/S0005-1098(99)00113-2](https://doi.org/10.1016/S0005-1098(99)00113-2).

**Confidence:** High. The exact weakest hypotheses depend on the desired solution concept.

---

### A2 — Order-minimal control

**Primary verdict:** `FALSE_AS_STATED` — the diagnosis is correct.

**Corrected statement.** For the resource–sink order

\[
(S_1,L_1)\succeq(S_2,L_2)
\iff S_1\ge S_2,\ L_1\le L_2,
\]

suppose a fixed admissible minimum harvest \(h_{\min}\) exists and comparison establishes

\[
(S^{h_{\min}}(t),L^{h_{\min}}(t))
\succeq (S^{H}(t),L^{H}(t))
\]

for every admissible harvest path \(H(t)\ge h_{\min}\) with the same initial state. If \(K\) is upward closed in this order, then

\[
\operatorname{CViab}(K)\ne\varnothing
\iff
(S^{h_{\min}}(t),L^{h_{\min}}(t))\in K\ \forall t\ge0.
\]

This is an **existential** result. It does **not** say every higher-harvest path is safe.

**Minimal assumptions.** The minimum control must be admissible along its proposed trajectory; the order comparison must be proved for the actual dynamics; and \(K\) must be order-upward. For a state-dependent pointwise minimum \(\underline H(S)\), a separate feedback-comparison proof is required; the fixed-floor formulation is the clean canonical theorem.

**Proof sketch.** If any admissible policy is safe, the order-better minimum-harvest trajectory is safe by upward closure. Conversely, if the minimum-harvest path is safe, it itself is an admissible witness.

**Counterexample.** With \(\dot S=1-H\), \(S\ge0\), \(H\in[0,2]\), and \(S(0)=1\), the minimum control \(H=0\) is safe, whereas \(H=2\) exits at time \(1\).

**Recommended source status:** Theorem after wording correction.

**Downstream consequences.** The scalar kernel results can remain, but every statement that says the minimum path makes *all* policies safe must be replaced by the existential equivalence.

**Literature:** Monotone systems/comparison arguments: Hirsch & Smith, *Monotone Dynamical Systems* (2005).

**Confidence:** High.

---

### A3 — Pollution-feedback comparison sign

**Primary verdict:** `FALSE_AS_STATED` — the conclusion can survive, but the displayed comparison sign in the proof is reversed.

**Corrected statement.** If \(g_K(S,K)\le0\) and \(0\le K\le K_{\max}\), then

\[
g(S,K)\ge g(S,K_{\max}).
\]

Thus the \(K_{\max}\)-frozen stock equation is the lower-growth comparison system. If the frozen lower bound \(S\ge S_\circ(K_{\max})\) is invariant under \(\dot S=g(S,K_{\max})-h_{\min}\), and \(K\le K_{\max}\) is invariant under the sink dynamics, then the corresponding rectangle is an inner robust/controlled-invariant bound for the actual minimum-harvest system.

**Minimal assumptions.** In addition to \(g_K\le0\), require regularity for comparison, the sink-face condition \(w(h_{\min})-\delta(K_{\max})\le0\), admissibility of \(h_{\min}\), and the frozen lower-face condition

\[
g(S_\circ(K_{\max}),K_{\max})-h_{\min}\ge0.
\]

**Proof sketch.** At the lower stock face, the actual drift is at least the frozen drift; at the upper sink face, the sink drift is nonpositive. The rectangle is therefore invariant by the appropriate tangent/comparison argument.

**Counterexample.** For \(g(S,K)=S/(1+K)\), \(K=0<K_{\max}=1\), one has \(g(S,0)>g(S,1)\), directly contradicting the source’s reversed sentence.

**Recommended source status:** Conditional theorem after proof correction.

**Downstream consequences.** The inner-bound conclusion is salvageable; the source must not claim that the actual slice lies below the \(K_{\max}\)-frozen slice. The claimed exact curved frontier remains a separate issue.

**Confidence:** High.

---

### A4 — Capital-consumption kernel

**Primary verdict:** `FALSE_AS_STATED` — the existential kernel claim is repairable; the claim about arbitrary higher consumption is false.

**Corrected statement.** Consider

\[
\dot A=\Phi(A)-c,\qquad c\in\mathcal U_c(A),\qquad c_{\min}\in\mathcal U_c(A).
\]

Let \(\Phi\) be continuous, concave, and locally Lipschitz, and suppose the superlevel set

\[
G=\{A\ge0:\Phi(A)\ge c_{\min}\}
\]

is nonempty and closed. If \(a=\min G\), then, under the constant witness \(c\equiv c_{\min}\), \([a,\infty)\) is viable. Under the stated one-dimensional signature, it is the controlled viability kernel; no statement about all \(c\ge c_{\min}\) follows.

**Minimal assumptions.** Include attainment/nonemptiness of \(G\), local well-posedness, and admissibility of \(c_{\min}\). If \(\sup\Phi=c_{\min}\) is not attained, the kernel can be empty despite equality of the supremum.

**Proof sketch.** Concavity makes \(G\) an interval. At its lower endpoint the minimum-consumption drift is nonnegative; above the upper endpoint, if one exists, the drift is negative and trajectories approach that endpoint without crossing the lower endpoint. States below \(a\) have negative drift under every admissible \(c\ge c_{\min}\).

**Counterexample.** Let \(\Phi(A)=1\), \(c_{\min}=1\), and start at \(A=1\). The witness \(c=1\) preserves \(A\), but choosing \(c=2\) gives \(\dot A=-1\) and exits the safe half-line. Thus higher consumption does not preserve the kernel.

**Recommended source status:** Conditional theorem after correction.

**Downstream consequences.** Article 001 Theorem 7.1 remains valid only because it explicitly uses \(c\equiv c_{\min}\). Remove the erroneous universal-control sentence.

**Confidence:** High.

---

### A5 — Generic non-polyhedrality

**Primary verdict:** `PROOF_INCOMPLETE` — the current algebraic-hypersurface argument does not establish the advertised open-dense theorem.

**Corrected statement.** A safe, useful replacement is:

> For a specified parameter vector, if a regular viability-frontier segment is a \(C^2\) graph \(S_2=\Gamma(S_1)\) and \(\Gamma''(s_0)\ne0\) at one point, then that frontier segment is not polyhedral.

A generic open-dense result requires a defined parameter manifold, regular dependence of the frontier on parameters, exclusion of tangency degeneracies, and a transversality or elimination proof showing that flat barrier segments form a proper nowhere-dense exceptional set.

**Minimal assumptions.** The frontier must exist as a regular graph; the denominator in the orbital slope equation must not vanish; and the parameter family must be specified before “generic” has meaning.

**Proof sketch.** A polyhedral graph is affine on each relative-interior face. Nonzero curvature at one regular point rules out affinity in a neighbourhood. To prove genericity, differentiate the orbital ODE and apply an explicit parametric-transversality or algebraic-elimination argument; merely observing polynomial identities with unknown slope/intercept does not prove that their projection is a finite union of proper hypersurfaces.

**Counterexample if assumptions are removed.** At zero coupling, the product kernel can have axis-aligned/polyhedral boundary. If the whole constraint orthant is invariant (corner Nagumo holds), the viable set is itself polyhedral. These cases show why nondegeneracy and a proper-barrier hypothesis are necessary.

**Recommended source status:** Demote the open-dense statement to conjecture or replace it with the pointwise conditional proposition above.

**Downstream consequences.** Preserve the numerical orbital examples and the destruction/rescue examples. Do not use “generic non-polyhedrality” as a canonical theorem until repaired.

**Literature:** Standard transversality methods, e.g. Hirsch, *Differential Topology*; viability-barrier theory in Aubin’s viability texts.

**Confidence:** High that the present proof is incomplete; medium on the truth of the intended generic claim.

---

### A6 — Rosen uniqueness

**Primary verdict:** `PROOF_INCOMPLETE` — the Rosen calculation is invalid for heterogeneous \(d_i\), although a uniqueness result can be proved directly for the displayed aggregative game.

**Corrected statement, Rosen route.** Rosen’s diagonal strict concavity requires the symmetric part of the weighted pseudo-gradient Jacobian to be negative definite:

\[
\frac12\left(Dg_r(h)+Dg_r(h)^\top\right)\prec0,
\qquad
[g_r(h)]_i=r_i\,\partial_{h_i}U_i(h),\quad r_i>0.
\]

For heterogeneous \(d_i\), this condition must be checked as a matrix condition; it does not follow merely from \(\pi_i''<0\) and \(d_i''\ge0\).

**Corrected statement, direct route.** For compact intervals \([0,\bar h_i]\), \(C^1\) strictly concave \(\pi_i\), and nondecreasing convex \(d_i\), the game

\[
U_i(h)=\pi_i(h_i)-d_i\!\left(\sum_jh_j\right)
\]

has a unique Nash equilibrium. This is an aggregative-game theorem and should not be attributed to Rosen unless the DSC matrix condition is separately verified.

**Proof sketch for direct uniqueness.** For a proposed aggregate \(H\), define \(r_i(H)\) by the one-dimensional first-order/boundary condition

\[
\pi_i'(r_i(H))=d_i'(H)
\]

with the natural projection to \([0,\bar h_i]\). Since \(\pi_i'\) is strictly decreasing and \(d_i'\) is nondecreasing, \(r_i(H)\) is nonincreasing. An equilibrium aggregate solves

\[
H=\sum_i r_i(H).
\]

The left side is strictly increasing and the right side is nonincreasing, so there is at most one solution; compactness and continuity give existence.

**Counterexample to the source’s Rosen verification.** With two agents, equal Rosen weights, \(\pi_i''=-1\), \(d_1''=100\), and \(d_2''=0\), the symmetric pseudo-gradient part is

\[
\begin{pmatrix}-101&-50\\-50&-1\end{pmatrix},
\]

whose determinant is negative. It is not negative definite. Thus the claimed Rosen sufficient condition has not been verified, even though direct uniqueness may still hold.

**Recommended source status:** Theorem after a complete direct aggregative-game proof; reserve Rosen for the exact DSC condition.

**Downstream consequences.** This repairs the commons-game foundation without overclaiming a general game-theoretic theorem.

**Literature:** Rosen, “Existence and uniqueness of equilibrium points for concave N-person games,” *Econometrica* 33 (1965), 520–534.

**Confidence:** High.

---

### A7 — Commons obstruction

**Primary verdict:** `TYPE_OR_DOMAIN_ERROR` — \(H_{\rm safe}\) is underdefined, and the global-empty-kernel conclusion needs a reachability or uniform-drift condition.

**Corrected statement.** For an autonomous Nash-induced stock law

\[
\dot S=g(S)-H^{\rm NE}(S),
\]

let \(K_S=[S_{\min},S_{\max}]\). If there is \(\varepsilon>0\) such that

\[
H^{\rm NE}(S)-g(S)\ge\varepsilon
\qquad\forall S\in K_S,
\]

then every trajectory exits below \(S_{\min}\) in finite time and the Nash-play safe kernel is empty. A weaker strip version needs both

\[
H^{\rm NE}(S)-g(S)\ge\varepsilon
\qquad\text{on }[S_{\min},S_{\min}+a]
\]

and a separately proved statement that every admissible trajectory reaches that strip.

Define a “safe harvest” only after specifying its role—for example, \(H_{\rm nd}(S)=g(S)\) for instantaneous stock nondecline, or a control-dependent viability boundary. Do not use one undefined \(H_{\rm safe}\) for both.

**Proof sketch.** The uniform drift gives \(\dot S\le-\varepsilon\), hence exit by at most \((S(0)-S_{\min})/\varepsilon\). The strip conclusion uses the finite-time obstruction only after strip entry is established.

**Counterexample.** With \(S_{\min}=0\) and \(\dot S=-S^2\), the drift is negative for every \(S>0\), but trajectories approach zero asymptotically and do not exit \([0,\infty)\) in finite time. A sign statement alone is insufficient.

**Recommended source status:** Conditional theorem after replacement.

**Downstream consequences.** The tragedy-of-commons narrative is preserved, but its safety claim becomes an explicit drift certificate rather than a label.

**Confidence:** High.

---

### A8 — Quota rescue

**Primary verdict:** `FALSE_AS_STATED` — the diagnosis is correct.

**Corrected statement.** If the underlying ecological model imposes \(H\ge H_{\min}\), then a quota profile must produce

\[
H_Q=\sum_i q_i\in[H_{\min},H_{\rm eco}],
\]

where \(H_{\rm eco}\) is a declared safe upper bound satisfying stock, sink, and harvest-capacity conditions. The simplest corollary sets \(H_Q=H_{\min}\). If enforcement establishes realized harvest \(H=H_Q\), the ecological viability theorem must be applied at \(H_Q\), not automatically at \(H_{\min}\).

**Minimal assumptions.** Specify the exact quota implementation mechanism, a safe constant-harvest interval, feasibility of quota allocation, and the sanction/behaviour conditions needed to make the prescribed total realized.

**Proof sketch.** Under implementation, the aggregate harvest is a fixed feasible \(H_Q\). Apply the corrected scalar viability result at that harvest level.

**Counterexample.** If \(H_Q<H_{\min}\), the quota action violates the model’s own lower-harvest/output constraint and is not an admissible witness.

**Recommended source status:** Conditional corollary after correction.

**Downstream consequences.** Article 001 must not equate a quota cap with a lower harvest floor. This repair links directly to A9.

**Confidence:** High.

---

### A9 — Sanction sufficiency

**Primary verdict:** `FALSE_AS_STATED` — the stated argument blocks upward deviations but does not establish that quota is the unique best response.

**Corrected statement.** Let \(Q=\sum_jq_j\). To make \(q_i\) the unique best response to \(q_{-i}\), sufficient local conditions are:

\[
\pi_i'(q_i)-d_i'(Q)>0
\]

(to make payoff strictly increase up to quota) and

\[
C_i'(h)-\bigl[\pi_i'(h)-d_i'(h+Q-q_i)\bigr]>0
\qquad\forall h>q_i
\]

(to make payoff strictly decrease above quota). A simple stronger upper-deviation condition is \(C_i'(h)\ge\gamma>\pi_i'(q_i)\), together with the first displayed lower-side condition.

For a dominant-strategy claim rather than a Nash claim, the lower-side inequality must hold uniformly over every admissible opponents’ aggregate harvest.

**Proof sketch.** Concavity of \(\pi_i\) and convexity of \(d_i\) make the unsanctioned marginal payoff weakly decrease in own harvest. The two sign conditions make it positive below quota and negative above quota, giving a unique maximizer at quota.

**Counterexample.** Let \(\pi(h)=2h-h^2/2\), \(q=1\), and \(d(H)=2H\). Even with a sanction slope \(\gamma>\pi'(q)=1\) above quota, the marginal payoff just below quota is \(\pi'(1)-2=-1\). The best response lies below quota, not at it.

**Recommended source status:** Conditional theorem after correction.

**Downstream consequences.** Quota rescue can remain, but only after the behavioural implementation theorem is repaired and linked to the ecological safe interval.

**Confidence:** High.

---

### A10 — Ostrom sufficiency and necessity

**Primary verdict:** `FALSE_AS_STATED` — the current eight-principle theorem is not a valid general sufficiency or necessity theorem.

**Corrected statement.** The eight principles should be treated as **mechanism-to-model maps**, not as jointly sufficient mathematical conditions by their labels. A sound restricted theorem is:

> If a specified institution induces an information process and an implementable prescription class such that, at every reachable information state, there exists a policy prescription whose every allowed realization satisfies the robust tangent/tube condition for a closed set \(Q\), and if allocation, enforcement, and external-interface conditions are simultaneously satisfied, then \(Q\) is robustly viable.

Ostrom mechanisms may provide empirical or institutional evidence for the theorem’s hypotheses—better information, enforceable prescriptions, viable allocation, and safe interfaces—but do not substitute for them.

The correct non-necessity statement is existential and model-class relative:

> For each selected formal mechanism \(P_k\), one can construct a model in which the other selected mechanisms hold, \(P_k\) fails, and the kernel is empty.

This establishes non-redundancy of the **formalized mechanism in that class**, not universal necessity of an Ostrom principle.

**Minimal assumptions.** Use the corrected A1 robust-invariance conditions; specify the belief/update process; define enforcement as a realized-action correspondence; require a common feasible allocation; and state external/nested-system interfaces as contracts.

**Counterexample.** Bounded monitoring error alone does not ensure safe output feedback when there is no inward safety margin. Likewise, collective choice does not imply that agents can choose \(H=H_{\min}\) if the selected social optimum is higher or the lower output constraint is binding.

**Recommended source status:** Replace the current theorem with a conditional institutional-implementation theorem; retain the principle table as a template/research programme.

**Downstream consequences.** The master should describe Ostrom as a typed implementation map, not as a universal theorem. Article 001 Theorem 13.2 also needs the A1 strong-invariance repair.

**Literature:** Ostrom (1990); robust institutional/controlled-invariance theory after the A1 correction.

**Confidence:** High.

---

### A11 — Implementation lattice

**Primary verdict:** `FALSE_AS_STATED` — existential viability is not downward closed under arbitrary contraction of the action correspondence.

**Corrected statement.** With dynamics, safe set, and policy-information structure fixed,

\[
\mathcal U_{\exists}
=\{U':\operatorname{CViab}(K;U')\ne\varnothing\}
\]

is **upward closed** under pointwise action-set inclusion: if \(U_1\subseteq U_2\) and \(U_1\) has a viable policy, the same policy remains available under \(U_2\).

By contrast, a family defined by universal action safety,

\[
\mathcal U_{\forall}
=\{U':\exists C\ne\varnothing\text{ strongly invariant under every admissible }U'\text{-selection}\},
\]

is downward closed, subject to nonempty selectable actions and well-posedness. Neither family should be called a lattice unless closure under the relevant meet/join operations is actually shown.

**Proof/counterexample.** Let \(K=[0,\infty)\), \(\dot x=-u\), and \(U_1(x)=\{0,1\}\). The policy \(u=0\) makes \(K\) viable. The contracted correspondence \(U_0(x)=\{1\}\) forces exit from \(x=0\). Thus viability is not downward closed.

**Recommended source status:** Replace Proposition 13.1 with two oppositely ordered families and explicit policy semantics.

**Downstream consequences.** This is important for the slogan “governance restricts.” A restriction can remove unsafe actions under a universal/compliance interpretation, but it cannot automatically enlarge an existential viability kernel merely because it is a restriction.

**Confidence:** High.

---

## Article 002

### B1 — Canonical notation and operator hierarchy

**Primary verdict:** `NOT_AN_ERROR_BUT_NEEDS_CLARIFICATION`.

**Corrected action.** Adopt Section 2 of this report as the official notation table. In particular, reserve \(\mathsf K\) for safe sets, \(L\) for sink loads, \(C_{\rm cap}\) for carrying capacity, \(\mathfrak A\) for architectures, \(\mathsf O\) for observation, \(\mathsf A\) for assessment, and \(\mathsf S_{\rm svc}\) for service readout.

**Minimal assumptions/proof.** None; this is a type discipline. A notation table should precede every technical paper and appear in the master’s appendix.

**Counterexample.** Confusing a physical sink stock \(K\) with a safe set \(K\), or a service readout with an observation operator, makes set inclusions and domains ill-typed before any theorem is reached.

**Recommended source status:** Definition/style correction.

**Downstream consequences:** High editorial value; no loss of content.

**Confidence:** High.

---

### B2 — Selector regularity

**Primary verdict:** `NOT_AN_ERROR_BUT_NEEDS_CLARIFICATION`.

Article 002 correctly says when it permits arbitrary pointwise selectors. Such statements are mathematically useful, but they should be labelled **choice-theoretic** unless measurable or continuous policy implementation is proved.

**Corrected statement.** In a compact metric sampled model, define the safe-action correspondence

\[
\Gamma_A(x)=\{u\in U: F(x,u,w)\in A\ \forall w\in W\}.
\]

If the information/state domain is standard Borel, \(U\) is Polish, and \(\Gamma_A\) has nonempty closed values and measurable graph, then a Borel selector exists by Kuratowski–Ryll-Nardzewski. For continuous feedback, add lower semicontinuity and nonempty closed convex values in an appropriate Banach-valued action space, permitting a Michael-selection argument. For continuous-time feedback, selector measurability alone does not guarantee well-posed closed-loop trajectories; add the needed Carathéodory/Lipschitz or differential-inclusion solution assumptions.

For finite-clopen information kernels, the same argument applies to the compact hyperspace/information-state domain once the exact update map is Borel/continuous. A policy over \((\Omega,y)\) should be explicitly Borel in that pair if it is to be called implementable.

**Counterexample.** The axiom of choice yields a pointwise selector from arbitrary nonempty sets but does not make it measurable, continuous, causal in an implementable information filtration, or capable of generating a unique solution.

**Recommended source status:** Keep existing theorems as conditional theorems with an “arbitrary selector” label; add a measurable-selection corollary only where its hypotheses are checked.

**Literature:** Kuratowski & Ryll-Nardzewski, “A general theorem on selectors,” *Bull. Acad. Polon. Sci.* 13 (1965), 397–403; Michael, “Continuous selections I,” *Annals of Mathematics* 63 (1956), 361–382, DOI: [10.2307/1969615](https://doi.org/10.2307/1969615).

**Confidence:** High.

---

### B3 — Exact information and hybrid-tube assumptions

**Primary verdict:** `NOT_AN_ERROR_BUT_NEEDS_CLARIFICATION`.

**Corrected statement.** Every result should separate three layers:

1. **Abstract theorem assumptions:** compact information state, exact filter, compact exact reachable tubes, Hausdorff continuity, and admissible selectors.
2. **Application construction:** a proof that a particular observation/dynamics model produces those objects.
3. **Numerical approximation:** an error-certified approximation of the constructed objects.

A finite-clopen conditioning theorem proves one concrete exact-filter class. It does not establish that noisy continuous observations, real institutional records, or variable-time delayed hybrids satisfy the same assumptions. Likewise, a bounded-jump hybrid theorem with Hausdorff-continuous exact tubes cannot be applied merely because a hybrid model has outer semicontinuous solution sets.

**Counterexample.** Article 002’s grazing-event counterexample already shows that outer semicontinuity alone does not close a universal tube-containment predecessor.

**Recommended source status:** Retain as conditional theorems; add an application-admission checklist and a separate “constructed versus assumed” column in the theorem table.

**Downstream consequences:** Prevents the strongest formal results from being over-transferred to the master or domain papers.

**Confidence:** High.

---

## Article 006

### C1 — Fixed-point operator mismatch

**Primary verdict:** `FALSE_AS_STATED` — the diagnosis is correct.

**Corrected statement.** Let \(\mathfrak S\) be the declared safe information-state family. The canonical operator is

\[
\Phi(\mathcal Q)=\mathfrak S\cap\operatorname{Pre}(\mathcal Q),
\qquad \mathcal Q\subseteq\mathfrak S.
\]

Initialize \(\mathcal Q_0=\mathfrak S\) and set

\[
\mathcal Q_{n+1}=\Phi(\mathcal Q_n).
\]

This is equivalent to

\[
\mathcal Q_{n+1}=\mathcal Q_n\cap\operatorname{Pre}(\mathcal Q_n)
\]

**only** when the recursion begins at \(\mathfrak S\), remains inside \(\mathfrak S\), and the descending property has been established. The safe-base operator should be canonical because it makes the safety domain explicit.

The desired object is the greatest post-fixed/invariant family:

\[
\operatorname{gfp}(\Phi)
=\bigcup\{\mathcal Q\subseteq\mathfrak S:\mathcal Q\subseteq\Phi(\mathcal Q)\}.
\]

**Countable versus transfinite descent.** Monotonicity alone gives a greatest fixed point by Knaster–Tarski, but it does not guarantee that \(\bigcap_{n<\omega}\mathcal Q_n\) is fixed. Countable descent is justified in a finite model, or in the compact constructions of Article 002 when the predecessor is closed under nested compact intersections and the nested action-witness sets have a nonempty compact intersection. In a general powerset lattice, transfinite iteration may be required.

**Counterexample.** Consider a robust one-action tree indexed by ordinals, where a state of rank \(\alpha\) has adverse successors at every lower rank and rank zero has an unsafe successor. Backward elimination removes rank \(0\), then each successor rank, and at a limit ordinal only after all lower ranks have been removed. The closure ordinal can exceed \(\omega\). Thus a generic monotone predecessor cannot be assumed to stabilize after countably many finite-horizon steps.

**Policy selection in the limit.** At the limit, retain a policy only after proving that the sets of finite-horizon safe actions are nonempty, closed, nested subsets of a compact action space; their intersection supplies a limiting action. Then separately apply B2 if measurable rather than arbitrary selection is required.

**Recommended source status:** Replace the flawed theorem with a conditional fixed-point theorem; do not use countable descent outside a stated continuity/compactness class.

**Literature:** Knaster–Tarski; Cousot & Cousot, “Constructive versions of Tarski’s fixed point theorems,” *Pacific Journal of Mathematics* 82 (1979), 43–57.

**Confidence:** High.

---

### C2 — Common safe prescription

**Primary verdict:** `TYPE_OR_DOMAIN_ERROR` — raw-action intersection is correct only for a centralized common-action semantics.

**Corrected statement.** At belief \(B\), define a class of implementable prescriptions \(\Gamma(B)\). A safe prescription is

\[
\mathsf{Pres}_{Q}(B)=
\left\{\gamma\in\Gamma(B):
\forall x\in B\cap Q\ \forall d\in D(x),
\ f(x,\gamma(x),d)\in T_Q(x)
\right\}.
\]

The obstruction is \(\mathsf{Pres}_{Q}(B)=\varnothing\). If the central institution can issue only one state-independent action, \(\Gamma(B)\) consists of constant maps and this reduces to the raw-action intersection. If a local implementer observes the latent mode/state and can lawfully apply a state-contingent rule, the raw intersection is too strong.

**Counterexample.** Let a hidden mode \(\theta\in\{-1,+1\}\) govern \(\dot z=\theta u\) at the boundary \(z=0\), with \(u\in\{-1,+1\}\). A central common action cannot protect both modes. A local implementer who observes \(\theta\) can use \(\gamma(\theta)=\theta\) and protect both. The difference is information and authority, not algebra.

**Recommended source status:** Conditional theorem/template after an explicit prescription semantics is chosen.

**Confidence:** High.

---

### C3 — Information-refinement inclusion

**Primary verdict:** `TYPE_OR_DOMAIN_ERROR` — kernels in different belief spaces cannot be literally compared by inclusion without a map.

**Corrected statement.** Let a finer information history \(h_1\) generate a coarser history \(h_2=G(h_1)\) through a causal garbling map. For a common prior domain, any coarse-information policy \(\pi_2\) lifts to \(\pi_1(h_1)=\pi_2(G(h_1))\). Hence the set of viable **priors** under the coarse information structure is contained in the corresponding viable-prior set under the finer structure. Alternatively, compare physical projections only after defining a projection from each viable-belief family.

Do not write \(\operatorname{EViab}_{\mathcal I_2}\subseteq\operatorname{EViab}_{\mathcal I_1}\) when the left and right sides inhabit different hyperspaces.

**Counterexample.** A singleton fine posterior and a two-state coarse posterior are different types of objects. Neither is literally an element of the other belief space even when the fine posterior is set-theoretically contained in the coarse posterior.

**Recommended source status:** Corrected conditional theorem.

**Confidence:** High.

---

## Article 007

### D1 — Hybrid phase space

**Primary verdict:** `TYPE_OR_DOMAIN_ERROR`.

**Corrected statement.** For a continuous history and a discrete institutional mode, use the disjoint hybrid phase space

\[
\mathsf X^{\rm hyb}=igsqcup_{h\in\mathsf H}
\bigl(\mathcal C([ -\tau,0],\mathbb R^n)\times\{h\}\bigr),
\]

or the equivalent pair \((x_t,h)\). A reset must be a typed map

\[
R_{h\to h'}:\mathsf X_h\to\mathsf X_{h'}.
\]

A pointwise jump in the current physical value with an unchanged continuous delay tail does not map into \(\mathcal C([ -\tau,0],\mathbb R^n)\). Either use a declared continuous phase-space memory reset, use a carefully developed piecewise-history/càdlàg state space with an appropriate topology, or move the memory into a finite-dimensional augmented ODE state.

**Counterexample.** Replace only \(x_t(0)\) while retaining \(x_t(\theta)\) for \(\theta<0\). The resulting history has a jump at zero and is not continuous.

**Recommended source status:** Supersede the flawed phase-space construction; retain the taxonomy and use Article 002’s restricted hybrid constructions.

**Literature:** Goebel, Sanfelice & Teel, *Hybrid Dynamical Systems* (2012), DOI: [10.1515/9781400842636](https://doi.org/10.1515/9781400842636).

**Confidence:** High.

---

### D2 — Duplicated institutional mode

**Primary verdict:** `TYPE_OR_DOMAIN_ERROR`.

**Corrected statement.** If the mode is unobserved, the information state is one belief/set over the full hybrid state:

\[
B_t\subseteq\bigsqcup_{h\in\mathsf H}\mathsf X_h.
\]

Do not append a second separate \(h\). If the mode is known, write \((B_t,h_t)\) only when \(B_t\) is explicitly a conditional belief over the continuous history given \(h_t\), i.e. \(B_t\subseteq\mathsf X_{h_t}\).

**Counterexample.** A belief that already contains \((x_t,h)\) assigns probabilities/possibilities to modes. Adding a second mode coordinate can produce contradictory states such as a belief supported only on \(h=0\) paired with displayed mode \(h=1\).

**Recommended source status:** Type correction; otherwise superseded by Article 002.

**Confidence:** High.

---

## Article 011 V2

### E1 — Hold/interpolation mismatch

**Primary verdict:** `NOT_AN_ERROR_BUT_NEEDS_CLARIFICATION`.

**Corrected statement.** The displayed SD-E-B3 model is a zero-order-hold model: \(E_n\) is held on \([t_n,t_{n+1})\). The positivity proposition can validly be generalized to any declared measurable interpolation satisfying

\[
E(t)\in\operatorname{co}\{E_n,E_{n+1}\}\subseteq[0,E_{\max}]
\]

on each interval, provided the process equation is rewritten with that realized \(E(t)\) and the command/assessment timing is specified.

**Proof sketch.** The factorized stock equation preserves non-negativity for any bounded measurable \(E(t)\); variation of constants preserves \(Z\ge0\); convex interpolation preserves the effort bounds.

**Counterexample.** An interpolation that overshoots \([0,E_{\max}]\), or an unspecified lagged deployment rule, does not inherit the proposition. More importantly, it defines a different sampled-data map and cannot inherit response regions calculated for zero-order hold.

**Recommended source status:** Keep as a proposition after separating “SD-E-B3 zero-order hold” from a generalized bounded-interpolation lemma.

**Confidence:** High.

---

### E2 — Sampled-data empirical identification

**Primary verdict:** `NOT_AN_ERROR_BUT_NEEDS_CLARIFICATION`.

**Minimal defensible identification sequence.**

1. **Mechanism registration.** Fix controller sign, state/assessment/command/implementation timing, predicted phase ordering, competing ecological mechanisms, and a falsification rule.
2. **Source-linked event panel.** Record raw observation, assessment completion, decision, legal adoption, implementation, compliance, realized pressure, and ecological response separately. A nominal review schedule is not evidence of an effective review opportunity.
3. **First-stage causal variation.** Identify exogenous or quasi-exogenous variation in decision/deployment timing, or randomize it in an ethical simulation/human-in-the-loop design. Test anticipation, manipulation, spillovers, and concurrent shocks.
4. **Closed-loop model comparison.** Compare preregistered environmental, demographic/cohort, institutional-delay, combined, and null models out of sample. An ordinary stock–effort cross-spectrum cannot identify open-loop causal direction.
5. **Power before interpretation.** Simulate detection under the actual record lengths, missingness, sampling interval, and multiplicity plan. A low-power spectral null is non-adjudicative.
6. **MSE for policy claims.** Only after the mechanism is identified or explicitly treated as uncertain should review cadence, protective versus extractive response, deployment lags, and structural uncertainty be compared in closed loop.

**Recommended source status:** The prospective design is a valuable research programme. The current retrospective spectral screen is a selected-cohort descriptive/null result, not causal identification.

**Downstream consequences.** Article 011 should not be a standalone empirical test until the delayed-recruitment variants, histories, data-processing archive, and eligibility protocol are fully registered.

**Confidence:** High.

---

## Article 012

### T12.1 — Boundary effort equilibrium on the extinction face

**Primary verdict:** `MODEL_INCOMPLETE`.

At \(N=0\), the signal equilibrium is \(Z=\delta\). Because the boundary gate vanishes at \(E=E_{\max}\),

\[
(N,Z,E)=(0,\delta,E_{\max})
\]

is always an equilibrium of M3-B. The bracket-root equilibrium \((0,\delta,E^*)\) is not the only extinction-face equilibrium. If \(E_{\max}<r/q\), an additional positive-stock boundary-effort equilibrium may also exist.

**Downstream consequence.** The statement that the positive equilibrium exists exactly when “the extinction equilibrium” is stock-unstable must be restricted to the interior-effort extinction branch. This alters global/basin interpretation, not the interior equilibrium calculation or cubic Hopf-frequency theorem.

**Recommended status:** Add as an identity/model-completion correction. High confidence.

### T12.2 — Fixed-demand stock culling at zero

**Primary verdict:** `MODEL_INCOMPLETE`.

In the fixed-demand M3-LC experiment, a constant stock-culling term remains negative at \(N=0\) unless it is donor limited or the process is stopped at the extinction event. Use, for example, a donor-limited removal \(D\chi(N)\) with \(\chi(0)=0\), or define an absorbing event/reset at \(N=0\).

**Downstream consequence.** A reported finite “time to zero” under unbounded fixed culling is not a valid trajectory of the non-negative stock model. The qualitative contrast with recruitment suppression may remain, but the finite-extinction claim and comparison need recomputation under the corrected law.

**Recommended status:** Model correction; high confidence.

### T12.3 — \(\omega_A\) versus \(\kappa_A\)

**Primary verdict:** `TYPE_OR_DOMAIN_ERROR`.

Choose one symbol for the active-pool relaxation/turnover parameter, state its units, and use it in the equation, equilibrium branch, sweep, and reported threshold. Preserve a versioned mapping if two different parameters were actually used.

**Downstream consequence:** Mostly reproducibility, unless the symbols refer to distinct mechanisms. High confidence.

### T12.4 — MPF invariant simplex

**Primary verdict:** `MODEL_INCOMPLETE`.

For the displayed MPF ecological subsystem,

\[
\dot X=g(X,A)-m(X)-qEX,
\qquad
\dot U=m(X)-\gamma_UU,
qquad A=\mathcal M-X-U,
\]

one has at \(X+U=\mathcal M\), hence \(A=0\) and \(g(X,0)=0\),

\[
\frac{d}{dt}(X+U)=-qEX-\gamma_UU\le0.
\]

Together with \(\dot X=0\) at \(X=0\) and \(\dot U=m(X)\ge0\) at \(U=0\), the triangle

\[
\{X\ge0,\ U\ge0,\ X+U\le\mathcal M\}
\]

is forward invariant under the stated regularity and \(E\ge0\) assumptions.

**Downstream consequence:** This supplies the missing physical admissibility result for MPF. It does not transfer the M3-B box theorem or its bifurcations.

**Recommended status:** Add as a theorem/proposition with proof. High confidence.

### T12.5 — Fold/SNPO language

**Primary verdict:** `NOT_AN_ERROR_BUT_NEEDS_CLARIFICATION`.

Maintain the stated numerical status: a persistence bracket, branch fold candidate, or multiplier near one is not a saddle-node-of-periodic-orbits theorem without branch collision and nondegeneracy evidence. Do not use SNPO language in title, abstract, or conclusion unless that evidence is added.

**Downstream consequence:** No change to the local cubic theorem or reported numerical observations. High confidence.

---

## Article 013

### T13.1 — Service readout name

**Primary verdict:** `TYPE_OR_DOMAIN_ERROR`.

Rename the service map to \(\mathsf S_{\rm svc}(z,u,\theta)\), reserving \(\mathsf O\) for an observation map. This is necessary for the master/Article 002 architecture to remain type-clear.

### T13.2 — Directional support fraction

**Primary verdict:** `TYPE_OR_DOMAIN_ERROR` — the requested closedness/attainment repair is necessary but not fully sufficient for the usual “fraction” interpretation.

Let

\[
A_{\bar s}=\{\alpha\in[0,1]:\alpha\bar s\in\Gamma_{\rm reg}(z)\}.
\]

If \(\Gamma_{\rm reg}(z)\) is closed and \(0\in\Gamma_{\rm reg}(z)\), then \(A_{\bar s}\) is compact and the supremum is attained. To interpret \(\alpha_{\rm reg}\) as a maximal feasible **fraction with every smaller fraction feasible**, also require radial/star-shaped feasibility along \(\bar s\):

\[
\alpha\bar s\in\Gamma_{\rm reg},\ 0\le\beta\le\alpha
\implies\beta\bar s\in\Gamma_{\rm reg}.
\]

Convexity plus \(0\in\Gamma_{\rm reg}\) is sufficient.

Without radial feasibility, the supremum can be attained while intermediate fractions are infeasible, so “fraction supported” is misleading. Without closedness, the supremum need not be feasible.

**Recommended status:** Corrected definition/conditional proposition. Preserve the accounting paper’s central conclusion.

**Confidence:** High.

---

# 4. Restricted Operator II theorem target

The smallest useful theorem is a **finite-mode, fixed-review, robust reach–avoid–maintain theorem**. It should be a real theorem, not a restatement of transformation language.

### Proposed class

- A finite architecture graph \(Q\) and disjoint-union state space
  \[
  \mathsf X^\sqcup=\bigsqcup_{q\in Q}(\{q\}\times\mathsf X_q).
  \]
- Each \(\mathsf X_q\) is compact metric; each safe set \(K_q\) and transition-safe set \(K_q^{\rm tr}\) is compact.
- At a fixed review period, an action either remains in \(q\) or selects an edge \(e:q\to q'\). The exact tube and endpoint maps are compact-valued and Hausdorff-continuous.
- Every transition has a typed reset/translation map \(R_e\) that carries physical stocks, liabilities, obligations, and an identity label. Identity/obligation preservation is encoded as a closed transition guard \(G_e\).
- There is at most one mode transition per review interval, excluding Zeno behaviour by construction.
- The destination robust kernel \(D\subseteq\{q'\}\times K_{q'}\) is already constructed by an Article 002-type tube predecessor.

Define the transition predecessor

\[
\operatorname{Pre}_{\rm tr}(A)=
\left\{(q,x)\in K_q^{\rm tr}:
\exists a\in\mathsf A(q,x)\ \forall w,
\ \mathsf T(q,x,a,w)\subseteq K^{\rm tr},
\ (q_a,\mathsf G(q,x,a,w))\in A,
\quad q_a\text{ the destination mode selected by }a
\right\}.
\]

Set \(R_0=D\) and

\[
R_{j+1}=R_j\cup\operatorname{Pre}_{\rm tr}(R_j).
\]

### Theorem target

Under compactness, exact-tube continuity, and selector assumptions, \(R_j\) is exactly the set from which one causal hybrid policy reaches the destination robust kernel in at most \(j\) review intervals while satisfying all transition-safe, identity, and obligation guards for every disturbance realization. Once in \(D\), the destination invariance policy maintains safety. The proof is a finite-horizon induction plus the destination-kernel invariance theorem.

### Why this is nontrivial

It permits different state spaces, explicit reset maps, protected obligation translation, robust disturbance quantification, reach–avoid constraints, and post-arrival maintenance. It does not pretend to solve arbitrary variable-time delayed hybrids, unknown architectures, or contested identity criteria.

### Necessary failure example

If a reset maps a physical stock into a destination coordinate but drops a liability/rights obligation, then reachability in the destination physical coordinates does not prove admissible transformation. If the target is merely reached but not robustly invariant, reachability also does not prove sustainability.

**Recommended source status:** Conditional theorem target. Implement first in the fixed-review setting; general delayed-hybrid transformation belongs in the research programme.

---

# 5. Restricted composition theorem target

Do not begin with all deterministic, probabilistic, strategic, and scenario contracts. Begin with a robust continuous-time or sampled-data **input-bounded contract** class.

### Proposed theorem class

Let

\[
\dot x_i=f_i(x_i,u_i,z_i,d_i),
\qquad z_i=C_i(x_{-i}),
\]

with local closed safe sets \(K_i\), local input-assumption sets \(Z_i\), and a shared-resource allocator. Assume:

1. **Local robust contract.** For every \(x_i\in K_i\) and \(z_i\in Z_i\), a local control exists whose all disturbance velocities lie in \(T_{K_i}(x_i)\).
2. **Self-consistent interface bounds.** Contract gains obey a checkable small-gain/monotone condition. For a linear margin bound, require
   \[
   a\ge d+\Gamma a,
   \qquad \rho(\Gamma)<1,
   \]
   so \(a=(I-\Gamma)^{-1}d\) supplies compatible bounds.
3. **Shared source/sink feasibility.** At every \(x\in\prod_iK_i\), the joint action set satisfying local safe-action conditions and
   \[
   \sum_i r_i(u_i)\le R(x),
   \qquad
   \sum_i\ell_i(u_i)\le C(x)
   \]
   is nonempty.
4. **Joint selection and well-posedness.** The allocator selects a joint action with the regularity required by the dynamics.

Then \(\prod_iK_i\), intersected with the shared-resource constraints, is a robustly controlled-invariant set. The proof is a product-tangent-cone argument after the small-gain condition proves that every module’s input assumption is met.

### Why this is stronger than “assumptions imply guarantees”

The small-gain fixed point verifies that circular assumptions are jointly satisfiable; the shared allocator verifies that local controls can coexist; and the conclusion is global robust invariance, not merely a restatement of local contracts.

### Required counterexamples

- **Destruction:** two locally viable modules that each assume access to 0.6 units of a shared source with total capacity 1 cannot compose. The Article 001 asymmetric MSY coupling example can be retained as a richer dynamical destruction example after its prerequisites are verified.
- **Rescue:** a source-transfer/coupling channel can create a viable joint equilibrium where one isolated subsystem is nonviable, as in the registered two-patch rescue example. The mechanism and all sink constraints must be stated.

**Literature:** Chen et al., “Compositional Set Invariance in Network Systems with Assume-Guarantee Contracts,” ACC (2019); Saoud, Girard & Fribourg, “Assume-guarantee contracts for continuous-time systems,” *Automatica* 134 (2021), DOI: [10.1016/j.automatica.2021.109910](https://doi.org/10.1016/j.automatica.2021.109910).

**Recommended source status:** Conditional theorem target; do not label the master’s general contract layer a theorem before this restricted result exists.

---

# 6. Rejected-formulation redesign

## 6.1 Institutional measurement

Use a staged, non-compensatory measurement architecture.

1. **First measurement layer: a dashboard/profile.** Record separately: observation coverage and error, assessment latency, decision authority, implementation/deployment lag, enforcement probability, compliance, mandate workload, learning capacity, and budget/staff margins. Each entry needs a unit, scale, source, uncertainty, and threshold where meaningful.
2. **Second layer: a dynamics-aware timing margin.** For a declared hazard/threshold,
   \[
   M_\tau=T_{\rm exit}-T_{\rm response}
   \]
   is interpretable only after defining both times, uncertainty, buffers, and which population bears the risk. It is one margin, not a universal institutional score.
3. **Third layer: epistemic-institutional viability/capture.** Build a belief-state kernel or capture basin only when an exact/validated information process and implementable prescription class have been constructed.

The profile is the correct first empirical object. The timing margin is the first dynamic synthesis. The kernel is the right formal endpoint, not a replacement for measured institutional facts.

## 6.2 Distributive measurement

A valid design should use:

- **Dimensionless group-specific margins:** for a lower bound \(y_{gj}\ge y^{\min}_{gj}\), define
  \[
  m_{gj}=\frac{y_{gj}-y^{\min}_{gj}}{s_{gj}},\qquad s_{gj}>0,
  \]
  with scales declared prospectively.
- **Exact conjunction:** \(\min_{g,j}m_{gj}\ge0\). This is nonsmooth but exactly represents the protected conjunction.
- **Conservative smooth certificate:**
  \[
  \operatorname{smin}_\beta(m)
  =-\beta^{-1}\log\sum_{g,j}e^{-\beta m_{gj}}.
  \]
  Since \(\operatorname{smin}_\beta(m)\le\min m_{gj}\), the condition \(\operatorname{smin}_\beta(m)\ge0\) is sufficient but not equivalent at finite \(\beta\).
- **Correct lower-tail statistic:** use an essential infimum when every person’s right is protected; use a named lower quantile only when the normative rule explicitly protects that percentile.
- **Correct pooling:** for group distributions \(F_g\) and population weights \(w_g\), use \(F_{\rm pool}=\sum_gw_gF_g\), not an average of group deciles.
- **Dynamic condition:** include group distributions, capacities, and transition matrices in the state; then impose a genuine common-control viability/barrier condition on every protected margin.

No LogSumExp construction should mix dimensional quantities, and no finite smoothing should be called equivalent to the exact conjunction.

---

# 7. First end-to-end domain case

**Recommendation: groundwater, but only a tightly bounded aquifer/governance case—not a basin-wide anomaly illustration.**

Groundwater is the stronger first full architecture test because it can exercise physical stock accounting, observation/assessment uncertainty, decision and deployment dates, permit/enforcement capacity, heterogeneous users, cross-boundary recharge/import interfaces, and emergency/recovery policy. It can therefore test the architecture rather than only the ledger.

The case must use a site with: calibrated storage or defensible water-level-to-storage conversion; pumping records; recharge/climate data; dated assessments, permits, and implementation; a declared allocation/justice rule; and an explicit boundary. G3P anomalies alone are not enough for a physical viability claim.

**Phosphorus should be the second case.** It is superior for typed moiety accounting, provenance, quality grades, and global/catchment commons, but less naturally exercises the information-and-institution modules unless a specific watershed/trade-governance case is chosen.

---

# 8. Recommended minimum-paper architecture

## Paper 1 — Architectural flagship

**Role:** revised master manuscript.  
**Claim:** candidate architecture and disciplined research programme, not a completed universal law.  
**Include:** frozen specification; typed registry and verdict; Operator I definitions; Operator II semantics and restricted theorem target; boundary/interface/commons/contract templates; claim-status ledger; one concise end-to-end groundwater protocol.  
**Exclude:** long proof corpus, unregistered numerical claims, and broad Article 001 theorem inventory.

## Paper 2 — Formal foundations

**Base:** Article 002.  
**Role:** technical theorem paper.  
**Include:** typed conservation/invariance; substitution/Farkas result; observation-fibre theorem; clearly separated sampled/full-state, finite-clopen, RFDE, hybrid, and exact-information-state kernels; projectability and reduction; selected corrected Article 001 propositions only where they genuinely support the common formal spine.  
**Required repair:** selector status, strict theorem/application separation, canonical notation.

Article 001 should not be published in its current omnibus form. Preserve its valid material in a traceable technical supplement/source registry. A later resource-viability paper is justified only if the corrected scalar resource, coupling, commons, and institutional results are rewritten around one coherent independent question.

## Paper 3 — Registered delay-dynamics paper

**Base:** Article 012.  
**Role:** independent nonlinear-dynamics/numerical paper.  
**Include:** the registered M3/MPF models, corrected admissible domains, exact local cubic result, versioned numerical evidence, and strict distinction between theorem, numerical proposition, inferred classification, and conjecture.  
**Required repair:** T12.1–T12.5 and an archive sufficient to reproduce every numerical proposition.

## Not yet a separate paper

- **Article 011 V2:** retain as a registered supplement/methods programme until delayed-recruitment variants and empirical artifacts are complete. It merits a separate empirical-methods paper only after the event panel, model registry, source data, and identification design are implemented.
- **Article 013:** retain as a core accounting module and/or formal-foundations application. It could become a separate accounting paper only if the worked case is expanded into a fully reproducible end-to-end empirical analysis.

This is the minimum currently merited architecture: **three papers**, with Article 011 and Article 013 developing further only when their independent evidentiary cases are complete.

---

# 9. Top five priorities

1. **Repair the robust-invariance/fixed-point foundation.** Audit every \(\exists\pi\forall d\), weak viability, strong invariance, and belief-kernel claim (A1, C1–C3, and all downstream institutional/composition uses).
2. **Canonize Article 002 and notation.** Create a single theorem registry naming exact domain, information, selector, and tube assumptions.
3. **Correct or demote the Article 001 overclaims.** A2, A4–A11 should be fixed before any flagship citation; A5 should be demoted unless a genuine generic proof is supplied.
4. **Complete Article 012’s model admissibility and numerical archive.** The extinction-face equilibrium and MPF simplex are not editorial details; they affect interpretation of global dynamics.
5. **Prove one restricted composition theorem and one fixed-review Operator II theorem, then execute a bounded groundwater case.** Do not attempt all social/ecological/general transformation claims simultaneously.

---

# 10. Major issues absent from the packet

1. **Robust-versus-chance semantics in the master.** The master’s probability statement needs a probability law, filtration, and a policy measurability condition. It must not share notation or conclusions with adversarial robust viability.
2. **Global audit of information timing.** The sources use full-state feedback, belief-state feedback, observation-only feedback, local prescriptions, and institutional implementation. Every theorem must state who observes what and when action is selected relative to disturbance and observation.
3. **Institutional Theorem 13.2 requires the A1 repair.** “Measurable selection and Nagumo applied to belief-state dynamics” is not enough until an actual belief transition law and strong-invariance hypotheses are supplied.
4. **No theorem-to-application bridge should be implicit.** An Article 002 theorem using exact compact filters/tubes is not an application result until those objects are constructed or independently verified for the application.
5. **Operator II must preserve typed liabilities, not merely coordinate values.** Translation maps should have explicit domains/codomains and a conservation/obligation ledger; otherwise transformation can erase obligations by re-description.
6. **Numerical status must be versioned.** A numerical proposition needs a model hash, parameter file, history class, algorithm, tolerance/refinement, and archived output. Long integration alone is not a bifurcation certificate.

---

# 11. Core references

- Aubin, J.-P. (1991). *Viability Theory*. Birkhäuser.
- Aubin, J.-P., Bayen, A. M., & Saint-Pierre, P. (2011). *Viability Theory: New Directions*. Springer.
- Blanchini, F. (1999). Set invariance in control. *Automatica, 35*(11), 1747–1767. DOI: [10.1016/S0005-1098(99)00113-2](https://doi.org/10.1016/S0005-1098(99)00113-2).
- Cousot, P., & Cousot, R. (1979). Constructive versions of Tarski’s fixed point theorems. *Pacific Journal of Mathematics, 82*(1), 43–57.
- Goebel, R., Sanfelice, R. G., & Teel, A. R. (2012). *Hybrid Dynamical Systems: Modeling, Stability, and Robustness*. DOI: [10.1515/9781400842636](https://doi.org/10.1515/9781400842636).
- Kuratowski, K., & Ryll-Nardzewski, C. (1965). A general theorem on selectors. *Bulletin of the Polish Academy of Sciences*, 13, 397–403.
- Michael, E. (1956). Continuous selections I. *Annals of Mathematics, 63*, 361–382. DOI: [10.2307/1969615](https://doi.org/10.2307/1969615).
- Rosen, J. B. (1965). Existence and uniqueness of equilibrium points for concave N-person games. *Econometrica, 33*(3), 520–534.
- Saoud, A., Girard, A., & Fribourg, L. (2021). Assume-guarantee contracts for continuous-time systems. *Automatica, 134*, 109910. DOI: [10.1016/j.automatica.2021.109910](https://doi.org/10.1016/j.automatica.2021.109910).
- Chen, Y., Anderson, J., Kalsi, K., Low, S. H., & Ames, A. D. (2019). Compositional set invariance in network systems with assume-guarantee contracts. *American Control Conference*, 1027–1034.

---

## Final assessment

The project should proceed, but only with an explicit hierarchy of claim strength. The architecture is publishable as an architecture. Article 002 contains a credible restricted theorem programme. Article 012 can become a strong registered applied dynamics paper once its boundary/model corrections are made. The most important intellectual discipline is to preserve the distinction between a possible trajectory, a robust policy, a belief-state policy, a state-contingent delegated prescription, and a stochastic chance guarantee. That distinction will make the resulting general theory substantially more rigorous rather than less ambitious.

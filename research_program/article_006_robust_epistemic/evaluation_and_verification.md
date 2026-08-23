# Article 006 Evaluation and Verification

## Bibliographic identity

**Source file:** `uploads/Paper_II_Robust_Epistemic_Viability_V2.txt`  
**Title:** *Robust and Epistemic Viability for Hybrid Material–Institution Systems*  
**Format:** LaTeX article source  
**Length:** approximately 2,290 words, 228 lines  
**Formal content:** four theorems, one lemma, five propositions, one definition, six remarks, one unnumbered conjecture  
**Evaluation status:** evaluated; integration not yet executed

## Executive assessment

The article presents a compact conditional mathematical spine for material feasibility, partial observation, institutional authority, uncertain implementation, recovery, and compositional safety. Most of its legitimate results are mathematically sound at the stated level or become sound after modest clarification.

One critical formal problem occurs in the sampled epistemic-institutional fixed-point theorem: the recursive finite-horizon operator and the monotone operator to which Tarski’s theorem is applied are not the same operator as written. The finite-horizon recursion uses

\[
\mathfrak K_{n+1}
=
\mathfrak K_n
\cap
\operatorname{Pre}_{\mathfrak I}(\mathfrak K_n),
\]

whereas the theorem defines

\[
\mathcal T(\mathfrak Q)
=
\mathfrak S
\cap
\operatorname{Pre}_{\mathfrak I}(\mathfrak Q).
\]

Unless additional definitions make these equivalent, the countable/transfinite fixed-point claim does not follow from the displayed recursion. This must be corrected before integration.

The article also overlaps extensively with stronger and more detailed results already present in Articles 001 and 002. Under the minimum-paper rule, it does not currently merit a separate publication. Its unique value lies in the compact institutional information-state formulation \((B,h)\), the explicit prescription/implementation lower-game semantics, and a concise claim-status spine. Those parts should be integrated into the flagship or Article 002. Duplicated theorem families should be marked superseded-but-preserved rather than published again.

---

## 1. Information-state setting

The information state

\[
Z=(B,h),
\qquad
B\subseteq\mathscr H\times\Theta,
\qquad
\mathscr H=C([ -\tau_{\max},0],\mathcal X)
\]

is appropriate for a delayed partially observed system when:

- \(\mathcal X\) and \(\Theta\) are declared;
- the history norm and topology are specified;
- \(B\) is nonempty and belongs to a chosen hyperspace of closed or compact sets;
- institutional mode space for \(h\) is specified;
- compatible-state updates preserve the information-state domain.

As written, \(\mathfrak S\) is not formally defined as a complete lattice, compact hyperspace, or measurable state space. The powerset lattice argument later can use an abstract set \(\mathfrak S\), but applications need an exact domain and update map.

Decision times are assumed locally finite. This prevents finite-interval event accumulation but does not prove existence or continuation of the physical RFDE between events.

---

## 2. Conditional hybrid moiety balance

The theorem states

\[
\mathsf L^\top r(t)-\mathsf L^\top r(0)
=
\int_0^t
\mathsf L^\top b(\phi_s,u(s),\omega(s),s)\,ds
+
\sum_{t_k\le t}
\mathsf L^\top[r(t_k^+)-r(t_k^-)].
\]

Given absolute continuity between locally finite events and

\[
\mathsf L^\top\mathsf S=0,
\]

the identity is correct. It records all jump increments rather than claiming they are internally conservative.

### Clarifications

- If a jump is an internal transformation, require \(\mathsf L^\top(r^+-r^-)=0\) or a jump incidence factorization with left-kernel conservation.
- If a jump crosses the boundary, classify it as a boundary impulse.
- The proof is correct but terse; it should explicitly sum flow intervals and jump increments.
- The yield-routing obligation is correct: missing yield must be another compartment or boundary transfer, not silent loss of the accounting moiety.

This result is largely duplicated by Article 002’s typed hybrid-conservation theorem, which provides a fuller proof and explicit jump matrices. Article 002 should be the canonical source unless this paper’s history-state setting adds a needed specialization.

---

## 3. Conditional hybrid history-cone invariance

Under:

1. well-posed unique RFDE flow;
2. quasipositivity at every zero material component for every nonnegative history;
3. reset preservation of nonnegative material states;
4. locally finite events;

the nonnegative material cone is forward invariant on the interval of existence. This is a standard and valid conditional result.

### Required clarification

- Specify the RFDE phase space and norm.
- State whether functional and institutional history coordinates are unrestricted while material coordinates are nonnegative.
- Require post-reset history, not only current material state, to belong to the RFDE phase space if the reset changes delayed coordinates.
- Preserve the interval-of-existence limitation.

Article 002 again contains a more detailed version. This theorem is a concise specialization, not an independent publication contribution.

---

## 4. Full-information benchmark and stability lemma

The full-information benchmark is correctly limited to a sufficiently regular finite-dimensional ODE and requires:

- closed safe set;
- robust tangency/common control at active constraints;
- a suitable selection or solution concept;
- existence over the declared horizon.

It is more a conditional invocation of established invariance theory than a new proposition.

The first counterexample in the stability/safety lemma is explicit and correct:

\[
\dot x=-(x+1)
\]

has a stable equilibrium at \(-1\), outside the safe set \([0,\infty)\).

The second half should use an explicit system. For example,

\[
\dot x=-x+w,
\qquad
\mathcal C=[-1,1],
\qquad
w\in[-2,2].
\]

The nominal equilibrium \(x=0\) is safe and stable for \(w=0\), but admissible disturbance \(w=2\) drives the state above the safe interval. The current phrase “take a nominally safe stable system” is too informal for a proved lemma.

---

## 5. Prescription, implementation, and quantifier order

The distinction

\[
a\in\Gamma(B,h),
\qquad
u\in\mathcal E(B,h,a)
\]

is correct and valuable. Robust institutional safety requires one nonanticipating prescription strategy that succeeds for all compatible implementations, disturbances, parameters, and observation branches.

The warning that

\[
\forall w\,\exists u_w
\]

is not implementable when \(w\) is unknown at decision time is correct.

### Required clarification

- \(\Gamma\) supplies prescriptions; \(\mathcal E\) supplies possible implemented actions.
- Tube safety must aggregate every physical state in \(B\), every implementation in \(\mathcal E\), and every disturbance branch.
- If implementation depends on the latent physical state, the update must aggregate those outcomes rather than assume one known implementation.

This is one of the article’s most useful concise contributions and should be preserved in the flagship policy architecture.

---

## 6. Sampled predecessor and fixed-point theorem

### 6.1 Finite-horizon recursion

The predecessor

\[
\operatorname{Pre}_{\mathfrak I}(\mathfrak Q)
\]

has the intended lower-game structure. However, the compatible-state update is written

\[
\Psi(B,h,a,Y^+)
\]

without explicit implemented action, disturbance, parameter, or structural branch arguments, even though the successor must range over all of them. Either \(\Psi\) must be set-valued and already aggregate those branches, or its signature must include them.

The recursion

\[
\mathfrak K_0=\mathfrak S,
\qquad
\mathfrak K_{n+1}
=
\mathfrak K_n
\cap
\operatorname{Pre}_{\mathfrak I}(\mathfrak K_n)
\]

can characterize states safe for at least \(n\) intervals if TubeSafe includes present and inter-sample safety and the successor semantics are exact.

### 6.2 Critical operator mismatch

The theorem then defines

\[
\mathcal T(\mathfrak Q)
=
\mathfrak S
\cap
\operatorname{Pre}_{\mathfrak I}(\mathfrak Q).
\]

Because \(\operatorname{Pre}_{\mathfrak I}(\mathfrak Q)\subseteq\mathfrak S\), this is generally just the predecessor, while the recursion uses \(\mathfrak Q\cap\operatorname{Pre}_{\mathfrak I}(\mathfrak Q)\). They are not identical.

Two coherent repairs are possible.

#### Repair A — safe base set and ordinary predecessor

Define a safe information-state domain \(\mathfrak S_{safe}\) and

\[
\Phi(\mathfrak Q)
=
\mathfrak S_{safe}
\cap
\operatorname{Pre}_{\mathfrak I}(\mathfrak Q),
\]

then set

\[
\mathfrak K_0=\mathfrak S_{safe},
\qquad
\mathfrak K_{n+1}=\Phi(\mathfrak K_n).
\]

This is the standard greatest-invariant-set form.

#### Repair B — contracting operator

Retain the displayed recursion and define

\[
\Phi(\mathfrak Q)
=
\mathfrak Q
\cap
\operatorname{Pre}_{\mathfrak I}(\mathfrak Q).
\]

Tarski gives fixed points of this contracting monotone operator. The interpretation is a greatest post-fixed/invariant family, and countable descent still requires continuity from above or compactness/closedness conditions.

The current proof mixes these two forms. Until repaired, the infinite-horizon fixed-point theorem is not verified as written.

### 6.3 Countable versus transfinite iteration

The article correctly notes that monotonicity alone gives a greatest fixed point by Tarski but not necessarily by countable intersection. Identifying

\[
\bigcap_{n\ge0}\mathfrak K_n
\]

with the greatest fixed point requires an appropriate continuity-from-above, compactness, or closure/selection result. Otherwise transfinite iteration may be required. This is a valuable correction and should be preserved after the operator mismatch is fixed.

---

## 7. Information-refinement monotonicity

The policy-class argument is sound: a controller with finer information can ignore it and implement a coarser-information strategy.

Literal set inclusion

\[
\operatorname{IViab}^{\mathcal I_2}_T
\subseteq
\operatorname{IViab}^{\mathcal I_1}_T
\]

requires the two kernels to be represented in a common physical initial-state space or through a declared map between belief-state spaces. Otherwise the sets have different element types. The theorem should state the projection or identification used for comparison.

Article 001 contains a more detailed information-refinement result. The canonical theorem should be selected after notation harmonization.

---

## 8. Common-action obstruction

The obstruction is correct if \(\mathcal U_{com}(B)\) is defined over prescriptions or implemented-action sets in a way that respects state-dependent implementation.

Potential ambiguity arises if one prescription can induce different safe realized actions in different latent states. An empty intersection of raw implemented actions does not necessarily imply that no common prescription exists. The robust object should be

\[
\mathcal A_{com}(B,h)
=
\left\{
a\in\Gamma(B,h):
\mathcal E(x,h,a)
\subseteq U_{safe}(x)
\quad\forall x\in B
\right\}.
\]

If this prescription set is empty before new information arrives, robust institutional viability fails. This formulation directly matches the article’s lower-game semantics.

---

## 9. Observer-to-safety transfer

The local bound is valid after correcting the notation to a dot product:

\[
\left|
\nabla b_i(X)\cdot
[f(X,k(\widehat X),w)-f(X,k(X),w)]
\right|
\le
L_i\|\widehat X-X\|.
\]

If the full-state feedback has inward margin \(\eta_i\) for all active constraints and disturbances, then the estimated-state feedback preserves nonnegative inward derivative whenever

\[
L_i\|\widehat X-X\|
\le
\eta_i.
\]

Additional requirements:

- the applied control remains admissible;
- the trajectory remains in the region where the margin and Lipschitz bound hold;
- an observer-error theorem supplies the bound.

The article correctly labels this local and does not claim to construct an observer. Article 001 contains stronger observer-transfer and eroded-kernel formulations.

---

## 10. Information value, recovery, and safe learning

The safety value

\[
V_T^{\mathcal I}(B,h)
=
\sup_{\Pi\in\Pi_{\mathcal I}}
\inf_{compatible\ branches}
\min_{0\le t\le T}q(X(t),u(t))
\]

is meaningful when trajectories, policy classes, and optimization are well posed. The article correctly notes that \(V_T\ge0\) does not imply existence of a safe policy if the supremum is zero but unattained. One may use an attained maximum, \(\varepsilon\)-viability convention, or closure of the viable set.

The information-refinement difference is a safety-margin value of information, not entropy. This is valid under aligned initial information states and policy classes.

The recovery and safe-learning templates are sound. Physical entry into a viable physical set does not establish institutional recovery unless the information/institution state also belongs to the epistemic-institutional kernel.

---

## 11. Conditional compositional safety

The proposition is directionally correct but nearly all substantive work is contained in its hypotheses. For a usable theorem, it must specify:

- subsystem state and policy classes;
- interface assumptions and guarantees;
- shared-control feasibility;
- disturbance correlation;
- event synchronization or nonblocking composition;
- how local certificates generate a product or non-product global set.

It is appropriately labeled conditional. Article 001 Theorem 16.1 and Article 002’s contract architecture provide stronger restricted formulations.

---

## 12. Normative monotonicity

If

\[
\mathcal C_X(\lambda_1)
\subseteq
\mathcal C_X(\lambda_2)
\]

and the admissible action/policy system under \(\lambda_1\) is a subset of that under \(\lambda_2\), then the stricter viability kernel is contained in the weaker one, assuming all other dynamics, information, implementation, and disturbance classes are aligned. This is a valid monotonicity result.

The result exposes feasibility consequences of normative choices; it does not justify the choices.

---

## 13. Delay and nonlinear-transition statements

The no-sign-free-delay proposition is valid as a non-universality statement, but it would be stronger with explicit parameter examples showing contrasting stability for the two signs.

The Tikhonov paragraph correctly limits ODE reduction and does not transfer it to RFDEs, global folds, or infinite-horizon safety.

The nonlinear-transition conjecture overlaps Articles 002 and 003. It should be merged into one conjecture with dynamical-class-specific assumptions. “Fast difference-operator contractivity” applies to particular neutral/difference formulations and should not be a universal RFDE condition.

---

## 14. Overlap and supersession

Most theorem families in this article have stronger versions elsewhere in the programme:

| Article 006 content | Stronger or fuller source |
|---|---|
| Hybrid moiety balance | Article 002 typed hybrid conservation |
| Hybrid positivity | Article 002 nonnegative invariance theorem |
| Full-information robust benchmark | Article 001 robust tangency theorem, subject to its verification queue |
| Epistemic fixed point | Articles 001–002 belief and restricted information kernels |
| Information refinement | Article 001 information-refinement theorem |
| Common-action obstruction | Article 001 common-action and hidden-mode results |
| Observer safety margin | Article 001 observer-transfer and safety-buffer theorems |
| Information value | Article 001 value-of-information formulation |
| Recovery | Article 001 emergency and informational capture |
| Compositional safety | Article 001 restricted composition theorem and Article 002 contract framework |
| Nonlinear-transition conjecture | Articles 002–003 conjecture programme |

The unique compact contribution is the joint institutional information state \((B,h)\) with prescription authority \(\Gamma\), implementation correspondence \(\mathcal E\), and lower-game predecessor. That formulation should be preserved and used to organize the stronger results.

---

## 15. Publication assessment

Under the minimum-paper rule, Article 006 does not merit a separate paper in its current form because:

- most results duplicate stronger versions in Articles 001–002;
- the main fixed-point theorem requires correction;
- the unique institutional-state formulation can be integrated into the flagship;
- the nonlinear-transition material overlaps Article 003.

Recommended status:

- **superseded but preserved** for duplicated theorem statements after canonical source selection;
- **integrate after correction** for the \((B,h)\), \(\Gamma\), \(\mathcal E\), lower-game predecessor formulation;
- **merge** the conjecture with the Article 002–003 conjecture programme.

---

## 16. Verification verdict

### Verified or sound after minor clarification

- hybrid moiety identity;
- conditional material positivity;
- prescription/implementation distinction;
- lower-game quantifier order;
- stability/safety independence;
- information-refinement principle;
- observer margin inequality;
- safety-margin value of information caveat;
- informational recovery and safe-learning templates;
- normative monotonicity;
- no sign-free delay conclusion.

### Critical correction required

- predecessor recursion and Tarski fixed-point operator mismatch.

### Additional corrections required

- exact compatible-state update signature;
- common comparison space for information-refinement inclusion;
- common-prescription rather than raw-action obstruction;
- explicit disturbance example in the stability lemma;
- dot product and region/admissibility conditions in observer transfer;
- formal interface assumptions in compositional safety;
- class-specific persistence conjecture.

### Not established by this source

- nonempty kernel for a concrete system;
- construction or tractability of compatible-state updates;
- observer existence or estimator bounds;
- empirical institutional response;
- a specific delay threshold or nonlinear transition;
- a calibrated domain-module result.

Article 006 should remain on integration hold until the critical fixed-point repair and source-selection/supersession map are completed.

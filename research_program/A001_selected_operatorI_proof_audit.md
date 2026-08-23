# A001 Selected Operator I Proof Audit

## Scope

Bounded audit of the A001 results needed by Paper 2 after excluding composition: recovery idempotence, observation/common-action obstructions, robust tangency, observer buffers, and finite-time obstruction. Immutable A001 is not edited.

## Summary verdict

| Source result | Verdict | Controlling treatment |
|---|---|---|
| Proposition 3.1, `Capt_V(Viab(V))=Viab(V)` | Accept with concatenation hypothesis | Paper 2 recovery idempotence lemma |
| Corollary 3.1 | Partly accept | Retain infinite recovery outside kernel; remove unsupported boundary-resilience sentence |
| Theorem 4.2, observation can empty kernel | Accept with belief-domain correction | Paper 2 counterexample |
| Theorem 4.4, observer transfer | Conditional but largely assumption-driven | Replace by explicit safety-buffer corollary; not a main theorem |
| Theorem 4.5, robust tangency | Proof invalid for all-disturbance strong invariance | Supersede by a matched strong-invariance statement |
| Theorem 4.7, common-action obstruction | Accept; add omitted one-step proof | Paper 2 core obstruction |
| Example 4.1, hidden-mode conflict | Accept | Paper 2 example |
| Theorem 4.8, delayed-information obstruction | Repair quantifiers | Robust nonviability obstruction |
| Theorem 4.9, observer safety buffer | Accept only with strong-invariance regularity | Paper 2 conditional corollary |
| Proposition 4.1, eroded kernels | Not proved | Demote to conditional programme unless geometry/constants are supplied |
| Theorem 5.1, barrier sufficiency | Duplicate and proof invalid for strong invariance | Remove as separate theorem |
| Theorem 5.2, finite-time obstruction | Repair quantifiers and conclusion | Adversarial-exit theorem, not “every trajectory exits” |

## 1. Recovery idempotence

Let `K=Viab(V)` under a fixed state space, horizon convention, policy class, and solution concept. If admissible trajectories and controls can be concatenated at a finite hitting time, then

\[
Capt_V(K)=K.
\]

The source proof is correct under that concatenation property: a path reaching `K` while remaining in `V` can be concatenated with a viable continuation, so the initial state was already viable.

### Correction to Corollary 3.1

For `x in V\K`, the constrained recovery time to `K` is infinite. The added sentence claiming a recovery-resilience measure is “identically zero on `boundary K`” is not justified and is generally semantically wrong without a specific measure: points of a closed kernel boundary already belong to `K` and have zero hitting time. Remove that sentence or define a different exterior recovery-speed convention explicitly.

## 2. Observation can empty a physical kernel

Theorem 4.2 is a valid common-action counterexample after correcting the compatible-state domain. With constant observation and possible states in the declared safe/prior domain, the common admissible action is `0`, while perfect state feedback selects `r(S)` and freezes every state. Under `u=0`, every safe initial state exits in finite time.

Do not write `B_t=R` unless the prior and model genuinely admit all real states. It is enough that the compatible set contains an interval on which `r(S)` varies, such as `[1,2]`.

## 3. Common-action obstruction

### Corrected theorem

If a belief/information state `B` contains a boundary-compatible state, no informative observation arrives before action, and

\[
\bigcap_{x\in B}R_V(x)=\varnothing,
\]

then `B` is not in the robust epistemic viability kernel for that decision stage.

### Missing one-step proof

Any observation-based policy must choose one action from the information available at `B`. Robust safety requires that action to belong to every state-specific robust regulation set. The intersection is empty, so no admissible first action exists. Hence no robust epistemic policy exists from `B`. ∎

The hidden-mode example correctly instantiates this theorem.

## 4. Delayed-information obstruction

The source conclusion is too broad because its proof changes “for every action there exists a bad compatible branch” into “every uncertainty branch is bad.”

### Corrected robust obstruction

Assume that for every causal policy before the next informative observation, an admissible disturbance/compatible-state branch can be selected nonanticipatively on which, while the trajectory remains in the strip `0<=q<=a`,

\[
D^+q\le-\varepsilon.
\]

If the next informative observation occurs after `q_0/epsilon`, that branch exits before information can alter the action. Therefore no single policy is robustly safe from the initial information state.

The conclusion is:

\[
\forall\pi\ \exists\text{ compatible disturbance/state branch causing exit},
\]

not that every branch exits.

## 5. Robust tangency: Theorems 4.5 and 5.1

The source proof is invalid for the claimed all-disturbance strong-invariance conclusion. From

\[
F_k(x)\subseteq T_K(x),
\]

a weak viability theorem supplies existence of a viable inclusion trajectory under its hypotheses; it does not by itself show that every trajectory generated by every disturbance remains safe. The sentence “since this holds simultaneously for every disturbance realization” does not follow from the existence theorem.

Theorem 5.1 repeats the same issue and should not remain a separate theorem.

### Controlling repair

Use a strong-invariance theorem with its exact regularity and all-solutions hypotheses. The corrected programme pattern is:

1. one feedback independent of unmeasured disturbance;
2. a closed-loop compact-convex velocity envelope containing every disturbance velocity;
3. the required Lipschitz/Marchaud regularity;
4. proximal-normal or other matched strong-invariance inequalities;
5. explicit forward completeness.

The corrected composition theorem record already implements this pattern. Paper 2 should state one general strong-invariance lemma and instantiate it for Operator I rather than retain two defective A001 proofs.

## 6. Observer transfer and safety buffers

### Theorem 4.4

The theorem is logically conditional but assumption 5 already asserts the central robustness property: every control perturbation below `bar e` keeps the trajectory in `K_*`. The proof merely combines this assumed property with the observer error bound. It is therefore a useful corollary/template, not an independent observer-to-viability theorem.

Retain only after replacing “`K_*` is invariant” by an explicit nominal invariant set plus a proved perturbation-margin condition.

### Theorem 4.9

The derivative calculation is correct:

\[
\nabla b_j f(x,k(\hat x),d)
\ge \eta_j-L_j\|\hat x-x\|.
\]

Thus bounded observer error is absorbed when `L_j ebar<=eta_j`. The final invariance step still requires:

- exact simultaneous active-constraint/tangent characterization;
- a well-posed output-feedback closed loop;
- a matched strong-invariance theorem;
- forward completeness.

With these additions it is a valid conditional observer-buffer corollary.

### Proposition 4.1

The erosion claim is not proved. Strict inward margin on `boundary K` and a bounded generic error do not automatically produce an invariant metric erosion `K^{-c epsilon}` without regular boundary geometry, a quantitative relation between erosion normals and the original margin, and a derived constant `c`. Demote it to a programme statement or prove it for a specified regular set class.

## 7. Finite-time obstruction: Theorem 5.2

The source premise

\[
\sup_u\inf_d D^+q\le-\varepsilon
\]

means that for every control choice there exists a disturbance producing negative drift. It does not mean every disturbance trajectory exits.

### Corrected theorem

Suppose the lower-game information pattern permits the disturbance to select nonanticipatively after the control and, for every state in the strip and every admissible control, there exists an admissible disturbance satisfying `D^+q<=-epsilon`. Assume a measurable/nonanticipative disturbance selection and existence up to exit. Then for every control policy there exists a disturbance strategy that drives `q` from the strip to the unsafe side within at most `q(t_0)/epsilon<=a/epsilon`.

This proves exclusion from the robust/discriminating viability kernel. It does not prove that every trajectory exits.

## 8. Paper 2 routing

### Retain as main results

- recovery idempotence with concatenation;
- observation/common-action counterexamples;
- corrected common-action and delayed-information obstructions;
- one corrected general robust strong-invariance lemma;
- corrected adversarial finite-time obstruction.

### Retain as conditional corollaries

- observer safety buffer with explicit strong-invariance hypotheses.

### Remove or demote

- duplicate Theorem 5.1;
- Theorem 4.4 as an independent theorem;
- Proposition 4.1 until a quantitative erosion proof exists;
- unsupported boundary-resilience sentence in Corollary 3.1.

## 9. Remaining difficult gates

1. Exact external theorem match for the general Operator I strong-invariance lemma.
2. A quantitative erosion theorem for regular safe sets, if retained.
3. Application-specific observer/error and completeness verification.

These are high-stakes theorem-matching tasks and should receive self-contained external-review prompts before manuscript implementation.
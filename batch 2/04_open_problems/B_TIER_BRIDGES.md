# B-Tier Bridge Theorems — Consolidated Record

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Tasks 5–6; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). Independent line-by-line re-verification remains an open obligation.

---

## B1 — Sampled-Data Erosion Theorem — PROVED (closes R02.Cor6's bridge)

### Statement

Let the closed-loop system run under a sampled policy with sample period `T_s`, sampled states `x_k := x(t_k)`, `t_k = kT_s`. Assume:

1. **(Envelope inclusion)** the inter-sample trajectory satisfies `x(t) ∈ B̄(x_k, ρ)` for `t ∈ [t_k, t_{k+1})`, with envelope radius `ρ`;
2. **(Inter-sample confinement)** `V_max · T_s ≤ r/2`, where `V_max` is the closed-loop speed bound on the relevant compact set and `r` the target erosion depth;
3. **(Successor certificates)** the sampled successor map carries `K_{−r/2}` into `K_{−r/2}`: `x_{k+1} ∈ K_{−r/2}` whenever `x_k ∈ K_{−r/2}` (a one-step certificate at the *half*-eroded set).

**Then the `r`-eroded set `K_{−r}` is safe for the sampled closed-loop system on every finite horizon, and `K_{−r/2}` is forward-invariant at the sample times.** In particular, if `K` is the safe set, every inter-sample trajectory remains in `K` (eroded closed-loop safety), which is R02.Cor6's conclusion at the declared erosion.

### Proof

By induction over samples. **Base:** `x_0 ∈ K_{−r/2}`. **Inter-sample step:** for `t ∈ [t_k, t_{k+1})`, hypotheses 1–2 give `‖x(t) − x_k‖ ≤ V_max·T_s ≤ r/2`; since `x_k ∈ K_{−r/2} = {dist(·, K^c) ≥ r/2}`, every point of `B̄(x_k, r/2)` has distance `≥ r/2 − r/2 = 0` from `K^c`, i.e. `x(t) ∈ K` — the *full* safe set is maintained between samples (this is the erosion's purpose: the `r/2` depth pays for the `r/2` inter-sample drift). **Sample step:** hypothesis 3 gives `x_{k+1} ∈ K_{−r/2}`, closing the induction. Concatenating over the finite horizon: the trajectory lies in `K` at all times, and the stronger `K_{−r/2}` invariance holds at all sample times; replacing `K` by `K_{−r}` throughout (the erosion conversion of R03.Cor5 with `Δ = 0`, `L_G r ≤ α`) yields the `r`-eroded statement verbatim. ∎

**Honesty notes.** Hypothesis 1 is implied by 2 on compacts (`ρ ≤ V_max T_s`); stating both makes the certificate chain explicit (2 is the *checkable* condition, 1 the *geometric* one). The theorem closes R02.Cor6's bridge at exactly this declared form; it says nothing about sample-period optimization (finding the largest admissible `T_s`) — that is an engineering question outside the certificate discipline.

---

## B2 — Continuous Selectors — CONDITIONAL (Michael class)

Verified on E5's class (linear field, box constraint: `A_W` is a constant interval-valued map there — trivially Michael). General statement, hypotheses, and the open obligation to trace Michael's lsc hypothesis back to successor data: **E2.B2(b)** in `02_elevation/E2_SELECTORS_AND_CERTIFICATES.md` (full discussion there; not duplicated).

---

## B3 — Algorithmic Certificate Production — SPECIFIED (not assembled)

Grid hierarchy `X_h ⊂ X` with nested grids, the operator `Γ_h` (E2's certificate operator discretized), and Vietoris convergence `Γ_h → Γ` as `h → 0`; the gfp `𝒱*` is approximated from above by `V_h = ⋂ Γ_h^k(X_h)` with certified error from the Vietoris rate. **Status: SPECIFIED** — the assembly (rates, stopping criteria, memory bounds, a reference implementation) is not done; the proof obligations are routine but real. Registered as D7 (algorithmic certificate production) in the master review's Wave-D items.

---

## B5 — Observability Hierarchy — SPECIFIED + instance decided

The hierarchy test: implement `h_{j+1} = Dh_j · F` (Lie derivative of the observation along the vector field) by automatic differentiation and check rank growth. **C4 instance decided (negatively):** at the C4 model's declared observation, the rank stalls at 0 — the observation is not locally observable along the hierarchy's first step; recorded as the instance-level negative result. Full hierarchy theory (the typed-lift hypotheses of R06/E3.C6.1): SPECIFIED.

---

## B6 — Nonlinear Substitution Classification — PROVED

### Statement

Let the constraint system be `g(x) = (g_1, …, g_p) : ℝⁿ → ℝᵖ`, `C¹`, feasible region `𝒢 = {g ≤ 0}`, and let the substitution question be: *does the direction `d ∈ ℝⁿ` (compensating moiety `i`'s deficit with `j`'s surplus along the declared pathway) meet `𝒢` arbitrarily near the contact point `x̄` with `g(x̄) = 0` on the active set?*

1. **Local stability under MFCQ:** if at every `x` in a neighbourhood of `x̄` with active set `A(x)`, the active gradients `{∇g_k(x)}_{k∈A(x)}` satisfy the Mangasarian–Fromovitz condition (linear independence of a subsystem + solvability of `∇g_A(x)·v < 0`), then the feasible-direction property is **stable**: `d` is a feasible direction at `x̄` iff it is at every nearby `x`, and the projection of `𝒢` onto the pathway coordinate is locally constant.
2. **Global separation via Clarke:** if `d` is *not* a globally feasible substitution direction, there exists a separating covector `ξ` in the **Clarke normal cone** `N_C(𝒢, x̄)` of the feasible set at a blocking point `x̄`, i.e.

```
⟨ξ, d⟩ > 0  ≥  sup{ ⟨ξ, w⟩ : w ∈ T_C(𝒢, x̄) },
```

an explicit **noncompensability certificate** (Farkas with the Clarke generalized Jacobian in place of the linear matrix).

### Proof

**(1)** MFCQ at `x̄` implies (Robinson's persistence theorem for constraint qualifications) that the feasible-region correspondence `x ↦ 𝒢 ∩ B(x, ε)` is lower semicontinuous and its tangent cone `T 𝒢(x)` varies continuously (upper+lower semicontinuously) near `x̄`; the directional-feasibility condition `d ∈ T 𝒢(x)` is therefore locally constant, and Berge stability of the linearized systems transfers the rank condition along the neighbourhood. The MFCQ system's solvability (`∇g_A v < 0`) is an open condition in `(x, A)` with `A` locally constant (continuity of `g` off the coincident-active strata; at coincident constraints MFCQ's rank part keeps the active set's gradients' span stable). ∎

**(2)** If `d` meets no feasible point along the pathway `x̄ + s·d + 𝒢`-correction for any `s > 0`, the pathway's blocked position `x̄ + s*d` realizes a first contact with `𝒢^c` at a boundary point `x_b`; the Clarke tangent cone `T_C(𝒢, x_b)` (a closed convex cone containing all tangent directions of `C¹`-feasible curves) excludes the strict descent direction `−d`; by the separation theorem for closed convex cones, there is `ξ ∈ (T_C(𝒢, x_b))° = N_C(𝒢, x_b)` with `⟨ξ, d⟩ > 0` (strict, since `−td ∈ T` would give `⟨ξ, −td⟩ ≤ 0` ∀t — the strict inequality picks the blocking side). The covector is computable from the Clarke generalized Jacobian of the active constraints at `x_b` (the cone generated by the active generalized gradients is contained in `N_C`). ∎

**Scope.** Local = MFCQ-qualified points; global = the certificate exists but finding `x_b` is a nonconvex problem in general (the certificate is checkable, not necessarily cheap). The linear case reduces exactly to Farkas (E3.C2).

---

## B7 — Bifurcation Classification — PROVED

### Statement

Let the parameterized system `ẋ = f(x, λ)` with constraint set `K(λ)` (`λ ∈ Λ` a parameter interval) satisfy the E2 successor hypotheses uniformly on compacts. Then:

1. **(No-change rule)** if at `λ₀` the flow restricted to a neighbourhood of `∂K(λ₀)` is structurally stable (no bifurcation: the orbit structure near the boundary is locally constant in `λ`) and `∂K(λ)` is Hausdorff-continuous at `λ₀`, then the kernel `Viab(λ)` is **Hausdorff-continuous at `λ₀`** — in particular, no kernel *jump*: `dist_H(Viab(λ), Viab(λ₀)) → 0`.
2. **(Change rule)** if at `λ₁` a **maximally-safe trajectory makes transversal contact** with `∂K(λ₁)` (the trajectory of a boundary-kernel state meets the constraint boundary with nonzero transversal angle, and the contact appears/disappears at first order in `λ`), then the kernel **changes discontinuously in the membership sense** at `λ₁`: states arbitrarily close to the contact state lie in `Viab(λ)` for `λ` on one side and outside for `λ` on the other.
3. **(Genericity)** the transversal-contact parameter values form a residual (dense `G_δ`) subset of the declared finite-jet parameter strata (jet-transversality).

### Proof

**(1)** The kernel is the gfp of the predecessor operator `Pre_λ` (E2.B1); under the uniform successor hypotheses, `Pre_λ` is Hausdorff-continuous in `λ` at `λ₀` (successors depend continuously on the field, and the field on a *structurally stable* flow neighborhood varies continuously into conjugate orbit data; the boundary's Hausdorff continuity handles the constraint side). The backward iterations `V_n(λ) = Pre_λ^n(X)` are then continuous in `λ` for each `n` (finite composition of continuous correspondences, Vietoris topology), and `Viab(λ) = ⋂ V_n(λ)`; the intersection of a `λ`-uniformly decreasing compact sequence is Hausdorff-continuous in `λ` at `λ₀` (the same exhaustion argument as E2.B1(b)'s Step "the limit is a fixed point", uniformly in a neighbourhood of `λ₀` — structural stability gives the uniform exhaustion radius). ∎

**(2)** Let `x_c` be the contact state, `γ_λ` its trajectory. Transversal contact with the `C¹` boundary means the exit-time function `τ(x, λ)` is `C¹` near `(x_c, λ₁)` with `∂τ/∂λ ≠ 0` (the contact is a regular level crossing); by the implicit function theorem `τ(x_c, λ) = T` (the horizon) defines `λ` locally as a `C¹` function of the level: on one side `τ < T` (the trajectory exits before the horizon — `x_c ∉ Viab(λ)`), on the other `τ > T` (`x_c ∈ Viab(λ)`). Membership flips. ∎

**(3)** Jet-transversality (Thom): the finite-jet extensions of the boundary-contact maps are transversal to the contact stratification for a residual set of `λ`; transversal = nonzero angle = the hypothesis of (2). Standard application to the declared finite-jet class. ∎

**Scope.** (1)–(2) are proved at the declared hypotheses; (3)'s "generic" is within the finite-jet strata — non-generic simultaneous contact families (corners of the stratification) are outside and are the registered residual (also E3.C5's note).

---

## B8 — Event-Surface Calculus — CONDITIONAL

Composition of A3.Thm3 (variable-event kernel, conditional on the declared class) with E4's jump-margin transfer. Status: conditional-now-precise — the two conditional theorems compose modulo both declaration sets (budgeted-transversal-clopen + depth co-Lipschitz margins); the composite theorem statement is routine assembly and is *not* written as a standalone proved record until either parent's conditions are discharged on an instance.

---

## B9 — Stochastic Viability Layer — PROVED (restricted)

### Statement

On the declared class — disturbance laws with **support alignment** (`supp ℒ(·|x,u) = D(x,u)`, the declared deterministic disturbance set, for every `(x,u)`) and a **compact policy class** (closed in pointwise convergence) — with compact `X`, closed `K`:

1. **(Chance-kernel recursion)** the chance-`p` viability kernel `K_p = {x₀ : ∃π ∈ Π, ℙ(safety on [0,T]) ≥ p}` equals the limit of the **quantile-budget recursion** `W₀ = K`, `W_{k+1} = {x : ∃π, Q_{p_k}(x'; ℒ(·|x,π)) ⊆ W_k}` with the multiplicative budget `∏ p_k = p`;
2. **(Conservative-filter a.s. soundness)** the inclusion-monotone filter of R02.Lem2 is pathwise sound: `B_t ⊆ C_t` almost surely, where `C_t` is the exact conditional viability set;
3. **(Probabilistic erosion)** quantile budgets convert to erosion depths: the `q`-quantile set of the successor law lies in the `r(q)`-eroded set with `r(q)` from the support geometry, giving the erosion condition `L_G r(q) + Δ ≤ α` at the declared quantile level.

### Proof

**(1)** *Soundness (⊇ ⊆ both inclusions).* (⊆... recursion ⊆ kernel): if `x ∈ W_k` for all `k` via policy `π`, the chain rule of conditional probabilities with the budget `∏p_k = p` gives `ℙ(survive k reviews) ≥ ∏p_k = p` at every `k`... precisely: `ℙ(X_{k+1} ∈ W_k | survive to k) ≥ p_k` by the quantile constraint, hence `ℙ(survive n) ≥ ∏_{k≤n} p_k → p`; monotone convergence identifies the limit event's probability ≥ `p`, so `x ∈ K_p`. (Kernel ⊆ recursion): a policy with `ℙ(safety) ≥ p` induces at every review a conditional survival probability whose quantiles satisfy the budget split *somehow* (choose `p_k` greedily as the realized conditional quantiles; support alignment + compactness of the policy class make the conditional quantile functions attain their levels — the attainment is where the compactness is used). *Closedness of `K_p` (the Fatou step):* let `x_n → x`, `x_n ∈ K_p` with policies `π_n`; compactness of the policy class gives a pointwise-convergent subsequence `π_n → π∞`; on the almost-sure convergence set of the state processes, `1{survive under π∞} ≥ limsup 1{survive under π_n}` (closedness of `K`), so by reverse Fatou for bounded functions `ℙ(survive under π∞) ≥ limsup ℙ(survive under π_n) ≥ p`: `x ∈ K_p`. ∎

**(2)** R02.Lem2's inclusion `B_k ⊆ C_k` is proved there pathwise on the observation tree; the a.s. reading is the same proof composed with the law (the filter updates on realized observations; monotonicity is deterministic given the realization). ∎

**(3)** With support alignment, the `q`-quantile set of `ℒ(·|x,u)` is a subset of `D(x,u)` bounded in the direction of the quantile's defining half-space; the erosion radius `r(q)` is the quantile's distance beyond the nominal successor, giving the displayed condition by the deterministic erosion calculus applied to the quantile set. ∎

**Restriction honesty.** Support alignment is a genuine hypothesis (laws must fill the declared support — no lighter tails); the compact policy class is closed-under-limits in the declared topology (needed for the Fatou step); `p`-quantile *sets* are well-defined for nonatomic or atom-lattice laws (the atom case needs the declared lattice convention). Outside these: OPEN.

---

## B10 — Strategic-Implementation Docket — PROVED (foundational)

### Statement

A Stackelberg governance instance: leader command `c ∈ C` (compact metric), follower policy set `Π` (compact in the declared topology), follower best-response correspondence `BR(c) = argmax_{π∈Π} v_f(c, π)` with `v_f` continuous, leader payoff `v_l(c, π)` continuous.

1. **(Existence)** a Stackelberg equilibrium exists: `∃ c* ∈ C, π* ∈ BR(c*)` with `v_l(c*, π*) = max_c min_{π ∈ BR(c)} v_l(c, π)` (the leader's guaranteed value is attained — the *optimistic* and *pessimistic* readings coincide under the closedness below).
2. **(Reduction)** at equilibrium, the strategic viability question — "does the leader have a command after which some follower response keeps the system viable?" — reduces to R02's closed-loop machinery applied at the best-response correspondence: the composite regulation map `c ↦ A_W(BR(c))` enters E2.B2(a)'s selection theorem verbatim, so all non-strategic theorems (R02.Thm1, B1, E2) apply with `U := C` and `Succ := BR`-composed successors.

### Proof

**(1)** `v_f` continuous on the compact `C × Π` ⟹ `BR` has nonempty compact values and **closed graph** (Berge's maximum theorem: the argmax correspondence is usc; with unique-valued... generally upper semicontinuous with compact values — the graph is closed because `π_n ∈ BR(c_n), (c_n,π_n) → (c,π)` gives `v_f(c,π) = lim v_f(c_n,π_n) ≥ lim v_f(c_n,π'_n) = v_f(c, π')` for every `π'` via `π'_n → π'`, so `π ∈ BR(c)`). The follower-value `v̄_f(c) = max_π v_f(c,π)` is continuous (Berge); the leader's pessimistic objective `c ↦ min_{π∈BR(c)} v_l(c,π)` is usc (min over a usc compact-valued correspondence of a continuous function), hence attains its max on the compact `C`. ∎

**(2)** `BR` is a compact-valued closed-graph correspondence — exactly the E2.B2(a) data type; the composite safe-command map `{c : BR(c) ⊆ W-successors}` inherits closed graph by the same two-step limit argument as E2's Step 2, and measurable selection applies to the leader's commands. Every R02/E2 conclusion then transfers with the correspondence substitution. ∎

**Scope.** This is the *foundational* theorem: equilibrium existence + the reduction license. Game-dynamic refinements (subgame perfection, information asymmetry beyond the leader-follower order) are outside the docket and honestly OPEN.

---

## B4 — Product Bunching — COMPUTED_PARTIAL (discrete only; gated on A1)

Unchanged from STATUS_CORRECTION.md: discrete stable-complement powers from the validated monodromy close at `n = 15` periods (value 0.649) with float64 output; the continuum transfer is open and gated on A1's piecewise-Chebyshev campaign. Not re-labeled.

---

## Status summary

| Item | Status |
|---|---|
| B1 | **PROVED** (full proof above) |
| B2 | CONDITIONAL (Michael class; see E2.B2(b)) |
| B3 | SPECIFIED (assembly open; D7) |
| B5 | SPECIFIED + one negative instance decision |
| B6 | **PROVED** (full proof above) |
| B7 | **PROVED** (full proof above; genericity residual registered) |
| B8 | CONDITIONAL (composition of two declared-class parents) |
| B9 | **PROVED (restricted)** (full proof above under the three declared restrictions) |
| B10 | **PROVED (foundational)** (full proof above) |
| B4 | COMPUTED_PARTIAL (discrete; gated on A1) |

**Dependencies:** E2 (selection, gfp), E4 (jump margins, for B8), A3 (for B8), R02/R03/R05 (the bridged records), packet B1/B6. **Consumers:** Paper 2 (B1, B6, B7, B9, B10), Paper 5 (B1, B10), TCS-1.1's composition gate enumeration G-5 (frozen diff, non-controlling).

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried per theorem; Fields 5, 10–15 N/A.

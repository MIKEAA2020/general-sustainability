# B-Tier Bridge Theorems — Consolidated Record

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Tasks 5–6; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). Independent line-by-line re-verification remains an open obligation.

---

## B1 — Sampled-Data Erosion Theorem — PROVEN (repaired: two-depth form)

> **Repair note (PROOF_REAUDIT finding 8; consolidated in `batch 4/PROOF_ELEVATION.md` Finding 8).** The recorded headline was ambiguous, and on its invariance reading **irreparably false**: with `K = [0,1]`, `r = 0.4`, `T_s = 1`, `V_max = 0.2`, sampled dynamics `x_{k+1} = min(x_k + 0.2, 0.8)` linear between samples, all three recorded hypotheses hold and `x₀ = 0.4 ∈ K_{−r}`, yet the sample states `0.4, 0.6, 0.8, 0.8, …` leave `K_{−r}` at `k = 2` while remaining in `K_{−r/2}` at samples and in `K` throughout. No nonzero sample period admits continuous-time invariance of an eroded set under these hypotheses (the two-depth theorem at `(R, r) = (R, R)` requires `V_max T_s ≤ 0`). The closing "verbatim" sentence required a successor certificate at depth `3r/2`, not supplied. The theorem below replaces the headline with a **two-depth statement** that separates the certified depth from the safety depth; the recorded *proved* content is the special case `(R, r) = (r_rec/2, 0)`. Full development and verification: `batch 4/B1_THM1_REPAIRED.md`.

### Statement

Let `K ⊆ ℝⁿ` be closed, and let `R > r ≥ 0` be two erosion depths. Let the closed-loop system run under a sampled policy with sample period `T_s`, sampled states `x_k := x(t_k)`, `t_k = kT_s`. Assume:

1. **(Envelope inclusion)** the inter-sample trajectory satisfies `x(t) ∈ B̄(x_k, ρ)` for `t ∈ [t_k, t_{k+1})`, with envelope radius `ρ ≤ V_max T_s` (`V_max` the closed-loop speed bound on the relevant compact set);
2. **(Confinement)** `V_max · T_s ≤ R − r`;
3. **(Successor certificate at depth `R`)** the sampled successor map carries `K_{−R}` into `K_{−R}`: `x_{k+1} ∈ K_{−R}` whenever `x_k ∈ K_{−R}`.

**Then, for every trajectory with `x₀ ∈ K_{−R}`: (a) `x_k ∈ K_{−R}` at every sample time — sample-time invariance at the certified depth; (b) `x(t) ∈ K_{−r}` for every `t` — continuous-time safety at depth `r`.**

The confinement bound is **tight**: an inter-sample excursion of `V_max T_s` from a point at depth exactly `R` reaches depth `R − V_max T_s`, which stays above `r` iff `V_max T_s ≤ R − r`. The sample-period budget is explicit: `T_s ≤ (R − r)/V_max`.

### Proof

**(a)** Induction over samples with base `x₀ ∈ K_{−R}` and step hypothesis 3. **(b)** For `t ∈ [t_k, t_{k+1})`, the triangle inequality for the distance to the closed set `K^c` gives `dist(x(t), K^c) ≥ dist(x_k, K^c) − ‖x(t) − x_k‖ ≥ R − V_max T_s ≥ R − (R − r) = r`, using (a) at `t_k`, hypothesis 1, and hypothesis 2. At the sample times themselves `x_k ∈ K_{−R} ⊆ K_{−r}` since `R > r`. ∎

**Corollary (the closed R02.Cor6 bridge).** Suppose packet Lemma 2's hypotheses hold for `K` (two-sided tubular radius `ρ`, envelope modulus `L_G`, boundary margin `α`, implementation/model error budget `Δ`), and the sampled loop satisfies hypothesis 1. If `L_G R + Δ ≤ α`, `0 < R < ρ`, `K_{−R} ≠ ∅`, and `V_max T_s ≤ R − r`, then every sampled trajectory from `K_{−R}` is safe at depth `r` in continuous time. Lemma 2's strong invariance of `K_{−R}` supplies hypothesis 3 at depth `R`; the corollary is the bridge with explicit depth bookkeeping. The residual conditions are model-level (verification of `L_G R + Δ ≤ α` and `V_max T_s ≤ R − r` on an instance — the empirical NOT CONFIRMED gate is untouched).

**Honesty notes.** Hypothesis 1 is implied by 2 on compacts; stating both keeps the certificate chain explicit. The recorded content ("`K_{−r/2}` forward-invariant at sample times; every inter-sample trajectory remains in `K`") is the case `(R, r) = (r_rec/2, 0)` and is recovered verbatim. The invariance reading ("`K_{−r}` is safe" as `x(t) ∈ K_{−r}` for all `t` from `K_{−r}` initials) is **withdrawn** — refuted by the counterexample above. Sample-period selection is now a one-line corollary (`T_s ≤ (R − r)/V_max`), which is what a governance-design paper needs: the certificate depth you can afford to lose per sample is exactly the drift budget.

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

## B6 — Nonlinear Substitution Classification — PROVEN (repaired)

### Statement

Let the constraint system be `g(x) = (g_1, …, g_p) : ℝⁿ → ℝᵖ`, `C¹`, feasible region `𝒢 = {g ≤ 0}`, and let the substitution question be: *does the direction `d ∈ ℝⁿ` (compensating moiety `i`'s deficit with `j`'s surplus along the declared pathway) meet `𝒢` arbitrarily near the contact point `x̄` with `g(x̄) = 0` on the active set?*

> **Repair note (PROOF_REAUDIT finding 2; consolidated in `batch 4/PROOF_ELEVATION.md` Finding 2).** Part (1) as recorded is **false**: on `𝒢 = {y ≥ x²}`, `x̄ = (0,0)`, `d = (1,0)`, MFCQ holds at every point (`∇g = (2a, −1) ≠ 0`) yet `d` is a feasible direction at `x̄` and at no nearby boundary point — and the failure is robust to *every* strengthening of the MFCQ data (with witness `v̄ = (0,1)`, `⟨∇g, v̄⟩ = −1` at every point of the parabola with the same constant `γ = 1` and 2-Lipschitz `∇g`). The recorded part (2) additionally had the **blocking direction's sign wrong**: on the same witness `−d = (−1, 0)` lies in `T_C` at every point, so the recorded hypothesis is false on the theorem's own example — the blocking direction is `d`, not `−d`. Both parts are replaced below; neither is weakened. Full development and verification: `batch 4/B6_THM1_REPAIRED.md`.

1. **(Quantitative stability under MFCQ).** Let `g ∈ C^{1,1}` near `x̄` with `∇g` `L`-Lipschitz, and let MFCQ hold at `x̄` with witness `v̄` (`‖v̄‖ ≤ 1`) and constant `γ > 0`. Put `U = {‖x − x̄‖ < γ/(2L)}`. Then for every `x ∈ 𝒢 ∩ U`:
   - **(a)** `A(x) ⊆ A(x̄)`; MFCQ holds at `x` with the same witness `v̄` and constant `γ/2`; and Abadie's constraint qualification holds, so `T_𝒢(x) = {v : ⟨∇g_k(x), v⟩ ≤ 0, k ∈ A(x)}`;
   - **(b)** **quantitative lower semicontinuity:** for every `d ∈ T_𝒢(x̄)` there exists `d_x ∈ T_𝒢(x)` with `‖d_x − d‖ ≤ (2L/γ)·‖x − x̄‖·‖d‖` (take `d_x = d + t v̄` with `t = (2L/γ)‖x − x̄‖‖d‖`) — the linear rate is sharp in order (closed form `2a/√(4a²+1)` on the witness);
   - **(c)** **exact constancy at the sharp hypothesis:** if `d` is *strictly* feasible at `x̄` (`⟨∇g_k(x̄), d⟩ < 0` for every `k ∈ A(x̄)`), then `d ∈ T_𝒢(x)` for every `x ∈ 𝒢` sufficiently close to `x̄`, with no modulus and no approximation; this fails for weakly feasible directions (the witness's `d = (1,0)`) — sharpness;
   - **(d)** upper semicontinuity of `x ↦ T_𝒢(x)` **fails** in general;
   - **(e)** **ray form (A1's ray lemma):** if `d` is strictly feasible at `x̄` — `η := min_{k∈A(x̄)}(−⟨∇g_k(x̄), d⟩) > 0` — then `x̄ + t·d ∈ int 𝒢` for every `t ∈ (0, t*]`, with `t*` explicit: any value with `ω(t*) ≤ η/2` inside a ball on which `ω` is a modulus for `∇g` and the inactive constraints remain inactive (`r_in`; for `Λ`-Lipschitz `∇g`, `t* = min(r_in, η/(2Λ))`). So `d` is **ray-feasible** at `x̄` — and remains so at every feasible point of the (c)-stability ball.
   No claim of locally-constant projection of `𝒢` is made (false on the witness).
2. **(Global separation via Clarke, corrected hypothesis).** Let `x_b ∈ 𝒢` be a blocking point at which

```
d ∉ T_C(𝒢, x_b)        (BLK)
```

— the blocking direction is `d` itself (not `−d`). Then there exists `ξ ∈ N_C(𝒢, x_b)` with

```
⟨ξ, d⟩ > 0  ≥  sup{ ⟨ξ, w⟩ : w ∈ T_C(𝒢, x_b) },
```

an explicit **noncompensability certificate**; under MFCQ at `x_b`, `N_C(𝒢, x_b) = {Σ_{k∈A(x_b)} λ_k ∇g_k(x_b) : λ_k ≥ 0}`, so the certificate has explicit nonnegative multipliers. For affine `g` this reduces exactly to the homogeneous Farkas alternative (a single active row certifies: `ξ = a_i` with `a_i·d > 0`).

### Proof

**(1)(a)** Let `x ∈ 𝒢 ∩ U` and `k ∈ A(x)`: `g_k(x) = 0` gives `g_k(x̄) = 0` by continuity, so `A(x) ⊆ A(x̄)`; then `⟨∇g_k(x), v̄⟩ ≤ −γ + L‖x − x̄‖ ≤ −γ/2` — MFCQ at `x` with data `(v̄, γ/2)`. MFCQ implies Abadie, giving the cone identity. **(b)** For `d ∈ T_𝒢(x̄)` (so `⟨∇g_k(x̄), d⟩ ≤ 0` on `A(x̄)` by Abadie at `x̄`), set `t = (2L/γ)‖x − x̄‖‖d‖` and `d_x = d + t v̄`: for `k ∈ A(x) ⊆ A(x̄)`, `⟨∇g_k(x), d_x⟩ ≤ [⟨∇g_k(x̄), d⟩ + L‖x − x̄‖‖d‖] + t·(−γ/2) = 0`, so `d_x ∈ T_𝒢(x)` by Abadie at `x`, and `‖d_x − d‖ ≤ t`. **(c)** With `η := min_{k∈A(x̄)}(−⟨∇g_k(x̄), d⟩) > 0`: `⟨∇g_k(x), d⟩ ≤ −η + L‖x − x̄‖‖d‖ < 0` whenever `‖x − x̄‖ < η/(L‖d‖)`. **(d)** In the witness, `w = (−1, −½) ∈ T_𝒢((a, a²))` for `a ≥ ¼` but `w ∉ T_𝒢(x̄)`. **(e)** For `k ∈ A(x̄)` and `t ∈ (0, t*]`: `g_k(x̄ + td) = ∫₀ᵗ(⟨∇g_k(x̄), d⟩ + ⟨∇g_k(x̄ + sd) − ∇g_k(x̄), d⟩) ds ≤ t(−η + ω(t)) ≤ −(η/2)t < 0`, while the inactive `g_j` stay negative by the choice of `r_in`; hence `x̄ + td ∈ int 𝒢`. The same computation at any `x` of the (c)-ball uses `η(x, d) ≥ η/2`. ∎

**(2)** `T := T_C(𝒢, x_b)` is a closed convex cone; by (BLK), `d ∉ T`. Strict separation of a point from a closed convex set gives `ξ₀` and `α` with `⟨ξ₀, d⟩ < α ≤ ⟨ξ₀, w⟩` for all `w ∈ T`. Since `0 ∈ T`, `α ≤ 0`; since `T` is a cone, `t·w ∈ T` for all `t > 0` forces `⟨ξ₀, w⟩ ≥ 0`. Hence `⟨ξ₀, d⟩ < 0`; set `ξ := −ξ₀ ∈ T° = N_C(𝒢, x_b)`, giving `⟨ξ, d⟩ > 0` and `sup_T ⟨ξ, ·⟩ ≤ 0`. The multiplier representation is the standard consequence of Abadie plus the Clarke calculus under MFCQ; the affine reduction is immediate (a violating row certifies). ∎

**Scope and reading.** Local = MFCQ-qualified points; global = the certificate exists (unconditionally given (BLK)) but finding `x_b` is a nonconvex problem in general (checkable, not necessarily cheap). The linear case reduces exactly to Farkas (E3.C2). The recorded proof conflated **tangential feasibility** (`d ∈ T_𝒢(x̄)`: feasible curves with tangent `d`, possibly leaving the ray) with **ray feasibility** (`x̄ + sd ∈ 𝒢` for small `s`): on the witness, `d = (1,0)` is in `T_𝒢(x̄) = {v : v₂ ≥ 0}` yet the ray `(s, 0)` leaves `𝒢` immediately (`0 < s²`). Downstream consumers must say which they mean; E3.C2/E7.Thm2 consume the *strict local alternative* and the linear case, both intact. By (e), strictly-feasible directions are not only tangentially stable (c) but **ray**-feasible with an explicit radius — the substitution direction that strictly pays a deficit enters `𝒢` along the ray itself, not merely along curved tangents; grazing directions do neither, and no MFCQ strengthening rescues them.

---

## B7 — Bifurcation Classification — PROVED

### Statement

Let the parameterized system `ẋ = f(x, λ)` with constraint set `K(λ)` (`λ ∈ Λ` a parameter interval) satisfy the E2 successor hypotheses uniformly on compacts. Then:

1. **(No-change rule)** if at `λ₀` the flow restricted to a neighbourhood of `∂K(λ₀)` is structurally stable (no bifurcation: the orbit structure near the boundary is locally constant in `λ`) and `∂K(λ)` is Hausdorff-continuous at `λ₀`, then the kernel `Viab(λ)` is **Hausdorff-continuous at `λ₀`** — in particular, no kernel *jump*: `dist_H(Viab(λ), Viab(λ₀)) → 0`.
2. **(Change rule)** if at `λ₁` a **maximally-safe trajectory makes transversal contact** with `∂K(λ₁)` (the trajectory of a boundary-kernel state meets the constraint boundary with nonzero transversal angle, and the contact appears/disappears at first order in `λ`), then the kernel **changes discontinuously in the membership sense** at `λ₁`: states arbitrarily close to the contact state lie in `Viab(λ)` for `λ` on one side and outside for `λ` on the other.
3. **(Genericity, under a versal unfolding)** *if the family `λ ↦ (f(·,λ), K(λ))` is a `C^r` versal unfolding of the boundary-contact geometry at `λ₁`* (equivalently, its jet-extension map `λ ↦ j^k(f, ∂K)` is transverse to the tangency stratification of the contact jet space), *then* the transversal-contact parameter values form a residual (dense `G_δ`) subset of the parameter stratum. Without versality the conclusion **fails**: for `f ≡ 0`, `K = [−1,1]`, every `λ` gives tangential contact (the transversal-contact set is empty, not residual).

### Proof

**(1)** The kernel is the gfp of the predecessor operator `Pre_λ` (E2.B1); under the uniform successor hypotheses, `Pre_λ` is Hausdorff-continuous in `λ` at `λ₀` (successors depend continuously on the field, and the field on a *structurally stable* flow neighborhood varies continuously into conjugate orbit data; the boundary's Hausdorff continuity handles the constraint side). The backward iterations `V_n(λ) = Pre_λ^n(X)` are then continuous in `λ` for each `n` (finite composition of continuous correspondences, Vietoris topology), and `Viab(λ) = ⋂ V_n(λ)`. The last step requires the exhaustion to be **uniform on a neighbourhood `U` of `λ₀`**: `sup_{λ∈U} d_H(V_n(λ), Viab(λ)) → 0`. This uniform exhaustion radius is an explicit *hypothesis* of the no-change rule (named per the reaudit; structural stability supplies it when the conjugacy modulus and boundary variation are themselves uniform on `U` — an implication used here as declared, not derived). Under it the intersection is Hausdorff-continuous in `λ` at `λ₀`. ∎

**(2)** Let `x_c` be the contact state, `γ_λ` its trajectory. Transversal contact with the `C¹` boundary means the exit-time function `τ(x, λ)` is `C¹` near `(x_c, λ₁)` with `∂τ/∂λ ≠ 0` (the contact is a regular level crossing); by the implicit function theorem `τ(x_c, λ) = T` (the horizon) defines `λ` locally as a `C¹` function of the level: on one side `τ < T` (the trajectory exits before the horizon — `x_c ∉ Viab(λ)`), on the other `τ > T` (`x_c ∈ Viab(λ)`). Membership flips. ∎

**(3)** Thom's jet-transversality theorem is a statement about a **space of maps**: for a residual set of `C^k` maps (Whitney topology), the jet extension is transverse to a given stratification. To conclude that a residual set of *parameters* `λ` in a *fixed* family gives transversal contact, the family must realise that function space — a **versal unfolding** (the transversality of the jet-extension map `λ ↦ j^k(f, ∂K)` to the tangency stratification). Under the versality hypothesis, Thom applied to the jet-extension map gives transversality for a residual set of `λ`; transversality to the tangency stratum is exactly "nonzero contact angle", the hypothesis of (2). Without versality the conclusion fails (the `f ≡ 0` family satisfies every other recorded hypothesis and has an empty transversal-contact set; the contrasting versal family `f = λ` is transversal for every `λ ≠ 0` with the single-point exceptional set `{0}`). Equivalently: for a residual set of `C^k` *families* the contact set is empty or transversal — an unfolding-level statement (3a); for a *fixed* family, transversality at `λ₁` is a hypothesis of (2), not a conclusion (3b). ∎

**Scope.** (1)–(2) are proved at the declared hypotheses — (1) now with the uniform exhaustion radius named as a hypothesis; (3) is **conditional on versality** (narrowed per the reaudit finding 19 and `batch 4/PROOF_ELEVATION.md` Finding 19 — no strengthening is available: the `f ≡ 0` family satisfies every other recorded hypothesis). Within the finite-jet strata, non-generic simultaneous contact families (corners of the stratification) remain outside and registered (also E3.C5's note).

---

## B8 — Event-Surface Calculus — CONDITIONAL

Composition of A3.Thm3 (variable-event kernel, conditional on the declared class) with E4's jump-margin transfer. Status: conditional-now-precise — the two conditional theorems compose modulo both declaration sets (budgeted-transversal-clopen + depth co-Lipschitz margins); the composite theorem statement is routine assembly and is *not* written as a standalone proved record until either parent's conditions are discharged on an instance.

---

## B9 — Stochastic Viability Layer — PROVEN (restricted; repaired)

### Statement

On the declared class — disturbance laws with **support alignment** (`supp ℒ(·|x,u) = D(x,u)`, the declared deterministic disturbance set, for every `(x,u)`) and a **compact policy class** (closed in pointwise convergence) — with compact `X`, closed `K`:

1. **(Chance-kernel characterisation — repaired).** The chance-`p` viability kernel `K_p = {x₀ : ∃π ∈ Π, ℙ(safety on [0,T]) ≥ p}` is characterised **exactly** by the value iteration `V₀ = 1_K`, `V_{k+1}(x) = sup_{π∈Π} ∫ V_k(y) ℒ(dy|x,π)`: `K_p = {x : V_N(x) ≥ p}` (ordinary dynamic programming for the joint chance constraint — no quantile convention needed). The **quantile-budget recursion** `W₀ = K`, `W_{k+1} = {x : ∃π, Q_{p_k}(x'; ℒ(·|x,π)) ⊆ W_k}` is a **sound lower bound** at any fixed budget split `∏ p_k = p`: `∩_k W_k ⊆ K_p`. The recorded equality at a fixed split is **false** (refuted below), and so is completeness over splits: there are models with `x ∈ K_p` lying in no split's `∩_k W_k`. The exact quantile-form recursion is the **residual-budget DP**: `V_k(x, q) = 1` iff `x ∈ K` and `∃u ∃` measurable `r : X → [0,1]` with `𝔼[r(X′)|x,u] ≥ q` and `V_{k+1}(y, r(y)) = 1` a.e.; then `x ∈ K_p ⟺ V₀(x, p) = 1` — the budget becomes state-dependent, which is what mixture witnesses demand. At `p = 1` under support alignment this reduces to the robust predecessor `{x : ∃u, D(x,u) ⊆ K}`, complete;
2. **(Conservative-filter a.s. soundness)** the inclusion-monotone filter of R02.Lem2 is pathwise sound: `B_t ⊆ C_t` almost surely, where `C_t` is the exact conditional viability set;
3. **(Probabilistic erosion)** quantile budgets convert to erosion depths: the `q`-quantile set of the successor law lies in the `r(q)`-eroded set with `r(q)` from the support geometry, giving the erosion condition `L_G r(q) + Δ ≤ α` at the declared quantile level.

### Proof

**(1)** *Value iteration (exact).* Induction: `V_N(x) = sup_π ℙ(X₁,…,X_N ∈ K | x)` by the Markov property and the tower rule; the optimal Markov policy exists by compactness of `Π` (or measurable selection), so the sup is attained and `K_p = {V_N ≥ p}`. *Soundness of any fixed split:* if `x ∈ ∩_k W_k` via policy `π`, the chain rule with `ℙ(X_{k+1} ∈ W_k | survive to k) ≥ p_k` (implied by the quantile-set constraint) iterates to `ℙ(survive) ≥ ∏ p_k = p`. *Incompleteness (refutation of the recorded equality):* states `{x, y₁, y₂}`, `K = {x, y₁, y₂}` ∪ {safe terminal}, one policy, `x → y₁` or `y₂` w.p. `½` each, `ℙ(X₂ ∈ K | y₁) = 0.2`, `ℙ(X₂ ∈ K | y₂) = 0.8`: then `ℙ(survive | x) = ½·0.2 + ½·0.8 = 0.5` so `x ∈ K_{1/2}`, but for **every** split `t_init·t_term = ½`: `t_term ≤ 0.2` forces `t_init ≥ 2.5 > 1` (invalid); `0.2 < t_term ≤ 0.8` gives `W₁ = {y₂}`, `ℙ(X₁ ∈ W₁ | x) = ½`, requiring `t_init ≤ ½` while `t_init = ½/t_term ≥ 0.625` (contradiction); `t_term > 0.8` gives `W₁ = ∅`. So `x` lies in no split's recursion limit — the recorded reverse inclusion is false, and the failure is the *uniform-vs-average* gap: the recursion demands a uniform per-state conditional bound, `K_p` constrains only the average. The residual-budget DP closes the gap exactly by tracking the remaining budget as a state (proof by induction on the budget variable, forward and reverse). *Closedness of `K_p` (the Fatou step, retained):* let `x_n → x`, `x_n ∈ K_p` with policies `π_n`; compactness of the policy class gives a pointwise-convergent subsequence `π_n → π∞`; on the almost-sure convergence set, `1{survive under π∞} ≥ limsup 1{survive under π_n}` (closedness of `K`), so by reverse Fatou `ℙ(survive under π∞) ≥ limsup ℙ(survive under π_n) ≥ p`. ∎

**(2)** R02.Lem2's inclusion `B_k ⊆ C_k` is proved there pathwise on the observation tree; the a.s. reading is the same proof composed with the law (the filter updates on realized observations; monotonicity is deterministic given the realization). ∎

**(3)** With support alignment, the `q`-quantile set of `ℒ(·|x,u)` is a subset of `D(x,u)` bounded in the direction of the quantile's defining half-space; the erosion radius `r(q)` is the quantile's distance beyond the nominal successor, giving the displayed condition by the deterministic erosion calculus applied to the quantile set. ∎

**Restriction honesty.** Support alignment is a genuine hypothesis (laws must fill the declared support — no lighter tails); the compact policy class is closed-under-limits in the declared topology (needed for the Fatou step); `p`-quantile *sets* are well-defined for nonatomic or atom-lattice laws (the atom case needs the declared lattice convention — part (3) consumes quantile sets and now says so in the statement rather than a footnote). Outside these: OPEN. **Withdrawn:** the fixed-split (and split-union) equality of part (1) — refuted by the explicit witnesses above; see `batch 4/PROOF_ELEVATION.md` Finding 9 (with the numerical adjudication of the split-completeness claim).

---

## B10 — Strategic-Implementation Docket — PROVEN (repaired)

> **Repair note (PROOF_REAUDIT findings 10–11; consolidated in `batch 4/PROOF_ELEVATION.md` Findings 10–11, with the numerical adjudication of the semicontinuity dispute).** The recorded (1) claimed the pessimistic objective is usc and attains its max, and that the optimistic and pessimistic readings coincide — the first is **false** (`ψ` is *lower* semicontinuous; `sup ψ` need not be attained), the second needs a hypothesis. The recorded (2) claimed closed-graph inheritance for the *universal* safe-command set — **false** under Berge alone. Both are replaced below without weakening what survives: optimistic existence and the existential reduction are unconditional; pessimistic existence and the universal reduction carry named extra hypotheses. Full development and verification: `batch 4/B10_THM1_REPAIRED.md` (root copy, with the erratum of §I.3 applied).

### Statement

A Stackelberg governance instance: leader command `c ∈ C` (compact metric), follower policy set `Π` (compact in the declared topology), follower best-response correspondence `BR(c) = argmax_{π∈Π} v_f(c, π)` with `v_f` continuous, leader payoff `v_l(c, π)` continuous. Write `V_opt = max_c max_{π∈BR(c)} v_l(c,π)` (optimistic) and `V_pes = max_c min_{π∈BR(c)} v_l(c,π)` (pessimistic/robust); for closed `F ⊆ Π` write `E_F = {c : BR(c) ∩ F ≠ ∅}` (existential) and `U_F = {c : BR(c) ⊆ F}` (universal).

1. **(Existence, split).** (a) `BR` has nonempty compact values and closed graph; the optimistic value `V_opt` is attained. (b) The pessimistic objective `ψ(c) = min_{π∈BR(c)} v_l(c,π)` is **lower** semicontinuous and attains its *minimum*; `V_pes` need **not** be attained (witness: `C = [0,1]`, `v_f(c,b) = c−1`, `v_l(c,a) = c`, `v_l(c,b) = 0` — `BR(c) = {a}` for `c < 1`, `BR(1) = {a,b}`, `ψ(c) = c` for `c < 1`, `ψ(1) = 0`, so `sup ψ = 1` is not attained). (c) If `BR` is additionally lower semicontinuous, or single-valued, or `v_l(c,·)` is constant on `BR(c)`-fibres, then `ψ` is usc/continuous and a pessimistic Stackelberg pair exists (with `π*` attaining the inner minimum, `v_l(c*,π*) = V_pes`). Sufficient for all at once: `Π` compact convex and `v_f(c,·)` strictly concave. (d) `V_pes ≤ V_opt`, with equality iff `v_l(c*_opt, ·)` is constant on `BR(c*_opt)` — the gap `V_opt − V_pes` is the **price of follower non-uniqueness**, a governance quantity, not an artefact.
2. **(Reduction, split by quantifier).** For closed `Safe ⊆ Π`: the **existential** set `E_Safe = {c : BR(c) ∩ Safe ≠ ∅}` — the recorded question's actual form ("some follower response keeps the system viable") — is **closed under Berge alone** (it is the level set `{c : max_{π∈Safe} v_f(c,π) = v̄_f(c)}`), and KRN selection yields a measurable viable-response selection. The **universal** set `U_Safe` is generally open and is closed iff `BR` is lower semicontinuous. **Reduction license:** E2.B2(a) measurable selection and B1 (two-depth) transfer via `E_Safe` under Berge alone; `R02.Thm1` (an all-branches theorem) transfers only via `U_Safe`, hence requires `BR` lower semicontinuous. The recorded "all non-strategic theorems apply with `U := C`" is withdrawn as inflation.

### Proof

**(1)(a)** Closed graph of `BR`: if `π_n ∈ BR(c_n)` and `(c_n,π_n) → (c,π)`, then for every `π'`, `v_f(c,π) = lim v_f(c_n,π_n) ≥ lim v_f(c_n,π') = v_f(c,π')`, so `π ∈ BR(c)`. `φ(c) = max_{BR(c)} v_l` is usc (usc correspondence + compact values + continuous integrand: take maximising selections, pass to the graph limit) and attains its max on compact `C`. **(b)** The same argument with *minimising* selections gives `liminf ψ(c_n) ≥ ψ(c)` — ψ is lsc; the witness shows non-attainment (`BR` is usc there: values jump *up* at `1`). **(c)** Under the extra hypotheses ψ is usc (or continuous), so attains its max; the displayed pair takes `π*` attaining the inner min. **(d)** Trivially `V_pes ≤ V_opt`; equality forces the leader value to be constant on the optimal fibre, and conversely. ∎

**(2)** `E_F` closed: if `c_n → c` with `π_n ∈ BR(c_n) ∩ F`, compactness gives `π_{n_k} → π ∈ F` and the closed graph gives `π ∈ BR(c)`. `U_F` is the strict sublevel set `{c : v_f(c,π) < v̄_f(c) ∀π ∉ F}` — open; closedness under lsc `BR`: for `c_n → c` with `BR(c_n) ⊆ F` and any `x ∈ BR(c)`, lower semicontinuity makes every neighbourhood of `x` meet `BR(c_n) ⊆ F` for large `n`, so `x ∈ F`. The license table follows (E2.B2(a) needs the existential set; R02.Thm1's universal quantifier over implementation branches needs `U_Safe`). ∎

**Scope.** The *foundational* content survives at the corrected hypotheses: optimistic existence + existential reduction unconditionally; pessimistic existence and the all-branches license under the named extra hypotheses. Game-dynamic refinements (subgame perfection, information asymmetry beyond the leader-follower order) remain outside the docket and honestly OPEN.

---

## B4 — Product Bunching — COMPUTED_PARTIAL (discrete only; gated on A1)

Unchanged from STATUS_CORRECTION.md in status; **figure updated per `batch 4/CROSS_DOCUMENT_CONSISTENCY.md` C6**: the discrete stable-multiplier-only closure at `n = 15` periods (value 0.649) is superseded by the prefactor-aware product assessment — `research_program/article_A021_liebig_graph/product_prefactor_bunching_assessment.md` concludes the numerical `C1` product bunching inequality closes only marginally at 30 periods but **robustly by 35 periods** (`NUMERICALLY_VERIFIED_DISCRETE_PRODUCT_BUNCHING_AT_35_PERIODS`; "the stable multiplier alone cannot establish bunching"; not a continuum operator bound). Float64 output; the continuum transfer remains open and gated on A1's piecewise-Chebyshev campaign. Not re-labeled (`COMPUTED_PARTIAL` stands — the assessment's own status agrees).

---

## Status summary

| Item | Status |
|---|---|
| B1 | **PROVEN (repaired: two-depth form)** (full proof above; invariance reading withdrawn) |
| B2 | CONDITIONAL (Michael class; see E2.B2(b)) |
| B3 | SPECIFIED (assembly open; D7) |
| B5 | SPECIFIED + one negative instance decision |
| B6 | **PROVEN (repaired)** (full proof above; quantitative (1) incl. the ray lemma (e), (BLK)-hypothesised (2) with the blocking-direction sign corrected) |
| B7 | **PROVEN** ((1),(2) with the uniform-exhaustion hypothesis named; (3) **conditional on versality**) |
| B8 | CONDITIONAL (composition of two declared-class parents) |
| B9 | **PROVEN (restricted; repaired)** (exact V-iteration + residual-budget DP; fixed-split equality withdrawn) |
| B10 | **PROVEN (repaired)** (optimistic + existential reduction unconditional; pessimistic + universal conditional) |
| B4 | COMPUTED_PARTIAL (discrete; gated on A1) |

**Dependencies:** E2 (selection, gfp), E4 (jump margins, for B8), A3 (for B8), R02/R03/R05 (the bridged records), packet B1/B6. **Consumers:** Paper 2 (B1, B6, B7, B9, B10), Paper 5 (B1, B10), TCS-1.1's composition gate enumeration G-5 (frozen diff, non-controlling).

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried per theorem; Fields 5, 10–15 N/A.

# B6.Thm1 — Nonlinear Substitution Classification: REPAIRED

**Replaces:** the `B6` section of `batch 2/04_open_problems/B_TIER_BRIDGES.md`, and the manifest row `B6.Thm1 | PROVEN (reconstructed)` in `PROOF_MANIFEST.md` line 96.

**Disposition.** Part (1)'s stability claim is **false as stated** and is replaced. Part (2)'s conclusion was correct but its hypothesis was never stated precisely; it is now stated and proved cleanly. Neither part is weakened: part (1) is replaced by a **quantitative** theorem with an explicit modulus plus an **exact** local-constancy statement at the sharp hypothesis, and part (2) gains an explicit multiplier representation.

**Net change vs. the original.** Strictly stronger in four ways: (i) part (1) carries an explicit Lipschitz modulus `(2L/γ)‖x−x̄‖‖d‖` where the original asserted an unqualified equality; (ii) the exact local-constancy statement is recovered at its sharp hypothesis (strict feasibility); (iii) sharpness is proved — the failure of the original "iff" is shown to be robust to *any* strengthening of the MFCQ data; (iv) part (2)'s certificate is exhibited with explicit multipliers, reducing to Farkas in the affine case.

**Verification.** `reaudit/verify_b6_repair.py`, 31 assertions, exit 0. Output: `reaudit/b6_output.txt`.

---

## 0. What was false, and why it cannot be repaired in place

**Original part (1).** "If at every `x` in a neighbourhood of `x̄` with active set `A(x)`, the active gradients satisfy MFCQ, then the feasible-direction property is **stable**: `d` is a feasible direction at `x̄` **iff** it is at every nearby `x`, and the projection of `𝒢` onto the pathway coordinate is locally constant."

**Refutation.** `𝒢 = {(x,y) : y ≥ x²}`, i.e. `g(x,y) = x² − y ≤ 0`; `x̄ = (0,0)`; `d = (1,0)`.

| point | `∇g` | `⟨∇g, d⟩` | `d ∈ T_𝒢`? | MFCQ? |
|---|---|---|---|---|
| `(0,0)` | `(0,−1)` | `0` | **yes** | yes |
| `(a, a²)`, `a > 0` | `(2a, −1)` | `2a > 0` | **no** | yes |

MFCQ holds at `x̄` and at every nearby boundary point, yet `d` is feasible at `x̄` and at none of them.

**The failure is robust — this is why the claim is irreparable in place.** The MFCQ data do not degenerate along the sequence. With witness `v̄ = (0,1)`,

```
⟨∇g(x), v̄⟩ = −1     at every point of the parabola,
```

so MFCQ holds on a whole neighbourhood with the *same* witness and the *same* constant `γ = 1`, and `∇g` is `2`-Lipschitz throughout. No strengthening of the MFCQ hypothesis — uniformity, a positive MFCQ constant, Lipschitz gradients, `C^∞` data — repairs the "iff". The obstruction is not weak constraint qualification; it is that **a weakly feasible direction can be feasible at one point and infeasible at nearby points on the same smooth stratum**, because the linearized cone rotates with `x`.

The only hypothesis that does restore exact constancy is a condition on `d`, not on the constraints: strict feasibility. That is part (1c) below.

**The conceptual source of the error.** The original conflated two different notions:

- **tangential feasibility**, `d ∈ T_𝒢(x̄)`: there are feasible curves through `x̄` with tangent `d` — the curves may leave the ray;
- **ray feasibility**, `x̄ + sd ∈ 𝒢` for small `s > 0`: much stronger.

In the witness, `d = (1,0)` **is** in `T_𝒢(x̄) = {v : v_2 ≥ 0}`, yet the ray `(s, 0)` leaves `𝒢` immediately, since `0 < s²` for every `s > 0` (verified at `s = 0.5, 0.1, 0.01, 0.001`). A tangent cone controls infinitesimal feasibility along *perturbed* paths, not along the exact ray. Any stability statement about "the feasible-direction property" must say which of the two it means.

---

## 1. Setup and notation

`g : ℝⁿ → ℝᵖ` of class `C^{1,1}` on a neighbourhood of `x̄`, with `∇g` **L**-Lipschitz there. `𝒢 := {x : g(x) ≤ 0}`, `A(x) := {k : g_k(x) = 0}`. `T_𝒢(x)` is the Bouligand contingent cone, `T_C(𝒢,x)` the Clarke tangent cone, `N_C(𝒢,x) := (T_C(𝒢,x))^∘` the Clarke normal cone.

**MFCQ data at `x̄`.** A witness `v̄` with `‖v̄‖ ≤ 1` and a constant `γ > 0` with

```
⟨∇g_k(x̄), v̄⟩ ≤ −γ      for all k ∈ A(x̄).                                    (MFCQ)
```

---

## 2. Part (1) repaired — quantitative stability of feasible directions

> ### B6.Thm1(1) (repaired)
>
> Suppose (MFCQ) holds at `x̄` with data `(γ, v̄)` and `∇g` is `L`-Lipschitz near `x̄`. Put
> `U := {x : ‖x − x̄‖ < γ/(2L)}`. Then:
>
> **(a) MFCQ propagates, and Abadie holds.** For every `x ∈ 𝒢 ∩ U`, `A(x) ⊆ A(x̄)`, MFCQ holds at `x` with the *same* witness `v̄` and constant `γ/2`, and consequently
> ```
> T_𝒢(x) = { v : ⟨∇g_k(x), v⟩ ≤ 0, k ∈ A(x) }.
> ```
>
> **(b) Quantitative lower semicontinuity.** For every `x ∈ 𝒢 ∩ U` and every `d ∈ T_𝒢(x̄)` there exists `d_x ∈ T_𝒢(x)` with
> ```
> ‖d_x − d‖  ≤  (2L/γ) · ‖x − x̄‖ · ‖d‖.
> ```
> Equivalently, `dist(d, T_𝒢(x)) ≤ (2L/γ)‖x − x̄‖‖d‖`. The map `x ↦ T_𝒢(x)` is lower semicontinuous on `𝒢` at `x̄`, with an explicit linear modulus.
>
> **(c) Exact constancy at the sharp hypothesis.** If in addition `d` is **strictly feasible** at `x̄`, i.e. `⟨∇g_k(x̄), d⟩ < 0` for every `k ∈ A(x̄)`, then `d ∈ T_𝒢(x)` for every `x ∈ 𝒢` sufficiently close to `x̄` — with no modulus and no approximation.
>
> **(d) Upper semicontinuity fails.** `x ↦ T_𝒢(x)` is in general **not** upper semicontinuous at `x̄`.

### Proof

**(a)** Let `x ∈ 𝒢 ∩ U` and `k ∈ A(x)`. Then `g_k(x) = 0`, and by continuity `g_k(x̄) = 0`, so `k ∈ A(x̄)`; hence `A(x) ⊆ A(x̄)`. For such `k`,

```
⟨∇g_k(x), v̄⟩ = ⟨∇g_k(x̄), v̄⟩ + ⟨∇g_k(x) − ∇g_k(x̄), v̄⟩
             ≤ −γ + L‖x − x̄‖·‖v̄‖  ≤  −γ + L‖x − x̄‖  ≤  −γ/2,
```

using `‖v̄‖ ≤ 1` and `‖x − x̄‖ < γ/(2L)`. So MFCQ holds at `x` with witness `v̄` and constant `γ/2`. MFCQ implies Abadie's constraint qualification, so the contingent cone equals the linearized cone at `x`. (Applied at `x̄` itself: `T_𝒢(x̄) = {v : ⟨∇g_k(x̄), v⟩ ≤ 0, k ∈ A(x̄)}`.)

**(b)** Let `d ∈ T_𝒢(x̄)`; by Abadie at `x̄`, `⟨∇g_k(x̄), d⟩ ≤ 0` for all `k ∈ A(x̄)`. Define

```
t := (2L/γ)·‖x − x̄‖·‖d‖,        d_x := d + t·v̄.
```

For `k ∈ A(x) ⊆ A(x̄)`, using (a) at `x`:

```
⟨∇g_k(x), d_x⟩ = ⟨∇g_k(x), d⟩ + t·⟨∇g_k(x), v̄⟩
               ≤ [⟨∇g_k(x̄), d⟩ + L‖x − x̄‖‖d‖] + t·(−γ/2)
               ≤ 0 + L‖x − x̄‖‖d‖ − (2L/γ)‖x − x̄‖‖d‖·(γ/2)
               = L‖x − x̄‖‖d‖ − L‖x − x̄‖‖d‖  =  0.
```

So `d_x ∈ T_𝒢(x)`, and `‖d_x − d‖ = t‖v̄‖ ≤ t = (2L/γ)‖x − x̄‖‖d‖`.

**(c)** Put `η := min_{k ∈ A(x̄)} (−⟨∇g_k(x̄), d⟩) > 0` (positive by strict feasibility, minimum over a finite set). For `k ∈ A(x) ⊆ A(x̄)`,

```
⟨∇g_k(x), d⟩ ≤ ⟨∇g_k(x̄), d⟩ + L‖x − x̄‖‖d‖ ≤ −η + L‖x − x̄‖‖d‖ < 0
```

whenever `‖x − x̄‖ < η/(L‖d‖)`. So `d ∈ T_𝒢(x)` exactly, by Abadie at `x`.

**(d)** In the witness, `T_𝒢(x̄) = {v : v_2 ≥ 0}` while `T_𝒢((a,a²)) = {v : 2a v_1 ≤ v_2}`. Take `w = (−1, −1/2)`. For `a ≥ 1/4`, `2a(−1) − (−1/2) = 1/2 − 2a ≤ 0`, so `w ∈ T_𝒢((a,a²))`; but `w_2 = −1/2 < 0`, so `w ∉ T_𝒢(x̄)`. Hence `T_𝒢(x) ⊄ T_𝒢(x̄)` for `x` arbitrarily close to `x̄`, and upper semicontinuity fails. ∎

### Sharpness

**The modulus is of the right order.** In the witness, `L = 2`, `γ = 1`, so the bound is `4‖x − x̄‖‖d‖`, and the true distance has the closed form

```
dist(d, T_𝒢((a,a²))) = 2a / √(4a² + 1).
```

Both are `Θ(a)`, so the **linear rate** is sharp in order. The constant `2L/γ` is not claimed optimal: the computed ratios `dist/bound` run `0.500, 0.497, 0.488, 0.434, 0.316, …`, so there is slack in the constant. Tightening it is a separate question and is not needed downstream.

**The hypothesis in (c) is sharp.** Strict feasibility cannot be weakened to weak feasibility: the witness's `d = (1,0)` satisfies `⟨∇g(x̄), d⟩ = 0` and fails at every nearby point, with MFCQ data uniform throughout (§0). Conversely `d = (0,1)` satisfies `⟨∇g(x), d⟩ = −1 < 0` at *every* point of the parabola and remains feasible everywhere — verified out to `a = 5`.

---

## 3. Part (2) repaired — the Clarke noncompensability certificate

The original asserted the certificate's existence but never stated the hypothesis under which it holds; its phrase "the pathway's blocked position `x̄ + s*d` realizes a first contact with `𝒢^c` at a boundary point `x_b`" is not a well-formed condition. The correct hypothesis is a single cone-membership statement.

**The original also had the sign wrong.** It states that `T_C(𝒢, x_b)` "excludes the strict descent direction `−d`". On the parabola witness, `−d = (−1,0)` **is** in `T_C = {2a v_1 − v_2 ≤ 0}` at every point (`2a(−1) = −2a ≤ 0`), while `d = (1,0)` is not. So the hypothesis as written is false on the very example the theorem is meant to cover, and under it the conclusion is unreachable — separating `−d` from `T_C` is impossible when `−d ∈ T_C`. The blocking direction is `d`, not `−d`.

> ### B6.Thm1(2) (repaired)
>
> Let `𝒢 ⊆ ℝⁿ` be closed, `x_b ∈ 𝒢`, and let `d ∈ ℝⁿ` satisfy
> ```
> d ∉ T_C(𝒢, x_b).                                                            (BLK)
> ```
> Then there exists `ξ ∈ N_C(𝒢, x_b)` with
> ```
> ⟨ξ, d⟩ > 0  ≥  sup{ ⟨ξ, w⟩ : w ∈ T_C(𝒢, x_b) }.
> ```
> Moreover, if `𝒢 = {g ≤ 0}` with `g` of class `C¹` and MFCQ holding at `x_b`, then
> ```
> N_C(𝒢, x_b) = { Σ_{k ∈ A(x_b)} λ_k ∇g_k(x_b) : λ_k ≥ 0 },
> ```
> so the certificate may be taken as `ξ = Σ_{k ∈ A(x_b)} λ_k ∇g_k(x_b)` with explicit nonnegative multipliers `λ`.

### Proof

`T := T_C(𝒢, x_b)` is a **closed convex cone** (the Clarke tangent cone of a closed set). By (BLK), `d ∉ T`. Strict separation of a point from a closed convex set gives `ξ₀ ∈ ℝⁿ` and `α ∈ ℝ` with

```
⟨ξ₀, d⟩ < α ≤ ⟨ξ₀, w⟩      for all w ∈ T.
```

Since `0 ∈ T`, `α ≤ 0`. Since `T` is a cone, `tw ∈ T` for every `t > 0`, so `t⟨ξ₀, w⟩ ≥ α` for all `t > 0`; letting `t → ∞` forces `⟨ξ₀, w⟩ ≥ 0`. Hence `⟨ξ₀, d⟩ < α ≤ 0`. Set `ξ := −ξ₀`. Then `⟨ξ, d⟩ > 0`, and `⟨ξ, w⟩ ≤ 0` for every `w ∈ T`, i.e. `ξ ∈ T^∘ = N_C(𝒢, x_b)` and `sup_T ⟨ξ, ·⟩ ≤ 0`.

For the multiplier representation: under MFCQ at `x_b`, the Clarke normal cone of `{g ≤ 0}` coincides with the cone generated by the active gradients (a standard consequence of Abadie plus the Clarke calculus; MFCQ gives the required regularity). ∎

### Reduction to Farkas

For **affine** `g`, `T_C(𝒢, x_b)` does not depend on `x_b` and equals `K := {v : Av ≤ 0}` where `A` is the constraint matrix. If `d ∉ K`, some row `a_i` satisfies `a_i·d > 0`, and the certificate is simply

```
ξ = a_i,    λ = e_i:      ⟨ξ, d⟩ = a_i·d > 0,   and   ⟨ξ, w⟩ = a_i·w ≤ 0  ∀ w ∈ K
```

because row `i` is one of `K`'s defining constraints. This is exactly the homogeneous Farkas alternative, and no Clarke machinery is used. (Verified on 8 random instances: in each case a single active row certifies, with `a_i·d` ranging `+0.058` to `+4.537`.) So part (2) genuinely extends the linear noncompensability certificate of E3.C2 rather than restating it.

---

## 4. Application to the substitution question

The substitution question is: *does direction `d` — compensating moiety `i`'s deficit with moiety `j`'s surplus along the declared pathway — admit feasible compensation near the contact point `x̄`?* The repaired theorem answers it at two levels, and the distinction matters.

**(i) Infinitesimal compensation.** `d ∈ T_𝒢(x̄)` iff there are feasible curves through `x̄` with tangent `d` — compensation is achievable to first order, possibly by leaving the declared ray. Under MFCQ this is decidable by the linear test `⟨∇g_k(x̄), d⟩ ≤ 0` for `k ∈ A(x̄)`.

**(ii) Robustness of the answer along the feasible set.** If compensation is *strictly* achievable (`⟨∇g_k(x̄), d⟩ < 0` on the active set), then it remains achievable at every nearby feasible point — part (1c), exactly, with no modulus. If it is only weakly achievable, part (1b) gives the quantitative substitute: the deficit in feasibility at a nearby point `x` is at most `(2L/γ)‖x − x̄‖‖d‖`.

**(iii) Structural noncompensability.** If `d` is blocked — `d ∉ T_C(𝒢, x_b)` at some `x_b` on the pathway — then part (2) supplies an explicit certificate `ξ = Σ λ_k ∇g_k(x_b)`, `λ ≥ 0`, exhibiting the direction along which no feasible compensation exists. This is the analytic form of the noncompensation axiom (TCS-1.0 §9 axiom 4) at nonlinear scope, and the object E7.Thm2 and the D-tier H3 protocol consume.

**Scope honesty, retained from the original.** Locality is MFCQ-qualified. The certificate's *existence* is unconditional given (BLK); *finding* `x_b` is a nonconvex problem in general, so the certificate is checkable but not necessarily cheap.

---

## 5. Status and obligations

- **B6.Thm1(1): PROVEN (repaired).** Quantitative lower semicontinuity with modulus `(2L/γ)‖x − x̄‖‖d‖`, plus exact constancy for strictly feasible directions. The original "iff" is false and is **not** recoverable by strengthening the MFCQ data (§0).
- **B6.Thm1(2): PROVEN (repaired).** Hypothesis `(BLK)` now stated; proof by cone separation; explicit multiplier representation under MFCQ; exact Farkas reduction in the affine case.
- **Consumers to re-check.** `E3.C2` cites B6 for the nonlinear domain and should now cite part (1c) for local constancy and part (2) for the certificate. `E7.Thm2` invokes "packet B6's Farkas separation (C2's linear case)" — unaffected, since it uses the linear case. `PROOF_REAUDIT.md` finding 2 is discharged.
- **Obligation created.** Any downstream use of "the feasible-direction property is stable" must say which of tangential or ray feasibility is meant (§0). A grep for that phrase is recommended before Paper 2's composition/atlas sections are finalised.

---

## 6. Verification

`reaudit/verify_b6_repair.py` — 31 assertions, exit 0:

| # | Claim | Result |
|---|---|---|
| N1 | original "iff" refuted; MFCQ witness and `γ = 1` **uniform** along the sequence | `⟨∇g(x), v̄⟩ = −1.000` at every sampled point |
| N2 | `dist(d, T_𝒢(x)) ≤ (2L/γ)‖x−x̄‖‖d‖`; closed form `2a/√(4a²+1)`; the constructed `d_x = d + t v̄` works | max `dist/bound = 0.4999`; construction verified |
| N3 | strictly feasible `d = (0,1)` stays feasible everywhere | `⟨∇g(x), d⟩ = −1.000` even at `a = 5` |
| N4 | upper semicontinuity fails | `w = (−1, −1/2) ∈ T_𝒢(x)`, `∉ T_𝒢(x̄)` |
| N5 | explicit certificate `ξ = ∇g(x_b)` separates | `⟨ξ,d⟩ = +0.2 … +6.0 > 0`; `sup⟨ξ, T_C⟩ ≤ 0` |
| N6 | tangential ≠ ray feasibility | ray `(s,0)` outside `𝒢` for `s = 0.5, 0.1, 0.01, 0.001` |
| N7 | affine case reduces to Farkas via a single active row | 8/8 random instances certified |

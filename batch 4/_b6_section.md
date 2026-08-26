## B6 — Nonlinear Substitution Classification — PROVEN (repaired)

> **Repair note.** Part (1)'s stability claim in the reconstructed session record is **false as
> stated** and is replaced; part (2)'s hypothesis was never well formed and had the sign wrong.
> Neither part is weakened: part (1) becomes a **quantitative** theorem with an explicit modulus
> plus an **exact** constancy statement at its sharp hypothesis, and part (2) gains an explicit
> multiplier representation. Full development and verification: `batch 4/B6_THM1_REPAIRED.md`
> (`reaudit/verify_b6_repair.py`, 31 assertions, exit 0).

### 0. What was false (recorded, not deleted)

**Original part (1)** claimed: under MFCQ at every nearby point, "`d` is a feasible direction at
`x̄` **iff** it is at every nearby `x`". Refuted by `𝒢 = {y ≥ x²}` (`g = x² − y`), `x̄ = (0,0)`,
`d = (1,0)`:

| point | `∇g` | `⟨∇g, d⟩` | `d ∈ T_𝒢`? | MFCQ? |
|---|---|---|---|---|
| `(0,0)` | `(0,−1)` | `0` | **yes** | yes |
| `(a, a²)`, `a > 0` | `(2a, −1)` | `2a > 0` | **no** | yes |

**The failure is robust to any strengthening of the MFCQ data.** With witness `v̄ = (0,1)`,
`⟨∇g(x), v̄⟩ = −1` at *every* point of the parabola, so MFCQ holds on a whole neighbourhood with
the same witness and the same constant `γ = 1`, and `∇g` is 2-Lipschitz throughout. Uniformity, a
positive MFCQ constant, Lipschitz gradients, `C^∞` data — none repairs the "iff". The obstruction
is that a **weakly** feasible direction can be feasible at one point and infeasible at nearby
points of the same smooth stratum, because the linearized cone rotates with `x`.

**Original part (2)** stated that `T_C(𝒢, x_b)` "excludes the strict descent direction `−d`". On
this same witness, `−d = (−1,0)` **is** in `T_C = {2a v_1 − v_2 ≤ 0}` at every point, while `d` is
not. The hypothesis as written is false on the example the theorem is meant to cover, and under it
the conclusion is unreachable. The blocking direction is `d`, not `−d`.

**Conceptual source of the error.** The original conflated **tangential feasibility**
(`d ∈ T_𝒢(x̄)`: feasible curves through `x̄` with tangent `d`, which may leave the ray) with **ray
feasibility** (`x̄ + sd ∈ 𝒢` for small `s`). In the witness `d = (1,0)` **is** in
`T_𝒢(x̄) = {v : v_2 ≥ 0}`, yet the ray `(s, 0)` leaves `𝒢` immediately since `0 < s²` for every
`s > 0`.

### 1. Setup

`g : ℝⁿ → ℝᵖ` of class `C^{1,1}` near `x̄`, `∇g` **L**-Lipschitz; `𝒢 = {g ≤ 0}`;
`A(x) = {k : g_k(x) = 0}`. **MFCQ data** at `x̄`: a witness `v̄` with `‖v̄‖ ≤ 1` and `γ > 0` with
`⟨∇g_k(x̄), v̄⟩ ≤ −γ` for all `k ∈ A(x̄)`.

### 2. Part (1) repaired — quantitative stability

> **B6.Thm1(1).** Under (MFCQ) with data `(γ, v̄)` and `∇g` `L`-Lipschitz, put
> `U = {‖x − x̄‖ < γ/(2L)}`. Then for every `x ∈ 𝒢 ∩ U`:
> **(a)** `A(x) ⊆ A(x̄)`, MFCQ holds at `x` with the same `v̄` and constant `γ/2`, and
> `T_𝒢(x) = {v : ⟨∇g_k(x), v⟩ ≤ 0, k ∈ A(x)}` (Abadie).
> **(b)** For every `d ∈ T_𝒢(x̄)` there is `d_x ∈ T_𝒢(x)` with
> `‖d_x − d‖ ≤ (2L/γ)·‖x − x̄‖·‖d‖`; i.e. `x ↦ T_𝒢(x)` is lower semicontinuous on `𝒢` at `x̄` with
> an explicit linear modulus.
> **(c)** If `d` is **strictly feasible** (`⟨∇g_k(x̄), d⟩ < 0` for all `k ∈ A(x̄)`), then
> `d ∈ T_𝒢(x)` for all `x ∈ 𝒢` near `x̄` — exactly, with no modulus.
> **(d)** `x ↦ T_𝒢(x)` is in general **not** upper semicontinuous at `x̄`.

**Proof.** (a) `k ∈ A(x)` gives `g_k(x) = 0`, hence `g_k(x̄) = 0` by continuity, so `A(x) ⊆ A(x̄)`.
Then `⟨∇g_k(x), v̄⟩ ≤ −γ + L‖x − x̄‖‖v̄‖ ≤ −γ/2` on `U`, giving MFCQ at `x`; MFCQ implies Abadie.

(b) Let `d ∈ T_𝒢(x̄)`; by Abadie at `x̄`, `⟨∇g_k(x̄), d⟩ ≤ 0` for `k ∈ A(x̄)`. Set
`t := (2L/γ)‖x − x̄‖‖d‖` and `d_x := d + t v̄`. For `k ∈ A(x) ⊆ A(x̄)`:

```
⟨∇g_k(x), d_x⟩ ≤ [⟨∇g_k(x̄), d⟩ + L‖x−x̄‖‖d‖] + t(−γ/2)
              ≤ L‖x−x̄‖‖d‖ − (2L/γ)‖x−x̄‖‖d‖·(γ/2) = 0,
```

so `d_x ∈ T_𝒢(x)`, and `‖d_x − d‖ = t‖v̄‖ ≤ t`.

(c) With `η := min_{k∈A(x̄)}(−⟨∇g_k(x̄), d⟩) > 0`, `⟨∇g_k(x), d⟩ ≤ −η + L‖x−x̄‖‖d‖ < 0` whenever
`‖x − x̄‖ < η/(L‖d‖)`; Abadie at `x` gives `d ∈ T_𝒢(x)`.

(d) In the witness, `w = (−1, −1/2)` lies in `T_𝒢((a,a²))` for `a ≥ 1/4` (since
`2a(−1) + 1/2 ≤ 0`) but not in `T_𝒢(x̄) = {v_2 ≥ 0}`. ∎

**Sharpness.** In the witness the true distance has closed form `2a/√(4a²+1)` and the bound is
`4‖x − x̄‖`; both are `Θ(a)`, so the **linear rate is sharp in order** (the constant `2L/γ` is not
claimed optimal — computed `dist/bound` runs `0.500, 0.497, 0.488, 0.434, …`). The hypothesis in
(c) is sharp: `d = (1,0)` is weakly feasible and fails everywhere nearby with MFCQ data uniform,
while `d = (0,1)` is strictly feasible and stays feasible out to `a = 5`.

### 3. Part (2) repaired — the Clarke noncompensability certificate

> **B6.Thm1(2).** Let `𝒢 ⊆ ℝⁿ` be closed, `x_b ∈ 𝒢`, and let `d` satisfy
> **`d ∉ T_C(𝒢, x_b)`**. Then there is `ξ ∈ N_C(𝒢, x_b)` with
> `⟨ξ, d⟩ > 0 ≥ sup{⟨ξ, w⟩ : w ∈ T_C(𝒢, x_b)}`. If moreover `𝒢 = {g ≤ 0}` with `g ∈ C¹` and MFCQ
> at `x_b`, then `N_C(𝒢, x_b) = {Σ_{k∈A(x_b)} λ_k ∇g_k(x_b) : λ_k ≥ 0}`, so `ξ` may be taken with
> explicit nonnegative multipliers.

**Proof.** `T := T_C(𝒢, x_b)` is a closed convex cone, and `d ∉ T`. Strict separation gives `ξ₀`,
`α` with `⟨ξ₀, d⟩ < α ≤ ⟨ξ₀, w⟩` for all `w ∈ T`. As `0 ∈ T`, `α ≤ 0`; as `T` is a cone,
`t⟨ξ₀,w⟩ ≥ α` for all `t > 0` forces `⟨ξ₀, w⟩ ≥ 0`. Hence `⟨ξ₀, d⟩ < 0`. With `ξ := −ξ₀`:
`⟨ξ, d⟩ > 0` and `⟨ξ, w⟩ ≤ 0` for all `w ∈ T`, i.e. `ξ ∈ T^∘ = N_C(𝒢, x_b)`. The multiplier
representation is standard under MFCQ (Abadie plus the Clarke calculus). ∎

**Reduction to Farkas.** For affine `g`, `T_C = K := {v : Av ≤ 0}`. If `d ∉ K` then some row `a_i`
has `a_i·d > 0`, and the certificate is the **single row** `ξ = a_i` (`λ = e_i`): `⟨ξ,d⟩ = a_i·d > 0`,
and `⟨ξ,w⟩ = a_i·w ≤ 0` for all `w ∈ K` because row `i` is one of `K`'s defining constraints. This
is exactly the homogeneous Farkas alternative — no Clarke machinery. (Verified on 8 random
instances; `a_i·d` ranged `+0.058` to `+4.537`.)

### 4. Application to substitution

**(i) Infinitesimal compensation** — `d ∈ T_𝒢(x̄)` iff feasible curves through `x̄` have tangent
`d`; under MFCQ decidable by `⟨∇g_k(x̄), d⟩ ≤ 0` on the active set. **(ii) Robustness** — strictly
achievable compensation persists exactly at every nearby feasible point (1c); weakly achievable
compensation degrades at most linearly, `(2L/γ)‖x − x̄‖‖d‖` (1b). **(iii) Structural
noncompensability** — a blocked direction (`d ∉ T_C(𝒢, x_b)`) yields the explicit certificate
`ξ = Σ λ_k ∇g_k(x_b)`, `λ ≥ 0`: the analytic form of the noncompensation axiom (TCS-1.0 §9
axiom 4) at nonlinear scope, and the object E7.Thm2 and the D-tier H3 protocol consume.

**Scope.** Local = MFCQ-qualified points. The certificate's *existence* is unconditional given
`(BLK)`; *finding* `x_b` is a nonconvex problem in general, so it is checkable but not necessarily
cheap. The linear case reduces exactly to Farkas (E3.C2).

**Obligation.** Any downstream use of "the feasible-direction property is stable" must say whether
tangential or ray feasibility is meant (§0). `E3.C2` should cite (1c) for local constancy and (2)
for the certificate.


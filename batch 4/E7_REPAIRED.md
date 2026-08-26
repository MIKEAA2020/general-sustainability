# E7 — Conservation–Viability Coupling: REPAIRED

**Replaces:** `E7.Cor3`, `E7.Thm1(b)`, `E7.Thm1(c)`, `E7.Thm1(d)` and `E7.Thm2` in `batch 2/02_elevation/E7_CONSERVATION_VIABILITY_COUPLING.md`; `C-e.Thm1` in `batch 2/04_open_problems/C_TIER_COMPLETIONS.md`; and the manifest rows `E7.Thm1`, `E7.Thm2` (lines 83–84) and `C-e.Thm1` (line 102).

**Disposition.** `E7.Thm1(a)` and the inclusion half of `E7.Thm2` are correct and are retained. Four defects are repaired, and in three of the four the repair is **stronger** than what it replaces:

| # | Defect | Kind | Disposition |
|---|---|---|---|
| D1 | `Cor3` and `C-e` identify `L_G` as a barrier-geometry constant; the controlling packet defines it as the **velocity envelope's** Hausdorff–Lipschitz modulus | wrong object | repaired by separating two constants; the intended dichotomy survives and gains an explicit formula |
| D2 | `Thm1(b)`'s pathwise exit claim needs `F ≤ 0` for every realization, but the hypothesis only makes `F ≡ 0` *possible* | hypothesis/conclusion mismatch | split into a robust-kernel claim and a pathwise claim with the correct hypotheses |
| D3 | `Thm1(c)`'s displayed outer bound substitutes `F⁺_T` where the proof derives `F⁻_T` | sub-sharp | repaired to the sharp bound — **strictly stronger** |
| D4 | `Thm2`'s noncompensation claim uses the committed budget `D_{i,T}`, contradicting the file's own E5 sanity check | false as stated | repaired to the sharp bound, with an explicit certificate |

**Verification.** `reaudit/verify_e7_repair.py`, 40 assertions, exit 0. Output: `reaudit/e7_output.txt`.

---

## 0. D1 — what `L_G` is, and why the barrier cannot change it

The controlling definition is `research_program/general_theory_math_closure_packet/corrected_theorems/02_operator_I_strong_invariance_and_erosion.md`, Lemma 2. Its hypotheses are:

```
K has two-sided tubular radius rho > 0;  signed distance is C^{1,1} in |s_K| < rho;
normals of dK_{-r} correspond to normals of dK for 0 < r < rho;

d_H(G(x), G(p)) <= L_G ||x - p||          in the inner tube,      <- L_G is the ENVELOPE's modulus
sup_{v in G(p)} <n(p), v> <= -alpha < 0   on dK;
G~_eps(x) subset G(x) + Delta_eps B;

L_G r + Delta_eps <= alpha,  0 < r < rho,  K_{-r} != empty   ==>   K_{-r} strongly invariant.
```

`L_G` is a property of the **dynamics**. The barrier enters Lemma 2 only through `rho`, the `C^{1,1}` regularity of `s_K`, and the normal correspondence.

**`Cor3`'s claim is false.** It asserts `L_G = 0` for an affine moiety barrier because "the normal is constant". Counterexample: `K = {x ∈ ℝ² : x_2 ≥ 0}` (a half-space, i.e. exactly a moiety floor), with envelope

```
U(x) = [0, 1] × [-1 - x_1, 0].
```

Then `d_H(U(x), U(p)) = |x_1 − p_1| = ‖x − p‖` whenever `x, p` differ only in the first coordinate, so **`L_G = 1 > 0` on a half-space**. Verified: the ratio `d_H/‖x−p‖` is exactly `1.000000` for five separated pairs including `(0,1)`, `(−2,3)`, `(7,−4)`.

### 0.1 `E7.Cor3` repaired — affine barriers make the erosion calculus **global**

> **E7.Cor3 (repaired).** Let `K = {x : B(x) ≥ 0}` with `B(x) = ⟨a, x⟩ − c`, `a ≠ 0` (an affine moiety barrier; a half-space). Then:
>
> **(i)** the signed distance `s_K(x) = B(x)/‖a‖` is **affine**: `∇s_K = a/‖a‖` is constant with `‖∇s_K‖ = 1`, and `∇²s_K = 0`. In particular `s_K` is `C^{1,1}` globally, with `C^{1,1}` seminorm `0`.
>
> **(ii)** `K_{−r} = {x : B(x) ≥ r‖a‖}` for every `r ≥ 0`; each `K_{−r}` is a half-space, hence nonempty, and its outward normal equals that of `K`.
>
> **(iii)** consequently Lemma 2's geometric hypotheses hold with **tubular radius `rho = ∞`**, and the erosion condition reduces to
> ```
> L_G r + Delta <= alpha,        r > 0 arbitrary,
> ```
> with **no** upper bound on `r` other than that inequality.
>
> **(iv)** `L_G` is unaffected by the barrier's shape and is in general positive. The quantity that vanishes for an affine barrier is the **normal-variation constant**
> ```
> L_n := sup_{x in dK} ||D n(x)||,
> ```
> which is `0` here and strictly positive for a strictly convex barrier.

*Proof.* (i) `B` is affine, so `s_K = B/‖a‖` is affine with the stated gradient and zero Hessian. (ii) For a half-space, `dist(x, K^c) = max(0, B(x)/‖a‖)`, so `K_{−r} = {x ∈ K : B(x)/‖a‖ ≥ r} = {B ≥ r‖a‖}`; this is a half-space for every `r`, hence nonempty, with the same outward normal `a/‖a‖`. (iii) `s_K` is `C^{1,1}` on all of `ℝⁿ` and the normal correspondence holds for every `r > 0`, so the tubular-radius hypothesis is satisfied with `rho = ∞`. (iv) `L_G` bounds `d_H(G(x), G(p))`, which depends only on the envelope; the exhibited counterexample has `L_G = 1`. `n` is constant on `∂K`, so `Dn ≡ 0` and `L_n = 0`. ∎

**Why this is stronger than the original.** `Cor3` claimed a *degeneracy* — "the erosion condition `L_G r + Δ ≤ α` degenerates to `Δ ≤ α`", i.e. that erosion costs nothing for affine barriers. That is false and, if used, unsafe: it would license unbounded erosion depth with no budget. The repaired statement says the opposite and more useful thing — the erosion budget `L_G r + Δ ≤ α` is **fully operative**, but it is the *only* constraint, because there is no tubular-radius ceiling to hit. For a moiety floor this is exactly the right result: the ledger's linear geometry buys global validity of the calculus, not an exemption from it.

### 0.2 `C-e.Thm1` repaired — quadratic barriers confine the calculus to a finite tube

> **C-e.Thm1 (repaired).** Let `B(x) = c − xᵀMx` with `M ≻ 0` symmetric, so `K = {B ≥ 0} = {xᵀMx ≤ c}` is an ellipsoid. Let `λ_min ≤ λ_max` be the extreme eigenvalues of `M` and `a_i = √(c/λ_i)` the semi-axes. Then:
>
> **(i)** the boundary `∂K` has **finite reach**
> ```
> tau = min radius of curvature = sqrt(c) · sqrt(lambda_min) / lambda_max      (for c = 1:  sqrt(lambda_min)/lambda_max),
> ```
> and Lemma 2's erosion calculus applies only for `0 < r < tau`.
>
> **(ii)** the normal map `n(x) = Mx/‖Mx‖` varies along `∂K` with `sup ‖Dn‖ = 1/tau`, so `L_n = 1/tau > 0`.
>
> **(iii)** the sandwich of `E7.Thm1` holds in the quadratic bookkeeping unchanged (it uses only the ledger identity and the flux bounds, not the geometry).

*Proof sketch.* For the 2-D ellipse with semi-axes `a ≥ b`, the radius of curvature is `(a²sin²t + b²cos²t)^{3/2}/(ab)`, minimised at `t = 0` with value `b²/a`; the reach of a `C²` convex hypersurface is the reciprocal of its maximal principal curvature, hence `tau = b²/a`. Substituting `a = √(c/λ_min)`, `b = √(c/λ_max)` gives (i). (ii) follows because the normal map of a convex hypersurface has `‖Dn‖` equal to the principal curvatures, whose maximum is `1/tau`. (iii) is the original `C-e` sandwich proof, which never used the geometry. ∎

**Verified.** `min` radius of curvature equals `b²/a` to `1e−6` for `(a,b) = (3,1), (2,1), (5,2), (4,0.5)`; `sup|dn|/|ds|` on the `(3,1)` ellipse is `3.000000 = a/b² = 1/tau`; and `√λ_min/λ_max = b²/a` exactly for three eigenvalue pairs.

**The repaired dichotomy.** Affine barrier ⟹ `L_n = 0`, `rho = ∞`: the erosion calculus is global. Quadratic barrier ⟹ `L_n = 1/tau > 0`, `rho = tau < ∞`: the calculus is confined to a tube whose radius is the minimal radius of curvature, computable from the eigenvalues of `M`. That is the contrast `Cor3`/`C-e` were reaching for, stated in terms of the constants that actually carry it.

**Manifest consequence.** `C-e.Thm1`'s row currently reads "Quadratic moiety sandwich with `L_G > 0`". It should read "… with finite tubular radius `tau = √λ_min/λ_max` and normal variation `L_n = 1/tau`".

---

## 1. D2 — `E7.Thm1(b)` repaired

**Defect.** The hypothesis is "`D(t) ≥ γ > 0` policy-independent, and `F ≡ 0` is **possible**", and the conclusion has two parts: `Viab_T({q ≥ 0}) = ∅` for `T > q(0)/γ`, *and* "**every** trajectory exits the floor within time `q(0)/γ`". The first follows; the second does not. With `q(0) = 10`, `γ = 1`: under `F ≡ 0` exit is at `t = 10`; under `F ≡ 1` the trajectory never exits; under `F ≡ 3` it grows. Verified.

> **E7.Thm1(b) (repaired).** Let the outflow have the uniform obligatory minimum `D(t) ≥ γ > 0`, policy-independent.
>
> **(b1) Robust-kernel emptying.** If `F ≡ 0` is an admissible inflow realization, then `Viab_T({q_L ≥ 0}) = ∅` for every `T > q_L(0)/γ`. The pair `(γ, q_L(0)/γ)` is an **adversarial-exit certificate** in the sense of `R03.Thm1`'s first branch: the nonviability judgment is certified by conservation data alone.
>
> **(b2) Pathwise exit.** If additionally `F ≤ 0` for **every** admissible realization, then every trajectory satisfies `q_L(t) ≤ q_L(0) − γt` and exits the floor by time `q_L(0)/γ`.
>
> **(b3) Sharp exit time under a general inflow bound.** If `F ≤ F⁺`, every trajectory exits by `q_L(0)/(γ − F⁺)` when `γ > F⁺`, and need not exit at all when `γ ≤ F⁺`.

*Proof.* (b1) Robust viability requires safety against every admissible realization, in particular `F ≡ 0`; under it, `q_L(t) ≤ q_L(0) − γt < 0` for `t > q_L(0)/γ`, so no policy is safe. (b2) `q_L(t) = q_L(0) + ∫F − ∫D ≤ q_L(0) − γt`. (b3) `q_L(t) ≤ q_L(0) + F⁺t − γt`. ∎

Only (b1) is needed for the adversarial-exit certificate, and (b1) is what the original's hypothesis actually supports.

---

## 2. D3 — `E7.Thm1(c)` repaired to the sharp bound

**Defect.** The proof takes the inflow adversarial to the floor, `F ≡ F⁻`, and the policy minimal, `D ≡ D⁻`, and correctly derives `q_L(0) ≥ D⁻_T − F⁻_T`. The *displayed* conclusion substitutes the upper inflow bound: `q_L(0) ≥ D⁻_T − F⁺_T`, described as "crediting the best-case relief". Since `F⁺ ≥ F⁻`, the displayed bound is valid but strictly weaker — by `F⁺_T − F⁻_T`.

> **E7.Thm1(c) (repaired).** If viability of `{q_L ≥ 0}` on `[0,T]` holds at `x`, then necessarily
> ```
> q_L(x)  >=  D^-_T - F^-_T,
> ```
> and this is **sharp**: for every `q_L(0) ≥ D⁻_T − F⁻_T` the policy `D ≡ D⁻` keeps `q_L(t) ≥ q_L(0) + F⁻_T(t/T) − D⁻_T(t/T) ≥ 0` against the worst-case inflow `F ≡ F⁻`.

*Proof.* The adversary minimises `q_L`, so takes `F ≡ F⁻`; the policy maximises it, so takes `D ≡ D⁻`. Then `q_L(t) = q_L(0) + ∫F⁻ − ∫D⁻`, and safety at the binding time gives the bound. Sharpness is the same computation read forwards. ∎

**Verified.** The sharp bound dominates the record's in all tested cases, strictly whenever regeneration is material — slack `6.0, 5.0, 6.0, 0.0, 8.0` for `(D⁻_T, F⁻_T, F⁺_T) = (10,2,8), (10,0,5), (6,3,9), (12,4,4), (4,2,10)`.

---

## 3. D4 — `E7.Thm2` repaired

**Defect.** The record claims: "a deficit in moiety `i` (i.e. `q_{L_i}(0) < D_{i,T}`) cannot be compensated … the compensated state is **outside the kernel** of the product constraint." Deficit relative to the *committed budget* does not imply non-membership, because the inner rule is conservative — as the same file's E5 sanity check states ("the floor's `D_T = 0.4·T` is conservative against the true kernel `S ≥ 2`").

**Explicit refutation.** Take `D⁻ = 0.4`/unit, `F ∈ [0.2, 1.0]`/unit, `T = 10`, committed budget `D_T = D⁻_T = 4.0`. Then `D⁻_T − F⁻_T = 2.0 < D_T = 4.0`, a gap of `2.0`. For every `q(0) ∈ [2.0, 4.0)` the record's test declares the state outside the kernel — yet the admissible policy `D ≡ D⁻` gives

```
min_t q(t) = q(0) + F^-_T - D^-_T = q(0) - 2.0  >=  0,
```

so all of them are viable. Verified: `min_t q(t) = 0.000, 0.500, 1.000, 1.900` at `q(0) = 2.0, 2.5, 3.0, 3.9`. Only `q(0) < 2.0` forces non-membership.

> **E7.Thm2 (repaired) — Multi-moiety noncompensatory form.** For moieties `L_1, …, L_m` with separate ledgers and no declared conversion pathway between them:
>
> **(i) Inclusion** (unchanged, correct): `∏_i {q_{L_i} ≥ D_{i,T}} ⊆ Viab_T(∏_i {q_{L_i} ≥ 0})`.
>
> **(ii) Sharp noncompensation.** If `q_{L_i}(0) < D⁻_{i,T} − F⁻_{i,T}` for some `i`, then the state lies outside the kernel of the product constraint, and **no cross-moiety transfer can rescue it**: no allocation of moiety `j`'s surplus changes `q_{L_i}(T)`.
>
> **(iii) Certificate.** The certificate is the moiety-`i` ledger identity itself — the coordinate functional `e_i`. Since the declared flow cone has no `i ↔ j` pathway, `⟨e_i, ·⟩` applied to the dynamics depends only on moiety `i`'s flows; the deficit is therefore **structural**, not allocative.

*Proof.* (i) is `Thm1(a)` applied componentwise with the product policy. (ii) By `Thm1(c)` repaired, applied to moiety `i`, viability requires `q_{L_i}(0) ≥ D⁻_{i,T} − F⁻_{i,T}`; the contrapositive gives non-membership. For the transfer clause: moiety `j`'s flows do not appear in moiety `i`'s ledger identity, so `q_{L_i}(T)` is invariant under arbitrary changes to `(F_j, D_j)`. (iii) `e_i` is the exhibited functional. ∎

**Note on `Farkas`.** The record invoked "packet B6's Farkas separation" for this step. That is unnecessary and obscures the argument: with no declared pathway, noncompensation is a **conservation** fact, not a feasibility computation. Farkas is the right tool when a pathway *is* declared and the question is whether it suffices — which is `B6.Thm1(2)`'s setting, and where the certificate has explicit multipliers. Verified: `q_i(T)` takes exactly one value across 200 random draws of moiety-`j` flows.

**Sharpness of (ii).** `q_{L_i}(0) = D⁻_{i,T} − F⁻_{i,T}` is viable under `D ≡ D⁻` against `F ≡ F⁻` (the minimum is exactly `0`), so the bound cannot be improved.

---

## 4. The repaired sandwich

> **E7.Thm1(d) (repaired).**
> ```
> { q_L >= D_T }        subset   Viab_T({q_L >= 0})   subset   { q_L >= D^-_T - F^-_T },
> ```
> with the inner bound from the *committed* budget `D_T` and the outer bound sharp. The gap between them is `D_T − D⁻_T + F⁻_T`: the slack in the budget commitment, plus the regeneration the ledger ignores. The sandwich is consistent (`D⁻_T − F⁻_T ≤ D⁻_T ≤ D_T`) and is tight in the pure-drain, exactly-committed limit (`F ≡ 0`, `D ≡ D⁻`).

The record's version, `{q ≥ D⁺_T-budget} ⊆ Viab ⊆ {q ≥ D⁻_T − F⁺_T}`, had two problems: the inner bound was written with `D⁺_T-budget` while rule (a) uses the committed `D_T`, and the outer bound was weaker by `F⁺_T − F⁻_T`. On the worked numbers above the repaired outer bound is tighter by `8.0` (`2.0` against `−6.0`).

**Mixed regime (unchanged).** Where a floor on one moiety couples to a ceiling on another through the extraction — the E5 resource–sink geometry — neither rule alone decides viability, and the module's structure is required. That is the honest boundary of flux-only reasoning, and it is unaffected by these repairs.

---

## 5. Status and obligations

- **E7.Thm1(a): PROVEN**, unchanged.
- **E7.Thm1(b): PROVEN (repaired)** — split into (b1) robust-kernel, (b2) pathwise, (b3) sharp exit time.
- **E7.Thm1(c): PROVEN (repaired)** — sharp bound `D⁻_T − F⁻_T`, and sharpness proved.
- **E7.Thm1(d): PROVEN (repaired)** — tighter sandwich.
- **E7.Thm2: PROVEN (repaired)** — noncompensation at the sharp bound, with the ledger-identity certificate; `Farkas` invocation removed as unnecessary.
- **E7.Cor3: PROVEN (repaired)** — affine barriers give `rho = ∞` and `L_n = 0`; the erosion budget remains fully operative.
- **C-e.Thm1: PROVEN (repaired)** — quadratic barriers give `rho = tau = √c·√λ_min/λ_max` and `L_n = 1/tau`.
- **Withdrawn.** "`L_G = 0` for affine barriers" and "`L_G > 0` for quadratic barriers" — `L_G` is the envelope's modulus and is not a function of the barrier. Also withdrawn: "the compensated state is outside the kernel" at the committed-budget threshold, and "every trajectory exits within `q(0)/γ`" under the `F ≡ 0`-possible hypothesis.
- **Obligation created.** A grep for `L_G = 0` and for `D^-_T - F^+_T` across `revised_articles/` and the manuscripts is recommended before Paper 3 is finalised: the `L_G` confusion is exactly the kind of error that propagates into a paper's erosion-budget discussion unnoticed. `PROOF_REAUDIT.md` finding 13 is discharged.

---

## 6. Verification

`reaudit/verify_e7_repair.py` — 40 assertions, exit 0:

| # | Claim | Result |
|---|---|---|
| N1 | affine barrier (half-space) with `L_G = 1 > 0` | `d_H/‖x−p‖ = 1.000000` for 5 pairs |
| N2 | `s_K` affine and 1-Lipschitz; `K_{−r}` nonempty at `r = 0, 1, 10, 10⁶`; `rho = ∞` | all |
| N3 | `sup‖Dn‖ = a/b² = 3` on the `(3,1)` ellipse; `0` for a half-space | `3.000000` vs `3.000000` |
| N4 | reach `= b²/a` for 4 ellipses; `= √λ_min/λ_max` for 3 eigenvalue pairs; `sup‖Dn‖ = 1/tau` | all to `1e−6` |
| N5 | sharp `D⁻_T − F⁻_T` dominates the record's, strictly when `F⁺ > F⁻` | slack `6, 5, 6, 0, 8` |
| N6 | pathwise exit needs `F ≤ 0`; `F ≥ γ` never exits; `0 < F < γ` exits later | `20.0 > 10.0` |
| N7 | `q(0) ∈ [2.0, 4.0)` declared non-viable by the record, all viable | `min_t q = 0.000 … 1.900` |
| N8 | `q_i(T)` invariant under 200 random moiety-`j` flow draws | 1 distinct value |
| N9 | repaired sandwich tighter by `F⁺_T − F⁻_T = 8.0`, and consistent | `2.0 ≤ 4.0` |

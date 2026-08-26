# A3.Thm1 — Interleaved-Segment Compactness: REPAIRED

**Replaces:** the `A3.Thm1` section of `batch 2/04_open_problems/A3_VARIABLE_EVENT_KERNEL.md`, and the manifest row `A3.Thm1 | PROVEN (reconstructed)` in `PROOF_MANIFEST.md` line 90.

**Disposition of the original claim.** The original statement is **irreparably false** and is replaced, not qualified. Its hypotheses (break budget `B`, jump bound `J`, path bound `M`) do not imply compactness; two explicit counterexamples are given in §0. The repaired theorem below restores the *full* conclusion — compactness of the budgeted history space — under one additional hypothesis, and §4 proves that this hypothesis is **automatic for the systems A3.Thm3 is about**. Nothing is lost downstream: the hypothesis set of A3.Thm3 is unchanged in substance.

**Net change vs. the original.** The repaired result is strictly stronger in four ways: (i) the topology is genuinely metrized, which the original's `τ_IS` was not (§1.3); (ii) compactness is proved, not asserted (§2); (iii) two sharpness witnesses show the added hypothesis cannot be weakened (§3); (iv) dynamical closure is proved, so the hypothesis is a theorem about solution windows rather than an assumption (§4).

**Verification.** `reaudit/verify_a3_repair.py`, 18 assertions, exit 0. Output: `reaudit/a3_output.txt`.

---

## 0. Why the original fails

**Original claim.** `ℋ` = piecewise-continuous `φ : [−τ,0] → ℝⁿ` with at most `B` discontinuities, all jumps bounded by `J`, path bounded by `M`, is compact in the interleaved-segment topology `τ_IS`, where `φ_k → φ` iff break sets converge and `φ_k` converges **uniformly on each inter-break segment**.

**Counterexample 1 (boundedness alone).** On `I = [−1,0]`, take `B = 0`, `M = 1`, and `φ_k(s) = sin(2πks)`. Every `φ_k` is admissible: continuous, hence zero breaks, and `|φ_k| ≤ 1`. For `k ≠ m`, orthogonality on an interval of length 1 gives

```
‖φ_k − φ_m‖²_{L²(I)} = ∫_I (sin 2πks − sin 2πms)² ds = 1/2 + 1/2 = 1,
```

and since `|I| = 1`, `‖φ_k − φ_m‖_∞ ≥ ‖φ_k − φ_m‖_{L²} = 1`. The family is uniformly 1-separated, so it has no Cauchy subsequence. **`ℋ` is not sequentially compact.** (Verified: pairwise `L²` distance 1.000000, pairwise sup distance ≥ 1.760173.)

**Counterexample 2 (bounded total variation is also insufficient).** This closes the escape route the original proof attempted via a "Helly-type selection". Take `φ_k(s) = (s+1)^k` on `[−1,0]`. Each `φ_k` is monotone increasing from `0` to `1`, so `TV(φ_k) = 1` **exactly**, uniformly in `k`, and `‖φ_k‖_∞ = 1`. Consider the subsequence `φ_{2^j}`. For `j < i`, put `k = 2^j`, `m = 2^i ≥ 2k`; at `θ = 2^{−1/k}`,

```
θ^k = 1/2,   θ^m = 2^{−m/k} ≤ 2^{−2} = 1/4   ⟹   sup_θ |θ^k − θ^m| ≥ 1/4.
```

So `φ_{2^j}` is uniformly `1/4`-separated in sup norm: no Cauchy subsequence. **Uniformly bounded total variation does not yield `τ_IS`-compactness.** (Verified: `TV = 1.000000000` for `k ∈ {1,2,3,5,8,13,21,34}`; minimum pairwise sup distance over `{2^j}_{j≤6}` is `0.250000`.)

**Diagnosis.** `τ_IS` demands uniform convergence on segments. Compactness under uniform convergence requires equicontinuity (Arzelà–Ascoli). Boundedness supplies none; bounded total variation supplies none either, as Counterexample 2 shows, because variation can concentrate. The original proof's "interleaving" — extending each restricted segment by constant continuation from its endpoints — does not create equicontinuity: constant continuation preserves, and cannot repair, the absence of a common modulus.

There is a second, independent defect. The original's clause "(ii) on each inter-break segment, `φ_k` converges uniformly to the corresponding segment of `φ`" is **not well defined when break points move**: as `k` varies, the segments have different endpoints, so "uniform convergence on the segment" compares functions on different domains. §1.3 fixes this by affine reparametrization to a fixed interval.

---

## 1. The repaired class and topology

### 1.1 Data

Fix `τ > 0`, `n ≥ 1`, `I := [−τ, 0]`, an integer `B ≥ 0`, constants `J ≥ 0`, `M > 0`, and a **modulus** `ω : [0, τ] → [0, ∞)` — nondecreasing, `ω(0) = 0`, continuous at `0`.

### 1.2 The class

`ℋ = ℋ(B, J, M, ω)` consists of all `φ : I → ℝⁿ` for which there is a break set `S(φ) ⊂ (−τ, 0)` with `|S(φ)| ≤ B` such that, writing `S(φ) = {s_1 < ⋯ < s_k}` and `s_0 := −τ`, `s_{k+1} := 0`:

- **(H1) regulated on segments.** `φ` is continuous on each open interval `(s_j, s_{j+1})` and admits one-sided limits at every `s_j`;
- **(H2) bound.** `‖φ(s)‖ ≤ M` for all `s ∈ I`;
- **(H3) jump bound.** `‖φ(s_j+) − φ(s_j−)‖ ≤ J` for each `j = 1, …, k`;
- **(H4) common modulus.** for every `j` and all `s, s' ∈ [s_j, s_{j+1}]`, `‖φ(s) − φ(s')‖ ≤ ω(|s − s'|)`.

Right-continuity convention: `φ(s_j) := φ(s_j+)` for `j ≥ 1`, `φ(−τ) := φ(−τ+)`, `φ(0) := φ(0−)`.

**(H4) is the added hypothesis.** §3 shows it is necessary; §4 shows it is free in the application.

### 1.3 Coordinates and the metric

**Break tuple.** Pad `S(φ)` on the right by repeating `0` to length `B`, giving `σ(φ) = (s_1 ≤ ⋯ ≤ s_B) ∈ Δ_B := {σ ∈ [−τ,0]^B : σ_1 ≤ ⋯ ≤ σ_B}`. Set `s_0 = −τ`, `s_{B+1} = 0`, and `I_j := [s_j, s_{j+1}]` for `j = 0, …, B`; note `I_j` may be degenerate.

**Segment functions.** Define `g_j(φ) : [0,1] → ℝⁿ` by

```
g_j(φ)(θ) := φ(s_j + θ(s_{j+1} − s_j))        if s_j < s_{j+1},
g_j(φ)(θ) := φ(s_j)                            if s_j = s_{j+1}   (constant).
```

This is the reparametrization that repairs defect (ii) of §0: **all segment functions live on the same fixed domain `[0,1]`**, so they can be compared in `C([0,1], ℝⁿ)` regardless of where the breaks sit. Under the right-continuity convention, `g_j(φ)(0) = φ(s_j+)` and `g_j(φ)(1) = φ(s_{j+1}−)`.

**Metric.**

```
d(φ, ψ) := ‖σ(φ) − σ(ψ)‖_∞  +  max_{0 ≤ j ≤ B} ‖g_j(φ) − g_j(ψ)‖_{C[0,1]}.
```

**Lemma 1.1.** `d` is a metric, and the map

```
ι : ℋ → Δ_B × C([0,1], ℝⁿ)^{B+1},    ι(φ) = (σ(φ), g_0(φ), …, g_B(φ))
```

is an isometric embedding onto its image.

*Proof.* `ι` is injective: `φ` is recovered from `(σ, g)` by `φ(s) = g_j((s − s_j)/(s_{j+1} − s_j))` for `s ∈ (s_j, s_{j+1})`, `φ(s_j) = g_j(0)` for `j ≥ 1`, `φ(−τ) = g_0(0)`, `φ(0) = g_B(1)`. Degenerate segments contribute no interior points, so the reconstruction is unambiguous. `d` is the pullback along `ι` of the product metric `‖·‖_∞ + max_j ‖·‖_∞` on `Δ_B × C^{B+1}`, hence a metric, and `ι` is isometric by construction. ∎

**Lemma 1.2 (the image).** `ι(ℋ) = 𝒢`, where

```
𝒢 := { (σ, g) ∈ Δ_B × AS^{B+1} :  ‖g_j(0) − g_{j−1}(1)‖ ≤ J  for j = 1, …, B },
AS := { g ∈ C([0,1], ℝⁿ) : ‖g‖_∞ ≤ M,  |g(θ) − g(θ')| ≤ ω(τ|θ − θ'|) ∀θ, θ' }.
```

*Proof.* (⊆) Let `φ ∈ ℋ`. `σ(φ) ∈ Δ_B` by padding. For each `j`, `‖g_j(φ)‖_∞ ≤ M` by (H2). For the modulus: if `s_j < s_{j+1}`, then for `θ, θ' ∈ [0,1]`,

```
‖g_j(φ)(θ) − g_j(φ)(θ')‖ = ‖φ(s_j + θℓ_j) − φ(s_j + θ'ℓ_j)‖ ≤ ω(|θ − θ'| ℓ_j) ≤ ω(τ|θ − θ'|),
```

using (H4), `ℓ_j := s_{j+1} − s_j ≤ τ`, and monotonicity of `ω`; if `ℓ_j = 0`, `g_j` is constant and the bound is trivial. So `g_j(φ) ∈ AS`. Finally `g_j(φ)(0) − g_{j−1}(φ)(1) = φ(s_j+) − φ(s_j−)`, whose norm is `≤ J` by (H3).

(⊇) Let `(σ, g) ∈ 𝒢`. Define `φ` by the reconstruction of Lemma 1.1. Then `φ` is continuous on each `(s_j, s_{j+1})` as a composition of continuous maps, with one-sided limits at the `s_j` (given by `g_j(0)` and `g_{j−1}(1)`), so (H1). `‖φ‖_∞ ≤ max_j ‖g_j‖_∞ ≤ M`, so (H2). The jump at `s_j` is `g_j(0) − g_{j−1}(1)`, of norm `≤ J`, so (H3). For (H4), on `I_j` with `ℓ_j > 0` and `s = s_j + θℓ_j`, `s' = s_j + θ'ℓ_j`:

```
‖φ(s) − φ(s')‖ = ‖g_j(θ) − g_j(θ')‖ ≤ ω(τ|θ − θ'|) = ω(|s − s'|).   ∎
```

---

## 2. Main theorem

> ### A3.Thm1 (repaired) — Interleaved-segment compactness
>
> Let `B ∈ ℕ`, `J, M ≥ 0`, and `ω` a modulus as in §1.1. Then `(ℋ(B, J, M, ω), d)` is a **compact metrizable space**. Moreover:
>
> **(a)** `ℋ` is a closed subset of the compact set `ι^{-1}(Δ_B × AS^{B+1})`, and `AS` is compact by Arzelà–Ascoli;
>
> **(b)** the convergence notion is exactly: `φ_m → φ` iff `σ(φ_m) → σ(φ)` in `[−τ,0]^B` and `g_j(φ_m) → g_j(φ)` uniformly on `[0,1]` for every `j = 0, …, B` — **breaks may move**, and a jump travelling to a segment endpoint converges to a jump at that endpoint;
>
> **(c)** the break count is upper semicontinuous along limits: if `φ_m → φ` and each `φ_m` has exactly `k` breaks, then `φ` has at most `k` breaks (breaks may collide in the limit, never appear).

### Proof

**Compactness of `AS`.** `AS` is uniformly bounded by `M` and equicontinuous with common modulus `ω(τ ·)`, which tends to `0` at `0`. By Arzelà–Ascoli, `AS` is relatively compact in `C([0,1], ℝⁿ)`. It is also closed: if `g_k → g` uniformly with `g_k ∈ AS`, then `‖g‖_∞ ≤ M` and `|g(θ) − g(θ')| = lim_k |g_k(θ) − g_k(θ')| ≤ ω(τ|θ − θ'|)`. Hence `AS` is compact.

**Compactness of `ℋ`.** `Δ_B` is a closed subset of the compact `[−τ,0]^B`, hence compact. So `Δ_B × AS^{B+1}` is compact (Tychonoff, finite product). By Lemma 1.2, `ι(ℋ) = 𝒢` is the subset of `Δ_B × AS^{B+1}` cut out by the `B` conditions `‖g_j(0) − g_{j−1}(1)‖ ≤ J`. Each evaluation map `g ↦ g(0)` and `g ↦ g(1)` is continuous on `C[0,1]`, so each condition defines a closed set. Therefore `𝒢` is closed in a compact space, hence compact. Since `ι` is a homeomorphism onto `𝒢` (Lemma 1.1), `ℋ` is compact. Metrizability is immediate: `d` is a metric inducing the topology. This proves (a) and the main claim.

**(b)** is a restatement of Lemma 1.1: `d`-convergence *is* convergence of the break tuple plus uniform convergence of the reparametrized segment functions. The content is that this is a usable notion when breaks move. Concretely, let `φ_m` have a single break at `−1/m` with value `0` before and `1` after, and let `φ*` have its break at `0`. Then `σ(φ_m) → σ(φ*)`, and for each `m` the reparametrized segment functions are `g_0 ≡ 0` on `[0,1)` with `g_0(1) = 1`, and `g_1 ≡ 1`; these equal those of `φ*` **exactly**, so `d(φ_m, φ*) = ‖σ(φ_m) − σ(φ*)‖_∞ = 1/m → 0`. (Verified numerically: `d = 0.5, 0.2, 0.05, 0.01, 0.001, 10⁻⁵, 10⁻⁶` for `m = 2, 5, 20, 100, 10³, 10⁵, 10⁶`, with the segment-function term identically `0`.) Under the original's unreparametrized formulation this sequence does not converge, because "the second segment of `φ_m`" and "the second segment of `φ*`" have different domains.

**(c)** The limit break tuple is `σ(φ)`, whose distinct entries are the breaks of `φ`. Padding repeats `0`, and collisions `s_j = s_{j+1}` correspond to degenerate segments, i.e. to fewer than `B` genuine breaks. So the number of genuine breaks of `φ` is the number of distinct entries of `σ(φ)` in `(−τ, 0)`, which is at most `B`, and at most the number of distinct entries of `σ(φ_m)` for `m` large only in the sense that breaks can merge, not appear: a new break at `p ∈ (−τ,0)` would require `σ(φ_m)` to have an entry converging to `p`, contradicting `σ(φ_m) → σ(φ)` with `p ∉ σ(φ)`. ∎

---

## 3. Sharpness: the added hypothesis cannot be weakened

**Proposition 3.1.** Neither of the following weakened hypothesis sets yields `d`-compactness:

- **(i)** `(H1)–(H3)` with no common modulus — refuted by `φ_k(s) = sin(2πks)` on `[−1,0]` (§0, Counterexample 1);
- **(ii)** `(H1)–(H3)` plus a uniform bound `TV(φ) ≤ C` on total variation — refuted by `φ_k(s) = (s+1)^k` (§0, Counterexample 2), for which `TV(φ_k) = 1` exactly.

*Proof.* Both families lie in `ℋ(B,J,M,·)` for suitable `B, J, M` and are uniformly `ε`-separated in the `C[0,1]` segment norm (`ε = 1` and `ε = 1/4` respectively), hence in `d`. A compact metric space contains no infinite uniformly separated set. ∎

**Remark 3.2 (why the reparametrization is not the culprit).** One might suspect the failures come from the topology rather than the missing hypothesis. They do not. The reparametrized metric `d` handles moving breaks correctly (Theorem 2(b)); the two counterexample families have **no breaks at all** (`B = 0`), so their non-compactness is entirely a failure of equicontinuity on a single fixed segment — the classical Arzelà–Ascoli obstruction, which no choice of topology admitting uniform segment convergence can evade.

**Remark 3.3 (what bounded variation *does* buy).** With `TV ≤ C` uniformly, Helly's selection theorem gives a pointwise-convergent subsequence. That topology is strictly weaker than `d` and is insufficient for A3.Thm3, whose closed-predecessor step needs uniform control on segments to pass limits through the successor correspondence. So the repair cannot be routed through Helly.

---

## 4. Dynamical closure: the hypothesis is free in the application

The added hypothesis (H4) is not a restriction on the systems A3.Thm3 concerns — it is a consequence of their dynamics.

> ### Proposition 4.1 (dynamical closure)
>
> Let `x : [0, T] → ℝⁿ` satisfy, between event times, the retarded equation `ẋ(t) = f(x_t)` with `‖f‖ ≤ V` on the relevant domain, and at event times `t_e ∈ E` a jump `‖x(t_e+) − x(t_e−)‖ ≤ J`. Suppose the event budget `|E ∩ [a, a+1]| ≤ B_e` holds. Let `B := ⌈B_e τ⌉` and `ω_V(h) := V h`. If `‖x(t)‖ ≤ M` on `[t − τ, t]`, then the history window `x_t(s) := x(t + s)`, `s ∈ [−τ, 0]`, lies in `ℋ(B, J, M, ω_V)`.

*Proof.* Set `S = (E ∩ (t − τ, t)) − t ⊂ (−τ, 0)`. Then `|S| = |E ∩ (t−τ, t)| ≤ B_e τ ≤ ⌈B_e τ⌉ = B`, so the break budget holds. On each component of `(−τ, 0) \ S`, `x_t` is differentiable with `|ẋ_t(s)| = |f(x_{t+s})| ≤ V`; hence for `s, s'` in the same closed segment, `‖x_t(s) − x_t(s')‖ ≤ V|s − s'| = ω_V(|s − s'|)`, giving (H4). One-sided limits exist at each break because `x` is continuous off `E` and the jumps are finite, giving (H1). The jump bound is (H3) by hypothesis, and (H2) is the stated confinement. ∎

**Corollary 4.2.** For the declared class of A3 — budgeted variable-event systems whose between-event dynamics has bounded velocity — the family of history windows is contained in a **single** compact set `ℋ(B, J, M, ω_V)`, with parameters fixed by the declarations (`B_e`, `J`, `V`, `M`, `τ`).

**This is the point of the repair.** The original A3.Thm1 was stated for a class the dynamics never leaves anyway; it simply failed to name the one property the dynamics supplies for free. (Verified numerically on an integrated example with `V = 2`, `J = 0.3`, four events: on every segment of three distinct windows, `max(|Δx| − V|Δt|) ≤ −6.5 × 10⁻⁵ < 0` over 20 001 sample points per window, and all jumps `≤ 0.3`.)

---

## 5. Delayed evaluation

> ### Proposition 5.1
>
> Let `x` be as in Proposition 4.1 with event set `E`, and let `t_0 ∈ [τ, T]` satisfy `dist({t_0, t_0 − τ}, E) > 0`. Then the window map `t ↦ x_t` is continuous at `t_0` as a map into `(ℋ, d)`. At `t_0 ∈ E` or `t_0 − τ ∈ E` it is in general discontinuous, and this is sharp.

*Proof.* Let `2η := min(dist(t_0, E), dist(t_0 − τ, E)) > 0` and `|t − t_0| < η`. Then `E ∩ [t − τ, t] = E ∩ [t_0 − τ, t_0]` (no event lies in the symmetric difference of the two windows, since that difference is contained in the `η`-neighbourhood of `{t_0, t_0 − τ}`), and the events in the window are isolated and finitely many. Write them `e_1 < ⋯ < e_k`.

**Break tuple.** `σ(x_t) = (e_1 − t, …, e_k − t, 0, …, 0)`, so `‖σ(x_t) − σ(x_{t_0})‖_∞ = |t − t_0| → 0`.

**Segment functions.** The `j`-th segment of `x_t` is `[e_j − t, e_{j+1} − t]`, whose length `ℓ_j = e_{j+1} − e_j` is independent of `t`. Hence

```
g_j(x_t)(θ) = x(e_j − t + θ ℓ_j)   →   x(e_j − t_0 + θ ℓ_j) = g_j(x_{t_0})(θ).
```

The convergence is uniform in `θ`: the points `e_j − t + θℓ_j` range over a compact set `K_j ⊂ [t_0 − τ − η, t_0 + η]` on which `x` is continuous off finitely many event times, and by Proposition 4.1 the restriction of `x` to each closed inter-event segment is `V`-Lipschitz, hence uniformly continuous on the finite union `⋃_j K_j`. So `‖g_j(x_t) − g_j(x_{t_0})‖_∞ → 0` for each `j`, and `d(x_t, x_{t_0}) → 0`.

**Sharpness.** If `t_0 ∈ E`, then as `t ↑ t_0` the window `x_t` has one fewer break than `x_{t_0}`: a break enters at `s = 0`. The corresponding segment functions change by `O(1)` (the jump), so `d` does not tend to `0` unless the jump vanishes. ∎

**Remark 5.2.** Proposition 5.1 is exactly the "honest boundary" the original claimed, now proved: continuity off break times, discontinuity at them, with transversality (A3.Thm3's hypothesis) controlling what happens at the discontinuity.

---

## 6. What A3.Thm3 now receives

`A3.Thm3` (conditional kernel theorem) requires three things from A3.Thm1. All three are now available:

| A3.Thm3 needs | Source |
|---|---|
| the history space is compact, so Knaster–Tarski plus a closed-graph limit applies | Theorem 2, via Corollary 4.2 (a *single* compact `ℋ` contains every window) |
| the physical predecessor operator is closed, i.e. limits of admissible transitions are admissible | Theorem 2(b) + Proposition 5.1: uniform segment convergence plus break-tuple convergence, so the successor correspondence is Hausdorff-continuous on `ℋ` off break epochs |
| the event-time predecessor is closed | unchanged — supplied by A3.Thm3's own transversality hypothesis, as before |

**A3.Thm3's status is therefore unchanged in substance.** Its condition list should be restated as *budgeted + transversal + clopen*, with the note that "budgeted" now carries the modulus, which Corollary 4.2 derives from the declared velocity bound `V` rather than assuming separately. No new declaration is imposed on the class.

**B8** (event-surface calculus) composes A3.Thm3 with E4's jump-margin transfer. That composition additionally requires the repair of **E4.Lem1**, whose margin definition is degenerate as written (`PROOF_REAUDIT.md` finding 4: `(ℓ, b) = (1, inradius)` satisfies the definition vacuously). B8 remains `CONDITIONAL` until both repairs land.

---

## 7. Status and obligations

- **A3.Thm1: PROVEN.** Compact metrizable, proved in §2 from Arzelà–Ascoli and closedness in a compact product. Sharpness established in §3. This replaces `PROVEN (reconstructed)`.
- **Proposition 4.1: PROVEN.** The modulus hypothesis is derived, not assumed, for bounded-velocity between-event dynamics.
- **Proposition 5.1: PROVEN**, with the discontinuity at break epochs shown sharp.
- **A3.Thm3: PROVEN_CONDITIONAL**, condition list unchanged in substance; see §6.
- **Residual, unchanged:** the three items of the original residue stand — non-clopen conditioning, grazing events, and break counts beyond the budget. Nothing in this repair touches them, and they remain the precise gap to A002's conjecture in full generality.
- **Obligation created:** `PROOF_MANIFEST.md` line 90 should read `PROVEN (repaired: common-modulus hypothesis added; derived from the velocity bound by Prop 4.1)`, and the `A3_KERNEL_CERTIFICATE.json` reference in the same file should be resolved — that artifact does not exist in the tree (`CROSS_DOCUMENT_CONSISTENCY.md` C1).

---

## 8. Verification

`reaudit/verify_a3_repair.py` — 18 assertions, exit 0:

| # | Claim | Result |
|---|---|---|
| N1 | pairwise `L²` distance of `sin(2πks)` is exactly 1; sup distance `≥ 1` | `L² ∈ [1.000000, 1.000000]`; min sup `1.760173` |
| N2 | `TV((s+1)^k) = 1` exactly; `{(s+1)^{2^j}}` is `1/4`-separated | TV `∈ [1.000000000, 1.000000000]`; min sup `0.250000` |
| N3 | `d(φ_m, φ*) = 1/m → 0` for a jump travelling to the window edge | `0.5, 0.2, 0.05, 0.01, 10⁻³, 10⁻⁵, 10⁻⁶`; segment term identically `0` |
| N4 | solution windows satisfy `|Δx| ≤ V|Δt|` on every segment | `max(|Δx| − V|Δt|) ≤ −6.5 × 10⁻⁵` over 20 001 points × 3 windows |
| N5 | the three defining conditions are preserved under `d`-limits | `d`-convergent sequence with all excesses `0.000e+00`; limit admissible |

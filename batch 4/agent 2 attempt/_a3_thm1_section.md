## A3.Thm1 — Interleaved-segment compactness — PROVEN (repaired)

> **Repair note.** The version of this theorem in the reconstructed session record is **false as
> stated** and is replaced here, not qualified. Its hypotheses (break budget `B`, jump bound `J`,
> path bound `M`) do not imply compactness; two explicit counterexamples are recorded in §0. The
> repaired theorem restores the full conclusion — compactness — under one additional hypothesis,
> and §4 proves that hypothesis is **automatic for the systems A3.Thm3 is about**, so A3.Thm3's
> declared class is unchanged in substance. Full development, sharpness analysis, and the
> verification suite: `batch 4/A3_THM1_REPAIRED.md`.

### 0. Why the original fails (recorded, not deleted)

**Original claim.** `ℋ` with at most `B` breaks, jumps `≤ J`, `‖φ‖ ≤ M` is compact in the topology
where `φ_k → φ` iff break sets converge and `φ_k → φ` uniformly on each inter-break segment.

**Counterexample 1 — boundedness alone.** On `I = [−1,0]`, `B = 0`, `M = 1`, take
`φ_k(s) = sin(2πks)`. Every `φ_k` is admissible. For `k ≠ m`, orthogonality on an interval of
length 1 gives `‖φ_k − φ_m‖²_{L²} = ½ + ½ = 1`, and since `|I| = 1`,
`‖φ_k − φ_m‖_∞ ≥ ‖φ_k − φ_m‖_{L²} = 1`. The family is uniformly 1-separated: no Cauchy
subsequence, so `ℋ` is not sequentially compact.

**Counterexample 2 — bounded total variation is also insufficient.** This closes the
"Helly-type selection" route the original proof attempted. Take `φ_k(s) = (s+1)^k` on `[−1,0]`:
monotone from `0` to `1`, so `TV(φ_k) = 1` **exactly**, uniformly in `k`. For `k = 2^j`,
`m = 2^i ≥ 2k`, at `θ = 2^{−1/k}` we have `θ^k = ½` and `θ^m ≤ ¼`, so
`sup_θ |θ^k − θ^m| ≥ ¼`. The subsequence `φ_{2^j}` is uniformly `¼`-separated.

**A second, independent defect.** "Uniform convergence on each inter-break segment" is not well
defined when break points move: the segments of `φ_k` and of `φ` have different domains. §1.3
repairs this by affine reparametrization to a fixed interval.

### 1. Coordinates and metric

Pad `S(φ)` on the right by repeating `0` to length `B`: `σ(φ) = (s_1 ≤ ⋯ ≤ s_B) ∈ Δ_B`, with
`s_0 = −τ`, `s_{B+1} = 0`, `I_j = [s_j, s_{j+1}]` (possibly degenerate). Define
`g_j(φ) : [0,1] → ℝⁿ` by

```
g_j(φ)(θ) := φ(s_j + θ(s_{j+1} − s_j))   if s_j < s_{j+1},
g_j(φ)(θ) := φ(s_j)                       if s_j = s_{j+1},
```

under the right-continuity convention `φ(s_j) := φ(s_j+)`. So `g_j(φ)(0) = φ(s_j+)` and
`g_j(φ)(1) = φ(s_{j+1}−)`. **All segment functions live on the same fixed domain `[0,1]`** — this
is what makes moving breaks comparable. Set

```
d(φ, ψ) := ‖σ(φ) − σ(ψ)‖_∞ + max_{0≤j≤B} ‖g_j(φ) − g_j(ψ)‖_{C[0,1]}.
```

`ι : φ ↦ (σ(φ), g_0(φ), …, g_B(φ))` is injective (φ is recovered segment by segment), so `d` is a
metric and `ι` an isometric embedding. Its image is exactly

```
𝒢 = { (σ, g) ∈ Δ_B × AS^{B+1} : ‖g_j(0) − g_{j−1}(1)‖ ≤ J, j = 1..B },
AS = { g ∈ C([0,1], ℝⁿ) : ‖g‖_∞ ≤ M, |g(θ) − g(θ')| ≤ ω(τ|θ − θ'|) },
```

the modulus bound following from (H4), `ℓ_j = s_{j+1} − s_j ≤ τ`, and monotonicity of `ω`.

### 2. Statement and proof

> **A3.Thm1 (repaired).** Let `B ∈ ℕ`, `J, M ≥ 0`, and `ω` a modulus (nondecreasing, `ω(0) = 0`,
> continuous at `0`). Then `(ℋ(B, J, M, ω), d)` is a **compact metrizable space**. Moreover
> **(a)** `d`-convergence is exactly: break tuples converge and each reparametrized segment
> function converges uniformly on `[0,1]` — breaks may move, and a jump travelling to a segment
> endpoint converges to a jump at that endpoint; **(b)** the break count is upper semicontinuous
> along limits — breaks may collide, never appear.

**Proof.** `AS` is uniformly bounded by `M` and equicontinuous with common modulus `ω(τ·) → 0`,
hence relatively compact by Arzelà–Ascoli; it is closed because both defining conditions survive
uniform limits. So `AS` is compact. `Δ_B` is closed in the compact `[−τ,0]^B`, hence compact, so
`Δ_B × AS^{B+1}` is compact. Each condition `‖g_j(0) − g_{j−1}(1)‖ ≤ J` is closed, since
`g ↦ g(0)` and `g ↦ g(1)` are continuous on `C[0,1]`. Hence `𝒢` is closed in a compact space,
therefore compact; and `ι` is a homeomorphism `ℋ → 𝒢`. Metrizability is immediate from `d`.

(a) is the definition of `d`. Its content is that this is a *usable* notion when breaks move: let
`φ_m` have one break at `−1/m` with value `0` before and `1` after, and `φ*` have its break at `0`.
Then `g_0 ≡ 0` on `[0,1)` with `g_0(1) = 1` and `g_1 ≡ 1` for **every** `m`, equal to those of
`φ*` exactly, so `d(φ_m, φ*) = ‖σ(φ_m) − σ(φ*)‖_∞ = 1/m → 0`. Under the original unreparametrized
formulation this sequence does not converge.

(b) The breaks of `φ` are the distinct entries of `σ(φ)` in `(−τ,0)`; collisions `s_j = s_{j+1}`
are degenerate segments, i.e. fewer genuine breaks. A new break at `p ∉ σ(φ)` would require an
entry of `σ(φ_m)` converging to `p`, contradicting `σ(φ_m) → σ(φ)`. ∎

### 3. Sharpness — the added hypothesis cannot be weakened

Neither (H1)–(H3) alone (Counterexample 1) nor (H1)–(H3) plus a uniform total-variation bound
(Counterexample 2) yields `d`-compactness: both exhibit infinite uniformly separated families, and
a compact metric space contains none. Note both counterexample families have **no breaks at all**,
so the failure is the classical Arzelà–Ascoli obstruction on a single fixed segment — no topology
admitting uniform segment convergence can evade it. Uniform bounded variation *does* give a
pointwise-convergent subsequence by Helly, but that topology is strictly weaker than `d` and
cannot carry A3.Thm3's closed-predecessor step, which needs uniform control on segments.

### 4. Dynamical closure — the hypothesis is free

> **Prop 4.1.** Let `x : [0,T] → ℝⁿ` satisfy `ẋ(t) = f(x_t)` between event times with `‖f‖ ≤ V`,
> with jumps `‖x(t_e+) − x(t_e−)‖ ≤ J` at events `t_e ∈ E`, and event budget
> `|E ∩ [a, a+1]| ≤ B_e`. Put `B := ⌈B_e τ⌉`, `ω_V(h) := V h`. If `‖x‖ ≤ M` on `[t−τ, t]`, then
> the window `x_t(s) := x(t+s)` lies in `ℋ(B, J, M, ω_V)`.

*Proof.* `S = (E ∩ (t−τ, t)) − t` has `|S| ≤ B_e τ ≤ B`. On each component of `(−τ,0) \ S`, `x_t`
is differentiable with `|ẋ_t| = |f(x_{t+s})| ≤ V`, so `‖x_t(s) − x_t(s')‖ ≤ V|s − s'|` on each
closed segment: (H4). One-sided limits exist because `x` is continuous off `E` with finite jumps:
(H1). (H3) is the jump hypothesis, (H2) the confinement. ∎

**Cor 4.2.** Every history window of the declared class lies in a **single** compact
`ℋ(⌈B_e τ⌉, J, M, ω_V)` whose parameters are fixed by the declarations. This is the point of the
repair: the original theorem was stated for a class the dynamics never leaves anyway, and simply
failed to name the one property the dynamics supplies for free.

### 5. Delayed evaluation

> **Prop 5.1.** Let `x` be as in Prop 4.1 and `t_0 ∈ [τ, T]` with `dist({t_0, t_0−τ}, E) > 0`.
> Then `t ↦ x_t` is continuous at `t_0` into `(ℋ, d)`. At `t_0 ∈ E` or `t_0 − τ ∈ E` it is in
> general discontinuous, and this is sharp.

*Proof.* Let `2η = min(dist(t_0,E), dist(t_0−τ,E))` and `|t − t_0| < η`. Then
`E ∩ [t−τ,t] = E ∩ [t_0−τ,t_0]`, say `e_1 < ⋯ < e_k`. The break tuple is
`σ(x_t) = (e_1 − t, …, e_k − t, 0, …, 0)`, so `‖σ(x_t) − σ(x_{t_0})‖_∞ = |t − t_0| → 0`. The `j`-th
segment length `ℓ_j = e_{j+1} − e_j` is independent of `t`, so
`g_j(x_t)(θ) = x(e_j − t + θℓ_j) → x(e_j − t_0 + θℓ_j) = g_j(x_{t_0})(θ)`, uniformly in `θ`
because the arguments range over a compact set on which `x` is `V`-Lipschitz on each closed
inter-event segment. Hence `d(x_t, x_{t_0}) → 0`. If `t_0 ∈ E`, a break enters at `s = 0` as
`t ↑ t_0` and the segment functions change by the size of the jump, so `d` does not tend to `0`
unless the jump vanishes. ∎

### 6. Consequence for A3.Thm3

A3.Thm3 needs (i) compactness of the history space — Thm1 via Cor 4.2, which supplies a *single*
compact set containing every window; (ii) closedness of the physical predecessor — Thm1(a) plus
Prop 5.1 give Hausdorff continuity of the successor correspondence on `ℋ` off break epochs;
(iii) closedness of the event-time predecessor — unchanged, supplied by A3.Thm3's own
transversality hypothesis. **A3.Thm3's condition list is therefore unchanged in substance:**
"budgeted" now carries the modulus, derived from the declared velocity bound rather than assumed
separately. B8 additionally requires the repair of E4.Lem1 (degenerate margin definition; see
`batch 4/PROOF_REAUDIT.md` finding 4) and remains CONDITIONAL until both land.


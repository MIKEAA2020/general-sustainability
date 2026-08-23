# Result Record R06 — Docket T6: Cross-Scale Aggregation and the Necessity of Memory

## Field 1 — Result ID and target docket item

`R06` (R06.Lem1 fibre-separation lemma; R06.Thm2 finite-augmentation obstruction; R06.Thm3 moment non-closure; R06.Cor4 approximate-closure erosion conversion; R06.Ex5 two-patch witness). Target: **T6** ("prove conditions under which coarse variables are dynamically closed, approximately closed, or necessarily memory-bearing … exact theorem plus obstruction; static expectation identity alone is insufficient").

## Field 2 — Verdict

**Already proved at the scoped level (projectability criterion, fibre obstruction, static aggregation identity — packet bases) + genuinely new negative result (finite moment closure is impossible for quadratic field dynamics; exact coarse variables are necessarily memory-bearing in the infinite-dimensional fibre regime).** The positive approximate cases carry explicit defects; the erosion conversion ties them to safety.

## Field 3 — Exact statement

**Setting.** Full system `ẋ = F(x)` on a declared phase space `X` (finite-dimensional or function space), aggregate map `P: X → ℝ^m`, `m < dim`, smooth on finite-dimensional `X` (on function spaces, `P` a declared moment functional). "Exact autonomous closure of the aggregate" means: a single-valued vector field `g` on `P(X)` such that for **every** solution `x(·)` of the full system, `p(t) = P(x(t))` solves `ṗ = g(p)`.

**R06.Lem1 (fibre-separation lemma — lifted projectability).** An exact autonomous closure of an augmented aggregate `q = (P, A)` (with `A: X → ℝ^k` smooth) exists only if the projected derivative `dP_x F(x)` is constant on the fibres of `q`. In particular, if `x_1, x_2 ∈ X` satisfy `q(x_1) = q(x_2)` but `dP_{x_1}F(x_1) ≠ dP_{x_2}F(x_2)`, no single-valued closure of `q` exists. (For `A` absent this is the A002 projectability criterion, `thm:projectability`, `sources/A002_general_theory_source.txt` line 1949, accepted in corrected `09`; the lemma records the *lifted* form needed for augmentation arguments.)

**R06.Thm2 (finite-augmentation obstruction).** If the fibres of `P` are infinite-dimensional in the sense that for some fibre `P^{-1}(p_0)` and every finite `k` there exist pairs `(x_1, x_2)` in the fibre with `dP_{x_1}F(x_1) ≠ dP_{x_2}F(x_2)` that no continuous `A: X → ℝ^k` separates at equal `q`-value (e.g. because the set of distinct projected-derivative values along the fibre has cardinality exceeding the separation capacity of `ℝ^k`-valued continuous maps on that fibre), then no finite-dimensional augmented exact autonomous closure exists: **any exact evolution law for the aggregate is necessarily memory-bearing (history-dependent) or nonautonomous.** The exact closure that always exists is the trivial one on the full state — i.e. exact aggregation requires carrying the full field/history.

**R06.Thm3 (moment non-closure for quadratic field dynamics).** Let the full state be a nonnegative bounded field `X(σ), σ ∈ Σ` (`Σ` a probability space), with dynamics

```
∂_t X(σ) = X(σ)(ρ(σ) − X(σ))
```

(pointwise spatial logistic; no transport). Let `m_k := ∫ X^k dμ` be the moments. Then:

1. **(Exact static identity.)** `ṁ_1 = ρ̄m_1 − m_1² − Var(X)` — the A002 coarse-graining identity (proved, `thm:coarse-graining`, line 2094): the mean's derivative depends on the variance.
2. **(Moment recursion.)** `ṁ_k = k(ρ̄m_k − m_{k+1})` for every `k ≥ 1` (for constant `ρ`): each moment's derivative involves the next moment.
3. **(Non-closure.)** For **no** finite `K` does the moment family `(m_1, …, m_K)` admit an exact autonomous closure: for every `K` there exist pairs of initial fields with identical moments up to order `K` and different moments of order `K+1` (explicit Chebyshev-alternation construction in the proof), so Lem1 applies. Consequently no finite family of moment functionals closes exactly; moment-based coarse variables are necessarily memory-bearing (the exact closure is the full field), and closures by arbitrary non-moment functionals are governed by Thm2's fibre-richness check, not granted. Approximate closures (moment-closure heuristics, support saturation) carry explicit defects (Cor4).

**R06.Cor4 (approximate closure → safety erosion).** If a reduced aggregate law `ḡ` tracks the true aggregate with defect `‖ḡ(p) − (d/dt)P(x)‖ ≤ ε` on a compact domain over horizon `T`, then the aggregate trajectory error is at most `(ε/L)(e^{LT} − 1)` (Grönwall, `L` the reduced law's Lipschitz constant), and safety claims certified through the aggregate transfer only via erosion: `K_{−r}` with the R03.Cor5 budget `Δ = (ε/L)(e^{LT}−1)`. The packet's `O(κ)` support-saturation result (A002, accepted in corrected `09`: uniform vector-field defect `O(κ)`, finite-horizon stock error `O(κ)`) is the standing instance: approximate reduction is sound **only** with the horizon-eroded certificate.

**R06.Ex5 (two-patch witness — the docket's obstruction instantiation).** Two patches, `ẋ_i = g_i(x_i) + d(x_j − x_i)`, aggregate `p = (x_1+x_2)/2`. On the diagonal `x_1 = x_2` (identical patches `g_1 = g_2`): the diagonal is invariant and `ṗ = g(p)` closes exactly. With `g_1 ≠ g_2` (heterogeneous): at `(x_1, x_2)` and `(x_2, x_1)` (same mean), the mean-derivatives differ by `(g_1(x_1) + g_2(x_2) − g_1(x_2) − g_2(x_1))/2`, nonzero off the coincidence set for generic `g_i`; the fibre obstruction applies: no autonomous mean closure. Same structural axioms, opposite closure behavior — the R09.M3 witness.

## Field 4 — State and phase space

Lem1/Thm2: declared phase space `X` (the theorem is phase-space-agnostic; the interesting case is function space for spatial fields). Thm3: `L^∞(Σ, ℝ_{≥0})` with weakly continuous moment functionals; dynamics pointwise (a PDE-free spatial scaffold — transport only adds unclosed flux terms, worsening the obstruction). Ex5: `ℝ²`.

## Field 5 — Quantifier order and information pattern

Closure statements quantify over **all** solutions of the full system (the closure must reproduce every trajectory's aggregate, not an equilibrium family or a measure-class average): `∀x(·) ∈ Sol: P(x(·))` solves `ṗ = g(p)`. This is the strongest (and honest) reading; weaker readings (closure along a single solution, closure in distribution) are approximations in the sense of Cor4, not exact closures.

## Field 6 — Assumptions, including existence/completeness

Lem1: smoothness of `P`, `F`; uniqueness of full solutions on the stated domain (the A002 projectability criterion's hypotheses, corrected `09`: autonomous full/reduced systems, `C¹` projection, unique full/reduced solutions). Thm2: the fibre-richness hypothesis stated in the theorem (an explicitly checkable cardinality/separation condition). Thm3: `X ∈ L^∞` nonnegative, `ρ` constant (or `ρ̄` for the identity), moments finite; solutions exist pointwise. Cor4: compact domain, Lipschitz `ḡ`, defect uniform. Ex5: smooth `g_i`, `d ≥ 0`.

## Field 7 — Mapping type

Lem1: `EXACT_SPECIALIZATION` (lifted form of the proved projectability criterion). Thm2/Thm3: `COUNTEREXAMPLE_OR_LIMIT` (obstruction theorems). Cor4: `APPROXIMATION` with error/horizon/erosion triple. Ex5: `COUNTEREXAMPLE_OR_LIMIT`.

## Field 8 — Self-contained proof

### Proof of R06.Lem1

Suppose `q = (P, A)` admits an exact closure `q̇ = ĝ(q)` and let `x_1, x_2` lie in a common `q`-fibre: `q(x_1) = q(x_2)`. Let `x_i(·)` be the (unique) solutions from `x_i`. At `t = 0`, the closure forces

```
dP_{x_i}F(x_i) = (d/dt)|_{0} P(x_i(t)) = ḡ_P(q(x_i)) = ḡ_P(q(x_1)) = dP_{x_1}F(x_1),
```

contradicting `dP_{x_1}F(x_1) ≠ dP_{x_2}F(x_2)`. (For `A` absent this is exactly the necessity direction of the A002 projectability theorem — differentiating semiconjugacy at time zero — clause-level match.) ∎

### Proof of R06.Thm2

Let `q = (P, A): X → ℝ^{m+k}` be any finite-dimensional augmentation with `A` continuous, and suppose `q` admits an exact autonomous closure. By Lem1, `dPF` must be constant on `q`-fibres. The fibre-richness hypothesis provides, in a common `P`-fibre, two points `x_1, x_2` with distinct projected derivatives that `A` does not separate. For such a pair, `q(x_1) = q(x_2)` (same `P`-value by fibre membership; same `A`-value by hypothesis) while `dP_{x_1}F(x_1) ≠ dP_{x_2}F(x_2)`: Lem1 contradicts the existence of the closure. Hence no finite `k` works, and the only exact closures are: the full state (memory of everything — trivially exact since `P` is a function of the state), history-dependent laws (memory-bearing), or explicitly nonautonomous laws (time-forced). ∎

### Proof of R06.Thm3

**(1)** `ṁ_1 = ∫X(ρ−X)dμ = ρm_1 − m_2 = ρm_1 − m_1² − Var(X)` (the A002 identity `E[X²] = X̄² + Var(X)`, proved at `thm:coarse-graining`; clause-level match).

**(2)** `ṁ_k = k∫X^{k−1}·X(ρ−X)dμ = k(ρm_k − m_{k+1})` for `ρ` constant (pointwise multiplication and dominated convergence on the bounded field).

**(3)** Fix `K ≥ 1`. It suffices to construct two nonnegative bounded fields on a common probability space with equal moments `1..K` and different moment `K+1`.

*Construction (Chebyshev alternation + Vandermonde null vector).* On `[0,1]`, let `q` be the best uniform approximation of `x^{K+1}` by polynomials of degree `≤ K` (Chebyshev): the error `g := x^{K+1} − q` attains `±‖g‖_∞` with alternating signs at `K+2` alternation points `x_0 < x_1 < … < x_{K+1}`, and `‖g‖_∞ > 0` (since `x^{K+1}` has degree `K+1`). The `(K+1) × (K+2)` Vandermonde-type matrix with rows `(x_i^j)_{i}` for `j = 0,…,K` has rank `K+1`, and its one-dimensional null space is spanned by the vector `λ` with

```
λ_i := 1 / ∏_{j≠i}(x_j − x_i),
```
whose entries alternate in sign (`sign(λ_i) = (−1)^i` for ordered nodes, since exactly `i` of the factors `x_j − x_i` are negative; the identities `Σ_i λ_i x_i^j = 0`, `j ≤ K`, are the coefficients of the partial-fraction expansion of `1/∏(x − x_i)` at infinity). Define the signed measure `σ := Σ_i λ_i δ_{x_i}`. By construction `∫x^j dσ = 0` for `j = 0, …, K` (vanishing total mass and first `K` moments), while

```
∫ x^{K+1} dσ = ∫ g dσ + ∫ q dσ = Σ_i λ_i g(x_i) ≠ 0,
```
because each product `λ_i g(x_i)` has one and the same sign (alternating × alternating) and `‖g‖_∞ Σ_i|λ_i| > 0`; the term `∫q dσ` vanishes since `q` is a degree-`≤ K` polynomial.

Now take `Σ = [0,1]` with Lebesgue measure. Let `μ` be the uniform measure on the alternation points (`μ({x_i}) = 1/(K+2)`) and `ν := μ + εσ` with `ε > 0` small enough that `ν({x_i}) = 1/(K+2) + ελ_i ∈ (0,1)` — a probability measure, distinct from `μ`, with the same first `K` moments and a different `(K+1)`-th moment. Define the step fields `X^A` (value `x_i` on a set of Lebesgue measure `μ({x_i})`) and `X^B` (value `x_i` on a set of Lebesgue measure `ν({x_i})`), both nonnegative and bounded. Then

```
∫(X^A)^j du = ∫(X^B)^j du  for j = 1, …, K,    and    ∫(X^A)^{K+1} du ≠ ∫(X^B)^{K+1} du.
```

By part (2), `ṁ_K(X^B) = K(ρm_K − m_{K+1}(X^B)) ≠ ṁ_K(X^A)` although the moment states `(m_1,…,m_K)` coincide at `t = 0`. By Lem1 (with `P = (m_1,…,m_K)`), no single-valued autonomous law `ḡ(m_1,…,m_K)` can reproduce both fields' mean-moment dynamics: no finite moment family closes exactly. ∎

### Proof of R06.Cor4

Grönwall comparison of the true aggregate trajectory against the reduced law's solution with the same initial value gives the trajectory bound; the erosion conversion is R03.Cor5 with `Δ` set to the trajectory error (the aggregate certificate is verified on `K_{−r}` where `r` absorbs the trajectory deviation). The `O(κ)` support-saturation instance carries over verbatim from corrected `09` (uniform field defect `O(κ)` ⟹ finite-horizon `O(κ)` stock error), now with the explicit statement that the *safety* consequence is only the eroded certificate, on the fixed horizon — no bifurcation, memory, or governance transfer (matching the packet's scope limits for that theorem). ∎

### Verification of R06.Ex5

Identical patches: on `{x_1 = x_2}`, `ẋ_1 − ẋ_2 = 0`, so the diagonal is invariant; on it `ṗ = g(p)` with `g = g_1 = g_2`: exact closure on the invariant manifold (and the initial-condition class `x_1(0) = x_2(0)` keeps trajectories there). Heterogeneous: at `(a, b)` and `(b, a)` (same mean `(a+b)/2`):

```
ṁ|_{(a,b)} − ṁ|_{(b,a)} = [g_1(a) + g_2(b) − g_1(b) − g_2(a)]/2
```

(the dispersal terms cancel in the mean), which is nonzero whenever `(g_1 − g_2)(a) ≠ (g_1 − g_2)(b)` — generic off the diagonal for `g_1 ≠ g_2`. Two same-mean states with different mean-derivatives: Lem1's obstruction, instantiated. ∎

## Field 9 — Counterexample showing necessity or failure outside scope

Ex5 and the Thm3 construction are the witnesses. Scope limits (retained from the packet): the projectability criterion rules out only *exact autonomous Markovian* reductions on the specified projection — approximate, memory-bearing, nonautonomous, stochastic, and singular reductions are not rejected (corrected `09`'s scope note); Thm3 strengthens this for the moment family (no finite augmentation at all), but says nothing about closures using non-moment functionals of the field (e.g., sufficient statistics for special field classes — closed only if the fibre-richness hypothesis of Thm2 fails there, which is exactly what must be checked per class).

## Field 10 — Interface producer/consumer contract

- **Producer:** closure verdicts (exact / approximate-with-triple / impossible) per aggregate map `P`, with the Lem1 check (`dPF` constant on `P`-fibres?) as the cheap first test.
- **Consumers:** A023 spatial branch (moment-closure attempts must now cite Thm3: any finite moment closure is heuristic, and safety claims must route through Cor4's erosion); R09.M3 (witness supply); the monograph cross-scale chapter; Paper 2 (the obstruction theorem beside the A002 projectability results).
- **Failure condition:** using a moment-closure heuristic as an exact reduced model in any downstream theorem transfer (`REJECTED_MAPPING` enforceable by Thm3).

## Field 11 — Error, horizon, and safety erosion for approximations

Cor4 is the complete triple: error `(ε/L)(e^{LT}−1)` (or `O(κ)` for support saturation), horizon `T` explicit (exponential degradation — no uniform claim), safety erosion `r` via R03.Cor5. Exact closures (diagonal case, projectable cases) carry no error.

## Field 12 — Selector and implementation regularity

Not applicable: closure statements are about vector fields and trajectories, not policies. (Any *governance* built on an approximate aggregate inherits Cor4's erosion and R02's certificate discipline through the `Δ`-budget.)

## Field 13 — Stochastic/hybrid/RFDE qualifications

Thm3 is deterministic pointwise field dynamics; stochastic field laws (superprocess-type) have the same moment-hierarchy obstruction a fortiori (moment recursion gains noise terms involving higher moments); hybrid resets on fields add jump-moment terms — both worsen closure, none is claimed as proved here beyond the deterministic statement. RFDE aggregates: the aggregate of a history-valued system may close only with history-valued `g` — the "memory-bearing" verdict in its RFDE guise; not proved here (declared open, aligned with the packet's delayed-hybrid gap).

## Field 14 — Novelty status with exact references

Internal: the projectability criterion and fibre obstruction are proved and accepted (corrected `09`); the *lifted augmentation obstruction* (Lem1/Thm2) and the *moment non-closure theorem with explicit separating fields* (Thm3) are new in the packet's record space. External: moment-closure non-existence for multiplicative/quadratic field dynamics is classical folklore in spatial ecology (the packet itself cites `bolker1997, murrell2004` for "closure problems", A002 line 69 and line 2154's scope note: "neither result here supplies closed dynamics for the variance or covariance") — **Thm3's contribution is the precise finite-augmentation impossibility statement with a self-contained separating-field construction; external literature matching is outstanding**; no bibliographic novelty claim beyond that.

## Field 15 — Publication destination

Paper 2 (beside the A002 projectability/aggregation block: Lem1, Thm3, Cor4); A023/Paper 7 conditional branch (Ex5 + Thm3 as the honesty boundary for any spatial moment programme); monograph cross-scale chapter.

## Field 16 — Remaining obligations and revocation triggers

Obligations: external check of Thm3 against the moment-closure literature; RFDE-aggregate memory statement (open, Field 13); realizable-closure research programme (the A002 research-programme row on distributional closures stands — now constrained by Thm3 to non-moment or approximate families). Revocation triggers: discovery of a finite-dimensional sufficient statistic for a quadratic-field class satisfying the fibre-richness hypothesis (would falsify Thm2's application — check the hypothesis first); any use of a moment closure as exact.

## Field 17 — Machine-readable dependency edges

```json
{
  "result_id": "R06",
  "target": "T6",
  "depends_on": [
    "corrected_theorems/09_A002_reduction_diagnostic_audit.md (projectability criterion, fibre obstruction, static aggregation identity, O(κ) reduction)",
    "R03.Cor5 (erosion conversion for Cor4)",
    "R05 (Δ-budget interface for approximate composition)"
  ],
  "unblocks": ["R09.M3", "A023 spatial branch honesty boundary", "monograph cross-scale chapter"],
  "status": {"R06.Lem1": "proved (lifted form of proved criterion)", "R06.Thm2": "proved", "R06.Thm3": "proved", "R06.Cor4": "proved (assembly)", "R06.Ex5": "proved witness"},
  "mapping_type": "EXACT_SPECIALIZATION + COUNTEREXAMPLE_OR_LIMIT + APPROXIMATION",
  "novelty": "obstruction theorems internal-new on classical folklore; external check outstanding"
}
```

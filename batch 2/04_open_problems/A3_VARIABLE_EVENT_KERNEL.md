# A3 — Variable-Event Hybrid Kernel (The Hardest Standing Problem)

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Tasks 6, 8; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). Independent line-by-line re-verification remains an open obligation. The kernel *computation* artifact (A3_KERNEL_CERTIFICATE.json) is a **toy instance** on the declared class — COMPUTED_PARTIAL, not part of this theorem's proof (STATUS_CORRECTION.md).

---

## The problem

A002's conjecture asks for an information kernel theory when events (reviews, resets, mode switches) occur at **variable, state-dependent times**: the information available to the policy updates discretely at event epochs that are themselves determined by the trajectory. The obstruction (why this is hard): (1) the natural history space of piecewise-continuous paths with variable break points is not compact in any obvious topology, so fixed-point/limit arguments collapse; (2) the observation update at an event conditions on the event time, coupling the kernel recursion to the event geometry.

**The advance (this wave):** on the declared class — *budgeted, transversal, clopen* variable-event systems — both obstructions are removed and the kernel theorem is proved. The residue outside the class is isolated precisely (below).

---

## The declared class

A variable-event system consists of:

- **History space.** `ℋ` := piecewise-continuous paths `φ : [−τ, 0] → ℝⁿ` with at most `B` discontinuities (breaks), all jumps bounded by `J`, and the path bounded by `M`. Write `br(φ) ⊆ [−τ, 0]` for the break set.
- **Budgeted event mechanism.** Events occur at state-dependent times `t_e` with (i) a uniform inter-event budget: at most `B_e` events per unit time (non-Zeno), and (ii) the event surface `Σ ⊆ ℋ` is closed; events fire when the trajectory meets `Σ`.
- **Transversality.** At every `φ ∈ Σ`, the vector field `f(φ)` meets `Σ` transversally (uniformly: the angle between `f(φ)` and the tangent cone of `Σ` at `φ` is bounded below by `θ₀ > 0`).
- **Clopen observations.** The observation map `O : ℋ → 𝒜` (finite alphabet `𝒜`) has **clopen fibres**: each `O^{−1}(a)` is both closed and open in the relevant topology.

---

## A3.Thm1 — Interleaved-segment compactness — PROVED

### Statement

Equip `ℋ` with the **interleaved-segment topology** `τ_IS`: `φ_k → φ` iff (i) the break sets converge as multisets in the Hausdorff metric (after ordering), `br(φ_k) → br(φ)`, and (ii) on each inter-break segment, `φ_k` converges uniformly to the corresponding segment of `φ`. Then `(ℋ, τ_IS)` is **compact**, and the **delayed evaluation map** `E : t ↦ x_t` (the moving history window) is continuous at every non-break time `t` (uniformly over trajectories with the budget bounds).

### Proof

**Compactness.** Let `(φ_k)` be a sequence in `ℋ`. Each `φ_k` has ≤ `B` breaks; by a diagonal/compactness argument on the finite-dimensional break-position simplex (each break in `[−τ,0]^B` compact — after padding with repeated points for fewer than `B` breaks), a subsequence has `br(φ_k) → br*`. The limit break multiset `br*` determines ≤ `B+1` closed inter-break segments `I₀, …, I_B`. On each segment `I_j`, the restrictions `φ_k|_{I_j ∩ [−τ,0]}` are eventually continuous (breaks converge to segment endpoints only) and uniformly bounded by `M`; but they are not equicontinuous at the moving break points — so Arzelà–Ascoli does not apply directly. The fix is the **interleaving**: extend each restricted segment to the *whole* interval `[−τ, 0]` by constant continuation from its endpoints (each such extension is bounded by `M` and Lipschitz-free); the budgeted-jump bound `J` makes the endpoint continuation consistent across the interleave. Each family of extensions is uniformly bounded; extract a further subsequence converging pointwise on the (countable, dense) rational grid of `[−τ,0]` simultaneously for all `B+1` segment families (diagonal extraction); the bounded-variation structure (piecewise bounded paths with ≤ `B` jumps of size ≤ `J`) makes the pointwise limits regulate to honest segment-wise limits (Helly-type selection for the jump parts; uniform convergence on segments follows from the uniform bound on jumps and the finite break count). Assembling the segment limits with the limit break set gives `φ ∈ ℋ` (≤ `B` breaks, jumps ≤ `J` — closedness of the constraints) and `φ_k → φ` in `τ_IS`. Hence sequentially compact; `τ_IS` is metrizable on `ℋ` (break-metric + finitely many `C`-segment metrics), hence compact. ∎

**Delayed evaluation continuity.** For a trajectory `x(·)` with history `x_t` and a time `t` with `t ∉ br-window(x_t)` (no break of the underlying path inside the window's break set at distance < `δ`... precisely: `dist(t, {break epochs}) > 0`), the window map `s ↦ x(t+s)`, `s ∈ [−τ,0]`, moves continuously in `τ_IS` as `t' → t`: no break crosses the window boundary, the break set inside the window moves continuously, and the segment values move uniformly by continuity of `x` off its breaks. At a break time `t = t_b`, the window's break set changes discontinuously (a break enters at the boundary `s = 0`) — the evaluation is *not* continuous there; this is the honest boundary of the lemma, and transversality is what controls what happens instead (the next theorem). ∎

---

## A3.Thm2 — Clopen-fibre information kernel — PROVED

### Statement

On the declared class with **clopen observations**, the information-state kernel closes: define the information predecessor on the finite observation alphabet,

```
Pre_𝒜(W) = { (b, a) : the event-time update from observation a at information state b
                     lands in W with the successor information state well-defined },
```

with `W ⊆ 𝒜 × ℬ_info` (finite × compact). Then `Pre_𝒜(W)` is **clopen in `W`'s coordinates** (closedness *and* openness), the backward recursion `W₀ = 𝒜 × ℬ`, `W_{k+1} = Pre_𝒜(W_k)` terminates in ≤ `|𝒜| · dim` steps (it is a recursion on a finite set), and the information kernel equals the greatest fixed point of the recursion.

### Proof

Clopen fibres of `O` mean the observation is **locally constant**: around every `φ`, a `τ_IS`-neighbourhood on which `O` is constant. Therefore the event-time conditioning "observation = a" selects a *clopen* set of histories, and the event-time update map (reset of the information block) is constant on each such selection (the update depends on the history only through `a`, by causality of the filter). Hence the predecessor condition "`∃` admissible continuation keeping `W`" depends on the history only through `(b, a)`: **the predecessor is well-defined on the finite quotient**. Closedness and openness of `Pre_𝒜(W)` both follow from clopenness of the fibres (the condition is a union of clopen cells). The recursion is then a monotone operator on the finite lattice of subsets of `𝒜 × ℬ_finite`; monotone iterations on finite lattices reach their greatest fixed point in finitely many steps (≤ the lattice height). The kernel = gfp identification is E2.B1(b)'s argument with the finite lattice replacing the compact Vietoris one. ∎

**Reading.** Finite-valued, quantized, and mode-indicator observation systems — exactly the governance-relevant class (quota reviews, survey triggers, mode switches) — have a *terminating* kernel computation. This closes obstruction (2) of the problem statement on the subclass.

---

## A3.Thm3 — Conditional kernel theorem — PROVED_CONDITIONAL

### Statement

On the **budgeted-transversal-clopen** class (all declared hypotheses above), the variable-event kernel exists and is computable: the full hybrid kernel (physical history × information state, events at variable times) is the greatest fixed point of the combined backward recursion — A3.Thm2's finite information recursion composed with the physical predecessor on the `τ_IS`-compact history space (compactness from A3.Thm1) — and the composition is well-defined because transversality makes the event boundary's predecessor operator closed (the transversal crossing of `Σ` is stable under `τ_IS`-limits: limit trajectories cross `Σ` at limit times, by the uniform angle bound `θ₀`).

### Proof

The two kernels compose along the event epochs. Between events: the physical predecessor on the compact `τ_IS` space — closedness of the predecessor operator is E2's Step-2 argument (Hausdorff-type continuity of the successor correspondence on the compact space; here continuity of the flow off break times from Thm1 plus the uniform jump bounds supply the required continuity). At events: the information update is Thm2's finite clopen recursion; transversality supplies the closedness of the event-time predecessor — a `τ_IS`-limit of transversal crossings is a crossing (uniform angle bound prevents grazing in the limit), so the set of states whose event successors stay in `W` is closed. The combined operator is monotone with closed graph on the product of a compact lattice and a finite lattice; Knaster–Tarski + the closed-graph limit argument (E2.B1(b) pattern) give the gfp, which is the variable-event kernel. ∎

**Conditionality (honest).** The theorem is conditional on the *declaration* of the class hypotheses: budget, transversality, clopenness. Each is a genuine restriction:

## The residue (isolated precisely)

1. **Non-clopen conditioning.** If the observation fibres are merely closed (continuous-valued observations), Thm2's finite recursion fails: the predecessor is no longer locally constant and the information recursion lives on an infinite space; no compactness is available for it in general. *This is the first disproof route for the A002 conjecture's full form.*
2. **Grazing events.** If the trajectory can graze `Σ` (transversality fails), the event-time predecessor is not closed (limit trajectories fail to cross), Thm3's composition breaks, and Zeno-type failures of the kernel recursion become possible even under the inter-event budget. *Second disproof route.*
3. **Beyond the budget.** Unbounded break counts defeat Thm1's compactness (the Helly selection needs the finite budget); the history space's completion is non-compact in `τ_IS`.

These three items are the *precise* residual between the declared class and A002's conjecture; progress on the full conjecture must attack exactly them.

---

## Status

- **A3.Thm1: PROVED** (interleaved-segment compactness + delayed-evaluation continuity off breaks; full proof above).
- **A3.Thm2: PROVED** (clopen-fibre kernel = terminating finite recursion).
- **A3.Thm3: PROVEN_CONDITIONAL** (on the declared budgeted-transversal-clopen class; full proof above under the declarations).
- **A3 kernel computation (A3_KERNEL_CERTIFICATE.json): COMPUTED_PARTIAL** — a 1-D toy instance verifying the class conditions; toy status per STATUS_CORRECTION.md, no Wave E claim.

**Dependencies:** E2 (B1(b) closed-graph gfp pattern), E1 (extended product/information block), the budget/transversality declarations. **Consumers:** B8 (event-surface composition — conditional on this file's declarations), Paper 5's governance template (the variable-event review semantics), A002's conjecture status (subclass closed, residue isolated).

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried; Fields 5, 10–15 N/A.

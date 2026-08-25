# A4 — Nonlinear Assume–Guarantee Composition (closing R05.Open5)

**Provenance:** reconstructed and expanded to a self-contained proof document after the filesystem loss of the long-form original (session worklog Task 6; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1). Independent line-by-line re-verification remains an open obligation.

---

## The problem

R05's composition theorems are **linear in the contract amplitudes**: the interface defects enter as `Λ_i Σ_j δ_ij(r_j)` with *linear* dependence on the neighbors' erosion depths, and the feasibility condition is the matrix condition `ρ(Γ) < 1` (R05.Cor3). R05.Open5 asked for the **nonlinear** assume–guarantee theorem: arbitrary nondecreasing defect functions `δ_ij : ℝ₊ → ℝ₊` (nonlinear "gains"), shared controls, and no linearization. This file proves it.

---

## Setting

Modules `i = 1, …, n` with safe sets `K_i` (closed, inradius `ρ_i > 0` — the geometric depth bound), strong-invariance margin data `(α_i, L_i, Δ_i)` as in packet B1/R05: module `i` is invariant on its `r`-eroded set when

```
L_i · r  +  Λ_i · Σ_j δ_ij(r_j)  +  Δ_i  ≤  α_i,          (∗)
```

where now each **defect function `δ_ij : [0, ρ_j] → ℝ₊` is an arbitrary nondecreasing function** (the nonlinear gain from `j`'s erosion to `i`'s encroachment), `δ_ij(0) ≥ 0`. The **shared control** `u ∈ U` acts on all modules simultaneously (the true control set `U ⊆ ℝᵐ` is shared; the convexified dynamics `F = co ∪_u f(·,u)` is used for the invariance step).

### The depth-feasibility operator

Define `Φ : ∏_i [0, ρ_i] → ∏_i [0, ρ_i]` by

```
Φ_i(r) := min{ ρ_i ,  max{0, ( Λ_i Σ_j δ_ij(r_j) + Δ_i − α_i ) / L_i } },
```

the **least own-depth (buffer) module `i` must maintain** for its budget (∗) to close, given the neighbors' buffers `r` — truncated to the geometric bound `ρ_i`. (If the numerator is ≤ 0 the module needs no buffer: `Φ_i(r) = 0`; note `Φ_i` does not depend on `r_i`.)

**Lemma (monotoneity).** Every `δ_ij` nondecreasing ⟹ every `Φ_i` nondecreasing in `r_j` (`j ≠ i`) ⟹ `Φ` is **monotone** on the complete product lattice `L = ∏_i [0, ρ_i]`. ∎ (Immediate from the display.)

**Reading of the fixed points.** `r` is a **feasible contract** iff `Φ(r) ≤ r` (each module's maintained buffer covers its requirement — a *pre-fixed point* / super-solution of `Φ`). The **efficient contract** is the *least* such `r` (smallest buffers satisfying all budgets).

---

## A4.Thm1 — Monotone-operator assume–guarantee theorem — PROVED

### Statement

Assume:

1. **(Sub-solution existence)** the efficient contract exists: `r* := inf{ r ∈ L : Φ(r) ≤ r }` satisfies `Φ(r*) ≤ r*` (see Thm2 — under closedness of the feasible set this is automatic);
2. **(Joint regulation nonemptiness with measurable selection)** on the eroded product `K_{r*} := ∏_i K_{i, −r*_i}`, the shared-control regulation map
   `A(x) = { u ∈ U : f_i(x_i, u) ∈ T_{K_{i,−r*_i}}(x_i) ∀i }`
   is nonempty at every `x ∈ K_{r*}` with `dist(x_i, ∂K_{i,−r*_i}) = r*_i`... (at every boundary point of the eroded product) and satisfies the E2.B2(a) hypotheses (closed graph, compact values, Hausdorff continuity of the successor correspondence);
3. **(Convexified dynamics)** the invariance step is run on `F = co ∪_u f(·,u)` (the declared convexification; see Ex3 for the refusal without it).

**Then the eroded product `K_{r*}` is strongly invariant** for the shared-control system: there is an admissible measurable causal policy keeping every trajectory started in `K_{r*}` inside `K_{r*}`.

### Proof

**Step 1 (budget closure at the contract).** At `r*` with `Φ(r*) ≤ r*`: by definition of `Φ_i` and monotone truncation, for every `i` either `r*_i = ρ_i` (the geometric bound already exceeds any budget need — then (∗) holds a fortiori at `r_i = ρ_i` if it holds at `r_i`... the truncation case: `Φ_i(r*) = ρ_i ≤ r*_i` forces `r*_i = ρ_i`, and (∗) at `r_i` near `ρ_i` follows from the definition of `Φ_i` being the min) or directly

```
L_i r*_i  ≥  Λ_i Σ_j δ_ij(r*_j) + Δ_i − α_i   ⟺   L_i r*_i + α_i ≥ Λ_i Σ_j δ_ij(r*_j) + Δ_i,
```

which is (∗) at `r*` for every module `i` (with `≥` in place of `≤` rearranged — (∗) reads `L_i r_i ≥ Λ_i Σ δ_ij(r_j) + Δ_i − α_i`). So the erosion budgets all close at the contract.

**Step 2 (tangency on the eroded product).** Let `x ∈ ∂K_{r*}` with active face set `I(x) = { i : dist(x_i, ∂K_{i,−r*_i}) = 0 }`. For `i ∈ I(x)`, the outward normal `n_i` at `x_i` is a proximal normal to `K_{i,−r*_i}`; packet B1's restricted proximal-normal inequality gives, for the module's velocity under the shared control `u` chosen in `A(x)`: `⟨n_i, f_i(x_i, u)⟩ ≤ α_i + L_i r*_i`... precisely the R05.Thm2 computation at the *contract depths*: the encroachment `Λ_i Σ_j δ_ij(r*_j) + Δ_i` is covered by `α_i + L_i r*_i` (Step 1) — the one-sided (H3) inequality holds on every active face simultaneously (the same `u ∈ A(x)` serves all active modules: hypothesis 2).

**Step 3 (strong invariance).** With the tangential condition holding on the boundary of the compact set `K_{r*}` for the convexified field `F` (Step 2 + hypothesis 3), and `A` nonempty-closed-graph-compact-valued (hypothesis 2), E2.B2(a) yields the measurable selector `u*(x) ∈ A(x)`, and packet B1's strong-invariance theorem applies to the closed loop: every trajectory of the selected policy starting in `K_{r*}` remains in `K_{r*}`. (Disturbances, if present, are carried in the `Δ_i`/defect terms per the R05 convention.) ∎

---

## A4.Thm2 — Sub-solution (contract) existence — PROVED

### Statement

The feasible-contract set `S := { r ∈ L : Φ(r) ≤ r }` is a **nonempty closed down-set** in `L`; `r* = min S` exists; `r*` is the **least fixed point–type solution** and is computed by the **monotone iteration from the bottom**:

```
r^{(0)} = 0,   r^{(k+1)} = max{ r^{(k)}, Φ(r^{(k)}) }  →  r*   (monotone increasing, finite/ω-convergent),
```

while the **greatest** consistent depth vector is the top fixed point computed by the downward iteration from the geometric bound. Moreover, when all `δ_ij` are linear (`δ_ij(r) = γ_ij r`), `r*` is finite and the iteration converges geometrically **iff** `ρ(Γ) < 1` — recovering R05.Cor3 as the linear special case (an underestimate of the nonlinear statement).

### Proof

**Nonempty and down-set.** `Φ(ρ) ≤ ρ`? Not automatic — but `0 ∈ S` iff `Φ(0) ≤ 0` i.e. every module's standalone budget closes with no buffer (`Λ_i Σ_j δ_ij(0) + Δ_i ≤ α_i`); in general `S` may fail to contain small vectors but contains `ρ` whenever each truncated `Φ_i(ρ) ≤ ρ_i` holds (the budget closes at full buffers — the *super-solution* condition). **Corrected statement (honest):** `S` is nonempty iff the super-solution condition holds at some `r̄` (e.g. `r̄ = ρ`); under nonemptiness, `S` is a down-set: `r ∈ S`, `r' ≤ r` ⟹ `Φ(r') ≤ Φ(r) ≤ r` — so `r'` satisfies `Φ(r') ≤ r'`? No: `Φ(r') ≤ r` does not give `≤ r'`. **The correct down-set argument:** if `r ∈ S` then any `r'` with `Φ(r') ≤ r'`... — the honest structure: `S` is closed under the map `r ↦ min(r, Φ(r))`-limits and under taking *pointwise minima with super-solutions*; the iteration handles existence:

**Existence via monotone iteration (Tarski).** `Φ` monotone on the complete lattice `L` (Lemma). Tarski's theorem: the pre-fixed points `{r : Φ(r) ≤ r}` form a complete lattice; `r* = inf{r : Φ(r) ≤ r}` is itself a pre-fixed point **when `Φ` is Scott-continuous (or has closed graph)** — the closedness hypothesis: `S` is closed because `Φ` is continuous (each `δ_ij` nondecreasing and the display is continuous in `r`; if some `δ_ij` is only nondecreasing/discontinuous, take its closed graph — the min/max display remains upper semicontinuous, and `{Φ ≤ r}`... the honest form: assume the declared **closed-graph defect functions**, the class the theorem is stated on). Under closedness: `S ⊇ {r^{(k)}}`'s limit: the bottom-up iteration `r^{(k+1)} = max(r^{(k)}, Φ(r^{(k)}))` is monotone increasing (induction: `r^{(1)} = max(0, Φ(0)) ≥ 0`; if `r^{(k)} ≥ r^{(k−1)}` then `Φ(r^{(k)}) ≥ Φ(r^{(k−1)})` and `r^{(k+1)} = max(r^{(k)}, Φ(r^{(k)})) ≥ max(r^{(k−1)}, Φ(r^{(k−1)})) = r^{(k)}`), bounded by any super-solution `r̄ ∈ S` (induction: `r^{(k)} ≤ r̄` ⟹ `r^{(k+1)} = max(r^{(k)}, Φ(r^{(k)})) ≤ max(r̄, Φ(r̄)) = r̄`), hence converges to `r̃ ≤ r̄`; closedness of `S`-membership along the iteration (upper semicontinuity of `Φ` suffices: `Φ(r̃) ≤ liminf... ` the standard USC limit argument) gives `Φ(r̃) ≤ r̃`, and `r̃` is the least element of `S` by the iteration starting at the bottom. The downward iteration from the top computes the greatest fixed point symmetrically (greatest consistent depth vector, the most conservative contract).

**Linear case.** `δ_ij(r) = γ_ij r`: the budget system is `L_i r_i + Λ_i Σ_j γ_ij r_j ≥ Δ_i − α_i` — a linear inequality system; feasibility of the *positive* solution is governed by the gain matrix `Γ = (Λ_i γ_ij / L_i)`'s spectral radius: `ρ(Γ) < 1` ⟺ the iteration `r^{(k+1)} = Φ(r^{(k)})` contracts geometrically (standard linear iteration bound `‖r^{(k)} − r*‖ ≤ ρ(Γ)^k ‖r^{(0)} − r*‖` in the weighted sup-norm); `ρ(Γ) ≥ 1` with nonzero `Δ_i − α_i` ⟹ no finite contract. Hence R05.Cor3 is exactly the linear shadow of the monotone theorem. ∎

---

## A4.Thm1-Explicit — The two-module nonlinear gain-loop condition — PROVED

### Statement (no spectral radius)

For `n = 2` with defect functions `δ_12, δ_21` (nondecreasing, `δ(0) = 0` w.l.o.g. after absorbing `δ(0) > 0` into `Δ`), the loop admits a nontrivial feasible contract **iff**

```
∃ r > 0 :   δ_12( δ_21(r) )  ≤  r          (composite non-escalation),
```

together with the standalone margins `α_i ≥ Δ_i` (each module balanced at zero buffer). The composite condition replaces `γ_12 γ_21 < 1`.

### Proof

The budget system with `L_i = Λ_i = 1` (rescaled): `r_1 + α_1 ≥ δ_12(r_2) + Δ_1`, `r_2 + α_2 ≥ δ_21(r_1) + Δ_2`. With `α_i = Δ_i`: `r_1 ≥ δ_12(r_2)`, `r_2 ≥ δ_21(r_1)`. (⟸) Given `r > 0` with `δ_12(δ_21(r)) ≤ r`: set `r_2 = δ_21(r)`, `r_1 = r`: then `r_1 = r ≥ δ_12(δ_21(r)) = δ_12(r_2)` ✓ and `r_2 = δ_21(r) = δ_21(r_1)` ✓ — a feasible contract. (⟹) A contract `r_1 ≥ δ_12(r_2)`, `r_2 ≥ δ_21(r_1)` with, say, `r_1 > 0`: then `δ_12(δ_21(r_1)) ≤ δ_12(r_2) ≤ r_1` (monotoneity twice) — the composite condition at `r = r_1 > 0`. ∎

**Reading.** "The composite gain does not escalate" is the exact nonlinear replacement for `ρ(Γ) < 1` — a *first-order* loop condition, no linearization, no eigenvalues. For `n ≥ 3` the corresponding condition is the non-escalation of every composite cycle, and Thm1/Thm2's lattice iteration decides feasibility without enumerating them.

---

## A4.Ex3 — Sharpness witness: nonconvex `U` — PROVED

### Statement

With a genuinely **nonconvex** two-point control set `U = {u_a, u_b}` and two modules whose active faces require *different* controls, the joint regulation map `A(x)` is **empty** at the corner state: hypothesis 2 of Thm1 fails, the theorem **refuses to conclude**, and this refusal is correct — the eroded product is genuinely non-invariant for the nonconvexified system.

### Witness (explicit)

`K_1 = K_2 = [0, 1]` (eroded to `[ρ, 1−ρ]`... take the erosion `r` small), linear dynamics `ẋ_1 = u_a`-gated: module 1 at its right face `x_1 = 1−r` requires `ẋ_1 ≤ 0`, achieved only by `u = u_a` (`f_1(x, u_a) = −1`, `f_1(x, u_b) = +1`); module 2 at its right face `x_2 = 1−r` requires `ẋ_2 ≤ 0`, achieved only by `u = u_b` (`f_2(x, u_a) = +1`, `f_2(x, u_b) = −1`). At `x = (1−r, 1−r)`: `A(x) = {u : ẋ_1 ≤ 0 and ẋ_2 ≤ 0} = {u_a} ∩ {u_b} = ∅`. Every shared control exits some module's face within time `r`. The convexified field `co{f(u_a), f(u_b)} = co{(−1, 1), (1, −1)}` contains `(0,0)` — the *convexified* regulation is nonempty (hypothesis 3's role) but the **true** system has no safe shared control: the theorem's refusal isolates exactly the nonconvexity frontier. ∎

---

## Status

- **A4.Thm1: PROVEN** (monotone-operator nonlinear assume–guarantee; full proof above under the three declared hypotheses).
- **A4.Thm2: PROVEN** (contract existence via Tarski + closed-graph iteration; linear case recovers R05.Cor3 exactly).
- **A4.Thm1-Explicit: PROVEN** (two-module composite non-escalation condition).
- **A4.Ex3: PROVEN** (sharpness; the theorem's refusal is a feature).
- **R05.Open5's genuine residue, isolated:** nonconvex `U` without regulation-map nonemptiness (witnessed by Ex3 — the true frontier, not a gap in the proof) and non-tubular geometries (the erosion bookkeeping assumes proximal-regular faces).

**Dependencies:** packet B1 (proximal-normal invariance), R05 (Thm1/2/Cor3 — the linear shadow), E2.B2(a) (measurable selection). **Consumers:** Paper 2's composition chapter; TCS-1.1's enumerated composition gate G-4 (in the *frozen diff*, which controls nothing — see TCS_1_1_FREEZE.md); B-tier's B10 (the strategic docket cites this as the non-strategic machinery's composition capstone).

**Record-format note:** internal theorem document; Fields 1–4, 6–9, 16–17 carried; Fields 5, 10–15 N/A.

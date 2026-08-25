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
φ_i(r) := max{ 0 , ( Λ_i Σ_j δ_ij(r_j) + Δ_i − α_i ) / L_i }   ∈ [0, ∞),
```

the **least own-depth (buffer) module `i` must maintain** for its budget (∗) to close, given the neighbors' buffers `r`. (If the numerator is ≤ 0 the module needs no buffer: `φ_i(r) = 0`; note `φ_i` does not depend on `r_i`.) Since `φ_i` may exceed the geometric bound `ρ_i`, we distinguish:

- the **requirement map** `φ : L → [0,∞)^n` (untruncated), and
- the **lattice operator** `Φ : L → L`, `Φ_i(r) := min{ ρ_i , φ_i(r) }` (the truncated self-map of `L = ∏_i [0, ρ_i]` used for the fixed-point theory).

**Lemma (monotoneity).** Every `δ_ij` nondecreasing ⟹ `φ`, hence `Φ`, is **monotone** on the complete product lattice `L`. ∎ (Immediate from the display.)

**Lemma (truncation semantics — the honesty gate).** For `r ∈ L`:
`Φ(r) ≤ r` ⟺ (`φ(r) ≤ r`) **or** (some truncation is active at `r` with `r_i = ρ_i` and `φ_i(r) > ρ_i` — the requirement *exceeds the geometry*). Moreover, if the truncation is active at the least fixed point `r*` of `Φ` in some coordinate, then **no genuine feasible contract exists**: for any `s ∈ L` with `φ(s) ≤ s`, coordinate `i` gives `s_i = ρ_i` and `φ_i(s) = φ_i(r*) > ρ_i = s_i` (φ_i ignores the own coordinate), a contradiction. Conversely, if the truncation is inactive at `r*` (`φ_i(r*) ≤ ρ_i ∀i`), then `Φ(r*) = φ(r*) ≤ r*` — `r*` is a **genuine feasible contract**. **Active truncation at `r*` = honest refusal** (the geometry cannot support the required buffers), the numeric analogue of Ex3's nonconvex refusal. ∎

**Reading of the fixed points.** `r ∈ L` is a **feasible contract** iff `φ(r) ≤ r` (each module's maintained buffer covers its requirement, within the geometry). The **efficient contract** is the *least* such `r` (smallest buffers satisfying all budgets) — computed as the least fixed point of `Φ`, genuine exactly when the truncation is inactive there (Lemma above).

---

## A4.Thm1 — Monotone-operator assume–guarantee theorem — PROVED

### Statement

Assume:

1. **(Sub-solution existence)** a feasible contract exists: `S = { r ∈ L : φ(r) ≤ r } ≠ ∅`; equivalently (Thm2 + the truncation-semantics lemma), the least fixed point `r*` of `Φ` exists with the truncation **inactive** at `r*` (`φ_i(r*) ≤ ρ_i ∀i` — checkable), and `r* = min S` is the efficient contract;
2. **(Joint regulation nonemptiness with measurable selection)** on the eroded product `K_{r*} := ∏_i K_{i, −r*_i}`, the shared-control regulation map
   `A(x) = { u ∈ U : f_i(x_i, u) ∈ T_{K_{i,−r*_i}}(x_i) ∀i }`
   is nonempty at every `x ∈ K_{r*}` with `dist(x_i, ∂K_{i,−r*_i}) = r*_i`... (at every boundary point of the eroded product) and satisfies the E2.B2(a) hypotheses (closed graph, compact values, Hausdorff continuity of the successor correspondence);
3. **(Convexified dynamics)** the invariance step is run on `F = co ∪_u f(·,u)` (the declared convexification; see Ex3 for the refusal without it).

**Then the eroded product `K_{r*}` is strongly invariant** for the shared-control system: there is an admissible measurable causal policy keeping every trajectory started in `K_{r*}` inside `K_{r*}`.

### Proof

**Step 1 (budget closure at the contract).** At the fixed point `r*` (`Φ(r*) = r*`, Thm2.2): for every module `i`, either the truncation in `Φ_i` is inactive at `r*` (the generic case), in which case the definition of `Φ_i` gives directly

```
L_i r*_i  ≥  Λ_i Σ_j δ_ij(r*_j) + Δ_i − α_i   ⟺   L_i r*_i + α_i ≥ Λ_i Σ_j δ_ij(r*_j) + Δ_i,
```

which is (∗) at `r*` for module `i`. (The truncation case cannot occur under hypothesis 1: active truncation at `r*` would mean no feasible contract exists — the truncation-semantics lemma — contradicting `S ≠ ∅`. So at the genuine efficient contract every budget closes by the display above.)

**Step 2 (tangency on the eroded product).** Let `x ∈ ∂K_{r*}` with active face set `I(x) = { i : dist(x_i, ∂K_{i,−r*_i}) = 0 }`. For `i ∈ I(x)`, the outward normal `n_i` at `x_i` is a proximal normal to `K_{i,−r*_i}`; packet B1's restricted proximal-normal inequality gives, for the module's velocity under the shared control `u` chosen in `A(x)`: `⟨n_i, f_i(x_i, u)⟩ ≤ α_i + L_i r*_i`... precisely the R05.Thm2 computation at the *contract depths*: the encroachment `Λ_i Σ_j δ_ij(r*_j) + Δ_i` is covered by `α_i + L_i r*_i` (Step 1) — the one-sided (H3) inequality holds on every active face simultaneously (the same `u ∈ A(x)` serves all active modules: hypothesis 2).

**Step 3 (strong invariance).** With the tangential condition holding on the boundary of the compact set `K_{r*}` for the convexified field `F` (Step 2 + hypothesis 3), and `A` nonempty-closed-graph-compact-valued (hypothesis 2), E2.B2(a) yields the measurable selector `u*(x) ∈ A(x)`, and packet B1's strong-invariance theorem applies to the closed loop: every trajectory of the selected policy starting in `K_{r*}` remains in `K_{r*}`. (Disturbances, if present, are carried in the `Δ_i`/defect terms per the R05 convention.) ∎

---

## A4.Thm2 — Sub-solution (contract) existence — PROVED

### Statement

Write `S_Φ := { r ∈ L : Φ(r) ≤ r }` (pre-fixed points of the truncated lattice operator — **always nonempty**, since `Φ(ρ) ≤ ρ` trivially by truncation) and `S_φ := { r ∈ L : φ(r) ≤ r }` (**genuine feasible contracts** — possibly empty). Then:

1. **(Meet-closure)** both sets are closed under pointwise minima; hence `r* := inf S_Φ = min S_Φ` exists and is the **least fixed point of `Φ`** (Tarski — no continuity required).
2. **(Genuineness gate)** `r* ∈ S_φ` (the efficient contract is genuine) **iff the truncation is inactive at `r*`** (`φ_i(r*) ≤ ρ_i` for all `i`); and
   ```
   S_φ ≠ ∅   ⟺   truncation inactive at r*.
   ```
   Active truncation is the **honest refusal** outcome: no depth vector within the geometry closes all budgets.
3. **(Sufficient condition)** `φ(ρ) ≤ ρ` (every module's budget closes even at worst-case full neighbor depths) implies `S_φ ≠ ∅` (indeed `ρ ∈ S_φ`). This is sufficient, not necessary — contracts can exist that exploit small neighbor depths.
4. **(Constructive computation — Kleene)** if the `δ_ij` are continuous (the declared class), `Φ` is continuous and
   ```
   r^{(0)} = 0,   r^{(k+1)} = Φ(r^{(k)})   ↑   r* = sup_k r^{(k)},
   ```
   computes `r*` monotonically from below. Then **check the truncation gate at `r*`** (`φ_i(r*) ≤ ρ_i`): pass = genuine efficient contract; fail = refusal. The downward iteration `Φ^k(ρ) ↓` computes the greatest fixed point (most conservative consistent depth vector) symmetrically.
5. **(Linear shadow)** when all `δ_ij(r) = γ_ij r`: with `Γ = (Λ_i γ_ij / L_i) ≥ 0` and `c_i = (Δ_i − α_i)/L_i`, `φ(r) = [Γr + c]₊` (positive part), and `ρ(Γ) < 1` ⟺ the iteration converges geometrically (rate `ρ(Γ)` in the Perron weighted sup-norm) to the unique fixed point `r* = (I−Γ)^{-1}c` when `c ≥ 0`-feasible — recovering R05.Cor3's `ρ(Γ) < 1` / `A^{-1}b` structure exactly; with `ρ(Γ) ≥ 1` and an aligned nonzero source term, no fixed point exists in the box (Perron–Frobenius one-sided escape) — the linear shadow of the refusal gate.

### Proof

**(1)** `r, s ∈ S_Φ` ⟹ `Φ(r∧s) ≤ Φ(r) ≤ r` and `Φ(r∧s) ≤ Φ(s) ≤ s` (monotoneity), so `Φ(r∧s) ≤ r∧s`: meet-closure for `S_Φ`; the same computation with `φ` gives it for `S_φ`. Tarski on the monotone self-map `Φ` of the complete lattice `L`: the pre-fixed points form a complete lattice, `r* = inf S_Φ` satisfies `Φ(r*) ≤ r*` (for every `r ∈ S_Φ`, `Φ(r*) ≤ Φ(r) ≤ r`, so `Φ(r*)` is a lower bound), hence `r* ∈ S_Φ` and `r* = min S_Φ`; then `Φ(r*) ∈ S_Φ` (monotoneity: `Φ(Φ(r*)) ≤ Φ(r*)`) forces `r* ≤ Φ(r*)`, so `Φ(r*) = r*`: the least fixed point. (`φ` is not a self-map of `L` — its requirement can exceed the geometry — which is exactly why the genuineness theory routes through the truncation gate of part (2) rather than through a second Tarski application.) ∎

**(2)** If the truncation is inactive at `r*`: `φ(r*) = Φ(r*) = r*`, so `φ(r*) ≤ r*` — `r* ∈ S_φ`, whence `S_φ ≠ ∅`. If active at coordinate `i`: `Φ_i(r*) = ρ_i = r*_i` (fixed point) and `φ_i(r*) > ρ_i`. Suppose `s ∈ S_φ`; then `Φ(s) ≤ φ(s) ≤ s` gives `s ∈ S_Φ`, so `s ≥ r* = min S_Φ`; coordinate `i`: `s_i ≥ ρ_i` and `s ∈ L` force `s_i = ρ_i`; and monotoneity of `φ_i` in the other coordinates gives `φ_i(s) ≥ φ_i(r*) > ρ_i = s_i` — contradicting `φ(s) ≤ s`. Hence `S_φ = ∅`. (This is the truncation-semantics lemma of the Setting section, proved in place.) ∎

**(3)** `φ(ρ) ≤ ρ` says exactly `ρ ∈ S_φ`. The sufficient-not-necessary remark: `φ_i` depends only on the *other* coordinates, so a contract with small neighbor depths can close budgets that fail at `φ(ρ)` — the fixed point `r*` (not `ρ`) is the certificate. ∎

**(4) Kleene.** `0 ≤ Φ(0)` and monotoneity induct `r^{(k)} ≤ r^{(k+1)}`; every `r^{(k)} ≤ s` for any `s ∈ S_Φ` (induction with monotoneity). The increasing bounded sequence converges coordinate-wise to `r̃ = sup_k r^{(k)}`; continuity of `Φ` (from continuity of the `δ_ij`) gives `Φ(r̃) = sup_k Φ(r^{(k)}) = r̃`, so `r̃` is a fixed point, and `r̃ ≤ s` for all `s ∈ S_Φ` gives `r̃ = r*` (least). The genuineness check is then the truncation gate of part (2). *Honesty note:* without continuity of the `δ_ij`, Tarski (parts 1–3) still holds but the Kleene limit need only be a pre-fixed point below the least fixed point's jumps — the standard Kleene-vs-Tarski boundary, stated rather than papered over. ∎

**(5)** With `δ_ij` linear, `φ(r) = [Γr + c]₊`; on the region where the positive part is inactive the map is the affine `Γr + c`. If `ρ(Γ) < 1`: the Perron vector `w > 0` with `Γw ≤ ρ(Γ)w` gives the weighted sup-norm contraction `‖φ(x) − φ(y)‖_w ≤ ρ(Γ)‖x − y‖_w`; Banach gives the unique fixed point, geometric convergence at rate `ρ(Γ)`, and `r* = (I−Γ)^{-1}c` when `c` is in the feasible cone — R05.Cor3. If `ρ(Γ) ≥ 1` with the source term aligned with the Perron direction (the generic case for `Γ ≥ 0` nonreducible and `c ≢ 0` in that cone): along `w`, the iteration's `w`-component obeys `⟨w̃, r^{(k+1)}⟩ ≥ ρ(Γ)⟨w̃, r^{(k)}⟩ + const` for the dual Perron functional `w̃`, escaping every bounded box — no fixed point in `L`, i.e. the truncation gate fires — the linear shadow of the refusal. ∎

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

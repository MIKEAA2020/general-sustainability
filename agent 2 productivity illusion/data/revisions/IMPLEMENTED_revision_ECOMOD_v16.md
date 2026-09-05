# IMPLEMENTED REVISION — ECOMOD-26-1191 (Paper N′ + C)
## The corrected, manuscript-ready model that the Master Joint Assessment specifies

**What this is.** This is the **implemented version** of the Master Joint Assessment &
Implementation Plan (`MASTER_joint_assessment_and_implementation_plan.md`, Parts 1–12). It is a
*new, standalone, manuscript-ready* document that carries the paper's stated ambitions (emergent
carrying capacity, weak-vs-strong sustainability, a collapse-mechanism taxonomy, a policy extension)
in a form whose **equations implement the narrative**. It is the conclusion the whole exercise
converged on: the manuscript's algebra was sound, its narrative was not implemented by its
equations, and the fix is one equation, one measurable parameter, one interpretable dimension, and a
corrected analytic core. It is presented as **Paper N′ + C**: *narrative primary*, generalised to a
unified stock–flow model, labelled a conceptual/stylised model.

> **Accompanying files:** `IMPLEMENTED_demo.png` (a genuine overshoot→collapse run), the reference
> solver `demo_unified.py`, `IMPLEMENTED_demo_masking.png` (the corrected, converged
> small-deficit masking result — see §10, and note that an earlier Euler-based masking figure was
> withdrawn), the converged RK4 masking integrator `mask_rk4.py`, the **§4/§8 figures**
> (`scans/sustainable_yield_regimes.png` — regime-conditional MSY; `scans/feedback_diagram.png` —
> the two-loop causal diagram; `scans/r1_recovery_vs_collapse.png` — recovery vs collapse trajectories),
> the parent `MASTER_joint_assessment_and_implementation_plan.md`, **and the verification corpus** (`trace.py` →
> `SCAN_traceability_matrix.md`, `regression_test.py` → `SCAN_regression_report.md`,
> `audit_*.py` → `SCAN_numerical_audit.md`, `selfcheck.py` → `SCAN_selfconsistency.md`,
> `SCAN_risk_register.md`, `SCAN_process.md`).

---

## 1. Revised abstract (what the author should submit)

> We present a minimal coupled human–environment model in which carrying capacity is not an imposed
> ceiling but an emergent function of environmental stock, technological productivity, and per-capita
> resource demand. Environmental regeneration and demographic response are modelled as two distinct
> time delays; cumulative overshoot is tracked as an ecological debt that erodes productivity.
> Biocapacity is the sum of a **flow yield** (separable from the stock, as in an orchard) and a
> **stock increment** (harvested only by removal, as in a forest) — a decomposition that reduces to
> the standard harvest model in one limit and to the orchard metaphor in the other. For the
> constant-parameter subsystem, biocapacity defines a **one-parameter family of equilibria
> `P = B(A)/e`** rather than a single isolated attractor, and any interior point of it is
> **monotonically unstable** — a **positive real eigenvalue** for *every* delay (driven by the
> delayed-regeneration overshoot), with **no imaginary-axis crossing** — so the onset is a structural
> vicious cycle, **not** a delay-ratio Hopf and **not** controlled by a single `χ`. We
> identify two collapse mechanisms: debt accumulation that drives population collapse even with no
> delay, and a delay-amplified transient that shrinks the basin of attraction. A sufficiently early
> technology wave can produce a window in which biocapacity rises while the environmental stock falls
> — the weak-sustainability regime — but this masking is *narrow*, bounded, and transient, and is
> **confined to a small initial deficit**: it widens to only ~5 yr and collapses entirely beyond a
> modest overshoot (deficit ≈0.075, i.e. ≈15 % of the initial flow yield `b₀A₀`). The reason is
> twofold — yield gains saturate while debt compounds, and the
> same technology that raises biocapacity also raises the sustainable population and hence aggregate
> demand, tending to *increase* cumulative debt under overshoot. Rising biocapacity therefore need not signal improving environmental health;
> it may be a productivity illusion that precedes a reckoning. The paper is a conceptual/stylised
> model: parameters are representative, and the four predictions it makes are stated as falsifiable
> hypotheses, not calibrations.

---

## 2. The corrected model (`1‴`) and the full system

### 2.1 Variables and the units convention (GFN, stated once)

| Symbol | Meaning | Unit | State? |
|--------|---------|------|:------:|
| `A` | productive biocapacity **area** (the "trees") | ha | yes |
| `P` | human **population** | cap | yes |
| `D` | accumulated **ecological debt** (optional degradation channel) | gha·yr | yes (optional) |
| `b` | **flow yield** per unit area (fruit per tree) | gha·ha⁻¹·yr⁻¹ | no (derived) |
| `b_G` | value of one hectare of **standing stock** (the orchard's `V`) | gha·ha⁻¹ | parameter |
| `G(A)` | **regeneration / recruitment** rate | ha·yr⁻¹ | no |
| `B` | **biocapacity** = `bA + b_G G(A)` | gha·yr⁻¹ | no |
| `E` | **footprint** = `eP` | gha·yr⁻¹ | no |
| `K` | carrying capacity = `B/e` | cap | no (**algebraic**, not a state) |
| `e` | per-capita footprint | gha·cap⁻¹·yr⁻¹ | param |
| `ρ` | regeneration rate | yr⁻¹ | param |
| `r` | per-capita population growth rate | yr⁻¹ | param |
| `α` | degradation rate | (gha·yr)⁻¹ | param |
| `η` | debt-repayment rate | yr⁻¹ | param |
| `τ_g` | **recruitment** (regeneration) delay | yr | param |
| `τ_p` | demographic (generation) delay | yr | param |
| `A_max`, `b₀`, `A_ext` | carrying-area ceiling, base yield, extinction floor | ha, gha·ha⁻¹·yr⁻¹, ha | param |

Because `A` is in **physical ha**, it is independent of yield: `b = B/A` is then definable, and the
headline decomposition `B = b·A + b_G·G(A)` is identifiable. **This is the RC1 fix** — it is what the
original manuscript (with `M` in gha, so that a gha already embeds `b`) could not do.

### 2.2 The equations

```
Regeneration:  G(A) = ρ A (1 − A/A_max)                          (R)
Biocapacity:   B    = b A + b_G G(A)                            (B)
Footprint:     E    = e P                                       (E)
Stock:         dA/dt = G(A(t−τ_g)) − [E(t) − σ b A(t)]₊ / b_G   (1‴)
Population:    dP/dt = r P(t) [1 − P(t) / K(t−τ_p)]              (4′)
Carrying cap:  K    = B / e                                     (K)   [algebraic]
Debt:          dD/dt = [E − B]₊ − η D                           (6′)  [η primary]
Degradation:   b    = (b₀ + T_b(t)) e^{−α D(t)}                 (7′)  [multiplicative]
Technology:    T_b  = Δb / (1 + e^{−κ(t−t_wave)})               (8′)  [bounded logistic wave]
```

`σ` is the human-available share of the flow (σ = 1 with no reservation; set σ and the population
cap so that `E ≤ σ·B` for a reservation/Half-Earth policy). `[x]₊ = max(x, 0)`.

- **`(1‴)` is the key change.** Demand is met **first from the flow yield `bA`** (the fruit — leave
  the tree); **only the shortfall `[E − bA]₊`** liquidates stock, at rate `1/b_G`. This is the deficit
  mechanism, and it is why `B` finally appears in the stock equation (the two flow accounts are no
  longer parallel and unlinked). The original gross `γE` form is retained only as the "land-conversion
  / biomass-harvest" variant (the `b → 0` limit) in a supplement.
- **The refined diagnosis of the manuscript's B2 is a *bookkeeping* error, not a wrong direction
  (Part 11.5).** The original defined biocapacity in the **flow-book** (`B = bM`) while depleting with
  the **increment-book** quantity (`E`, a harvest of increment/stock), so the two accounts were measured
  in different "books" and never reconciled. It is therefore **correct-but-mislabelled**, not flatly
  wrong: in the `ψ → 0` (increment) limit the unified `(1‴)` **reproduces** the manuscript's Eq. (1)
  with `γ = 1/b_G`, so the manuscript was right in that limit and only mis-framed the bookkeeping. This
  is the more charitable and more precise reading than "the depletion term is simply wrong."
- **`(6′)` makes the model well-posed.** With `η > 0`, `D* = (E−B)/η` is finite, so the full
  overshoot model **has** an interior equilibrium (RC3/RC4 fix). `η → 0` is the singular, irreversible
  case (it is a primary parameter, not a robustness dial).
- **`(7′)` makes the asymmetry a theorem.** Multiplicative `b = (b₀+T_b)e^{−αD}` ⇒ `b → 0` as `D→∞`
  regardless of bounded `T_b`. "Technology saturates, debt compounds" is now derived, not asserted.

**Well-posedness at the boundary (the non-Lipschitz singularity fix).** The original `dP/dt` blows up
(`P/K → ∞` as `K → 0`). We impose an **extinction floor `A_ext > 0`** so `K ≥ b·A_ext/e > 0` is
bounded, and clamp `A ≥ A_ext`, `P ≥ 0`. Then "collapse" is a **well-defined approach to the
extinction boundary**, not a numerically clamped blow-up. (See §8.)

**Fork note (Part 6 F4).** This revision exercises the **"keep `D`"** branch (not the master's
*default* "drop `D`"), because the paper's strongest empirical message — accounted biocapacity is
overstated — is carried by the **degradation channel** `D → b` (master 11.5 treats it as a
separately-evidenced third ingredient, not as double-counting `A`). Consequently this is a **3-D**
model (`A, P, D`) with `K` algebraic, and the ill-posed "2-D with no degradation" special case is the
`α = 0`/`D`-dropped limit. State this choice explicitly in the paper.

**Ledger convention (frame from the companion typed-ledger study, P3 — frame only, no result).** The
three accounts in `(1‴)/(B)/(6′)/(7′)` live in **three distinct "books"**, and the whole revision is
written so they are never mixed: `A` is the **increment book** (the standing base, removed only by
liquidation); the flow yield `bA` is the **flow-yield book** (the fruit, separable from the base); and
`D` is the **degradation/debt book** (the erosion of the *surviving* stock's yield). **Conservation is a
property of the incidence structure** (each outflow is assigned to exactly one donor book), and **positivity
follows from donor limitation** (an outflow vanishes when its donor compartment is empty). This is why the
B2 fix is a *bookkeeping* correction and not a change of direction, and why the degradation channel
`D → b` is treated as a **separately-evidenced third ingredient rather than double-counting `A`**: the
`α = 0`/drop-`D` fork is not a second accounting of the same removal, it is the **closed single-book**
limit. Any parameter that is **pinned at a bound** (as a fit artefact) is reported as a **declared fit
defect**, never silently.

---

## 3. Assumption-before-equation (add one line to each)

> **Companion-framework convention used throughout.** Where a *conceptual distinction* is
> borrowed from a companion manuscript (all unpublished manuscripts by the same author, Amin
> Abaee), it is cited as an unpublished framework and **re-expressed in this model's own
> notation** (`A`, `B`, `E`, `D`, `K`). No companion **theorem, numerical result, or named
> finding** is imported as this paper's own; each is used either (i) as a *framing* that the
> model instantiates, or (ii) as a *corroborative analogy*, cited as such.

- **(R) Logistic regeneration** — symmetric self-limiting growth; a modelling convenience, not a law;
  it is the *maximal-growth* point that `A_max/2` refers to — **not** a threshold.
- **(B) Biocapacity is additive flow + increment** — the flow is separable (crops, orchard), the
  increment is removable-only-by-stock (forest, fish). The composition is captured by the flow share
  `ψ = bA*/B*`.
- **(E) Per-capita footprint is constant** — default; it is the *only* way to isolate the M–P–D–T
  feedbacks. We state this as a modelling choice; endogenising `e` and `r_opt` is an offered extension.
- **(1‴) Deficit-driven, immediate depletion** — liquidation is immediate; the delayed response is in
  **recruitment** `τ_g` (a tree takes `τ_g ≈ 20–80 yr` to bear fruit), not in the depletion term.
- **(4′) Demographic delay on carrying capacity** — `K(t−τ_p)` (the conditions a cohort "knew," the
  moving delayed ceiling), Hutchinson-style. The original `P(t−τ_p)/K(t)` did not match its
  justification.
- **(K) `K` is algebraic, not a state** — it is a function of the state; the system is genuinely 3-D
  (`A, P, D`), not "two-dimensional."
- **(6′) Debt accrues only in overshoot, repayed at `η`** — `η` is primary (it decides whether an
  equilibrium exists). We set **`η = 0.05 yr⁻¹`** — a minimal environmental regeneration /
  degradation-removal rate (slow, ≈20-yr timescale); the model is **insensitive to `η` over a modest
  range** provided `η > 0` (§13, point (3)). **State the delay asymmetry explicitly** (master 12G.7):
  liquidation/depletion is immediate while functional degradation is a separate, slower state; either
  **justify this asymmetry** or add a **third lag `τ_D`** (`dD/dt = [E(t−τ_D) − B]₊ − ηD` and/or
  `b = b₀e^{−αD(t−τ_D)} + T_b`) to keep the delay structure consistent. R1/R2 operate on the
  **constant-parameter S0** (`D` and `η` dropped), so the `η → 0` singular case concerns the **full
  `(6′)` model**, not R1/R2 (§13, point (3)). **Declare the aggregation of the governance clock before
  collapsing it (frame from P5):** `τ_p` lumps several institutional time objects (observation,
  assessment, review, decision/deployment, ecological-response, memory). State the aggregation rule rather
  than treating `τ_p` as one measured lag.
- **(7′) Degradation erodes the surviving stock's yield** — a separately-evidenced channel (soil
  fertility, over-picking), *not* double-counting the trees already removed by `A`.
- **(8′) Technology is bounded** — logistic waves; saturation is why the masking is transient.

---

## 4. The analytic core (re-derived, verified)

### 4.1 Carrying capacity, MSY, and the emergent ceiling
`K = B/e` is emergent (it moves with `A` and `b`). Because the increment `b_G G(A)` is only positive
for `0 < A < A_max`, the total sustainable-yield curve `B(A) = bA + b_G G(A)` has an **interior
maximum** — the max-sustainable-yield (MSY): via `dB/dA = b + b_G ρ(1 − 2A/A_max) = 0`,

```
A*  = A_max (b + b_G ρ) / (2 b_G ρ)
B_max = A_max (b + b_G ρ)² / (4 b_G ρ)
```

So the **sustainable equilibrium is interior (`A* < A_max`), not `A_max`** — a steady harvest of the
increment keeps the stock below its unmanaged maximum (the Schaefer/forestry picture). Only in the
flow-only limit (`b_G G ≪ bA`, the orchard) does the stock tend to `A_max` with a zero harvest drain.

**The interior-MSY statement is regime-conditional.** `A* < A_max` holds **only** in the
increment-dominated regime, i.e. when `b_G ρ > b` (equivalently `ψ → 0`). When **`b_G ρ < b`** (the
flow-dominated regime, `ψ → 1`) instead `B(A)` is **monotone increasing on `[0, A_max]`** and there is
**no interior maximum**: the sustainable point is the **boundary** `A_max` (fig.
`scans/sustainable_yield_regimes.png`). This is precisely the regime the **baseline** parameter set sits
in (`b_G ρ = 0.8·0.05 = 0.04 < b = 0.5`), so the corrected S0's sustainable state is the **boundary
`A_max`**, consistent with what R1 computes (it recovers `A → A_max`). State which regime applies before
quoting `A*`/`B_max`; they are the increment-only limit, not universal.

**The flow-share `ψ = bA*/B*` is the single control that interpolates between the two limits
(master Part 11 §4.6 / 12G.3).** Report its regime dependence explicitly, as it governs which
analytic core applies:
- **`ψ → 0`** (increment-dominated, the manuscript-like `b → 0` limit): interior `A*`, the `χ`
  classification of §4.3 applies.
- **`ψ → 1`** (flow-dominated, the orchard/hens limit): `A_max` at sustainability, a liquidation
  mask, and the vicious cycle — the `a₁₁ = ρ(1−2A*/A_max) + b/b_G` liquidation feedback.
- **in-between** (`0 < ψ < 1`): interior `A*` *and* liquidation feedback coexisting — the
  manuscript's increment model and the orchard are both recovered as limits, and the unified
  `(1‴)` is the general object. This is the quantitative content of the "deficit-driven"
  framing: `ψ` measures how much of sustainable biocapacity is a flow (separable) versus an
  increment (removal-only).
- **`γ` is measurable and equals `1/b_G = 1/V` (the orchard's salvage value).** `V` = standing
  biomass ÷ annual production (≈ 20–100 yr, e.g. forest timber vs. fish recruitment), so the
  increment-harvest `γ` is *not* a free parameter — it is the inverse of the standing-stock value.
  This is what makes the unified model empirically estimable rather than ad hoc.
- **`ψ` is a *testable* prediction, not just a decomposition (Part 11.3).** Small `ψ` (flow yield is a
  small share of biocapacity, cropland/grazing-dominated) ⇒ the model is near the manuscript's
  increment limit and a smooth decline is **stabilised by demographic feedback** — the illusion is
  small. Large `ψ` (forest/fishery, increment-dominated) ⇒ the overshoot is **invisible until demand
  exceeds the flow yield**, *then* liquidation with a threshold (`A_c(E)`). So the model predicts that
  the masking illusion should be **more visible in flow-dominated (high-ψ) systems than in
  increment-dominated (low-ψ) systems** — a falsifiable, GFN-faithful prediction that distinguishes
  the two regimes empirically.

**Regime → outcome (this is the analytic core in one place).** The single testable condition
`b_G ρ ⋚ b` (equivalently `ψ ⋚ 1/2`) decides everything downstream:

| Regime | Condition | `B(A)` shape | Sustainable point | MSY | Collapse/mask behaviour |
|---|---|:--:|---|---|---|
| increment-dominated | `b_G ρ > b` (`ψ → 0`) | interior maximum | interior `A* < A_max` | interior MSY `A*`, `B_max` | near-manuscript limit; smooth decline stabilised by demographic feedback — *illusion small* |
| **flow-dominated (baseline)** | `b_G ρ < b` (`ψ → 1`) | monotone ↑ | **boundary `A_max`** | none interior (max at `A_max`) | liquidation with threshold `A_c(E)`; overshoot **invisible until demand exceeds flow yield** — *illusion more visible* |
| marginal | `b_G ρ = b` | max at the boundary | `A* = A_max` (interior max merges with boundary) | boundary `A_max` | measure exactly; `ψ` → 1 |

This table and the §4.1 figure replace a purely algebraic statement with a single visual/verbal rule:
**whether the model is the orchard (flow/boundary) or the forest (increment/interior) is decided by
`b_G ρ ⋚ b`, and every downstream claim (MSY location, mask visibility, recovery target) follows from
that branch.** A parameter sitting exactly on the `b_G ρ = b` boundary is a non-generic choice, to be
stated as such and perturbed off.

### 4.2 Fixed-liability threshold and the saddle-node = MSY
For a **fixed** liability `E`, the deficit-region equation `dA/dt = 0` is a quadratic in `A`, with an
unstable root (the separatrix) — and the saddle-node is **exactly the MSY**:

```
A_c(E) = [ (b_G ρ + b) − √((b_G ρ + b)² − 4 b_G ρ E/A_max) ] A_max / (2 b_G ρ)
E_sn   = B_max = A_max (b + b_G ρ)² / (4 b_G ρ)            (safe basin vanishes at MSY)
```

Interpretation: a fixed liability above the maximum sustainable yield `B_max` cannot be sustained by
harvesting regrowth; the threshold is **emergent and `E`-dependent** (no Allee term needed), and it is
located at `A_c(E)`, never at `A_max/2`.

### 4.3 Stability; the vicious cycle; the χ-classification

**The deficit = stock-decline identity (exact, no ramp needed).** When demand exceeds the flow
yield (`E > bA`) the stock equation reduces exactly:
```
dA/dt = G(A(t−τ_g)) − [E − bA]₊/b_G  =  (B − E)/b_G
```
because `B = bA + b_G G(A)` and `[E − bA]₊ = E − bA` there. This is the algebraic identity that makes
"deficit-driven" rigorous — the *shortfall* between biocapacity and footprint, not the gross harvest,
drives stock decline, and the unified model's stock-buildup exactly cancels against its flow term.
It is why the two flow accounts (flow-yield vs increment) cease to be parallel.

Linearising `(1‴)+(4′)` in the deficit region gives (at the interior point)

```
a₁₁ = ρ(1 − 2A*/A_max) + b/b_G      ;  a₁₂ = −e/b_G      ;  a₂₂ = −r
det = r·ρ·A*/A_max > 0  (never a saddle)   →   zero-delay condition is  a₁₁ < r  (NOT a₁₁ < 0)
```

- **The vicious cycle is real and quantitative.** `a₁₁` gains the `+b/b_G` term; for liabilities that
  scale with the stock (`E = f·bA`) the interior point is `A* = A_max[1 − (f−1)b/(b_G ρ)]`, and it is
  **self-sustaining** (the environment's own mode goes locally runaway, `a₁₁ > 0`) precisely when
  `(2f−1) ν > 1`, where `ν = b/(b_G ρ)`. With `b_G` = standing-stock value (20–100 yr) and realistic
  `ρ ≈ 0.02–0.1 yr⁻¹`, `ν` is `O(0.1–2)` — treat `(2f−1)ν > 1` only as an **estimated indicator**,
  not a measured threshold, because `f` and the liability elasticity are set by the model, and this band
  is an original-model fast–slow result that does **not** transfer as a stability criterion to the
  corrected S0 (R2: §13, point 8). The paper's "vicious cycle" prose describes `1‴`, not its own `γE`
  equation.
- **The χ-classification (corrected sign).** For `ρ ≫ r`, the 2-D two-delay system reduces to a scalar
  two-gain delayed logistic with control `χ = q/(ρ − 2q)`, `q = γ e b₀/r_opt` (depletion pressure).
  - `χ > 1` (Λ > 0) ⇒ **τ_g-only** Hopf: `ω = r√(χ²−1)`, `τ_g* = arccos(−1/χ)/ω`.
  - `χ < 1` (Λ < 0) ⇒ **τ_p-only** Hopf: `ω = r√(1−χ²)`, `τ_p* = arccos(−χ)/ω`.
  - `χ = 1` (Λ = 0, i.e. `ρ = 3q`) ⇒ neither; two-delay boundary `s = π/ω`, `ω = 2r·cos(ωd/2)` ⇒
    `s ≈ π/(2r) = 78.5 yr` at `d → 0`.
  - **The sign structure is exact** (from the `|Q| = |P|` elimination); only `ω*, τ*` are `O(r/ρ)`
    approximate, and the fast–slow reduction is valid only while `a₁₁ ≤ 0` (else use the full 2-D
    transcendental equation, where the `A`-mode can itself oscillate).
  - **But on the corrected S0 this Hopf classification is NOT realised** — R2 finds the exact `[·]₊`
    gives a **monotone** positive-real eigenvalue with **no** imaginary-axis crossing for every delay
    (§8, §13 point (8)). The χ-Hopf rules above describe the *fast–slow reduction*; they do not predict
    the corrected model's actual (structural) instability.
  - Baseline sits at `χ = 1` **because `ρ` was set to `3q`** — a non-generic choice to be justified or
    perturbed off.

### 4.4 The complete dimensionless group set (not just χ)

`χ = q/(ρ−2q)` is the cleanest single control (it matches the scalar two-gain picture), but the paper
should carry the **complete** non-dimensionalization as the full generality statement (master 12G.3):
`t̂ = rt`, `a = A/A_max`, `p = P·r_opt/(b₀A_max)`, and the groups **`s = ρ/r`**, **`g = γ b₀ f/ρ`**,
**`f = e/r_opt`**, **`θ`**, plus scaled delays **`τ̂_M = rτ_g`**, **`τ̂_P = rτ_p`**. Present **both** —
`χ` for the clean stability-sign rule, the six-group set for full generality (they are complementary,
not competing).

---

## 5. The corrected headline claims (replacing the over-claims)

| Original claim | Corrected (defensible) claim |
|---|---|
| "instability requires both delays, threshold ≈ 80 yr" | "**corrected `(1‴)` S0:** the interior equilibrium is **monotonically unstable** — a **positive real eigenvalue** (≈ +0.62) for *every* delay, with **no imaginary-axis crossing**; and `D(0)=0` on the whole equilibrium family `P=B(A)/e`, so there is **no isolated interior attractor** to frame a delay-ratio Hopf. The `χ`/two-delay Hopf picture (`χ=1 ⇔ ρ=3q`, `τ_g*≈85`,`τ_P*≈225`, `Re λ ≲ 0.01`) is the **original-model** interior-attractor result and does **not** transfer (R2). The `78.5 yr = π/(2r)` coincidence is still a two-loop coincidence, **not** the Hutchinson `π/(2r)` demographic threshold." |
| "the productivity illusion is demonstrated" | "**It is real but conditional and narrow:** under the corrected model a genuine `B`-rising-while-`A`-falls window exists **only for a small initial deficit** (≈5.4 yr at `E−b₀A₀=0.06`, collapsing to zero at deficit ≈0.075; converged RK4 — see §10). The master's headline sets from the *original* model do **not** carry over; present it as *narrow, deficit-bounded, transient*, with `t_peak` and the critical deficit as numbers, never as generic." |
| "technology offsets debt" | "under overshoot, yield technology raises K, P and E, and can **increase** cumulative debt — a **Jevons-type rebound**." |
| "irreversible threshold at M_max/2" | "**There is no such threshold.** The real threshold is emergent: `A_c(E)` (fixed liability) or the MSY `B_max`; `A_max/2` is only the maximal-regeneration point." |
| "the equilibrium is locally stable" (Scenario D) | "the full overshoot model has an equilibrium only because of `η`; state `a₁₁ < r` and never assert stability for a model with no equilibrium." |
| "two-dimensional" | "the full system is three delayed states (`A,P,D`); only the `α=0` subsystem is 2-D; `K` is algebraic." |
| "debt compounds without bound while technology saturates" | "a theorem under multiplicative `b = (b₀+T_b)e^{−αD}`; false under the additive form." |

**Scenario B/C is the *inverse* of the orchard framing (master 12G.4).** In Scenarios B and C the
environmental stock `A` rebounds to ≈`A_max` (≈1.19) while population `P` and the harvest/biocapacity
`B` collapse — an "**environment recovers, humans collapse**" outcome that is the *opposite* of the
abstract's orchard framing ("humans die, orchard survives"). State this explicitly, or reconcile the
framing in the abstract; it is a scenario outcome, not a claim to be over-claimed. (These are
**original-model** scenarios; the corrected analogue must be recomputed — see §8 provenance note.)

---

## 6. Falsifiable predictions (emergent, not built in)

These are the honest, testable content (the model is no longer circular):

1. **Which lag destabilises** is set by the sign of `Λ`/`χ` (not set by the equations) — **original-model
   interior-attractor result**; on the corrected `(1‴)` S0 the interior point is instead **monotonically
   unstable for *every* delay** (positive real eigenvalue, no imaginary-axis crossing), so the
   "which-lag" question has no Hopf answer there (R2).
2. The **oscillation period near onset ≈ 4× the dominant lag** — applies only to the original model's
   **Hopf** boundary; the corrected S0 has **no** oscillatory onset (monotone collapse), though the full
   `(6′)` model (with `η`, `D`) can still show damped oscillatory transients.
3. The productivity illusion has a **computable peak-biocapacity time `t_peak`** with the signature
   "`B` rising while `A` falls" (and a measurable `t_peak`).
4. **Reducing a policy lag `τ_e` matters comparably to reducing the overshoot `f`** — a testable,
   policy-relevant ranking.

**The two masks (weak/strong sustainability), made observable.** *Technology mask:* `B` rises while
`A` falls (requires progress). *Liquidation mask:* `E` steady while `A` falls (requires none). The
discriminating observable is exactly which of these holds.

**Why the illusion is *necessarily* transient (Part 1, second strongest result — the proof).**
From `B = bA` (flow component) the growth rate of biocapacity is **`d ln B/dt = d ln b/dt + d ln A/dt`**.
Under the mask window `A` falls, so the second term is negative; the first term is bounded because
technology saturates (`T_b` is a logistic wave, so `d ln b/dt ≤ 0` eventually). Therefore the *sign* of
`d ln B/dt` is pinned by the **unboundedly negative** `d ln A/dt` under the stock-liquidation cycle —
so a `B`-rising-while-`A`-falls window cannot persist: the yield gain from a *bounded* technology wave
is finite, whereas the stock decline it is meant to offset is *unbounded* once liquidation takes over.
That is the analytic reason the mask is narrow and deficit-bounded (§10), and it is why the
"productivity illusion reads as if sustainability were improving" is a transient, recover-to-reckoning
signal rather than a new equilibrium.

---

## 7. Didactics / presentation
- **Symbol table** (§2.1); **assumption-before-equation** (§3).
- **Feedback diagram with a switch** (fruit harvest vs. capital liquidation): `A →^{\!b} B → K → P → E`,
  with `E − bA` deciding the switch, `D →^{\!α} b`, and an exogenous bounded `T_b`. Present it with the
  **two positive-feedback loops**: Loop 1 (stock-liquidation: `A↓ → B↓ → deficit↑ → liquidation↑ →
  A↓`) and Loop 2 (debt-erosion: `D↑ → b↓ → B↓ → deficit↑ → D↑`); they compound. (Rendered:
  `scans/feedback_diagram.png` — the causal/loop diagram with the `E − bA` switch node and both loops.)
- **Verbal walk-through of the (now seven) regimes** before any numbers.
- **Thought-experiment label** — present the orchard/hens framing explicitly as a *Gedankenexperiment*
  (the best available intuition, master didactics), and separately the flow/increment decomposition as
  the measurable representation of it. State that the model is a *stylised* illustration of the accounting
  logic, so the reader does not mistake the orchard metaphor for an empirical claim.
- **Parameter justification** — justify or caveat the representative values: `ρ` is large in the
  original scale, and `γ`, `α`, `τ` are lumped/effective parameters, not independently measured.
- **Assess the path, not just the endpoint (frame from P1).** Because the assessed object here is a
  *trajectory*, the intermediate passage where `A` falls — even one that later recovers — is itself a
  violation; report it as such, not only as an endpoint attractor. (Does not import P1's theorem.)
- **NFA data limitations** — note the limits of the National Footprint Accounts (account-based
  biocapacity; the accounts do not capture soil erosion, deforestation or groundwater depletion, so
  estimated biocapacity likely **overstates** and the Footprint likely **understates** the real
  overshoot). This undergirds the §11 caveat.
- **Non-smoothness:** at the switch `E = bA` the exact `[·]₊` is non-smooth, so the sustainable point is a
  **boundary of the deficit regime, not an interior point** — report **one-sided** stability (linearise
  from the deficit side only). The corrected model uses the exact switch (`ramp_soft=False`); the
  original-model reference implementation may use a smooth ramp, but then fix its width `w` and report
  insensitivity to it. Because R2 linearised the exact switch and found **no** imaginary-axis Hopf
  crossing, the non-smoothness does **not** create spurious oscillations (§13, point 4).
- **Delete:** "antibiotic resistance," the elevator/"sudden break" metaphor (B–C are asymptotic), the
  footnote-1 "per year" double-count, "independently verified to machine precision," and the truncated
  "when *ted…" sentence. Give units for `A_max, b₀, Δb`.
- **Literature (priority statement — be precise).** The delayed-logistic *stability* result is
  **Hutchinson (1948)**, G. E. Hutchinson, *Circular causal systems in ecology*, Annals of the New York
  Academy of Sciences **50**(4):221–246 — the reference for the single-delay logistic (the
  `π/(2r)` demographic threshold that our §4.3 explicitly distinguishes from the two-loop coincidence).
  **We cannot support the claim that Haberl & Aubauer "first introduced" time delay into human
  population dynamics**: their contribution is to apply the delayed-logistic framework to human
  population/load dynamics, not to originate it; state the attribution as Hutchinson (1948) with
  Haberl & Aubauer as an application. Correct the Brander–Taylor (1998) characterisation. Add the GFN
  account + limitations references (Wackernagel & Rees; Wackernagel et al. 2002 PNAS; Borucke et al.
  2013; Lin et al. 2018; Galli et al. 2016; Blomqvist / van den Bergh & Grazi / Giampietro &
  Saltelli), and append the **GFN-caveats sentence**: GFN's own documentation states the accounts are
  *aggregate and data-limited* — they rely on measured yields and conversion factors, do not capture
  soil erosion, deforestation or groundwater depletion, and GFN notes likely **overstate** biocapacity
  and **understate** the Footprint, so the 1961–2022 series is a **lower bound** on genuine overshoot
  (see §11). Cite or remove the orphan May (1973).
- **Submission hygiene:** unify "Modeling"/"Modelling"; reconcile the keyword lists; provide code as
  `.py` and the verification report as `.pdf` (not `.docx`); strip the PDF author metadata and the
  submission-system URL / margin callout grid.

---

## 8. Numerics, verification, and well-posedness (RC5)
- **Solver**: method-of-steps with RK4 (or `dde23`/`pydelay`; Shampine & Thompson 2001), the **exact
  `[·]₊` switch** as the model states it (`ramp_soft=False` — never a smooth ramp for the corrected
  model, because a softplus ramp leaks depletion when `E < bA`), **clamping** `A ≥ A_ext > 0`,
  `P ≥ 0`, `K ≥ K_min`, and an explicit **extinction floor** (so "collapse" is a model result, not a
  clamp). Where a *smooth* variant of the `[·]₊` switch is used (original-model reference
  implementation only), fix its width `w` and report **insensitivity** to it (§13, point 4); the
  corrected model must never be run with `ramp_soft=True`. **Full-`(6′)` runs use `η = 0.05 yr⁻¹`**
  (debt-repayment / regeneration rate, §13 point (3)); R1/R2 operate on the `D`/`η`-dropped
  constant-parameter S0, so `η` does not enter them.
- **Note on simulator corrections (earlier runs invalid).** Two bugs in the first corrected-model
  simulator made it collapse *everything* erroneously, and were the reason the first recompute of the
  corrected basin/figures looked pathological. (i) A **softplus ramp** for `[·]₊` (a smooth
  `ramp_soft=True` form) **leaks depletion** whenever `E < bA`, incorrectly liquidating the stock even
  when the flow yield is sufficient — the corrected model is never run with `ramp_soft=True`. (ii) The
  **regeneration/depletion coupling was evaluated at the wrong time**: `G(A(t−τ_g))` and the
  `K(t−τ_p)` argument were placed on the *current* state rather than their delayed times. Both are fixed
  (`model_sims/corrected.py` now uses the exact `[·]₊`, a method-of-steps + RK4 lag-angle `A(t−τ_g)`/`K(t−τ_p)`),
  and **every number in this revision uses the fixed simulator.** Any earlier revision/note that quotes
  the corrected-model basin or characteristic-equation figures from the buggy solver is **superseded** and
  should not be cited against these results.
- **Protocol + discrepancy**: state `dt`, history functions, and the **`Δt`-convergence table** (e.g.
  Scenario-A `A*`: 0.8022 at `dt=0.5` vs. 0.8021 at `dt=0.05`). Every "verified" number carries its
  protocol and its deviation from the original manuscript.
- **Concrete discrepancies to publish**: `b_final = 0.317` ⇒ `D ≈ 6.76` vs. the original table's
  `5.240 ⇒ b ≈ 0.336`; the endpoint `D_E` is method-dependent (5.26 / 6.74 / 18.70 for
  frozen/crashed/un-clamped); `τ_g* = 85.4 yr` vs. original 83; `τ_p* ≈ 231 yr` vs. 225.
- **The measured basin-shrinkage result (the most defensible numeric contribution; master 12G.2).**
  The qualitative "basin of attraction shrinks" (Scenario D) is *quantified*, not asserted: the stable
  fraction of the `(A₀,P₀)` initial-condition plane for the overshoot subsystem falls from
  **0.506 (no delays) → 0.042 (baseline `(τ_g,τ_p)=(30,25)`)**, and the standard IC `(1.0,0.1)`
  **flips from stable to collapse**. Report the stable-fraction as a function of `(τ_g,τ_p)` and add
  the two-panel figure. Complement it with the *closed-form* separatrix criterion `A_c(E)` (§4.2) —
  the measured fraction is the empirical witness, `A_c(E)` the analytic boundary; **report both.**
- **Provenance — these are ORIGINAL-model numbers (important, do not gloss).** The `0.506 → 0.042`
  basin fraction, the Scenario B/C endpoint `A ≈ 1.19` with population collapse, the `D_E ≈ 5.26`
  endpoint, and the `τ_g* = 85.4 / τ_p* ≈ 231` values were all computed on the **original
  gross-depletion model**, whose constant-parameter subsystem (S0) has a **unique interior attractor**
  (`M* = 0.740, P* = 0.370`). The **corrected** `(1‴)` S0 is *structurally different*: its
  "sustainable" state is a **one-sided boundary** at `A → A_max, P → b₀A_max/e` (the flow-only/orchard
  limit, where `E = B = bA`), and there is **no robust interior attractor** — any population overshoot
  into `E > bA` triggers the vicious-cycle collapse (`A → A_ext`). Consequently:
  - the original basin-shrinkage fraction does **not** transfer as a property of the corrected model —
    it must be **re-labeled as an original-model S0 result**, and
  - the corrected analogue is the **recover (`A→A_max`)/ collapse (`A→A_ext`) boundary** (with the
    one-sided/boundary caveat of §2.2/§7). **This is now computed (R1):** on the documented grid the
    recover fraction falls **39.9% (no delay) → 5.3% (baseline `(30,25)`)**; the regenerate-delay
    triggers an `A_max`-overshoot → `E>bA` → liquidation collapse, and the recover basin vanishes
    abruptly as `τ_g` crosses ~20 yr (figures `scans/r1_basin_baseline.png`,
    `scans/r1_basin_delay_response.png`; details `SCAN_risk_register_r1_r2.md`). A companion
    time-domain illustration (`scans/r1_recovery_vs_collapse.png`) shows the *same* initial condition
    `(A₀,P₀)=(1.0,0.1)` recovering (`A→A_max`, `τ_g=10`) versus collapsing (`A→A_ext`, overshoot
    `A→1.36`, `τ_g=30`) — the mechanism, in trajectories rather than only a basin fraction.
- **Scenario-D threshold is an accident, not a clean result (master 12G.5).** The D/not-D boundary is
  *near-critical*: `(20,20)` gives min `A = 0.631` and recovers, while `(30,25)` gives min `A < 0.6` and
  collapses (`0.6 = A_max/2`, the maximal-regeneration point, *not* a threshold). State the actual
  basin boundary, not a single point (the basin figure is the fix); this also explains the
  method-sensitivity (bare Euler, clamping).
- **Reporting rigour (master 12C / 12G.7).** (i) **State the grid range** of the stability scan and
  **normalise "barely positive" Re λ by `r`** (a margin of `< 0.01 yr⁻¹` is not small next to
  `r = 0.02`). **And the grid must actually be wide enough:** a scan over τ ∈ [0,80] yr **cannot
  rule out** a single-delay Hopf, because the competing demographic-delay Hopf appears only at a
  large τ_P ≈ 225 yr (slow ω ≈ 0.011 yr⁻¹) once parameters are perturbed off the knife-edge. State the
  location of any "no single delay destabilises" claim *as a function of* Λ/χ (which lag, if any),
  and ensure any such scan extends to τ_P ≳ 250 yr before concluding it. (ii) **State that no interpolation occurs** for the original `τ_g/τ_p` (both exact
  multiples of `Δt`), or use a genuinely non-multiple step. (iii) **Complete the scenario/parameter
  table** (which `e`, which lags, whether `T_b` is active; `F` is otherwise undetermined). (iv)
  **Analyse the trivial equilibrium `(A,P)=(0,0)` and the no-recovery region**; note that
  `A_max/2` is *not* where no-recovery begins. (v) **Reconcile the "max Ω not reported" footnote**
  with Fig. 4 (Ω peaks at ≈5.0 on `D`, ≈4.1 on `E`, clipped at 8.5).
- **Verified correctness (do not "fix"):** the characteristic equation and Appendix A linearisation;
  the two single-delay polynomials (modulo a harmless scalar factor, and *minus* the spurious `ω²+a₁₁²`
  and `ω=0` factors); the `τ_M ≈ 83 yr`,`ω≈0.026` one-delay Hopf; the two-mechanism collapse
  division; the `a₁₁ < r` condition (not `a₁₁ < 0`); the degree-4 `τ_M=0` polynomial.
- **The corrected characteristic equation, stability-crossing-curve and full-spectrum analysis is DONE
  (R2).** We applied the exact crossing-curve formalism (Hale & Huang 1993; Gu, Niculescu & Chen 2005)
  and a full-spectrum (roots of the characteristic equation) computation to the corrected `(1‴)` S0
  (see `model_sims/char_eq.py`). **Result — a structural, not a Hopf, instability:** linearising about an
  interior point `A*` of the equilibrium family `P=B(A)/e` gives
  `D(s;τ_g,τ_p)=(s−a₁e^{−sτ_g}−a₃)(s+r)−a_E a₄e^{−sτ_p}=0`, which has a **zero eigenvalue** `D(0)=0` on the
  whole family (a neutral continuum — no isolated interior attractor) and a **positive real** leading
  eigenvalue (`Re λ ≈ +0.62` at `A*=0.8`) for **all** delays. Scanning `s=iω` yields **no** imaginary-axis
  crossing, and the zero-delay `a₁₁<r` condition is **violated everywhere** (`a₁₁=G'(A*)+b/b_G ≥ 0.57 > r`).
  Accordingly the manuscript's `χ` two-gain **Hopf** classification (derived for the ORIGINAL model's
  interior attractor) does **not** transfer to the corrected S0; the crossing-curve method should be
  applied to the *boundary* equilibrium, not an interior point (figures `scans/r2_char_spectrum.png`,
  `scans/r2_a11_vs_delay.png`; details `SCAN_risk_register_r1_r2.md`). The original-model two-delay Hopf
  values (`τ_M≈83`, `τ_P≈225`, `s≈78.5`) remain original-model results and are labelled as such.
- **Add the "balanced-with-lags" scenario row (master B12 / receipt).** In the original model the
  *balanced* case (`e = r_opt`) **with** lags oscillates (the χ=1 Hopf, `τ_g* ≈ 85 yr`) rather than
  collapsing. **On the corrected S0 this row is not transferable** (no Hopf, §8 contrast below): the
  balanced case still lies on the *continuum* and its interior points are monotonically unstable, so the
  "no collapse at balance but oscillation with lags" dichotomy does not apply there. A full-`(6′)`
  recompute is required before asserting either outcome.

**Original Hopf picture vs the corrected monotone + neutral continuum (summary comparison).**

| | Original model (gross depletion) S0 | Corrected `(1‴)` S0 |
|---|---|---|
| Equilibrium | unique interior attractor `(M*=0.740, P*=0.370)` | **one-parameter family** `P = B(A)/e` (no isolated attractor) |
| Linearisation | interior point; `a₁₁ < r` can hold | interior point: `a₁₁ = G'(A*) + b/b_G > r` **everywhere** |
| Stability | stable for any single delay | **monotone positive-real eigenvalue** (≈ +0.62) for *every* delay |
| Hopf / onset | two-delay Hopf: `χ=1`, `τ_g*≈85`, `τ_P*≈225`, `s=π/ω` | **none**: `D(0)=0` (neutral continuum); **no** imaginary-axis crossing |
| Classification | `χ` two-gain Hopf (which-lag) | structural vicious cycle, no `χ`; crossing-curve → boundary eq. |
| Basin | stable fraction 0.506 → 0.042 | recover/collapse dichotomy 39.9% → 5.3% (R1) |

**Corrected-model scenario status (marking original-model benchmarks as non-transferable).**
The original-model scenario-table values are **not** corrected-model outputs; the corrected S0 is
structurally different, so each is either recomputed (R1/R2) or explicitly flagged non-transferable:

| Scenario | Original-model benchmark | Corrected `(1‴)` status |
|---|---|---|
| A (standard overshoot) | `A* = 0.8022` (dt-converged), stable | **computed (R1):** small-`τ_g` ICs recover to the boundary `A→1.2, P→1.09`; realistic lags → `A→A_ext` collapse |
| B/C (env recovers, humans collapse) | `A ≈ 1.19`, population collapse | **non-transferable.** Corrected attractors are recover (both `A`,`P` to the boundary) or both collapse — there is **no** mixed "environment recovers, humans die" attractor |
| D (basin shrinks) | stable fraction 0.506 → 0.042 | **computed (R1):** recover fraction 39.9% → 5.3% (recover/collapse dichotomy) |
| E (no mask) | `B ≈ 0.5588` via rising `M` (no mask) | §10: corrected masking is small-deficit only, non-generic |
| balanced-with-lags | oscillates (χ=1 Hopf, `τ_g*≈85`) | **non-transferable** (no Hopf on corrected S0); full-`(6′)` recompute needed |

**Empirical grounding of `τ_g` and the delay-response robustness sweep (v15, held in v16).**

- **Operational definition.** `τ_g` is the **regeneration/recruitment-response lag** — the delay between a
  change in the environment state `A` and the regeneration/recruitment response that rebuilds carrying
  capacity (`A(t − τ_g)`). In the paper's own framing, "a tree takes `τ_g ≈ 20–80 yr` to bear fruit."
  Concretely: **the time from environmental change until the regeneration/recruitment response begins to
  restore carrying capacity, approximated by the time to reach a substantial fraction (≈50 %) of the
  pre-disturbance productive capacity.** It is **decades-scale**, and is **not** the short lag before
  *measurable recovery onset* ("green shoots"), which is a few years and would place `τ_g` **below** the
  collapse cliff below — that would be a model misspecification, not a calibration.
  **Why 50 %.** The ≈50 % threshold is the point at which the regeneration/recruitment response has begun
  to restore carrying capacity in a way that (i) excludes the early transient "green shoots" that precede
  genuine regeneration, and (ii) matches the time to meaningful biomass/stock recovery in the cited field
  studies (forest AGB ≈50 % at ≈20 yr; soil SOC at a new equilibrium ≈20–23 yr). It is a **conservative
  definitional threshold, not a fitted value**: the collapse cliff sits at `τ_g ≳ 20 yr` either way, so
  the qualitative result does not hinge on the exact percentage.
- **Field-derived band (literature banding, cited; not a full digitisation).** *Forests:* AGB recovery is
  substantial by 20 yr (≈50 %), median ≈66 yr to 90 % of old-growth (Poorter et al. 2016, *Nature*
  **530**:211). *Soils:* SOC build-up begins ~5 yr and reaches a new equilibrium ~20–23 yr (Poeplau et al.
  2011, *Glob. Change Biol.* **17**:2415; IPCC 2006). *Fisheries:* rebuilding is slow and often
  incomplete — median ~12–13 yr to 50 %, 10 → >100 yr, many collapsed stocks never rebuild (Hutchings &
  Reynolds 2004; Neubauer et al. 2013). ⇒ **core band ≈ 10–40 yr; extended ≈ 5–60 yr**; the baseline
  `τ_g = 30` sits inside the band.
- **Delay-response sweep (R1/R2, baseline `τ_p=25`; `reports/empirical_tau_g_sweep.json`, `…_sweep.png`).**
  The **monotone structural instability (no Hopf, `Re λ ≈ +0.62`) holds for every `τ_g`**; the **collapse
  basin is robust (≈5 %) across the whole field-supported band**. A **1-yr-step fine sweep over
  `τ_g` ∈ [15, 25]** resolves the transition: the R1 recover fraction descends within a narrow band —
  **0.399 (`τ_g ≲ 17`), 0.394 (18), 0.240 (19), 0.053 (`τ_g ≳ 20`)** — so the "cliff" is a **steep
  transition band ≈ 18–20 yr** (half-way ≈ 0.24 at `τ_g = 19`), not a single hard edge. `τ_g ≲ 18` →
  recovery; `τ_g ≳ 20` → collapse; `τ_g ≈ 19` → the transition point.

  | `τ_g` (yr) | 0–17 | 18 | 19 | 20–60 |
  |:--|:--:|:--:|:--:|:--:|
  | R2 leading Re λ | 0.608–0.625 | 0.625 | 0.625 | **0.625 (constant)** |
  | R1 recover fraction | **0.399** | 0.394 | 0.240 | **0.0529** |

  So the collapse result **holds for `τ_g ≳ 20`** — the range the field data support for forests, soils,
  and many (non-recovered) fisheries — while the fast-regeneration regime (`τ_g ≲ 18`) is where the model
  returns the weak-sustainability/recovery outcome. State the interval **scoped**, never as a flat
  "10–40 yr": the relevant range for the collapse mechanism is `τ_g ≳ 20 yr`.

  **Figure caption (`empirical_tau_g_sweep.png`).** *R1 recover fraction (left) vs `τ_g` at `τ_p = 25` yr:
  ≈40 % for `τ_g ≲ 17` yr, falling to ≈5 % across a steep 18–20 yr band; the R2 leading real eigenvalue
  (right) stays ≈ +0.62 for every `τ_g` (monotone, no Hopf). Shaded: field-supported band (core
  ≈ 10–40 yr, extended ≈ 5–60 yr).* **The field-supported band lies entirely in the collapse regime for
  the baseline parameter set** — i.e. for the `τ_g` the literature supports (forests, soils, many
  fisheries), the model returns the collapse outcome, not recovery.
- **`τ_p` handling and robustness.** `τ_p` was held at `25 yr` for the sweep; the `(τ_g, τ_p)` grid
  (`reports/empirical_tau_g_tau_p_grid.json`, `…_grid.png`) now spans `τ_g ∈ {10,15,18,19,20,30}` ×
  `τ_p ∈ {10,20,25,30,40}`. The cliff is **governed by `τ_g`**: the recover fraction is **0.399 at
  `τ_g = 10–15`** and **0.053 at `τ_g = 30`** for **every `τ_p`**, and at the transition the intermediate
  values move only slightly with `τ_p` (0.399–0.394 at `τ_g=18`; 0.245–0.269 at `τ_g=19`; 0.053–0.058 at
  `τ_g=20`). So `τ_p` shifts the band by **< 1 yr across a 4× range (10–40 yr)** — the cliff is **not** a
  `τ_p` artefact. A **full two-delay sweep is left to future work**, but the coarse grid is no longer the
  only support: the flatness holds out to `τ_p = 10` and `40`.
- **Conditional on baseline parameters.** The transition and the recovery/collapse dichotomy are reported
  at the baseline `(b_G=0.8, A_ref=0.8, ρ=0.05, A_max=1.2, e=0.55, r=0.02)` and the documented IC grid; R1
  is robust to `b_G` (§13(6)), but a **full global sensitivity analysis over all parameters is not
  performed** — these are *conditional* statements holding while the other parameters stay at baseline.
- **Calibration outlook.** These are **qualitative/regime** claims from a **literature-banded sweep**,
  not a fitted forecast. A formal calibration (estimating `τ_g`, and possibly `b`, from a small set of
  well-documented case studies, or a full ML/Bayesian fit over `A`, `P`, `b`, `D`, `τ_g`, `τ_p`) is
  **feasible but not required** for the paper's conceptual claims and may not sharpen the conclusions given
  weak delay identifiability; it is left to **future/companion work**. The plan's Step 1a (per-study curve
  digitisation/extraction) is its prerequisite and is still pending (§ honesty caveat below).
- **Honesty caveat (residual).** This is a **literature-banded model sweep, not a full calibration**: the
  per-study curve digitisation and extraction table (the plan's Step 1a) is **still pending**, and `τ_g`
  here is a **lumped** regeneration-response delay across heterogeneous ecosystems (tropical/temperate
  forest, agricultural soil, marine fish). If the manuscript is submitted before that extraction is
  complete, state: *the empirical interval is based on published recovery curves and synthesis values; a
  formal per-study extraction of the regeneration/recruitment lag is **in progress**.* The defensible claim
  is that the collapse mechanism operates for any `τ_g` in the observed band — **not** that `τ_g` equals a
  single measured value. **Point-estimate/interval discipline (frame from the companion studies, P3/E3):**
  report `τ_g` as an **interval over the observed band**, not as a single number; and when a point margin is
  small relative to the spread of that band, do **not** present it as a precision result — the 50 % threshold
  here is a definitional choice, and the collapse cliff (≈18–20 yr) is the robust, band-level statement.

---

## 9. Policy extensions (Half-Earth & reservation)
- Cap the **human-available** flow at `σ B`; compute both `K` and the debt increment from that cap;
  report `Ω` against the **allocated** share (not full `B`); state whether lags/`T_b` are on. Then the
  impossible "`Ω = 0.575`, `D = 0`" pair is removed.
- Corrected cap: `K = 0.5 B / e` (not `0.5 B / r_opt`); verified to settle at `Ω → 0.500`, `P = 0.217`,
  and a **reservation policy that keeps `E` inside the allocated flow succeeds** (no liquidation).
- **The stabilising institutional *sign* is the protective one (frame from the companion delay study, P4 —
  frame only, no theorem).** ECOMOD's vicious cycle is the **mobilising / extractive** sign (demand responds to
  a perceived shortfall by raising pressure on the base); the §9 reservation/Half-Earth cap is the **protective**
  sign (demand is held to a cap). The companion distinguishes these two channels by *sign*, not by magnitude,
  and the protective channel is the one that keeps the loop gain below unity. The design principle this gives
  §9 is therefore a *sign* statement, not a delay statement: **the stabilising institutional response is the
  protective/effort-reducing one**, which is exactly why the reservation (protective) policy — not a
  mobilising one — is the candidate to pursue. State it as a framing (this paper does not prove a no-Hopf
  theorem for a protective channel); cite P4 as an unpublished framework.
- The debt-repayment dichotomy is resolved: report the qualitative change (collapse → oscillation for
  `η ≳ 0.02`) and treat `η = 0` as the irreversible-debt benchmark.
- **Discipline from the companion intervention studies (unpublished manuscripts, Amin Abaee) — declare a
  disturbance class and a retention rule before claiming a policy succeeds.** The reservation/Half-Earth
  result above ("`E` inside the allocated flow succeeds, no liquidation") is currently asserted under the
  *nominal* path. To make it defensible it should be scored as a **robust-viability** claim: declare a
  disturbance class (persistent productivity/`ρ`/`b`-shocks, as the companion cod and Edwards intervention
  studies do), define a **preregistered retention rule** ("a governance module is kept only if it improves
  a declared protection-and-supply score"), and apply an **erosion conversion** (convert the declared model
  defect into a certified-kernel erosion margin from the closed loop's contraction rate). Until that is done,
  state the result as a *nominal-path* consequence, **not** a robustly-viable policy claim. This is
  method-borrowing from the author's own companion works, cited as such — not a new result of this paper.
- **The reservation claim is certified only under a controller that observes the *typed* floor (frame from
  the companion obstruction-calculus study, P2 — frame only, no certificate).** §9's "`E` stays inside the
  allocated flow, no liquidation" result is scored against the *nominal* path. The reason it is only nominal
  is **structural, not "we haven't checked"**: the policy is certified for a controller that observes the
  **typed stock floor** `A` (and the allocated flow), **not** merely the composite `B`. If only an aggregate
  composite is observed, the obstruction view says **no** observation-based policy can guarantee the stock
  floor — the safe controls of the states consistent with a given observation may intersect **emptily**, so
  the failure is *informational* (which quantitative feature of the observation design — its **coarseness /
  aggregation** relative to the typed floor — is responsible) rather than dynamical. State this, so the reader
  sees the qualification is not a hedge but a declared information-structure boundary. Cite P2 as an
  unpublished framework; do not import any of its certificates.
- **Architecture-substitution caveat.** ECOMOD analyses *continuous* delays `τ_g, τ_p`. If a policy review
  cadence is modelled as **sample-and-hold / periodic review**, do **not** treat it as "the delay equation
  sampled at `T_r`": the two are different operators, and moving between them can move or delete stability
  boundaries (the companion governance papers state exactly this). Any future "review interval" extension must
  be a separate operator with its own monodromy, and continuous-`τ` conclusions must not be transferred to it.

---

## 10. Demonstration

**Fig. `IMPLEMENTED_demo.png`** (generated by `demo_unified.py`, the well-posed smooth-ramp solver) shows
a representative overshoot run: the stock `A`, biocapacity `B` and population `P` all rise (a
logistic overshoot / boom) and then the system collapses to the extinction floor with debt `D`
building up. Two model properties are visible and reproducible:
- the **delayed-regeneration overshoot** (`A` briefly exceeds `A_max` — the expected Hutchinson-style
  transient, here around a long `τ_g`/`τ_p`);
- the **debt → degradation → collapse** route, in which lifting yield `b` (the `t_wave` technology
  wave) raises `K`, `P`, and `E`, so that `D` accrues and `b` is eventually eroded.

**The productivity illusion ("`B` rises while `A` falls") — quantified, converged, and *conditional*.**
This is the one place where the corrected model does **not** reproduce the master's headline numbers,
and it must be stated plainly.

- **Method.** The reduced masking model (`dA/dt = G(A) − ramp(E−bA)/b_G`, `dD/dt = ramp(E−B) − ηD`,
  `B = bA + b_G G(A)`, `b = (b₀+T_b)e^{−αD}`, softplus ramp `w=0.05`) was integrated with a **converged
  RK4** (`mask_rk4.py`); a 7,128-case scan plus a deficit sweep (`deficit_map.py`). The softplus width
  `w = 0.05` is **stated**, and **insensitivity to `w`** should be reported (§13 point (4)); a mask is
  scored as a contiguous span with `dB/dt > 0` **and** `dA/dt < 0`, converged over `dt = 0.25 → 0.01`.
- **Result.** A **genuine mask exists, but only for a small initial deficit.** For the favourable
  configuration (`ρ=0.05, b_G=0.8, b₀=0.5, η=0.05, α=0.03, κ=0.2, t_wave=15, Δb=1.5`, `A₀=1.0`), the
  window is `5.4 yr` wide at deficit `E − b₀A₀ = 0.06`: across it (`t ≈ 1.4 → 6.8` yr) **`B` rises
  `0.576 → 0.647` (peak) while `A` falls `0.959 → 0.858`**; over the run from `t=0` (where `A=1.00`,
  `B=0.578`) the peak-`B` rise is `0.069` and `A` falls by `0.142` (fig. `IMPLEMENTED_demo_masking.png`,
  panel a). It is **converged** (identical at `dt = 0.1/0.05/0.02/0.01`), so it is *not* the Euler
  artifact of the withdrawn bare-Euler figure.
- **The mask is bounded and deficit-limited.** Window width grows with deficit up to `≈5.4 yr` at
  deficit `0.06`, then **collapses to zero at deficit `≈ 0.075`** (fig. panel b): beyond a small
  overshoot the stock-liquidation feedback dominates and technology cannot lift `B` — the run goes
  straight to the extinction floor with **no** mask.
- **Why this matters for the claim.** The master (Parts 12A.1, 12G.7) offered headline masking sets
  (`α=0.5, Δb=0.3, t_wave=100 ⇒ B 0.5→0.618` while `M→0.847`; and `e=1.15, α=0.2, Δb=0.8, t_wave=100,
  κ=0.05 ⇒ B 0.711→0.832` while `M→0.834`; "118 sets found"). **Those were computed on the *original*
  gross-depletion model, not on `(1‴)`; they do not carry over.** Under the corrected well-posed model,
  the illusion is reproduced only in the narrow small-deficit band above. The paper's "rising
  biocapacity masks a falling stock" narrative is therefore **conditional**: it holds *near balanced
  conditions*, and *fails* under a genuine overshoot (deficit ≳0.075, ≈15 % of the initial flow yield
  `b₀A₀`) — which is precisely the Jevons-rebound logic of §5 (technology raises `K`, `P`, `E`, so
  debt grows and closes the window). Add the master's proviso explicitly: the illusion **requires the
  wave to outpace the debt build-up** — it must arrive while the stock is still high and the cumulative
  deficit is still small. A slow/late technology wave merely props up a *falling* yield and cannot
  produce a real "B rises while A falls" window.

**The illusion is an instance of the compensatory-aggregation gap (frame from the companion separation
study, P1 — frame/analogy only, not a theorem).** This is the single most useful way to read it. The
weighted *composite* (`B`, the weak-sustainability index) satisfies its **aggregate floor** while the
**typed** floor — the stock `A` — is violated. To say it in this paper's notation: the aggregate that an
index reads is a weighted sum over several floors, so a deficit in one (the stock) can be masked by a
surplus in another (the yield), and a transition can satisfy the aggregate the whole way along while it
never satisfies the individual floors. Two consequences follow without importing anything:
- It answers "is this robust or a parameter quirk?" — the mask is a **structural failure of any
  aggregate that compensates a falling base with a rising yield**, not an accident of one parameter set.
- Under **exact-tube semantics** (a transition is safe only if *every* state along it, **not merely the
  endpoint**, satisfies the constraints), the intermediate passage where `A` falls is itself a violation
  **even if the endpoint recovers**. That is a precise reason to report the through-time trajectory (and
  the boundary curve of §13) rather than only an endpoint attractor. Cite P1 (unpublished manuscript,
  Amin Abaee) for this framing; it is not a result of this paper.
- **Why the paper's own Scenario E shows no illusion (master 12A.1 caveat (i)).** In the original
  Scenario E (`Δb=0.3, t_wave=150`) biocapacity does reach ≈0.5588, but **because `M` is rising** (the
  logistic overshoot off the low starting population), *not* because of the masking mechanism — so
  "no shown scenario exhibits the illusion" is the correct reading there. State this explicitly when
  discarding the headline set, so the reader sees the illusion was never demonstrated, only reached by
  a different route in that scenario.
- **Presentation rule.** Present the illusion as **narrow, deficit-bounded, and transient** (fig.
  `IMPLEMENTED_demo_masking.png`), with the computed `t_peak` and the critical deficit stated as
  numbers — never as a generic, robust result. (The withdrawn Euler figure should not be cited.)

---

## 11. Epistemic label (C)
This is a **conceptual / stylised model with representative calibration** — not a forecast. Its
purpose is to make explicit the logic connecting accounting, deficit, lags, and the stock/yield
decomposition, and to state which outcomes are *emergent* (falsifiable) versus *imposed* (logistic
regeneration, bounded technology, the lags, the accounting identity). The 1961–2022 sentence is
rewritten as a *qualified observation*: GFN accounts are conservative (biocapacity likely overstated,
overshoot understated); the series is *consistent with* the illusion reading but does not demonstrate
it. **National Footprint Accounts (NFA) data limitation (master didactics).** The GFN accounts are
*account-based*: they rely on measured yields and conversion factors, and do **not** capture soil
erosion, deforestation, groundwater depletion, or other cumulative degradation. Consequently the
estimated **biocapacity most likely overstates** the real resource base and the **Footprint most
likely understates** the true overshoot — i.e. the actual overshoot is likely *larger* than the
accounts document. This is the strongest reason to treat the 1961–2022 series as "consistent with"
the illusion reading rather than as evidence for it. The empirical programme the Discussion promises
is the **`d ln B = d ln b + d ln A`** decomposition with independent `A`-proxies (land cover, soil
carbon, NPP).

**Information-layer limit on the illusion (companion-study discipline, not a new result).** The
*signature* of the illusion — "`B` rises while `A` falls" — is **contemporaneously observable** (it is a
readoff of two measured series). But *whether* that rise is a genuine recovery or a technology-driven
**mask** is **not identifiable at the observation time**: identifying the mask requires knowing the
technology/`b`-channel contribution, which is not a signal available contemporaneously without independent
proxies. This is the same information-layer distinction the companion forecast-evaluation studies draw as
"an information-layer rent — the gap between what is knowable at the forecast origin and the oracle, which
no signal available at the origin recovers." Two consequences for this paper: (i) a real-time *observation*
of `B` rising while `A` falls is **not** evidence for the mask mechanism over the recovery mechanism —
both reproduce the same signature; and (ii) the empirical programme must therefore target the **`b`-channel
decomposition** (independent `A`-proxies), not the composite `B` series. Cite the companion
forecast/intervention manuscripts (unpublished manuscripts, Amin Abaee) for this discipline; do **not**
present it as a published result.

**The empirical programme is a flux-reconstruction, not a curve-fit (frame from the companion typed-ledger
study, P3 — frame only).** The `b`-channel (the technology contribution to yield) is precisely an
**unobserved internal flux**: it is not separately measured, but it is induced by the observed stock
changes. The typed-ledger frame gives the correct discipline for this — **reconstruct unobserved internal
fluxes from observed stock changes, and state which fluxes are identifiable** (the ledger identifies
fluxes only up to its declared observation operator; a flux that is not a readout of a measured stock is
not recoverable). So the programme is bounded: the `b`-channel is recoverable **only relative to a
declared observation operator**, which is why independent `A`-proxies are needed rather than a fit to the
composite `B`.

---

## 12. Review-point → revision coverage (the receipt)

> **Automated cross-check.** This receipt is backed by the formal traceability matrix
> `SCAN_traceability_matrix.md` (generated by `trace.py`), which maps each master item (Parts 12A–12G)
> to a status and a revision location, plus `SCAN_numerical_audit.md` / `SCAN_regression_report.md`
> (independent re-computation) and `SCAN_risk_register.md` (still-open items).

| Review/audit point | Where implemented here |
|---|---|
| B2 (deficit vs gross depletion) | `(1‴)` deficit `[E − bA]₊/b_G` (§2.2) |
| B1 / a₁₁ < r / false a₁₁ < 0 | §4.3, §8 |
| B3/B4 (delay placement) | `τ_g` recruitment + `K(t−τ_p)` (§2.2, §3) |
| B5 (additive floor → asymmetry false) | multiplicative `(7′)` (§2.2) |
| B6/B7 (co-evolution, general γ) | §3 (stated as a choice; γ ≠ 1 offered) |
| B8/B10/B11 (ρ implausible; η contradiction; no equilibrium) | §2.2 `(6′)` + `η` primary §4; §9 |
| B12 (nothing shown for balanced-with-lags) | §5, §8 (add the sustainable-with-lags row) |
| M_max/2 false threshold | §5 (emergent `A_c(E)`/`B_max`; no Allee) |
| Λ sign reversal | §4.3 corrected (`χ>1 ⇒ τ_g`, `χ<1 ⇒ τ_p`) |
| polynomial degree/ω=0 spurious roots | §8 |
| units / GFN convention mandatory | §2.1 |
| Half-Earth Ω=0.575 | §9 `K=0.5B/e` |
| 1961–2022 over-claim | §11 |
| K is a state; "2-D"; "first-order" | §3, §8 |
| ρ implausible / fast-slow validity | §4.3 (valid only while a₁₁ ≤ 0) |
| circular "verified to machine precision" | §8 (protocol + discrepancy) |
| orchard analogy (rounds 1–2) | §2.2 unified model; §4 (flow/increment; ψ) |
| presentation/hygiene (review §8, E1–E5) | §7 |
| reviewer (b)–(g) | §3 (c), §7 (d/f/g), §8 (e), §2.1 (b/f) |
| productivity illusion (12A.1 / 12G.7) | §10 (converged; *small-deficit only*, deficit-bounded) |
| measured basin-shrinkage (12G.2) | §8 (0.506→0.042, original) + **R1 corrected basin 39.9%→5.3%** + `A_c(E)` §4.2 |
| R1 / R2 resolution (corrected basin + char-eq/spectrum) | §8, §13 (computed; `SCAN_risk_register_r1_r2.md`) |
| dimensionless group set (12G.3) | §4.4 |
| Scenario B/C "recovers/collapse" (12G.4) | §5 |
| Scenario-D threshold accident (12G.5) | §8 |
| debt-lag τ_D / delay asymmetry (12G.7) | §3 |
| Jevons-type rebound (12G.7) | §5 ("technology offsets debt") |
| reporting rigour: grid/Ω/interp (12C, 12G.7) | §8 |
| scan-range sufficiency / τ_P≈225 yr Hopf (12C.9 + eval H / register F4) | §8 reporting-rigour (i): state range as f(Λ); scan to τ_P ≳ 250 yr |
| companion import — aggregate/typed gap identified as structural | §10 (P1 framing) |
| companion import — ledger book declared for `A`, `b·A`, `D` | §2.2 (P3); flux/identifiability §11 |
| companion import — observation-limited (informational) nonviability stated | §9 (P2 framing) |
| companion import — stabilising controller *sign* identified | §9 (P4 framing) |

---

## 13. Residual risks (honest)

> **Scope of verification — R1 and R2 are now RESOLVED (computed), not deferred.** Both were
> originally logged as open required work; they have since been computed on the corrected `(1‴)`
> model and are reported in §7/§8 and in `SCAN_risk_register_r1_r2.md`
> (`model_sims/r1_basin.py`, `model_sims/char_eq.py`, `model_sims/corrected.py`). The **quoted numeric
> results for the original model** still must carry their provenance: the corrected `(1‴)` S0 is
> structurally different from the original's (a one-sided boundary at `A→A_max, P→b₀A_max/e` and no
> robust interior attractor), so **the original-model numbers quoted in §8 (the 0.506→0.042 basin
> fraction, the Scenario B/C ~1.19 endpoint, the `D_E ≈ 5.26`, and the `τ_g* ≈ 85/τ_p* ≈ 231` Hopf
> values) are original-model results and are labelled as such throughout.** The structural, analytic,
> and didactic conclusions in this revision — the unified `(1‴)`, `A_c(E)`/`B_max`, the `χ`
> classification, the four falsifiable predictions, the Jevons rebound — are properties of the
> corrected model. **R1/R2 results are properties of the corrected model and do NOT inherit the
> original-model provenance caveat.**

**What R1 and R2 now establish (summary).**
- **R1 (basin recompute, corrected `(1‴)`).** On the documented `A0×P0` grid (13×16=208, `P`
  straddling `B*=b₀A_max/e≈1.09`), the recover-fraction of the corrected S0 falls from
  **39.9% (no delay) → 5.3% (baseline `(30,25)`)**; the collapse fraction rises 60.1% → 94.7%.
  With the regeneration delay the stock overshoots `A_max` (≈1.36), the population tracking the
  delayed `K` overshoots into `E>bA`, and the vicious-cycle liquidation drives `A→A_ext`. The
  recover basin vanishes abruptly as `τ_g` passes through ~20 yr (`scans/r1_basin_baseline.png`,
  `scans/r1_basin_delay_response.png`).
- **R2 (characteristic equation / crossing curves / full spectrum, corrected `(1‴)`).**
  Linearising the corrected S0 about an interior point `A*` of the equilibrium family `P=B(A)/e`
  gives a characteristic equation `D(s;τ_g,τ_p)=(s−a₁e^{−sτ_g}−a₃)(s+r)−a_E a₄e^{−sτ_p}=0`. **It has a
  zero eigenvalue `D(0)=0` on the whole family** (a neutral continuum — the S0 has no isolated
  interior attractor), and its leading mode is a **positive real eigenvalue** (`Re λ ≈ +0.62` at
  `A*=0.8`) for **every** delay — a **monotone** vicious-cycle instability, not a Hopf. Scanning
  `s=iω` finds **no** imaginary-axis stability-crossing curve, and the manuscript's zero-delay
  `a₁₁<r` condition (`a₁₁=G'(A*)+b/b_G`) is **violated at every** interior point (`a₁₁≥0.57>r`).
  Consequently the manuscript's `χ` two-gain *Hopf* classification (derived for the ORIGINAL model's
  interior attractor) does **not** transfer to the corrected S0; the corrected model's instability
  is a structural (monotone) one, and the crossing-curve method should be applied to the
  appropriate *boundary* equilibrium rather than an interior point
  (`scans/r2_char_spectrum.png`, `scans/r2_a11_vs_delay.png`).

**(1) R1 and R2 are now resolved, not "known but hidden."** Both were computed on the corrected `(1‴)`
S0 and are reported above and in §8/`SCAN_risk_register_r1_r2.md`. The key results to carry forward:
**R1** — recover fraction falls **39.9% → 5.3%** on the baseline `(τ_g,τ_p)=(30,25)` grid (collapse
fraction 60.1% → 94.7%); **R2** — the corrected S0 has a **neutral zero eigenvalue** across the whole
equilibrium family `P=B(A)/e` and a **monotone positive-real leading eigenvalue** (≈ +0.62) for every
delay, i.e. **no Hopf**. There is no outstanding "required work" on R1/R2. The corrected S0's numbers
are now rendered in the §8 **corrected-model scenario-status table** and the **Hopf-vs-monotone contrast
subsection**; the simulator-corrections note is in §8, and the original-model provenance of the §8 quoted
numbers is stated there. What remains is human review and the (deliberate, non-automated) full-`(6′)`
scenario recompute flagged as non-transferable in that table.

**(2) The fast–slow `χ` reduction is valid only for `ρ ≫ r`; all of R2 uses the full equation.** The
χ-classification of §4.3 reduces the 2-D two-delay system to a scalar two-gain delayed logistic under the
fast–slow separation `ρ ≫ r` (and while `a₁₁ ≤ 0`). That separation is **not** satisfied at realistic
`ρ`. The table below (computed at the sensitivity configuration `τ_g=30, τ_p=25, A*=0.8, b₀=0.5,
b_G=0.8, e=0.55, r=0.02`) reports the leading real eigenvalue of the **full** transcendental
`D(s;τ_g,τ_p)=0` alongside the fast–slow `a₁₁` and the timescale ratio `ρ/r`:

| `ρ` (yr⁻¹) | full-`D(s)=0` leading `Re λ` | fast–slow `a₁₁ = G′(A*)+b/b_G` | `a₁₁ > r`? | `ρ/r` |
|:--|:--|:--|:--:|:--:|
| 0.02 | +0.625 | 0.618 | yes | 1.0 |
| 0.05 | +0.625 | 0.608 | yes | 2.5 |
| 0.10 | +0.625 | 0.592 | yes | 5.0 |
| 0.50 | +0.625 | 0.458 | yes | 25 |
| 1.50 | +0.625 | 0.125 | yes | 75 |

Where the reduction **fails**: only at `ρ = 1.5` (`ρ/r = 75`, well separated) is the fast–slow scaling
justified, and even there `a₁₁` stays positive — no qualitative flip. At realistic `ρ ∈ [0.02, 0.1]`
(`ρ/r = 1–5`, not ≫ 1) the reduction is **out of its regime**, so the full `D(s)=0` must be used. R2
always uses the full equation. Note also the full leading eigenvalue is essentially **independent of `ρ`**
(≈ +0.62, dominated by the depletion gain `a₃ = b₀/b_G`) — itself evidence that the monotone instability
is structural, not a fast–slow artifact, so the χ-Hopf classification of §4.3 does not carry over (§8,
point (8)).

**(3) `η` is set physical (non‑zero); the singular `η → 0` case concerns the full `(6′)` model, not
R1/R2.** R1 and R2 operate on the **constant-parameter S0** (`D` and `η` dropped), where `η` is
**absent** — so the R1/R2 results do **not** inherit the η-singularity caveat. `η → 0` applies to the
**full `(6′)`** (`dD/dt = [E−B]₊ − ηD`), where `η` decides whether an equilibrium exists. We set
`η = 0.05 yr⁻¹`, justified as a **minimal environmental regeneration / degradation-removal** rate: the
accumulated "debt" is partially replenished by slow (≈20-yr) natural regeneration of the degraded
resource base. Outcomes are **insensitive to `η` over a modest range** provided `η > 0` (only the
*existence*, not the *magnitude*, of the equilibrium decision depends on it); `η = 0.05` is the value used
in the §10 converged masking run and is recorded in the §3/§8 assumptions. A reader setting `η = 0` is
deliberately removing the regeneration channel and should be told it removes the equilibrium rather than
perturbing it.

**(4) The sustainable point is a boundary equilibrium; stability is one-sided; the exact switch adds no
spurious oscillation.** The exact `[·]₊` is **non-smooth** at `A = A_max` (and at `E = bA`), so the
corrected S0's "sustainable" state is a **boundary of the deficit regime, not an interior point** —
linearise **one-sided (from the deficit/lower side only)** and report that stability as such (§7, §8).
R2 linearised the **exact** switch and found **no** imaginary-axis crossing, so **the non-smoothness does
not create spurious oscillations** — the manuscript should say so explicitly. Where a smooth ramp
replaces `[·]₊` (original-model reference implementation only), fix its width `w`, state it, and report
**insensitivity** to `w`; the corrected model is never run with `ramp_soft=True` (§8).

**(5) Masking illusion — small-deficit only, not generic.** §10 and §1 already bound it: the window
maxes at **≈5.4 yr** (deficit 0.06) and **vanishes at deficit ≈ 0.075** (≈15 % of the initial flow yield
`b₀A₀`), and it is **converged** (RK4, not the Euler artifact). Make the caveat explicit in the paper:
the illusion is **not generic**; it **does not appear for deficit ≳ 0.075**, and it must **not be cited
as a general phenomenon** — only as the narrow, transient, small-overshoot band of §10. The withdrawn
Euler figure (`demo_masking_euler.png`) is **not** referenced; only the converged
`IMPLEMENTED_demo_masking.png` is cited.

**(6) Parameters are representative, not estimated; the two headline results have been sensitivity
checked.** The results are **illustrative** and need calibration; `b_G`, `α` and the lags are lumped,
not measured. `τ_g` is the partial exception: it is now **field-banded** (§8, v15/v16 empirical-grounding
note) as a **regeneration/recruitment-response lag** (≈time to ~50 % of pre-disturbance productive
capacity), and the 1-yr-step fine R1/R2 sweep shows the **collapse basin and the monotone no-Hopf
instability are robust across that band for `τ_g ≳ 20 yr`** (transition band ≈18–20 yr), with the extended
`τ_p` grid (**{10,20,25,30,40}**) **not** moving the cliff; the fast-regeneration regime `τ_g ≲ 18` is
instead where the model returns the recovery outcome. **Fit-defect disclosure (frame from E2):** any parameter that sits **pinned at an
optimization bound** (a fit artefact rather than an estimate) is *declared* as such — E2 reports its
`K` at its bound as a "declared fit defect" — never presented silently as a calibration.
**Interval discipline (frame from E3):** a point-margin that is small next to an
uncertainty scale should be reported as a *coin-flip*, not as skill/stability — as E3 records for its
AR(1) improvement "whose bootstrap interval covers zero… a coin-flip recorded by a point-RMSE rule, not
a skill claim." Apply the same wording discipline to any tight margin here. Robustness:
- **Recover–collapse (R1) is robust to `b_G`.** On the documented grid (computed, `(30,25)` baseline):

| `b_G` | recover (no delay) | recover (baseline `(30,25)`) | Δ |
|:--|:--|:--|:--:|
| 0.4 | 0.394 | 0.053 | 0.341 |
| 0.6 | 0.399 | 0.053 | 0.346 |
| 0.8 | 0.399 | 0.053 | 0.346 |
| 1.0 | 0.404 | 0.053 | 0.351 |
| 1.2 | 0.404 | 0.053 | 0.351 |

Over a **3×** range of the standing-stock value, the no-delay recover fraction varies only 0.394→0.404
(±1.3 %) and the baseline-delay recover fraction is **pinned at 0.053** — so the qualitative result
"the regeneration delay collapses the recover basin from ~40 % to ~5 %" is **robust**, not a `b_G`
artefact.
- **The monotone instability (R2) is structural** (independent of `ρ`; §(2)), and the **masking band** is
  bounded by the §(5) deficit limits. `α` and `τ_p` were **not** independently swept here (each needs its
  own RK4 grid sweep); state `α = 0.03` and `τ_p = 25` as **illustration values needing calibration**,
  and soften the "dangerous band `(2f−1)ν > 1`" to "an **estimated** indicator" (§4.3).

**(7) Priority/literature — be precise.** The delayed-logistic *stability* result is **Hutchinson
(1948)**; we **cannot support** the claim that Haberl & Aubauer "first introduced" time delay into human
population dynamics — they *apply* the delayed-logistic framework to human load, they do not originate it
(§7). Add the **GFN-caveats** sentence: the accounts are aggregate and data-limited (measured yields and
conversion factors; no soil erosion, deforestation or groundwater depletion), so biocapacity is likely
**overstated** and the Footprint **understated** — meaning the 1961–2022 series is a **lower bound** on
genuine overshoot.

**(8) R1/R2-derived caveats that must accompany the results.** (i) **Monotone, not Hopf:** the leading
mode is a positive-real eigenvalue with **no imaginary-axis crossing**, so the old `χ` two-gain **Hopf**
classification derived for the ORIGINAL interior attractor does **not** transfer (§4.3, §8); the
abstract's "'onset of instability is controlled by χ'" phrasing is the original-model interior-attractor
statement — on the corrected S0 the instability is instead monotone and structural. (ii) **Neutral
continuum / no isolated interior attractor:** `D(0)=0` on the whole family `P=B(A)/e`, so there is no
isolated interior attracting state; the sustainable state is the **boundary** `(A_max, P=b₀A_max/e)`. Do
not report a "stable fraction of an interior point" for the corrected S0. (iii) **Grid-dependence of the
recover fraction is bounded but real** (computed, `τ_p=0`, same integrator, coarse 6×8 vs fine 25×31):

| `τ_g` (yr) | fine (0.05 step) | coarse (0.2 step) | fine / coarse |
|:--|:--|:--|:--:|
| 30 | 0.027 | 0.104 | 0.26 |
| 40 | 0.212 | 0.208 | 1.02 |
| 50 | 0.301 | 0.417 | 0.72 |
| 60 | 0.321 | 0.396 | 0.81 |

The **coarse grid overstates** the recover fraction near collapse (at `τ_g=30`: 0.104 coarse vs 0.027
fine), so publish the recover fraction computed on the **fine** mesh and report the coarse value only as a
bound. **More interpretable than a percentage — the boundary-curve result.** Under **no delay** the
separatrix (recover vs collapse boundary in `(A₀,P₀)`) is exactly the **equilibrium family line
`P₀ = B(A₀)/e`**: "recover ⟺ `P₀ < B(A₀)/e`" matches the classification on **99.0 % of the 208-cell grid**
(the only two exceptions are `A₀ > A_max`, outside the stock domain). This is the numerical witness to
R2's neutral continuum: the recover basin is precisely the *stable side* of the equilibrium line. Under
**baseline delays `(30,25)`** the basin collapses to a thin strip **`A₀ ≈ A_max` (1.2) with
`P₀ ≲ B(A_max)/e ≈ 1.09`, and nothing else recovers**, i.e. the delay strips away the protected
below-the-line region except right at the sustainable boundary (5.3 %). Present the boundary curve
(`P₀ = B(A₀)/e`) rather than only the fraction. (iv) **The delay-response non-monotonicity at `τ_g ≈ 40–60` is real, not a grid artifact.** The
fine grid confirms and sharpens it: the recover fraction has a **deep minimum at `τ_g=30` (≈0.03, the
vanished basin) and re-opens to ≈0.21 (40), ≈0.30 (50), ≈0.32 (60)**; the coarse grid shows the same
min→rise shape (0.10 → 0.21 → 0.42 → 0.40), so the re-entry is **retained**. A boundary (separatrix)
curve as a function of `(τ_g,τ_p)` is the natural follow-up to the §8 R1 figure.

**Companion-study discipline and attribution (Amin Abaee; all nine are unpublished manuscripts).**
**All companion works are by the same author (Amin Abaee) as this paper** — they are his own companion
manuscripts, cited here as the shared body of work, **not** as independent corroborating sources. They
strengthen this paper's *methods* and *framing*, and none of their results is claimed as this paper's own.
Several of the above caveats are strengthened by *methods* from the author's own companion manuscripts
(P1–P5 theory, E1–E4 empirical; all **unpublished manuscripts**, never "submitted," "under review," or
"in press"). The frameworks borrowed (each re-expressed in this paper's notation, cited, never imported as a
result) are, with their sites:

- **Negative certificate, not a null** (E1) — §13, §10: R2's "**no** imaginary-axis crossing" and §10's "the
  illusion **does not appear** for deficit ≳ 0.075" are **negative certificates** — machine-verified
  *non-retention* / *certified non-existence*, deliberately **distinct from a statistical null**; closures,
  not "absence of evidence."
- **Information-layer limit** (E1/E3) — §11: the illusion's *cause* is not identifiable at the observation
  time; under the typed-ledger frame (P3) the `b`-channel is an **unobserved internal flux**, recoverable
  only relative to a declared observation operator.
- **Robust-viability discipline** (E2/E4) — §9: declare a disturbance class + preregistered retention rule,
  apply an erosion conversion, before claiming a policy succeeds.
- **Compensatory-aggregation gap** (P1) — §10: the "`B` rises while `A` falls" signature is an instance of
  an aggregate satisfying its floor while a typed floor is violated; report the through-time violation, not
  only the endpoint (exact-tube semantics).
- **Typed-ledger / double-counting discipline** (P3) — §2.2, §11: three distinct "books" (`A` increment,
  `bA` flow, `D` debt); conservation from the incidence structure, positivity from donor limitation; fit
  defects pinned at a bound are *declared*, not silent.
- **Incomplete-observation nonviability** (P2) — §9: the reservation claim is certified only under a
  controller that observes the **typed** stock floor, not merely the composite; otherwise the safe controls
  of compatible states may intersect **emptily** (an information-structure, not dynamical, failure).
- **Mobilising vs protective controller *sign*** (P4) — §9: the stabilising institutional response is the
  protective/effort-reducing one, which is why the reservation policy is the candidate. (Borrowed as a *sign*
  design principle; this paper proves no no-Hopf theorem for a protective channel.)

Each is a method-borrowing; none is a result imported from the companions, so there is **no duplication and
no self-plagiarism** — always re-derive in this paper's notation and cite the companion.

**Citation note.** The nine companion works (P1–P5, E1–E4) are **unpublished manuscripts** by Amin Abaee.
Where referenced, cite them as *"Abaee, A., *Title*. Unpublished manuscript."* — using exactly
**"Unpublished manuscript"** (or **"Manuscript in preparation"**), and **never** "submitted," "under
review," or "in press." The recommended entries, keyed to the latest version in
`arena agent 1/paper rewrites`, are:

- Abaee, A. *The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong
  Sustainability Assessment.* Unpublished manuscript.
- Abaee, A. *An Obstruction Calculus for Viability under Incomplete Observation.* Unpublished manuscript.
- Abaee, A. *Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, and the
  Semantics of Depletion Horizons.* Unpublished manuscript.
- Abaee, A. *Delay-Induced Regime Change in Harvested Stocks: The Mobilising and Protective Channels of
  Institutional Feedback, and the Review Interval as Control.* Unpublished manuscript.
- Abaee, A. *Periodic Review as Sampled Governance: Sample-and-Hold Dynamics of Assessment-Driven Effort
  Control, a 42-Stock Spectral Null, and the Northern Cod Case.* Unpublished manuscript.
- Abaee, A. *Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO
  2J3KL.* Unpublished manuscript.
- Abaee, A. *Robust viability of the 2J3KL limit reference point under a surplus-production map: policy
  scoring, expansion, and when catch cannot help.* Unpublished manuscript.
- Abaee, A. *Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test
  at J-17.* Unpublished manuscript.
- Abaee, A. *Governance operators and viability kernels of the Edwards Aquifer: an intervention-selection
  test at J-17.* Unpublished manuscript.

Do **not** treat these as citable published sources or as evidence independent of this paper.

**Specific companion findings that independently support this paper's corrected-model picture (method /
analogy only — no companion result is claimed as this paper's own).** Two are directly relevant:

- **A constant-productivity surplus-production map cannot produce a crash-then-recover trajectory**
  (cod companion, E1). In the fitted collapse-window parameterisation the scalar one-step map has two
  positive equilibria — a lower *repelling* point (≈144 kt) and an upper *attractor* (≈889 kt), and is
  monotone below ≈783 kt — so every trajectory either settles to the attractor or collapses; **no path that
  crashes and then recovers is a trajectory of the map.** This is the companion's analogue of this paper's
  corrected-S0 result that the interior is monotonically (vicious-cycle) unstable and there is **no**
  oscillatory/Hopf recovery: two structurally different models reach the *same* "monotone, no
  crash-then-recover" conclusion, which is corroborative, not duplicative.
- **The scored predictand is the productive *stock*, not the catch** (cod, E1; the same separation as E3's
  "head (index) vs store (resource) vs flux (flow)"). E1 states plainly that "a fishery can return a high
  extracted yield while the stock that produces it declines," and forecasts/assesses the **stock**, not the
  catch. This is exactly this paper's `A` (stock) vs `B` (biocapacity/yield) vs `E` (footprint/demand)
  separation, and independently supports the "`B` can rise while `A` falls" reading — the illusion signature
  is a *stock vs yield* divergence, not a demand artefact.
- **Scoping discipline from E1/E4**: E1's negative certificate is explicitly *scoped to the estimator and
  ladder* (not a coarse "model X fails" claim), and E4 reports its findings as a **three-verdict** form (a
  nominal result at one threshold; **not certified** at another; nothing retained at a third). Both
  reinforce this paper's requirement that the "no Hopf"/"no illusion beyond a deficit" conclusions be
  stated **scoped**, not as universal negatives.

For an audit-trail-complete revision, the process items are gathered here so the paper and its
metadata carry them (not left in the master alone):

- **Claims ledger + mechanism↔equation map.** The §12 "review-point → revision coverage" table IS
  the claims ledger: every review/audit point, its source ID (B2, a₁₁<r, M_max/2, Λ sign, GFN
  convention, orchard rounds, reviewer (b)–(g), …), and *where* it is implemented. It doubles as the
  mechanism↔equation map (each mechanism → the equation `(1‴)/(B)/(E)/(4′)/(6′)/(7′)/(8′)`/§ that
  implements it). Keep both in the paper; do not ship only the narrative.
- **Attribution in an appendix.** Attribute each block to the source that contributed it — the two
  model audits, the two meta-audits, the human reviewer (b)–(g), the two orchard rounds, and the
  findings/all-sources registers — so nothing is claimed as novel that came from a specific audit
  (e.g. the `a₁₁ < r` correction, the χ/Λ sign, the GFN convention, the ψ decomposition). The
  consolidated source list and per-point attribution go in an appendix, keyed by the §12 IDs.
- **Decision document.** This revision deliberately restructures the master as a *decision* document
  (what was kept, what was changed, what is open) rather than a continuous audit narrative — the
  §5 "original claim → corrected claim" table and the §12/§13 receipts are the decision record.

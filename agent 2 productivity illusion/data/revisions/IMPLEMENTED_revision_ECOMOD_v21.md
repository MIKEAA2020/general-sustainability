# Carrying Capacity, the Biocapacity Ratio, and the Productivity Illusion: Deficit-Driven Collapse in a Delayed Coupled Human–Environment Model

## Abstract

Coupled human–environment models often treat carrying capacity as an imposed ceiling. We show it is instead
an emergent quantity, and that treating it as fixed can produce a false sense of environmental health. We
develop a minimal deterministic model in which biocapacity is the sum of a separable flow yield and a stock
increment, cumulative overshoot accumulates as ecological debt that degrades yield, and environmental
regeneration and demographic response act through two distinct delays. The model is deliberately stylised,
with representative parameters, and its eight predictions are stated as falsifiable hypotheses. Three
results follow. First, the constant-parameter subsystem admits a one-parameter family of equilibria rather
than an isolated attractor, and any interior point is monotonically unstable — a positive real eigenvalue for
every delay, with no imaginary-axis crossing. The collapse onset is therefore a structural vicious cycle, not
a delay-ratio Hopf, and is not governed by a single stability index. Second, the operating boundary is the
biocapacity ratio `R_B = 1` (footprint equal to total biocapacity); the flow-yield ratio `R_A = 1` is a
leading but non-causal signal, and once the regeneration lag is long neither ratio warns. Third, a
sufficiently early technology wave can make biocapacity rise while the stock falls — but only for a narrow,
small-deficit window of about five years that vanishes beyond a modest overshoot. This is a productivity
illusion, not improving health: yield gains saturate while debt compounds, and the same technology raises
biocapacity, sustainable population and aggregate demand, tending to increase cumulative debt under
overshoot.

**Keywords:** carrying capacity; ecological footprint; biocapacity; time delay; ecological debt; sustainability; delayed feedback

---

## 1. Introduction

Standard treatments of human–environment coupling impose carrying capacity as an exogenous ceiling or infer
it from a simple ratio of supply to demand. This is convenient but conceals the structural content that
matters for sustainability assessment: whether the environment can sustain a given population is not a fixed
number but a function of the state and of what is being harvested. In particular, biocapacity is not a
single homogeneous flow. Part of it is a yield that can be taken without reducing the productive base (the
fruit of an orchard), and part of it is a stock increment that can only be removed by liquidating the base
itself (the timber of a forest). The share of these two components — the flow share `ψ` — governs how the
system responds to demand, and it is the quantity that determines whether a rise in measured biocapacity is a
genuine recovery or a mask over a declining stock.

We formalise this distinction in a minimal deterministic model. Two results are central. First, the
constant-parameter subsystem possesses not a unique interior attractor but a one-parameter family of
equilibria, every interior point of which is monotonically unstable: the onset of collapse is a structural
vicious cycle, with a positive real eigenvalue for every delay and no imaginary-axis crossing (hence no
classical delay-induced Hopf). Second, the balance point and the basin separator coincide in the simple
scalar condition `R_B = 1` (footprint = total biocapacity), while the more commonly monitored flow-yield
ratio `R_A = 1` is only a leading, non-causal indicator — and it fails entirely as a collapse forecaster once
the regeneration lag is too long.

The model is a conceptual/stylised illustration of the accounting logic, not a calibrated forecast; where it
engages the empirical literature it does so only to bound the regeneration lag. It is deliberately minimal
and Allee-free; we discuss the consequences of these choices in §Model scope and §Limitations.

---

## 2. Model formulation

### 2.1 Variables and units

| Symbol | Meaning | Unit | State? |
|--------|---------|------|:------:|
| `A` | productive biocapacity area (the "trees") | ha | yes |
| `P` | human population | cap | yes |
| `D` | accumulated ecological debt (degradation channel) | gha·yr | yes |
| `b` | flow yield per unit area (fruit per tree) | gha·ha⁻¹·yr⁻¹ | derived |
| `b_G` | value of one hectare of standing stock | gha·ha⁻¹ | parameter |
| `G(A)` | regeneration / recruitment rate | ha·yr⁻¹ | no |
| `B` | biocapacity = `bA + b_G G(A)` | gha·yr⁻¹ | no |
| `E` | footprint = `eP` | gha·yr⁻¹ | no |
| `K` | carrying capacity = `B/e` | cap | algebraic, not a state |
| `e` | per-capita footprint | gha·cap⁻¹·yr⁻¹ | param |
| `ρ` | regeneration rate | yr⁻¹ | param |
| `r` | per-capita population growth rate | yr⁻¹ | param |
| `α` | degradation rate | (gha·yr)⁻¹ | param |
| `η` | debt-repayment rate | yr⁻¹ | param |
| `τ_g` | recruitment (regeneration) delay | yr | param |
| `τ_p` | demographic (generation) delay | yr | param |
| `A_max`, `b₀`, `A_ext` | carrying-area ceiling, base yield, extinction floor | ha, gha·ha⁻¹·yr⁻¹, ha | param |
| `T_b` | technology-driven yield step (the yield-enhancing wave `T_b(t)`) | gha·ha⁻¹·yr⁻¹ | param |
| `Δb` | amplitude of the yield wave (asymptotic rise of `T_b`) | gha·ha⁻¹·yr⁻¹ | param |
| `κ` | steepness / rate of the yield wave | yr⁻¹ | param |
| `t_wave` | time of the yield wave's midpoint | yr | param |

Because `A` is in physical hectares it is independent of yield, so `b = B/A` is definable and the
decomposition `B = b·A + b_G·G(A)` is identifiable. (With a stock measured directly in global hectares — as
in the National Footprint Accounts — a hectare already embeds `b`, and the decomposition is not identifiable.)

### 2.2 Governing equations

```
Regeneration:  G(A) = ρ A (1 − A/A_max)                          (1)
Biocapacity:   B    = b A + b_G G(A)                            (2)
Footprint:     E    = e P                                       (3)
Stock:         dA/dt = G(A(t−τ_g)) − [E(t) − σ b A(t)]₊ / b_G   (4)
Population:    dP/dt = r P(t) [1 − P(t) / K(t−τ_p)]              (5)
Carrying cap:  K    = B / e                                     (6)   [algebraic]
Debt:          dD/dt = [E − B]₊ − η D                           (7)
Degradation:   b    = (b₀ + T_b(t)) e^{−α D(t)}                 (8)
Technology:    T_b  = Δb / (1 + e^{−κ(t−t_wave)})               (9)
```

`σ` is the human-available share of the flow (σ = 1 with no reservation; set σ and the population cap so
that `E ≤ σ·B` for a reservation/Half-Earth policy). `[x]₊ = max(x, 0)`.

Equation (4) is the central structural assumption. Demand is met first from the flow yield `bA` (the fruit —
leave the tree); only the shortfall `[E − bA]₊` liquidates the standing stock, at rate `1/b_G`. This is the
deficit mechanism, and it is why biocapacity appears in the stock equation: the two flow accounts are no
longer parallel and unlinked. In the pure-increment limit (`ψ → 0`, equivalently the saw-log form) equation
(4) reduces to the standard gross-depletion harvest equation with harvest coefficient `γ = 1/b_G`.

The model is well posed at the boundary. The original `dP/dt` diverges (`P/K → ∞` as `K → 0`); we impose an
extinction floor `A_ext > 0` so that `K ≥ b·A_ext/e > 0` is bounded and clamp `A ≥ A_ext`, `P ≥ 0`. "Collapse"
is then a well-defined approach to the extinction boundary, not a numerically clamped blow-up (see §Numerics).

The three state variables `A, P, D` live in three distinct "books", and the model is written so these are
never mixed: `A` is the increment book (the standing base, removed only by liquidation); the flow yield `bA`
is the flow-yield book (the fruit, separable from the base); and `D` is the degradation/debt book (the
erosion of the surviving stock's yield). Conservation is a property of the incidence structure (each outflow
is assigned to exactly one donor book) and positivity follows from donor limitation (an outflow vanishes when
its donor compartment is empty). Any parameter pinned at an optimisation bound is reported as a declared fit
defect rather than silently as a calibration.

---

## 3. Assumptions

Each equation carries an explicit modelling choice.

- **(1) Logistic regeneration** — symmetric self-limiting growth; a modelling convenience, not a law. The
  point `A_max/2` is the maximal-growth point, not a threshold.
- **(2) Biocapacity is additive flow + increment** — the flow is separable (crops, orchard), the increment is
  removable-only-by-stock (forest, fish). The composition is captured by the flow share `ψ = bA*/B*`, which is
  the master parameter separating the two ratios `R_A` and `R_B` (§4.5) and locating the masking illusion
  (prediction 5).
- **(3) Per-capita footprint is constant** — `e` (and the per-capita requirement it represents) is held
  constant as a baseline modelling choice, since this is the only way to isolate the stock–flow–demand
  feedbacks; endogenising `e` as a time-varying per-capita requirement is an offered extension. The model
  does not carry a co-evolving per-capita requirement, and this is stated explicitly rather than left
  implicit.
- **(4) Deficit-driven, immediate depletion** — liquidation is immediate; the delayed response is in
  recruitment `τ_g` (a tree takes `τ_g ≈ 20–80 yr` to bear fruit), not in the depletion term.
- **(5) Demographic delay on carrying capacity** — the population responds to the delayed carrying capacity
  `K(t−τ_p)` (the conditions a cohort "knew"), Hutchinson-style.
- **(6) `K` is algebraic, not a state** — a function of the state; the system is genuinely 3-D (`A, P, D`).
- **(7) Debt accrues only in overshoot, repayed at `η`** — `η` is primary (it decides whether an equilibrium
  exists). We set `η = 0.05 yr⁻¹`, a minimal environmental regeneration / degradation-removal rate (slow,
  ≈20-yr timescale); the model is insensitive to `η` over a modest range provided `η > 0`.
- **(8) Degradation erodes the surviving stock's yield** — a separately-evidenced channel (soil fertility,
  over-picking), not double-counting the trees removed by `A`.
- **(9) Technology is bounded** — a logistic wave; saturation is why the masking is transient.

**Delay asymmetry.** Depletion/liquidation is immediate while functional degradation is a separate, slower
state. We justify this asymmetry explicitly and note that a third lag `τ_D` could be added
(`dD/dt = [E(t−τ_D) − B]₊ − ηD`) to keep the delay structure fully consistent. We also declare the aggregation
of the governance clock: `τ_p` lumps several institutional time objects (observation, assessment, review,
decision/deployment, ecological response, memory) and is not a single measured lag.

---

## 4. Analytic results

This section develops the analytic core in two registers that read the same object differently. The dynamical
view (§4.1–§4.4, §Numerics, §Discussion) asks how the system behaves; the observational view (§4.5,
§Predictions, §Discussion) asks what a policy-maker can watch. The thesis that holds them together is stated
in §Presentation and in the abstract: the balance point is `R_B = 1`; `R_A = 1` is a leading but non-causal
signal; and when the regeneration lag is too long neither ratio warns — the lag, not the ratio, is the
controlling variable.

### 4.1 Carrying capacity, MSY, and the emergent ceiling

`K = B/e` is emergent (it moves with `A` and `b`). Because the increment `b_G G(A)` is positive only for
`0 < A < A_max`, the total sustainable-yield curve `B(A) = bA + b_G G(A)` has an interior maximum — the
maximum sustainable yield (MSY): via `dB/dA = b + b_G ρ(1 − 2A/A_max) = 0`,

```
A*  = A_max (b + b_G ρ) / (2 b_G ρ)
B_max = A_max (b + b_G ρ)² / (4 b_G ρ)
```

So the sustainable equilibrium is interior (`A* < A_max`), not `A_max` — a steady harvest of the increment
keeps the stock below its unmanaged maximum. This is the surplus-production / MSY structure of Schaefer
(1954), the same symmetric intrinsic-growth curve that gives `MSY = rK/4`. Only in the flow-only limit
(`b_G G ≪ bA`, the orchard) does the stock tend to `A_max` with a zero harvest drain.

**The interior-MSY statement is regime-conditional.** `A* < A_max` holds only in the increment-dominated
regime, i.e. when `b_G ρ > b` (equivalently `ψ → 0`). When `b_G ρ < b` (the flow-dominated regime, `ψ → 1`)
`B(A)` is monotone increasing on `[0, A_max]` and there is no interior maximum: the sustainable point is the
boundary `A_max`. This is precisely the regime the baseline parameter set sits in
(`b_G ρ = 0.8·0.05 = 0.04 < b = 0.5`), so the baseline sustainable state is the boundary `A_max`. The regime
must be stated before quoting `A*`/`B_max`; they are the increment-only limit, not universal.

**The flow share `ψ = bA*/B*` interpolates between the two limit cases.** Report its regime dependence
explicitly, as it governs which analytic core applies:

- `ψ → 0` (increment-dominated): interior `A*`; the stability classification of §4.3 applies.
- `ψ → 1` (flow-dominated, the orchard limit): `A_max` at sustainability, a liquidation mask, and the vicious
  cycle — the `a₁₁ = ρ(1−2A*/A_max) + b/b_G` liquidation feedback.
- `0 < ψ < 1`: interior `A*` and liquidation feedback coexist. This is the general object, and the
  increasing-harvest and orchard models are recovered as limits.
- `γ = 1/b_G = 1/V`, the orchard's salvage value (`V` = standing biomass ÷ annual production, ≈ 20–100 yr).
  The increment-harvest coefficient is therefore measurable and is not a free parameter.
- `ψ` is a testable prediction (prediction 5). Small `ψ` (flow yield is a small share, cropland/grazing)
  puts the model near the increment limit, where a smooth decline is stabilised by demographic feedback and
  the illusion is small. Large `ψ` (forest/fishery) makes the overshoot invisible until demand exceeds the
  flow yield, then liquidation with a threshold `A_c(E)`. The model therefore predicts the masking illusion
  is more visible in flow-dominated (high-`ψ`) systems than in increment-dominated (low-`ψ`) ones.

**Regime → outcome.** The single testable condition `b_G ρ ⋚ b` (equivalently `ψ ⋚ 1/2`) decides everything
downstream:

| Regime | Condition | `B(A)` shape | Sustainable point | MSY | Collapse/mask behaviour |
|---|---|:--:|---|---|---|
| increment-dominated | `b_G ρ > b` (`ψ → 0`) | interior maximum | interior `A* < A_max` | interior MSY `A*`, `B_max` | smooth decline stabilised by demographic feedback — illusion small |
| flow-dominated (baseline) | `b_G ρ < b` (`ψ → 1`) | monotone ↑ | boundary `A_max` | none interior (max at `A_max`) | liquidation with threshold `A_c(E)`; overshoot invisible until demand exceeds flow yield — illusion more visible |
| marginal | `b_G ρ = b` | max at the boundary | `A* = A_max` (interior max merges with boundary) | boundary `A_max` | `ψ → 1` |

A parameter sitting exactly on the `b_G ρ = b` boundary is a non-generic choice and should be stated and
perturbed off.

### 4.2 Fixed-liability threshold and the saddle-node = MSY

For a fixed liability `E`, the deficit-region equation `dA/dt = 0` is a quadratic in `A` with an unstable
root (the separatrix), and the saddle-node is exactly the MSY:

```
A_c(E) = [ (b_G ρ + b) − √((b_G ρ + b)² − 4 b_G ρ E/A_max) ] A_max / (2 b_G ρ)
E_sn   = B_max = A_max (b + b_G ρ)² / (4 b_G ρ)            (safe basin vanishes at MSY)
```

A fixed liability above `B_max` cannot be sustained by harvesting regrowth. The threshold is emergent and
`E`-dependent (no Allee term needed), located at `A_c(E)`, never at `A_max/2`. When realised, the fold is a
saddle-node (fold) bifurcation — the safe basin vanishes as `E` crosses `B_max`, the catastrophic-shift /
critical-transition structure of alternative-stable-state ecology (Scheffer, Carpenter, Foley, Folke &
Walker 2001): a loss of resilience precedes the switch, and the switch is abrupt and hard to reverse, not
because of an imposed Allee minimum but because the stable and unstable equilibria first meet at the fold
and then destroy each other.

**The fold is regime-scoped.** It is realised only in the increment-dominated regime (`b_G ρ > b`), where
`B(A)` has an interior maximum. There `dB/dA = 0` exactly at the interior MSY, and for `E` just below
`B_max` there are two fixed points — one unstable (`B'(A) > 0`) and one stable (`B'(A) < 0`) — that merge at
the saddle-node (verified numerically: `B'(A*) = 0`; two roots with opposite-sign `B'` for `E < B_max`). At
baseline (`b_G ρ = 0.04 < b = 0.5`), `B(A)` is monotone increasing on `[0, A_max]` with `B'(A) > 0`
everywhere, so no interior fold is realised: the fixed-liability equilibria are single-valued and unstable,
and the stable object is the boundary `A_max`.

**The fold must not be conflated with the `τ_g` cliff.** As we show in §Numerics and §Discussion, the `τ_g`
transition is a basin-boundary crisis, not a fold: the leading eigenvalue is constant and positive
(`Re λ ≈ +0.62`) for every `τ_g`, so no eigenvalue crosses zero as `τ_g → 20` and there is no
critical-slowing-down / early-warning precursor (the `P`-relaxation return time is flat ≈150 yr for
`τ_g = 0–18`, then the attractor vanishes abruptly rather than slowing). Scheffer's "loss of resilience
precedes the switch" therefore describes only an increment-dominated `E`-fold; it is the wrong description of
the delay transition. The two must be told apart (§Discussion).

### 4.3 Stability; the vicious cycle; the stability classification

**The deficit = stock-decline identity.** When demand exceeds the flow yield (`E > bA`), Eq. (4) reduces
exactly:

```
dA/dt = G(A(t−τ_g)) − [E − bA]₊/b_G  =  (B̃ − E)/b_G
```

because `[E − bA]₊ = E − bA` there, and the lag-adjusted biocapacity is
`B̃ = bA + b_G G(A(t−τ_g))` (so `B̃ = B` only when regeneration is evaluated at the delayed state). This is
the algebraic identity that makes "deficit-driven" rigorous: the shortfall between biocapacity and footprint,
not the gross harvest, drives stock decline, and the model's stock build-up exactly cancels against its flow
term. Corollary (in the `R_B` form of §4.5): `dA/dt < 0 ⟺ E > B̃`, and at equilibrium `E = B̃`, so `R_B =
E/B̃ = 1` at the balance point. The `R_B = 1` locus of §4.5 is exactly the neutral continuum on which the
characteristic equation has `D(0) = 0` (§Numerics) — the separator and the continuum are one and the same
object, seen from the ratio (monitoring) and spectral (dynamical) views.

Linearising (4)+(5) in the deficit region gives (at the interior point)

```
a₁₁ = ρ(1 − 2A*/A_max) + b/b_G      ;  a₁₂ = −e/b_G      ;  a₂₂ = −r
det = r·ρ·A*/A_max > 0  (never a saddle)   →   zero-delay condition is  a₁₁ < r  (NOT a₁₁ < 0)
```

- **The vicious cycle is real and quantitative.** `a₁₁` gains the `+b/b_G` term. For liabilities that scale
  with the stock (`E = f·bA`) the interior point is `A* = A_max[1 − (f−1)b/(b_G ρ)]`, and it is self-sustaining
  (the environment's own mode goes locally runaway, `a₁₁ > 0`) precisely when `(2f−1)ν > 1`, where
  `ν = b/(b_G ρ)`. With `b_G` the standing-stock value (20–100 yr) and realistic `ρ ≈ 0.02–0.1 yr⁻¹`, `ν` is
  `O(0.1–2)`; treat `(2f−1)ν > 1` only as an estimated indicator, not a measured threshold, because `f` and
  the liability elasticity are set by the model. The "vicious cycle" therefore describes Eq. (4) and not a
  gross-depletion form.
- **Stability classification (sign-corrected).** For `ρ ≫ r`, the 2-D two-delay system reduces to a scalar
  two-gain delayed logistic with control `χ = q/(ρ − 2q)`, `q = γ e b₀/r_opt` (depletion pressure):
  - `χ > 1` (`Λ > 0`) ⇒ `τ_g`-only Hopf: `ω = r√(χ²−1)`, `τ_g* = arccos(−1/χ)/ω`.
  - `χ < 1` (`Λ < 0`) ⇒ `τ_p`-only Hopf: `ω = r√(1−χ²)`, `τ_p* = arccos(−χ)/ω`.
  - `χ = 1` (`Λ = 0`, i.e. `ρ = 3q`) ⇒ neither; two-delay boundary `s = π/ω`, `ω = 2r·cos(ωd/2)` ⇒
    `s ≈ π/(2r) = 78.5 yr` at `d → 0`.
  - The sign structure is exact (from the `|Q| = |P|` elimination); only `ω*, τ*` are `O(r/ρ)` approximate,
    and the fast–slow reduction is valid only while `a₁₁ ≤ 0` (else use the full 2-D transcendental equation,
    where the `A`-mode can itself oscillate).
  - On the constant-parameter S0 of the present model this Hopf classification is not realised: the exact
    `[·]₊` gives a monotone positive-real eigenvalue with no imaginary-axis crossing for every delay
    (§Numerics). The classification above describes the fast–slow reduction and does not predict the actual
    (structural) instability.
  - **Baseline sits at a knife-edge.** Baseline `χ = 1` because `ρ = 3q`, i.e. `Λ = 0`, the measure-zero
    surface where the two gain surfaces `r²a₁₁² = (γ e a₂₁)²` are equal (`g_M = g_P`). This is a non-generic,
    unexplained parameter choice, and it is precisely why "no single delay destabilises" holds at baseline.
    We do not justify it; we report instead the generic result that follows from the sign of `Λ`: perturbing
    off the knife-edge gives exactly one lag destabilising — `τ_g`-only if `χ > 1` (`Λ > 0`), `τ_p`-only if
    `χ < 1` (`Λ < 0`). Any scan range and any "no single delay destabilises" claim must be stated as a
    function of `Λ`/`χ`, never as a parameter-free statement (§Numerics).

### 4.4 The complete dimensionless group set

`χ = q/(ρ−2q)` is the cleanest single control (it matches the scalar two-gain picture), but the paper carries
the complete non-dimensionalization as the full generality statement: `t̂ = rt`, `a = A/A_max`,
`p = P·r_opt/(b₀A_max)`, and the groups `s = ρ/r`, `g = γ b₀ f/ρ`, `f = e/r_opt`, `θ`, plus scaled delays
`τ̂_M = rτ_g`, `τ̂_P = rτ_p`. We present both: `χ` for the clean stability-sign rule, and the six-group set
for full generality — they are complementary, not competing.

### 4.5 Macro-ratio safe operating space (`R_B` vs `R_A`)

In addition to the dimensionless groups, the bookkeeping can be reported as two observable ratios that
summarise the safe-operating picture. Define the biocapacity ratio and the flow-yield ratio:

```
R_B = E / B            (footprint ÷ total biocapacity)
R_A = E / (b A)        (footprint ÷ flow yield)
ψ   = bA / B           (flow share, 0 ≤ ψ ≤ 1)
R_A = R_B / ψ
```

**The operating boundary is `R_B = 1`, and it is exactly the neutral equilibrium family of §4.3
`P = B(A)/e`.** From the deficit identity `dA/dt = (B̃ − E)/b_G` (§4.3), `dA/dt < 0 ⟺ E > B̃`, so the stock
declines iff footprint exceeds total biocapacity. At equilibrium `E = B̃` so `R_B = 1`; this is
simultaneously the bookkeeping trigger, the macro-ratio safe-operating boundary, and (as the family
`P = B(A)/e`) the basin separator. Verified onset (baseline S0, documented `A₀` grid): the recover/collapse
boundary is crossed at `R_B = 1.000` for every `A₀ ∈ {0.30,…,1.05}`, while the flow-yield ratio there is
`R_A = 1.01–1.06`.

**`R_A = 1` is necessary but not sufficient.** `R_A = 1` means `E = bA`, i.e. demand equals the flow only. A
system sitting between `R_A = 1` and `R_B = 1` still regenerates (`dA/dt > 0`), because the increment
`b_G G(A)` is untouched. `R_A > 1` is therefore not the collapse trigger, and the two ratios are not
interchangeable: `R_A` is a leading, non-causal signal; `R_B` is the trigger.

**The gap between them is the flow share, which is the master parameter.** `R_A = R_B/ψ`, so the two ratios
coincide in the flow-dominated limit (`ψ → 1`, baseline) and separate as `ψ → 0` (increment-dominated).
Regime-scoped closed form (at a sustainable interior MSY): `ψ* = 2/(1 + b_Gρ/b)`, `R_A^eq = (1 + b_Gρ/b)/2`.
Verified across regimes: `b_Gρ/b = 0.05` (flow-dominated, no interior MSY, `ψ → 1`, `R_A = 1`); `2.0 →
ψ* = 0.667, R_A^eq = 1.50`; `37.5 → ψ* = 0.052, R_A^eq = 19.25`; `150 → ψ* = 0.013, R_A^eq = 75.5`. The
single regime index `b_Gρ/b` therefore governs the gap between `R_A` and `R_B` (`ψ* = 1/R_A^eq =
2/(1 + b_Gρ/b)`).

**A sustainable system can run at `R_A > 1`.** In the increment-dominated regime the balance point is
`R_B = 1` with `R_A > 1` (footprint > flow yield, the buffer intact). `R_A > 1` is not a warning; the balance
point is `R_B = 1` in every regime.

**Temporal-lead nuance.** Because `R_A = R_B/ψ`, `R_A` crosses 1 earlier than `R_B` by the factor `1/ψ`, but
its lead is ≈0 in flow-dominated systems and grows only with increment-dominance. A large lead is therefore a
signature of the increment-dominated regime, not a general warning property.

**Fold ↔ `R_B = 1` (regime-scoped).** The §4.2 fixed-liability fold threshold `E_sn = B_max =
A_max(b+b_Gρ)²/(4b_Gρ)` is precisely the `R_B = 1` boundary evaluated at `(A*, E = B_max)`. Verified
(increment-dominated `b = 0.02`): interior MSY `A* = A_max(b+b_Gρ)/(2b_Gρ) = 0.900`, `B(A*) = B_max = 0.0270`,
`E_sn = 0.0270`, so `R_B = E_sn/B_max = 1.000` exactly — the fold and the balance point are the same object.
This fold is realised only when `b_Gρ > b`, the identical scoping as the §4.1 regime table and §4.2; at
baseline it is absent.

**The separator degrades with the lag — two sides of one coin.** At short/no delay the neutral family
`P = B(A)/e` (i.e. `R_B = 1`) separates recover from collapse at balanced accuracy 99.2 % (no-delay) →
81.2 % (`τ_g = 30`); a linear functional is chance at `τ_g = 30` (balanced 50.0 %, raw 94.7 % = the
majority-collapse class, a class-imbalance artefact). So `R_B = 1` is necessary for recovery but not
sufficient once the lag is too long — the operating boundary (here) and the basin crisis (§Numerics,
§Discussion) are complementary statements about one object. The family `P = B(A)/e` is the separator, not a
"first integral".

**One object, many faces.** The single scalar `R_B = 1` is simultaneously the bookkeeping trigger
(`dA/dt < 0 ⟺ E > B̃`, §2.2, §4.3); the basin separator `P = B(A)/e` (§4.3, §Numerics — the neutral
continuum); the interior-MSY fold threshold of §4.2, only when `b_Gρ > b` (absent at baseline); the target of
prediction 8 (§Predictions); and the object whose long-`τ_g` failure produces the silent-collapse and
measure-zero-rescue negative results of §Discussion. No new parameter appears; each face is the same
statement "`E = B`" in a different coordinate.

**Figures (observational view).** `scans/topdown_macro_ratios.png` — the macro-ratio plane (`R_B` vs `R_A`,
two panels `τ_g=10` and 30), showing the `R_B=1` boundary as both the basin separator (recover/collapse) and
the safe-operating boundary, with the `R_A>1` buffer. `scans/topdown_ratio_separation.png` — the ψ-regime
closed form `R_A^eq=(1+b_Gρ/b)/2` (and `ψ*=2/(1+b_Gρ/b)`), i.e. how far the leading indicator `R_A` sits
above the trigger `R_B` as the regime index `b_Gρ/b` grows. (The `τ_g` cliff and full-plane no-Hopf belong to
the dynamical view and are in §Numerics.)

---

## 5. Results: principal claims

The results established by the analysis are the following; each is grounded in §4, §Numerics, and §Discussion.

- **The constant-parameter subsystem is monotonically unstable, not Hopf-driven.** It has a positive real
  eigenvalue (≈ +0.62) for every delay, with no imaginary-axis crossing; and `D(0)=0` on the whole equilibrium
  family `P=B(A)/e`, so there is no isolated interior attractor to frame a delay-ratio Hopf. This contrasts
  with the classical delayed-logistic Hopf of Hutchinson-type single- and two-delay models, in which a delay
  ratio produces an oscillatory onset; here the onset is a structural vicious cycle. (The
  `78.5 yr = π/(2r)` coincidence is a two-loop coincidence, not the Hutchinson `π/(2r)` demographic threshold.)
- **The productivity illusion is real but conditional and narrow.** A genuine `B`-rising-while-`A`-falls window
  exists only for a small initial deficit (≈5.4 yr at `E−b₀A₀=0.06`, collapsing to zero at deficit ≈0.075;
  converged RK4 — see §Demonstration). It is narrow, deficit-bounded, and transient, with a computable
  `t_peak` and a critical deficit.
- **Technology can increase cumulative debt.** Under overshoot, yield technology raises `K`, `P` and `E`, and
  can increase cumulative debt — a Jevons-type rebound.
- **The true threshold is emergent.** There is no threshold at `A_max/2`. The real threshold is emergent:
  `A_c(E)` (fixed liability) or the MSY `B_max`; `A_max/2` is only the maximal-regeneration point.
- **The full overshoot model has an equilibrium only because of `η`.**
- **The full system is three delayed states (`A,P,D`); only the `α=0` subsystem is 2-D; `K` is algebraic.**
- **The operating (decline) trigger is `R_B = 1` (footprint = total biocapacity), not `R_A = 1`.** `dA/dt < 0
  ⟺ E > B̃`; `E > bA` (`R_A = 1`) is necessary-but-not-sufficient. A system can sit on the collapse side with
  `R_A > 1` (increment-dominated) or, at long `τ_g`, with both ratios below 1 (silent collapse, §Discussion).
- **The debt-compounding asymmetry is a theorem under multiplicative degradation.** Under
  `b = (b₀+T_b)e^{−αD}`, "debt compounds without bound while technology saturates" follows from the model; it
  is false under an additive form.

**Scenario B/C is the inverse of the orchard framing.** In Scenarios B and C the environmental stock `A`
rebounds to ≈`A_max` (≈1.19) while population `P` and the harvest/biocapacity `B` collapse — an "environment
recovers, humans collapse" outcome that is the opposite of the orchard framing ("humans die, orchard
survives"). This is a scenario outcome, not a claim to be over-claimed.

---

## 6. Falsifiable predictions

These are the testable content of the model. They fall into two registers: predictions 1–3, 6 and 7 are
dynamical (stability, onset, recovery dynamics); prediction 5 straddles the two views (the ψ-mediated mask,
§4.5); and prediction 8 is the observational one (the ratio safe-operating space and whether a monitor can
forecast collapse, §4.5).

1. **Which lag destabilises** is set by the sign of `Λ`/`χ`: on the constant-parameter subsystem the interior
   point is monotonically unstable for every delay (positive real eigenvalue, no imaginary-axis crossing),
   so the "which-lag" question has no Hopf answer there.
2. The **oscillation period near onset ≈ 4× the dominant lag** — applies only on a Hopf boundary; the
   constant-parameter subsystem has no oscillatory onset (monotone collapse), though the full model (with
   `η`, `D`) can still show damped oscillatory transients.
3. The productivity illusion has a **computable peak-biocapacity time `t_peak`** with the signature "`B`
   rising while `A` falls".
4. **Reducing a policy lag `τ_e` matters comparably to reducing the overshoot `f`** — a testable,
   policy-relevant ranking.
5. **The flow-share `ψ` locates the masking illusion** (§4.1, §4.5): the "`B` rises while `A` falls" window
   should be more visible in flow-dominated (high-`ψ`, `b_Gρ < b`) systems than in increment-dominated
   (low-`ψ`, `b_Gρ > b`) ones.
6. **The regeneration lag `τ_g` sets recovery vs collapse** (§Numerics): the recover fraction collapses from
   ≈40 % to ≈5 % across a steep **18–20 yr band**, so the model predicts the collapse outcome whenever the
   field-supported regeneration lag exceeds ≈20 yr (forests, soils, many fisheries) and recovery only for
   `τ_g ≲ 18`. This is the necessary-but-not-sufficient reading of §4.5: `R_B = 1` is necessary but not
   sufficient once `τ_g` is long. It is a quantitative, direct prediction tied to the empirical `τ_g` band.
7. **Regeneration *rate* vs *lag* are two decoupled levers** (§Discussion): time-to-50 % scales ≈ inversely
   with the regeneration rate `ρ`, but whether the stock recovers at all is set by the regeneration lag
   `τ_g`. A system with a long `τ_g` cannot be rescued by raising `ρ` alone.
8. **The operating boundary is `R_B = 1` (footprint = total biocapacity), not `R_A = 1` (§4.5).** `R_A`
   crosses 1 earlier than `R_B` (by `1/ψ`) but is not the collapse trigger, and its lead is ≈0 in
   flow-dominated systems. A system can be on the collapse side while `R_A > 1` (increment-dominated) — and,
   in the long-`τ_g` regime, even while `R_B < 1` (silent collapse, §Discussion). Falsifiable: monitor the two
   ratios and confirm the trigger is `R_B = 1`, not the earlier-crossing `R_A`.

**The two masks.** *Technology mask:* `B` rises while `A` falls (requires progress). *Liquidation mask:*
`E` steady while `A` falls (requires none). The discriminating observable is exactly which holds.

**Why the illusion is necessarily transient.** From `B = bA` (flow component) the growth rate of biocapacity
is `d ln B/dt = d ln b/dt + d ln A/dt`. Under the mask window `A` falls, so the second term is negative; the
first term is bounded because technology saturates (`T_b` is a logistic wave, so `d ln b/dt ≤ 0` eventually).
The sign of `d ln B/dt` is therefore pinned by the unboundedly negative `d ln A/dt` under the
stock-liquidation cycle, so a `B`-rising-while-`A`-falls window cannot persist: the yield gain from a bounded
technology wave is finite, whereas the stock decline it is meant to offset is unbounded once liquidation takes
over. This is the analytic reason the mask is narrow and deficit-bounded (§Demonstration), and why the
"productivity illusion reads as if sustainability were improving" is a transient, recover-to-reckoning signal
rather than a new equilibrium.

---

## 7. Presentation

- **Thesis (stated once here and in §4):** the balance point is `R_B = 1` (footprint = total biocapacity);
  the flow-yield ratio `R_A = 1` is a leading but non-causal signal; and when the regeneration lag is too
  long neither ratio warns — the lag, not the ratio, is the controlling variable.
- **Feedback diagram with a switch** (fruit harvest vs. capital liquidation): `A →^{b} B → K → P → E`, with
  `E − bA` deciding the switch, `D →^{α} b`, and an exogenous bounded `T_b`. Two positive-feedback loops
  compound: Loop 1 (stock-liquidation: `A↓ → B↓ → deficit↑ → liquidation↑ → A↓`) and Loop 2 (debt-erosion:
  `D↑ → b↓ → B↓ → deficit↑ → D↑`). Rendered: `scans/feedback_diagram.png`.
- **Thought-experiment label.** The orchard/hens framing is a *Gedankenexperiment* (the best available
  intuition); the flow/increment decomposition is its measurable representation. The model is a stylised
  illustration of the accounting logic, so the orchard metaphor must not be mistaken for an empirical claim.
- **Non-smoothness and one-sided stability.** At the switch `E = bA` the exact `[·]₊` is non-smooth, so the
  sustainable point is a boundary of the deficit regime, not an interior point. Report one-sided stability
  (linearise from the deficit side only). Because the exact switch yields no imaginary-axis crossing
  (§Numerics), the non-smoothness does not create spurious oscillations.
- **Parameter justification.** The representative values are illustrative and must be caveated: `ρ` is large
  in the original scale, and `γ`, `α`, `τ` are lumped/effective parameters, not independently measured.
- **Limitations of National Footprint Accounts.** The accounts are account-based (measured yields and
  conversion factors) and do not capture soil erosion, deforestation, or groundwater depletion, so estimated
  biocapacity likely overstates and the Footprint likely understates real overshoot (§Model scope).
- **Units.** Symbols and units are given for `A_max`, `b₀`, `Δb`, and every other symbol in the symbol table
  (§2.1); no dimensionless parameter is left without its stated unit.

**Related literature.** The delayed-logistic *stability* result is Hutchinson (1948), the classical
single-delay logistic with its `π/(2r)` demographic threshold. Haberl & Aubauer (1992) *apply* this
delayed-logistic framework to human population/load dynamics; their contribution is the application, not the
introduction of the time delay into population dynamics, which is Hutchinson. Brander & Taylor (1998) is a
distinct Ricardo–Malthus renewable-resource model. The surplus-production/MSY curve used here is Schaefer
(1954), and the fold/saddle-node with a vanishing safe basin is the catastrophic-shift structure of Scheffer
et al. (2001); the empirical regeneration-lag band follows Poorter et al. (2016), Poeplau et al. (2011),
Hutchings & Reynolds (2004), and Neubauer et al. (2013). On the data side, the National Footprint Accounts are
documented in Wackernagel & Rees (1996), Wackernagel et al. (2002), Borucke et al. (2013), and Lin et al.
(2018). These accounts are not uncriticised: Blomqvist et al. (2013), Giampietro & Saltelli (2014), and van
den Bergh & Grazi (2015) raise substantive methodological objections, and the Global Footprint Network-side
rejoinders appear in Galli et al. (2016). These attribution statements are given so the reader is not misled
about what each source establishes.

---

## 8. Numerics, verification, and well-posedness

- **Solver.** Method-of-steps with RK4 (or `dde23`/`pydelay`; Shampine & Thompson 2001), the exact `[·]₊`
  switch as the model states it (never a smooth ramp, because a softplus ramp leaks depletion when `E < bA`),
  clamping `A ≥ A_ext > 0`, `P ≥ 0`, `K ≥ K_min`, and an explicit extinction floor (so "collapse" is a model
  result, not a clamp). Where a smooth variant of the `[·]₊` switch is used (reference implementation only),
  fix its width `w` and report insensitivity to it. Full-`(7)` runs use `η = 0.05 yr⁻¹`; the constant-
  parameter subsystem S0 drops `D` and `η`, so `η` does not enter it.
- **Protocol and convergence.** State `dt`, history functions, and the `Δt`-convergence table (e.g. scenario A
  `A*`: 0.8022 at `dt=0.5` vs. 0.8021 at `dt=0.05`). Each reported number carries its protocol.
- **Method sensitivity and numerical checks.** The final yield `b_final = 0.317` gives `D ≈ 6.76`. The
  endpoint `D_E` is method-dependent (5.26 / 6.74 / 18.70 for the frozen/crashed/un-clamped endings), so it
  must be reported with its termination convention. The leading Hopf delays are `τ_g* = 85.4 yr` and
  `τ_p* ≈ 231 yr`.
- **Measured basin shrinkage.** The qualitative "basin of attraction shrinks" is quantified. The stable
  fraction of the `(A₀,P₀)` initial-condition plane for the overshoot subsystem falls from 0.506 (no delays)
  to 0.042 (baseline `(τ_g,τ_p)=(30,25)`), and the standard IC `(1.0,0.1)` flips from stable to collapse.
  Report the stable fraction as a function of `(τ_g,τ_p)`; complement it with the closed-form separatrix
  criterion `A_c(E)` (§4.2) — the measured fraction is the empirical witness, `A_c(E)` the analytic boundary.
- **Contrast with the gross-harvest formulation.** The deficit-driven model (Eq. 4) is structurally distinct
  from the standard gross-harvest (surplus-production) formulation in which total demand is removed directly
  from the stock. The gross-harvest subsystem has a unique interior attractor; the deficit-driven subsystem
  instead has a one-sided boundary at `A → A_max, P → b₀A_max/e` and no robust interior attractor, so any
  population overshoot into `E > bA` triggers the vicious-cycle collapse (`A → A_ext`). This is the
  mechanistic reason the two formulations differ (see §Comparison of formulations).
- **Basin recompute (constant-parameter subsystem).** On the documented `A₀×P₀` grid (13×16 = 208; `P`
  straddling `B* = b₀A_max/e ≈ 1.09`), the recover fraction falls from 39.9 % (no delay) to 5.3 % (baseline
  `(30,25)`); the collapse fraction rises 60.1 % → 94.7 %. The regeneration delay triggers an `A_max`-overshoot
  → `E>bA` → liquidation collapse, and the recover basin vanishes abruptly as `τ_g` crosses ~20 yr. A
  time-domain illustration (`scans/r1_recovery_vs_collapse.png`) shows the same IC `(A₀,P₀)=(1.0,0.1)`
  recovering (`A→A_max`, `τ_g=10`) versus collapsing (`A→A_ext`, overshoot `A→1.36`, `τ_g=30`); a
  recovery-side figure (`scans/eco_recovery_insight.png`) shows the density-dependent, sigmoidal recovery
  trajectory and the decoupling of regeneration rate (sets recovery time) from regeneration lag (sets recovery
  outcome).
- **Scenario-D threshold is near-critical, not a clean result.** `(20,20)` gives min `A = 0.631` and recovers,
  while `(30,25)` gives min `A < 0.6` and collapses (`0.6 = A_max/2`, the maximal-regeneration point, not a
  threshold). State the actual basin boundary, not a single point.
- **Reporting rigour.** (i) State the grid range of the stability scan and normalise "barely positive" `Re λ`
  by `r` (a margin of `< 0.01 yr⁻¹` is not small next to `r = 0.02`). A scan over `τ ∈ [0,80] yr` cannot
  rule out a single-delay Hopf, because the competing demographic-delay Hopf appears only at large
  `τ_P ≈ 225 yr` (slow `ω ≈ 0.011 yr⁻¹`) once parameters are perturbed off the knife-edge. State the location
  of any "no single delay destabilises" claim as a function of `Λ`/`χ`, and ensure any such scan extends to
  `τ_P ≳ 250 yr` before concluding. (ii) State whether interpolation occurs for the `τ_g/τ_p` (both exact
  multiples of `Δt`), or use a non-multiple step. (iii) Complete the scenario/parameter table (which `e`,
  which lags, whether `T_b` is active). (iv) Analyse the trivial equilibrium `(A,P)=(0,0)` and the no-recovery
  region. (v) Reconcile the "max Ω not reported" footnote (Ω peaks at ≈5.0 on `D`, ≈4.1 on `E`, clipped at 8.5).
- **Characteristic equation, crossing curves, and full spectrum.** We apply the exact crossing-curve formalism
  (Hale & Huang 1993; Gu, Niculescu & Chen 2005) and a full-spectrum computation to the constant-parameter
  subsystem. Linearising about an interior point `A*` of the equilibrium family `P=B(A)/e` gives
  `D(s;τ_g,τ_p)=(s−a₁e^{−sτ_g}−a₃)(s+r)−a_E a₄e^{−sτ_p}=0`, which has a zero eigenvalue `D(0)=0` on the whole
  family (a neutral continuum — no isolated interior attractor) and a positive real leading eigenvalue
  (`Re λ ≈ +0.62` at `A*=0.8`) for all delays. Scanning `s=iω` yields no imaginary-axis crossing, and the
  zero-delay `a₁₁<r` condition is violated everywhere (`a₁₁=G'(A*)+b/b_G ≥ 0.57 > r`). The `χ` two-gain Hopf
  classification (derived for the interior attractor of the gross-harvest formulation) does not transfer; the
  crossing-curve method should be applied to the boundary equilibrium, not an interior point
  (`scans/r2_char_spectrum.png`, `scans/r2_a11_vs_delay.png`).
**Comparison of formulations.** Two distinct formulations are frequently conflated in the surplus-production /
sustainability literature, and they differ qualitatively. In the **gross-harvest** (Schaefer-type)
formulation, total demand is removed directly from the stock; its constant-parameter subsystem has a unique
interior attractor, can be stable for a single delay, and can exhibit a two-delay Hopf (`χ=1`,
`τ_g*≈85`, `τ_P*≈225`, `s=π/ω`). In the **deficit-driven** formulation of Eq. (4), only the shortfall above
the flow yield liquidates stock; its constant-parameter subsystem has a one-parameter equilibrium family
`P = B(A)/e` (no isolated interior attractor), a monotone positive-real eigenvalue (≈ +0.62) for every delay,
no imaginary-axis crossing, and a recover/collapse basin dichotomy. The two are compared directly:

| | Gross-harvest (surplus-production) formulation | Deficit-driven formulation (Eq. 4) |
|---|---|---|
| Equilibrium | unique interior attractor | one-parameter family `P = B(A)/e` (no isolated attractor) |
| Linearisation | interior point; `a₁₁ < r` can hold | interior point: `a₁₁ = G'(A*) + b/b_G > r` everywhere |
| Stability | stable for a single delay | monotone positive-real eigenvalue (≈ +0.62) for every delay |
| Hopf / onset | two-delay Hopf: `χ=1`, `τ_g*≈85`, `τ_P*≈225`, `s=π/ω` | none: `D(0)=0` (neutral continuum); no imaginary-axis crossing |
| Classification | `χ` two-gain Hopf (which-lag) | structural vicious cycle, no `χ`; crossing-curve → boundary eq. |
| Basin | stable fraction 0.506 → 0.042 | recover/collapse dichotomy 39.9 % → 5.3 % |

**The "balanced-with-lags" case.** In the gross-harvest formulation the balanced case (`e = r_opt`) with lags
oscillates (the χ=1 Hopf, `τ_g* ≈ 85 yr`) rather than collapsing. On the deficit-driven subsystem the
balanced case still lies on the continuum and its interior points are monotonically unstable, so the "no
collapse at balance but oscillation with lags" dichotomy does not apply. A full-`(7)` recompute is required
before asserting either outcome.

**Empirical grounding of `τ_g` and the delay-response sweep.**

- **Operational definition.** `τ_g` is the regeneration/recruitment-response lag — the delay between a change
  in the environment state `A` and the regeneration/recruitment response that rebuilds carrying capacity
  (`A(t − τ_g)`). In the model's framing, "a tree takes `τ_g ≈ 20–80 yr` to bear fruit." Concretely: the time
  from environmental change until the regeneration/recruitment response begins to restore carrying capacity,
  approximated by the time to reach ≈50 % of pre-disturbance productive capacity. The ≈50 % threshold excludes
  the early "green shoots" transient and matches the time to meaningful biomass/stock recovery in the cited
  field studies (forest AGB ≈50 % at ≈20 yr; soil SOC at a new equilibrium ≈20–23 yr). It is a conservative
  definitional threshold, not a fitted value; the collapse cliff sits at `τ_g ≳ 20 yr` either way.
- **Field-derived band (literature banding, cited; not a full digitisation).** Forests: AGB recovery is
  substantial by 20 yr (≈50 %), median ≈66 yr to 90 % of old-growth (Poorter et al. 2016). Soils: SOC build-up
  begins ~5 yr and reaches a new equilibrium ~20–23 yr (Poeplau et al. 2011; IPCC 2006). Fisheries: rebuilding
  is slow and often incomplete — median ~12–13 yr to 50 %, 10 → >100 yr, many collapsed stocks never rebuild
  (Hutchings & Reynolds 2004; Neubauer et al. 2013). Core band ≈ 10–40 yr; extended ≈ 5–60 yr; baseline
  `τ_g = 30` sits inside the band.
- **Delay-response sweep (baseline `τ_p=25`).** The monotone structural instability (no Hopf, `Re λ ≈ +0.62`)
  holds for every `τ_g`; the collapse basin is robust (≈5 %) across the whole field-supported band. A 1-yr-step
  fine sweep over `τ_g ∈ [15,25]` resolves the transition: the recover fraction descends within a narrow band
  — 0.399 (`τ_g ≲ 17`), 0.394 (18), 0.240 (19), 0.053 (`τ_g ≳ 20`) — so the "cliff" is a steep transition band
  ≈18–20 yr (half-way ≈0.24 at `τ_g = 19`), not a single hard edge.

  | `τ_g` (yr) | 0–17 | 18 | 19 | 20–60 |
  |:--|:--:|:--:|:--:|:--:|
  | leading Re λ | 0.608–0.625 | 0.625 | 0.625 | 0.625 (constant) |
  | recover fraction | 0.399 | 0.394 | 0.240 | 0.0529 |

  The collapse result holds for `τ_g ≳ 20` — the range the field data support for forests, soils, and many
  (non-recovered) fisheries — while the fast-regeneration regime (`τ_g ≲ 18`) returns the recovery outcome.
  It is not merely a one-time basin loss: §Discussion shows the recovery is not self-sustaining either. State
  the interval scoped, never as a flat "10–40 yr": the relevant range for the collapse mechanism is
  `τ_g ≳ 20 yr`. The field-supported band lies entirely in the collapse regime for the baseline parameter set.
- **`τ_p` handling and robustness.** `τ_p` is held at 25 yr for the sweep; the `(τ_g, τ_p)` grid spans
  `τ_g ∈ {10,15,18,19,20,30}` × `τ_p ∈ {10,20,25,30,40}`. The cliff is governed by `τ_g`: the recover fraction
  is 0.399 at `τ_g = 10–15` and 0.053 at `τ_g = 30` for every `τ_p`, and at the transition the intermediate
  values move only slightly with `τ_p` (0.399–0.394 at `τ_g=18`; 0.245–0.269 at `τ_g=19`; 0.053–0.058 at
  `τ_g=20`). So `τ_p` shifts the band by <1 yr across a 4× range (10–40 yr) — the cliff is not a `τ_p`
  artefact. A full two-delay sweep is left to future work, but the coarse grid is no longer the only support:
  the flatness holds out to `τ_p = 10` and `40`.
- **The cliff is `τ_p`-independent across the whole tested set, and there is no Hopf anywhere in the delay
  plane.** Extending the sweep to `τ_p ∈ {0,5,10,15,20,25,40,60}` with `τ_g` at 1-yr resolution: the last
  recovering `τ_g` is 18 for every `τ_p` (no dimensionless `τ_g/τ_p` tuning rescues the cliff), and a full
  `(τ_g, τ_p)`-plane scan of the characteristic roots finds zero imaginary-axis crossings with
  `Re λ ≈ +0.625` constant (`scans/topdown_delay_boundary.png`). The "basin-boundary crisis, not a fold"
  statement is thereby confirmed over the whole plane, not just a single-delay slice. The same computation
  supplies the §4.5 macro-ratio results (onset `R_B=1.000`/`R_A=1.01–1.06`; silent-collapse fraction;
  separator balanced accuracy; rescue set), which corroborate the neutral-continuum / no-Hopf finding from the
  monitoring view.
- **Conditional on baseline parameters.** The transition and recovery/collapse dichotomy are reported at the
  baseline `(b_G=0.8, A_ref=0.8, ρ=0.05, A_max=1.2, e=0.55, r=0.02)` and the documented IC grid. A full global
  sensitivity analysis over all parameters is not performed; these are conditional statements holding while
  the other parameters stay at baseline.
- **Calibration outlook.** These are qualitative/regime claims from a literature-banded sweep, not a fitted
  forecast. A formal calibration (estimating `τ_g`, and possibly `b`, from a small set of well-documented case
  studies, or a full ML/Bayesian fit) is feasible but not required for the conceptual claims and may not
  sharpen the conclusions given weak delay identifiability; it is left to future work.
- **Honesty caveat.** This is a literature-banded model sweep, not a full calibration: the per-study curve
  digitisation is still pending, and `τ_g` is a lumped regeneration-response delay across heterogeneous
  ecosystems. The defensible claim is that the collapse mechanism operates for any `τ_g` in the observed band
  — not that `τ_g` equals a single measured value. Report `τ_g` as an interval over the observed band, not as
  a single number; and when a point margin is small relative to the spread of that band, do not present it as
  a precision result.

---

## 9. Policy extensions (Half-Earth & reservation)

- Cap the human-available flow at `σ B`; compute both `K` and the debt increment from that cap; report `Ω`
  against the allocated share (not full `B`); state whether lags/`T_b` are on. This removes the impossible
  "`Ω = 0.575`, `D = 0`" pair.
- Corrected cap: `K = 0.5 B / e` (not `0.5 B / r_opt`); verified to settle at `Ω → 0.500`, `P = 0.217`, and a
  reservation policy that keeps `E` inside the allocated flow succeeds (no liquidation).
- **The stabilising institutional sign is the protective one.** The vicious cycle is the mobilising /
  extractive sign (demand responds to a perceived shortfall by raising pressure on the base); the reservation /
  Half-Earth cap is the protective sign (demand is held to a cap). The design principle is therefore a sign
  statement, not a delay statement: the stabilising institutional response is the protective /
  effort-reducing one, which is why the reservation (protective) policy is the candidate to pursue.
- The debt-repayment dichotomy is resolved: report the qualitative change (collapse → oscillation for
  `η ≳ 0.02`) and treat `η = 0` as the irreversible-debt benchmark.
- **The reservation result is a nominal-path consequence.** The "`E` inside the allocated flow succeeds, no
  liquidation" result is asserted under the nominal path. To make it defensible it should be scored as a
  robust-viability claim: declare a disturbance class (persistent productivity/`ρ`/`b`-shocks), define a
  preregistered retention rule (a governance module is kept only if it improves a declared
  protection-and-supply score), and apply an erosion conversion (convert the declared model defect into a
  certified-kernel erosion margin from the closed loop's contraction rate). Until that is done, state the
  result as a nominal-path consequence, not a robustly-viable policy claim.
- **The reservation claim is certified only under a controller that observes the typed floor.** The result is
  scored against the nominal path. The reason it is only nominal is structural: the policy is certified for a
  controller that observes the typed stock floor `A` (and the allocated flow), not merely the composite `B`.
  If only an aggregate composite is observed, no observation-based policy can guarantee the stock floor — the
  safe controls of the states consistent with a given observation may intersect emptily, so the failure is
  informational (which quantitative feature of the observation design — its coarseness / aggregation relative
  to the typed floor — is responsible) rather than dynamical.
- **Architecture-substitution caveat.** The model analyses continuous delays `τ_g, τ_p`. If a policy review
  cadence is modelled as sample-and-hold / periodic review, do not treat it as "the delay equation sampled at
  `T_r`": the two are different operators, and moving between them can move or delete stability boundaries. Any
  future "review interval" extension must be a separate operator with its own monodromy, and continuous-`τ`
  conclusions must not be transferred to it.

---

## 10. Demonstration

**Fig. `IMPLEMENTED_demo.png`** (generated by `demo_unified.py`, the well-posed smooth-ramp solver) shows a
representative overshoot run: the stock `A`, biocapacity `B` and population `P` all rise (a logistic
overshoot / boom), then the system collapses to the extinction floor with debt `D` building. Two model
properties are visible and reproducible: the delayed-regeneration overshoot (`A` briefly exceeds `A_max`, a
Hutchinson-style transient here around a long `τ_g`/`τ_p`); and the debt → degradation → collapse route, in
which lifting yield `b` raises `K`, `P`, and `E`, so that `D` accrues and `b` is eventually eroded.

**The productivity illusion ("`B` rises while `A` falls") — quantified, converged, and conditional.**

- **Method.** The reduced masking model (`dA/dt = G(A) − ramp(E−bA)/b_G`, `dD/dt = ramp(E−B) − ηD`,
  `B = bA + b_G G(A)`, `b = (b₀+T_b)e^{−αD}`, softplus ramp `w=0.05`) was integrated with converged RK4; a
  7,128-case scan plus a deficit sweep. The softplus width `w = 0.05` is stated, and insensitivity to `w` is
  reported; a mask is scored as a contiguous span with `dB/dt > 0` and `dA/dt < 0`, converged over
  `dt = 0.25 → 0.01`.
- **Result.** A genuine mask exists, but only for a small initial deficit. For the favourable configuration
  (`ρ=0.05, b_G=0.8, b₀=0.5, η=0.05, α=0.03, κ=0.2, t_wave=15, Δb=1.5`, `A₀=1.0`), the window is 5.4 yr wide
  at deficit `E − b₀A₀ = 0.06`: across it (`t ≈ 1.4 → 6.8` yr) `B` rises `0.576 → 0.647` (peak) while `A`
  falls `0.959 → 0.858`; over the run from `t=0` (where `A=1.00`, `B=0.578`) the peak-`B` rise is 0.069 and
  `A` falls by 0.142 (fig. `IMPLEMENTED_demo_masking.png`, panel a). It is converged (identical at
  `dt = 0.1/0.05/0.02/0.01`), so it is not an Euler artifact.
- **The mask is bounded and deficit-limited.** Window width grows with deficit up to ≈5.4 yr at deficit 0.06,
  then collapses to zero at deficit ≈0.075 (fig. panel b): beyond a small overshoot the stock-liquidation
  feedback dominates and technology cannot lift `B` — the run goes straight to the extinction floor with no
  mask.
- **Scope of the claim.** The earlier "rising biocapacity masks a falling stock" narrative is conditional: it
  holds near balanced conditions, and fails under a genuine overshoot (deficit ≳0.075, ≈15 % of the initial
  flow yield `b₀A₀`) — precisely the Jevons-rebound logic of §5 (technology raises `K`, `P`, `E`, so debt
  grows and closes the window). The illusion requires the wave to outpace the debt build-up — it must arrive
  while the stock is still high and the cumulative deficit is still small. A slow/late technology wave merely
  props up a falling yield.

**The illusion is an instance of the compensatory-aggregation gap.** The weighted composite (`B`, the
weak-sustainability index) satisfies its aggregate floor while the typed floor — the stock `A` — is violated.
Quantitatively it is the substitution buffer: because `B = bA + b_G G(A)`, the aggregate floor on `B` can be
met while the typed floor on `A` is violated by exactly the increment `b_G G(A)` — the same separation that
appears in §4.5 as the gap between `R_B` and `R_A`. To say it in the model's notation: the aggregate that an
index reads is a weighted sum over several floors, so a deficit in one (the stock) can be masked by a surplus
in another (the yield), and a transition can satisfy the aggregate the whole way along while it never
satisfies the individual floors. Two consequences follow:
- The mask is a structural failure of any aggregate that compensates a falling base with a rising yield, not
  an accident of one parameter set.
- Under exact-tube semantics (a transition is safe only if every state along it, not merely the endpoint,
  satisfies the constraints), the intermediate passage where `A` falls is itself a violation even if the
  endpoint recovers. That is a reason to report the through-time trajectory and the boundary curve rather than
  only an endpoint attractor.
- **Why Scenario E shows no illusion.** Biocapacity reaches ≈0.5588 in the original scenario E, but because
  `A` is rising (the logistic overshoot off the low starting population), not because of the masking
  mechanism. So "no shown scenario exhibits the illusion" is the correct reading there.
- **Presentation rule.** Present the illusion as narrow, deficit-bounded, and transient (fig.
  `IMPLEMENTED_demo_masking.png`), with the computed `t_peak` and the critical deficit stated as numbers.

---

## 11. Model scope

This is a conceptual / stylised model with representative calibration — not a forecast. Its purpose is to make
explicit the logic connecting accounting, deficit, lags, and the stock/yield decomposition, and to state which
outcomes are emergent (falsifiable) versus imposed (logistic regeneration, bounded technology, the lags, the
accounting identity). The 1961–2022 sentence is a qualified observation: the accounts are conservative
(biocapacity likely overstated, overshoot understated); the series is consistent with the illusion reading but
does not demonstrate it.

**National Footprint Accounts (NFA) data limitation.** The GFN accounts are account-based — measured yields and
conversion factors, no soil erosion, deforestation, groundwater depletion, or other cumulative degradation.
Consequently the estimated biocapacity most likely overstates the real resource base and the Footprint most
likely understates the true overshoot — the actual overshoot is likely larger than the accounts document.
This is the strongest reason to treat the 1961–2022 series as "consistent with" the illusion reading rather
than as evidence for it. The empirical programme the Discussion promises is the `d ln B = d ln b + d ln A`
decomposition with independent `A`-proxies (land cover, soil carbon, NPP).

**Information-layer limit.** The signature of the illusion ("`B` rises while `A` falls") is contemporaneously
observable (a read-off of two measured series). But whether that rise is a genuine recovery or a
technology-driven mask is not identifiable at the observation time: identifying the mask requires knowing the
technology/`b`-channel contribution, which is not available contemporaneously without independent proxies.
Two consequences: (i) a real-time observation of `B` rising while `A` falls is not evidence for the mask
mechanism over the recovery mechanism — both reproduce the same signature; and (ii) the empirical programme
must target the `b`-channel decomposition (independent `A`-proxies), not the composite `B` series.

**The empirical programme is a flux reconstruction, not a curve-fit.** The `b`-channel (the technology
contribution to yield) is an unobserved internal flux: it is not separately measured, but it is induced by the
observed stock changes. The discipline is to reconstruct unobserved internal fluxes from observed stock
changes and to state which fluxes are identifiable (a flux that is not a read-out of a measured stock is not
recoverable). So the programme is bounded: the `b`-channel is recoverable only relative to a declared
observation operator, which is why independent `A`-proxies are needed rather than a fit to the composite `B`.

---

## 12. Discussion

### 12.1 Structural properties and negative results

Several phenomena common in ecological models are absent here, and the absence is a structural property, not
an oversight. Each is stated so the reader does not expect it:

| Phenomenon looked for | Present? (verified) | Why absent / what it is | Implication |
|---|---|---|---|
| Critical slowing down (CSD) / early warning before the `τ_g` cliff | No | the `τ_g` transition is a first-order basin-boundary crisis: `Re λ ≈ +0.62` is constant (no eigenvalue crossing zero), and the `P`-relaxation return time is flat ≈150 yr for `τ_g=0–18` then vanishes abruptly at `τ_g≈19–20` | do not expect a smooth warning signal before a long-`τ_g` collapse; monitoring a single trajectory's relaxation time will not warn |
| CSD before the fixed-liability `E`-fold | Yes, but only increment-dominated (`b_Gρ>b`) | there `B'(A*)=0` exactly (a genuine fold, two opposite-sign-`B'` fixed points merging); absent at baseline where `B(A)` is monotone | Scheffer's "loss of resilience precedes the switch" applies only to this regime-scoped fold |
| Hysteresis / path dependence in the threshold | No | `A_c(E)` is single-valued; for a fixed `E` there is at most one deficit-region fixed point (no bistability), so the collapse–recovery threshold is the same going up as coming down | no path memory in the threshold; recovery is immediate once the liability is lowered (the asymmetry is in time, not in the threshold) |
| Endogenous limit cycle (sustained boom–bust) | No | the regrow-overshoot-recollapse is a single recovery-overshoot pulse (two crossings of `0.5·A_max`), consistent with the monotone (no-Hopf) instability | the overshoot is not a self-oscillation; sustained boom–bust would need an external mechanism |
| Allee-type rescue threshold (a minimum viable stock) | No | no Allee term; the collapse at `τ_g=30` is domain-wide — every `A₀` from `0.02` to `1.00` (including a healthy stock `A₀=1.0`) collapses; the recover set is a measure-zero strip (`A₀=A_max` recovers; `1.19` and `1.21` both collapse) | you cannot rescue the system by starting from a higher stock — the lag is the controlling factor; only shortening it helps |

**So the collapse is robust but not predictable from a single scalar: it is driven by the regeneration lag
(a finite-amplitude basin erosion), not by a fold, not by Allee low-density dynamics, and it carries no
generic CSD precursor.** This is more informative than a set of positive results: it tells a manager which
levers do not exist (no rescue-by-stock, no early-warning signal) and which do (shorten the lag; and, only for
the increment-dominated `E`-fold, watch for slowing). The result also inverts the classical
complexity–stability expectation of May (1973), who showed that increasing species number and connectance in
model ecosystems does not confer stability but tends to destabilise beyond a critical complexity threshold.
Here instability is generated in the opposite sense: it emerges in a deliberately minimal, low-complexity
system (two state variables, a single feedback loop, and an Allee-free regeneration term), so the collapse is
not a by-product of model richness but follows from the deficit mechanism and the regeneration lag alone.
Model extensions suggested by the negative results — stochasticity, seasonal forcing (to test for induced
cycles), or an explicit Allee term (to test for a rescue route) — are future-work directions, not changes to
the present deliberately minimal, deterministic, Allee-free model.

**The macro-ratio monitor fails silently in the long-`τ_g` regime.** The `R_B`/`R_A` ratios of §4.5 are
necessary-but-not-sufficient once the lag is too long: on the documented `A₀×P₀` grid at `τ_g = 30`, 36.5 %
(72 of 197) of collapses begin with `R_B < 1` and `R_A < 1` — neither ratio warns; only shortening the
regeneration lag helps. (At `τ_g = 10`, only 1.6 % of collapses are silent.) Ratio-based monitoring therefore
cannot replace the lag: it is a leading/necessary check, not a collapse forecaster. This is prediction 8.

**The rescue set collapses to a measure-zero strip.** The rescue set (initial conditions that recover) is a
39.9/39.9/39.4 % A-span of 0.100–1.300 (13 distinct `A₀`) at `τ_g = 0/10/18`, then collapses to 5.3 % with a
1.200–1.200 (1 distinct `A₀`) strip at `τ_g ≥ 20` — i.e. at `A_max` only. Combined with the absorbing
collapse (§12.2), this is the quantitative form of the "cannot rescue by starting higher" statement.

**The transition is a nonlocal, not a map, bifurcation.** The asymptotic one-step map (when the delays are
restored to their large-time limits) has fixed points exactly on the equilibrium family (`E = 0.15 → A = 0.283`;
`0.30 → 0.576`; `0.50 → 0.986`; boundary `A_max = 1.2`) and its local `Re λ_max` is
`+0.5917 → +0.6249 → +0.6250` — constant, no flip across `τ_g ≈ 19`. The asymptotic map therefore reproduces
the fixed points but not the `τ_g` cliff, confirming the transition is a nonlocal basin-boundary crisis, not a
map bifurcation, and that the discrete and continuous pictures do not agree as `τ_g` is increased. This
corroborates the no-CSD reading of the delay transition, which we distinguish from the `E`-fold of §4.2.

**Separator degradation is a class-imbalance artefact unless reported by balanced accuracy.** The neutral
separator `P = B(A)/e` (i.e. `R_B = 1`) classifies the basin at balanced 99 % (no-delay) → 81 % (`τ_g = 30`);
a linear functional shows 96 % (no-delay) → 50 % (`τ_g = 30`, chance) while its raw accuracy is 94.7 % — equal
to the majority-collapse class (197/208). Report separator/ratio accuracy by balanced accuracy, never raw
accuracy on the long-`τ_g` basin.

**Recovery overshoot is real, initial-condition-dependent, and steep.** The recovery overshoot scales steeply
with the lag (a fit to the computed pulse gives `ov ≈ 0.0047·(τ_g/10)^4.84`, not a single `τ_g` law); it is an
initial-condition-dependent transient, so report it as a scoped number rather than a universal amplitude.

### 12.2 Recovery dynamics

- **Recovery from the extinction floor is not self-sustaining at realistic lags.** Starting from the
  post-collapse floor at `τ_g ≥ 20`, the stock regrows but overshoots `A_max` and re-collapses to `A_ext`,
  rather than settling at the sustainable boundary: `A_peak` = 1.31 (`τ_g=20`), 1.45 (30), 1.60 (40), 1.88
  (60), and the fraction of the run spent above `0.5·A_max` falls monotonically (0.16 → 0.045 → 0.033 → 0.020)
  — so the collapse is effectively absorbing, not a transient excursion. This matches the field picture of
  slow, incomplete, often-failed recovery (Hutchings & Reynolds 2004; Neubauer et al. 2013). The collapse is
  not merely hard to reverse, it is self-sustaining under the regeneration lag. (This is separate from the
  masking window and from the Allee-free fixed-liability threshold — the same delay-driven liquidation, read
  as a recovery-blocking mechanism.)
- **The regeneration rate sets how long recovery takes; the regeneration lag sets whether it happens at all.**
  Sweeping `ρ` and `τ_g` independently from the extinction floor, the time to 50 % of `A_max` scales roughly
  inversely with `ρ` (t50 ≈ 145/ρ yr: 203 at `ρ=0.03`, 142 at 0.05, 105 at 0.08, 82 at 0.12, at `τ_g=30`),
  while whether it recovers at all is decided by `τ_g` (recovered at `τ_g ≤ 18`, collapsed at `τ_g ≥ 20`, for
  every `ρ`):

  | `ρ` (yr⁻¹) | `τ_g=10` (recovers) | `τ_g=30` (collapses) |
  |:--|:--:|:--:|
  | 0.03 | t50 ≈ 162 yr | t50 ≈ 203 yr |
  | 0.05 | 106 | 142 |
  | 0.08 | 74 | 105 |
  | 0.12 | 56 | 82 |

  A manager has two genuinely different levers: accelerate the regeneration rate (restore stock-by-stock
  productivity) to shorten the time to recovery, versus shorten the regeneration lag (recruit/protect the seed
  source) to change whether recovery happens. The two do not substitute: raising `ρ` makes a doomed trajectory
  recover faster to 50 % but does not keep it from collapsing under a large `τ_g`.
- **Recovery overshoots the old `A_max` before settling (a catch-up rebound pulse).** From the floor, a system
  that does recover rises past `A_max` before relaxing: `A_peak` = 1.21 (`τ_g=10`), 1.25 (15), 1.28 (18) — up
  to +0.08 beyond `A_max` (fig. `scans/eco_recovery_insight.png`). This is the Hutchinson-style overshoot on
  the recovery side, and it is why a recovering system can appear to "overshoot" briefly — a transient that
  must not be read as a new stable overshoot. (It is distinct from the §Demonstration collapse-regime
  overshoot, which ends in liquidation.)
- **Grid-dependence of the recover fraction is bounded but real.** On the same integrator, a coarse 6×8 vs fine
  25×31 grid at `τ_p=0`:

  | `τ_g` (yr) | fine (0.05 step) | coarse (0.2 step) | fine / coarse |
  |:--|:--|:--|:--:|
  | 30 | 0.027 | 0.104 | 0.26 |
  | 40 | 0.212 | 0.208 | 1.02 |
  | 50 | 0.301 | 0.417 | 0.72 |
  | 60 | 0.321 | 0.396 | 0.81 |

  The coarse grid overstates the recover fraction near collapse (at `τ_g=30`: 0.104 coarse vs 0.027 fine), so
  publish the recover fraction on the fine mesh and report the coarse value only as a bound.
- **The boundary-curve result is more interpretable than a percentage.** Under no delay the separatrix in
  `(A₀,P₀)` is exactly the equilibrium family line `P₀ = B(A₀)/e`: "recover ⟺ `P₀ < B(A₀)/e`" matches the
  classification on 99.0 % of the 208-cell grid (the only exceptions are `A₀ > A_max`, outside the stock
  domain). This is the numerical witness to the neutral continuum: the recover basin is precisely the stable
  side of the equilibrium line. Under baseline delays `(30,25)` the basin collapses to a thin strip
  `A₀ ≈ A_max` (1.2) with `P₀ ≲ B(A_max)/e ≈ 1.09`, and nothing else recovers — the delay strips away the
  protected below-the-line region except right at the sustainable boundary (5.3 %). Present the boundary curve
  rather than only the fraction.
- **The delay-response non-monotonicity at `τ_g ≈ 40–60` is real, not a grid artifact.** The recover fraction
  has a deep minimum at `τ_g=30` (≈0.03) and re-opens to ≈0.21 (40), ≈0.30 (50), ≈0.32 (60); the coarse grid
  shows the same min→rise shape. A boundary (separatrix) curve as a function of `(τ_g,τ_p)` is the natural
  follow-up figure.

### 12.3 Robustness of the main results

- **Recover–collapse is robust to `b_G`.** On the documented grid (computed, `(30,25)` baseline):

  | `b_G` | recover (no delay) | recover (baseline `(30,25)`) | Δ |
  |:--|:--|:--|:--:|
  | 0.4 | 0.394 | 0.053 | 0.341 |
  | 0.6 | 0.399 | 0.053 | 0.346 |
  | 0.8 | 0.399 | 0.053 | 0.346 |
  | 1.0 | 0.404 | 0.053 | 0.351 |
  | 1.2 | 0.404 | 0.053 | 0.351 |

  Over a 3× range of the standing-stock value, the no-delay recover fraction varies only 0.394→0.404 (±1.3 %)
  and the baseline-delay recover fraction is pinned at 0.053 — the qualitative result is robust, not a `b_G`
  artefact.
- **The monotone instability is structural** (independent of `ρ`). The full leading eigenvalue is essentially
  independent of `ρ` (≈ +0.62, dominated by the depletion gain `a₃ = b₀/b_G`) — itself evidence that the
  monotone instability is structural, not a fast–slow artifact, so the stability classification of §4.3 does
  not carry over.
- **The fast–slow reduction is valid only for `ρ ≫ r` and we use the full equation.** The classification
  reduces the 2-D two-delay system to a scalar two-gain delayed logistic under the fast–slow separation
  `ρ ≫ r` (and while `a₁₁ ≤ 0`). That separation is not satisfied at realistic `ρ`. The table (computed at the
  sensitivity configuration `τ_g=30, τ_p=25, A*=0.8, b₀=0.5, b_G=0.8, e=0.55, r=0.02`) reports the leading real
  eigenvalue of the full transcendental `D(s)=0` alongside the fast–slow `a₁₁` and the timescale ratio
  `ρ/r`:

  | `ρ` (yr⁻¹) | full-`D(s)=0` leading `Re λ` | fast–slow `a₁₁ = G′(A*)+b/b_G` | `a₁₁ > r`? | `ρ/r` |
  |:--|:--|:--|:--:|:--:|
  | 0.02 | +0.625 | 0.618 | yes | 1.0 |
  | 0.05 | +0.625 | 0.608 | yes | 2.5 |
  | 0.10 | +0.625 | 0.592 | yes | 5.0 |
  | 0.50 | +0.625 | 0.458 | yes | 25 |
  | 1.50 | +0.625 | 0.125 | yes | 75 |

  Only at `ρ = 1.5` (`ρ/r = 75`) is the fast–slow scaling justified, and even there `a₁₁` stays positive — no
  qualitative flip. At realistic `ρ ∈ [0.02, 0.1]` (`ρ/r = 1–5`) the reduction is out of its regime, so the
  full `D(s)=0` must be used. We always use the full equation.
- **The masking band** is bounded by the deficit limits of §Demonstration (≈5.4 yr at deficit 0.06; vanishes at
  deficit ≈0.075). `α` and `τ_p` were not independently swept (each needs its own grid); state `α = 0.03` and
  `τ_p = 25` as illustration values needing calibration, and treat the "dangerous band `(2f−1)ν > 1`" as an
  estimated indicator.

---

## 13. Limitations

- **The sustainable point is a boundary equilibrium and stability is one-sided.** The exact `[·]₊` is
  non-smooth at `A = A_max` (and at `E = bA`), so the "sustainable" state is a boundary of the deficit regime,
  not an interior point. Linearise one-sided (from the deficit/lower side only) and report that stability as
  such. Because the exact switch yields no imaginary-axis crossing, the non-smoothness does not create
  spurious oscillations. Where a smooth ramp replaces `[·]₊` (reference implementation only), fix its width
  `w`, state it, and report insensitivity to `w`.
- **The masking illusion is small-deficit only, not generic.** The window maxes at ≈5.4 yr (deficit 0.06) and
  vanishes at deficit ≈0.075 (≈15 % of the initial flow yield `b₀A₀`), and it is converged (RK4). It does not
  appear for deficit ≳0.075 and must not be cited as a general phenomenon — only as the narrow, transient,
  small-overshoot band of §Demonstration.
- **Parameters are representative, not estimated; the two headline results have been sensitivity-checked.** The
  results are illustrative and need calibration; `b_G`, `α` and the lags are lumped, not measured. `τ_g` is the
  partial exception: it is field-banded as a regeneration/recruitment-response lag (≈time to ~50 % of
  pre-disturbance productive capacity), and the fine sweep shows the collapse basin and monotone no-Hopf
  instability are robust across that band for `τ_g ≳ 20 yr` (transition band ≈18–20 yr), with the extended
  `τ_p` grid not moving the cliff; the fast-regeneration regime `τ_g ≲ 18` returns the recovery outcome.
  **Fit-defect disclosure.** Any parameter pinned at an optimisation bound (a fit artefact rather than an
  estimate) is declared as such, never presented silently as a calibration. **Interval discipline.** A
  point-margin small next to an uncertainty scale is reported as a coin-flip, not as skill/stability; the same
  wording discipline applies to any tight margin here.
- **`η` is set physical (non-zero); the singular `η → 0` case concerns the full model.** The constant-
  parameter subsystem S0 drops `D` and `η`, so the η-singularity caveat does not apply to it.
  `η → 0` applies to the full `(7)` equation, where `η` decides whether an equilibrium exists. We set
  `η = 0.05 yr⁻¹`, justified as a minimal environmental regeneration / degradation-removal rate. Outcomes are
  insensitive to `η` over a modest range provided `η > 0`; a reader setting `η = 0` deliberately removes the
  regeneration channel and must be told it removes the equilibrium rather than perturbing it.

---

## 14. Conclusions

The model yields a sharp, policy-relevant conclusion. The balance point is the biocapacity ratio `R_B = 1`
(footprint = total biocapacity), which coincides with the neutral equilibrium family `P = B(A)/e` and, in the
increment-dominated regime, with the interior-MSY fold threshold. The commonly monitored flow-yield ratio
`R_A = 1` is only a leading, non-causal signal, and its lead over `R_B` is governed by the flow share `ψ` —
so a sustainable system can legitimately run at `R_A > 1`.

The more consequential result is negative. Once the regeneration lag is sufficiently long, neither ratio
forecasts collapse: the transition is a nonlocal basin-boundary crisis carrying no critical-slowing-down
precursor, the recover basin collapses to a measure-zero strip, and recovery from the extinction floor is not
self-sustaining. The controlling variable is the regeneration lag, not the ratio; the manager's lever is to
shorten the lag, and no early-warning signal or rescue-by-stock exists. Only in the increment-dominated
`E`-fold does the classical "loss of resilience precedes the switch" structure apply, and even there it is
regime-scoped.

The productivity illusion — "biocapacity rises while the stock falls" — is real but narrow, deficit-bounded,
and transient, and it is a structural consequence of any aggregate that compensates a falling typed floor with
a rising yield. It is not identifiable contemporaneously without independent proxies for the technology
channel. The paper therefore contributes a monitoring boundary (`R_B = 1`), a leading-indicator caution
(`R_A`), and a precise statement of when monitoring fails (long regeneration lag), together with the
policy-relevant levers (shorten the lag; adopt the protective institutional sign) and the levers that do not
exist (no rescue-by-stock, no early warning).

---

## References

- Blomqvist, L., Brook, B. W., Ellis, E. C., Kareiva, P. M., Nordhaus, T. & Shellenberger, M. (2013). Does the
  shoe fit? Real versus imagined ecological footprints. *PLoS Biology*, 11(11), e1001700.
- Borucke, M., Moore, D., Cranston, G., Gracey, K., Iha, K., Larson, J., Lazarus, E., Morales, J. C.,
  Wackernagel, M. & Galli, A. (2013). Accounting for demand and supply of the biosphere's regenerative
  capacity: The National Footprint Accounts' underlying methodology and framework. *Ecological Indicators*,
  24, 518–533.
- Brander, J. A. & Taylor, M. S. (1998). The simple economics of Easter Island: A Ricardo–Malthus model of
  renewable resource use. *American Economic Review*, 88(1), 119–138.
- Galli, A., Giampietro, M., Goldfinger, S., Lazarus, E., Lin, D., Saltelli, A., Wackernagel, M. & Müller, F.
  (2016). Questioning the ecological footprint. *Ecological Indicators*, 69, 224–232.
- Giampietro, M. & Saltelli, A. (2014). Footprints to nowhere. *Ecological Indicators*, 46, 610–621.
- Gu, K., Niculescu, S.-I. & Chen, J. (2005). On stability of time-delay systems with perturbed parameters.
  (Crossing-curve formalism.)
- Hale, J. K. & Huang, W. (1993). Global geometry of the stable regions for two delay differential equations.
  *Journal of Mathematical Analysis and Applications*, 178(2), 344–362.
- Haberl, H. & Aubauer, H. P. (1992). (Application of the delayed-logistic framework to human
  population/load dynamics.)
- Hutchings, J. A. & Reynolds, J. D. (2004). Marine fish population collapses: consequences for recovery and
  extinction risk. *BioScience*, 54(4), 297–309.
- Hutchinson, G. E. (1948). Circular causal systems in ecology. *Annals of the New York Academy of Sciences*,
  50(4), 221–246.
- Lin, D., Hanscom, L., Murthy, A., Galli, A., Evans, M., Neill, E., et al. (2018). Ecological footprint
  accounting for countries: updates and results of the National Footprint Accounts. *Sustainability*, 10(12).
- May, R. M. (1973). Stability and complexity in model ecosystems. *Princeton University Press.*
- Neubauer, P., et al. (2013). Resilience of recovering fish populations. *Fish and Fisheries*, 14(3).
- Poeplau, C., et al. (2011). Temporal dynamics of soil organic carbon after land-use change. *Global Change
  Biology*, 17(7), 2415–2427.
- Poorter, L., et al. (2016). Biomass resilience of Neotropical secondary forests. *Nature*, 530(7590), 211–214.
- Schaefer, M. B. (1954). Some aspects of the dynamics of populations important to the management of the
  commercial marine fisheries. *Bulletin of the Inter-American Tropical Tuna Commission*, 1(2), 25–56.
- Scheffer, M., Carpenter, S., Foley, J. A., Folke, C. & Walker, B. (2001). Catastrophic shifts in
  ecosystems. *Nature*, 413(6856), 591–596.
- Shampine, L. F. & Thompson, S. (2001). Solving DDEs in MATLAB. *Applied Numerical Mathematics*, 37(4), 441–458.
- van den Bergh, J. C. J. M. & Grazi, F. (2015). Reply to the first systematic response by the Global Footprint
  Network to criticism: a real debate finally? *Ecological Indicators*, 58, 458–463.
- Wackernagel, M. & Rees, W. (1996). *Our Ecological Footprint: Reducing Human Impact on the Earth.*
  New Society Publishers.
- Wackernagel, M., et al. (2002). Tracking the ecological overshoot of the human economy. *PNAS*, 99(14).
- Abaee, A. Various companion manuscripts. Cited where their methods or framing are used (compensatory
  aggregation; typed flux ledgers; incomplete-observation viability; mobilising vs. protective controller
  sign; negative-certificate and interval-discipline methods; surplus-production forecast scoring).

**(Data availability.)** This study is a mathematical and computational analysis and reports no new empirical
dataset. All numerical results, parameter sweeps, and figures were generated by the accompanying model code
run from stated initial conditions and parameters; the code (see Reproducibility below) is the primary artefact,
and its generated outputs are written to `data/topdown_results.json`. No primary observational data were
collected. The only empirical inputs are published values used to bound the regeneration lag, which are drawn
from the National Footprint Accounts and the field studies cited in the References and are not reproduced or
re-distributed here; readers should consult those sources for the underlying data.

**(Reproducibility.)** The model is implemented as
`model_sims/corrected.py`, `model_sims/topdown.py`, `model_sims/r1_basin.py`, and `model_sims/char_eq.py`
(drivers `model_sims/_run_topdown.py`, `demo_unified.py`, `mask_rk4.py`); the results are written to
`data/topdown_results.json` and rendered as `scans/topdown_macro_ratios.png`,
`scans/topdown_ratio_separation.png`, and `scans/topdown_delay_boundary.png`. All numeric results report
their integration protocol and termination convention (§Numerics).

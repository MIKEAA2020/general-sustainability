# Supplementary Information

**Manuscript:** Emergent Carrying Capacity, the Biocapacity Ratio, and the Productivity Illusion: Deficit-Driven Collapse in a Delayed Coupled Human–Environment Model

*Revision 29 · Companion to `IMPLEMENTED_revision_ECOMOD_v29.md` · Journal: Ecological Modelling*

This document collects the supporting material that keeps the main text focused: the full model specification, the scaling, the analytic derivations, the scenario and parameter tables, the sensitivity/robustness record, the prediction-to-section map, and the supplementary references. It does not restate results already in the main text; it provides the derivations and tables behind them. Where a derivation is used in the main text, the relevant section is cited so the reader can cross-reference.

---

## S1. Model equations and symbol table

### S1.1 Governing equations

The model is a system of four equations in three state variables (`A`, `P`, `D`) plus one algebraic carrying-capacity relation, coupled through two discrete delays:

```
Regeneration:  G(A) = ρ A (1 − A/A_max)                          (S1)
Biocapacity:   B    = b A + b_G G(A)                            (S2)
Footprint:     E    = e P                                       (S3)
Stock:         dA/dt = G(A(t−τ_g)) − [E(t) − σ b A(t)]₊ / b_G   (S4)
Population:    dP/dt = r P(t) [1 − P(t) / K(t−τ_p)]              (S5)
Carrying cap:  K    = B / e                                     (S6)   [algebraic]
Debt:          dD/dt = [E − B]₊ − η D                           (S7)
Degradation:   b    = (b₀ + T_b(t)) e^{−α D(t)}                 (S8)
Technology:    T_b  = Δb / (1 + e^{−κ(t−t_wave)})               (S9)
```

`[x]₊ = max(x, 0)`. `σ` is the human-available share of the flow; `σ = 1` with no reservation policy, and setting `σ` together with a population cap enforces a reservation / Half-Earth stance (`E ≤ σ·B`).

**Central structural assumption (Eq. S4).** Demand is satisfied *first* from the flow yield `bA` (the fruit — leave the tree); only the shortfall `[E − bA]₊` liquidates the standing stock, at rate `1/b_G`. This is the deficit mechanism, and it is what makes the two flow accounts no longer parallel: biocapacity appears directly in the stock equation. In the capital-only limit (`ψ → 0`, equivalently the saw-log form) Eq. (S4) reduces to the standard gross-depletion harvest equation with harvest coefficient `γ = 1/b_G`.

**Well-posedness at the boundary.** The original `dP/dt` diverges as `K → 0`; an extinction floor `A_ext > 0` bounds `K ≥ b·A_ext/e > 0` and the state is clamped `A ≥ A_ext`, `P ≥ 0`. "Collapse" is therefore a well-defined approach to the extinction boundary, not a numerically clamped blow-up.

**Conservation structure (three "books").** The state variables live in three distinct books that are never mixed: `A` is the **capital book** (the standing base, removed only by liquidation); the flow yield `bA` is the **flow-yield book** (the fruit, separable from the base); and `D` is the **degradation/debt book** (the erosion of the surviving stock's yield). Conservation follows from the incidence structure (each outflow assigned to exactly one donor book) and positivity from donor limitation (an outflow vanishes when its donor compartment is empty).

### S1.2 Symbol table

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
| `R_B` | biocapacity ratio = `E/B` | — | derived |
| `R_A` | flow-yield ratio = `E/(bA)` | — | derived |
| `ψ` | flow share = `bA/B` (0 ≤ ψ ≤ 1) | — | derived |

Because `A` is in physical hectares it is independent of yield, so `b = B/A` is definable and the decomposition `B = b·A + b_G·G(A)` is identifiable. (With a stock measured directly in global hectares — as in the National Footprint Accounts — a hectare already embeds `b`, and the decomposition is not identifiable.)

---

## S2. Non-dimensionalisation and scaling

The full generality statement and the single clean control are complementary.

**Six-group set (full statement).** `t̂ = rt`, `a = A/A_max`, `p = P·r_opt/(b₀A_max)`, and the groups `s = ρ/r`, `g = γ b₀ f/ρ`, `f = e/r_opt`, `θ`, with scaled delays `τ̂_M = rτ_g`, `τ̂_P = rτ_p`.

**Single clean control.** Reducing the 2-D two-delay system to a scalar two-gain delayed logistic (fast–slow separation, `ρ ≫ r`) gives the control

```
χ = q/(ρ − 2q),   q = γ e b₀ / r_opt
```

with `Λ` the sign of the gain-surface comparison `r²a₁₁² − (γ e a₂₁)²`. `χ` (and its sign structure) is the cleanest single stability index; the six-group set is retained for full generality. The two are complementary, not competing.

The `2` appears throughout because the two regime classes are separated at `b_G ρ = b`, equivalently `ψ = 1/2`.

---

## S3. Analytic derivations

### S3.1 Carrying capacity and the MSY

`K = B/e` is emergent (it moves with `A` and `b`). Because the capital growth `b_G G(A)` is positive only for `0 < A < A_max`, the total sustainable-yield curve `B(A) = bA + b_G G(A)` has an interior maximum — the MSY:

```
dB/dA = b + b_G ρ(1 − 2A/A_max) = 0
A*  = A_max (b + b_G ρ) / (2 b_G ρ)
B_max = A_max (b + b_G ρ)² / (4 b_G ρ)
```

The sustainable equilibrium is interior (`A* < A_max`), not `A_max` — a steady harvest of the capital growth keeps the stock below its unmanaged maximum. This is the surplus-production / MSY structure of Schaefer (1954). Only in the flow-only limit (`b_G G ≪ bA`, the orchard) does the stock tend to `A_max`.

**Regime-conditional interior statement.** `A* < A_max` holds only in the **capital-dominated** regime, i.e. `b_G ρ > b` (equivalently `ψ → 0`). When `b_G ρ < b` (flow-dominated, `ψ → 1`) `B(A)` is monotone increasing on `[0, A_max]` and there is no interior maximum: the sustainable point is the boundary `A_max`. This is precisely the regime the baseline parameter set sits in (`b_G ρ = 0.8·0.05 = 0.04 < b = 0.5`).

### S3.2 Fixed-liability threshold; the saddle-node = MSY

For a fixed liability `E`, the deficit-region equation `dA/dt = 0` is a quadratic in `A` with an unstable root (the separatrix), and the saddle-node is exactly the MSY:

```
A_c(E) = [ (b_G ρ + b) − √((b_G ρ + b)² − 4 b_G ρ E/A_max) ] A_max / (2 b_G ρ)
E_sn   = B_max = A_max (b + b_G ρ)² / (4 b_G ρ)              (safe basin vanishes at MSY)
```

A fixed liability above `B_max` cannot be sustained by harvesting regrowth. The threshold is emergent and `E`-dependent (no Allee term needed), located at `A_c(E)`, never at `A_max/2`. When realised the fold is a saddle-node (fold) bifurcation — the catastrophic-shift / critical-transition structure of alternative-stable-state ecology (Scheffer et al. 2001). **The fold is regime-scoped:** it is realised only in the capital-dominated regime (`b_G ρ > b`); at baseline it is absent.

### S3.3 The equilibrium family `P = B(A)/e`

In the deficit region (`E > bA`), Eq. (S4) reduces exactly to

```
dA/dt = G(A(t−τ_g)) − [E − bA]₊/b_G  =  (B̃ − E)/b_G
```

where the lag-adjusted biocapacity is `B̃ = bA + b_G G(A(t−τ_g))` (so `B̃ = B` only when regeneration is evaluated at the delayed state). At the balance point `E = B̃`, so `R_B = 1`. The constant-parameter subsystem therefore has a **one-parameter family of equilibria** `P = B(A)/e` — a neutral continuum — rather than an isolated interior attractor. The `R_B = 1` locus is exactly this family, seen from the ratio (monitoring) and spectral (dynamical) views.

### S3.4 Stability classification and the vicious cycle

Linearising (S4)+(S5) in the deficit region at an interior point gives

```
a₁₁ = ρ(1 − 2A*/A_max) + b/b_G   ;  a₁₂ = −e/b_G   ;  a₂₂ = −r
det = r·ρ·A*/A_max > 0  (never a saddle)   →   zero-delay condition is  a₁₁ < r  (NOT a₁₁ < 0)
```

**The vicious cycle is real and quantitative.** `a₁₁` gains the `+b/b_G` term. For liabilities that scale with the stock (`E = f·bA`) the interior point is `A* = A_max[1 − (f−1)b/(b_G ρ)]`, self-sustaining (`a₁₁ > 0`) precisely when `(2f−1)ν > 1`, where `ν = b/(b_G ρ)`.

**Sign-corrected two-gain classification.** For `ρ ≫ r`, the reduced scalar two-gain delayed logistic with control `χ = q/(ρ − 2q)` gives:

- `χ > 1` (`Λ > 0`) ⇒ `τ_g`-only Hopf: `ω = r√(χ²−1)`, `τ_g* = arccos(−1/χ)/ω`.
- `χ < 1` (`Λ < 0`) ⇒ `τ_p`-only Hopf: `ω = r√(1−χ²)`, `τ_p* = arccos(−χ)/ω`.
- `χ = 1` (`Λ = 0`, i.e. `ρ = 3q`) ⇒ neither; two-delay boundary `s = π/ω`, `ω = 2r·cos(ωd/2)` ⇒ `s ≈ π/(2r) = 78.5 yr` at `d → 0`.

On the constant-parameter S0 of the present model this Hopf classification is **not** realised: the exact `[·]₊` gives a monotone positive-real eigenvalue with no imaginary-axis crossing for every delay. The classification describes the fast–slow reduction and does not predict the actual (structural) instability.

---

## S4. Scenario and parameter tables

### S4.1 Baseline parameter set

| Parameter | Value | Note |
|---|---|---|
| `ρ` | 0.05 yr⁻¹ | regeneration rate |
| `A_max` | 1.2 | carrying-area ceiling |
| `b₀` (baseline `b`) | 0.5 | base yield |
| `b_G` | 0.8 | standing-stock value |
| `e` | 0.55 | per-capita footprint |
| `r` | 0.02 yr⁻¹ | per-capita growth |
| `A_ext` | 0.02 | extinction floor |
| `η` | 0.05 yr⁻¹ | debt-repayment rate (full model) |
| `α` | 0.03 | degradation rate (illustration) |
| `τ_g`, `τ_p` | 30, 25 yr | baseline delays |

Baseline sits at a **knife-edge** `χ = 1` because `ρ = 3q` (`Λ = 0`), the measure-zero surface where the two gain surfaces are equal (`g_M = g_P`). This is why "no single delay destabilises" holds at baseline; perturbing off the knife-edge gives exactly one lag destabilising.

### S4.2 Regime table

| Regime | Condition | `B(A)` shape | Sustainable point | MSY | Collapse / mask behaviour |
|---|---|:--:|---|---|---|
| capital-dominated | `b_G ρ > b` (`ψ → 0`) | interior maximum | interior `A* < A_max` | interior MSY `A*`, `B_max` | smooth decline stabilised by demographic feedback — illusion small |
| flow-dominated (baseline) | `b_G ρ < b` (`ψ → 1`) | monotone ↑ | boundary `A_max` | none interior (max at `A_max`) | liquidation with threshold `A_c(E)`; overshoot invisible until demand exceeds flow yield — illusion more visible |
| marginal | `b_G ρ = b` | max at the boundary | `A* = A_max` (interior max merges with boundary) | boundary `A_max` | `ψ → 1` |

### S4.3 Delay-response sweep (baseline `τ_p = 25`)

| `τ_g` (yr) | 0–17 | 18 | 19 | 20–60 |
|:--|:--:|:--:|:--:|:--:|
| leading Re λ | 0.608–0.625 | 0.625 | 0.625 | 0.625 (constant) |
| recover fraction | 0.399 | 0.394 | 0.240 | 0.0529 |

The collapse result holds for `τ_g ≳ 20` — the range the field data support for forests, soils, and many (non-recovered) fisheries — while the fast-regeneration regime (`τ_g ≲ 18`) returns recovery. The cliff is a steep transition band (≈18–20 yr), not a single hard edge. `τ_p` shifts the band by <1 yr across a 4× range (10–40 yr).

### S4.4 Representative overshoot / masking configuration

```
ρ=0.05, b_G=0.8, b₀=0.5, η=0.05, α=0.03, κ=0.2, t_wave=15, Δb=1.5, A₀=1.0
```

The mask window is 5.4 yr wide at deficit `E − b₀A₀ = 0.06`, vanishing at deficit ≈0.075.

---

## S5. Sensitivity and robustness

- **Robust to `b_G`.** Over a 3× range of the standing-stock value (0.4–1.2), the no-delay recover fraction varies only 0.394→0.404 (±1.3 %) and the baseline-delay recover fraction is pinned at 0.053.
- **Monotone instability is structural** (independent of `ρ`). The leading eigenvalue is essentially independent of `ρ` (≈ +0.62, dominated by the depletion gain `a₃ = b₀/b_G`).
- **Fast–slow reduction is valid only for `ρ ≫ r`.** The full `D(s)=0` leading eigenvalue stays +0.625 for every `ρ` (0.02–1.5); at realistic `ρ ∈ [0.02, 0.1]` (`ρ/r = 1–5`) the reduction is out of regime, so the full equation is always used.
- **Masking band** is bounded by the deficit limits of §Demonstration (≈5.4 yr at deficit 0.06; vanishes ≈0.075). `α` and `τ_p` are illustration values needing calibration.
- **Grid dependence is bounded.** A fine (0.05 step) vs coarse (0.2 step) grid at `τ_p=0`: at `τ_g=30` the coarse grid overstates the recover fraction (0.104 coarse vs 0.027 fine). The fine mesh is the published value; the coarse value is reported as a bound.
- **The separator degrades with lag** — balanced accuracy 99.2 % (no-delay) → 81.2 % (`τ_g = 30`); a linear functional is chance (50.0 % balanced) at `τ_g = 30`.

---

## S6. Mapping of the eight falsifiable predictions to manuscript sections

| # | Prediction | Primary section | Supporting sections |
|:--:|---|---|---|
| 1 | Which lag destabilises is set by the sign of `Λ`/`χ`; on S0 the interior point is monotonically unstable for every delay | §6, §4.3 | §8 Numerics |
| 2 | Oscillation period near onset ≈ 4× dominant lag — only on a Hopf boundary; S0 has no oscillatory onset | §6 | §8 |
| 3 | Productivity illusion has a computable peak-biocapacity time `t_peak` | §6, §10 Demonstration | §10 |
| 4 | Reducing a policy lag `τ_e` matters comparably to reducing overshoot `f` | §6 | §9 |
| 5 | Flow share `ψ` locates the masking illusion | §6, §4.1, §4.5 | §10 |
| 6 | Regeneration lag `τ_g` sets recovery vs collapse (18–20 yr band) | §6, §8 | §12.2 |
| 7 | Regeneration rate vs lag are two decoupled levers | §6, §12.2 | §8 |
| 8 | Operating boundary is `R_B = 1`, not `R_A = 1` | §6, §4.5 | §8, §12.1 |

**The two masks.** *Technology mask:* `B` rises while `A` falls (requires progress). *Liquidation mask:* `E` steady while `A` falls (requires none). The discriminating observable is exactly which holds.

---

## S7. Supplementary references

Sources cited for the empirical regeneration-lag band, the National Footprint Accounts, and the standard modelling structures used in the derivations. (Full reference list in the manuscript.)

- Scheffer, M., Carpenter, S., Foley, J. A., Folke, C. & Walker, B. (2001). Catastrophic shifts in ecosystems. *Nature*, 413(6856), 591–596.
- Schaefer, M. B. (1954). Some aspects of the dynamics of populations important to the management of the commercial marine fisheries. *Bulletin of the Inter-American Tropical Tuna Commission*, 1(2), 25–56.
- Poorter, L., et al. (2016). Biomass resilience of Neotropical secondary forests. *Nature*, 530(7590), 211–214.
- Poeplau, C., et al. (2011). Temporal dynamics of soil organic carbon after land-use change. *Global Change Biology*, 17(7), 2415–2427.
- Hutchings, J. A. & Reynolds, J. D. (2004). Marine fish population collapses: consequences for recovery and extinction risk. *BioScience*, 54(4), 297–309.
- Neubauer, P., et al. (2013). Resilience of recovering fish populations. *Fish and Fisheries*, 14(3).
- Borucke, M., et al. (2013). Accounting for demand and supply of the biosphere's regenerative capacity: the National Footprint Accounts' underlying methodology and framework. *Ecological Indicators*, 24, 518–533.
- Wackernagel, M., et al. (2002). Tracking the ecological overshoot of the human economy. *PNAS*, 99(14).
- Hutchinson, G. E. (1948). Circular causal systems in ecology. *Annals of the New York Academy of Sciences*, 50(4), 221–246.
- Kuang, Y. (1993). *Delay Differential Equations, with Applications in Population Dynamics.* Academic Press.
- Shampine, L. F. & Thompson, S. (2001). Solving DDEs in MATLAB. *Applied Numerical Mathematics*, 37(4), 441–458.

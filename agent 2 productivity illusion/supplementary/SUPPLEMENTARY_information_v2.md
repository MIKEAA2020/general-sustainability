# Supplementary Information

**Manuscript:** Emergent Carrying Capacity and the Composition Illusion: Two-Land Conversion and the Identifiability of Collapse

*Companion to `manuscript_ECOMOD_v34.tex` (two-land). Journal: Ecological Modelling.*

This document collects the supporting material: the full model specification, the scaling, the analytic
derivations, the scenario and parameter tables, the sensitivity/robustness record, the prediction-to-section
map, and the supplementary references. It provides the derivations and tables behind the main-text results.
Where a derivation is used in the main text, the relevant section is cited so the reader can cross-reference.

**Structure and scope.** The manuscript is the **two-land** (fast-provisioning + ecological-capital) model.
§S1–§S4 and the *first* block of §S5 describe the **one-stock** (single-capital `A`) base model, which
the manuscript retains explicitly as a **one-stock comparator** (it recovers as a limit; its spectral features
`+0.62`/`+0.625`, the `5.4 yr` masking window and the `τ_g≈18–20 yr` recovery cliff are one-stock, *not*
two-land, properties). The **two-land** specification and its robustness are given by the manuscript's
"Model formulation" section and by §S5.1–§S5.5 below. Do not read the one-stock §S1–§S4 values as the
two-land result. Likewise the comparator's symbols and parameter values are comparator-only and must not be
imported into the two-book model: `A_max=1.2`, `b₀=0.5`, `A_ext`, `ρ=0.05`, the area-based MSY/saddle-node of
§S3, and the comparator's units `[D]=gha·yr`, `[α]=(gha·yr)⁻¹`. The two-book model instead uses `D` in
**gha** and `α` in **gha⁻¹** (so `αD` is dimensionless), a per-hectare quality state `q∈[0,q_max]`, and has
**no** interior area-based capacity maximum.

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
| `σ` | human-available share of the flow (dimensionless, 0 ≤ σ ≤ 1); σ = 1 means all flow yield harvestable without stock damage | — | param |

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

**The family is defined under full harvest, `σ = 1`.** Imposing `dA/dt = 0` on the family at an interior
point `A*` (with `E* = eP* = B(A*)` in the deficit region) gives

```
G(A*) = [E* − σ b A*]₊/b_G = G(A*) + (1−σ) b A*/b_G
```

which holds for arbitrary interior `A*` only if `σ = 1`. Thus the one-parameter family `P = B(A)/e` and
the neutral continuum below require `σ = 1`. Under a reservation `σ < 1` the equilibrium locus shifts to
`P = (σbA + b_G G(A))/e < B/e`, which removes `(1−σ)bA` from the sustainable population (verified: at
`σ = 0.9`, `dA/dt(P = B/e)` is negative for every interior `A*`). Each interior point is nevertheless
locally unstable, and the family is a continuum bounded by the conservation of the deficit identity.

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

On the constant-parameter S0 of the present model this Hopf classification is **not** realised: the exact `[·]₊` gives a monotone positive-real eigenvalue with no imaginary-axis crossing for every delay. **This is conditional, not parameter-free.** The sufficient condition is `S = a₁ + a₃ = G′(A*) + b/b_G > r` (with the delay condition `F′(0) = r − S + r a₁ τ_g − r S τ_p < 0`), which at baseline (`a₁ = −0.0167`, `S = 0.6083`, `r = 0.02`) holds over the whole `(τ_g, τ_p)` plane (`max F′(0) = −0.5883`), so a positive real eigenvalue is guaranteed for every delay combination (verified: leading `Re λ = +0.625` real across the plane; zero imaginary-axis crossings by the exact `s = iω` crossing-curve method). The classification describes the fast–slow reduction and does not predict the actual (structural) instability.

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
| capital-dominated | `b_G ρ > b` (`ψ → 0`) | interior maximum | interior `A* < A_max` | interior MSY `A*`, `B_max` | smooth decline stabilised by demographic feedback — masking weak |
| flow-dominated (baseline) | `b_G ρ < b` (`ψ → 1`) | monotone ↑ | boundary `A_max` | none interior (max at `A_max`) | liquidation with threshold `A_c(E)`; overshoot invisible until demand exceeds flow yield — masking more visible |
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

**Scope note.** The first block below is the **one-stock comparator** robustness (single capital `A`; spectral
values `+0.62`/`+0.625`, `5.4 yr`, `τ_g≈18–20 yr`). The **two-land** spectral robustness is in §S5.1–§S5.2
(composition diagnostic, leading eigenvalue `O(10⁻² yr⁻¹)` negative and CSD-free, basin demand thresholds).

- **Robust to `b_G`.** Over a 3× range of the standing-stock value (0.4–1.2), the no-delay recover fraction varies only 0.394→0.404 (±1.3 %) and the baseline-delay recover fraction is pinned at 0.053.
- **Monotone instability is structural** (independent of `ρ`). The leading eigenvalue is essentially independent of `ρ` (≈ +0.62, dominated by the depletion gain `a₃ = b₀/b_G`).
- **Fast–slow reduction is valid only for `ρ ≫ r`.** The full `D(s)=0` leading eigenvalue stays +0.625 for every `ρ` (0.02–1.5); at realistic `ρ ∈ [0.02, 0.1]` (`ρ/r = 1–5`) the reduction is out of regime, so the full equation is always used.
- **Masking band** is bounded by the deficit limits of §Demonstration (≈5.4 yr at deficit 0.06; vanishes ≈0.075). `α` and `τ_p` are illustration values needing calibration.
- **Grid dependence is bounded.** A fine (0.05 step) vs coarse (0.2 step) grid at `τ_p=0`: at `τ_g=30` the coarse grid overstates the recover fraction (0.104 coarse vs 0.027 fine). The fine mesh is the published value; the coarse value is reported as a bound.
- **The separator degrades with lag** — balanced accuracy 99.2 % (no-delay) → 81.2 % (`τ_g = 30`); a linear functional is chance (50.0 % balanced) at `τ_g = 30`.

### S5.1 Sensitivity of the proxy decomposition to the calibration `α` (share caveat, quantified)

The absolute split of World biocapacity into a fast-book proxy `X_t = b_f,t · A_f,t` and an
accounting residual `C_t = B_t − X_t` turns on the (unidentified) base-year calibration
`α = b_f(1961)·A_f(1961)/B(1961)` — the cropland share of `B` at the base year. The share-weighted
(decomposition log-mean / Divisia) contributions were recomputed over `α ∈ [0.10, 0.34]`:

| α | w_X | w_C | yield contrib. | area contrib. | residual contrib. | **sum** | dominant |
|---|---:|---:|---:|---:|---:|---:|---|
| 0.10 | 0.183 | 0.795 | +0.207 | +0.029 | −0.029 | +0.207 | yield |
| 0.15 | 0.275 | 0.689 | +0.310 | +0.044 | −0.148 | +0.207 | yield |
| **0.19** | **0.349** | **0.600** | **+0.393** | **+0.056** | **−0.242** | **+0.207** | yield |
| 0.25 | 0.459 | 0.457 | +0.517 | +0.073 | −0.384 | +0.207 | yield |
| 0.30 | 0.550 | 0.315 | +0.621 | +0.088 | −0.502 | +0.207 | yield |
| 0.34 | 0.622 | 0.087 | +0.702 | +0.100 | −0.594 | +0.207 | yield |

`α = 0.19` is the GFN (cropland ≈ 19 % of footprint) anchor. The columns after `w_C` are **weighted
contributions**, not raw component log-changes. Across `α ∈ [0.10, 0.34]` the weighted identity sums to
`d ln B = +0.207` **exactly**, and the *yield* channel is the dominant positive term in every row: the
qualitative conclusion (intensification dominates; residual falls) is robust to `α`. The **quantitative**
split is not: `w_X` ranges 0.183–0.622, the fast-book share in 2022 `s_X(2022)` ranges ≈0.30–≈1.00, and the raw
residual log-change ranges ≈−0.04–≈−6.8. Because the absolute split is this sensitive, only the **sign
ordering** (not the magnitudes) should be carried forward. Reproducible:
`model_sims/twoland_nfa_proxy_sensitivity.py`.

### S5.2 Spectral robustness of the composition diagnostic and the conversion-loop eigenvalue

This complements §S5.1 with the corresponding robustness of the two *spectral / structural* quantities
reported in `tab:conv` (composition diagnostic `Δb_conv` and leading eigenvalue `λ_+`) and `tab:basin`
(capital-crash demand threshold). Reproducible: `model_sims/verify_tab_conv_basin.py` and
`model_sims/twoland_fixed.py`.

**Composition diagnostic `Δb_conv = b_f − b_c_eff` at `q* = q_max/2`.** `b_c_eff = b_c + b_Gc·g_c(q*)`
(=`0.0660` at baseline). Across the fast-land yield, the sign is robustly positive — conversion *raises*
accounting capacity — and this is the structural (not contingent) composition mechanism:

| b_f | b_c_eff | Δb_conv | regime |
|---|---:|---:|---|
| 0.60 | 0.0660 | +0.534 | composition-premium |
| **0.85 (baseline)** | **0.0660** | **+0.784** | composition-premium |
| 1.20 | 0.0660 | +1.134 | composition-premium |
| 2.00 | 0.0660 | +1.934 | composition-premium |

Sensitivity to the standing-stock value `b_Gc` (at `b_f = 0.85`): `b_c_eff = 0.0580 / 0.0660 / 0.0740` for
`b_Gc = 0.4 / 0.8 / 1.2`, so `Δb_conv = +0.792 / +0.784 / +0.776` — the sign is robust over a 3× range.

**Leading eigenvalue `λ_+` of the frozen-demand active-conversion subsystem.** It is **negative** at every
row (no destabilising `+` eigenvalue) and **constant along the frozen-demand branch** (it does not vanish as
`E → E_ceil`), so there is **no critical slowing down** — verified at machine precision:

| E / E_ceil | 0.50 | 0.90 | 0.99 | 0.999 |
|---|---:|---:|---:|---:|
| Re λ_+ (baseline b_f=0.85) | −0.05366 | −0.05366 | −0.05366 | −0.05366 |

**But `λ_+` is NOT a single universal number.** It varies **monotonically with `b_f`** (with the second
(high-κ) mode `λ_2` also pushing negative):

| b_f | λ_+ | λ_2 |
|---|---:|---:|
| 0.60 | −0.0522 | −0.974 |
| **0.85 (baseline)** | **−0.0537** | **−0.998** |
| 1.20 | −0.0547 | −1.014 |
| 2.00 | −0.0556 | −1.029 |

**Other parameter sensitivity of `λ_+`.** It is **exactly independent of `ρ_c`** (the regeneration rate:
`−0.0537` at `ρ_c = 0.04/0.08/0.16`) — a genuinely robust structural result. It varies **mildly with the
conversion time constant** (`−0.0553 / −0.0537 / −0.0505 / −0.0417` at `τ_conv = 0.5 / 1.0 / 2.0 / 5.0` yr)
and **more strongly with the maintenance rate `μ`** (`−0.0254 / −0.0537 / −0.1099` at `μ = 0.03 / 0.06 / 0.12`
yr⁻¹, evaluated at a fixed fraction of each `μ`'s own `E_ceil`). The last is the one caveat worth flagging: the
*value* of `λ_+` depends on the cropland-maintenance term, so it should be reported as an order-of-magnitude
`𝒪(10⁻² yr⁻¹)` negative value that never crosses zero — not as a precise number — while the *qualitative* claims
(no `+` eigenvalue, no CSD, no fold) hold across all sweeps.

**`tab:basin` thresholds.** Endogenous-demand runs (`τ_g=20`, `τ_p=25`), grid-converged at `dt=0.05`,
`T=1000` yr: crash threshold is **monotone increasing in `A_c0`** (`≈2.41 → 2.70 → 2.98 → 3.14` for
`A_c0 = 0.40 / 0.70 / 1.00 / 1.18`), i.e. **higher initial capital supports higher demand** before the capital
book is drawn down; the boundary shifts by a band between `dt=0.1` and `dt=0.05` (grid convergence, reported as
`≈`).

### S5.3 Illustrative empirical anchoring of the regeneration timescale

**What is anchored, and what is not.** The model separates two regeneration quantities: the regeneration
**rate** `ρ` (yr⁻¹), which sets *how long* recovery takes (the recovery timescale ≈ `1/ρ = 20 yr` at the
baseline `ρ = 0.05`), and the regeneration **lag** `τ_g` (yr), which sets *whether* the stock recovers at all
(§12.2). Published "recovery-time" and "time-to-equilibrium" statistics are therefore, in the model's terms,
statements about the *rate* `ρ` (they are timescales); they become statements about the *lag* `τ_g` only
under an explicit "effective-timescale" reading, stated below. We label the result **illustrative** — it is a
transparency exercise, not a formal parameter estimation.

**The recovery statistics as reported (verified against the sources).** The three published measures are
heterogeneous in metric (time to a recovery level, time to a new equilibrium, probability of recovery over a
window), so there is no single clean `t₅₀`:

| System | Metric actually reported | Source |
|---|---|---|
| Tropical secondary forest | 122 Mg ha⁻¹ above-ground biomass recovered within 20 yr; median 66 yr to reach 90 % of old-growth biomass | Poorter et al. (2016) |
| Temperate soil (land-use change) | new SOC equilibrium reached after 23 yr (deforestation) and 17 yr (grassland→cropland) | Poeplau et al. (2011) |
| Marine fisheries | only 29 % of collapsed stocks recovered to 50 % within 5–15 yr; most showed little change by 15 yr; recovery generally within ≈20 yr once fishing pressure reduced to FMSY | Hutchings & Reynolds (2004); Neubauer et al. (2013) |

**The exponential-recovery conversion, used as an effective-timescale heuristic.** If recovery is
approximated as exponential so the time to 50 % recovery satisfies `t₅₀ = τ̄ ln 2`, then the effective
regeneration timescale is `τ̄ ≈ 1.44 · t₅₀`. Applied to the sourced timescales (soil 17–23 yr → 25–33 yr;
fisheries ≈20 yr under FMSY → 29 yr, with the Hutchings–Reynolds caveat that recovery is often far slower or
fails, extending the upper edge) this gives an **effective regeneration timescale ≈ 25–33 yr, representative
≈ 29 yr**, consistent with the manuscript's baseline `τ_g = 30 yr` and its core band of order 10–40 yr.

The readings "forest ≈ 50 % by 20 yr" and "fisheries ≈ 12–13 yr to 50 %" are **not** what those sources report;
the sourced statistics are as given in the table above. These conversions are transparent transformations of
published summary values under a stated recovery model; they are not formal parameter estimates from raw
recovery curves.

**Rate vs. lag, and the sensitivity statement.** Because the model assigns recovery time to `ρ`
(`1/ρ = 20 yr`) and recovery type to `τ_g`, converting a recovery-time statistic into `τ_g` is a
category-crossing heuristic: it is a useful order-of-magnitude anchor for `τ_g`, but it is not the same
object as the model's `ρ`-based timescale. The model's *structural* results are robust across this band —
at `τ_g = 17, 25, 30, 33 yr` the constant-parameter subsystem keeps a positive real leading eigenvalue
(`+0.625`, real) and no imaginary-axis crossing (no Hopf), so the monotone instability, the
`R_B = 1` necessary-but-not-sufficient bound, and the silent-collapse signature are unchanged (verified). The
*recover-vs-collapse outcome*, by contrast, is *not* band-insensitive: the recover fraction falls through the
≈18–20 yr cliff (coarse grid 0.54 at `τ_g = 18` → 0.21 at `τ_g = 20` → 0.00 at `τ_g ≥ 25`; reported fine
values 0.399 → 0.240 → 0.0529). The effective anchored band (≈25–33 yr) therefore lies at or above the
collapse threshold, so the model's principal prediction — that these regeneration timescales place forests,
soils, and many fisheries in the collapse regime — holds. The blanket statement that "the model's qualitative
results are unchanged over 17–33 yr" is thus not accurate: the *mechanism* is unchanged over the whole band,
but the *outcome* switches inside it.

### S5.3a Formal raw-curve estimation of the regeneration timescale (forest + fishery legs; soil cited)

The band above (`≈25–33 yr`, rep `≈29 yr`) was derived from **published summary statistics** (e.g. "median
66 yr to 90% of old-growth") under an effective-timescale heuristic. As stated there, that is *illustrative*,
not a formal parameter estimate. To sharpen it, we estimate the regeneration timescale directly from the
underlying **plot-level curves** rather than from the summaries, by fitting a lagged saturating recovery model
to raw age--biomass pairs.

**Data.** Poorter et al. (2016), *Biomass resilience of Neotropical secondary forests*, Nature 530:211–214;
2ndFOR database (`doi:10.5061/dryad.82vr4`). 1,334 plots across 41 Neotropical chronosequences, recording
stand age vs above-ground biomass (AGB) — the same study the summary statistic "122 Mg ha⁻¹ within 20 yr,
median 66 yr to 90%" was drawn from. This is a genuine recovery *curve* dataset (raw age–AGB pairs), not a
set of t₅₀ summaries. Reproducible: `model_sims/calibrate_tau_g_recovery_curves.py`; figure
`S1b_tau_g_calibration.png`.

**Relevance of forest regeneration data to the human--ecological model.** The model is human--ecological, but the
parameter this dataset constrains is *not* a human quantity. `τ_g` and `ρ` govern how fast the **capital-land class
regenerates** — the ecological recovery of the standing stock after it is drawn down. That is a property of the
ecosystem (how long a forest or soil takes to rebuild its productive capacity), not of the human population
that consumes it. The demand side is carried by `P`, `e` and demand `E = eP`; the regeneration leg is
ecological. A forest chronosequence is therefore the *right* object for this parameter — it is exactly the
field measurement of capital-land recovery that `ρ`/`τ_g` summarise — and it is independent of, and hence does
not confound, the human demand terms. What this dataset does *not* constrain is the human population or demand
side, which remains a representative parameter as stated above.

**Model and operational definition.** In the manuscript the regeneration is
`G(A(t−τ_g)) = ρ·A(t−τ_g)(1 − A(t−τ_g)/A_max)`, so `τ_g` is the **time lag between a change in the stock and
the subsequent regeneration response**. Operationally this is the lag before measurable recovery onset, NOT
the total or half-recovery time. Per chronosequence we fit

```
AGB(t) = AGB_inf (1 − e^(−(t − t_lag)/τ_r)),   AGB = 0 for t < t_lag
```

A per-site screen removed a small number of non-physical outliers (a site aggregate at 3655 Mg ha⁻¹ ≈ 8× the
plausible old-growth maximum; sites with no measurable recovery). 39 of 41 systems converged; 35 with
R² > 0.20 were retained (median R² ≈ 0.68).

**Result.** Across the 35 fits:

| quantity | median | IQR | 95% interval |
|---|---|---:|---:|
| onset lag `t_lag` | 1.4 yr | −0.5–3.5 | −2.0–8.8 |
| recovery timescale `τ_r` | 38.3 yr | 19.5–120 | 9.8–120 |
| time to 50% `t₅₀` | **29.9 yr** | 15.8–81.8 | 14.4–120 |
| asymptote `AGB_inf` | 310 Mg ha⁻¹ | — | — |

The fitted **`t₅₀ ≈ 30 yr`** reproduces the earlier illustrative band's representative value (`≈29 yr`)
**independently from the raw curves**, and the recovery timescale `τ_r ≈ 38 yr` lies at or above the one-stock
comparator's ≈18–20 yr cliff. (This cliff is a **one-stock comparator** feature, not a two-land property: in
the two-land model the recover/collapse boundary is a demand threshold, essentially flat in `τ_g` — see the
manuscript. We use the comparator cliff only as a reference scale, and do not imply the two-land model has it.) The early-accumulation onset lag `t_lag ≈ 1.4 yr` is
*not* the model's `τ_g` (a regeneration *delay*, not the onset of biomass accumulation) and is explicitly not
used as such — it confirms the SI's earlier caution that these are separate objects.

**Fishery leg (RAM Legacy B/BMSY).** For each of 439 stocks we located the depletion trough and fit the
rising tail of relative biomass `(B/BMSY)` with the same saturating model. 33 stocks showed a deplete-then-rebuild
episode and were fit (median R² ≈ 0.92):

| quantity | median | IQR | 95% interval |
|---|---|---:|---:|
| onset lag `t_lag` | 1.8 yr | — | — |
| recovery timescale `τ_r` | 3.4 yr | 2.3–5.8 | 1.0–7.7 |
| time to 50% `t₅₀` | **5.6 yr** | 4.0–6.5 | 2.0–9.7 |
| right-censored trajectories | 13 of 33 | — | — |

The fishery `t₅₀ ≈ 5.6 yr` is much faster than the forest `t₅₀ ≈ 30 yr` — as expected for short-lived, fast-growing
exploited stocks recovering under reduced fishing pressure, and consistent with Hutchings & Reynolds (2004)'s
"recovery generally within ≈20 yr under FMSY" being an upper bound. 13 of the 33 fitted trajectories are
right-censored (the rebuild is still in progress at the 2015 end of the window), so their fitted `τ_r` should be
read as a lower bound on the true timescale; that censoring is flagged rather than hidden. Figure
`S1c_fishery_recovery.png` shows representative fits; full per-stock table is
`scans/tau_g_calibration_fisheries.csv`.

**What this does and does not establish.** The model distinguishes the regeneration **rate** `ρ`
(which sets *how long* recovery takes) from the regeneration **lag** `τ_g` (which sets *whether* the stock
recovers at all). The fit here estimates a **recovery timescale** — the `ρ`-object — not the lag `τ_g`. The
mapping from a recovery timescale to `τ_g` is the *same category-crossing heuristic* described in §S5.3 (the
`t₅₀` effective-timescale reading); the present fit makes that heuristic *quantitative* by estimating `τ_r` and
`t₅₀` from raw curves rather than from the published summaries. So this is not a direct measurement of the
delay `τ_g`, and we do not present it as one.

**Scope: two fit legs, one cited leg.** Three ecosystem classes are represented, but only two are *fit* from
raw curves. **(i) Forest (fit).** 41 Neotropical chronosequences (Poorter et al. 2016) — see the forest table
above; `t₅₀ ≈ 30 yr`. **(ii) Fishery (fit).** RAM Legacy B/BMSY per-stock time series (OHI 2019 processing;
`doi:10.5281/zenodo.2542919`, 439 stocks, 2001–2015); 33 stocks show a deplete-then-rebuild episode and are fit
with the same saturating model (`t₅₀ ≈ 5.6 yr`, `τ_r ≈ 3.4 yr`; median R² ≈ 0.92; 13 right-censored). **(iii) Soil
(cited, not fit).** Soil organic-carbon re-equilibration is not fit here: the available SOC databases are
intervention-comparison (% SOC under perennial/annual/agroforestry) rather than a single population recovering
toward a shared reference, so a recovery-timescale fit would not be well-posed. The soil leg is therefore
retained as a cited timescale (Poeplau et al. 2011: ≈23 yr after deforestation, ≈17 yr grassland→cropland), as in
§S5.3. The model's `τ_g` is an *effective* consolidation across types (convention (i)); the two fit legs bound it
from either side (forest slow, fishery fast) and the soil cited value falls between.

**Fit-defect disclosure (per §13).** Six fits pinned `τ_r` at its 120-yr upper bound — these are slow-recovery
systems where the timescale is not resolved within the data and the bound, not an estimate, is returned. They
are retained in the table but the 95% upper edge (`120`) is a fit bound, not a measured value; the median `τ_r`
(≈38 yr) and the `t₅₀` median (≈30 yr) are robust to their exclusion (recomputed without them the medians move
by <3 yr). We flag this rather than presenting the 120-yr tail as a clean estimate.

**Relationship to §S5.3.** §S5.3 gives the illustrative band from published summaries; §S5.3a estimates the
same effective timescale from raw curves. The two agree where they overlap (the forest fit `t₅₀ ≈ 30 yr` matches
the illustrative representative `≈29 yr`), so the earlier forest band is now supported by a fit. Across the two
fit legs the timescale spans a wide, honest range — forest `t₅₀ ≈ 30 yr` (and `τ_r ≈ 38 yr`), fishery
`t₅₀ ≈ 5.6 yr` (and `τ_r ≈ 3.4 yr`) — with the cited soil value (`≈17–23 yr`) falling between. This spread is a
property of genuine biological differences among the ecosystem classes, and the model's `τ_g` is an *effective*
consolidation across them; the fit does not collapse them to one number, and we do not present it as if it did.
Both `t₅₀` values are rate (`ρ`)-timescales; their reading as a `τ_g` band is the stated heuristic, not a
measurement of the lag.

**What is NOT calibrated.** `b` is *not* estimated here. The forest dataset measures above-ground biomass
recovery, which is not the flow-yield coefficient; calibrating `b` would require an independent observation
operator (an FAO yield series) and remains future work. We therefore do not claim a calibrated `b`, and the
`T_b` bounds on `b` in the manuscript are not upgraded by this dataset.

### S5.3b Calibrating the provisioning-book yield `b_f` and area `A_f` (food-supply subsystem)

The regeneration-timescale legs above (§S5.3a, §S5.3) estimate the *ecological* side — how fast the capital-land
class regenerates. The food-supply (provisioning) subsystem is represented by the fast land book; its calibration
is a **different object**: the fast provisioning area `A_f` and its flow yield `b_f`. This is the
provisioning-book leg of the empirical programme, and it uses the
observation operator stated in the manuscript (§12.3): `A_f(t)` = cropland area, `b_f(t)` = crop production /
`A_f(t)`, normalised to the base year.

**Data (World aggregate, 1961–2022).** Cropland area and cereal yield/production from FAOSTAT via Our World in
Data, plus the measured NFA world cropland biocapacity and total biocapacity for the base-year anchor:

| quantity | 1961 | 2022 | growth |
|---|---:|---:|---:|
| cropland area `A_f` | 1.34e9 ha | 1.57e9 ha | 1.17× |
| cereal yield `b_f` (physical, numerator) | 1.35 t/ha | 4.21 t/ha | 3.11× |
| cereal production | 877 Mt | 3,133 Mt | 3.57× |
| world biocapacity `B` | **9.73e9 gha** | **1.21e10 gha** | 1.25× |
| NFA cropland biocapacity | **1.251e9 gha** | 3.568e9 gha | 2.85× |
| **absolute `b_f = cropland biocapacity / A_f`** | **0.93 gha·ha⁻¹·yr⁻¹** | 2.27 gha·ha⁻¹·yr⁻¹ | 2.43× |

The last three rows are fully **measured** from the NFA land-type data (`Record = BiocapTotGHA`,
`Cropland` column; world, 1961–2022), so the absolute `b_f(1961) = 0.93 gha·ha⁻¹·yr⁻¹` no longer needs the
unidentified share `α` (the cropland biocapacity *is* the cropland share of `B`) and no longer rests on an
author-supplied value. Two measures of the yield channel are used and reported side-by-side (§S5.3b): the
physical cereal sentinel (continuous, no splicing, `d ln b_f = +1.128`) and the measured NFA cropland
biocapacity per area (model units, `d ln b_f = +0.888`); both give the same qualitative conclusion.

**The decomposition (index form, robust to `α`).** Applied over 1961–2022, the identity
`d ln B = d ln b_f + d ln A_f` gives:

| channel | raw component log-change |
|---|---:|
| fast-book yield `b_f` | **+1.128** |
| fast-book area `A_f` | +0.160 |
| sum | **+1.288** |

These are the raw component log-changes the manuscript reports (§12.3, SI §S5.1); the weighted (log-mean)
contributions are +0.393 (yield) and +0.056 (area), summing to `d ln B = +0.207` exactly. The result is a
**composition premium**: `b_f` (yield) rose 3.11× while `A_f` (area) rose only 1.17×, so intensification
dominates land expansion. This is the provisioning-side expression of the model's composition mechanism — the
aggregate, and its yield component, can rise even if the capital book falls.

**Data-fetch note on the preferred numerator (aggregate crop-production index).** The manuscript's operator
says `b_f(t) = crop production / A_f(t)`. The crop-production line we fetch directly is the **cereal** series
(physical tonnes); a full all-crops aggregate would be the FAOSTAT **Gross Crop Production Index** (domain
Production Indices `QI`, item `2041` "Crops, gross", element `432` "Production Index Number", base
2014–2016 = 100). We attempted this. The World Bank transmits that series as indicator `AG.PRD.CROP.XD`, and it
was retrieved, **but it cannot be used as a continuous numerator**: the transmitted series shows several
base-period **splice discontinuities** — physically impossible single-year jumps of **+52 % in 2000, +43 % in
1993, −18 % in 1989** — which are index-rebasing artefacts, not changes in crop output. The native FAOSTAT
API (`fenixservices.fao.org`) and bulk-data host were unreachable from the analysis environment (HTTP 521 /
connection failed), so a clean, continuously-rebased `QI`/`2041`/`432` series could not be obtained. We
therefore retain the **cereal sentinel** (a physical quantity, continuous, no splicing) as the numerator and
note that, **to replace it with the aggregate index, the author should download the `QI`/`2041`/`432`,
1961–2022 table directly from FAOSTAT or the UN Data portal** and confirm the base is continuous across the
window.

**Aggregate composition attribution (measured NFA, world 1961–2022).** The decomposition of the *cropland
book alone* is exact and measured: `d ln B_f = d ln b_f + d ln A_f = +0.888 + +0.160 = +1.048` (i.e. cropland
biocapacity grew 2.85×, area 1.17×, per-ha yield 2.43×). Against the aggregate, the cropland book is the
dominant driver: world total biocapacity grew only 1.25× (`d ln B = +0.219`) while the non-cropland book grew
just 1.008× (`d ln ≈ +0.008`), so the cropland (fast) book accounts for **≈97 %** of the entire aggregate
biocapacity growth over 1961–2022. This is a direct, measured expression of the composition mechanism — the
aggregate rose chiefly through the fast provisioning book — and it is reported alongside the growth indices
rather than alone.

**Calibration caveat, and the absolute `b_f` (stated in the manuscript, restated here).** FAOSTAT yields are
physical output per hectare (t/ha), not `gha·ha⁻¹·yr⁻¹`. An *absolute* `b_f` in the model's units needs a
base-year anchor. In the manuscript this is `b_f(1961) = α·B(1961)/A_f(1961)` with the unidentified cropland
share `α` (the manuscript uses `α = 0.19`). Here we anchor directly on the **measured NFA
cropland-biocapacity** category, `b_f(1961) = CroplandBiocapacity(1961)/A_f(1961)`, which removes the
`α`-dependence — the cropland biocapacity *is* the cropland share of `B`. The NFA land-type value was supplied
as a local table (`NFA_world_landtype_biocapacity_footprint_1961_2023.csv`, `Record = BiocapTotGHA`,
`Cropland` column); the live `data.footprintnetwork.org` API remained auth-gated (HTTP 403), but the data were
obtained directly from this land-type dataset. This gives **`b_f(1961) = 0.93 gha·ha⁻¹·yr⁻¹`** and
`b_f(2022) = 2.27` (2.43×). Two measures of the yield channel are reported — physical cereal sentinel
(`d ln b_f = +1.128`) and measured NFA per-ha biocapacity (`d ln b_f = +0.888`) — which differ in level (the
NFA value embeds the ~2.5 cropland equivalence factor) and magnitude but agree in sign and dominance. Only the
**index / sign** of the yield channel and the **composition-premium sign** (`b_f >> b_{c,eff}`) are robust to
the choice of numerator; the fast-book share `w_X` ranges 0.183–0.622 (SI §S5.1), and the *absolute* `b_f`
(0.93 gha·ha⁻¹·yr⁻¹) is now measured rather than α-anchored or author-supplied.

**What this does NOT calibrate.** It says nothing about the capital book `A_c` or the regeneration timescale
`τ_g`/`ρ_c` — those require land-cover (FRA/LUH2/HYDE) and the recovery data of §S5.3a. It also does not resolve
the yield-vs-area split *within* `b_f` (that is the identifiability limit of §12.3).

**Reproducibility.** `model_sims/calibrate_bf_af_provisioning_leg.py`; figure `S1d_bf_af_calibration.png`; series
`scans/bf_af_calibration_series.csv`; NFA land-type input
`data/nfa/NFA_world_landtype_biocapacity_footprint_1961_2023.csv`.

### S5.4 Recovery metric `\mathcal{R}_c(T)` and the gate-sign asymmetry

We define an explicit recovery metric on the capital book, measured from a degraded level `A_c^deg` back
toward the healthy reference `A_c^init`:

```
\mathcal{R}_c(T) = (A_c(T) − A_c^deg) / (A_c^init − A_c^deg)
```

`A_c^init` / `P^init` are taken to be the **base-model healthy reference** — the representative member of the
one-parameter equilibrium family (the `A_c0 → long-run` attractor at `A_c0=0.9`, giving
`A_c^init=0.8225`, `P^init=1.489`); `A_c^deg=0.0513` is the degraded crash-equilibrium capital level
(capital driven to its typed floor under an over-populated start). All runs are on the **base model**
(`T_b=0`, i.e. the technology step is not applied — the configuration used for every reported result).
Reproducible: `model_sims/recovery_metric_and_tau_p_scan.py`.

**Model-fidelity note.** On the base model the capital book is bounded by `A_tot` and `A_c^min`, the reserve
`A_r` **never** approaches its floor (min `0.602`), `B` stays bounded, and the over-restoration is a modest
move along the equilibrium family (`\mathcal{R}_c` ≈ 1.07–1.27). In the *surplus-restoration* rows the final aggregate
biocapacity lies at `B≈0.70–0.91`; the no-restoration and deficit-gating rows remain near the degraded
high-`B` equilibrium (`B≈1.13–1.14`). Applying the bounded technology step `T_b` non-contingently would not be
a model result: it drives `A_c` to ≈2.39 (96% of `A_tot`), pushes `A_r` below its stated floor
(`0.049 < 0.10`), collapses `B` to ≈0.17, and yields an apparent "over-restoration" of `\mathcal{R}_c` ≈ 2.07 with
`P_end/P_init≈0.26` — an artefact of applying the step without the correct gate, not a property of the model.
We report the base-model result here.

The metric is evaluated from the **non-equilibrium post-crash state** (`A_c=0.058` near the floor, `A_f=0.6`,
`q=0.9`, `P=1.2`), because — and this is the phase-dependence the manuscript's gate claim implies — **both
gates are exactly zero at the degraded equilibrium itself**: there `R_B=1`, so `B=E` and neither `(B−E)_+`
nor `(E−B)_+` can fire. Restoration therefore needs a *surplus* to act on, and it is tested on a state that
has one. `χ_r` values are the manuscript's surplus-gated reserve→capital rate.

| Restoration policy / gate                        | \mathcal{R}_c(100) | \mathcal{R}_c(900) | A_c   | A_f   | A_r   | B     | E     | R_B(T) | P/P^init | min A_r | max A_c | D_peak |
|--------------------------------------------------|---------:|---------:|------:|------:|------:|------:|------:|-------:|---------:|--------:|--------:|-------:|
| none (`R_rc=0`)                                  | −0.00    | −0.00    | 0.051 | 1.336 | 1.113 | 1.138 | 1.138 | 1.00   | 1.39     | 1.113   | 0.057   | 0.152  |
| **surplus-gated**, `χ_r=0.02`                    | 0.69     | 0.73     | 0.612 | 1.030 | 0.858 | 0.906 | 0.906 | 1.00   | 1.11     | 0.858   | 0.612   | 0.152  |
| **surplus-gated**, `χ_r=0.05`                    | 1.08     | 1.07     | 0.875 | 0.886 | 0.738 | 0.797 | 0.797 | 1.00   | 0.97     | 0.724   | 0.885   | 0.152  |
| **surplus-gated**, `χ_r=0.10`                    | 1.28     | 1.27     | 1.030 | 0.802 | 0.668 | 0.733 | 0.733 | 1.00   | 0.90     | 0.602   | 1.092   | 0.152  |
| surplus, `χ_r=0.10` **target-capped** (`A_c^*=0.8225`) | 1.00 | 1.00 | 0.822 | 0.915 | 0.763 | 0.819 | 0.819 | 1.00 | 1.00 | 0.664 | 0.822 | 0.152 |
| surplus, `χ_r=0.10` *conversion frozen*            | 1.35     | 1.36     | 1.098 | 0.765 | 0.637 | 0.705 | 0.705 | 1.00   | 0.86     | 0.602   | 1.098   | 0.546  |
| **deficit-gated**, `χ_r=0.05`                    | 0.00     | 0.00     | 0.055 | 1.334 | 1.112 | 1.136 | 1.136 | 1.00   | 1.39     | 1.112   | 0.060   | 0.145  |
| **deficit-gated**, `χ_r=0.10`                    | 0.01     | 0.01     | 0.059 | 1.331 | 1.110 | 1.135 | 1.135 | 1.00   | 1.39     | 1.110   | 0.065   | 0.139  |
| deficit, `χ_r=0.10` *conversion frozen*           | 0.05     | 0.05     | 0.088 | 1.315 | 1.096 | 1.123 | 1.123 | 1.00   | 1.37     | 1.096   | 0.088   | 0.159  |

(`A_c^init=0.8225`, `A_c^deg=0.0513`; `\mathcal{R}_c=1` corresponds to exact return to `A_c^init`. `E=eP` is the
end-state footprint and `R_B=E/B`; every row re-equilibrates to `R_B=1`, i.e. `E=B`, so the value in the
`E` column equals that in `B` and `R_B(T)=1.00` throughout. `min A_r` and `max A_c` are over the whole run;
area conservation `|A_f+A_c+A_r−A_tot|` is `0.0` to machine precision in every row, so no
`A_r`-is-taken-below-floor or `A_c`-exceeds-`A_tot` artefact is present.)

**Reading — a *phase-dependent* gate-sign asymmetry, not "surplus works" or "deficit is false."**
- **No restoration** → no recovery (`\mathcal{R}_c≈0`); the degraded capital floor persists and the fast land supports a
  *larger-than-reference* population (`P/P^init=1.39`). The degraded state is a valid `R_B=1` equilibrium,
  just a low-capital, high-population one.
- **Surplus-gated restoration** recovers the capital book, but **at `χ_r≥0.05` it restores it *beyond* the
  reference** (`\mathcal{R}_c>1`): because the flow keeps running while `B>E`, the capital book moves up the
  one-parameter family to a *higher-capital*, *lower-biocapacity* member, and the supported population falls
  below the reference (`P/P^init` 0.97 at `χ_r=0.05`, 0.90 at `χ_r=0.10`). This is **over-restoration relative
  to the reference target**, not an ecosystem optimum, and the population change is best read neutrally: the
  path **re-equilibrates at a modestly lower supported population** (`R_B=1` at the new member,
  `P/P^init` 0.97–0.90 for `χ_r=0.05`–0.10).
- **Surplus-gated with a target cap** (`R_rc` limited so `A_c` stops at `A_c^*`) recovers *exactly* to the
  reference (`\mathcal{R}_c=1.00`) with `P/P^init=1.00` and no overshoot — the clean target-level stopping rule.
- **Deficit-gated restoration** is **not false, but insufficient at these rates**: it is the one gate that can
  act *during* the shortfall (`(E−B)_+>0`), yet the concurrent conversion channel outpaces it, so it gives
  essentially **no net recovery** (`\mathcal{R}_c≈0`). Its role is necessary-but-insufficient, and it may be swamped by
  conversion unless `χ_r` is large or conversion is capped (the frozen-deficit row still gives `\mathcal{R}_c=0.05`).

**Interpretation / policy reading.** Recovery is not automatic and the gate sign is decisive, but only in a
*phase-dependent* sense: a surplus-gated flow is the **ecologically sign-correct rewilding** (it retires land
only when the system has spare capacity, i.e. `B>E`), but it is **inert exactly during the shortfall it must
address** (and at the degraded `R_B=1` equilibrium), so it can only act once a surplus has opened up, and then
it may **over-restore** the capital book while the supported population re-equilibrates downward. Deficit-gating
is the only gate that acts *during* the shortfall, but on its own it is swamped by conversion. The clean policy
implication is therefore exactly as the manuscript's stabilising-institutional-signature point states:
**restoration should be correctly gated, correctly sized, and bounded by typed floors or a target-level
stopping rule** — and a surplus-gated flow should be *paired with a conversion ceiling or target cap* rather
than left unbounded.

| Restoration policy                 | Expected/measured role                                      |
|------------------------------------|-------------------------------------------------------------|
| no restoration                     | baseline failure — capital stays at floor, population large  |
| deficit-gated only                 | acts during shortfall but may be swamped (≈no net recovery)  |
| surplus-gated only                 | inert during shortfall; later restores, may over-restore     |
| surplus-gated + conversion freeze  | over-restores further and *raises* `D_peak` (0.546)          |
| surplus-gated + target cap         | **clean recovery to reference, `\mathcal{R}_c=1.00`, `P/P^init=1.00`** |

**Why conversion-freeze *raises* `D_peak` (0.152 → 0.546), and how `A_f` falls despite the freeze.**
Freezing conversion sets `u_c=0`, so the fast-land-release channel cannot close the deficit. The
surplus-gated restoration then over-supplies `A_c` (a lower-yield book), so aggregate `B` stays
lower while the population re-equilibrates only slowly (`τ_p`); `E>B` therefore persists for a
larger fraction of the run (measured `frac(E>B)` rises from 0.10 to 0.23), and net debt accrues
faster (mean positive `dD/dt` rises from 0.0009 to 0.0013), so `D_peak` more than triples. `A_f`
can still fall under the freeze because `A_f` is replenished only by reserve→fast maintenance
`μA_r` and drained by retirement `η_fA_f`; restoration drains `A_r→A_c`, so `A_r` shrinks and
`μA_r` can no longer sustain the reference `A_f`, which settles lower (to the point where
`μA_r=η_fA_f`).

**Added value.** `\mathcal{R}_c(T)` — reported together with `P_end/P^init`, `min A_r` and `max A_c` (not alone) —
converts the qualitative gate-sign claim into a measured trade-off, and the target-capped row shows the exact
bound that turns "recovers but over-restores" into "recovers to the reference."

### S5.5 `τ_p`-extended delay scan (to `τ_p = 2000` yr)

The delay scan is extended to `τ_p ≳ 250` yr. Reproducible:
`model_sims/recovery_metric_and_tau_p_scan.py`. (a) recover/collapse fraction vs `τ_p` (grid over
`A_c0 ∈ {0.40,0.70,1.00,1.18}`, `P_0 ∈ {0.5,…,3.0}`; crash = `min A_c ≤ A_c^min`), `τ_g = 20`, `χ_r=0`;
(b) long-horizon (`T=3000` yr) probe for a limit cycle / Hopf, measured as the peak-to-peak `P` amplitude in
each quarter of the run.

**(a) Recover/collapse fraction is flat in `τ_p`.**

| τ_p (yr) | 25 | 100 | 200 | 300 | 500 |
|---|---:|---:|---:|---:|---:|
| recover fraction | 0.833 | 0.833 | 0.833 | 0.833 | 0.833 |

The boundary is set by demand `P_0` (hence `E`), **not** by the demographic lag `τ_p` — the same conclusion
the manuscript reports for `τ_g`, now confirmed for `τ_p` across an extended range up to 500 yr (and the
24-cell grid stays 20/24 = 0.833 throughout).

**(b) No sustained limit cycle / no Hopf up to `τ_p = 2000` yr.** The `P`-amplitude by quarter:

| τ_p (yr) | Q1 | Q2 | Q3 | Q4 |
|---|---:|---:|---:|---:|
| 25 | 0.491 | 0.000 | 0.000 | 0.000 |
| 300 | 0.572 | 0.000 | 0.000 | 0.000 |
| 500 | 0.565 | 0.007 | 0.000 | 0.000 |
| 1000 | 0.182 | 0.572 | 0.000 | 0.000 |
| 1500 | 0.182 | 0.000 | 0.572 | 0.000 |
| 2000 | 0.182 | 0.000 | 0.565 | 0.007 |

The single recovery-overshoot pulse keeps a **bounded** amplitude (≈0.57) and simply **moves later in time**
as `τ_p` grows (Q1 → Q2 → Q3), then settles. There is **no** growing oscillation, hence **no Hopf** and **no
sustained boom–bust limit cycle** at any `τ_p` up to 2000 yr. This extends the manuscript's
"single recovery-overshoot pulse, no-Hopf, no-limit-cycle" negative result to the full demographic-delay
range and to `τ_p` far beyond the baseline `25` yr.

**Numerical robustness.** The bounded pulse is not a step-size artefact: at `τ_p=2000` the Q3 amplitude is
`0.565` (`dt=0.1`), `0.514` (`dt=0.05`), `0.484` (`dt=0.02`) — bounded and monotonically *decreasing* as the
step is refined, so there is no growing oscillation and no Hopf regardless of resolution.

**Summary of the two supplementary results.** `\mathcal{R}_c(T)` turns the gate-sign claim into a measured metric with an
explicit population trade-off; the `τ_p`-extended scan confirms the recover-boundary is demand-set (not lag-set)
and that no limit cycle appears.

---

## S6. Mapping of the falsifiable predictions to manuscript sections

The manuscript's §6 (Falsifiable predictions) states **seven** predictions, each framed against the two-book
series (`B`, `A_c`, `A_f` and the land-cover/yield proxies) rather than the one-stock aggregate. Predictions
1–4 and 6 are dynamical (onset, duration, response to a regime index, recovery); prediction 5 is the
regime-conditional (fold) statement; prediction 7 is the observational (identifiability) one. The table maps
each to the manuscript section that establishes it.

| # | Prediction | Primary section | Supporting sections |
|:--:|---|---|---|
| 1 | The masking signal is `\dot A_c < 0` with `R_B ≲ 1` (aggregate at or below demand while ecological capital falls) | §6, §4.4 | §2.2, §5 |
| 2 | The duration of the composition window is set by `Δb_conv` and the demand deficit, not a fixed horizon | §6 | §4.1, §4.3 |
| 3 | No critical slowing precedes the drawdown (leading eigenvalue constant ≈ −0.0537 yr⁻¹; no CSD precursor) — a *negative* prediction | §6, §4.3 | §8 |
| 4 | The collapse trigger is a demand threshold in `P_0` (hence `E`), essentially flat in `τ_g` — not a regeneration-delay threshold | §6 | §4.2, §5, §8 |
| 5 | The capital-land catastrophic shift (fold) does not exist; the drawdown is a floor collision — a *negative* structural statement | §6, §4.1 | §4.2, §5, Tables `tab:basin`, `tab:conv` |
| 6 | Recovery requires an explicit restoration flow with a gate whose sign matters | §6, §12.2 | §4.3 |
| 7 | The composition step is not identifiable from aggregate biocapacity (observational programme) | §6, §12.3 | §4.4, §5 |

**The two masks.** *Composition mask:* `B` rises while `A_c` falls (requires a productivity contrast
`b_f > b_{c,eff}`). *Liquidation mask:* `E` steady while `A_c` falls (requires none). These are distinct and
the discriminating observable is which holds.

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

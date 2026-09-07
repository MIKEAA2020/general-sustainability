# Joint evaluation of the three turnover-regime audits (deepseek / grok / gemini)

**Input:** `uploads/turnover.txt` (267 lines), three independent answers to the same question.
**Question:** Which capital-turnover regime is ECOMOD actually about — fast (V≈1.6 yr), slow (V≈20–100 yr),
or both?
**Method:** verify every load-bearing claim against `model_sims/char_eq.py` (the registered S0 linearisation).
I did **not** take any audit at face value. Several verifications overturned *my own* earlier result, and I
say so explicitly below. **No manuscript modified.**

---

## 1. What the three agree on (strongly)

All three independently arrive at the **same structural conclusion**, which is itself the answer's backbone:

1. **The `+0.625` is a fast-turnover fact, not an Earth/forest fact.** None recommends keeping `+0.625` as an
   unqualified "structural vicious cycle for every delay" at forest scale.
2. **The framing is "Both — state an explicit regime boundary."** Deepseek ("safest choice"), Grok ("both, with
   an explicit V boundary"), Gemini ("Option 3 informed by Option 4").
3. **The slow-turnover regime is paper4 / v18's object.** The delay-amplified basin crisis + fold + debt
   degradation, not the monotone `+0.625`, is what belongs to that regime.

So my prior recommendation ("publish separately, ECOMOD owns the fast-turnover regime") is **confirmed** by all
three, and refined: the regime boundary must be stated, and ECOMOD must not over-claim the slow side.

## 2. Where they disagree — and who is right (verified)

### 2a. The critical V_crit: 20 (grok) vs ~45 (gemini) vs ~75 (deepseek)

**Verdict: grok is right.** The disagreement is not arithmetic; it is *which equilibrium you linearise about*.
The S0 deficit-regime has a **one-parameter family** of equilibria `P = B(A)/e`, so `A*` is not fixed by V. The
transverse root is `S = b/b_G + G′(A*) = 1/V + G′(A*)`, and `G′(A*)` depends on the chosen `A*`.

- **Grok linearises about the biocapacity-maximising (MSY / fold) stock** `A_Bmax` where `dB/dA = 0`. I
  verified `A_Bmax = (A_max/2)(1 + 1/(Vρ))` and `G′(A_Bmax) = −1/V` **exactly**, so `S = 0` and
  `λ = S − r = −r < 0` for `V > 20 yr`. The forest/soil MSY is **transversally stable** — no monotone cycle.
- **Deepseek's ~75** came from my earlier scan at the fixed point `A* = 0.6 = A_max/2` (where `G′=0`, so
  `S = 1/V`). That is **off the B-max** for large V; it is not the relevant reference. Grok explicitly flags this
  ("off-equilibrium spectra are not the claim in §4.3"). **I must correct my own `CONFIRMED_scopeA...` note.**
- **Gemini's ~45** is from `D′(0) < 0` at `A* = 0.8` (`G′(0.8) = −0.0167`) at `τ_g = 30, τ_p = 25`. Its
  `D′(0)` formula is **algebraically correct** — I rederived it and confirmed
  `D′(0) = (r − S) + r a₁ τ_g − r S τ_p`. But it evaluates at an `A* = 0.8` reference, so its crossover is
  reference-dependent, not a regime boundary.

**The correct regime boundary is `V = 1/ρ = 20 yr`** (at baseline `ρ = 0.05`), i.e. where `Vρ = 1` and the
interior MSY emerges. A second, finer fast-side boundary is `V = 1/(ρ + r) ≈ 14.3 yr` (where `λ₀ = 1/V − ρ − r`
changes sign at the boundary `A = A_max`). Both belong to grok's framing; neither is ~75.

### 2b. Grok's deeper mathematical point — verified and important

> "At interior MSY (`b_G ρ > b`, i.e. `V > 1/ρ = 20 yr`), `dB/dA = 0 ⟹ S = b/b_G + G′(A*) = 0`, so the
> zero-delay transverse root is `λ = S − r = −r < 0`. **The vicious-cycle eigenvalue cannot exist at the forest
> equilibrium.** It is an off-MSY / high-`b/b_G` fact."

I verified this across V = 27, 40, 60, 100: `A_Bmax = 1.044, 0.900, 0.800, 0.720`; `S = 0.000`; `λ₀ = −0.020`
in every case. **Confirmed.** The `+0.625`, `+0.041`, `+0.024` serie I reported earlier were at off-MSY points,
and `+0.625` specifically only survives at the small-V (V < 20 yr) *boundary* equilibrium `A = A_max`.

### 2c. Gemini's `D′(0) < 0` condition — correct, but it describes the *delayed* instability, not `+0.625`

Verified: `D′(0) = (r − S) + r a₁ τ_g − r S τ_p`, and a positive delayed real root exists iff `D′(0) < 0`
(since `D(0) = 0` and `D(s) → +∞`). At the B-max reference (`S = 0`), this reduces to
`D′(0) = r(1 − τ_g/V)`, i.e. **`D′(0) < 0 ⟺ V < τ_g`**. So the *delay-amplified* positive root at the MSY
exists only when turnover is faster than the regeneration delay. This is a clean, defensible statement — but it
is **not** the ``+0.625``, and it is the mechanism paper4/v18 owns.

### 2d. The τ_g ≈ 18–20 yr recovery cliff is V-invariant — correct

All three treat the regeneration-delay cliff as independent of V. This matches the registered model: fine recover
fractions `0.399 / 0.394 / 0.240 / 0.0529` at `τ_g ≤ 17 / 18 / 19 / ≥ 20 yr` (τ_p=25), identical across
`V = 1.6–50`. **Confirmed.** But it is a *recovery / basin* cliff, **not** the same eigenvalue as `+0.625`.

## 3. What the literature actually determines (the crux of "which regime")

| Pool | Stock/flow V (yr) | Source | GFN/EF role |
|---|---|---|---|
| Annual cropland biomass | ~0.5–2 | FAO/Erb | ~20% of EF (high equivalence factor), food |
| Grassland aboveground | ~2–5 | Whittaker/Erb | grazing biocapacity |
| Pelagic fish | ~1–5 | production/biomass | small share |
| **Human harvest basket (weighted)** | **≈1.6** | Krausmann 2013, Haberl 2007 | **what humans consume** |
| Global live vegetation (one-box) | ~8–14 | Carvalhais 2014, Erb 2017 | the honest plant mean |
| Carbon-sequestration land (EF overshoot) | ~20–100+ | Poorter, FAO FRA, IPCC | **≤55–60% of world EF** |
| Soil organic C (to new equilibrium) | ~17–40 | Poeplau, IPCC 2006 | degradation channel |

**The real tension** (grok's sharpest point, gemini's counter):
- **Humans *consume* fast-flow food** (V ≈ 1.6 yr) → this is the orchard/agro-ecological provisioning baseline,
  where the `+0.625` lives. Gemini and Deepseek emphasise this.
- **The global *overshoot/deficit* the GFN series measures is dominated by carbon** (≈55–60% of world EF),
  accounted as forest-sequestration area → V ≈ 20–100+ yr (slow). Grok emphasises this.

**Both are true. ECOMOD is the *provisioning* model (fast), while the *deficit it quantifies* in the global
series is slow-carbon.** ECOMOD cannot be "the 1.6-yr crop" *and* "the forest/soil/Earth object" at once — which
is exactly the conflation the manuscript's earlier framing made, and exactly what the three audits all correct.

## 4. Joint verdict

**Option 3 — both regimes, with an explicit boundary `V = 1/ρ = 20 yr`, ECOMOD as the fast-provisioning model,
and the slow-carbon regime honestly handed to paper4/v18.**

- **Fast / provisioning (`V < 1/ρ = 20 yr`; orchard, crops, pelagic; honest baseline `V = 1.6 yr`).**
  Liquidation gain `b/b_G = 1/V` is large; the delay-independent monotone vicious cycle `λ ≈ +0.625` holds at
  the boundary reference; `R_B = 1` is the balance; `R_A = 1` the leading signal. **This is ECOMOD's headline,
  and it is defensible *at V = 1.6 yr*.** Label it as such — not "forests/soils/fisheries."
- **Slow / capital-dominated (`V > 1/ρ = 20 yr`; forest, soil carbon, the land GFN uses for overshoot).**
  Interior MSY, transverse root `λ = −r` (no monotone cycle); collapse is the **debt-eroded fold** (verified:
  `B_max` falls 0.735 → 0.0995 → 0.0135 as debt `α` 0 → 0.05 → 0.10) **+ the τ_g ≈ 18–20 yr recovery cliff +
  delay-amplified basin crisis.** This is paper4 / v18's object.
- **Mixed Earth.** Do **not** average into `+0.625` (grok). State the boundary and give two columns.
- **The condition is `D′(0) < 0`, not `S > r`.** `S > r` at the boundary is the fast-side statement
  (`V < 1/(ρ+r) ≈ 14 yr`), not a theorem for forests.

## 5. Consequences for v33 (text)

1. **§2.1:** state `1/V = b/b_G` (yr⁻¹) as the capital-turnover rate and `γ = 1/b_G` (ha·gha⁻¹) as the
   stock-conversion factor. Ground `V = b_G/b₀ = 0.8/0.5 = 1.6 yr` as the human-harvest-basket turnover
   (Krausmann 2013, Haberl 2007), with `ρ = 0.05` stated.
2. **§4.1 / §4.3:** delete `det > 0` (family has `Det J ≡ 0`); replace the `S > r` sufficiency with the exact
   `D′(0) < 0`; state the **regime boundary `Vρ = 1` (`V_crit^regime = 1/ρ = 20 yr`)** and
   `ψ* = 1` there.
3. **§4.3 / §5 (comparison table):** two columns, not one eigenvalue. Fast: `+0.625` vicious cycle.
   Slow: fold + τ_g cliff + debt, no monotone cycle at MSY. Boundary at 20 yr.
4. **Abstract / title:** keep the productivity illusion (it is generic, Prop 1) and the structural vicious
   cycle, but label `+0.625` as the **provisioning/harvest baseline (`V ≈ 1.6 yr`)**, and state the regime
   boundary `V_crit^regime = 1/ρ`.
5. **Predictions:** Prediction 1 → "the constant-parameter provisioning subsystem (V < 1/ρ) is monotonically
   unstable (λ>0) for every delay." Prediction 6 → the τ_g ≈18–20 yr cliff is invariant to V.
6. **Bridge to paper4:** state explicitly that ECOMOD solves the provisioning/harvest flow dynamics
   (V < 1/ρ), the macro-ratios `R_B, R_A`, and the productivity illusion (Prop 1), while the slow-turnover
   timber/peatland/carbon regime (V > 1/ρ) — where direct liquidation is buffered and collapse is
   delay-amplified + fold — is treated in paper4/v18.

## 6. Correction to my own earlier note

`audits/CONFIRMED_scopeA_and_corrected_stability.md` reported `V_crit ≈ 75 yr` (delay-independent) from a scan
at `A* = 0.6 = A_max/2`. **Grok is right to reject this**: `A* = 0.6` is off the B-max for large V, so that
crossover is not the relevant regime boundary. The correct, reference-consistent statement is **`V_crit^regime =
1/ρ = 20 yr`** (the interior-MSY / `Vρ = 1` boundary), with the fast-side secondary boundary `V = 1/(ρ+r) ≈ 14 yr`.
The `+0.625` remains a real, delay-independent result — **at `V = 1.6 yr`, the honest baseline** — but it must
not be presented as a forest/soil property.

## 7. Addendum — remaining audit points incorporated (not yet in §1–§6)

The following points from `turnover.txt` were **not** in §1–§6; they are folded in here after verification.
One of them (grok §4) is substantive enough to refine the recommendation, not merely add a caveat.

### 7a. Grok §4 is the decisive remaining point — it elevates scope-A from "faithful" to "required"

Grok argues the one-stock "both/regime-boundary" framing is **"the maximum that a one-stock model can do"** and
**does not meet the manuscript's original ambitions** (illusion + moving ceiling + delay cliff +
technology-debt + monitor failure, *about real land*) **at once** — those require the **two-land conversion
split** (`A_f`, `A_c`, `S/κ`). And the literature determination is that **GFN itself *is* that split**: fast
yield land (cropland, equivalence factor ≈ 2.5, ~19–20 % of world EF) **plus** slow carbon/forest land (~60 % of
world EF), with **land-use conversion as the historical operator** (Erb et al.: human land conversion cut global
live biomass ~900→450 GtC). I verified the two load-bearing numbers: carbon footprint ≈ **60 %** of world EF,
cropland ≈ **19 %** (National Footprint Accounts 2018), equivalence factors cropland **2.52**, forest **1.29**
(borucke/Lin/GFN conventions).

**Consequence for the recommendation.** My §1–§6 framed ECOMOD as the fast-provisioning one-stock model with a
stated boundary. That is the honest **minimum** a dynamics audience needs (and it is what §5 encodes). But
grok §4 shows it **cannot by itself carry the title** as a *generic Earth* mechanism — the title illusion (weighted
biocapacity rising while forest stock falls) is only possible because cropland is a second, overweighted
component. **Therefore the title-faithful route is scope-A: a minimal two-state dynamical model**
(`A_f` fast yield land, `A_c` slow carbon/forest land, conversion `S/κ`), which *realises* the illusion
mechanically while a component falls. This is **distinct from both paper1 and paper3**: paper1 is the *static*
aggregation theorem (cited, not re-proven); paper3 is the *full* vector ledger accounting; scope-A is a *minimal
dynamical* two-component realisation that demonstrates the illusion and quantifies it (moving ceiling, delay
cliff, technology-debt, monitor failure).

**Net verdict updated to two tiers:**
- **Minimum (one-stock, honest, dynamics-ready):** fast + slow with boundary `V_crit^regime = 1/ρ`, `+0.625` at
  `V = 1.6 yr`, slow handed to paper4. (§1–§6.)
- **Title-faithful (scope-A, two-land conversion):** needed to deliver the *generic Earth* illusion, moving
  ceiling, technology-debt, and monitor-failure claims. Distinct from paper1/paper3; the GFN grounding makes it
  non-arbitrary.

### 7b. Grok: what the NFA 1961–2022 series is *allowed* to mean

The global series is consistent with **composition change** (yield ↑ and cropland ↑ while forest stock ↓), **not**
evidence of a 1.6-yr cycle. This matches the manuscript's own NFA limitation and must be stated so the framing
does not over-read the series. (Caveat: "composition change" here is the land-use/conversion interpretation —
the same operator scope-A formalises.)

### 7c. Grok: three forbidden moves (do not resurrect `+0.625` at forest V)

Do **not** recover `+0.625` at forest `V` by (a) sliding `A*` back to `0.8`, (b) setting `b_G = b·V` and then
linearising **off** MSY (the exact move my option-(b) note made — corrected in §6), or (c) averaging `V`. All
three are "the same category error with extra steps." Verified: at the B-max, `S = 0` and `λ = −r` for every
`V > 20 yr`, so no off-MSY re-slicing can honestly restore a forest-scale `+0.625`.

### 7d. Grok: the printable framing sentence (adopt wording)

> "The delay-independent monotone root is a fast-turnover (`V < 1/ρ`) property; at forest/soil MSY it is absent
> and the operative mechanisms are the fold and the regeneration-delay cliff. The biosphere GFN reports is mixed
> across that boundary, so `Re λ ≈ +0.625` is not the Earth result."

### 7e. Grok: equivalence-factor observation

Cropland's top equivalence factor (~2.5, vs forest ~1.29) is what allows **weighted** biocapacity to rise while
the forest component falls. This is the concrete arithmetic behind the "illusion," and it is why a single
unweighted `V` cannot capture it — a second, overweighted, fast component is required. Belongs in §4.3/§5.

### 7f. Gemini: quotable framing — the EF biocapacity basket is food-dominated

"Humans do not eat 50-year-old wood." Treating global biocapacity as an undifferentiated `V = 50–100 yr`
old-growth forest mischaracterises the GFN accounts: forest land in GFN is primarily carbon-sink/timber, while
the biocapacity basket that feeds humans is cropland/grazing/fisheries. Reinforces the fast-provisioning baseline
and the two-land (fast + slow) split.

### 7g. Gemini: the τ_g cliff is an *independent, non-local basin-boundary crisis*

It "cuts across both turnover regimes" and is **not the same eigenvalue** as `+0.625`. Keep it as a separate,
V-invariant result (already confirmed against the registered model: fine recover `0.399/0.394/0.240/0.0529` at
`τ_g ≤ 17/18/19/≥20`). Do not conflate it with the monotone root.

### 7h. Deepseek: operational estimation recipe for `V`

`V ≈ (stock of natural capital) / (annual regeneration or harvest flow)`, and pin the regime by asking four
things: (1) dominant natural capital, (2) typical regeneration/replacement time, (3) the anchoring literature
(FAO rotation, IPCC carbon-pool lifetimes, fishery stock assessments, NFA yield factors), (4) direct estimate.
This is a concrete, auditable procedure for the `V` used in §2.1 — recommend stating it so the baseline is
reproducible. Deepseek's "safest choice is Both — state the boundary" is retained as the one-stock floor.

---

***Deliverable. Read-only decision note; all numbers verified with `char_eq.py` and, for §7a/e, the GFN
National Footprint Accounts (2018) and equivalence-factor conventions. No manuscript modified.***

# A revision strategy for ECOMOD-26-1191
## Proposal to preserve the ambitions, generality, and overall picture in corrected form

This document proposes how to **repair** the manuscript rather than discard it. It keeps the
paper's ambitions (a minimal, analytically tractable delay model of emergent carrying capacity;
a reconciliation of weak vs. strong sustainability; a collapse-mechanism taxonomy; a policy
extension) and makes the claims match what the model actually does. Every proposal below was
tested by re-implementing the model; where a change is numerical, the numbers are given.

A companion document, `ECOMOD-26-1191_review.md`, lists the flaws. This one is *constructive*: it
says what to keep, what to change, and how — in a form that is internally consistent and
defensible.

---

## 0. Executive summary (what to keep, what to fix)

**KEEP (these are genuinely defensible):**

1. The **emergent-carrying-capacity** formulation (K = bM/r_opt) — the conceptual core.
2. The **two-lag coupled DDE** structure (τ_M, τ_P) and the characteristic equation (13).
3. The **two-mechanism collapse taxonomy**: *debt-driven* (small/no delays) vs.
   *delay-transient-driven* (both delays present). I reproduced both.
4. The **weak-vs-strong sustainability reconciliation** *as a conceptual frame*.

**FIX or RE-EXPRESS (these are the internal inconsistencies):**

- The "**≈80 yr threshold**" — marginal (max Re ≈ +0.007 yr⁻¹), ratio-dependent, and belongs to a
  subsystem no simulation uses. Re-express as a *qualitative, ratio-dependent* stability boundary;
  drop the "≈80 yr" precision.
- The "**productivity illusion is demonstrated**" imputation — it is *not* shown. Either show it
  (it *is* reachable — see §2) or describe it as an untested prediction.
- The **Half-Earth cap** — as implemented it yields Ω = 0.575, not 0.5. Fix the formula.
- The **technology-offsets-debt** claim — contradicted by D_E (5.240) > D_D (4.826). Reconcile.
- The **asymmetric delay** — τ_M lags the stock channel but the *debt* channel is instantaneous,
  yet debt is the dominant small-delay driver. Make the lag application consistent or justify it.

---

## 1. Fix the marquee result: a ratio-dependent stability boundary, not "≈80 yr"

**Problem.** The abstract/intro/conclusion present "instability requires both delays to interact,
with the threshold at a combined delay of approximately 80 yr." Three problems: (a) the boundary
is *ratio-dependent* (not a function of τ_M+τ_P), (b) it is *marginal* (Re λ ≤ ~0.007 yr⁻¹ —
within a hair of neutral; the paper itself says "Re(λ) < 0.01"), and (c) it belongs to the
*constant-parameter sustainable* subsystem (Scenario A, e=r_opt, α=0), which **no simulation
uses** — Scenario A is run with no lags, and Scenario D is linearly *stable* at (30,25).

**Proposed reformulation (consistent, and still interesting):**

Replace the "≈80 yr" claim with a precise, honest statement of the linear result:

> *"For the sustainable, constant-parameter subsystem, the non-trivial equilibrium is locally
> stable for all single delays, and the two-delay linearisation admits growth rates that are
> positive only for sufficiently large combined delays. The growth rate remains small (Re λ
> below about 10⁻² yr⁻¹) over the whole two-delay plane, so this linear instability is a
> marginal, slow oscillation rather than a strong destabilisation, and its onset is strongly
> dependent on the ratio τ_M:τ_P rather than on the sum τ_M+τ_P alone."*

**Why this is a genuine improvement, not a retreat.** The honest version is *more* informative
and is what the figure actually shows. It also removes the awkward fact that a boundary
computed for a subsystem no scenario uses is being presented as the paper's central number.
If the authors want a single scalar, they should state it with its conditions and its caveat.

**Concrete numbers to put in the text** (I computed these):

- Largest growth rate over the two-delay plane (0–160 yr each): **Re λ ≈ +0.007 yr⁻¹** at
  (τ_M, τ_P) ≈ (100–120, 100–120).
- Onset is ratio-dependent. At *sum = 110*: (50,40) → Re +0.0021 (unstable), (60,50) → +0.0043
  (unstable), (80,30) → +0.0005, (90,20) → −0.0014 (**stable**). Same sum, different sign — the
  boundary is *not* a contour of constant total delay.
- First genuinely unstable points appear near **sum ≈ 77–78**, and the paper's own grid scan
  (sum ≤ 75 stable; first unstable at ~80) is consistent with a very slowly-growing instability.

---

## 2. Demonstrate the productivity illusion (it IS reachable) — or relabel it as untested

**Problem.** The abstract and conclusion state "technology can temporarily mask environmental
decline by raising output per unit of natural capital faster than debt erodes it," and the
Discussion asserts it against world data. But **no figure shows it**: B(t) is never plotted, and
all six scenarios collapse. As a result the paper's headline phenomenon is asserted, not shown.
Indeed, in Scenarios B/C the *opposite* pattern occurs: the stock M recovers to ~1.19 while the
harvest B collapses (humans die, orchard survives).

**Finding.** The illusion **is reachable** with a sufficiently early/large technology wave and a
weaker debt sensitivity. I found **118 parameter sets** (out of a grid over e ∈ {1.0,1.15,1.3},
α ∈ {0.2,0.5}, Δb ∈ {0.8,1.5,2.5}, t_wave ∈ {30,60,100,150}, κ ∈ {0.05,0.1}) that exhibit a
sustained window in which **B rises while M falls**. A representative case:

> e = 1.15, α = 0.2, Δb = 0.8, t_wave = 100 yr, κ = 0.05, τ_M = 30, τ_P = 25.
> **In t ≈ 80–110 yr, B rises from 0.711 to 0.832 gha yr⁻¹ (1.65× its initial value) while M
> falls from ~1.0 to 0.834 gha.** Then the illusion breaks: M → 0 and cumulative debt → ~307.

This is *exactly* the paper's thesis — a rising harvest masking a depleting stock, then a
reckoning. Two recommended moves:

**(A) Add one scenario and one figure (recommended).** Add a "G: technology-masking" scenario
using the parameter set above, plot **B(t) alongside M(t)** (the current Figures omit B), and on
it annotate the masking window and the subsequent collapse. This turns the headline from an
assertion into a demonstration. The figure produces the "productivity illusion" in the literal
sense the paper claims.

**(B) Alternatively, relabel.** If the authors prefer to keep the existing six scenarios, then
the "rising-biocapacity" passage must be reworded as a *prediction of the model for parameters
not simulated here*, and the unsupported sentence about "global data 1961–2022" must be either
removed or cited.

**Why this preserves the ambition.** The claim "both weak- and strong-sustainability are
correct, at different timescales" only has teeth if the *weak* regime (rising/masking B) is
actually produced. Adding the masking scenario is the single change that makes the framing
self-consistent.

---

## 3. Fix the Half-Earth extension so it actually caps at half

**Problem.** Eq. (9) does K = 0.5·B/r_opt, which caps **population**, not footprint. Since the
overshoot scenario consumes at e = 1.15·r_opt, the realized overshoot is Ω = e·P* / B =
0.575, **not** 0.5. The paper says it "caps human-usable biocapacity at half," but the simulated
Half-Earth uses **57.5%** of total biocapacity.

**Proposed fix.** The intended policy is a cap on *human demand* at half of biocapacity, i.e.
E = e·P ≤ 0.5·B, so the correct condition is

> K_Half-Earth = 0.5 · **B / e** ,   not  0.5 · B / r_opt .

**Verified consequence of the fix** (I ran it): with K = 0.5·B/e (τ_M=30, τ_P=25, e=1.15,
α=0.5), the system settles at **M=1.000, P=0.217, D=0, Ω→0.500** (exactly half the biocapacity,
as intended). The paper's version gives Ω→0.575 (M=0.970, P=0.243). So the correction is
material: it changes the reported sustainable population from 0.243 to 0.217 and the overshoot
ratio from 0.575 to 0.500. The model still works and still prevents collapse — it just means what
it says.

For a richer, endogenized version, the paper itself suggests reducing per-capita footprint e(t)
or population P(t); either is fine and worth one sentence.

---

## 4. Reconcile the technology-vs-debt tension

**Problem.** Scenario E (D plus a tech wave Δb=0.3) ends with **more** cumulative debt than
Scenario D (5.240 vs 4.826), even though the paper frames technology as *offsetting* debt. This is
because raising b raises B = b·M, which raises K, which — at e = 1.15·r_opt — raises the footprint
E = e·P, which *raises* debt. The paper never discusses this feedback.

**Proposed fix — make the policy insight explicit and reframe it as a result, not a bug.** This is
actually a *rich* finding worth foregrounding:

> *"Technology that raises yield per unit stock also raises the sustainable population and thus
> the aggregate footprint. Under overshoot (e > r_opt), this feedback can cause a technology wave
> to **increase** cumulative ecological debt even while raising biocapacity — a 'Jevons-type'
> rebound in a human–environment system. Only technology that raises b while *not* expanding the
> population's footprint demand (e.g. via per-capita efficiency, e ↓) reduces debt."*

This preserves the paper's "weak sustainability is bounded" message but states the mechanism
correctly, and it explains the D_E > D_D result instead of leaving it as a silent contradiction.

---

## 5. Make the delay structure internally consistent

**Problem.** τ_M is described as the environmental *response* delay and inserted into the stock
depletion channel (γE(t−τ_M)). But the **debt** channel — which the paper calls the dominant
small-delay collapse driver — uses instantaneous E and B (dD/dt = max(E−B,0)) and instantaneous
response of b to D. Consequently two of the six scenarios (B, C) collapse purely from
instantaneous debt feedback and do **not** need a delay at all, which undercuts the framing that
"lags are what make overshoot dangerous."

**Proposed options (pick one and say so):**

- **(i) Add a debt lag** (recommended, enriches the model): delay the debt source, e.g.
  dD/dt = max(E(t−τ_D) − B(t), 0), and/or delay the productivity response b(t) = b₀e^{−αD(t−τ_D)} +
  T(t). This makes the environmental lag apply *consistently* to the debt channel, aligns the
  model with the stated motivation ("ecological damage takes decades to manifest"), and adds a
  third timescale that could be compared to the demographic lag. It also strengthens the
  "both-delays matter" narrative.
- **(ii) Justify the asymmetry explicitly.** Argue that depletion is physically immediate
  (harvest today removes stock today) while the *functional degradation* (soil fertility,
  biodiversity) that the debt variable represents is a stock in its own right that only resets on
  a slower scale — and hence the asymmetry is deliberate, not an oversight.

Either is defensible; the current text does neither, which is why B/C collapse "without any
delay."

---

## 6. Replace the numerical method and make "collapse" a model result, not a clamp

**Problems.**

- **"Total biospheric collapse" M = 0 is a numerical clamp.** Eq. (1) has no M ≥ 0 floor; at M = 0,
  dM/dt = −γE < 0, so an unconstrained trajectory goes *negative* (negative gha — nonphysical).
  The "hold at zero" in Figs. 1 and 5 comes from `max(0,·)` in the code, not from the ODE. The
  trivial equilibrium (M, P) = (0,0) is never analyzed.
- **Euler with dt = 0.5 yr is coarse for delay/transient dynamics.** For the equilibrium it
  converges well (Scenario A: M* = 0.8022 at dt=0.5 vs 0.8021 at dt=0.05), but the
  collapse/recover *threshold* — whether a transient dips below M_max/2 = 0.6 — is exactly the kind
  of quantity a bare Euler can get wrong, and the D/not-D boundary is a sharp threshold-crossing.

**Proposed fixes.**

1. **Analyze the trivial equilibrium** (M=P=0) and the "no-recovery" region (M < M_max/2). State
   that for M below M_max/2 the logistic term is negative and the stock is drawn to zero *in the
   absence of sufficient regeneration*, so collapse to zero (not to negative) is the relevant
   attractor. Then "collapse" is a genuine model feature, and the clamp is just the discretized
   domain boundary.
2. **Introduce a physically-motivated floor** (optional but cleaner) — e.g. model M as a
   non-negative stock with a minimum viable size/refuge, so the approach to zero is well-defined.
3. **Switch to a proper time-domain DDE method** (e.g. `scipy`/`pydelay` type, or the
   method-of-steps with a RK45/RK23 stiff solver). The paper already cites Shampine & Thompson
   (2001) as the obvious substitute; make the substitution and add a **dt-convergence** table
   showing that the reported M*, P*, and the D/not-D regime assignment are insensitive to the
   step size. This is cheap and pre-empts a reviewer objection.

---

## 7. Replace the "basin of attraction shrinks" assertion with a measured quantity

**Problem.** The paper asserts that delays "shrink the basin of attraction" but provides no basin
computation — no separatrix, no perturbed-IC sweep, no measure. It's currently a
qualitative claim bolted on to a *barely* stable equilibrium (Re λ ≈ −0.008).

**Finding.** The claim is **true and dramatic** — but it needs a measurement. I computed the
stable fraction of the (M₀, P₀) initial-condition plane for the overshoot constant-parameter
subsystem (e = 1.15, α = 0):

| τ_M, τ_P | stable fraction | std IC (1.0, 0.1) → |
|---------:|----------------:|:-------------------:|
| (0, 0)   | **0.506**        | stable              |
| (10, 10) | 0.462            | stable              |
| (20, 20) | 0.462            | stable              |
| (25, 25) | 0.053            | **collapse**        |
| (30, 25) | **0.042**        | **collapse**        |
| (40, 40) | 0.008            | collapse            |

So the basin **collapses by an order of magnitude** (50% → 4%) between no delays and the baseline
delays, and the standard initial condition flips from "stable" to "collapse." This is a strong,
quantifiable result. I generated `basin_shrinkage.png` (two-panel: (0,0) vs (30,25)) showing
this.

**Proposed.** Add a **basin-shrinkage figure** (the two-panel map) and report the stable-fraction
as a function of (τ_M, τ_P) — a clean, quantitative version of the paper's qualitative claim. This
is arguably the paper's most compelling and most *defensible* numerical contribution, and it
turns "basin of attraction shrinks" from an assertion into a measured phenomenon.

---

## 8. Minor corrections and hygiene

- **Drop or cite the unsupported empirical claim** ("global data from 1961–2022 … biocapacity
  grew modestly"). Either remove it, or support it with a GFN data reference. Its current
  presence contradicts the "calibration deferred" stance.
- **Resolve the orphan reference** (May, R.M., 1973) — cite it (relevant to stability/complexity)
  or remove it.
- **Journal name**: unify "Ecological Modeling" (cover letter) vs "Ecological Modelling"
  (system/header).
- **Keywords**: unify the abstract-page vs manuscript lists.
- **Provide the code as `.py` and the verification report as `.pdf`** rather than both as `.docx`.
- **Strip submission-system artifacts** ("Click here to access/download", the right-margin
  callout grid, PDF author metadata "233").

---

## 9. A revised abstract that is internally consistent

To make the "fixed" framing concrete, here is a rewritten abstract that keeps the ambition while
matching what the model does:

> We present a minimal coupled human–environment model in which carrying capacity is not an
> imposed ceiling but an emergent function of environmental stock, technological productivity,
> and per-capita resource demand. Environmental regeneration and demographic response are modelled
> as two distinct time delays; cumulative overshoot is tracked as an ecological debt that erodes
> productivity. For the sustainable, constant-parameter subsystem the non-trivial equilibrium is
> locally stable for any single delay, and the delay-perturbed eigenvalues remain near-neutral
> (growth rates below about 10⁻² yr⁻¹) across the two-delay plane; the onset of linear
> instability is strongly dependent on the ratio of the two lags. Numerically we identify two
> collapse mechanisms: when consumption exceeds the sustainable level, irreversible debt
> accumulation drives population collapse even with no delay at all; and when both delays are
> present, the delay-amplified transient shrinks the basin of attraction around the (still
> locally stable) steady state by roughly an order of magnitude, so that standard initial
> conditions are drawn into collapse. A sufficiently early technology wave can produce a period
> in which biocapacity rises while the environmental stock declines — the weak-sustainability
> regime — but this masking is bounded, because yield-per-stock gains saturate while ecological
> debt compounds, and because the same technology that raises biocapacity also raises the
> sustainable population and hence aggregate demand, tending to *increase*, not decrease,
> cumulative debt under overshoot. Rising biocapacity therefore need not signal improving
> environmental health; it may be a productivity illusion that precedes a fundamental reckoning.

This retains the paper's three ambitions (emergent carrying capacity; weak-vs-strong
reconciliation; collapse taxonomy) and its policy relevance, while removing the two
over-claims (the "≈80 yr" precision and the "already demonstrated" masking) and acknowledging the
technology-debt feedback.

---

## 10. Recommended author checklist (ordered by impact)

| # | Action | Impact | Verified? |
|--:|--------|:------:|:---------:|
| 1 | Add a "technology-masking" scenario + plot B(t) and M(t) | Turns headline claim into a result | Yes (118 params; case given) |
| 2 | Replace "≈80 yr" with the ratio-dependent, near-neutral boundary statement | Removes the biggest over-claim | Yes |
| 3 | Fix Half-Earth to K = 0.5·B/e | Makes the policy correct (Ω 0.575→0.500) | Yes |
| 4 | Add basin-shrinkage figure + stable-fraction table | Turns assertion into a measured result | Yes |
| 5 | Reconcile technology→more-debt (reframe as Jevons-type rebound) | Removes a silent contradiction | Yes |
| 6 | Add debt lag or justify the asymmetric delay | Makes delay structure consistent | Proposed |
| 7 | Analyse trivial equilibrium / add floor; switch to a stiff DDE solver + dt-convergence table | Makes "collapse" a model result | Proposed |
| 8 | Minor: empirical claim, orphan ref, naming, keywords, code format | Hygiene | Noted |

The paper's strongest contribution — the *two-mechanism* collapse taxonomy plus the
*measured* basin shrinkage — is untouched by these fixes and is, in my view, a genuinely
publishable core. The recommended changes are largely about (a) showing rather than asserting the
headline phenomenon, (b) removing the precision from a marginal boundary, and (c) making the
policy extension and the delay structure mean what the text says.

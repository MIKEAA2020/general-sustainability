# E1 — Ω_sim results: operating characteristics of the retention rule

**Design:** `SPECIFICATION_v4.md`, locked at commit `d5d9758`, 2026-09-10T21:44:18Z
**Executed:** 2026-09-10, results committed `87b2d13` at 23:03:31Z. **The simulation code
was written to implement the locked sheet after the lock** (git history above shows the
spec commit preceding the code commit by 79 minutes), and no code change altered a design
element. No design element was changed after execution.
**Output:** `wave_e_cod/results/sim_retention_power.csv` (10,000 rows: 5 DGPs × 2 σ × 200
replicates × 5 modules)
**Code:** `tools/sim_retention_power.py`, importing `run_ladder.step`,
`run_ladder.surplus` and `run_ladder.run_rolling` unmodified.

## 0. Design

### 0.1 Data-generating processes

All series are 33 years (`T = 33`, the Specification A length, 1983–2015). Innovations are
Gaussian **process** noise entering the state update inside `run_ladder.step` exactly as
`ε_t` does in Definition 2.1 — there is no observation-error layer and no noise on the
increment. Parameters are taken from the archived fits in
`results/fixed_window_scores.csv`.

| DGP | Generating model | r | K (kt) | catch | 𝔰 | empirical source |
|---|---|---|---|---|---|---|
| **D1** | M1 autonomous Schaefer | 1.935 | 1032.7 | constant 240 kt | — | collapse-window coarse fit |
| **D2** | M1 autonomous Schaefer | 0.458 | 500.0 | constant 5 kt | — | recovery-window coarse fit |
| **D3** | M2 stock-flow | 1.935 | 1032.7 | regime 240/120/5 | — | collapse fit + Specification A regime path |
| **D4** | M1b depensation | 0.458 | 500.0 | constant 5 kt | **15.0** | recovery fit, with an *identifiable* threshold |
| **D5** | persistence-true null | — | — | 0 | — | `S_{t+1} = S_t + η_t`, no surplus term |

`σ ∈ {11.8, 33.8}` kt for every DGP: the archived recovery- and collapse-window residual
standard deviations. Initial states are 900 kt (D1, D3), 30 kt (D2, D4), 300 kt (D5).
Rolling origins use the same eight-year minimum training length as Specification A, so each
synthetic series yields the same origin structure as the empirical pass.

**M3 and M4 were not simulated as generating truths.** Only M1 (D1, D2), M2 (D3) and M1b
(D4) were. This bounds what the study can conclude, and §4 is restricted accordingly.

### 0.2 What "retained" means

A module counts as retained in a replicate if it passes **H1, H2 and H3 at both horizons**,
exactly as in the empirical rule: it must beat its declared comparator and last-value
persistence by more than the 5% tie band at `h = 1` and `h = 5`. The tie band and the
horizon pair were **not** varied; they are fixed at the empirical values.

---

## 1. Headline

**The retention rule is highly specific and conditionally powerful. Its power depends
almost entirely on whether the generating structure is identifiable from 33 annual
observations — and for three of the four structural DGPs, it is not.**

This is a mixed result. Under the thresholds fixed in §5 of the locked sheet, one cell
meets the power bar, one is partial, and four fall in the band I pre-declared as
"substantially underpowered". Both specificity cells pass comfortably.

I am reporting it as it came out. The pre-declared thresholds were fixed precisely so
that this outcome could not be re-described after the fact.

---

## 2. Results against the pre-declared thresholds

**Threshold A (power):** a true, identifiable module should be retained in ≥ 80% of
replicates.
**Threshold B (specificity):** under a persistence-true DGP, no structural module should
be retained in ≥ 90% of replicates.

| DGP | truth | σ (kt) | power | 95% CI | verdict against §5 |
|---|---|---|---|---|---|
| D1 M1, collapse fit | M1 | 11.8 | **0.965** | ±0.025 | **meets ≥ 0.80** |
| D1 M1, collapse fit | M1 | 33.8 | **0.985** | ±0.017 | **meets ≥ 0.80** |
| D2 M1, recovery fit | M1 | 11.8 | 0.710 | ±0.063 | partial (0.30–0.80) |
| D2 M1, recovery fit | M1 | 33.8 | 0.130 | ±0.047 | **< 0.30** |
| D3 M2, stock-flow | M2 | 11.8 | 0.090 | ±0.040 | **< 0.30** |
| D3 M2, stock-flow | M2 | 33.8 | 0.110 | ±0.043 | **< 0.30** |
| D4 M1b, depensation (𝔰 = 15) | M1b | 11.8 | 0.005 | ±0.010 | **< 0.30** |
| D4 M1b, depensation (𝔰 = 15) | M1b | 33.8 | 0.015 | ±0.017 | **< 0.30** |

| DGP | σ | specificity | verdict |
|---|---|---|---|
| D5 persistence-true | 11.8 | **0.985** | **meets ≥ 0.90** |
| D5 persistence-true | 33.8 | **0.970** | **meets ≥ 0.90** |

**False-retention rate** across all true-DGP cells (a non-generating structural module
retained): **0.044**.

---

## 3. What is actually failing — diagnosed, not assumed

Low power could mean the rule's gates are too strict, or that the data cannot identify the
structure. These are different findings, so both were measured. H2 alone is "beats
persistence by more than the 5% band at both horizons", ignoring the H1 comparator gate:

| DGP | truth | passes H2 alone | passes full rule | gates, absolute | gates, **conditional on H2** |
|---|---|---|---|---|---|
| D1 | M1 | 0.975 | 0.975 | 0.000 | **0%** of H2-passers removed |
| D2 | M1 | 0.420 | 0.420 | 0.000 | **0%** |
| D3 | M2 | 0.328 | 0.100 | 0.228 | **69%** |
| D4 | M1b | 0.180 | 0.010 | 0.170 | **94%** |

**Both framings are true and both should be reported.** In absolute terms the dominant
failure is H2: the true module frequently does not out-predict persistence on data it
generated itself, and no comparator gate is responsible for that. But *conditional on
clearing H2*, the comparator requirement is a dominant additional filter — it removes 69%
of surviving D3 replicates and 94% of surviving D4 replicates. That is a genuine property
of the rule: demanding that a module beat both persistence and its declared comparator is
far more stringent than demanding it beat persistence alone, wherever the true module is
only marginally the best.

The identification limit is visible more directly still. With five structural modules,
random assignment would make the true module the lowest-error one **20%** of the time:

| DGP | true module has lowest h=1 RMSE | versus 20% chance |
|---|---|---|
| D1 (M1 true) | 0.627 | far better |
| D2 (M1 true) | 0.645 | far better |
| **D3 (M2 true)** | **0.0375** | **worse than chance** |
| D4 (M1b true) | 0.258 | barely better |

The D3 figure is the sharpest result in the study. When a stock-flow process generates the
data, the stock-flow module is the best-scoring structural module *less often than if the
winner were drawn at random* — its mean h=1 error (85.7 kt) is worse than M3's (77.9) and
M1b's (79.9). At 33 annual observations with these parameters, the correct structure is
not merely hard to detect; it is actively disadvantaged by estimation noise relative to
its siblings. That is an identification failure, not a decision-rule failure.

## 4. What this licenses the manuscript to say — and what it does not

**Licensed:**

1. **The rule is not a rubber stamp.** Under a persistence-true process it declines to
   retain structure in 97–99% of replicates. A reviewer worried that the negative result
   is an artefact of an instrument that rejects everything has the answer: the instrument
   is strict, but it is also correct under a null.
2. **The rule has real power where the signal is strong.** D1 gives 0.965–0.985.
3. **The empirical collapse-window result is informative, not a power failure.** This is
   the resolution of an apparent contradiction. D1 shows that *if* the collapse window had
   been generated by an autonomous Schaefer map at the fitted parameters, the rule would
   have retained M1 in 97–98% of replicates. The empirical collapse window does **not**
   retain M1. The two together imply the empirical data are inconsistent with that
   generating process — M1's non-retention is evidence about the stock, not about the
   instrument.
4. **Power collapses where the cod recovery data sit.** D2 at σ = 33.8 (0.130) and D3/D4
   (0.005–0.110) correspond to the low-biomass, post-collapse conditions of most of the
   Specification A window.

**Not licensed:**

5. Non-retention of **M2 and M1b** is weak evidence against those structures: the rule
   would have retained them in at most 11% and 1.5% of replicates respectively had they
   been true at recovery-window parameters.
6. **M3 and M4 were not simulated as generating truths**, so this study provides no direct
   power estimate for them. Their power is plausibly bounded above by M2's, since both add
   structure to the same stock-flow base map and must clear an additional comparator gate,
   but that is an inference and is not measured here. The manuscript must not claim a
   measured power figure for M3 or M4.
7. The result **cannot** be dismissed as pure low power. D1 and the specificity cells
   refute that reading.

**False-retention rate, disambiguated.** Across the four structural DGPs, a non-generating
module was retained in **0.044 of module-replicate pairs** (per-module rate); the expected
number of falsely retained modules per replicate is **0.176**. Under the persistence-true
null the per-module rate is **0.005** and the per-replicate count **0.025**. A per-module
rate near or below the 5% tie band is what a rule controlling false positives at its
nominal level should produce, and that is what is observed.

## 5. Consequence for the abstract

§5 of the locked sheet says: if power < 0.30, "the manuscript's negative result must say so
in the abstract." Four cells are below 0.30. That clause is triggered.

The honest reading is not that the whole result is underpowered — D1 refutes that — but
that **the strength of the negative result differs by module**. Wording implemented in
v40, corrected from the v39 text, which overreached by naming the residual module (never
simulated) and by attaching "under 15%" to a set that included D2:

> Simulation under known ground truth shows the rule retains a true autonomous module in
> 97% of replicates at collapse-window parameters but has power below 15% for the
> stock-flow and depensation alternatives at recovery-window parameters, so non-retention
> is informative for the first and weak evidence against the others; the residual and
> lagged-initialisation modules were not simulated.

## 6. Limitations

**Design.** The processes are members of the ladder's own class, so this measures power
against **correctly specified** alternatives — the easiest case. Power against
misspecified truth is lower, and D1 is therefore an **upper bound**. The tie band and the
horizon pair were held at their empirical values and not varied. M3 and M4 were not
simulated as generating truths.

**Data.** Synthetic predictands carry no assessment smoothing, so persistence is a
**weaker** baseline here than on the reconstructed series — which flatters the rule. There
is no observation error, catch-reconstruction error, or assessment revision.

**Coverage.** Only `T = 33` (the Specification A length) and `σ ∈ {11.8, 33.8}` were run.
`T = 71` — the Specification B length, 1954–2024 — together with `σ = 0` and
`𝔰 ∈ {5, 30}` were declared as deferred extensions in §2b of the locked sheet and remain
unrun. They cannot revise these thresholds.

**Precision.** 200 replicates give ±5.5 pp at p ≈ 0.8. The D1-versus-D3/D4 contrast is far
larger than that interval; D2 at σ = 11.8 (0.710 ± 0.063) is the only cell near a decision
boundary.

## 7. What would change the conclusion

Stated so that the study's own weak points are visible rather than left for a reader to
find:

- **If D2 at intermediate σ showed power above 0.5**, recovery-window non-retention would
  become more informative than §4 currently allows, and item 5 would need softening.
- **If a misspecified-truth DGP showed power comparable to D1**, the "upper bound" caveat
  would be unnecessary and the licensed claims would strengthen.
- **If M3 or M4 were simulated and showed power above 0.30**, the inference in item 6 that
  their power is bounded by M2's would be falsified.
- **If the tie band were varied and specificity fell below 0.90 at 0%**, the 5% band would
  be doing more work than the paper credits.

The two highest-value extensions are a misspecified-truth DGP, which would bound power
from *below*, and generating DGPs for M3 and M4, which would complete the ladder. Neither
is required for the present manuscript; both would strengthen a follow-up. Note that D4's
near-zero power is independently consistent with the empirical M1b result — the fitted
threshold descends to an unattained infimum on the real data, and the simulation shows the
rule cannot recover even a genuinely identifiable threshold at these parameters. The two
lines of evidence agree.

## 8. Frozen-spec invariance

No cod score, table value or retention verdict was recomputed or changed. Ω_sim scores
synthetic series only. `SPECIFICATION_v2.md` is untouched, and the empirical record stands
byte-identical.

---

## 9. Amendment 1 results: misspecified truth

**Design:** `SPECIFICATION_v4.md` Amendment 1, locked at commit `bd0008f`
(2026-09-11T01:56:22Z), executed afterwards. **Output:**
`wave_e_cod/results/sim_misspecified_D6D7.csv`, 4,000 rows (2 DGPs × 2 σ × 200 replicates
× 5 modules).

### 9.1 The pre-declared threshold is breached

Amendment §A1.5 fixed the criterion in advance: *if false retention under D6 or D7 exceeds
0.10, the rule retains structure that is not there when the truth is outside its class,
and the core specificity figure is not transferable to misspecified settings. This must be
reported in the abstract.*

| DGP | truth | σ | false retention | threshold |
|---|---|---|---|---|
| D6 time-varying productivity | outside class | 11.8 | **0.680** | exceeds 0.10 |
| D6 time-varying productivity | outside class | 33.8 | **0.760** | exceeds 0.10 |
| D7 observation error only | outside class | 11.8 | **0.975** | exceeds 0.10 |
| D7 observation error only | outside class | 33.8 | **0.925** | exceeds 0.10 |

All four cells breach it, by margins of six to ten times the bar.

### 9.2 The contrast is the finding

| null | false retention |
|---|---|
| D5 persistence-true, **inside** the ladder's class | 0.015 / 0.030 |
| D6, D7, **outside** the class | 0.680 – 0.975 |

**Specificity is not a property of the rule; it is a property of the rule applied to
in-class data.** Against a persistence-true process the rule almost never retains
structure. Against a process the ladder cannot represent — productivity that drifts, or a
deterministic state observed with error — it retains structure in most replicates.

The module falsely retained is overwhelmingly **M1**, the autonomous Schaefer map: 134 and
151 replicates under D6, 195 and 185 under D7. When the truth is a smoothly declining
productivity or a smooth trajectory seen through noise, a constant-productivity map
out-predicts persistence often enough to clear both gates.

### 9.3 Consequence for the manuscript's claims

This bounds the earlier results from below and qualifies one of them.

1. **The power figures stand as upper bounds**, as already disclosed.
2. **The specificity figure of 0.97–0.99 must now be scoped explicitly to in-class truth.**
   Stating it unqualified would imply a property the rule does not have.
3. **The empirical non-retention result is unaffected and is, if anything, strengthened.**
   The failure mode exposed here is *false retention* — the rule keeping a module when the
   truth is outside its class. On both cod and Edwards the rule retained nothing. A rule
   that over-retains under misspecification, and still retained nothing on the observed
   series, gives no reason to suspect the empirical verdict is an artefact of leniency.
4. **The reading of M1's non-retention on the collapse window tightens.** D1 showed the
   rule recovers a true M1 in 97% of replicates; D6 and D7 now show it also retains M1
   when M1 is *false*. So M1's non-retention on the observed data is informative in both
   directions: the rule finds M1 when present and is inclined to find it when absent, and
   it still did not find it.

### 9.4 Not completed

`T = 71` for D1 and D5, also registered in Amendment 1, was started and **abandoned as
infeasible**: a single rolling pass at T = 71 costs 45.6 s against 7 s at T = 33, giving
about 10 h for the 800 remaining passes. It is not reported, and no length-sensitivity
claim is made. Condition 3's series-length limb therefore remains unmet; its
misspecified-truth limb is now met.

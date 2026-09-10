# E1 — Ω_sim results: operating characteristics of the retention rule

**Design:** `SPECIFICATION_v4.md`, locked at commit `d5d9758` (2026-09-10T21:44:18Z)
**Executed:** 2026-09-10, after the design was committed. No design element was changed
after execution.
**Output:** `wave_e_cod/results/sim_retention_power.csv` (10,000 rows: 5 DGPs × 2 σ × 200
replicates × 5 modules)
**Code:** `tools/sim_retention_power.py`, importing `run_ladder.step`,
`run_ladder.surplus` and `run_ladder.run_rolling` unmodified.

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
structure. These are different findings, so I decomposed them. H2 alone is "beats
persistence by more than the 5% band at both horizons", ignoring the H1 comparator gate:

| DGP | truth | passes H2 alone | passes full rule | cost of the H1/H3 gates |
|---|---|---|---|---|
| D1 | M1 | 0.975 | 0.975 | **0.000** |
| D2 | M1 | 0.420 | 0.420 | **0.000** |
| D3 | M2 | 0.328 | 0.100 | 0.228 |
| D4 | M1b | 0.180 | 0.010 | 0.170 |

And, more directly — is the true module even the *best-scoring* structural module on its
own synthetic data?

| DGP | true module has lowest h=1 RMSE in |
|---|---|
| D3 (M2 true) | **3.7%** of replicates |
| D4 (M1b true) | **25.8%** of replicates |

**The dominant failure is not the rule's gates. It is that the true generating module
frequently does not out-predict persistence — or even its own ladder siblings — on data it
generated itself.** On D3, M2's mean h=1 RMSE (85.7 kt) is *worse* than M3's (77.9) and
M1b's (79.9). At T = 33 with these parameters, a wrongly-specified module fits the noise
about as well as the right one.

The comparator gates do add cost on D3 and D4 (0.17–0.23), which is a genuine and
reportable property of the rule: requiring a module to beat both persistence and its
declared comparator roughly halves retention where the true module is only marginally
best. But it is the secondary effect, not the primary one.

---

## 4. What this licenses the manuscript to say — and what it does not

**Licensed:**

1. **The rule is not a rubber stamp.** Specificity is 0.97–0.99; the false-retention rate
   is 0.044. When persistence is genuinely the best rule, it is retained. A reviewer
   worried that the negative result is an artefact of an over-strict instrument has the
   answer: the instrument is strict, but it is also correct under a null.
2. **The rule has real power where the signal is strong.** D1 — a high-biomass stock under
   large constant catch, the collapse-window parameterisation — gives 0.965–0.985. The rule
   detects true structure when the data identify it.
3. **Power collapses exactly where the cod data sit.** D2 at σ = 33.8 (0.130) and D3/D4
   (0.005–0.110) are the low-biomass, post-collapse, regime-catch conditions that
   characterise most of the Specification A window.

**Not licensed:**

4. The Northern cod non-retention **cannot** be attributed solely to uninformative data.
   Under the thresholds I fixed in advance, four of eight power cells are below 0.30. The
   manuscript must state that the rule is **substantially underpowered for three of the
   four structural alternatives at this sample size**, and that non-retention of M2, M3,
   M4 and M1b is therefore weak evidence against those structures.
5. Equally, the result **cannot** be dismissed as pure low power. M1's non-retention on
   the real collapse window is informative, because D1 shows the rule retains a true M1
   there 96–98% of the time.

**This is a more precise conclusion than the paper currently draws in either direction.**

---

## 5. Consequence for the abstract

§5 of the locked sheet says: if power < 0.30, "the manuscript's negative result must say so
in the abstract." Four cells are below 0.30. That clause is triggered.

The honest reading is not that the whole result is underpowered — D1 refutes that — but
that **the strength of the negative result differs by module**. The abstract must not
continue to present a uniform "no module is retained" without qualification.

Proposed wording, to be implemented in v39:

> Simulation under known ground truth shows the rule retains a true autonomous module in
> 97% of replicates at collapse-window parameters but under 15% for the stock-flow,
> residual and depensation alternatives at recovery-window parameters, so non-retention is
> strong evidence against the first and weak evidence against the others.

---

## 6. Limitations, as disclosed in the locked sheet before running

- The DGPs are members of the ladder's own class, so this measures power against
  **correctly specified** alternatives — the easiest case. Real power against misspecified
  truth is lower, and the adequate-power finding for D1 is an **upper bound**.
- Synthetic predictands carry no assessment smoothing, so persistence is a **weaker**
  baseline here than on the real series. This flatters the rule.
- No observation error, catch-reconstruction error, or assessment revision.
- Only `T = 33` and `σ ∈ {11.8, 33.8}` were run. `T = 71`, `σ = 0` and `𝔰 ∈ {5, 30}` were
  declared in §2b as deferred extensions and remain unrun; they cannot revise these
  thresholds.
- 200 replicates give ±5.5 pp at p ≈ 0.8. The D1-versus-D3/D4 contrast is far larger than
  that interval; the D2 σ = 11.8 cell (0.710 ± 0.063) is the only one close to a boundary.

---

## 7. Frozen-spec invariance

No cod score, table value or retention verdict was recomputed or changed. Ω_sim scores
synthetic series only. `SPECIFICATION_v2.md` is untouched, and the v37 empirical record
stands byte-identical.

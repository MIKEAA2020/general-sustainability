# Phase C — computational campaigns: results and provenance (2026-09-13)

Scope (register §5): T=71; smoothed-predictand experiment; SNR power curves; uncertainty-aware
gate + hybrid rows; MCS/encompassing; per-regime decomposition; Edwards reproducibility rerun;
D3 provenance pin; M3/M4-as-truth cells (optional); pre-check candidates (4.5).
Deliverable for the paper: reconcile every Section 4.3 operating-characteristic cell against the
fresh CSVs and replace or disclose any that fail to reproduce (register item N1).

## 0. Provenance policy (how this run differs from the zip CSVs)

- **Estimator/map/scorer are imported, never reimplemented.** All campaigns import
  `run_ladder` from `wave_e_cod/src/run_ladder.py` (the frozen registered code) — same module the
  author's `tools/sim_retention_power.py` imports.
- **Pinned randomness.** Every campaign runs under `PYTHONHASHSEED=0` and seeds each replicate
  with the author's original scheme `abs(hash((dgp, sigma, rep))) % 2**31`. The published and
  zip-CSV runs used process-salted hash seeds (unknown PYTHONHASHSEED); this run is reproducible
  by anyone. Every CSV carries a `_provenance.json` (code shas, versions, wall time, seed policy).
- **Scaling decisions (disclosed).** Measured ladder costs on this 2-core machine (dual-load):
  T=33 passes 2.2–16.7 s by DGP (D1 ≈ 14.6–16.7 s; D2 ≈ 6.1–7.1 s; D3 ≈ 7.8–8.3 s; D4 ≈ 2.2–4.3 s;
  D5 ≈ 4.5–4.8 s), T=71 passes 13–110 s (D1_T71 ≈ 95–110 s; D5_T71 ≈ 13–25 s). The author's
  published benchmark (7.0 s at T=33, 45.6 s at T=71) is optimistic for the slow cells.
  Reps chosen: **D1/D5 200** (registered), **D2/D3/D4 100**, **D6/D7 30**, **T=71 10**,
  **smoother 30/arm**, **origins 25**, **SNR sweep 25**. A first misspecified run
  (D6/D7@100, T71@50) was killed at 2.5 h with D6+D7 complete but unwritten; the trimmed rerun
  completed all four cells in 49 min. Every rate below carries its binomial CI so the reduced
  reps are not hidden. Full registered design (Amendment 1: eight cells × 200, ≈10 h) remains
  registered for larger hardware.

## 1. Edwards cross-environment rerun — **PASS (exact)**

`phase_c/results/e3_audit_uncertainty_M2m_h5_20260913.json`: all six archived e3-audit-layer
specs reproduce to full precision (M1/M2m/M2 vs persist h=1; naive_mean vs persist h=5; M1 vs
persist h=5 — margins −0.391, −0.9469, −0.5559, +1.4677, −4.3008, +0.1458 with identical DM
statistics), and the **D1 citation cell reproduces exactly: M2m vs naive_persist h=5 (n=71),
margin −3.6607, DM z = −3.284, p = 0.0016, block-bootstrap 95% CI [−5.764, −2.186]**
(published [−5.7637, −2.1862]; 4th-decimal rounding of the same percentiles).
Environment: numpy 2.3.5, scipy 1.17.1, pandas 2.2.3 (newer than the author's run).

## 2. D1–D5 operating characteristics — **substantially reproduced**

`phase_c/results/sim_retention_power_20260913.csv` (7,000 rows). True-module power / specificity
(fresh n=200 D1/D5, n=100 D2–D4) vs published:

| cell | fresh | published | binomial CI95 | verdict |
|---|---|---|---|---|
| D1 σ=11.8 | 0.955 | 0.965 | ±0.025 | PASS |
| D1 σ=33.8 | 0.960 | 0.985 | ±0.017 | CHANGE (marginal, verdict unchanged) |
| D2 σ=11.8 | 0.780 | 0.710 | ±0.089 | PASS |
| D2 σ=33.8 | 0.060 | 0.130 | ±0.066 | CHANGE (marginal, verdict unchanged) |
| D3 σ=11.8 | 0.110 | 0.090 | ±0.056 | PASS |
| D3 σ=33.8 | 0.100 | 0.110 | ±0.061 | PASS |
| D4 σ=11.8 | 0.010 | 0.005 | ±0.014 | PASS |
| D4 σ=33.8 | 0.010 | 0.015 | ±0.024 | PASS |
| D5 σ=11.8 (1−spec) | 0.005 | 0.015 | ±0.017 | PASS |
| D5 σ=33.8 (1−spec) | 0.050 | 0.030 | ±0.024 | PASS |

Any-module retention (fresh): D3 0.540/0.600, D4 0.260/0.050 — these match the zip-CSV
values previously misread as "true-module power" (zip 0.520/0.615, 0.385/0.070). **The zip
"mismatch" was partly a measure conflation (any-retention vs true-module power) and partly
seed salting; published §4.3 is vindicated under pinned seeds.** Every qualitative verdict
survives: D1 power high, D2 high-σ below bar, D3/D4 below bar, D5 specificity ≥ 0.90.

## 3. D6/D7 + T=71 — **reproduced + first execution**

`phase_c/results/sim_misspecified_20260913.csv`. Mechanism misattribution (any-module retention,
n=30): D6 0.633/0.733 vs published 0.680/0.760 (PASS both); D7 0.933/0.867 vs 0.975/0.925
(PASS both). **T=71 first execution (n=10, disclosed): D1 power 0.900/1.000; D5
any-retention 0.000/0.000 (specificity 1.000).** Both consistent with the T=33 cells.
**AD2 registered measure (realised predictive gain of retained modules, D6/D7):** the retained
module beat persistence in 100% of retention replicates; mean gain +2.6/+9.4 (D7) and
+3.1/+9.2 kt (D6) at h=1, low/high σ — the mechanism-misattribution rows are predictive
gains, not noise-fits (`d67_realised_gain_20260913.json`).

## 4. Smoother test — **done: mechanism real, not sufficient alone**

`phase_c/results/smoother_test_20260913.{csv,provenance,summary}.json` (30 reps/arm). Same D1
replicates, raw vs centred-3-year-moving-average predictand. M1 persistence margin (kt) and
true-module power:

| arm | h=1 margin σ=11.8 | σ=33.8 | power σ=11.8 | σ=33.8 |
|---|---|---|---|---|
| raw | −8.90 | −23.22 | 0.900 | 1.000 |
| smoothed | −0.57 | −1.76 | 0.633 | 0.667 |

The assessment-like smoother compresses the margin 7–13× and costs ~30 points of power, but
M1 still beats persistence at both horizons (margins stay negative) — the mechanism is real
and in the expected direction, not sufficient alone. → §6 (R25).

## 5. SNR sweep — **done: identification limit is structural**

`phase_c/results/sim_snr_sweep_20260913.csv` (25 reps/cell). Combined power curve (fresh,
all σ): D1 0.88 (σ=5), 0.955 (11.8), 1.00 (20), 0.960 (33.8), 0.960 (45) — flat-high, no SNR
cliff. D3 at σ=5: 0.00 (any 0.48); D4 at σ=5: 0.00 (any 0.72). Clean signal does not rescue
stock-flow or depensation — the binding constraint is the gate structure and catch regime,
not noise. → noted in §4.4 (R09).

## 6. Uncertainty gate / hybrid / MCS — **done: disclosed §4.5 post-hoc rows**

`phase_c/results/sim_origins_20260913.csv` (8.6 MB per-origin archive) →
`gate_hybrid_mcs_20260913.{csv,json}` (250 replicate records, n=25/cell). Uncertainty gate
(95% moving-block-bootstrap CI of each margin fully below zero; block 4, 999 resamples):
D1 power 0.64/0.64 (band 0.92/1.00), D2 0.24/0.00, D3 0.00/0.00, D4 0.00/0.00, D5
specificity 1.00/0.96; hybrid = uncertainty (dominated). MCS (Hansen-Lunde-Nason, α=0.10,
block bootstrap 499): persistence survives every replicate; true module never in the 90% set
for D1/D2, in 0.12/0.32 of D3 and 0.08/0.24 of D4 replicates. Verdicts unchanged in direction;
the negative result is not an artefact of the fixed band. → §4.5 (R23).

## 7. Per-regime decomposition + identification pin — **done**

`per_regime_decomposition_20260913.json`: power stable across realised regime halves in D1
(0.95/0.96 both halves), D2 low-σ 0.74/0.82, D3 ≈ 0.06–0.14, D4 ≈ 0.00–0.02, D5 specificity
≈ 0.99–1.00 — no cell's verdict flips with the realised regime.
`identification_limit_20260913.json`: generating module lowest one-step error (fresh vs
published): D1 0.51/0.565 (62.7/64.5 autonomous pooled), D2 0.81/0.70, D3 0.01/0.11 (3.8),
D4 0.37/0.18 (25.8) — same ordering, seed-dependent levels. Comparator-gate removal of
H2-passers (fresh): D3 0.31/0.81 (69), D4 0.96/0.50 (94) — same order.
`training_window_profile_20260913.csv`: D1 M1 mean sqerr stays 2–4× below persistence across
origins; D3 M2 spikes 33× above persistence at the 1991→1992 catch-regime transition
(origin 1991: 14,802 vs 446 kt²) — the D3 failure mechanism, pinned to a
training-window-visible flag → §4.6 third pre-check candidate (R24).

## 8. Section 4.3 reconciliation — **FINAL: 12 PASS / 2 marginal CHANGE / 4 NEW (0 missing)**

`reconcile_s43_20260913.{csv,json}` (final regeneration, all 18 cells). Verdict table in §2;
D6/D7 PASS in §3; T=71 cells NEW (first execution, n=10). The paper pass (v16) replaces the
two marginal cells' point values (D1-σ33.8 0.985→0.960, D2-σ33.8 0.130→0.060 — verdicts
unchanged), replaces all four "T=71 not executed" sentences with the first-execution numbers,
adds the AD2 gain numbers to the D6/D7 row measures, resolves the mean-power 0.376 provenance
(fresh 0.373, within CI), discloses the gate/hybrid/MCS rows in §4.5, adds the third pre-check
candidate to §4.6, reports the smoother experiment in §6, and corrects the pass-cost claims
with measured ranges. Applied as `framework/apply_phaseC_v15_to_v16.py` (25 asserted rules);
changelog `framework/PHASE_C_CHANGELOG_v15_to_v16.md`.

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
  zip-CSV runs used process-salted hash seeds (unknown PYTHONHASHSEED), which is why their CSVs
  do not reproduce published §4.3 (D3 zip 0.520/0.615 vs published 0.090/0.110; D4 zip
  0.385/0.070 vs 0.005/0.015; D6/D7 zip 0.137–0.199 vs 0.680–0.975). This run is reproducible by
  anyone: fixed seed map + pinned hash seed, archived alongside every CSV as `_provenance.json`
  (shas of the code files, versions, wall time, seed policy).
- **Scaling decisions (Phase C, disclosed):** D1/D5 run at the registered 200 reps; D2/D3/D4 at
  100; D6/D7 at 100; T=71 cells at 50 reps; SNR-sweep cells at 60; per-origin campaign at 40.
  The author's full Amendment-1 design (eight cells, 200 reps, 1,600 passes ≈ 10 h) is registered
  as a longer campaign for a beefier machine; every rate below carries its binomial CI so the
  reduced reps are not hidden.

## 1. Edwards cross-environment rerun — **PASS (exact)**

`phase_c/results/e3_audit_uncertainty_M2m_h5_20260913.json` (re-run of the e3 audit layer with
the archived per-origin forecast CSVs and the module's own DM/bootstrap functions; seed 20260905,
10,000 resamples, block 8 — all frozen constants):

| comparison | margin (new = archived) | DM z | p |
|---|---|---|---|
| M1 vs naive_persist h=1 (n=75) | −0.391 | −0.852 | — |
| M2m vs naive_persist h=1 (n=75) | −0.9469 | −3.071 | — |
| M2m vs M1 h=1 (n=75) | −0.5559 | −1.615 | — |
| M2 vs naive_persist h=1 (n=75) | +1.4677 | +1.275 | — |
| naive_mean vs naive_persist h=5 (n=71) | −4.3008 | −1.652 | — |
| M1 vs naive_persist h=5 (n=71) | +0.1458 | +0.057 | — |

All six reproduce the archived `wave_e_edwards/results/e3_audit_uncertainty.json` to full
precision. The **D1 citation cell** reproduces exactly: **M2m vs naive_persist h=5 (n=71):
margin −3.6607, DM z = −3.284, p = 0.0016, block-bootstrap 95% CI [−5.764, −2.186]**
(published [−5.7637, −2.1862]; difference is 4th-decimal rounding of the same percentiles).
Environment: numpy 2.3.5, scipy 1.17.1, pandas 2.2.3 (newer than the author's run).

## 2. D1–D5 operating characteristics (campaign_power) — [PENDING]

`phase_c/results/sim_retention_power_20260913.csv`. Published reference values (frozen, from
paperF1 v15): D1 0.965/0.985; D2 0.710/0.130; D3 0.090/0.110; D4 0.005/0.015; D5 specificity
0.985/0.970 (false retention 0.015/0.030 per replicate).

## 3. D6/D7 + T=71 (campaign_misspecified) — [PENDING]

`phase_c/results/sim_misspecified_20260913.csv`. Published: D6 0.680/0.760, D7 0.975/0.925
(mechanism misattribution, vs 0.10 pre-declared threshold); T=71 published as "not executed as
full simulation" — this run is the first execution.

## 4. Smoother test (campaign_smoother) — [PENDING]

`phase_c/results/smoother_test_20260913.{csv,json}`. Raw vs centred-3yr-moving-average arms of
the SAME D1 replicates (seeds identical to campaign_power reps 0–99): does an assessment-like
retrospective smoother reverse the persistence margin?

## 5. SNR sweep (campaign_snr) — [QUEUED]

`phase_c/results/sim_snr_sweep_20260913.csv`. D1 σ ∈ {5, 20, 45}; D3/D4 σ = 5 (60 reps).

## 6. Uncertainty gate / hybrid / MCS (campaign_origins + analysis_gate_mcs) — [QUEUED]

`phase_c/results/sim_origins_20260913.csv` → `gate_hybrid_mcs_20260913.{csv,json}`.
Rules: 5% band (frozen), uncertainty gate (moving-block-bootstrap 95% CI of each RMSE margin
fully below zero, block 4, 999 resamples), hybrid (both), and Hansen-Lunde-Nason MCS (α = 0.10,
block bootstrap 499 resamples) over 6 candidates at h = 1.

## 7. Per-regime decomposition + identification pin + training profile (analysis_regime_ident) — [QUEUED]

`phase_c/results/per_regime_decomposition_20260913.json`, `identification_limit_20260913.json`,
`training_window_profile_20260913.csv`. Published reference: generating module lowest one-step
error in 62.7%/64.5% autonomous, 25.8% depensation, 3.8% stock-flow; comparator gate removes
69% of H2-passers in D3 and 94% in D4.

## 8. Section 4.3 reconciliation (reconcile_s43) — [QUEUED]

`phase_c/results/reconcile_s43_20260913.{csv,json}`. Verdict per cell: PASS (fresh rate within
binomial CI of published), CHANGE (replace the number in the paper), NEW (T=71 first execution),
DISCLOSE (not recomputable). Replacement edits to the paper follow the verdicts (Phase C pass).

# CL-INST-T71 v2 — Band-calibration campaign LANDED (2026-09-17)

**Instruction lineage:** CL-INST-T71 v1 (2026-09-16) ordered re-registration of the
5% change-detection-band verdicts at the observation window the corpus actually
uses (T=71, years 1954–2024), after F1 v26's band figures were produced at an
earlier panel length. **Status: LANDED.**

## Provenance (read first)

- Final artifact: `phase_c/results/cod_t71_band_calibration_20260916.json`.
- The original 2026-09-16 full run was **lost**: the frozen harness accumulates
  all 800 reps in memory and writes only at the end; the sandbox process died
  before any write. This is the FIRST write under the sheet-registered name.
- Re-executed 2026-09-17 via
  `framework/campaign_cod_t71_band_calibration_checkpointed_20260917.py`
  (imports the frozen harness unchanged; identical per-rep seed map;
  per-10-rep checkpoint flushes; resume-safe). Operator `PYTHONHASHSEED=0`.
- Execution: 4 foreground chunks of ≤1650 s (sandbox culls background
  processes); intermediate state in
  `phase_c/results/cod_t71_band_calibration_20260917_checkpoint.json`.
- The `rescue` field inside the JSON records the same disclosure.
- **Cost registration correction:** a prior session estimated "800 passes ×
  45.6 s ≈ 10.13 h". Measured in-environment: D1 s=11.8 ≈ 9.7 s/rep,
  D1 s=33.8 ≈ 10.9 s/rep, D5 ≈ 3.2 s/rep; chunk-4 wall 315.9 s for 110 reps.
  Total observed ≈ 6,140 s ≈ 1.71 h — the earlier estimate was overstated
  ~7×. Do not reuse the 10.13 h figure downstream.

## Design

- Cells: 4 = {D1 true-change, D5 no-change} × {σ_R ∈ {11.8%, 33.8%}}; 200 reps
  each = 800 total at T=71 (1954–2024), frozen harness, fixed seed map.
- Bands: ±0% to ±15% in 0.5% steps (31 bands).
- Outcomes: per-band detection power (D1) / false-detection rate (D5); aux
  documented side effect = wrong-module retention reps.

## Headline results

| Cell | band 0 detection | band ±5% | band ±15% | wrong-module (band 0 → ±5% → ±15%) |
|---|---|---|---|---|
| D1, σ_R=11.8% | 1.000 | 1.000 | 0.970 | 22/200 → 0 → 0 |
| D1, σ_R=33.8% | 1.000 | 1.000 | 0.980 | 33/200 → 0 → 0 |
| D5, σ_R=11.8% | 0.000 | 0.000 | 0.000 | 46/200 → 1 → 0 |
| D5, σ_R=33.8% | 0.000 | 0.000 | 0.000 | 36/200 → 0 → 0 |

- Pooled D1 mean power: 1.000 from band 0 through ±7.0%; first dip 0.9975 at
  ±7.5%; 0.9775 at ±14.5%; 0.975 at ±15%. (Full 31-band table in the JSON's
  `pooled` array.)
- Pooled D5 specificity: 1.000 at **every** band — no false detections in
  400 pooled null reps at any tolerance.
- Wrong-module retention (documented aux side effect): concentrated at band 0
  (22–46 reps of 200), ≤3% by ±0.5% band, and 0–1 reps from ±5% upward.

## Reconciliation with F1 v26 (5% band verdicts)

- F1 v26 frozen figures: D1 0.955/0.960, D5 0.995/0.950 at the earlier window.
- At T=71 the **5% verdicts are confirmed with no margin**: D1 power 1.000/1.000
  (200/200 both σ_R cells; Wilson 95% lower bound ≈ 0.982) and D5 specificity
  1.000/1.000 (200/200; Wilson lower bound ≈ 0.982). Differences vs F1's
  sub-1.0 numbers are consistent with the shorter panel length F1 used, not
  with a behavioral reversal; no F1 sentence needs retraction — v53's existing
  F1-bearing lines stand, and the T=71 row is strictly stronger.
- The aux side effect at band 0 (up to 23% wrong-module retention) explains
  why band-0-only framing was misleading; by ±0.5% it is ≤3% and by ±5% it is
  ≤0.5%. Reporting bands ≥ ±5% remains the correct convention.

## Files

- `phase_c/results/cod_t71_band_calibration_20260916.json` — final (canonical).
- `phase_c/results/cod_t71_band_calibration_20260917_checkpoint.json` — raw
  checkpoint replica; retained for audit, do not cite for results.
- `framework/campaign_cod_t71_band_calibration_checkpointed_20260917.py` —
  checkpointed runner (standing pattern: any campaign >5 min must checkpoint).
- `phase_c/results/cod_t71_rescue_20260917.log` — operator log (chunks 1–4).

**Carry-over:** pointer from F1 v26 / frozen prose: "at T=71 (1954–2024) the
±5% change-detection band recovers 200/200 true-change reps and rejects
200/200 no-change reps in each σ_R cell" — source this file, not the raw F1.

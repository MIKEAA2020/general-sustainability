# Paper E1 — v50 Addendum (outcome years, threshold definition-dependence, observation suspension)

**Base:** `paperE1_cod_forecast_ladder_v49.tex` (remote main). **Scope:** three new results subsections (3.8–3.10) built from published data archived in-repo, plus abstract/highlights/discussion/conclusions/data-availability updates. **No change to the scored comparison, the frozen specification, or any existing table; the retention verdict stands as published.**

## 1. Changes (9 asserted patches)

| # | Change | Detail |
|---|--------|--------|
| P1 | §3.8 The outcome years (2016–2021) | RAM Legacy v4.66 per-year SSB (same NCAM-family assessment of record, 2021 vintage): 340/433/394/419/440/411 kt; xteNCAM reads the same years at 339/451/369/400/414/423 (mean |diff| 16.8 kt); persistence from the 2015 origin errs low every year (MAE 129.2 kt, RMSE 133.3 kt; 107.5 kt from the Table A2 origin). Outcome window is an increase regime: no collapse event; the frozen verdict neither confirmed nor reversed. Module re-scoring on the extension is NOT claimed (archived-pipeline work). |
| P2 | §3.9 Threshold definition-dependence | On the xteNCAM file (71 years): 45 years ≥ Blim 276; 16 years ≥ LRP 884.6 (1954–69 only); 29 disagreement years (1970–1992 sans 1977–79; 2016–2024). Under 884.6 the stock is below for 55 consecutive years (1970–2024); under Blim, 26 years (1977–79, 1993–2015). The 1980s-mean LRP is itself vintage-dependent: 884.58 kt (Table A2) vs 790.00 kt (RAM vintage), a 94.6 kt shift. The October 2023 framework revision (critical → cautious without a change in the stock) is the experiment executed by the authority itself. Brier-layer verdicts inherit the dependence; the RMSE comparison does not use thresholds. |
| P3 | §3.10 The 2022–2023 observation suspension | Survey gap 2021–22 → leading indicator uncomputable → no 2022/2023 updates → stewardship maximum frozen at 12,999 t → vessel condemned Feb 2023 → Mar 2024 assessment (1.2 Blim; 22% critical) → Jun 2024 reopening at 18,000 t → 2025 (38,000 t; LRP revised) → Apr 2026 healthy-zone report (≈540 kt, CI 420–700). Framed by the programme's monitoring-companion review-timing identity (boundary case in the wild). |
| P4–P9 | Abstract extension; 6th highlight; discussion paragraph; conclusions paragraph; data-availability extension (RAM DOI 10.5281/zenodo.14043038 + in-repo dataset); reproducibility sentence naming the v50 verification script. |

## 2. Verification

`paperE1_cod_forecast_ladder_v50_verification.py` (standard library only): **47/47 checks pass** — regenerates every §3.8–3.10 number from the archived files (`ncam_2016_table_a2.csv`, `paperE1_calibration_data_v1_ram_timeseries.csv`, `xtencam_table17_ssb.csv`, `capelin_acoustic_observed.csv`), asserts the checkpoints (26/451/342; implied Blim 250–289, mean 275.5; capelin missing-year list), and pins the suspension facts in the text.

## 3. Build record

35 pages; zero errors; all internal references resolve; **the new sections introduce zero overfull warnings**; the build inherits the small table-layout overfulls (all ≤ 10.4 pt) of the shipped v49 longtables in §3.4–3.5, which are untouched by this edition by design (surgical diff).

## 4. Provenance of the new sources

RAM Legacy Stock Assessment Database v4.66 (10.5281/zenodo.14043038, downloaded 2026-09-24; per-year extract shipped as `paperE1_calibration_data_v1_ram_timeseries.csv`); DFO 2016 SAR Table A2 (digitized, in-repo, cross-checked 33/33 against the primary PDF); xteNCAM Table 17 (Regular et al. 2025, Res. Doc. 2025/048, digitized, checkpoints verified); suspension and reopening events: Res. Doc. 2025/048; Government of Canada news release 2024-06-26; trade press (SeafoodSource 2023-06-30; SaltWire 2025-04-08, 2026-04-02; FFAW 2025-04-03, 2026-04-01; MSC 2026-04-20). Full log: `paperE1_calibration_data_v1.md` §7 and `paperE1_calibration_data_v1_addendum.md`.

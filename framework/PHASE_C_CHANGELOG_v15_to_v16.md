# Phase C changelog — v15 → v16 (2026-09-13)

Phase C = computational campaigns (register §5): T=71; smoothed-predictand experiment; SNR power
curves; uncertainty-aware gate + hybrid rows; MCS/encompassing; per-regime decomposition; Edwards
reproducibility rerun; D3 provenance pin; pre-check candidates (4.5). One coordinated pass,
25 asserted replacement rules, applied to `paperF1_retention_framework_v16.md` (68,918 chars,
454 lines). v15 remains frozen. Verification: all old strings absent, all new strings present,
idempotent re-apply byte-identical, journal-style scan 0 blockers.

## The campaigns (inputs to the pass)

All campaigns import the frozen estimator/map/scorer from `wave_e_cod/src/run_ladder.py`
(never reimplemented) and run under `PYTHONHASHSEED=0` with the original hash-based seed map,
archived with `_provenance.json` (code shas, versions, wall time, seed policy) in
`phase_c/results/`. Reps (disclosed scaling): D1/D5 200; D2–D4 100; D6/D7 30; T=71 10;
smoother 30/arm; origins 25; SNR sweep 25. Full Amendment-1 design (8 cells × 200 ≈ 10 h)
remains registered for larger hardware.

| campaign | result |
|---|---|
| Edwards rerun (`rerun_edwards.py`) | all six archived e3-layer specs reproduce to full precision; D1 citation cell exact (M2m vs naive_persist h=5, n=71: margin −3.6607, z=−3.284, p=0.0016, CI [−5.764, −2.186]) |
| D1–D5 power (`campaign_power.py`) | fresh 0.955/0.960 (D1), 0.780/0.060 (D2), 0.110/0.100 (D3), 0.010/0.010 (D4), specificity 0.995/0.950 (D5) |
| D6/D7 + T=71 (`campaign_misspecified.py`) | D6 0.633/0.733, D7 0.933/0.867 (n=30); T=71 first execution: D1 0.900/1.000, D5 0.000/0.000 (n=10) |
| AD2 gain (`analysis_d67_gain.py`) | retained modules beat persistence in 100% of D6/D7 retention replicates; mean gain +2.6…+9.4 kt at h=1 |
| Smoother test (`campaign_smoother.py`) | assessment-like centred-3yr smoother compresses M1 persistence margin 7–13× (h=1: −8.9→−0.6 kt low-σ, −23.2→−1.8 kt high-σ); D1 power 0.90/1.00 → 0.63/0.67 |
| SNR sweep (`campaign_snr.py`) | D1 power flat 0.88–1.00 over σ∈{5,20,45}; D3/D4 power 0.00 even at σ=5 — identification limit is structural, not noise |
| Gate/hybrid/MCS (`campaign_origins.py` + `analysis_gate_mcs.py`) | uncertainty gate: D1 0.64/0.64, D2 0.24/0.00, D3/D4 0.00, D5 specificity 1.00/0.96 (n=25); MCS never eliminates persistence; true module never in 90% set for D1/D2 |
| Regime/ident (`analysis_regime_ident.py`) | power stable across realised-regime halves; truth-best-h1: D1 51–57%, D2 70–81%, D3 1–11%, D4 18–37% (same ordering as published 62.7/64.5, 25.8, 3.8); gate removal D3 31–81%, D4 50–96% (published 69/94) |
| Training profile (register 4.5) | M2 sqerr spikes 33× above persistence at the catch-regime transition (origin 1991: 14,802 vs 446 kt²) — a training-window-visible flag separating D3 from D1; does not fire for D4 |
| §4.3 reconciliation (`reconcile_s43.py`) | 18 cells: **12 PASS, 2 marginal CHANGE, 4 NEW**; mean power 0.373 (fresh) reproduces the paper's 0.376 |

## The 25 rules (each asserted to occur exactly once before replacement)

| # | location | change |
|---|---|---|
| R01 | Abstract | D1/D2 high-σ cells updated to fresh point estimates (0.985→0.960, 0.130→0.060) |
| R02 | Abstract | "T=71 benchmark…not executed" → executed 2026-09-13, n=10, with the global pinned-seed reproduction note |
| R03 | §4.2 | T=71 executed + rerun reps (D2–D4 100, D6/D7 30, T=71 10) + seed pinning archived |
| R04 | §4.3 table D1 row | 0.985→0.960 with rerun annotation (n=200) |
| R05 | §4.3 table D2 row | 0.130→0.060 with rerun annotation (n=100) |
| R06 | §4.3 table D6 row | row measure += rerun rates (0.633/0.733, within CI) + AD2 gain (+3.1/+9.2 kt h=1, 100% beat persistence) |
| R07 | §4.3 table D7 row | row measure += rerun rates (0.933/0.867) + AD2 gain (+2.6/+9.4 kt h=1) |
| R08 | §4.3 | "T=71 not executed, reported as not done" → first execution disclosed; 200-rep design registered |
| R09 | §4.4 | identification fresh-pin appended (51–57/70–81/18–37/1–11%; gate removal 31–81/50–96% — same ordering) |
| R10 | §4.4 | headline ranges 97–99% → 95–99% / 96–99% (fresh 0.995/0.950, 0.955/0.960) |
| R11 | §6 table | D1 0.965/0.960, D2 high-noise 0.060 |
| R12 | §7 | "(D1 0.965/0.985)" → "(D1 0.965/0.960)" |
| R13 | §7 | T=71 executed sentence + measured costs 13–110 s/pass |
| R14 | §7 | D6/D7 sentence gains rerun rates (n=30, within CI) |
| R15 | §7 | specificity summary 97–99% → 95–99% |
| R16 | §7 | "recovers true autonomous 97%" → 96% |
| R17 | §7 | "over-retains 68–98%" → 63–93% (pinned-seed rerun) |
| R18 | §7 | pass-cost claim replaced with measured ranges (2.2–16.7 s T=33; 13–110 s T=71; D1_T71 95–110 s) |
| R19 | §7 | reproducibility sentence extended (numpy 2.3.5/scipy 1.17.1/pandas 2.2.3; Edwards layer exact; §4.3 within CI) |
| R20 | Appendix | "D1 0.965/0.985 power exceeds 80% bar" → 0.965/0.960 |
| R21 | Appendix | "D2 0.710/0.130 near bar / below" → 0.710/0.060 |
| R22 | Appendix | D6/D7 line gains rerun rates |
| R23 | §4.5 | mean-power 0.376 provenance resolved (fresh 0.373, within CI); new disclosed post-hoc paragraph: uncertainty-aware gate, hybrid, MCS (values above) — verdicts unchanged in direction, persistence in every 90% confidence set |
| R24 | §4.6 | third pre-check candidate: training-window profile curvature / regime-transition flag (D3 pinned to the 1991–92 catch transition; D4 unexplained; open problem stands) |
| R25 | §6 | smoother experiment executed: margin compression 7–13×, power 0.90/1.00→0.63/0.67 — real but not sufficient alone |

## What did NOT change

- All qualitative verdicts (retention decisions) — frozen; the two marginal numeric cells keep
  their verdicts ("above bar" / "below bar").
- D3/D4/D5/D6/D7 published point values — all PASS the binomial test; kept with rerun notes.
- The frozen 5% band, Table 2b labels (AD2), the AD4 future-only band sentence, and the
  AD6 reporting-standard framing.
- Everything outside §4.2–§4.6, §6, §7, Abstract, Appendix.

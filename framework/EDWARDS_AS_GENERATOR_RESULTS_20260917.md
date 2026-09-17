# Edwards-as-generator suite — landed results and registration (2026-09-17)

Owner-directed item (strengthening-plan §2b). Discovery this turn: the suite was
already executed 2026-09-16 under the frozen sheet (`framework/
campaign_edwards_band_calibration.py`, full mode) and survived in the workspace;
this note extracts, reconciles, and registers it. Nothing was recomputed.

## What the suite is

Six cells × 100 reps/cell × 31 bands (0–15% by 0.5%), T = 90, σ = 12.34,
wall 233.1 s, seeds pinned by MD5 salt, PYTHONHASHSEED=0. Generators are
Edwards-native structures fitted on the archived panel
(`wave_e_edwards/data/annual_panel.csv`):
- E0 persistence null (specificity)
- E1 AR(1) (the retained-point-rule module)
- E2 water-balance map with realised fluxes R,P
- E2m same map under climatological fluxes — class-grounds gate applies;
  recorded under the with-decline convention (power 0 at all bands, disclosed)
- E3 water-balance + AR(1) residual
- E4 delayed information
Prerequisite self-test PASSED before scoring: under constant fluxes the M2 step
reduces to AR(1) to machine tolerance for every cell's fitted coefficients
(E2m reduction, sheet 3a) — abort-on-fail did not trigger.

## Frontier (exact counts, Wilson discipline per sheet 4b)

- Qualifying window (power ≥ 0.80 AND specificity ≥ 0.90): bands 0–9.5%
  (20 of 31). Adopted band per frozen rule = smallest qualifying = 0.000
  (strict-domination; harness comparison is "+>"-free).
- At adopted band 0: power E1–E4 = 1.000/1.000/1.000/1.000 (400/400,
  Wilson [0.9905, 1.000]); specificity 0.900 (200 draws; Wilson
  [0.8506, 0.9343]) — exactly at the registered 90% bar, extra-precision note:
  the bar is met inclusively at this cell count.
- 5%-row reconciliation: the pre-registered 5% band lies INSIDE the qualifying
  window — power 0.995 (398/400; Wilson [0.9820, 0.9986]; single miss in E1 and
  E3), specificity 0.990 (Wilson [0.9643, 0.9973]). Reported verdicts
  (E3 L311 point-rule M1 retention vs unified-rule withholding) are a recorded
  rule-version difference and are unchanged; band-adoption changes no verdict.
- Power decay: band 0.10 → mean power 0.7825 (E1 0.48 first to erode), spec 1.0;
  band 0.15 → 0.415, spec 1.0.

## What this closes — and what it does not

Closes (for the Edwards side) the portability asymmetry named in the
strengthening plan §2: true Edwards-native generators (AR(1); real-flux water
balance; residual-structured; delayed-information) are recovered at every
qualifying band, and the null refrains — the same signature the cod-side
D1/D5 suite shows, now exhibited on the second system's own structures.

NOT claimed here (scope discipline):
1. Generators AND estimators are Edwards-native (same-domain self-measurement).
   The cross-domain variant (cod ladder vs Edwards DGPs or vice versa) remains
   open and would be a separate frozen sheet.
2. E2m-as-truth is recorded with-decline: the detecting ladder declines it on
   class grounds by construction (it IS AR(1) under the constant-flux map) —
   recovered only through the E1 cell it reduces to.
3. M3/M4 were never simulated as generating truth on the cod side either;
   E3/E4 cells here partially answer that for Edwards.

## Companions
Origin-2024 first scoring (extracted separately, E3-owned):
H_2025 = 629.7684 ft (provisional USGS J-17, 2026 vintage); persistence
633.93 (err 4.17) vs M1 644.10 (err 14.33) → M1 NOT retained at h=1;
M2/M3/M4 deferred (P_2024/P_2025 archived NaN); h=5 awaits the 2029 actual;
certificate N2. Band-invariance recorded: no 2024 h=1 margin falls inside any
band, so band 0 vs 5% changes no verdict.

## Registration
- Archive: phase_c/results/edwards_band_calibration_full_20260916.json
  (md5 611440eeba6f1b92fc6a8c6167e39c7d). Harness: framework/
  campaign_edwards_band_calibration.py (md5 26bb9780fba29011493685b650950237).
- Ledger rows added 2026-09-17 (append-only): CL-INST-EDW-GENSUITE (F1,
  frozen), CL-EDW-GENPARAM (E3/ARCHIVE pointer to panel+harness fits, frozen),
  CL-EDW-ORIGIN2024 (E3, parked — provisional target, h=5 pending 2029).
- F1 pointer discipline: this note is the citable artifact; no paper text was
  modified. A future F1 supplement version may cite framework/claims_ledger/
  claims_ledger.csv rows CL-INST-EDW-GENSUITE and CL-EDW-ORIGIN2024.

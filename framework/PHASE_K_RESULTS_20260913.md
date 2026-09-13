# Phase K results — O6 prospective-registration execution (2026-09-13)

The §8 prospective-registration items, executed to the extent the registration
itself permits. The registration sequence is binding: band calibration precedes
any new-origin scoring; nothing here scores an origin before its calibration.

## 1. Cod band calibration — EXECUTED (result: 5% band retained)

Script `phase_c/o6_cod_band_calibration_20260913.py`; archive
`phase_c/results/o6_cod_band_calibration_20260913.json`. The §8 procedure run
on the pinned-seed T=33 archive (200/100 reps per cell — the registered
machinery), all bands 0–15% in 0.5% steps evaluated on the same replicates
(no refit per band).

- **Validation:** at the 5% band the recomputation reproduces all ten published
  cells exactly (0.955/0.960, 0.780/0.060, 0.110/0.100, 0.010/0.010,
  0.995/0.950; pooled 0.3731/0.9725 vs published 0.373/0.973).
- **Frontier:** mean power 0.444 (band 0) → 0.312 (band 15%); specificity 0.760
  → 1.000. Narrowest band meeting the specificity target alone: 3.5%
  (specificity 0.935, power 0.395). **No band attains power ≥ 0.80 and
  specificity ≥ 0.90 — power is identification-limited at every width.**
- **Outcome per §8:** the attainable frontier is reported; the 5% band is
  retained for the cod application. Reported verdicts untouched.
- **T=71 (Spec B's own length):** only the registered ten-replicate point
  exists (D1 power 0.900/1.000, D5 specificity 1.000/1.000 at the 5% band).
  The full 200-replicate T=71 frontier remains the registered campaign (O5) —
  to be completed before Spec B origin scoring begins.

## 2. Edwards band calibration — DRAFT sheet registered (owner-gated)

`specifications/SPECIFICATION_prospective_band_edwards_DRAFT.md`. Six cells
(persistence null + five in-class truths), T=90, σ=12.34 ft, 100 reps per
cell, band sweep 0–15% in 0.5% steps, estimators imported from the Edwards
ladder code (never reimplemented). Owner-gated choice: the class-grounds
convention for the fitted M2m (proposed: mirror the frozen protocol). No
simulation runs until the sheet is approved and frozen.

## 3. Data availability records

- **Edwards panel (origin-2024 inputs) already archived:** 2024 H 633.93 ft
  (provisional) and R 154.0; 2025 H 629.77 ft (provisional) — the h=1 target
  for origin 2024. P_2024 (pumpage) is unarchived → M2's persisted-flux score
  waits; M1/M2m/M3/M4 score with the archived inputs. 2026 H incomplete
  (235 days at archive time).
- **Cod Spec B vintage trigger:** the 2026 DFO assessment (1 Apr 2026)
  published the new xteNCAM vintage (SSB ≈ 540 kt, 420–700; healthy zone;
  quotas 18,000→38,000 t). Origin 2025's forecast target year is 2026 → scored
  once the 2027 vintage is published. Archive-grade extraction of the vintage
  table needs the official DFO Science Advisory Report.

## 4. Paper

v24_restructured: §8 gains the executed-calibration paragraph (frontier
numbers, retained 5% band, T=71 point, Edwards sheet registration, Spec B
scoring timeline); Data availability gains the calibration archive path. All
scanners green; coverage clean; idempotent.

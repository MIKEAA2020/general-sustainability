# Companion Cross-Check — F1 v21_restructured vs newest E1/E3 (2026-09-13)

Merged-plan item O7, executed against the newest companion copies in the
workspace: `e1/paperE1_cod_forecast_ladder_v49.tex` (E1) and
`e3/paperE3_edwards_forecast_ladder_v16.md` (E3), plus the cited archives
(`batch 7 (audits of agent arena 1 paper rewrites)/results/e1_dm_uncertainty.csv`,
`wave_e_cod/results/rolling_summary.csv`, `xte_rolling_summary.csv`,
`wave_e_edwards` climate tables). Verdicts: two findings (NEW-4a text fix,
NEW-4b archive fix), everything else verified consistent.

## 1. Titles, records, citations — VERIFIED

| F1 claim | Companion source | Result |
|---|---|---|
| Abaee 2026a = "Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17", zenodo.22552680 | E3 title line 20; E1 v49 refs cite 2026a = 22552680 | ✓ |
| Abaee 2026b = "Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL", zenodo.22553609 | E1 v49 title; E3 v16 refs cite the cod companion = 22553609 | ✓ |
| "Table 8 of companion" = capelin index module (E1) | E1 v49: "the index modules' origin sets (Table 8)" | ✓ |
| "Table 7 of the Edwards companion" = climate table (E3) | E3 v16 Table 7 | ✓ (Phase F NEW-3) |
| xteNCAM (Regular et al. 2025); LRP 884.6 / 276 kt | E1 v49: LRP 884.6 (1983–2015), 276 kt (95% CI 180–423) | ✓ |

## 2. Cod numbers (F1 Tables 2/3 vs E1 v49) — VERIFIED

| F1 | E1 v49 | Result |
|---|---|---|
| Spec A persist 98.05; M1b 114.80 (+17.09%) | "(114.80−98.05)/98.05 = 17.1%" | ✓ |
| Spec A h=5 M1b 288.58 / M1 288.72 (closest = M1b) | M1b 288.6, M1 288.7 (closest = M1b) | ✓ (F1 carries CSV precision) |
| Spec B persist 87.65 / 317.71; origin-matched 84.43 / 299.98 | 88 / 318; 84.4 / 300.0 | ✓ (E1 rounds; 3.22 kt = 88−84.4 apparent 3.6 kt rounding artefact) |
| Spec B M1 119.47 (+36.30% mixed, +41.50% matched) | 119.5 vs 88 / 84.4 | ✓ |
| capelin 97/193 (n=24/20), 79/288 (n=36/32); 150.02/262.34, 132.02/491.74; 264.72→193 shift | n=24/20, n=36/32, "1988 (n=36 at h=1, n=32 at h=5)"; 150/262, 132/492; 193 kt matched | ✓ |
| M4 Spec A coarse-regime 195.6 vs 206.3 annual landings | 195.6 (coarse) | ✓ |
| n=63/59 naive vs n=59/55 structural (Spec B) | "n=59/55"; mixed-origin over longer naive sets | ✓ |

## 3. Cod DM universe — VERIFIED against the cited archive

- "5 of 32 rows" computed exactly from the cited batch-7 replication: rows with
  CI excluding zero and |z|<1.96 = {A h1 M4vM3 (z=0.99), B h1 M3vP (z=1.85),
  B h5 M1bvP (z=1.80), B h5 M4vM3 (z=1.88), B h5 M2vM1b (z=1.93)} — the fifth
  being one of the four alternative-comparator M2-vs-M1b rows. ✓
- F1's three worked examples match the archive exactly (z=0.99 [4.7,144.7];
  z=1.85 [1.0,92.5]; z=1.88 [20.2,177.4]). ✓
- E1 v49's own DM table prints z=1.21, [4.4,134.4] for the A h1 M4vM3 row
  (its coarse-regime pass; M4 195.6 vs the replication's annual-landings 206.3).
  Companion-side difference; F1's cited source matches F1. Flagged for the
  E1 finalization pass; no F1 edit.
- E1 v49's "four of the twenty-eight" wording is consistent with F1's
  "companion's 28-row subset excludes" the four alternative-comparator rows. ✓

## 4. Edwards numbers (F1 §4/Tables 4, 5, 5b vs E3 v16) — VERIFIED except NEW-4a

| F1 | E3 v16 Table 4/5 | Result |
|---|---|---|
| persist 13.23/21.11; M1 12.84/21.25; M2m 12.28/17.44; M2 14.70; oracle 7.55 (10.87); training mean 16.80 beats persist at h=5 | identical | ✓ |
| margins: M1 h1 −2.96%; M2m h1 vs M1 −4.33%; M3 h1 −1.63% (vs M2); M4 h1 −1.13% (vs M3); M3 h5 −0.08% (vs M2); M4 h5 −0.21% (vs M3) | M2 14.70, M3 14.46, M4 14.30 at h1; M2 33.49, M3 33.46, M4 33.39 at h5 | ✓ |
| band 12.57 = 0.95×13.23; 20.05 = 0.95×21.11 | (E3 has no band — point rule) | ✓ arithmetic |
| climate Table 5b rows | E3 Table 7 | ✓ (NEW-3, Phase F) |

**NEW-4a (adjudicated, fixed in v22):** E3 v16 retains M1 at h=1 by its
pre-registered point rule ("retained (point rule; margin within noise)",
one-year RMSE-level statement, no band, h=1-only). F1's unified rule (5% band,
both horizons) withholds M1, and F1's §4 never reconciled the companion's
verdict. Fix: F1 §4 now states the reconciliation — the companion's h=1 point
rule retains M1 provisionally (0.39 ft margin within noise, MAE tie, five-year
loss); the unified rule withholds it (2.96% h=1 margin inside the band; h=5
loss); the empty retained set is a property of the unified rule, and the M1
difference is a recorded rule-version difference, not a data difference. The
"no outcome changes" sentence is sharpened (band + both-horizon addition
changes no outcome within the unified rule).

**NEW-4b (adjudicated, archive fixed):** the O9 co-primary IC check
(`phase_c/results/o9_ic_coprimary_20260913.json`) derived Edwards M3/M4 RMSEs
(12.483/12.624 ft) by misapplying F1's comparator margins (which are vs M2/M3,
not vs M2m). Corrected to the companion's Table 4 values (M3 14.46, M4 14.30);
IC(M3)=486.8, IC(M4)=484.8 — still above M2m's 455.5, so the IC-best on
Edwards remains M2m and the paper's §6.5 block is unaffected (it cites only
M2m/M1/persistence). JSON and runner note regenerated.

## 5. Verdict

O7 executed as-of the current companion versions: **every F1-companion number
verified consistent** except the two adjudicated findings above. The check
re-runs when E1/E3 are finalized (event trigger).

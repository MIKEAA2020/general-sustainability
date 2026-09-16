# Edwards band-calibration campaign + first-origin-2024 scoring (2026-09-16)

## Campaign (registered, executed this pass)

- **What ran.** The registered 100-rep-per-cell calibration, one flag:
  `PYTHONHASHSEED=0 python3 framework/campaign_edwards_band_calibration.py --full`.
  6 cells × 100 reps × 31 bands, band sweep on shared replicates (frozen design).
  Wall 233 s. Harness artifact corrected post-run: the JSON kept the dry-run
  filename/frontier_note while running `--full`; archived as
  `phase_c/results/edwards_band_calibration_full_20260916.json`.
- **Frozen-rule outcome.** 20 bands attain power ≥ 0.80 ∧ specificity ≥ 0.90
  (the pooled frontier, mean over E1–E4; E2m declined by class-grounds every
  band — sheet §3a/§4). Smallest qualifying band = **0.000** (power 1.000,
  specificity 0.900). The 5% pre-registered band is inside the qualifying
  window (power 0.995, specificity 0.990).
- **Why it looks like cod's mirror image (root cause, not a defect).** Cod's
  pooled campaign (T = 33, σ up to 33.8) is identification-limited (max power
  0.4437 at band 0 → frontier + 5% retained). Edwards' window is much longer
  relative to its noise (T = 90, σ = 12.34) and the fitted M2 self-correction
  δ ≈ −0.273 makes the objects separable at near-zero margin, so even band 0
  attains both targets. Same rule, two regimes; nothing retuned.
- **Adopted band for future Edwards applications: 0** (strict beat of the
  baseline and the next-simpler comparator), basis stated. The 5% band's
  presence inside the qualifying window confirms the pre-registration rather
  than overturning it; reported (L311) verdicts remain decided by the
  pre-registered 5% band and are unchanged — the calibration governs future
  verdicts only.

## First origin 2024 — provisional scoring (h = 1 now; h = 5 at the 2029 actual)

Scored against the archived 2025 actual (H 629.77 ft, provisional), fit window
through 2023, at the adopted band 0.

| Module | Forecast | Error | Verdict (h=1) |
|---|---|---|---|
| M1 (AR(1)) | 644.10 | +14.33 | **not retained** (|14.33| > |4.17| persistence) |
| M2 (persisted-flux) | — | — | deferred (P_2024 unarchived) |
| M3 (residual AR) | — | — | deferred (P_2025 unarchived) |
| M4 (delayed info) | — | — | deferred (P_2025 unarchived) |
| M2m | — | — | excluded: declined on class grounds (with-decline) |

M1 does not beat persistence at band 0 — and the margin lies outside every
band, so the adoption of band 0 vs the 5% band changes nothing on this cell.
The H3 verdict needs both horizons; **h = 5 scores at the 2029 actual.** The
deferred modules score only when the pumpage/recharge inputs exist (sheet §6.3).
Artifact: `phase_c/results/edwards_origin2024_scores_20260916.json`.

## Cod Specification B — why it was NOT executed in this pass

Deep root-cause memo: `framework/COD_SPECB_ROOTCAUSE_20260916.md`. Three
coupled problems; the data-availability one (A) is resolved (post-2026
assessment vintage), the T = 71 identifiability one (B) is deferred by frozen
sheet v4, which places T = 71 outside the core design (§83/§96/§237) — its
harness runs a 25-rep exploratory geometry, no T = 71 band-sweep script exists,
and executing against that freeze is exactly the pressure-driven scope
expansion the sheet exists to prevent. Execution (C) follows B. Trigger:
a dedicated pre-registered Spec-B sheet (new sheet, adopting §3a/§4 as-is)
+ owner approval.

## Close-out (this pass)

NEW-20/NEW-22 and O34/O35 closed as bequeathals (none highly merited in-version;
fold points recorded). Edwards: campaign done, band adopted, first origin
scored provisionally — the remaining registered gates are the deferred inputs
(P_2024/P_2025, R_2025) and the 2029 actual.

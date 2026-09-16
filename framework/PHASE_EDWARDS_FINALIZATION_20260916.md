# Edwards prospective band calibration — finalization and root-cause harness finding (2026-09-16)

## What was finalized

1. **Owner review closed** (`OWNER_REVIEW_20260913_RELAXATION_AND_PHASING.md` §6):
   NEW-20 (certificate-level semantics — filed with a home at the NEW-21
   submission pass) and NEW-22 (extended instrument grid — bequeathed to the next
   registered campaign) settled as bequeathals; no actionable review item remains.
2. **Spec sheet FROZEN** (`specifications/SPECIFICATION_prospective_band_edwards_DRAFT.md`,
   2026-09-16): O19 criterion at §3a, E2m convention DECIDED with-decline at §4
   (root-cause memo in-sheet), §6 sequence and §7 owner-gate updated to future tense.

## Root-cause method applied to the harness

- Estimators/maps/scorer IMPORTED from `wave_e_edwards/src/run_ladder.py`
  (never reimplemented — cod convention).
- **E2m-collapse self-test as the first gate**: before any scoring, the harness
  asserts that the M2 map with constant (climatological) fluxes is analytically
  equal to the AR(1) x → C + (1+δ)x for every fitted cell; on failure the campaign
  aborts. This is §3a's as-implemented reduction, and it is what makes the
  E2m-row power = 0 at every band a *protocol feature*, not a missing cell.
- Duplicate-symbol hazard (path_errors / self_test / sim_persistence exist in
  several tools) guarded by qualified names and a repo-root anchor.

## The dry-run finding (root cause, not a defect to patch)

Dry run (3 reps/cell, pools over the full band sweep on shared replicates) is
**degenerate**: specificity = 1.000 at all 31 bands and power = 1.000 up to the
9% band. The cause is measured, not guessed: at T = 90 with σ = 12.34 and the
fitted M2 self-correction δ ≈ −0.273, a random-walk null is separable from the
in-class truths by inspection, so no band can catch a false positive and every
in-class truth is already above every tested margin. This is the *Edwards*
regime — longer window relative to noise than the cod campaign (T = 33, σ up to
33.8), whose .373/.973 pool was genuinely noisy.

**Consequence, honestly recorded:** the calibration will not reproduce the cod
"no band attains both targets" result, because the target quantities differ by
regime. The frozen sheet's decision rule is unchanged and survives either
outcome: with 100 reps/cell it returns the smallest band attaining
power ≥ 0.80 ∧ specificity ≥ 0.90, and otherwise reports the frontier (and then
the 5% band is retained, per the sheet).

**What was NOT done (the shallow fix):** retune σ, T, or the cells to make the
Edwards frontier look like the cod one. That would manufacture a familiar answer
rather than measure the Edwards one; the regime difference is the finding.

## What remains registered, not speculative

- Full campaign `PYTHONHASHSEED=0 python3 framework/campaign_edwards_band_calibration.py --full`
  (100 reps/cell × 31 bands × 6 cells ≈ 50 min dry-run-scaled; pinned-seed
  per band/cell/rep, provenance JSON archived alongside).
- After the campaign: adopt the smallest qualifying band (or frontier + 5%),
  then score first new origin 2024 (h=1 now; h=5 at the 2029 actual; M2's
  persisted-flux score waits on P_2024).
- Cod Spec-B T=71 frontier and Spec-B origin 2025 remain owner-gated and
  untouched (sheet §7).

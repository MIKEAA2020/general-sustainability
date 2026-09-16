# Specification — Prospective band calibration, Edwards J-17 ladder (DRAFT for approval)

**Status:** FINALISATION-GATED (2026-09-16). Both previously-open choices are
now resolved in-sheet: the prospective class-grounds criterion (§3a) and the
E2m convention (§4 — with-decline, mirroring the frozen protocol). No design
element remains open. Once finalised (this sheet, dated 2026-09-16), it is
frozen and the campaign runs under PYTHONHASHSEED=0 with seeds pinned and
archived (the Phase C convention).
Purpose: the Section 8 procedure of the framework paper — before the first new
Edwards origin (2024) is scored, the object's own ladder is simulated at its
own series length and noise scale, and the smallest band attaining power ≥ 0.80
and specificity ≥ 0.90 is adopted; if no band attains both, the attainable
frontier is reported and the 5% band is retained.

## 1. Ladder and rule (frozen, Section 4/5.2 of the framework paper)

Candidates: persistence, training mean, M1 (affine AR(1)), M2 (one-pool
stock-flow, persisted fluxes), M2m (climatological-flux map), M3 (M2 + AR(1)
residual), M4 (delayed information); the oracle is excluded from retention.
Unified rule: H2 — beat persistence at h=1 and h=5 by (1−b); H1 — beat the
next-simpler comparator by (1−b) at both horizons (M1: none; M2→M1; M2m→M1;
M3→M2; M4→M3); H3 — both horizons. The band b is swept 0–15% in 0.5% steps,
all bands evaluated on the same replicates (no refitting per band), exactly as
the cod archive method.

## 2. Simulation design

- Series length T = 90 (the Edwards record 1934–2023), origins per the rolling
  design (minimum training window 8 years), noise σ = 12.34 ft (the paper's
  SD(Δtarget) scale for Edwards).
- Estimators, maps, and scorer are imported from `wave_e_edwards/src/run_ladder.py`
  (never reimplemented) — the cod convention.

## 3. Generating truths (in-class members + null)

| Cell | Truth | Generation |
|---|---|---|
| E0 | persistence null | H_{t+1} = H_t + ε (specificity) |
| E1 | M1 AR(1) | fitted 1934–2023 coefficients (φ̂ = 0.66); iterate + ε |
| E2 | M2 stock-flow, persisted fluxes | fitted map; fluxes = archived annual R, P series (real-flux design) |
| E2m | M2m climatological-flux map | fitted map; fluxes = climatological means (constant) — an AR-equivalent series by construction |
| E3 | M2 + AR(1) residual | fitted map + persisted residual (φ_r fitted) |
| E4 | delayed information | E3 with lag-1 start state |

## 3a. Prospective class-grounds criterion (O19)

The class-grounds check is a pre-gate: it is evaluated before any scoring, is
declared with reasons, and once declared it is not re-opened by the scores.
This section registers the concrete criterion in advance.

For each candidate module, before any replicate is generated:

1. **As-implemented reduction.** Simulate the module's fitted map under its
   *as-implemented* driver conditions. If it is mathematically equivalent to a
   forward-simpler ladder member under those conditions — M2m with
   climatological (constant) fluxes collapses to an affine AR(1), i.e. to M1 —
   the module is declined on class grounds for every scoring under those
   conditions.
2. **s → 0 boundary check.** A module whose distinguishing parameter may sit
   at its boundary under the generating truth (M1b's depensation threshold
   s → 0 reduces the Allee branch to the Schaefer branch) is checked at the
   boundary; if the boundary form is the simpler member, the module is not
   evidence for the mechanism it names.
3. **Declaration.** The outcome for every candidate is written into the
   run-log before step 4 (generation). The frozen output vocabulary
   {retained, not retained, declined on class grounds} is unchanged; the
   criterion only makes the third output's trigger explicit and auditable.

Approximate collapse — a flux variance small but nonzero, a threshold near but
not at zero — is not a class-grounds basis: it is an operating-
characteristic question and is measured, not vetoed.

## 4. Class-grounds handling (convention DECIDED 2026-09-16: mirror the protocol)

**Decision (2026-09-16): with-decline — mirror the frozen protocol.** The frozen
protocol declines M2m on class grounds (collapses to AR(1) under constant
fluxes). In simulation the decline applies mechanically to the fitted M2m.
Power for E2m-truth is reported **both** with and without the decline (the
without-decline number stays visible), and the **primary** number — the one the
adequacy targets and the power ≥ 0.80 mean are computed against — is the
with-decline.

**Root cause.** The question is what "power for E2m-truth" is power *for*. The
class-grounds decline is an analytical reduction, not a scoring event: under
constant fluxes the fitted M2m *is* an AR(1), so its parameters carry no
structure beyond the simpler member regardless of its RMSE. The instrument can
never "retain" M2m — measuring its power without the decline measures a cell
that cannot occur under the protocol, and would misstate the very quantity the
calibration exists to report (the protocol's evidential reach). The
without-decline number is informative as a sensitivity — it says what the rule
*would* see if the decline were dropped — so it is kept alongside, not deleted.

**What was rejected.** Setting the decline aside once, "to see both fairly",
would let the simulation silently redefine the target cell post-hoc — the E2m
cell's power would no longer describe the frozen protocol it calibrates, and the
adequacy verdict (smallest band attaining the targets) would be computed against
a different object than the one Section 4 freezes. That is the quick fix; the
honest fix is to keep the decline where the protocol puts it and disclose the
counterfactual.

## 5. Design parameters

- Replicates: 100 per cell (6 cells → 600 simulations; ≈1–2.5 CPU-hours on the
  two-core machine, by the cod cost rates).
- Adequacy targets: mean power ≥ 0.80 over the five in-class cells; specificity
  ≥ 0.90 over the null. Outcome: smallest qualifying band, or the frontier
  reported with the 5% band retained.
- Pre-registration declares, before any run: seed map (salt by cell and rep),
  the band grid, the comparator map, the class-grounds convention, and the
  adequacy targets. No design element is tuned to a result.

## 6. Sequence and data

1. Approval → sheet frozen (dated; supersedes this draft by a new sheet, never
   an edit).
2. Campaign runs; provenance JSON archived with the results.
3. Band adopted (or frontier + 5%) → first new origin (2024) scored: h=1
   scored now (2025 actual archived: H 629.77 ft, provisional); h=5 at the 2029
   actual; the verdict needs both horizons (H3). M2's persisted-flux score for
   origin 2024 waits on the 2024 pumpage value (P_2024 currently unarchived);
   M1/M2m/M3/M4 score with the archived inputs.
4. The 2024–2025 panel rows are already archived (`wave_e_edwards/data/annual_panel.csv`).

## 7. Cod side (for completeness)

Cod calibration executed on the pinned-seed T=33 archive — no band attains both
targets; the 5% band is retained and the frontier is reported (Section 8 of the
framework paper; `phase_c/results/o6_cod_band_calibration_20260913.json`).
Specification B's own T=71 frontier awaits the registered 200-replicate
campaign; the first Spec B origin (2025) is scored once the vintage following
the 2026 assessment is published.

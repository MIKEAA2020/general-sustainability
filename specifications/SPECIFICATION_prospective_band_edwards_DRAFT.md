# Specification — Prospective band calibration, Edwards J-17 ladder (DRAFT for approval)

**Status:** DRAFT (2026-09-13). No simulation is run until the owner approves
this sheet. Once approved, it is frozen, dated, and the campaign runs under
PYTHONHASHSEED=0 with seeds pinned and archived (the Phase C convention).
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

## 4. Class-grounds handling (owner-gated choice, proposed: mirror the protocol)

The frozen protocol declines M2m on class grounds (collapses to AR(1) under
constant fluxes). In simulation the decline applies mechanically to the fitted
M2m. Power for E2m-truth is reported **both** with and without the decline; the
adopted convention mirrors the frozen protocol (with decline). The owner may
choose the without-decline convention instead before the sheet is frozen.

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

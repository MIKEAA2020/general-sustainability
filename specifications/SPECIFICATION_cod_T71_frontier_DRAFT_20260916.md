# Specification — Cod Specification-B band calibration at T = 71 (DRAFT for owner approval)

**Status:** DRAFT (2026-09-16). This is a **new sheet** — it does not edit or
amend `SPECIFICATION_v4.md` (LOCKED 2026-09-10). Its purpose is narrow and
explicit: to lift the `T = 71` cells from "declared but deferred" (v4 §96) into
their own pre-registered execution, matching Specification B's own window
(1954–2024, T = 71) so the *Spec-B* verdict's band can be calibrated at the
Spec-B series length rather than inherited from the T = 33 core. Nothing here
re-opens any reported verdict; the frozen cod pooled result (no band attains
both targets at T = 33; 5% band retained) stands for the T = 33 objects.

**Owner gates (resolved exactly as the Edwards sheet resolved them):**

- **§3a class-grounds criterion** — adopted as-is from the Edwards sheet:
  as-implemented reduction → s → 0 boundary check → declaration before
  generation. For cod: M2m does not exist here; the class-grounds candidates
  are M1b (s → 0 boundary against M1) and any module-as-implemented reduction
  declared before scoring. Approximate collapse is an operating-characteristic
  question, not a veto.
- **§4 convention** — adopted as-is: with-decline. A module whose
  as-implemented reduction is declared is declined, never scored (power = 0 at
  every band), and the counterfactual is kept visible as sensitivity.

## 1. What is lifted verbatim from v4 (frozen, no drift)

From v4 A1.3–A1.5 (the registered-but-deferred T = 71 addendum), unchanged:

- **Cells:** `D1_M1_collapse` and `D5_persist_null` at `T = 71`, the strongest
  in-class process and the persistence-true null ("tests length sensitivity for
  both power and specificity without re-running every cell" — v4 A1.3), **plus**
  the misspecified-amendment cells `D6` (threshold production, K = 950.8 general
  recovery bound) and `D7` (observation-error-only state), each at `σ ∈ {11.8, 33.8}`
  (`σ` scales as in v4 A1.2 — the two v4 noise levels).
- **Replicates:** 200 seeded per cell (v4 A1.4); `σ ∈ {11.8, 33.8}`.
- **Rule:** the frozen pre-registered retention rule, applied unchanged
  (v4 A1.4). Ladder, comparators ({M1: none, M1b→M1, M2→M1, M3→M2, M4→M3}),
  output vocabulary, horizons (1, 5), and the 5% tie band are all inherited
  frozen from v4.
- **Elements still deferred (not lifted):** `σ = 0` and `𝔰 ∈ {5, 30}` — v4 §96
  leaves these deferred and this sheet does not change that.

## 2. Registered refinement (this sheet's only addition)

v4's T = 71 addendum checks D1 power / D5 specificity **at the 5% band only**
(the single-row test in A1.5, length-sensitivity threshold 0.15). This sheet
runs the **band sweep 0–15% in 0.5% steps** on the same replicates — i.e. it
applies the §8 prospective procedure at the Spec-B window, exactly as the
Edwards sheet does for Edwards. This is a superset of v4's single-band check,
not a contradiction of it: the 5% row must be reproducible from the sweep, and
the first execution action (§4 below) reconciles it against the observed pilot
points (D1 power 0.900/1.000, D5 specificity 1.000/1.000 at band 5%,
n = 10 — accepted at face value as motivation, not as a substitute for the
200-replicate resolution).

## 3. Harness and provenance (cod-native, same pattern as the Edwards harness)

- Harness: `phase_c/campaign_cod_t71_band_calibration.py` (new), mirroring the
  archived `o6_cod_band_calibration_20260913.py` band-sweep logic on the
  `sim_origins_20260913.csv` schema (T = 71, `band_retained` per band), with a
  per-origin persistence-baseline recomputation (no single shared den).
- Estimators/maps/scorer IMPORTED from `wave_e_cod/src/run_ladder.py` (never
  reimplemented). Seeds pinned per (cell, σ, rep, band); `PYTHONHASHSEED=0`;
  provenance JSON archived with the results.
estimated cost: 8 cells × 200 reps × 2 σ × 31 bands ≈ 3.1 h at the archived
  `sim_origins` rate (1,718 s for 25 reps × 2 σ), inside the sandbox window.
- Runtime guard: a wall-clock cap may abort the run; the sidecar
  `phase_c/results/cod_t71_calibration_partial_20260916.json` (cells completed
  so far, provenance) is written per finished σ-scale so a partial run is
  resumable and never silently half-pooled.
- Self-gates before `--full`: (a) the 5% row reconciles with the pilot points;
  (b) D1 at T = 71 tracks v4's length-sensitivity check against T = 33.
- Seed map, declared before any run: `seed(cell, σ, rep) = MD5("cod_t71_2026-09-16:{cell}:{σ}:{rep}") mod 2^31`
  (same MD5-salt convention as the Edwards campaign, `edwards_band_calibration_2026-09-16`,
  so a leaked convention cannot masquerade as a new draw); `PYTHONHASHSEED=0`.

## 4. Sequence

1. Owner approval → this sheet frozen (dated 2026-09-16 on approval).
2. Harness written; dry-run (3 reps/cell/band) reconciled against the pilot
   5% points; only then the 100→200-rep full campaign.
3. Outcome: smallest band attaining power ≥ 0.80 ∧ specificity ≥ 0.90 at T = 71,
   or the attainable frontier reported and the 5% band retained (mirrors the
   frozen §8 rule). D6/D7 false-retention answered against v4's own 0.10
   threshold as the out-of-class control.
4. Only then is Specification-B origin 2025 scored (h = 1, once the vintage
   following the 2026 assessment publishes — A, resolved), and h = 5 at the
   2029 actual; the verdict needs both horizons (H3).

## 4a. Pooled-mean and frontier conventions (closed, no drift)

The Phase-K cod calibration's pooled frontier is reproduced here *as archived*,
with its exact weighting, so "≥ 0.80 / ≥ 0.90" inherits the same meaning:

- **Power:** the **unweighted mean over the in-class cells** (D1, D3, D6, D7's
  per-cell truth power), **each cell's value being the unweighted mean over its
  two σ scales** (σ ∈ {11.8, 33.8}). No weighting by rep count (reps differ
  across v4 cells by design: D1/D5 200, others 100 per σ — the convention
  holds the cell, not the replicate, constant).
- **Specificity:** 1 − (retention under `D5_persist_null`) at each **σ scale
  separately**, then the unweighted mean over the two scales.
- **Frontier:** the (band → power, specificity) curve is reported per σ scale
  AND pooled (unweighted mean over scales), so the σ-divergence — the very
  thing that made the cod T = 33 result band-insensitive — is visible as its
  own diagnostic, never averaged away. The adopted/smallest-qualifying band is
  chosen on the **pooled** curve, and the per-σ curves are reported alongside
  (if the two scales select different bands, the smaller is adopted and the
  split is reported).

## 4b. Monte-Carlo interval reporting

Every power / specificity / false-retention figure carries its exact count
(k/n) and a Wilson 95% score interval, matching `sim_origins`-family archived
practice. The pilot points (D1 .9/1.0, D5 1.0/1.0, n = 10, band 5%) are
reconciled at this precision at the dry-run gate: with n = 200 per cell the
0.80 / 0.90 targets are trivially separable (200 × 0.8 = 160; the 95% interval
half-width at 0.85 is ≈ 0.05), so the calibration selects the band with
decision-relevant resolution, not pilot noise.

## 5. Relationship to the other sheets

Orthogonal to the Edwards sheet (`SPECIFICATION_prospective_band_edwards_DRAFT.md`,
FROZEN 2026-09-16 — executed, band adopted 0, origin 2024 scored provisionally).
Both implement the same §8 prospective procedure at their own object's own
length; this one is the cod/Spec-B instance. No element of either frozen sheet
is edited by the other.

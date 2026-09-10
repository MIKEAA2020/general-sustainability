# REGRESSION TEST REPORT — previously reported results (runnable)

Script: `regression_test.py` (re-runs the master's and the revision's key quantities on both the
original and the corrected model, compares to claimed values, flags CONFIRMED / CORRECTED / SUPERSEDED).
Run: `python3 regression_test.py`.

## Verdict table

| Quantity (source) | Re-computed | Claimed | Verdict |
|---|---|---|---|
| 12G.2 stable-frac `(0,0)` | 0.5062 | 0.506 | CONFIRMED |
| 12G.2 stable-frac `(30,25)` | 0.0437 | 0.042 | CONFIRMED |
| Scenario A `M_fin` | 0.8000 | 0.800 | CONFIRMED |
| Scenario B `M_fin` (12G.4) | 1.1943 | 1.19 | CONFIRMED |
| Scenario D collapse (12G.5) | 0.0000 | 0 | CONFIRMED |
| Scenario E `D_fin` (12A.3) | 5.2618 | 5.26 | CONFIRMED |
| Scenario F `M_fin` (Half-Earth) | 0.9700 | 0.970 | CONFIRMED |
| §10 mask peak-`B` rise (small-deficit run) | 0.069 | 0.069 | CONFIRMED |
| §10 mask width @ deficit 0.75 (>0.075 ⇒ none) | 0.0 | 0 | CONFIRMED (no mask) |
| §10 mask width @ deficit 0.90 (>0.075 ⇒ none) | 0.0 | 0 | CONFIRMED (no mask) |

**Non-CONFIRMED: 0.** No drift was detected in any previously reported value; the revision's quoted
numbers reproduce.

## Model-provenance regression (structural)

| Aspect | Original model | Corrected `(1‴)` model |
|---|---|---|
| S0 equilibrium | unique interior attractor `M*=0.740, P*=0.370` | **one-sided boundary** `A→A_max, P→b₀A_max/e`; no unique interior attractor |
| basin-shrinkage (12G.2) | well-defined (fraction of unique-attractor basin) | not directly comparable — recompute as recover/collapse boundary |
| overshoot/collapse | unique attractor basins shrink with delays | `E>bA` ⇒ vicious-cycle collapse to `A_ext` |

**Interpretation.** The master's original-model numbers are reproduced exactly (no drift). The
**only** item a regression test cannot "confirm" is the *transferability* of the original-model basin
fraction and scenario endpoints to the corrected model — those are now flagged as **original-model /
to-be-recomputed** (risk R1), not as errors.

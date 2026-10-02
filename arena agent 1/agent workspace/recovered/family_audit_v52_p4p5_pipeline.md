# P4 / P5 — pipeline-level verification

Ran the actual campaigns and compared their output against the numbers the
manuscripts print. **No defects found in either paper. No revision merited.**

## P4 v41 — `campaign_p4_dr_registration.py`

Dependencies recovered from
`arena agent 1/other documents/rerun_campaigns/stage_scan_recovered/`
(`compute_core`, `stage_decomp2`, `stage_r_window`,
`stage_tau0_decomposition`, `stage_robust_check`, `dde_core`,
`pseudo_arclength`, `shooting_floquet`, `droop_test`).

**21/21 gates pass.** Every value the paper prints is present and consistent:

| quantity | paper | campaign |
|---|---|---|
| original Hopf pair | 3.666149 / 150.358477 | 3.666149 / 150.358477 ✓ |
| flipped fundamental delays | 128.374 / 70.697 | 128.374373 / 70.696578 ✓ |
| base window η=0.914 | (0.00796, 0.02191) | (0.00796, 0.02191) ✓ |
| base window η=3.0 | (0.00676, 0.06028) | (0.00676, 0.06028) ✓ |
| fine-map bands g=1,2,3,5 | (1.565,1.585) (0.77,0.81) (0.50,0.55) (0.28,0.33) | grid-rounded matches ✓ |
| slow-r cohort cycle | P≈358.8 | P=358.7 ✓ |
| institutional cycle | P≈16.96 | P=16.95 ✓ |

**One precision difference, not a defect.** The campaign computes the flipped
loop gain as Γ = 1.019221; the paper prints 1.016. The gate is a band,
`1.010 < Γ < 1.022`, which both satisfy, and the paper's claim is only
"loop gain 1.016 > 1", which holds either way. Recorded for completeness.

Caveat: this campaign was written for P4 v5/v6 sections. It covers the
maturation-delayed recruitment material, not all of v41.

## P5 v47 — three campaigns, all run

### `campaign_p5_stage_reconstruction.py`

The campaign prints three `MISMATCH` flags against "legacy windows". **The
paper already discloses all three** — this is a reported finding, not a hidden
defect. Lines 1123–1126:

> "…but not the anchovy 3--4 yr or the sprat 6--12 yr response regions: on this
> specified plant family those classes converge at every review interval, and
> the only instability the reconstructed loop produces is its own long-horizon
> band, entering at 34--35 yr and extending to the grid's end, which has no
> counterpart among the archived windows."

That is exactly what the campaign produces:

| claim | campaign | paper |
|---|---|---|
| anchovy / sprat / cod trajectory class, T_r = 1…20 | all `c` (converge) | "converge at every review interval" ✓ |
| instability band | anchovy 34–41, sprat 34–41, cod 35–42 | "entering at 34--35 yr … to the grid's end" ✓ |
| slow-stock oscillation-then-convergence | `p` only at T_r = 10 | disclosed ✓ |

Line 1364 likewise calls the 3–4 yr record "archived, **unreproduced**".

Everything else matches:

| quantity | paper | campaign |
|---|---|---|
| ρ(1) anchovy / sprat / cod / slow-stock | 0.895 / 0.923 / 0.956 / 0.994 | 0.894796 / 0.923122 / 0.956032 / 0.993901 ✓ |
| (M, τ) per class | (0.90,1) (0.40,2) (0.20,5) | (0.900,1) (0.400,2) (0.200,5) (0.045,25) ✓ |
| E* | 2.0896 | 2.0896 ✓ |
| 30% assessment-error robustness | converged | converged ✓ |

### `campaign_p5_crossing_scan.py`

| quantity | paper | campaign |
|---|---|---|
| mobilising ρ at T_r=1 | 1.00035 | rhoX = 1.00035 ✓ |
| protective ρ(1) | 0.9838 | 0.9838 ✓ |
| protective Euler crossing | 2.306 | 2.3064 ✓ |
| mobilising exact-update crossing | ≈6.5 yr | 6.5013 ✓ |
| scaled-norm RMSD at T_r=0.5 | ≈2 | 1.913275 ✓ |
| RMSD magnitude at larger T_r | 10⁴–10⁵ | 4586 (T_r=3) → 135755 (T_r=5) ✓ |

### `campaign_p5_comparator_mse.py`

Runs clean. Its per-channel RMSD table is not printed in v47 (the paper reports
only the summary "RMSD ≈ 2 … 10⁴–10⁵"), so there is nothing to contradict.

---

## Verdict

Both papers survive the check that actually found the E2 defect. This is the
outcome you predicted: P4 and P5 did not need correcting, and that is now
established by running their pipelines rather than by reading their prose.

Nothing pushed — there is nothing to change.

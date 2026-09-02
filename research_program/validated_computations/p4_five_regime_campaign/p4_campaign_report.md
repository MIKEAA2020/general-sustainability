# P4 five-regime continuation campaign — EXECUTION REPORT

**Campaign**: the pre-registered plan
(`arena agent 1/other documents/rerun_campaigns/
p4_continuation_campaign_preregistration.md`, document date label
2026-09-03, git-committed 2026-09-02 03:19:28 UTC in commit 9a26c7e —
the label/commit-clock difference is the prior session's date labeling;
the verifiable ordering is the git history), executed 2026-09-02
04:37–04:57 UTC, ~78 minutes after the pre-registration commit, by
`p4_campaign.py` + `p4_kernels.py` (this directory). All parameters,
grids, histories, acceptance criteria and comparison criteria were frozen
before the run; the executed values are recorded in
`p4_environment.json` (PAR verified identical to the pre-registration's
declared numbers; the numba RHS re-implementation verified equivalent to
the committed `a025_model.rhs` to 5.7e-14 over 20,000 random states).

## Provenance statement (pre-registration §7, printed with the results)

The original five-regime records are not in the repository (registry
verified negative, 2026-09). The records below are the output of the
pre-registered campaign of 2026-09-03: the committed gated three-state
model continued, tracked, and basin-tested by the committed pipeline
machinery, with all parameters, grids, criteria, and comparison rules
fixed before the run. The inherited A018 §6 numbers keep their
exploratory status; a match is a consistency statement for the inherited
record, and a mismatch adjudicates nothing about numbers whose
generating objects remain unavailable. The small-branch fold and the
Hopf pair are interval-certified inputs; all other records are nominal
with the declared acceptance criteria.

## The records (the publication-artifact archives)

| Archive | File | Content |
|---|---|---|
| Branch (per family) | `p4_branch_{small_lower,large_lower,small_upper,large_upper}.csv` | 148 records (47/55/46/0 converged + 2 recorded failures); per point: tau, T, N ptp, Z/E extrema, residual, Nyquist content, continuation step, mu1 (mod/re/im), mu2/mu3 mod, trivial eigenvalue, alignment |
| Floquet | columns of the branch CSVs | variational segment-map multipliers at every converged continuation point (real at every record; imaginary part reported per point) |
| History/basin | `p4_basin_archive.csv` | 87 runs (27 taus × 3 histories at dt=0.02 + 6 dt-halving runs at dt=0.01): classification, tail N-extremes, tail RSD, max E, gate-floor flag, clip counts |
| Solver | `p4_solver_archive.log` | the full console trail: residual floors, stall acceptances, failed seeds, step sequences, ladder scans, per-run timings |
| Environment | `p4_environment.json` | versions, machine, date, committed-code hashes, seeds (none; deterministic — fixed LCG seed 1 for the Arnoldi start vectors only), inherited certificates |
| Fold solves | `p4_fold_ms_large_lower.npz`, `p4_branch_orbits.npz` | the Moore–Spence fold solutions at m=64/96/128 and the cached branch orbits |

### Acceptance criteria (pre-registration §4, all met or honestly failed)

- Collocation residuals: 121/148 records at ≤1e-11 inf-norm; 27
  stall-accepted points at ≤3.61e-10, all within the declared
  stall-acceptance level 3e-9 (the committed pipeline's own near-fold
  residual floor, as documented in `a025_fold_pipeline.py`).
- Fold events: the lower fold is interval-certified (the inherited
  Krawczyk certificate; re-verified by this campaign's independent m=64
  Moore–Spence solve to 2.5e-12 and by the m=96/128 seeded solves);
  the three-order agreement is **2.69e-11** (m=64: 5.587236198690,
  m=96: 5.587236198664, m=128: 5.587236198663) — far inside the 1e-6
  requirement. No other fold was locatable (see deviations).
- Multiplier crossings: the +1 crossing of the dominant real multiplier
  bracketed to **5.98e-08** (small arm) and **1.07e-07** (large arm),
  both far inside the ≤1e-3 requirement; both brackets contain the
  Moore–Spence fold 5.5872362. No complex-pair crossing was found at
  any record (imaginary part identically zero to 1e-6 at every point of
  every family).
- Basin dt-halving: classifications UNCHANGED at both pre-registered
  points (5.575 and 148.3) and all three histories.
- Classification thresholds: applied as frozen (captured = tail RSD ≥
  2%; settles = < 0.1%; intermediate reported as its own class).

## The five-regime boundary table (brackets only)

| Boundary | Campaign bracket | Source |
|---|---|---|
| τ− (eq gains stability; regime i→ii) | [3.6661490142739, 3.6661490142743] | inherited interval certificate |
| lower fold (regime ii→iii) | [5.587236198663, 5.587236198690] | three-order MS + Krawczyk certificate + both +1-crossing brackets; basin-grid corroboration: H2 capture persists to 5.6 as a ghost transient (settles at 4× horizon — diagnostic note below) |
| small-branch fold (same object: the S-branch's single fold) | [5.587236198689, 5.587236198691] | inherited Krawczyk certificate; stage-2 independent m=64 MS re-verification (2.5e-12) |
| upper capture onset (regime iii→iv) | [148.6, 149.5] | basin-grid H1 capture onset (no collocation fold locatable — see deviations) |
| τ+ (eq loses stability; regime iv→v) | [150.3584773101408, 150.3584773101421] | inherited interval certificate |
| interior monostability | finite-search statement: all 6 interior grid taus (6.0–130.0) settle for all three histories; no periodic-orbit family in the branch records on 5.6 < τ < 147.5 | a finite search, not a proof |

The five-regime topology: (i) 0<τ<3.666: eq unstable, the large cycle the
attractor (basin: captured ×3 at 1.0–3.65); (ii) 3.666<τ<5.5872:
bistable (eq + the large arm of the S-branch; basin: H2 captured,
H1/H3 settle at 5.0–5.6 — the REVERSED asymmetry, see comparison);
(iii) 5.5872<τ<148.6: monostable settling (finite-search); (iv) the
upper window: the captured E~Emax face cycle from ~148.6–149.5 beside
the still-stable eq; (v) τ>150.358: eq unstable, the face cycle the
attractor (H1/H2 captured by 155; H3 escapes slowly — finite-horizon
intermediate).

## Comparison verdicts (pre-registration §5, reported ONCE, no re-runs)

MATCH (5): large-branch multiplier at 5.5815 (0.9692 vs 0.964); small-arm
multiplier at 5.587 (0.9942 vs 0.99898); family separation at 5.575
(amp gap 4.98 ≥ 2, period gap 14.4 ≥ 5; amps 24.91/19.94 vs ~25/~21.7,
periods 322.60/308.16 vs ~322.9/~314.3); the small-branch fold
(5.5872362 ≈ legacy 5.587 within its 3-decimal rounding); the upper
small-branch amplitude window (0.100 at 150.31 vs 0.11; 1.874 at 130
vs 1.87 — both ends within 15%).

MISMATCH (6): large-branch multiplier at 4.0 (0.2040 vs 0.240, diff
0.036 > 0.02); small-arm multiplier at 5.584 (1.0192 vs 1.0514, diff
0.032); the lower-boundary bracket (campaign 5.5872362 vs legacy
[5.574, 5.576] — the campaign locates the fold 0.011 above the legacy's
basin-bisection estimate; the legacy's own collocation evidence — a
residual-1e-12 orbit with μ=0.964 at 5.5815, past its own claimed fold
— already pointed here); the upper-boundary bracket (campaign
[148.6, 149.5] vs legacy [148.125, 148.438]); the H1/H2 basin asymmetry
(REVERSED at 5.575: H1 settles / H2 captured; at 148.3 both
intermediate); the basin-grid agreement (53/81 agree; the disagreements
concentrate exactly where the legacy claim was qualitative: the
asymmetry inside the windows and the near-Hopf critical-slowing points).

NOT-TESTED (1): the interior large family's amplitude window (the
campaign's basin runs never find a 15.9–19.5-amplitude cycle at
147.5–160 — they find the E~Emax face cycle (amp ~44) instead, which is
not Fourier-collocatable; the legacy's interior family, if it exists in
this system, was not searched for by continuation seeding from legacy
numbers — the independence discipline forbids it).

The structural finding behind the two bracket mismatches: **the lower
"two families" are two arms of ONE S-shaped branch.** The subcritical
Hopf small arm (amplitude 1.10 at 3.716, unstable, μ>1) and the large
amplitude arm (63.6 at 1.703 down to 21.8 at the fold, stable, μ<1)
meet at a single fold — 5.587236198690 at all three collocation orders,
inside the Krawczyk-certified box, with both arms' +1-crossing brackets
at the same τ (width ~1e-7). The two coexisting cycles at 5.575 are
genuinely distinct (amp 24.91 vs 19.94, period 322.60 vs 308.16 — the
separation criterion MATCHES), but the legacy's picture of two separate
folds (its [5.574, 5.576] "large-cycle fold" plus its 5.587
"small-branch fold") is replaced by one fold at 5.5872362.

## Deviations and honest failures (recorded, no criterion changed)

1. **The upper captured family is not Fourier-collocatable.** The basin
   runs at 149.5–155 capture an E~Emax face cycle (N ptp ~44, E ∈
   [0.35, 29.91]); its basin-seed orbit has m=64 Fourier residual 4.5e2
   (Newton diverged; m=128 seed residual 9.0e2, Newton stalled at 30.1).
   The family's existence and location are recorded by the basin archive
   only; no collocation branch record, no Moore–Spence fold location,
   no Floquet record. Consequently the upper-boundary comparison uses
   the basin-grid bracket. (The legacy's separately-described "interior
   large family" (amp 15.9–19.5, E ≤ 26, residual 1e-13 on
   [147.5, 160]) is a different object from anything the campaign's
   histories find; per the independence discipline it was not hunted
   for.)
2. **m=128 attempt for that family** (recorded as the resolution
   cross-check `basin-seed-m128`): a deviation from "m=64 primary" —
   recorded here and in the solver log; it also failed.
3. **The large arm's lower end**: the natural continuation stalls at
   τ=1.703322 with clean residuals (4–6e-12; amplitude 63.6, μ=0.044);
   the arclength pass could not traverse further (the tangent from the
   micro-step secant is degenerate). The record window [1, 6] is covered
   down to 1.7033 only; the basin archive shows the captured cycle
   continuing to τ=1 (E approaching the Emax face — the same
   sharpness that defeats the collocation).
4. **Ghost-transient diagnostic (not a criterion)**: H2 is classified
   captured at τ=5.6 (tail RSD 6.8%) although the collocation fold is at
   5.5872362; at a 4× horizon (1.6e5 yr) the same run settles. The
   frozen 4e4-horizon classification stands in the CSV; this note
   records that the 5.6 capture is a saddle-node ghost transient, not a
   persistent cycle — i.e. the collocation fold and the basin archive
   are consistent.
5. **Methods note (implementation choices, documented per the plan's
   freedom)**: the Floquet multipliers are those of the discrete
   period map (method-of-steps RK4, dt adjusted to divide the period
   exactly, ~0.02; linear interpolation of the delayed δZ read at the
   exact τ), evaluated along the collocation orbits — the committed
   machinery's own shooting/period-map Floquet method, with the
   reference coefficients following the collocation system's own
   delayed-Z definition (the circular shift matrix). The machinery is
   validated by: the phase-tangent Rayleigh quotient = 1 + 8.7e-08; the
   trivial Ritz eigenvalue 0.9999989–0.9999997 at mid-branch; the exact
   reproduction of the nonlinear fixed-point map (errors 4e-6, the
   interpolation level); the fold straddle (trivial 0.99965 /
   nontrivial 1.00035 at the MS fold). The Arnoldi dimension is 128
   (deterministic LCG start, seed 1); the identification of the trivial
   multiplier uses the orbit-tangent alignment (1.000 at every record).

## The figure

`p4_topology_figure.png` (built by `p4_topology_figure.py`): the
four-panel topology — (a) the lower S-branch (both arms, stability
colored, the certified Hopf and the fold marked); (b) the upper region
(the small branch + the basin capture strip + the capture-onset
bracket); (c) the multiplier tracks with the +1 line; (d) the full
basin grid. Per the pre-registration's §6 rule, the figure is drawn
ONLY from this campaign's committed records (the branch/basin CSVs and
the results JSON); no legacy number is drawn. The figure un-gates the
P4 topology figure assessment (the visual-aids item) — whether to
insert it into the paper's manuscript is a venue-pass/owner decision,
not taken here.

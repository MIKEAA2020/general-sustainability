# Post-v1.0 computation reruns (2026-08-26): dt=0.1 monodromy and the A025 fold pipeline m=64

**Scope.** The two post-v1.0 computations rebuilt in the Task-31 session were first-run with no rerun:

1. **C4 monodromy at dt=0.1** — `research_program/validated_computations/a021_c4/c4_monodromy_dt0p1.py` → `c4_monodromy_dt0p1_phase1.npz`, `c4_monodromy_dt0p1_contour.npz`, `c4_monodromy_dt0p1.npz`, `c4_monodromy_dt0p1_enclosure.json`.
2. **A025 fold pipeline at m=64 (nominal)** — `research_program/validated_computations/a025_fold/a025_fold_pipeline.py` → `a025_moore_spence_fold.npz`, `a025_branch_continuation.json`.

This record documents their rerun by a second agent session.

**Environment.** Python 3.12.13 (`/home/z/.venv/bin/python3`) / numpy 2.1.3, x86_64 Linux — the SAME machine, interpreter, and library versions as the original Task-31 runs. **Honest scope note (as in `../intervention_rerun/`):** this is a same-environment second-session rerun, not a cross-toolchain rerun. It verifies committed-code reproducibility, determinism (both pipelines are deterministic), and freedom from uncommitted state. It does not verify numerical stability across library versions.

**Procedure.** Committed artifacts snapshotted and hashed (`dt0p1/committed/`, `fold_m64/committed/`); the working checkpoints and finals deleted; the pipelines executed fresh from the committed code; the regenerated artifacts compared byte-for-byte against the snapshots.

**Results.**

| Computation | Artifacts | Result |
|---|---|---|
| C4 monodromy dt=0.1 (all three phases: simulate+partials+ball; 60 000-SVD contour scan in five chunked `--resume` invocations; enclosure write) | 4/4 (phase1 npz, contour npz, final npz, enclosure json) | **HASH-IDENTICAL** — `9dce7344…` / `51824e18…` / `6ebe7358…` / `22cefc8f…` |
| A025 fold pipeline m=64 (Hopf start → 48-point tau continuation to 5.587236 → Moore–Spence solve, 17 iterations) | 2/2 (MS npz, continuation json) | **HASH-IDENTICAL** — `353f5559…` / `9d882b04…` |

**Verdicts re-observed identically.** dt=0.1 monodromy: period 371.10 yr; rigorous ball 1.286e-04; phase multiplier 0.996387 certified simple/neutral; dominant nontrivial 0.686932 + disc 0.066052 < 1 certified below one; all nontrivial multipliers strictly inside the unit disc = True; contour exceeds_ball = False (informational, as at dt=0.25 and as recorded in the committed enclosure). Fold m=64: tau_f = 5.587236198690, T_f = 315.322196, Npk = 22.3300, |M| = 2.260e-12 — INSIDE the lost certificate interval [5.587236197890, 5.587236199490] at distance 1.15e-13; the continuation's last residual 2.3e-12 over 48 points.

**What this does and does not close.**

- CLOSED: the "first run / not yet independently rerun" limitation on these two computations, at the reproducibility level (same-env second-session byte-identical rerun; the cross-toolchain standard of the Task-29 Part II reruns remains available to a future rerun).
- NOT CLOSED: the fold's interval Krawczyk stage (the nominal Moore–Spence point is not an interval certificate); the m=96/128 resolution cross-checks remain first-run (not rerun here — they are resolution cross-checks of the m=64 point, which is the rerun-verified object); Wave E Part III paper-support rows; no theorem status changes.

Files: `dt0p1/committed/` + `dt0p1/committed_hashes.txt` + `dt0p1/rerun_console_excerpt.log`; `fold_m64/committed/` + `fold_m64/committed_hashes.txt` + `fold_m64/rerun_console.log`.

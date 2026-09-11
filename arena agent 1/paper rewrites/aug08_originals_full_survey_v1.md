# August-8 originals: full release survey (scaffold / stage / RAM / verification)

Scope: every re-runnable scaffold, stage, RAM, and verification script in the
release asset `workspace-*.zip` (release `compendium-v1.0`, "2nd workspace",
2026-09-04), plus directly adjacent closure/support scripts. Continues
`paper5_aug08_deposit_verification.md` (v1: the seven paper-5 files), which
stands unchanged. Verification runs 2026-09-11: numpy 2.3.5, scipy 1.17.1,
numba 0.66.0, jax 0.11.1 (pip-installed for this session), Python 3.13.14,
2 cores. All scripts below were executed from originals; no original was
modified (one diagnostic used a patched /tmp-only copy, stated where used).

## 1. Paper-5 completion (extends the v1 deposit)

Sampled-governance full grid, previously spot-checked (2 cells), now re-ran
complete: output IDENTICAL to committed `sampled_governance_v2.log` (all rows,
both eta values). The superseded v1 record (`sampled_governance.log`, different
format, wrong v1 controller) is deposited alongside for provenance.

Stage chain (all four scripts + four logs recovered; scripts byte-identical to
the tracked September recovery, which is thereby validated):

| Script | Re-run vs committed log |
|---|---|
| `stage_r_window.py` | IDENTICAL to `stage_run.log` (437 s: g=0 validation + stage-scanned r-windows) |
| `stage_decomp2.py` | IDENTICAL to `stage_decomp2.log` (modulo warning-header paths) |
| `stage_robust_check.py` | IDENTICAL to `stage_robust.log` |
| `stage_tau0_decomposition.py` | IDENTICAL to `stage_tau0.log` |

Paper-5 computation state is now: screen, BH zero count, power method + table
(driver gap remains, v1 section 3), discriminator, sampled windows, noise
experiments, Droop negative, and the full stage chain all re-executed from
originals. Deposited under `paper5_aug08_originals/` (new: 4 stage scripts
minus the 2 already there, `stage_decomp_results.md`, 6 logs).

## 2. Scaffold: 8/8 run (general-theory manuscript, not paper 5)

Scripts serve `manuscript_v11_scaffold_appendix.tex`
("Scarcity-Driven Capital Liquidation and Delay-Amplified Instability", Ricker
+ maturation-cascade + abiotic + product/waste + gated-effort 9-state
scaffold). All numpy/scipy-only, all exit 0. No committed run logs exist; the
two results notes corroborate:

| Script | Outcome |
|---|---|
| `scaffold_hopf_search.py` | best gap 3.079 EXACT vs note ("max gap up to +3.08", 54/3000 pass) |
| `scaffold_hopf_definitive.py` | 8 genuine Hopfs, first 5 EXACT vs note (e.g. w*=0.00665, tau=222.69, period=945.08, \|char\|~1e-17) |
| `scaffold_items_1_2.py` | stabilizing crossing EXACT (tau*=7769.54, dRe/dtau=-1.159e-08); fragmented windows, no clean two-crossing structure, as noted |
| `scaffold_item_3_anchor.py` | "NO anchored parameter set satisfies the modulus condition" EXACT |
| `scaffold_item3_refine.py` | cod Hopf EXACT (+0.163 at (5.0,0.8,0.03,0.01), tau*=43.29, period=263.4) |
| `scaffold_hopf_verify.py`, `scaffold_root_track.py`, `scaffold_summary.py` | run clean (seeded RNG); outputs consistent with the notes' caveats |

This survey's rerun logs (8) are deposited as the only execution records.

## 3. verification_scripts: 11/11 executed

Serve `corrected_manuscript.tex` (general vector-accounting + 3/4-state cores;
see `verification_scripts/README.md`). Needed inputs recovered: dependency
closure (17 support modules, all in-zip) and `unstable_clean_ckpt.npz` (793 KB,
in-zip; scripts hardcode `/home/user/` or cwd paths).

| Script | Outcome |
|---|---|
| `verify_kappaA_sweep.py` | exit 0, VERDICT: GAP CLOSED |
| `verify_fourstate_pipeline.py` | exit 0 (Candidate B tau_-=6.25115, tau_+=99.79060) |
| `verify_fourstate_sensitivity.py` | exit 0, complete 3-sweep tables (tau=0 stable everywhere; tau_- 6.9-7.4, tau_+ 131.8-132.4) |
| `verify_fourstate_fold_tracking.py` | exit 0, self-verdict PARTIAL (some folds not located; a result, not a failure) |
| `verify_hybrid_folds.py` | exit 0 |
| `verify_ungated_floquet.py` | exit 0 (198 s; stable limit cycle, modulation = integrator artifact) |
| `verify_branch_structure.py` | exit 0, ALL CHECKS PASSED (1996 s) |
| `verify_corrected_core_folds.py` | exit 0 (Candidate B folds corrected: upper ~76.075) |
| `verify_hopf_nature.py` | exit 0 |
| `verify_unified_eta_sweep.py` | exit 0 (eta=10 tau_-=17.568 EXACT) |
| `verify_branch_folds.py` | checks 1-2 PASS; check_3 crashes on a committed float-key dict bug (`moduli[t+0.01]` asks for keys never stored; fails on any machine). Patched-copy diagnostic (/tmp only): math PASSES (0.9470/0.9568/0.9666 monotone, matching the expected values exactly) |

## 4. Root verify_*: 8/8 green

| Script | Outcome |
|---|---|
| `verify_ai_reports.py` | exit 0 (hardcoded arithmetic checks; companion note + the two `ai report*.txt` subjects deposited) |
| `verify_candB_sanity.py`, `verify_candB_stability.py`, `verify_candB_variants.py` | exit 0 |
| `verify_fourstate_candidateB.py` | exit 0 |
| `verify_floquet_points.py` | exit 0 after creating `/home/user/dde_floquet/` (hardcoded output path) |
| `verify_tethered_unified_hopf.py` | exit 0 (tethered core: Hopf NONE) |
| `verify_snpo_fold_correction.py` | exit 0, ALL CHECKS PASSED (genuine fold at tau=5.46833; jax required) |

## 5. Adjacent closure/support scripts (bonus)

Ran: `close_item11_candidateB.py` / `close_item11_sweep.py` /
`close_d12_fourstate_gated.py` exit 0. `multishoot.py`, `pseudo_arclength.py`,
`dde_core.py`, `solver2.py` are library-only (no `__main__`), import clean.
`item2_retry.py`: all 4 seeds completed, then crashes on a stray `PYEOF` token
at line 77 (heredoc residue; the file's only defect).
`close_item3_high_delay.py`: broken as committed (imports `physical_branch`
from `fourstate_pipeline`, where it does not exist; the name lives in
`verify_kappaA_sweep`). `close_A4_amplitude.py`: fails under current scipy
(CubicSpline "x must be strictly increasing" on checkpoint-derived grid).
`snpo_piecewise_collocation.py` (numpy/scipy-only) imports clean but was
time-boxed out before running (17-tau two-branch job); its input CSVs
(`snpo_lower_fold_*.csv`) are deposited.
Runnable but not run (deps satisfiable, time-boxed out): `collocation_orbit.py`,
`continuation.py`, `palc_through_folds.py` (jax), `feasibility_fourstate_gated_folds.py`,
`fourstate_gated_fold_hunt.py` (numba).
Not runnable here: `jitc_core.py` (missing `jitcdde`), 7 MATLAB `.m` files
(no MATLAB; deposited as reference), `track_fold_branches.m` likewise.
Out of scope, intentionally not deposited: `apply_*` (5 manuscript-edit
scripts), `content_loss_scan.py`, `p2/p3.log` (pdflatex-missing trivia),
`session_summaries_decoded.txt`, `uploads/*.txt` byte-duplicates of deposited
`.py` files. Referenced-but-absent: `verify_gated_fourstate.py`,
`verify_folds*.py`, `verify_basins.py` (cited by `VERIFICATION_REPORT.md` as
workspace-only; not in the release).

## 6. Deposits (this commit)

- `analysis/paper5_aug08_originals/`: + stage_robust_check.py,
  stage_tau0_decomposition.py, stage_decomp_results.md, stage_run.log,
  stage_tau0.log, stage_robust.log, stage_decomp2.log, sampled_governance.log,
  sampled_governance_v2.log.
- `analysis/aug08_theory_originals/` (new): 8 scaffold scripts + 2 results
  notes + 8 rerun logs; `verification_scripts/` (11 scripts + README);
  8 root verify scripts + 2 review notes; 17 support modules; 5 close_*
  scripts; item2_retry + unified_v2_intermittency + snpo_piecewise_collocation
  + 3 fold CSVs; feasibility + fold_hunt + jitc_core; 7 MATLAB files;
  scaffold appendix tex; VERIFICATION_REPORT + 2 ai-report subjects;
  `unstable_clean_ckpt.npz`; this note as README.
- Workspace + `paper rewrites/`: this note.

## 7. Reproduction

PYTHONPATH must include the deposit root and `verification_scripts/`
(sibling imports). Place `unstable_clean_ckpt.npz` at `/home/user/` (absolute)
or cwd per script; create `/home/user/dde_floquet/` for the Floquet table.
Runtimes (2 cores, contested): stage_r_window 437 s, droop_test ~206 s,
branch_structure 1996 s, snpo ~20 min, sensitivity ~40 min, fold_tracking
~20 min, sampled_governance full ~25 min. Full re-execution needs
numpy+scipy+numba+jax; the paper-5 chain needs only numpy+scipy.

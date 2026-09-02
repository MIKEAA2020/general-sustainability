#!/usr/bin/env python3
"""C-g: build the computational-artifact manifests.

Walks the committed computational artifacts (validated_computations/ and the
two Wave E scored trees' results), hashes every file, attaches the documented
reproduction command and status per artifact, and writes
research_program/validated_computations/ARTIFACT_MANIFESTS.json.

Consistency: the pinned SHA-256 prefixes in reaudit/verify_validated_computations.py
must match the manifest hashes (checked here; a mismatch is a hard failure).
"""
from __future__ import annotations

import hashlib
import json
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
VC = REPO / 'research_program' / 'validated_computations'

# artifact -> (reproduction command, working dir, status note)
COMMANDS = {
    'a025_fold/a025_interval_hopf.json': (
        'python3 research_program/validated_computations/a025_fold/'
        'a025_interval_hopf.py', 'repository root',
        'Part II certificate; INDEPENDENT_RERUN 2026-08-26 (hash-identical)'),
    'a025_fold/a025_moore_spence_fold.npz': (
        'python3 research_program/validated_computations/a025_fold/'
        'a025_fold_pipeline.py 64', 'repository root',
        'NOMINAL Moore-Spence fold solve (rebuilt pipeline); no interval '
        'certification; RERUN 2026-08-26 hash-identical, same-env second '
        'session (reaudit/postv10_rerun/POSTV10_RERUN.md)'),
    'a025_fold/a025_branch_continuation.json': (
        'python3 research_program/validated_computations/a025_fold/'
        'a025_fold_pipeline.py 64', 'repository root',
        'NOMINAL fold record (rebuilt pipeline); tau_f inside the lost '
        'certificate interval; RERUN 2026-08-26 hash-identical, same-env '
        'second session (reaudit/postv10_rerun/POSTV10_RERUN.md)'),
    'a021_c4/c4_orbit_krawczyk_certificate.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_orbit_krawczyk.py', 'repository root',
        'Part II certificate; INDEPENDENT_RERUN 2026-08-26 (re-certified at '
        'a nearby Newton centre)'),
    'a021_c4/c4_orbit_krawczyk_box.npz': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_orbit_krawczyk.py', 'repository root',
        'Part II certificate companion; re-certified (max delta-u 4.3e-11)'),
    'a021_c4/c4_offgrid_residual_interval.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_offgrid_interval_v2.py', 'repository root',
        'Part II certificate; INDEPENDENT_RERUN 2026-08-26 (re-certified; '
        'A 6% higher)'),
    'a021_c4/c4_monodromy_enclosure.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_monodromy.py', 'repository root',
        'Part II certificate; INDEPENDENT_RERUN 2026-08-26 (hash-identical)'),
    'a021_c4/c4_monodromy_dt0p25.npz': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_monodromy.py', 'repository root',
        'Part II certificate companion; hash-identical rerun'),
    'E5_NUMBERS.json': (
        'python3 research_program/validated_computations/e5_admission.py',
        'repository root',
        'Part II certificate; INDEPENDENT_RERUN 2026-08-26 (hash-identical); '
        'toy scope, R04 transfer prohibition applies'),
    'a025_fold/a025_moore_spence_fold_m96.npz': (
        'python3 research_program/validated_computations/a025_fold/'
        'a025_fold_pipeline.py 96 --dtau-min 5e-6 --tau-end 5.62',
        'repository root',
        'NOMINAL m=96 Moore-Spence fold (resolution cross-check); INSIDE '
        'the lost interval'),
    'a025_fold/a025_branch_continuation_m96.json': (
        'python3 research_program/validated_computations/a025_fold/'
        'a025_fold_pipeline.py 96 --dtau-min 5e-6 --tau-end 5.62',
        'repository root',
        'NOMINAL m=96 fold record; INSIDE the lost interval'),
    'a025_fold/a025_moore_spence_fold_m128.npz': (
        'python3 research_program/validated_computations/a025_fold/'
        'a025_fold_pipeline.py 128 --dtau-min 5e-6 --tau-end 5.62 --resume-ms',
        'repository root',
        'NOMINAL m=128 Moore-Spence fold (resolution cross-check); INSIDE '
        'the lost interval'),
    'a025_fold/a025_branch_continuation_m128.json': (
        'python3 research_program/validated_computations/a025_fold/'
        'a025_fold_pipeline.py 128 --dtau-min 5e-6 --tau-end 5.62 --resume-ms',
        'repository root',
        'NOMINAL m=128 fold record; INSIDE the lost interval'),
    'a025_fold/a025_fold_krawczyk.json': (
        'python3 research_program/validated_computations/a025_fold/'
        'a025_fold_krawczyk.py', 'repository root',
        'INTERVAL KRAWCZYK CERTIFICATE (2026-09-03, re-attempt of the lost '
        'stage): unique Moore-Spence zero in the box tau_f in '
        '[5.587236197890, 5.587236199490] (the lost interval, 1 ulp '
        'widened), final enclosure [5.587236198689, 5.587236198691]; G\' '
        'nonsingular throughout (simple nondegenerate fold of the m=64 '
        'collocation system); psi^T F_tau in [0.313266, 0.314822] and '
        'psi^T D2F[v,v] in [5.6923e-5, 5.8943e-5] both exclude 0; '
        'first-run status (no independent rerun yet)'),
    'p4_five_regime_campaign/p4_campaign.py': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py all',
        'repository root',
        'P4 five-regime campaign orchestrator (the pre-registered plan of '
        '2026-09-03, EXECUTED 2026-09-02/03): stages 0-4; FIRST-RUN status '
        '(no independent rerun); deterministic (fixed LCG seed 1 for the '
        'Arnoldi starts)'),
    'p4_five_regime_campaign/p4_kernels.py': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py all',
        'repository root',
        'P4 campaign numba kernels (method-of-steps RK4 basin + variational '
        'segment map); RHS equivalence vs a025_model.rhs verified to '
        '5.7e-14 (stage 0)'),
    'p4_five_regime_campaign/p4_branch_small_lower.csv': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 2',
        'repository root',
        'P4 campaign branch record, small arm of the lower S-branch '
        '(subcritical Hopf small branch): 47 converged collocation points '
        '+ variational Floquet at every point; the +1 crossing bracket '
        '[5.587236127, 5.587236187]; FIRST-RUN'),
    'p4_five_regime_campaign/p4_branch_large_lower.csv': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 2',
        'repository root',
        'P4 campaign branch record, large arm of the lower S-branch '
        '(seeded from the basin archive at tau=4.0): 55 converged points, '
        'tau in [1.703322, 5.587236], Floquet at every point; the +1 '
        'crossing bracket [5.587236089, 5.587236197]; lower-end stall '
        'recorded honestly; FIRST-RUN'),
    'p4_five_regime_campaign/p4_branch_small_upper.csv': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 2',
        'repository root',
        'P4 campaign branch record, upper Hopf small branch: 46 converged '
        'points on tau in [130.0, 150.3085], amplitude 0.100-1.874, '
        'residual ~1e-12, unstable (mu>1) at every point; FIRST-RUN'),
    'p4_five_regime_campaign/p4_branch_large_upper.csv': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 2',
        'repository root',
        'P4 campaign branch record, upper large family: the HONEST FAILURE '
        'record (the captured E~Emax face cycle is not m=64/128 '
        'Fourier-resolvable; seed residuals 4.5e2 / 9.0e2, Newton '
        'diverged/stalled); the family is recorded by the basin archive; '
        'FIRST-RUN'),
    'p4_five_regime_campaign/p4_branch_archive.csv': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 2',
        'repository root',
        'P4 campaign branch records, the union of the four families (148 '
        'records); FIRST-RUN'),
    'p4_five_regime_campaign/p4_basin_archive.csv': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 1',
        'repository root',
        'P4 campaign history/basin archive: 87 runs (27-tau grid x 3 '
        'history classes at dt=0.02 + 6 dt-halving runs at dt=0.01, all '
        'classifications UNCHANGED under halving); the pre-registered '
        'classifications; FIRST-RUN'),
    'p4_five_regime_campaign/p4_environment.json': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 0',
        'repository root',
        'P4 campaign environment record (versions, machine, committed-code '
        'hashes, no random seeds; the inherited Hopf/fold certificates '
        'recorded as inputs); FIRST-RUN'),
    'p4_five_regime_campaign/p4_campaign_results.json': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 4',
        'repository root',
        'P4 campaign results: the section-5 comparison verdicts reported '
        'ONCE (MATCH 5 / MISMATCH 6 / NOT-TESTED 1) + the five-regime '
        'boundary table (brackets only) + the fold solves; FIRST-RUN'),
    'p4_five_regime_campaign/p4_campaign_report.md': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 4',
        'repository root',
        'P4 campaign execution report: the section-7 provenance statement, '
        'the records table, the acceptance-criteria outcomes, the boundary '
        'table, the verdicts, the deviations/honest failures; FIRST-RUN'),
    'p4_five_regime_campaign/p4_solver_archive.log': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py all',
        'repository root',
        'P4 campaign solver archive (the documentation action the paper '
        'names): residual floors, stall acceptances, failed seeds, '
        'continuation step sequences, ladder scans, per-run timings; '
        'FIRST-RUN'),
    'p4_five_regime_campaign/p4_fold_ms_large_lower.npz': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 3',
        'repository root',
        'P4 campaign Moore-Spence fold solves for the lower S-branch at '
        'm=64/96/128 (three-order agreement 2.69e-11; the same fold as '
        'the Krawczyk-certified small-branch fold); FIRST-RUN'),
    'p4_five_regime_campaign/p4_branch_orbits.npz': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 2',
        'repository root',
        'P4 campaign cached branch/fold orbits (the collocation solve '
        'vectors behind the CSV records); FIRST-RUN'),
    'p4_five_regime_campaign/p4_basin_seeds.npz': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py 1',
        'repository root',
        'P4 campaign basin seed trajectories (the captured-cycle rings at '
        'tau=4.0 and 155.0 used to seed the collocation); FIRST-RUN'),
    'p4_five_regime_campaign/p4_topology_figure.py': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_topology_figure.py',
        'repository root',
        'P4 topology figure builder: reads ONLY the committed campaign '
        'records (the pre-registration section-6 ungating rule); '
        'FIRST-RUN'),
    'p4_five_regime_campaign/p4_topology_figure.png': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_topology_figure.py',
        'repository root',
        'P4 topology figure (the first five-regime figure drawn from '
        'committed records; un-gates the visual-aids item; deliberately '
        'not hash-pinned, per the standing figure policy)'),
    'p4_five_regime_campaign/p4_stage_status.json': (
        'python3 research_program/validated_computations/'
        'p4_five_regime_campaign/p4_campaign.py all',
        'repository root',
        'P4 campaign internal stage checkpoint (resumability state); '
        'FIRST-RUN'),
    'a021_c4/c4_piecewise_chebyshev_stage1.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage1.py',
        'repository root',
        'A1 piecewise-Chebyshev campaign Stage 1 (substrate + local-gain '
        'diagnostic); NOT a certificate; A1 remains COMPUTED_PARTIAL'),
    'a021_c4/c4_piecewise_chebyshev_stage2.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage2.py',
        'repository root',
        'A1 piecewise-Chebyshev campaign Stage 2 (outward-rounded interval '
        'evaluation of the collocation defects and Jacobian blocks + the '
        'tube-inflation ladder); deterministic, byte-identical across '
        'reruns; NOT a certificate; A1 remains COMPUTED_PARTIAL'),
    'a021_c4/c4_piecewise_chebyshev_stage2.npz': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage2.py',
        'repository root',
        'A1 Stage-2 companion arrays (the interval defect enclosures '
        'Y_cheb/Y_four and the gain interval at every node, M=8000 x 9); '
        'deterministic; NOT a certificate'),
    'a021_c4/c4_piecewise_chebyshev_stage3.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage3.py',
        'repository root',
        'A1 piecewise-Chebyshev campaign Stage 3 (the local '
        'Krawczyk/radii-polynomial systems in the marching form with the '
        'finite-band delay coupling enclosed; all M=8000 local systems '
        'close; the assembly constants measured; the dichotomy premise '
        'confirmed at the collocation level); deterministic, byte-identical '
        'across reruns; NOT a certificate; A1 remains COMPUTED_PARTIAL'),
    'a021_c4/c4_piecewise_chebyshev_stage3.npz': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage3.py',
        'repository root',
        'A1 Stage-3 companion arrays (per-patch q_total, the rigorous '
        'inverse-norm and sensitivity bounds, the Lagrange constants, the '
        'Y-inputs and closing radii by combo, M=8000); deterministic; NOT a '
        'certificate'),
    'a021_c4/c4_piecewise_chebyshev_stage4a.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4a.py',
        'repository root',
        'A1 piecewise-Chebyshev campaign Stage 4a (the assembly '
        'measurements: the independent monodromy reconstruction validated '
        'against the Stage-3 preview, the dichotomy constant K_0 = 731.6, '
        'the pinned/bordered inverse conditioning, the ~1.2e-8 float '
        'mismatch march; the interval-march obstruction MEASURED '
        '(width-growth 1.00264/step defeats the direct and windowed '
        'interval marches — the Stage-4b correlation-tracking requirement '
        'grounded in measured constants); and THE RIGOROUS BETWEEN-NODES '
        'CONTINUUM DEFECT BOUND sup_t |p\' - rho f(p, p_delayed)| <= '
        '2.5938e-8 uniform over the rho-family); deterministic, '
        'byte-identical across reruns; NOT the assembly certificate; A1 '
        'remains COMPUTED_PARTIAL'),
    'a021_c4/c4_piecewise_chebyshev_stage4a.npz': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4a.py',
        'repository root',
        'A1 Stage-4a companion arrays (per-patch node-residual sups, the '
        'Chebyshev-coefficient derivative bounds B_{v,j}, the per-sector '
        'Faà di Bruno ninth-derivative bounds, the dichotomy norm profile, '
        'the monodromy spectrum, the tangent); deterministic; NOT a '
        'certificate'),
    'a021_c4/c4_piecewise_chebyshev_stage4b.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4b.py A  then  '
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4b_certify.py eval / checks / '
        'r:<radius> / final',
        'repository root',
        'A1 piecewise-Chebyshev campaign Stage 4b — THE BORDERED ASSEMBLY '
        'CERTIFICATE (CLOSED at r = 3e-7): the correlation-tracking '
        '(block-wrapped affine noise-symbol) march — the operator columns '
        'propagate SIGNED (the dichotomy cancellation preserved) while the '
        'interval evaluation widths and tube Jacobian widths inject as '
        'fresh noise symbols, in-block magnitude-accumulated and '
        'block-wrapped; the rigorous monodromy enclosure; the mpmath '
        'mismatch center (sup 9.65e-9); and the Krawczyk bordered system '
        'in (delta, p) with the marched dPsi/dp column and the tangent '
        'phase pin: Y + Z(r)·r <= r CLOSES at r = 3e-7 (Y = 8.99e-8, '
        'Z = 0.444) — the DISCRETE periodic collocation fixed point of '
        'the one-period local-Newton map is certified to exist within '
        '3e-7 (sup-norm, augmented state) of the substrate at a period '
        'P + p* with |p*| <= 3e-7. Two implementation defects caught and '
        'fixed during development (the p-column landing-PATCH indexing '
        'bug — H_sub indexed by the ring slot instead of the landing '
        'patch, corrupting the phase/A component, caught by the '
        'finite-difference check at exactly one coordinate; the '
        'injection-tube bound using the sum|Lw| proxy where the '
        'landing-H tube requires sum|dLw/dsigma|·|H| — up to 15.6x '
        'underestimate, replaced by the channel-explicit sound bound). '
        'All 10 verification checks pass. The 123 MB Phase-A checkpoint '
        'is regenerable (gitignored; ~83 s). The continuum '
        'orbit-to-solution lift remains Stage 4c; deterministic, '
        'byte-identical across reruns'),
    'a021_c4/c4_piecewise_chebyshev_stage4b_results.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4b.py A  then  '
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4b_certify.py eval / checks / '
        'r:<radius> / final',
        'repository root',
        'A1 Stage-4b Phase-B accumulation record: the eval-only march '
        '(mon_gap 3.0e-16, ap_gap 4.7e-15, T_unc0_sup 4.82e-3 — '
        'phase-direction-dominated exactly as designed), the 10 '
        'verification checks (all pass; the p-column finite-difference '
        'gap 1.14e-5 after the landing-patch fix), and the full r-ladder '
        '(3e-5/1e-5/3e-6/1e-6 fail with the sound tube bound — the '
        'near-miss at 1e-6 recorded honestly — 3e-7 CLOSES); '
        'deterministic'),
    'a021_c4/c4_piecewise_chebyshev_stage4b_phaseA.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4b.py A',
        'repository root',
        'A1 Stage-4b Phase-A summary: the float monodromy (top eigenvalues '
        'matching the committed preview to 1.8e-12), the corrected '
        'p-column (sup 0.665 — the phase direction, matching the '
        'tangent), the bordered inverse (norm 254.2, q0 1.06e-13), the '
        'mpmath mismatch center 9.65e-9, and the mismatch width '
        'enclosure sup 1.93e-7; deterministic'),
    'a021_c4/c4_stage4b_Tunc_eval.npy': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4b_certify.py eval',
        'repository root',
        'A1 Stage-4b eval-only operator extent vector (the additive '
        'monodromy-enclosure widths at r = 0; sup 4.82e-3 dominated by '
        'the undamped phase coordinate, the certificate Z-term handles '
        'it through the bordered inverse); deterministic'),
    'a021_c4/c4_piecewise_chebyshev_stage4d.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4d.py A / gap / jac / final '
        '(resumable; consumes the committed 4b/4c checkpoints)',
        'repository root',
        'A1 piecewise-Chebyshev campaign Stage 4d — THE LOCALISED KINK '
        'LADDER (the read-channel enclosure sharpening; THE CONTINUUM '
        'LIFT CLOSED): the kink sources localised to the ~98 '
        'ring-window boundaries; the per-patch lattice-image chains '
        'with the local tube gains (eps_read 4.16e-9 uniform -> 2.07e-12 '
        'worst); the ladder extended to m=40 with rigorous '
        'Hermite-Genocchi/Lebesgue tail bounds; the per-radius '
        'consistency-Jacobian (base + r*adv exactly); T_gap 6.42e-4 -> '
        '3.29e-8 (12.3x above the measured proxy); Y = 1.492e-7, '
        'Z(3e-7) = 0.469 — the closure Y + Z(r)*r <= r HOLDS at '
        'r = 3e-7 (and 4e-7): a TRUE periodic solution of the C4 DDE '
        'certified within 3e-7 of the substrate at a period within '
        '3e-7 of P; all 13 checks pass; deterministic (the JSON '
        'byte-identical across reruns)'),
    'a021_c4/c4_piecewise_chebyshev_stage4c.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4c.py A  (resumable: rerun across '
        'sessions until "Phase A done")  then  python3 '
        'research_program/validated_computations/a021_c4/'
        'c4_piecewise_chebyshev_stage4c.py final',
        'repository root',
        'A1 piecewise-Chebyshev campaign Stage 4c — THE CONTINUUM '
        'ORBIT-TO-SOLUTION LIFT (EXECUTED; the certificate DOES NOT '
        'CLOSE at the current gap-enclosure sharpness): Psi_true (the '
        'true-DDE one-period march on the augmented state with the '
        'ring-interpolated history reads) with the coupled (u, eta) '
        'system; the consistency-gap machinery (the exact Peano '
        'constants |w\'| and the truncated-power divided-difference '
        'functionals; the read-kink ladder with the OWN-smoothness '
        'bootstrap Y9 = 2.89e6; the Bell-DP derivative bootstrap; the '
        'per-patch truncation forcing marched by the Stage-4b '
        'block-wrapped affine noise-symbol machinery); the eta-lift '
        '(eta_bound 1.18e-16, L_eta 5.65e3, eta_Y 6.7e-13). ALL EIGHT '
        'machinery checks pass (monodromy 1.8e-12, operator-march '
        'consistency, tight-width validity, gap-vs-measured enclosure '
        'validity, forcing sanity, bootstrap sanity, eta-lift, and the '
        'honest closure check). THE CLOSURE FAILS: Y = 3.547e-4 '
        '(T_gap-dominated: the enclosed consistency gap sup 6.42e-4) '
        'against the 1e-7..1e-6 ladder — Z = 0.78..2.10; the '
        'measured-gap proxy is 2.68e-9, so the sound enclosure is '
        '2.4e5 pessimistic, the obstruction diagnosed channel-by-channel '
        '(the read-channel kink ladder: eps_read 4.16e-9 per read is '
        'kink-dominated — the smooth part is ~9e-17 — with the '
        'Dv3_sup^(m-1) compounding reaching 1.1e6, accumulated over the '
        '~8000 per-patch reads under the independent-noise treatment); '
        'the three refinement paths recorded in the artifact. The '
        'Phase-A checkpoint + the six partial checkpoints are '
        'regenerable (gitignored; ~25 min). A1 remains COMPUTED_PARTIAL '
        '— the continuum-lift gate remains open; deterministic'),
    'a021_c4/c4_monodromy_dt0p1.npz': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_monodromy_dt0p1.py (rerun with --resume until phase 3)',
        'repository root',
        'Monodromy matrix + eigenvalues, dt=0.1 (second mesh level); RERUN '
        '2026-08-26 hash-identical, same-env second session '
        '(reaudit/postv10_rerun/POSTV10_RERUN.md)'),
    'a021_c4/c4_monodromy_dt0p1_enclosure.json': (
        'python3 research_program/validated_computations/a021_c4/'
        'c4_monodromy_dt0p1.py (rerun with --resume until phase 3)',
        'repository root',
        'dt=0.1 enclosure (second mesh level; mesh-stable confirmation); '
        'RERUN 2026-08-26 hash-identical, same-env second session '
        '(reaudit/postv10_rerun/POSTV10_RERUN.md)'),
}

ENV_ORIGINAL = ('Python 3.12.13, numpy 2.1.3, scipy 1.14.1, mpmath 1.3.0')
ENV_RERUN = ('Python 3.13.14, numpy 2.3.5, scipy 1.17.1, mpmath 1.3.0 '
             '(second agent, 2026-08-26)')

# per-file status overrides (first-run artifacts at manifest-build time; the
# 2026-08-26 same-env second-session reruns are recorded in
# reaudit/intervention_rerun/ (Edwards), reaudit/intervention_rerun_cod/
# (cod), and reaudit/postv10_rerun/)
STATUS_OVERRIDE = {
    'wave_e_cod/results/intervention_results.json': (
        'cod intervention-leg artifact (protocol_intervention.md); first run '
        '2026-08-26; rerun 2026-08-26 byte-identical on a fresh second-session '
        'execution, same environment as the original run '
        '(reaudit/intervention_rerun_cod/INTERVENTION_RERUN_COD.md) — the G1a '
        'kernel-level Cor2 leg: productivity negative certificate, no '
        'retention, maximal robust flat catch 57.6 kt at UC-q10, expansive-form '
        'erosion certified to T <= 5 yr'),
    'wave_e_cod/results/intervention_boundaries.csv': (
        'cod intervention-leg artifact (protocol_intervention.md); first run '
        '2026-08-26; rerun 2026-08-26 byte-identical on a fresh second-session '
        'execution, same environment as the original run '
        '(reaudit/intervention_rerun_cod/INTERVENTION_RERUN_COD.md)'),
    'wave_e_edwards/results/intervention_results.json': (
        'intervention-leg artifact (protocol_intervention.md); first run '
        '2026-08-26; rerun 2026-08-26 byte-identical on a fresh second-session '
        'execution, same environment as the original run '
        '(reaudit/intervention_rerun/INTERVENTION_RERUN.md)'),
    'wave_e_edwards/results/intervention_boundaries.csv': (
        'intervention-leg artifact (protocol_intervention.md); first run '
        '2026-08-26; rerun 2026-08-26 byte-identical on a fresh second-session '
        'execution, same environment as the original run '
        '(reaudit/intervention_rerun/INTERVENTION_RERUN.md)'),
}

PINNED = {
    'a025_fold/a025_interval_hopf.json': ('eda36cd1', '95b3b2'),
    'E5_NUMBERS.json': ('5670bcc8', '236e72db'),
    'a021_c4/c4_monodromy_enclosure.json': ('01d8c253', 'dbaef76'),
    'a021_c4/c4_monodromy_dt0p25.npz': ('f3dc5445', 'a7ca5f'),
    'a021_c4/c4_orbit_krawczyk_certificate.json': ('5e8df633', '65ab133'),
    'a021_c4/c4_orbit_krawczyk_box.npz': ('85f72c76', '7ba4c69'),
    'a021_c4/c4_offgrid_residual_interval.json': ('2a4a5e82', '1c74a7f4'),
}


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def main():
    entries = []
    problems = []

    # 1. validated_computations artifacts with documented commands
    for rel, (cmd, workdir, note) in COMMANDS.items():
        p = VC / rel
        if not p.exists():
            problems.append(f'missing: {rel}')
            continue
        digest = sha256(p)
        entries.append(dict(
            artifact=f'research_program/validated_computations/{rel}',
            sha256=digest, bytes=p.stat().st_size,
            reproduction_command=cmd, working_directory=workdir,
            status=note))

    # 2. the two Wave E scored trees' result artifacts (regenerable by the
    #    committed scripts; byte-identical independent rerun on record)
    for tree, cmds in (
            ('wave_e_cod', ['python3 src/run_ladder.py; python3 src/make_figures.py']),
            ('wave_e_edwards', ['python3 src/build_panel.py; python3 src/run_ladder.py; '
                                'python3 src/make_figures.py'])):
        base = REPO / tree / 'results'
        for p in sorted(base.iterdir()):
            if p.is_file():
                rel = f'{tree}/results/{p.name}'
                status = STATUS_OVERRIDE.get(rel, None)
                if status is None:
                    status = ('scored-tree result artifact; INDEPENDENT_RERUN '
                              '2026-08-26 (30/30 result files byte-identical); '
                              'spec-matched (batch 4/WAVE_E_SPEC_MATCH.md)')
                entries.append(dict(
                    artifact=rel,
                    sha256=sha256(p), bytes=p.stat().st_size,
                    reproduction_command=f'cd {tree}; ' + (
                        'python3 src/run_intervention.py'
                        if 'intervention' in p.name else cmds[0]),
                    working_directory=f'repository root / {tree}',
                    status=status))

    # 3. pinned-hash consistency (hard failure on mismatch)
    for rel, (pre, post) in PINNED.items():
        p = VC / rel
        if not p.exists():
            problems.append(f'pinned artifact missing: {rel}')
            continue
        digest = sha256(p)
        if not (digest.startswith(pre) and digest.endswith(post)):
            problems.append(f'PIN MISMATCH: {rel} ({digest}) vs pinned '
                            f'{pre}...{post}')
        else:
            e = next(x for x in entries if x['artifact'].endswith(rel))
            e['pinned_hash_verified'] = True

    manifest = dict(
        title='Computational artifact manifests (C-g)',
        built=str(date.today()),
        environment_original=ENV_ORIGINAL,
        environment_independent_rerun=ENV_RERUN,
        verification=(
            'reaudit/verify_validated_computations.py pins the Part II '
            'certificate hashes (pinned_hash_verified flags); the Wave E '
            'trees are verified by reaudit/verify_wave_e.py and the spec '
            'match by reaudit/verify_wave_e_spec_match.py'),
        note=('NOMINAL artifacts (a025_fold pipeline outputs) are hashed for '
              'provenance; they carry no certificate claim. Figure files '
              'are deliberately not pinned (SVG non-determinism; see '
              'PROOF_MANIFEST Part VI).'),
        artifacts=entries,
    )
    out = VC / 'ARTIFACT_MANIFESTS.json'
    out.write_text(json.dumps(manifest, indent=2))
    print(f'wrote {out}: {len(entries)} artifacts hashed')
    if problems:
        print('PROBLEMS:', problems)
        sys.exit(1)
    pinned_ok = sum(1 for e in entries if e.get('pinned_hash_verified'))
    print(f'pinned-hash consistency: {pinned_ok}/{len(PINNED)} verified')


if __name__ == '__main__':
    main()

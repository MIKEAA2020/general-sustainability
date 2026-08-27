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

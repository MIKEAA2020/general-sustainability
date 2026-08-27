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

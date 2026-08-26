#!/usr/bin/env python3
"""C4 monodromy at the second mesh level dt=0.1.

Runs the same run_level() as c4_monodromy.py (imported unchanged) at
dt=0.1 and writes SEPARATE artifacts (c4_monodromy_dt0p1.npz,
c4_monodromy_dt0p1_enclosure.json) so the pinned dt=0.25 artifacts and
their hashes in PROOF_MANIFEST.md Part II remain untouched.

This retires the 'monodromy dt=0.25 only' limitation: the enclosure is
then available at two mesh levels (dt=0.25 and dt=0.1).
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
import c4_monodromy  # noqa: E402


def main():
    t_start = time.time()
    dt = 0.1
    tag = 'dt0p1'
    print(f'=== dt = {dt} ===', flush=True)
    lv, M, lam = c4_monodromy.run_level(dt)
    np.savez(ROOT / f'c4_monodromy_{tag}.npz', M=M, lam=lam)
    print(f'  period: {lv["period_steps"]} steps = {lv["discrete_period_yr"]:.2f} yr', flush=True)
    print(f'  ball: {lv["rigorous_ball_inf"]:.3e}', flush=True)
    print(f'  phase: {lv["phase_multiplier"]}', flush=True)
    print(f'  dominant: {lv["dominant_nontrivial"]}', flush=True)
    print(f'  all inside: {lv["all_nontrivial_strictly_inside_unit_disc"]}', flush=True)

    out = {
        'title': 'Monodromy/Floquet enclosure for the validated C4 cycle '
                 '(second mesh level dt=0.1)',
        'method': 'single-step insertion-identity sensitivity + Bauer-Fike '
                  'eigenvalue discs + sigma_min contour counting '
                  '(identical run_level as the dt=0.25 enclosure)',
        'levels': {tag: lv},
        'note': 'Companion to c4_monodromy_enclosure.json (dt=0.25, pinned). '
                'The dt=0.25 artifacts and hashes are untouched; this file '
                'records the second mesh level only.',
    }
    (ROOT / 'c4_monodromy_dt0p1_enclosure.json').write_text(json.dumps(out, indent=2))
    print(f'written c4_monodromy_dt0p1_enclosure.json ({time.time()-t_start:.0f}s)',
          flush=True)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Phase 1 remaining work, item 1: make the three v3 scripts relocatable.

Each hardcodes  REPO = Path("/home/user/repo")  and then derives
  COD   = REPO / "wave_e_cod" / "src"
  ....  = REPO / "wave_e_cod" / "results" / ...

Scripts live in <repo>/wave_e_cod/src/, so from a script file:
  Path(__file__).resolve().parent       -> <repo>/wave_e_cod/src
  Path(__file__).resolve().parents[2]   -> <repo>

This replaces the constant with that resolution and verifies the derived
paths still point at real directories afterwards. Nothing else is touched.
"""
import io
import os
import sys
from pathlib import Path

OLD = 'REPO = Path("/home/user/repo")'
NEW = ('REPO = Path(__file__).resolve().parents[2]  '
       '# repo root, resolved from this file so the tree is relocatable')

TARGETS = [
    'wave_e_cod/src/campaign_e2_allee_declared_v3.py',
    'wave_e_cod/src/campaign_e2_depensation_v3.py',
    'wave_e_cod/src/campaign_e2_fox_form_v3.py',
]

root = Path(__file__).resolve().parent
ok = True

for rel in TARGETS:
    p = root / rel
    print('=' * 72)
    print(rel)
    if not p.exists():
        print('  MISSING')
        ok = False
        continue
    src = io.open(p, encoding='utf-8', errors='replace').read()
    n = src.count(OLD)
    if n != 1:
        print('  expected 1 occurrence of the hardcoded path, found %d' % n)
        ok = False
        continue
    src = src.replace(OLD, NEW)
    io.open(p, 'w', encoding='utf-8').write(src)
    print('  replaced 1 occurrence')

    # derive what REPO now resolves to, exactly as the script will
    REPO = p.resolve().parents[2]
    COD = REPO / 'wave_e_cod' / 'src'
    RES = REPO / 'wave_e_cod' / 'results'
    for label, path in (('REPO', REPO), ('COD', COD), ('results', RES)):
        good = path.is_dir()
        print('  %-8s %-52s %s' % (label, str(path), 'OK' if good else 'MISSING'))
        ok &= good
    if (RES / 'intervention_results_v3.json').exists():
        print('  results/intervention_results_v3.json  OK')
    else:
        print('  results/intervention_results_v3.json  MISSING')
        ok = False

print('=' * 72)
print('RESULT: %s' % ('PASS' if ok else 'FAIL'))
sys.exit(0 if ok else 1)

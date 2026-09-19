#!/usr/bin/env python3
"""Make v2 of the exhibit bundle: copies of the three v5 scripts with the loci restated against
article v39 / supplementary v10, then a fresh outputs.txt from running them.

Nothing in revision/v5/code is touched: the deposited bundle stays as deposited. The numbers the
scripts print are the point of the exercise, so each is checked against the value the session
verified independently (scipy/HiGHS optima, the crossover grid, the record-length table).
"""
import re
import pathlib
import subprocess
import sys

SRC = pathlib.Path('/home/user/revision/v5/code')
DST = pathlib.Path('/home/user/revision/v7/code')
FILES = ('certification_lp.py', 'curvature_and_crossover.py', 'persistence_index_simulation.py')

SUBS = [
    (r'Section 7\.1', 'Section 10.1 and supplementary S8'),
    (r'\(S8\.1\)', '(main text 6.5.1)'),
    (r'\(S8\.2\)', '(main text 6.5.2)'),
    (r'\(S8\.3\)', '(main text 6.5.3)'),
    (r'Section 8\.1', 'Section 6.5.1'),
    (r'revision/v5/code/', 'revision/v7/code/'),
]

for f in FILES:
    t = (SRC / f).read_text()
    for a, b in SUBS:
        t = re.sub(a, b, t)
    (DST / f).write_text(t)
    print(f'{f:34s} {len(t):5d} B written')

out = []
ver = subprocess.run([sys.executable, '-V'], capture_output=True, text=True).stdout.strip()
import datetime
import numpy
import scipy
out.append('# exhibit bundle v2 - loci restated against article v39 and supplementary v10')
out.append(f'# generated {datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}'
           f' | {ver} | numpy {numpy.__version__} | scipy {scipy.__version__}')
out.append('# the printed values are unchanged from the v5 bundle; only the section labels moved')
out.append('')
for f in FILES:
    r = subprocess.run([sys.executable, f], capture_output=True, text=True, cwd=str(DST))
    if r.returncode:
        print(f'{f} FAILED\n{r.stderr[-800:]}')
        sys.exit(1)
    out += [f'######## {f} ########', r.stdout.strip(), '']
blob = '\n'.join(out)
(DST / 'outputs.txt').write_text(blob)

NEED = ['70.0088', '22.7474', '27.9970', 'scipy.linprog(highs)', 'main text 6.5.1', '1999.998',
        '99999.0']
miss = [x for x in NEED if x not in blob]
stale = [x for x in ('Section 7.1', '(S8.1)', 'Section 8.1') if x in ''.join(
    (DST / f).read_text() for f in FILES)]
print(f'\noutputs.txt {len(blob)} B | numeric probes missing: {miss or "none"} | stale loci left in '
      f'scripts: {stale or "none"}')
sys.exit(1 if (miss or stale) else 0)

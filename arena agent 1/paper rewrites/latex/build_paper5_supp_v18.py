"""Build paper5 supplementary v18 from v17 (one reproducibility fix).

S1 S4 anchoveta entry: owner-supplied working filenames (shortened.txt,
    SAU Taxa 600004 v50-1.csv -- never deposited) -> deposited equivalents
    (peru_anchoveta_catch_sau.csv, sau_taxa600004_reporting.json).
"""
import re

SRC = '/home/user/paper5_v41/paper5_supplementary_v17_NatSustain.md'
DST = '/home/user/paper5_v42/paper5_supplementary_v18_NatSustain.md'

s = open(SRC, encoding='utf-8').read()

EDITS = [
 ('S1-sau-filenames',
  r'`shortened\.txt`, and the global taxon-600004 aggregate, `SAU Taxa 600004 v50-1\.csv`',
  ('`peru_anchoveta_catch_sau.csv` (Peru series, deposited), and the global '
   'taxon-600004 aggregate, `sau_taxa600004_reporting.json` (deposited)'), 1),
]

for name, pat, rep, expect in EDITS:
    s, n = re.subn(pat, rep, s, flags=re.M)
    print(f'{name}: {n} (expect {expect})')
    assert n == expect, name

assert 'shortened.txt' not in s and 'v50-1' not in s
open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST, len(s), 'chars')

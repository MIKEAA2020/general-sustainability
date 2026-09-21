"""Build paper5 supplementary v19 from v18 (one-clause S4 repair).

S1 S4 anchoveta entry: the r=-0.31/p=0.009 parenthetical (false NINO1
    precision -- the committed battery cell for that specification is
    r=-0.08, p=0.53) -> exploratory framing with battery cross-check
    and verification-record pointer.
"""
import re

SRC = '/home/user/paper5_v42/paper5_supplementary_v18_NatSustain.md'
DST = '/home/user/paper5_v44/paper5_supplementary_v19_NatSustain.md'

s = open(SRC, encoding='utf-8').read()

NEW = ("(author calculation from the archived figure, retained as exploratory: "
       "the provenance record does not identify the exact ENSO product release, "
       "and the committed battery's NINO1 one-year-lead cell is null at $r=-0.08$, "
       "$p=0.53$; full battery reconciliation in "
       "`analysis/anchoveta_enso/verify_battery_v1/BATTERY_VERIFICATION_v1.md`)")

EDITS = [
 ('S1-enso-exploratory',
  r'\(detrended log catch against NINO1 at one-year lead, r = -0\.31, p = 0\.009\)',
  NEW, 1),
]

for name, pat, rep, expect in EDITS:
    s, n = re.subn(pat, rep, s, flags=re.M)
    print(f'{name}: {n} (expect {expect})')
    assert n == expect, name

assert 'r = -0.31' not in s
open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST, len(s), 'chars')

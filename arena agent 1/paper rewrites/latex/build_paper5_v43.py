"""Build paper5 v43 main from v42 (A002-hypotheses disposition sentence).

R1 disposition sentence at the end of section 4.5 (adopt-as-motivation +
    explicit deferral of observation aggregation, governance phase ordering,
    substitution certificate)
R2 version comment line v42 -> v43
"""
import re

SRC = '/home/user/paper5_v42/paper5_sampled_governance_v42_NatSustain.tex'
DST = '/home/user/paper5_v43/paper5_sampled_governance_v43_NatSustain.tex'

s = open(SRC, encoding='utf-8').read()

SENT = ("Three wider empirical hypotheses of the programme's general theory "
        "--- observation aggregation, governance phase ordering, and "
        "substitution certificate --- are adopted here only as motivation, "
        "and otherwise explicitly deferred: governance phase ordering "
        "supplies the gain--phase diagnostic target the designs above "
        "inherit, while testing any of the three requires prospective, "
        "adequately powered designs this paper specifies but does not execute.")

EDITS = [
 ('R1-disposition',
  r'(cannot be generalised to governance as a whole\.)(\s+\\subsubsection\{4\.6)',
  r'\1 ' + SENT + r'\2', 1),
 ('R2-version-line',
  r'^% The decision clock \(paper 5, revision v42\):.*$',
  ('% The decision clock (paper 5, revision v43): A002-hypotheses disposition '
   'sentence in section 4.5, with line numbers for review.'), 1),
]

for name, pat, rep, expect in EDITS:
    s, n = re.subn(pat, rep, s, flags=re.M)
    print(f'{name}: {n} (expect {expect})')
    assert n == expect, name

open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST, len(s), 'chars')

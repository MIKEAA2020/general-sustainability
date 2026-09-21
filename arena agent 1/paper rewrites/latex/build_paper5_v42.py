"""Build paper5 v42 main from v41 (audit-sweep corrections, no science changes).

R1 figure paths ../figs_p5/ -> figs_p5/ (house convention: compile from root)
R2 spectral-margins para: theta/lambda "not listed" -> listed in Table 3
R3 undelayed-limit para: lambda "not listed" -> listed in Table 3
R4 section 3.7 heading rename (zero-count -> no qualifying cases)
R5 stale supplementary filename (v12) -> version-free pointer
R6 version comment line v41 -> v42
R7 limitation-(v) name follows the section 3.7 rename
"""
import re

SRC = '/home/user/paper5_v41/paper5_sampled_governance_v41_NatSustain.tex'
DST = '/home/user/paper5_v42/paper5_sampled_governance_v42_NatSustain.tex'

s = open(SRC, encoding='utf-8').read()

EDITS = [
 ('R1-figpaths',
  r'\.\./figs_p5/', r'figs_p5/', 3),
 ('R2-margins-theta-lambda',
  r'are not listed here; they are in the\s+computational record \(Appendix A\)',
  r'are listed in Table 3 (Appendix A)', 1),
 ('R3-undelayed-lambda',
  r'is not listed here\s+\(the spectral-margins record above; Appendix A\); it is a derived eigenvalue',
  r'is listed in Table 3; it is a derived eigenvalue', 1),
 ('R4-heading-37',
  r'subsubsection\{3\.7 The zero-count case\s+search\}',
  r'subsubsection{3.7 Structured case search: no qualifying cases}', 1),
 ('R5-supp-pointer',
  r'\(the\s+accompanying file \\texttt\{paper5\\_supplementary\\_v12\.md\}\)',
  r'(the accompanying Supplementary file)', 1),
 ('R7-limitation-v-name',
  r'\\item The zero-count case search does not independently disconfirm',
  r'\\item The structured case search does not independently disconfirm', 1),
 ('R6-version-line',
  r'^% The decision clock \(paper 5, revision v41\):.*$',
  ('% The decision clock (paper 5, revision v42): audit-sweep corrections '
   '(figure paths, Table-3 theta/lambda pointers, section 3.7 heading, '
   'supplementary-file pointer) with line numbers for review.'), 1),
]

for name, pat, rep, expect in EDITS:
    s, n = re.subn(pat, rep, s, flags=re.M)
    print(f'{name}: {n} (expect {expect})')
    assert n == expect, name

open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST, len(s), 'chars')

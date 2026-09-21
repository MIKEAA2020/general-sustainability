"""Build paper5 supplementary v20 blinded from v19 (double-blind review copy).

C0 prepend invisible HTML comment (blinded pointer to unblinded v19)
C1 (Abaee, 2026, S9.5) -> (citation blinded for review, S9.5)
C2 ; Abaee, 2026) -> ; citation blinded for review)
C3 published as Abaee, 2026; -> published (citation blinded for review);
C4 arena agent 1/ workspace paths -> [repository]/ (filenames kept)
C5 @ 24c980cd -> @ [blinded]
"""
import re

SRC = '/home/user/paper5_v44/paper5_supplementary_v19_NatSustain.md'
DST = '/home/user/paper5_supp_v20/paper5_supplementary_v20_blinded_NatSustain.md'

s = open(SRC, encoding='utf-8').read()

EDITS = [
 ('C0-pointer',
  r'\A(# Supplementary Material)',
  '<!-- Blinded review copy. Unblinded counterpart: '
  'paper5_supplementary_v19_NatSustain.md. Accompanies blinded main v47. -->\n\n\\1',
  1, 0),
 ('C1-s2.3-cite',
  r'\(Abaee, 2026, §9\.5\)',
  '(citation blinded for review, §9.5)',
  1, 0),
 ('C2-budworm-cite',
  r'; Abaee, 2026\)',
  '; citation blinded for review)',
  1, 0),
 ('C3-delay-study-published',
  r'published as Abaee, 2026; the other companions',
  'published (citation blinded for review); the other companions',
  1, 0),
 ('C4-agent-paths',
  r'arena agent 1/',
  '[repository]/',
  4, 0),
 ('C5-commit-hashes',
  r'@ 24c980cd',
  '@ [blinded]',
  3, 0),
]

for name, pat, rep, expect, flags in EDITS:
    s, n = re.subn(pat, rep, s, flags=flags)
    print(f'{name}: {n} (expect {expect})')
    assert n == expect, name

for leak in ['Abaee', 'arena agent 1', '24c980cd']:
    assert leak not in s, f'LEAK: {leak}'
assert s.count('citation blinded for review') == 3
assert 'Blinded review copy' in s

open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST, len(s), 'chars')

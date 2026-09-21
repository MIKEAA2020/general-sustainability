"""Build paper5 v47 blinded main from v46 (double-blind review copy).

B1 version comment line -> v47 blinded note
B2 author identity comment -> blinded
B3 \\author block (name/affiliation/ORCID/email) -> Anonymous
B4 in-text self-cites (Abaee, 2026) -> (citation blinded for review
B5 reference entry (title blurb + Zenodo DOI) -> Author. 2026. [Blinded for review.]
B6 repo commit hashes -> @ [blinded]
B7 all four declaration subsections -> Anonymized for review.
"""
import re

SRC = '/home/user/paper5_v46/paper5_sampled_governance_v46_NatSustain.tex'
DST = '/home/user/paper5_v47/paper5_sampled_governance_v47_blinded_NatSustain.tex'

s = open(SRC, encoding='utf-8').read()

BLINDED_DECLS = (
"\\subsection*{Author contributions} Anonymized for review.\n\n"
"\\subsection*{Funding} Anonymized for review.\n\n"
"\\subsection*{Conflicts of interest} Anonymized for review.\n\n"
"\\subsection*{AI declaration} Anonymized for review.\n\n"
"\\end{document}")

EDITS = [
 ('B1-version-line',
  r'^% The decision clock \(paper 5, revision v46\):.*$',
  '% The decision clock (paper 5, revision v47, blinded for review): '
  'author details, self-citations and declarations anonymized. Unblinded counterpart: v46.',
  1, re.M),
 ('B2-author-comment',
  r'^% Amin Abaee.*$',
  '% Author details blinded for review.',
  1, re.M),
 ('B3-author-block',
  r'\\author\{Amin Abaee.*?ut\.ac\.ir\}\}\}',
  '\\author{Anonymous}',
  1, re.S),
 ('B4-self-cites',
  r'\(Abaee,\s*2026',
  '(citation blinded for review',
  6, 0),
 ('B4b-bare-cite',
  r'Abaee, 2026\)',
  '(citation blinded for review)',
  1, 0),
 ('B5-ref-entry',
  r'Abaee, A\. 2026\. Delay-induced.*?22554217\.',
  'Author. 2026. [Blinded for review.]',
  1, re.S),
 ('B6-commit-hashes',
  r'@ 24c980cd',
  '@ [blinded]',
  9, 0),
 ('B7-declarations',
  r'\\subsection\*\{Author contributions\}.*?\\end\{document\}',
  BLINDED_DECLS,
  1, re.S),
]

for name, pat, rep, expect, flags in EDITS:
    s, n = re.subn(pat, lambda m: rep, s, flags=flags)
    print(f'{name}: {n} (expect {expect})')
    assert n == expect, name

# Leak asserts: no identifier may survive.
for leak in ['Abaee', 'abaee', 'Amin', 'orcid', 'ORCID', '24c980cd',
             'zenodo', 'Zenodo', '22554217', 'ut.ac.ir', 'A. A.', 'Z.ai']:
    assert leak not in s, f'LEAK: {leak}'
assert s.count('Anonymized for review.') == 4
assert 'citation blinded for review' in s

open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST, len(s), 'chars')

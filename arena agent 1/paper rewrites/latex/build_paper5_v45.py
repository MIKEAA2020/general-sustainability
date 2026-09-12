"""Build paper5 v45 main from v43 (declarations completion).

R1 Author contributions placeholder -> A. A. statement
R2 Funding placeholder -> no-funding statement
R3 AI declaration: Z.ai hyperlink + author-responsibility sentence
R4 version comment line v43 -> v45
"""
import re

SRC = '/home/user/paper5_v43/paper5_sampled_governance_v43_NatSustain.tex'
DST = '/home/user/paper5_v45/paper5_sampled_governance_v45_NatSustain.tex'

s = open(SRC, encoding='utf-8').read()

EDITS = [
 ('R1-contributions',
  r'\\subsection\*\{Author contributions\}\s*\{\[}To be completed at submission\.\{\]}',
  r'\\subsection*{Author contributions} A. A. conceived the entire work and wrote and edited the manuscript.', 1),
 ('R2-funding',
  r'\\subsection\*\{Funding\}\s*\{\[}To be completed at submission\.\{\]}',
  r'\\subsection*{Funding} No funding was received.', 1),
 ('R3-ai-declaration',
  r'GLM \(Z\.ai\), Qwen \(Alibaba Cloud\) and DeepSeek AI assisted with drafting and iterative review\.',
  r'GLM (\\href{http://Z.ai}{Z.ai}), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review. The author reviewed and edited the work and takes responsibility for the content of the manuscript.', 1),
 ('R4-version-line',
  r'^% The decision clock \(paper 5, revision v43\):.*$',
  ('% The decision clock (paper 5, revision v45): declarations completion '
   '(contributions, funding, AI responsibility), with line numbers for review.'), 1),
]

for name, pat, rep, expect in EDITS:
    s, n = re.subn(pat, rep, s, flags=re.M)
    print(f'{name}: {n} (expect {expect})')
    assert n == expect, name

assert 'To be completed at submission' not in s
open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST, len(s), 'chars')

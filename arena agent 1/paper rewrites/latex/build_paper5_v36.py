"""Build paper5 v36 from v35 (supp v12 pointer). Asserted-once."""
import sys

SRC = '/home/user/paper5_v35/paper5_sampled_governance_v35.tex'
DST = '/home/user/paper5_v36/paper5_sampled_governance_v36.tex'

s = open(SRC, encoding='utf-8').read()
n0 = len(s)

SUBS = [
 ('Q-header',
  "% Periodic Review as Sampled Governance (paper 5, revision v35): supplementary-completeness and alignment revision (S1 currency, S2 notation, S2.3/Table-3 closed-form bridge, S8/App-A register pointers) with line numbers for review.",
  "% Periodic Review as Sampled Governance (paper 5, revision v36): supplementary-readability revision (sentence splits, glossary lists; no content change) with line numbers for review."),
 ('Q-pointer',
  "accompanying file \\texttt{paper5\\_supplementary\\_v11.md}",
  "accompanying file \\texttt{paper5\\_supplementary\\_v12.md}"),
]

fails = []
for tag, old, new in SUBS:
    c = s.count(old)
    if c != 1:
        fails.append((tag, c))
        continue
    s = s.replace(old, new, 1)

if fails:
    print('FAILED:', fails)
    sys.exit(1)
open(DST, 'w', encoding='utf-8').write(s)
print(f'v36 built: {len(SUBS)}/{len(SUBS)} subs ok, {n0} -> {len(s)} bytes')

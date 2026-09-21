"""Build paper5 supplementary v14 from v13: v38 consistency (title, S1 4.8 row, S8 fig script)."""
import re

SRC = '/home/user/paper5_v37/paper5_supplementary_v13.md'
DST = '/home/user/paper5_v38/paper5_supplementary_v14.md'
s = open(SRC, encoding='utf-8').read()
n0 = len(s)

def rep(old, new, tag):
    global s
    c = s.count(old)
    assert c == 1, f'{tag}: count={c}\n---\n{old[:200]}'
    s = s.replace(old, new, 1)
    print(f'{tag}: OK')

rep('*Accompanies: "Periodic Review as Sampled Governance: Sample-and-Hold Dynamics of Assessment-Driven Effort Control, a Selected 42-Stock Spectral Screen, and the Northern Cod Case."*',
    '*Accompanies: "The decision clock: review intervals as a design lever for stable resource governance."*',
    'P1-accompanies')

rep('- **Main text §4.7:** the nine limitations (status declarations; the battery outcomes restated from S9.1).',
    '''- **Main text §4.7:** the nine limitations (status declarations; the battery outcomes restated from S9.1).
- **Main text §4.8:** the four design principles and eight management implications (interpretive synthesis of the reported results; the cross-sector reading is illustrative, not a case claim).''',
    'P2-s1-48')

rep('and the η-basis window runs (`eta_basis.py`, `eta_basis.log`). On the open docket:',
    'and the η-basis window runs (`eta_basis.py`, `eta_basis.log`); and the conceptual-figure script (`fig_concept_v38.py`). On the open docket:',
    'P3-s8-figscript')

print('len delta:', len(s) - n0)
open(DST, 'w', encoding='utf-8').write(s)
print('WROTE', DST)

#!/usr/bin/env python3
"""Non-destructive cross-family abstract qualification for already-repaired paper01.
The earlier four scientific repairs and its live head/supplement remain untouched.
"""
from pathlib import Path
from difflib import unified_diff
import re
r=Path('/home/user');b=r/'content_audit/claim_alignment';src=r/'papers/paper01_obstruction_calculus_v63.tex';old=src.read_text();s=old
abstracts=re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',old,re.S);assert len(abstracts)==1
(b/'original_abstracts'/(src.stem+'.txt')).write_text(abstracts[0])
needle='The central common-action obstruction shows\nthat when the safe controls of compatible states intersect emptily, no\nobservation-based policy is viable, though every compatible state is\nindividually viable under full information.'
assert s.count(needle)==1
s=s.replace(needle,'The central common-action obstruction shows that, at a declared\ninformation state under its held-action and local adverse-selection\nhypotheses, disjoint safe-control sets exclude a jointly safe\nobservation-based policy, even when every compatible state is\nindividually viable under full information.',1)
assert old.count('A.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.')==s.count('A.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.')
out=b/'drafts'/src.name;out.write_text(s)
(b/'diffs'/(src.stem+'.diff')).write_text(''.join(unified_diff(old.splitlines(True),s.splitlines(True),fromfile=str(src),tofile=str(out))))
print(out)

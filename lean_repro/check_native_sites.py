#!/usr/bin/env python3
"""Block any change to the three approved native_decide source sites until reapproval.

Run against the verified checkout under the pinned toolchain. The exact SHA is
intentional: a moved/edited tactic cannot silently inherit the allowlist.
"""
from pathlib import Path
import hashlib
import re
import sys

APPROVED_SHA256 = '715659ee5cc53109c1e75f03a5a116fc03be7e752812c6728c645e9b6d08ac4c'
source = Path(sys.argv[1]) if len(sys.argv) == 2 else Path('lean/Formalizations/P3_SupportValue.lean')
raw = source.read_bytes()
sha = hashlib.sha256(raw).hexdigest()
assert sha == APPROVED_SHA256, f'APPROVED_NATIVE_SITE_CHANGED: {source} sha256 {sha}; separate review required'
text = raw.decode()
assert len(re.findall(r'\bnative_decide\b',text)) == 3, 'Native tactic site count drift'
assert 'cases x <;> native_decide' in text
for name in ('rat_half_ne_zero', 'wmBelief_total'):
    assert re.search(r'theorem '+name+r'\b[^\n]*:= by\s+native_decide\b',text),name
print('APPROVED_NATIVE_SITES_PASS three P3_SupportValue uses, SHA-256',sha)

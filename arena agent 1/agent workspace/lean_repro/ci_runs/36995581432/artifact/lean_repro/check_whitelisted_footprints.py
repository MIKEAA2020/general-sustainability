#!/usr/bin/env python3
"""Exact-name exception audit for AllFootprints.lean output.

Report-only by default; --gate fails on missing/malformed data, sorryAx,
unknown axioms, or malformed/duplicate allowlist. No wildcard allowance.
The pre-existing check_all_footprints.py remains the strict zero-exception gate.
"""
from collections import Counter
from pathlib import Path
import re
import sys

if len(sys.argv) not in (3, 4) or (len(sys.argv) == 4 and sys.argv[3] != '--gate'):
    raise SystemExit('usage: check_whitelisted_footprints.py ALL_LOG ALLOWLIST [--gate]')
text = Path(sys.argv[1]).read_text(errors='replace')
allowed_lines = [s.strip() for s in Path(sys.argv[2]).read_text().splitlines()
                 if s.strip() and not s.lstrip().startswith('#')]
assert len(allowed_lines) == len(set(allowed_lines)), 'Duplicate allowlist names'
assert allowed_lines and all(re.fullmatch(
    r'Formalizations\.P3\.(rat_half_ne_zero|wmBelief|wmBelief_total)\._native\.native_decide\.ax_[0-9_]+', n
) for n in allowed_lines), 'Unexpected or malformed explicit allowlist entry'
allowed = set(allowed_lines)
end = re.findall(r'^FOOTPRINT_TOTAL (\d+) UNEXPECTED_REFERENCES (\d+)$', text, re.M)
assert len(end) == 1, 'Missing or duplicate Lean completion marker'
rows = re.findall(r'^FOOTPRINT ([^ ]+) AXIOMS ', text, re.M)
pairs = re.findall(r'^UNEXPECTED ([^ ]+) AXIOM (.+)$', text, re.M)
assert len(rows) == int(end[0][0]) and len(rows) == len(set(rows)), 'Incomplete declaration inventory'
assert len(pairs) == int(end[0][1]), 'Incomplete unexpected-axiom inventory'
counts = Counter(ax for _, ax in pairs)
unknown = set(counts) - allowed
stale = allowed - set(counts)
print(f'DECLARATIONS={len(rows)} UNEXPECTED_REFERENCES={len(pairs)} DISTINCT_GENERATED_OR_OTHER_AXIOMS={len(counts)}')
print(f'EXACT_ALLOWLIST={len(allowed)} OBSERVED_ALLOWED={len(set(counts) & allowed)} UNKNOWN={len(unknown)} STALE={len(stale)}')
for name in sorted(counts):
    print(f'{"UNKNOWN" if name in unknown else "ALLOWED"}\t{counts[name]}\t{name}')
for name in sorted(stale):
    print(f'STALE_ENTRY\t{name}')
# A stale entry flags a cleanup task, but does not fail a successfully
# repaired declaration: it cannot admit a NEW axiom unless the name matches.
if unknown:
    print('AXIOM ALLOWLIST BLOCKED: unexplained generated or explicit axiom', file=sys.stderr)
    if '--gate' in sys.argv:
        raise SystemExit(2)
else:
    print('EXACT AXIOM ALLOWLIST PASS (not a zero-axiom verdict)')

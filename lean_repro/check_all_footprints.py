#!/usr/bin/env python3
"""Parse the report-only whole-project Lean footprint sweep, fail gate if unexplained.
Keep the report even on failure: generated native_decide axioms are real footprints.
"""
from collections import Counter
from pathlib import Path
import re
import sys

text = Path(sys.argv[1]).read_text(errors='replace')
end = re.findall(r'^FOOTPRINT_TOTAL (\d+) UNEXPECTED_REFERENCES (\d+)$', text, re.M)
assert len(end) == 1, 'Missing or duplicate full-environment completion marker'
rows = re.findall(r'^FOOTPRINT ([^ ]+) AXIOMS ', text, re.M)
assert len(rows) == int(end[0][0]) and len(set(rows)) == len(rows), 'Not one row per declaration'
pairs = re.findall(r'^UNEXPECTED ([^ ]+) AXIOM (.+)$', text, re.M)
assert len(pairs) == int(end[0][1]), 'Unexpected-axiom lines do not match Lean total'
axioms = Counter(ax for _, ax in pairs)
affected = len({name for name, _ in pairs})
print(f"DECLARATIONS={len(rows)} UNEXPECTED_REFERENCES={len(pairs)} DISTINCT_AXIOMS={len(axioms)} AFFECTED_DECLARATIONS={affected}")
for ax, n in sorted(axioms.items()):
    print(f'{n}\t{ax}')
assert not any('sorryAx' in ax for ax in axioms), 'sorryAx present'
if axioms:
    print('STRICT AXIOM GATE BLOCKED: do not silently whitelist native_decide axioms', file=sys.stderr)
    raise SystemExit(2)
print('STRICT AXIOM GATE PASS')

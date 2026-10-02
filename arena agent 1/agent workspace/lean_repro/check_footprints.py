#!/usr/bin/env python3
"""Fail closed if any requested #print axioms result is absent or unexpected.
This checks the named declarations in AxiomFootprint.lean, not every theorem in the project.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
queries = re.findall(r'^#print axioms ([\w.\u0080-\uffff]+)$', (ROOT / 'AxiomFootprint.lean').read_text(), re.M)
assert len(queries) == 21 and len(set(queries)) == len(queries), queries
text = Path(sys.argv[1]).read_text(errors='replace')
# Standard Lean 4 #print axioms info messages, with optional line wrapping.
no_axiom = re.findall(r"'([^']+)' does not depend on any axioms", text)
with_axioms = re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", text, re.S)
reported = no_axiom + [name for name, _ in with_axioms]
assert len(reported) == len(queries) and set(reported) == set(queries), (
    f'Footprint messages not one-for-one with source queries: expected {queries}, reported {reported}'
)
allowed = {'propext', 'Classical.choice', 'Quot.sound'}
for name, raw in with_axioms:
    found = {x.strip() for x in raw.split(',')}
    assert found and all(x in allowed for x in found), (name, 'unexpected axiom', sorted(found - allowed))
assert 'sorryAx' not in text, 'sorryAx found'
print(f'FOOTPRINT PASS: {len(queries)} named declarations; expected Lean-standard axioms only; no sorryAx')

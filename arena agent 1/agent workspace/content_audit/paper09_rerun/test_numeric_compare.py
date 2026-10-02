#!/usr/bin/env python3
"""Corpus and false-negative trials: report-only before CI policy promotion."""
from pathlib import Path
import csv
import json
import tempfile
from numeric_compare import compare, ABS_LIMIT, REL_LIMIT

B=Path(__file__).resolve().parent
root=B/'ci_runs/36958434317/artifact/arena agent 1/agent workspace/content_audit/paper09_rerun/ci_out'
assert root.is_dir()
core=[p for p in (root/'generated').rglob('*') if p.is_file() and 'xte' not in p.parts]
assert len(core)==5
for generated in sorted(core):
    expected=root/'expected'/generated.relative_to(root/'generated')
    result=compare(expected,generated)
    assert result['within_observed_envelope'],(generated,result['problems'])
    assert result['numeric_changed']>0
    print('REPORT_ONLY_CORE',generated.relative_to(root/'generated'),result['numeric_changed'],
          f"abs={result['max_absolute_difference']:.9g}",f"rel={result['max_relative_difference']:.9g}")
    assert result['max_absolute_difference']<=ABS_LIMIT and result['max_relative_difference']<=REL_LIMIT
    assert compare(expected,expected)['within_observed_envelope']
with tempfile.TemporaryDirectory() as d:
    test=Path(d)/'mutant.json'
    original=root/'expected/wave_e_cod/results/intervention_results_v3.json'
    obj=json.loads(original.read_text());obj['fit']['r']+=0.001;test.write_text(json.dumps(obj))
    assert not compare(original,test)['within_observed_envelope'];print('NEGATIVE_TEST numeric reported-parameter mutation detected')
    obj=json.loads(original.read_text());obj['fit']['r']+=0.0000005;test.write_text(json.dumps(obj))
    assert not compare(original,test)['within_observed_envelope'];print('NEGATIVE_TEST small-value relative drift detected')
    obj=json.loads(original.read_text());obj['fit'].pop('r');test.write_text(json.dumps(obj))
    assert not compare(original,test)['within_observed_envelope'];print('NEGATIVE_TEST dropped-key mutation detected')
    original=root/'expected/wave_e_cod/results/intervention_boundaries_v3.csv';test=Path(d)/'mutant.csv'
    rows=list(csv.reader(original.open()));rows[1][5]=rows[1][5].replace('1025.4856833494782','1025.5856833494782');
    with test.open('w',newline='') as f:csv.writer(f).writerows(rows)
    assert not compare(original,test)['within_observed_envelope'];print('NEGATIVE_TEST embedded-interval mutation detected')
    rows=list(csv.reader(original.open()));rows[0][0]='not_policy'
    with test.open('w',newline='') as f:csv.writer(f).writerows(rows)
    assert not compare(original,test)['within_observed_envelope'];print('NEGATIVE_TEST CSV schema mutation detected')
print('REPORT_ONLY_CORPUS_AND_NEGATIVE_TESTS_PASS',len(core),'drifted core files')

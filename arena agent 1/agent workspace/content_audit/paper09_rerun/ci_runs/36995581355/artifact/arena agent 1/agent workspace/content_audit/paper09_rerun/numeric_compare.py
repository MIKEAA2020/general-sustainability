#!/usr/bin/env python3
"""Report-only-first structural/numeric comparator for paper09 core JSON/CSV.

Preserves byte-SHA drift separately. Fails any schema/text/finite-status change,
and any numeric delta outside BOTH the declared absolute and relative limits.
Its limits describe the observed cross-host core corpus, not scientific proof.
"""
from pathlib import Path
import csv
import json
import math

ABS_LIMIT = 3e-5  # per-file native units; greater than observed core 2.3864e-6 .. 2.2158e-5
REL_LIMIT = 1e-6 # greater than observed core maximum 5.363e-7


def compare(expected: Path, generated: Path) -> dict:
    problems = []
    stats = {'numeric_changed': 0, 'max_absolute_difference': 0.0, 'max_relative_difference': 0.0}

    def walk(a, b, loc):
        if isinstance(a, bool) or isinstance(b, bool):
            if a != b or type(a) is not type(b): problems.append(f'{loc}: Boolean changed')
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if not (math.isfinite(a) and math.isfinite(b)):
                problems.append(f'{loc}: nonfinite number')
                return
            if a != b:
                absolute = abs(a-b)
                relative = absolute / max(abs(a),abs(b))
                stats['numeric_changed'] += 1
                stats['max_absolute_difference'] = max(stats['max_absolute_difference'], absolute)
                stats['max_relative_difference'] = max(stats['max_relative_difference'], relative)
                if absolute > ABS_LIMIT or relative > REL_LIMIT:
                    problems.append(f'{loc}: numeric drift {a!r} -> {b!r} (abs={absolute:.9g}, rel={relative:.9g})')
        elif isinstance(a, dict) and isinstance(b, dict):
            if a.keys() != b.keys():
                problems.append(f'{loc}: object keys changed')
            else:
                for key in a: walk(a[key], b[key], loc + '.' + key)
        elif isinstance(a, list) and isinstance(b, list):
            if len(a) != len(b):problems.append(f'{loc}: list length {len(a)} -> {len(b)}')
            else:
                for i,(x,y) in enumerate(zip(a,b)):walk(x,y,f'{loc}[{i}]')
        elif a != b or type(a) is not type(b):
            problems.append(f'{loc}: value changed {a!r} -> {b!r}')

    if expected.suffix == '.json':
        walk(json.loads(expected.read_text()),json.loads(generated.read_text()),'$')
    elif expected.suffix == '.csv':
        with expected.open(newline='') as f:aa=list(csv.reader(f))
        with generated.open(newline='') as f:bb=list(csv.reader(f))
        if len(aa)!=len(bb):problems.append(f'rows: {len(aa)} -> {len(bb)}')
        else:
            for i,(row,other) in enumerate(zip(aa,bb)):
                if len(row)!=len(other):problems.append(f'row {i}: column count changed');continue
                for j,(x,y) in enumerate(zip(row,other)):
                    if x==y:continue
                    # Embedded JSON interval arrays are semantic numeric cells.
                    if x.startswith('[') and y.startswith('['):
                        try:walk(json.loads(x),json.loads(y),f'row{i}.col{j}')
                        except (ValueError,TypeError) as ex:problems.append(f'row{i}.col{j}: malformed nested data: {ex}')
                        continue
                    try:
                        a,b=float(x),float(y)
                    except ValueError:
                        problems.append(f'row{i}.col{j}: text changed {x!r} -> {y!r}')
                        continue
                    walk(a,b,f'row{i}.col{j}')
    else:raise ValueError(f'unsupported comparison type: {expected}')
    stats['problems'] = problems[:20]
    stats['problem_count'] = len(problems)
    stats['within_observed_envelope'] = not problems
    return stats

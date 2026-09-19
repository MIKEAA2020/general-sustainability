#!/usr/bin/env python3
r"""pin_waiver_scope_v1.py - the row list the v49 waiver is allowed to touch, pinned and re-derived.

Why this file exists. The counts drifted in prose: "208 verbatim rows" and "222 more ruled sentences" were quoted
as if they were two disjoint populations, when the ruling's population is 290 reused rows of which 208 were actually
placed verbatim, and 222 is 290 minus the 68 rows that fall in Section 1. The gate cannot enforce "these rows may be
reworded, those may not" against a number quoted in prose, so this script recomputes every figure from the v48
artifacts, asserts them against the counts the v48 run recorded, and writes the authoritative lists to
`waiver_scope_v1.json`. If the v48 artifacts change, this script fails rather than silently re-pinning.

Run:  python3 /home/user/revision/v49/pin_waiver_scope_v1.py
"""
import collections
import hashlib
import json
import os
import sys

V48 = '/home/user/revision/v48'
OUT = '/home/user/revision/v49/waiver_scope_v1.json'
FILES = {n: f'{V48}/{n}' for n in ('split', 'audit', 'ledger', 'splice_log', 'overrules')}
FILES['split'] = f'{V48}/v48_reuse_split.json'
FILES['audit'] = f'{V48}/v48_reuse_audit.json'
FILES['ledger'] = f'{V48}/claim_ledger_v1.json'
FILES['splice_log'] = f'{V48}/v48_splice_log.json'
FILES['overrules'] = f'{V48}/v48_overrules.csv'


def sha(p, n=64):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:n]


def main():
    sp = json.load(open(FILES['split']))
    log = json.load(open(FILES['splice_log']))
    led = json.load(open(FILES['ledger']))
    overr = [l.strip().split(',')[0] for l in open(FILES['overrules']).read().strip().split('\n')[1:] if l.strip()]

    reuse = {r['id']: r for r in sp['reuse']}
    regen = {r['id']: r for r in sp['regen']}
    states = {l['id']: l['state'] for l in log['splice_log']}

    placed = {i for i, s in states.items() if s.startswith('inserted')}
    not_placed = {i for i, s in states.items() if not s.startswith('inserted')}

    # ---- assertions: the pin has to agree with what the v48 run recorded ----
    c = sp['counts']
    def eq(name, got, want):
        assert got == want, f'{name}: recomputed {got}, v48 recorded {want}'
        return got
    eq('reuse rows', len(reuse), c['reuse'])
    eq('regen rows', len(regen), c['regen'])
    eq('ledgered', len(reuse) + len(regen), c['ledgered'])
    eq('overrules recorded', len(overr), c['overrules_recorded'])
    eq('splice log length', len(states), len(reuse))
    eq('placed', len(placed), log['insert']['inserted'])
    eq('reuse split by kind', c['reuse_high_supported'] + c['reuse_signposting'], len(reuse))
    eq('regen split by kind', c['regen_medium_low_supported'] + c['regen_flagged'] + c['regen_by_overrule'], len(regen))
    assert not (set(overr) & set(reuse)), 'the 16 overrules are regen rows; none may sit in the reuse set'
    assert set(overr) <= set(regen), 'every overrule id must be a regen row'

    # ---- the Section 1 subset, and its placed / not-placed split ----
    s1 = sorted(i for i, r in reuse.items() if str(r.get('section', '')).startswith('1.'))
    s11 = sorted(i for i, r in reuse.items() if str(r.get('section', '')) == '1.1')
    s1_placed = [i for i in s1 if i in placed]
    s1_not = [i for i in s1 if i in not_placed]
    out_s1 = sorted(set(reuse) - set(s1))
    out_s1_placed = [i for i in out_s1 if i in placed]

    # what the waiver actually frees: reuse rows in Section 1 that v48 placed verbatim.
    # A row that was never placed has no verbatim protection in the built document to lift.
    pin = {
        'source_files': {os.path.basename(p): sha(p) for p in FILES.values()},
        'v48_counts': c,
        'recomputed': {
            'ruling_population_reuse_rows': len(reuse),
            'regenerated_rows': len(regen),
            'ledgered_total': len(reuse) + len(regen),
            'overrules_applied': len(overr),
            'reuse_placed_verbatim': len(placed),
            'reuse_not_placed': len(not_placed),
            'not_placed_by_reason': dict(collections.Counter(s for i, s in states.items() if i in not_placed)),
        },
        'section1': {
            'reuse_rows': len(s1),
            'reuse_rows_in_1_1': len(s11),
            'placed_verbatim': len(s1_placed),
            'not_placed': len(s1_not),
            'outside_section1_reuse_rows': len(out_s1),
            'outside_section1_placed_verbatim': len(out_s1_placed),
        },
        'waiver': {
            'granted_by': 'the author, 2026-09-19: "waive for the front matter only", with three guardrails',
            'scope': 'Section 1 and the abstract may be reworded; every other reuse row keeps its verbatim protection',
            'ids_freed_from_verbatim_protection': s1_placed,
            'ids_still_verbatim_protected': out_s1_placed,
            'ids_in_s1_already_not_placed': s1_not,
            'note': ('"ids_freed" is the set the gate may accept in reworded form. It is not permission to change a '
                     'claim: guardrails 1-3 in v49_waiver_gate_v1.py apply to exactly these rows.'),
        },
        'prose_claims_this_pin_corrects': {
            '"222 more ruled sentences stay verbatim"': (
                'wrong as phrased. 290 rows are ruled, 68 of them in Section 1, so 222 lie outside it - but only 145 '
                'of those 222 are placed verbatim, the other 77 were never placed. Outside Section 1 the verbatim '
                'protection the gate enforces is over ' + str(len(out_s1_placed)) + ' rows, not 222.'),
            '"208 verbatim rows and 222 more"': (
                '430 was never a population. 290 reuse + 268 regenerate = 558 ledgered sentences; 208 of the 290 were '
                'placed verbatim by the splice, 82 were not.'),
        },
    }
    json.dump(pin, open(OUT, 'w'), indent=1)

    print(f'pin written: {OUT}')
    print(f'  ruled reuse rows .............. {pin["recomputed"]["ruling_population_reuse_rows"]}   '
          f'(placed verbatim {pin["recomputed"]["reuse_placed_verbatim"]}, not placed {pin["recomputed"]["reuse_not_placed"]})')
    print(f'  regenerated rows .............. {pin["recomputed"]["regenerated_rows"]}   '
          f'(of which {c["regen_by_overrule"]} by overrule; overrules recorded {pin["recomputed"]["overrules_applied"]})')
    print(f'  ledgered total ................ {pin["recomputed"]["ledgered_total"]}')
    print(f'  Section 1 reuse rows .......... {pin["section1"]["reuse_rows"]}  '
          f'(in 1.1: {pin["section1"]["reuse_rows_in_1_1"]})')
    print(f'    placed verbatim, so freed ... {pin["section1"]["placed_verbatim"]}')
    print(f'    never placed, nothing to free  {pin["section1"]["not_placed"]}')
    print(f'  outside Section 1 ............. {pin["section1"]["outside_section1_reuse_rows"]} rows, '
          f'{pin["section1"]["outside_section1_placed_verbatim"]} of them verbatim-protected in the build')
    print('\n  not-placed reasons:', json.dumps(pin['recomputed']['not_placed_by_reason']))
    print('\n  source hashes:', json.dumps(pin['source_files'], indent=1).replace('\n', '\n  '))
    return 0


if __name__ == '__main__':
    sys.exit(main())

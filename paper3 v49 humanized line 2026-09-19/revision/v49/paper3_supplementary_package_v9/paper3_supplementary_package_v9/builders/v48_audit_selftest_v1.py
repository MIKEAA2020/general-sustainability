#!/usr/bin/env python3
"""Spot-check the audit's zero: plant six defects in rows the audit called clean, see how many it finds.

`v48_reuse_audit_v1.py` reported 296 of the 306 reused sentences with nothing raised. A number like that is either
the sentence set being clean or the checks being blind, and the two look identical from the outside. The ledger
already taught that lesson - the condition-removal detector caught 0 of 4 planted removals - so the same test is
run here on the audit itself: seven rows are taken from the reuse set, the audit is run over them as they stand to
get a baseline, then six of them are mutated one at a time and run again. A planted defect counts as caught only if
the flag it raises is a *new* one and names the check it was meant to trip. The seventh row is a control, mutated by
nothing, and should raise nothing new.

Writes `v48_audit_selftest.md`, the mutated `v48_reuse_split_selftest.json`, and the baseline file the diff is
taken against. Nothing here edits a document.
"""
import json
import subprocess
import sys

V48 = '/home/user/revision/v48'
AUDIT = f'{V48}/v48_reuse_audit_v1.py'
split = json.load(open(f'{V48}/v48_reuse_split.json'))
rows = split['reuse']


def find(sub, skip=()):
    for r in rows:
        if sub in r['text'] and r['id'] not in skip:
            return r
    raise SystemExit(f'self-test anchor not present in the reuse set: {sub}')


reserve = find("phosphate reserves have stayed near")
pointer = find("§2.1")
name = find("Illakwahhi")
status = find("uniform-margin assumption is doing all the work")
control = find("vintage is pinned once", skip={status['id']})
# two plants that need a row the audit currently clears outright, so a new flag cannot be pre-existing
plain = [r for r in rows if r['id'] not in {reserve['id'], pointer['id'], name['id'], status['id'],
                                            control['id'], 'D0156'}]
scope_row = next(r for r in plain if len(r['text']) < 170 and '§' not in r['text']
                 and 'Figure' not in r['text'] and r['text'].count('.') == 1)
voice_row = next(r for r in plain if r['text'].count('.') == 1 and 'The ' in r['text']
                 and r['id'] != scope_row['id'])

PLANTS = [
    ('unit', reserve, lambda t: t.replace('1,000,000 kt', '1,500,000 kt'), 'unit',
     'a reserve figure moved off the value the deposit attaches the unit to'),
    ('ref', pointer, lambda t: t.replace('§2.1', '§2.9'), 'ref',
     'a pointer to a subsection the deposited article does not have'),
    ('name', name, lambda t: t.replace('Illakwahhi', 'Zbarovski'), 'name',
     'a surname no source in the document carries'),
    ('status', status, lambda t: t + ' The certified version of this claim holds across every ledger.',
     'status', "a status label ('certified') on an object the deposit does not label so"),
    ('universal', scope_row, lambda t: t.rstrip('.') + ' Every reader of the ledger will want this number.',
     'universal', "an 'every' generalising who the statement is for"),
    ('voice', voice_row, lambda t: 'We argue in this paper that ' + t[0].lower() + t[1:], 'voice',
     'a first-person framing the deposited sentence does not carry'),
]


def run(rows_, tag):
    json.dump({'reuse': rows_}, open(f'{V48}/v48_reuse_split_{tag}.json', 'w'), indent=1)
    subprocess.run([sys.executable, AUDIT, f'{V48}/v48_reuse_split_{tag}.json',
                    f'{V48}/v48_reuse_audit_{tag}'], check=True, capture_output=True)
    return {r['id']: r['flags'] for r in json.load(open(f'{V48}/v48_reuse_audit_{tag}.json'))}


selected = [r for _, r, _, _, _ in PLANTS] + [control]
base = run(selected, 'selftest_base')
mut = []
for tag, row, fn, kind, why in PLANTS:
    after = fn(row['text'])
    assert after != row['text'], f'plant {tag} changed nothing - the anchor is wrong'
    r = dict(row)
    r['text'] = after
    r['why'] = f'{tag}: {why}'
    mut.append(r)
mut.append(dict(control))
got = run(mut, 'selftest')

lines = ["# Does the line-level audit see a planted flaw?\n",
         """Six defects planted in sentences taken from the 306 the audit cleared, one control left exactly as the
draft wrote it, both sets fed through `v48_reuse_audit_v1.py`. A flag counts only if it was not already on the
baseline run, so a row the audit happens to dislike for its own reasons cannot inflate the score.\n""",
         '\n| planted defect | row | expected | raised as a new flag | what the audit said |', '|---|---|---|---|---|']
caught = 0
detail = []
for tag, row, fn, kind, why in PLANTS:
    new = [x for x in got.get(row['id'], []) if x not in base.get(row['id'], [])]
    hit = [x for x in new if x.startswith(kind + ':')]
    caught += bool(hit)
    detail.append((kind, row['id'], bool(hit), new))
    lines.append(f'| {kind} - {why} | {row["id"]} | `{kind}` | {"**yes**" if hit else "**no**"} | '
                 f'{(hit[0] if hit else ("nothing new; new flags: " + (", ".join(x.split(":")[0] for x in new) or "none")))}'
                 f' |')
cn = [x for x in got.get(control['id'], []) if x not in base.get(control['id'], [])]
lines.append(f'| control, untouched | {control["id"]} | nothing | {"clear" if not cn else "not clear"} | '
             f'{", ".join(cn) or "no new flags"} |')
lines.append(f"\n**Detection {caught}/6**, control {'clean' if not cn else 'raised something'}. " + (
    'Every planted defect raised the check it was planted to trip, so the 296 cleared rows are a reading of the '
    'sentences and not the silence of a blind filter - for the six classes these checks claim to cover, which is '
    'what the row-level read in `v48_reuse_read.md` then stands on.'
    if caught == 6 else
    'Where the table says no, that class of flaw is not detectable by this audit, and the rows the audit cleared '
    'are only as good as the six kinds that did fire. Those classes get read by hand.'))
open(f'{V48}/v48_audit_selftest.md', 'w').write('\n'.join(lines) + '\n')
print(f'detection {caught}/6; control new flags {len(cn)}')
for kind, rid, ok, new in detail:
    print(f'  {kind:10s} {rid} {"CAUGHT" if ok else "MISSED":7s} new={[x.split(":")[0] for x in new]}')

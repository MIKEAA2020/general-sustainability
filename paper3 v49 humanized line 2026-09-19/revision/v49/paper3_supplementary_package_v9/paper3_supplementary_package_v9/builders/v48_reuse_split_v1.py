#!/usr/bin/env python3
"""The reuse ruling for v48, written down where the build reads it.

    Reuse the 306 as-is. Regenerate the 252 from the deposit in the draft's register - and for the 188 medium and
    low-confidence rows go to the deposit rather than minimally editing the draft, because the alignment is what is
    uncertain there and the truth source is the safer input. Keep the one unsupported sentence, regenerated at the
    deposit's scope. Disclose the 306 as screened, not certified.

This file turns that ruling into data so the build does not re-derive it at a seam, which is the failure the
project has been paying for all week. It reads `claim_ledger_v1.json`, applies the rule, and writes
`v48_reuse_split.json` (the two sets, each row carrying its draft sentence and the deposit passage to regenerate
from) and `v48_reuse_split.md` (the same, in prose, plus the disclosure line the package README must carry).

It changes no document. It is a ruling made mechanical, not an edit.
"""
import csv
import json
import os
import re

OUT = '/home/user/revision/v48'
LEDGER = f'{OUT}/claim_ledger_v1.json'
DEPOSIT = '/home/user/revision/v7/paper3_material_ledgers_v42.md'


def conf(x):
    return 'high' if x['ratio'] > .60 or x['score'] > .45 else ('medium' if x['score'] > .18 else 'low')


def flat_str(s):
    return re.sub(r'\s+', ' ', re.sub(r'\*\*|`|\$', '', s)).strip()


def main():
    rows = json.load(open(LEDGER))['rows']
    led = [x for x in rows if not x['verdict'].startswith('excluded')]
    sup = [x for x in led if x['verdict'].startswith('supported')]
    sig = [x for x in led if x['verdict'].startswith('not a claim')]
    flg = [x for x in led if x['verdict'].startswith(('needs check', 'unsupported', 'contradicted'))]
    reuse = [x for x in sup if conf(x) == 'high'] + sig
    regen = [x for x in sup if conf(x) != 'high'] + flg
    assert len(reuse) + len(regen) == len(led), 'the two sets do not partition the ledger'

    # The author's markup, if there is any. The ruling is the default and the adjudication is the exception, so an
    # overrule moves a row from one set to the other and says so in the file, rather than being remembered in a
    # chat that the next build will not read. One line per row: `id,decision`, decision in
    # {keep, regenerate}; `claim_ledger_v1_attribution_review.md` is where they are most likely to be found.
    import os
    moved = []
    if os.path.exists(f'{OUT}/v48_overrules.csv'):
        keep, drop = {x['id'] for x in reuse}, {x['id'] for x in regen}
        with open(f'{OUT}/v48_overrules.csv') as fh:
            for row in csv.DictReader(fh):
                rid = (row.get('id') or '').strip()
                dec = (row.get('decision') or '').strip().lower()
                if rid not in keep | drop or dec not in ('keep', 'regenerate'):
                    moved.append((rid, dec, 'ignored: unknown id or decision'))
                    continue
                if (dec == 'keep' and rid in keep) or (dec == 'regenerate' and rid in drop):
                    moved.append((rid, dec, 'no change: that is already the ruling\u2019s set'))
                elif dec == 'keep' and rid in drop:
                    x = next(y for y in regen if y['id'] == rid)
                    regen.remove(x)
                    x['overruled'] = 'the author keeps the draft’s sentence'
                    reuse.append(x)
                    moved.append((rid, dec, 'regenerated -> reused'))
                elif dec == 'regenerate' and rid in keep:
                    x = next(y for y in reuse if y['id'] == rid)
                    reuse.remove(x)
                    x['overruled'] = 'the author sends it to the deposit anyway'
                    regen.append(x)
                    moved.append((rid, dec, 'reused -> regenerated'))
        reuse.sort(key=lambda x: x['id'])
        regen.sort(key=lambda x: x['id'])
    assert len(reuse) + len(regen) == len(led), 'an overrule broke the partition'

    # counts from final membership: an overrule moves a row between sets, and the breakdown has to follow it,
    # or the table adds up to a partition that no longer exists
    # a row the author moved is its own category: it is neither medium/low-supported nor flagged, and calling it
    # flagged would put my instrument's verdict on the author's decision
    reuse_mv = sum(1 for x in reuse if x.get('overruled'))
    reuse_hi = sum(1 for x in reuse if not x.get('overruled') and x['verdict'].startswith('supported')
                   and conf(x) == 'high')
    reuse_sig = len(reuse) - reuse_hi - reuse_mv
    regen_mv = sum(1 for x in regen if x.get('overruled'))
    regen_med = sum(1 for x in regen if not x.get('overruled') and x['verdict'].startswith('supported')
                    and conf(x) != 'high')
    regen_flg = len(regen) - regen_med - regen_mv
    assert reuse_hi + reuse_sig + reuse_mv == len(reuse), 'the reuse breakdown does not sum'
    assert regen_med + regen_flg + regen_mv == len(regen), 'the regenerate breakdown does not sum'

    # the deposit's own scope, for the one sentence the draft wrote on its own authority
    dep = open(DEPOSIT).read()
    ent = {'id': 'D0081', 'draft': next(x['draft'] for x in led if x['id'] == 'D0081'),
           'deposit_says': re.findall(r'[^.\n]{0,300}cross-component trades?[^.\n]{0,120}\.', dep)[:3],
           'rule': 'regenerate at the deposit\u2019s scope: non-compensation is asserted of the certificate that '
                   'a weighted sum returns, not of the ledger entire, and the deposit never uses the word revenue'}

    json.dump(dict(
        ruling=('the draft\u2019s non-shared sentences are reused verbatim only where the ledger pairs them with a '
                'deposit proposition at high confidence, or where they assert nothing; everything else is written '
                'again from the deposit in the draft\u2019s register'),
        screened_not_certified=('the reused set is screened, not certified: what the ledger checked is that a '
                               'partner passage exists and that values, hedges, conditions, attributions and '
                               'inference markers do not diverge from it. It did not check that the draft understood '
                               'the argument. Register is certified by the draft being the source; accuracy is '
                               'certified for the regenerated set by coming from the deposit, and for the reused '
                               'set only by the absence of a divergence the rules can see.'),
        counts=dict(ledgered=len(led), reuse=len(reuse), regen=len(regen),
                    reuse_high_supported=reuse_hi, reuse_signposting=reuse_sig,
                    regen_medium_low_supported=regen_med, regen_flagged=regen_flg,
                    reuse_by_overrule=reuse_mv, regen_by_overrule=regen_mv,
                    overrules_effective=reuse_mv + regen_mv,
                    overrules_recorded=len([m for m in moved if 'already' not in m[2]])),
        reuse=[dict(id=x['id'], section=x['sec'], text=x['draft'], why=('supported at high confidence'
                                                                        if x['verdict'].startswith('supported')
                                                                        else 'signposting: asserts nothing'),
                    verdict=x['verdict'], confidence=conf(x)) for x in reuse],
        regen=[dict(id=x['id'], section=x['sec'], text=x['draft'], verdict=x['verdict'], confidence=conf(x),
                    deposit_passage=x.get('dep_passage', ''), deposit_sentence=x.get('dep', ''),
                    flags=[f'{g[0]}: {g[1]} \u2014 {g[2]}' for g in x['flags']]) for x in regen],
        unsupported_addition=ent, overrules_applied=moved),
        open(f'{OUT}/v48_reuse_split.json', 'w'), indent=1)

    from collections import Counter
    n_hi, n_med = reuse_hi, regen_med
    n_sig, n_flg = reuse_sig, regen_flg
    n_mv = (reuse_mv, regen_mv)
    quoted = ' and '.join('"' + re.sub(chr(92) + 's+', ' ', s).strip().rstrip('.') + '"'
                           for s in ent['deposit_says'][:2])
    if not quoted:
        quoted = 'nothing about revenue at all'
    L = []
    L.append('# v48: what is reused, what is regenerated\n')
    L.append('Written by `v48_reuse_split_v1.py` from the claim ledger, so the ruling is one file the build reads '
             'instead of a decision re-made at each seam. **' + str(len(reuse)) + ' sentences are reused as the '
             'draft wrote them; ' + str(len(regen)) + ' are written again from the deposit in the draft\u2019s '
             'register.** The two sets partition the ' + str(len(led)) + ' ledgered sentences; the '
             + str(sum(1 for x in rows if x['verdict'].startswith('excluded')))
             + ' sentences the draft shares verbatim with the deposit are outside the question, since they are the '
             'deposit\u2019s own wording.\n')
    L.append('| set | n | why |\n|---|---|---|')
    L.append(f'| reused: high-confidence supported | {n_hi} | a partner passage was found and no marker diverges |')
    L.append(f'| reused: signposting | {n_sig} | the sentence reports what the document does and asserts nothing '
             f'about the world |')
    if n_mv[0]:
        L.append(f'| reused: by the author\u2019s markup | {n_mv[0]} | moved out of the regenerated set by '
                 f'`v48_overrules.csv` |')
    L.append(f'| regenerated: medium or low confidence | {n_med} | the pairing itself is uncertain, so the '
             f'draft\u2019s sentence is not a safe input; go to the deposit |')
    L.append(f'| regenerated: flagged | {n_flg} | a value, hedge, condition, attribution or inference differs '
             f'from the passage it restates |')
    if n_mv[1]:
        L.append(f'| regenerated: by the author\u2019s markup | {n_mv[1]} | moved out of the reused set by '
                 f'`v48_overrules.csv`; the reuse was sound on words and unsound on notation |')
    L.append('')
    L.append('## The medium and low-confidence rows, in the author\u2019s words\n')
    L.append('Thin confidence is not a finding against the draft; it is a finding about the alignment - a '
             'plain-English sentence and its technical original share few words, so the pairing is thin and the '
             'marker comparison is only as good as it. The ruling therefore sends those rows to the deposit rather '
             'than asking the build to touch up the draft: where the alignment is uncertain, the truth source is '
             'the safer input. The draft supplies the voice for them, not the sentence.\n')
    L.append('## The one sentence the draft wrote on its own authority\n')
    L.append('`' + ent['id'] + '` reads: "' + flat_str(ent['draft']) + '" The deposit\u2019s claim is narrower and '
             'differently worded: ' + quoted + '. The word *revenue* does not appear in the deposited article. It is '
             'kept - it is the draft\u2019s own synthesis and the one place the humanizer said something its source '
             'did not - and it is regenerated at the deposit\u2019s scope: non-compensation is a claim about what a '
             'weighted sum can certify, not a prohibition written into every line of the ledger. Disclosed here, in '
             'the build note, and in the package README.\n')
    L.append('## Screening, not certification\n')
    L.append('The line-level read of these sentences (`v48_reuse_audit.md`, `v48_reuse_read.md`, '
             '`v48_reuse_findings.md`) raised three prose flaws the marker rules could not see - D0089, D0108, '
             'D0158 - and found 16 sentences carrying a symbol form the deposited article reserves for another '
             'object. `v48_overrules_notation_candidate.csv` moves those 16 to the regenerated set; nothing has '
             'been applied, and the counts below are the ruling as the ledger gives it.\n')
    L.append('The ' + str(len(reuse)) + ' reused sentences are **screened, not certified**. What the ledger checked '
             'is that a partner passage exists and that values, hedges, conditions, attributions and inference '
             'markers do not diverge from it. It did not check that the draft understood the argument, and a '
             'sentence can pass every test here while carrying a claim the paper means differently. The register of '
             'the reused set is owed to the draft being its own source; the accuracy of the regenerated set is owed '
             'to coming from the deposit; the accuracy of the reused set is owed to the author, and this file is '
             'where that is said out loud instead of being implied by a green check.\n')
    L.append('## The regenerated rows, by class\n\n| verdict | n |\n|---|---|')
    for k, v in Counter(x['verdict'] for x in regen).most_common():
        L.append(f'| `{k}` | {v} |')
    L.append('\nEvery row is in `v48_reuse_split.json`: the reused ones with the reason they are reused, the '
             'regenerated ones with the deposit passage to write from and the flags that sent them there.\n')
    open(f'{OUT}/v48_reuse_split.md', 'w').write('\n'.join(L))
    if moved:
        print('overrules applied: ' + '; '.join(f'{a} {b} {c}' for a, b, c in moved))
    print(f'reuse {len(reuse)} (high supported {reuse_hi} + signposting {reuse_sig}), '
          f'regenerate {len(regen)} (medium/low {sum(1 for x in sup if conf(x) != "high")} + flagged {len(flg)}), '
          f'partition {len(reuse) + len(regen)} of {len(led)}')


if __name__ == '__main__':
    main()

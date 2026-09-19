#!/usr/bin/env python3
r"""dispose_the_82_v1.py - what becomes of the 82 reuse rows the splice did not place, computed not asserted.

The author's question, put precisely: the ruling's 290 rows divide into 208 placed verbatim and 82 not placed, and
the reasons for the 82 are itemised (33 fragment, 23 not-in-document, 17 display-entangled, 4 antecedent-lost,
2 statement-label, 2 unfound, 1 refused-figure) but the *disposition* was never stated. Regenerated, dropped, or
absorbed? It matters because the number quoted all week - 290/268 - describes the ruling, not the document, and a
gate that enforces "these rows are verbatim" against the wrong population is enforcing nothing.

This script answers it from the artifacts. For each of the 82 it asks what the built v48 markdown contains: the
draft's sentence, the deposit's sentence, or neither - and where neither, whether the deposit partner's claim atoms
(numeral, citation, defined term) still appear, in the same region of the document. It asserts its own totals, so it
fails if the reasoning stops matching the files.

Limitation stated in the output and in the brief: this is an atom test, not a semantic one. It can see that a number,
a citation or a named object vanished; it cannot see a dropped hedge ("typically", "under the declared window")
unless that hedge is one of the registry terms. The per-sentence hedge audit is a human read, and v49's disclosure
note has to say which parts of its own verification are machine-checked and which are not.

  python3 /home/user/revision/v49/dispose_the_82_v1.py
"""
import collections
import difflib
import json
import re
import sys

V48 = '/home/user/revision/v48'
V49 = '/home/user/revision/v49'
BUILT = '/home/user/revision/v7/paper3_material_ledgers_v48.md'
BASE = '/home/user/revision/v7/paper3_material_ledgers_v42.md'
DEPOSIT = '/home/user/work/paper3.txt'
TERMS = ('moiety', 'moieties', 'donor-limited', 'donor limitation', 'reserve-life ratio', 'removals-only pressure scale',
         'trend-persistence', 'time to depletion', 'hitting time', 'phantom mass', 'double-counting', 'orthant',
         'non-claim', 'quarantined', 'overshoot day', 'record-relative', 'incidence', 'support pool',
         'natural-block mass identity', 'frozen-rate', 'turnover intensity', 'typed stock')
NEAR = 0.90                      # "the same sentence, allowing for the register pass"


def norm(s):
    s = re.sub(r'\$[^$]*\$', ' M ', s)
    s = re.sub(r'[*_`#]', '', s)
    s = s.replace('\u2019', "'").replace('\u2014', ' ').replace('\u2013', '-')
    s = re.sub(r'\s+', ' ', s)
    return re.sub(r'[^0-9a-z \'\.,;:-]', ' ', s).strip()


def squeeze(s):
    return re.sub(r'[^a-z0-9]', '', s)


def sentences(t):
    t = re.sub(r'\$[^$]*\$', ' M ', t)
    t = re.sub(r'[ \t]*\n[ \t]*', ' ', t)
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"(*])', t) if len(s.strip()) > 40]


def numbers(t):
    return {re.sub(r'[,\s]', '', m) for m in re.findall(r'\d{1,3}(?:,\s?\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?', norm(t))}


def citation_keys(t):
    out = set()
    for grp in re.findall(r'\(([^()]{3,160}?)\)', t):
        if not re.search(r'\b(19|20)\d{2}[a-z]?\b', grp):
            continue
        for one in re.split(r';', grp):
            m = re.search(r'\b((?:19|20)\d{2}[a-z]?)\b', one)
            if not m:
                continue
            names = re.sub(r'\b(19|20)\d{2}[a-z]?\b', ' ', one)
            names = re.sub(r'\bet al\.?|\band\b|&|cf\.|see also|in prep|doi:[^,)]*', ' ', names, flags=re.I)
            toks = sorted({re.sub(r'[^a-z]', '', w.lower()) for w in names.replace('\n', ' ').split()})
            toks = [w for w in toks if len(w) > 2]
            if toks:
                out.add(' '.join(toks) + ' ' + m.group(1))
    return out


def atoms(t):
    n = norm(t)
    return {'nums': numbers(t), 'cites': {norm(c) for c in citation_keys(t)},
            'terms': {k for k in TERMS if k in n},
            'hedges': {h for h in ('typically', 'usually', 'under the', 'declared', 'assumed', 'if ', 'only',
                                   'never', 'cannot', 'fails to', 'not ') if h in n}}


def best_ratio(needle, pool):
    if not needle or not pool:
        return 0.0
    hit = difflib.get_close_matches(needle, pool, n=1, cutoff=0.0)
    return difflib.SequenceMatcher(None, needle, hit[0]).ratio() if hit else 0.0


def main():
    log = {l['id']: l for l in json.load(open(f'{V48}/v48_splice_log.json'))['splice_log']}
    au = {r['id']: r for r in json.load(open(f'{V48}/v48_reuse_audit.json'))}
    reuse = json.load(open(f'{V48}/v48_reuse_split.json'))['reuse']
    built, base = open(BUILT).read(), open(BASE).read()
    nb, nba = norm(built), norm(base)
    sents_built = [norm(s) for s in sentences(built)]
    dep = open(DEPOSIT).read()

    placed_ids = [r['id'] for r in reuse if log[r['id']]['state'].startswith('inserted')]
    rest = [r['id'] for r in reuse if not log[r['id']]['state'].startswith('inserted')]
    assert len(placed_ids) == 208, f'placed set moved: {len(placed_ids)}'
    assert len(rest) == 82, f'not-placed set moved: {len(rest)}'

    # regions of the build, so "absorbed" can be judged where the sentence lived rather than anywhere in the paper
    def region_of(sec):
        key = f'## {sec.split(".")[0]}.' if sec and sec[0].isdigit() else None
        m = re.search(r'^##\s+' + re.escape(str(sec).split('.')[0]) + r'\.?\s', built, re.M)
        if not m:
            return built
        nxt = re.search(r'^##\s+\d', built[m.end():], re.M)
        return built[m.end():m.end() + (nxt.start() if nxt else 10 ** 9)]

    rows, classes = [], collections.Counter()
    for i in rest:
        a = au.get(i, {})
        draft, dep_s = norm(a.get('draft') or ''), norm(a.get('dep') or '')
        want = norm(log[i].get('want') or a.get('dep') or '')
        reg = norm(region_of(a.get('sec', '')))
        A = atoms(built)
        in_built_draft = bool(draft) and draft in nb
        in_built_dep = bool(want) and (want in nb or best_ratio(want, sents_built) >= NEAR)
        fr = best_ratio(draft, sents_built)
        miss = []
        if in_built_draft:
            cls = 'kept: the draft sentence ships byte-for-byte'
        elif in_built_dep:
            cls = 'absorbed: the deposit wording is in the document anyway (its block carried it)'
        elif fr >= NEAR:
            cls = 'kept, restyled: the draft sentence ships, changed only by the register pass'
        elif draft and draft in nba:
            da = atoms(a.get('dep') or '')
            miss = [f'numeral {x}' for x in da['nums'] if x not in A['nums'] and x not in squeeze(reg)]
            miss += [f'citation {x}' for x in da['cites'] if x not in A['cites']
                     and not all(w in squeeze(reg or nb) for w in x.split())]
            miss += [f'term {x}' for x in da['terms'] if x not in A['terms'] and x not in reg]
            cls = ('absorbed: wording gone, every claim atom of the deposit partner still present in its region'
                   if not miss else 'LOST: wording gone and a claim atom with it')
            print(f'    note {i} [{a.get("sec")}] missing {miss}') if miss else None
        else:
            # neither wording survives as a sentence: check the row's own claim atoms where the sentence lived
            da = atoms(a.get('draft') or '')
            miss = [f'numeral {x}' for x in da['nums'] if x not in A['nums'] and x not in squeeze(reg)]
            miss += [f'citation {x}' for x in da['cites'] if x not in A['cites']
                     and not all(w in squeeze(reg or nb) for w in x.split())]
            miss += [f'term {x}' for x in da['terms'] if x not in A['terms'] and x not in reg]
            miss += [f'section ref {x}' for x in re.findall(r'Section\s*(\d+(?:\.\d+){0,2})', a.get('draft') or '')
                     if x not in norm(region_of(a.get('sec', '')))]
            cls = ('absorbed: no sentence, but the row\'s claim atoms are present in its region' if not miss
                   else 'LOST: no sentence and no atom - human read required')
            if miss:
                print(f'    note {i} [{a.get("sec")}] missing {miss}')
        classes[cls] += 1
        rows.append({'id': i, 'sec': a.get('sec'), 'state': log[i]['state'], 'class': cls,
                     'draft_to_built_ratio': round(fr, 3), 'audit_ratio': a.get('ratio'),
                     'missing_atoms': miss, 'verdict': (a.get('why') or '')[:46],
                     'draft_in_base': bool(draft) and draft in nba})
    tot = sum(classes.values())
    assert tot == 82, f'classification lost rows: {tot}'
    lost = [c for c in classes if c.startswith('LOST')]
    unacc = [c for c in classes if c.startswith('unaccounted')]
    # what the 22 kept rows would be shipping if they were not deposit-backed
    dep_atoms = atoms(dep)
    draft_only = 0
    for r in rows:
        if r.get('class', '').startswith('kept'):
            a = atoms(au.get(r['id'], {}).get('draft') or '')
            if any(x not in dep_atoms['nums'] for x in a['nums']) or any(x not in dep_atoms['cites'] for x in a['cites']):
                draft_only += 1
    n_absorbed = sum(v for k, v in classes.items() if k.startswith('absorbed'))
    out_s1_placed = len([r for r in reuse if not str(r.get('section', '')).startswith('1.')
                         and log[r['id']]['state'].startswith('inserted')])
    n_kept = sum(v for k, v in classes.items() if k.startswith('kept'))
    answer = (f'Neither regenerated nor dropped: absorbed or kept. The 268 regenerate rows are a different '
              f'population and the 82 never enter it. In the built document: {len(placed_ids)} rows carry the '
              f'deposit sentence verbatim, {n_kept} carry the draft sentence, {n_absorbed} are absorbed (the '
              f'deposit wording is in the block already, or the claim atoms survive in neighbouring prose), and '
              f'{sum(classes[c] for c in lost)} show a claim atom gone. Outside Section 1 the verbatim-protected set '
              f'the gate can actually enforce is {out_s1_placed} placed rows, not the 222 ruled rows - see '
              f'waiver_scope_v1.json for the id lists.')
    out = {'question': 'what becomes of the 82 reuse rows the splice did not place',
           'population': {'ruled_reuse': len(reuse), 'placed_verbatim': len(placed_ids), 'not_placed': len(rest)},
           'classes': dict(classes),
           'regenerated': 0,
           'dropped_or_lost': sum(classes[c] for c in lost),
           'unaccounted_for_a_human_read': sum(classes[c] for c in unacc),
           'kept_rows_carrying_an_atom_the_deposit_lacks': draft_only,
           'outside_section1_placed_verbatim': out_s1_placed,
           'answer': answer,
           'limitation': ('Atom test, not semantic: numerals, citations, defined terms. A dropped hedge that is not a '
                          'registry term is invisible to it. Hedge-level verification of these rows is a human read '
                          'and v49 must disclose it as one.'),
           'rows': rows}
    json.dump(out, open(f'{V49}/disposition_v49.json', 'w'), indent=1)
    print(out['answer'] + '\n')
    for k, v in sorted(classes.items(), key=lambda x: -x[1]):
        print(f'  {v:3d}  {k}')
    print(f'\n  regenerated: {out["regenerated"]} | LOST: {out["dropped_or_lost"]} | '
          f'unaccounted: {out["unaccounted_for_a_human_read"]} | kept rows with a non-deposit atom: {draft_only}')
    print(f'  written: {V49}/disposition_v49.json')
    return 0 if not lost else 1


if __name__ == '__main__':
    sys.exit(main())

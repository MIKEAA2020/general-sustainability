#!/usr/bin/env python3
"""The document-pointers in the reused set, checked against what they point at.

A signposting sentence was reused because it asserts nothing about the world. But it asserts something about the
document - `§2.1`, `Theorem 8`, `the eight zero entries`, `three certification layers` - and the ledger never
checked any of that: its markers look at values, hedges, conditions, attributions and inference words inside the
aligned passage, and a pointer is none of those. This file takes the 290 rows the ruling keeps and verifies each
pointer twice: that the target exists in the deposited article, and that the target is about what the sentence says
it is about. The second test is deliberately loose - overlap of content words - because its job is to produce a list
to read, not a verdict.

It also checks the count assertions: `the three X`, `the eight Y`, `all six Z`, `both W`. Those are the sentences
that most look like harmless connectives and most often state something the paper does not.

Writes `v48_pointers.md`, `v48_pointers.json`, `v48_pointers.csv`. Nothing here edits a document.
"""
import csv
import json
import re
from collections import Counter

V48 = '/home/user/revision/v48'
DEPOSIT = '/home/user/revision/v7/paper3_material_ledgers_v42.md'
SPLIT = f'{V48}/v48_reuse_split.json'
AUDIT = f'{V48}/v48_reuse_audit.json'
DRAFT = '/home/user/humanized/v1/paper3_humanized_v1_full.md'

POINTER = re.compile(r'\b(?P<noun>Sections?|Theorems?|Lemmas?|Propositions?|Definitions?|Remarks?|Corollaries?|'
                     r'Tables?|Figures?|Exhibits?|Assumptions?|Protocols?|Counterexamples?|Examples?|'
                     r'Conditional Theorems?)\s*(?P<num>\d+(?:\.\d+){0,3})(?:[–—-](?P<thru>\d+(?:\.\d+){0,3}))?')
SECREF = re.compile(r'§\s*(?P<num>\d+(?:\.\d+){0,3})(?:[–—-]\s*(?P<thru>\d+(?:\.\d+){0,3}))?')
COUNTS = re.compile("(?:the|all|both|of the|into)\\s+(?P<w>one|two|three|four|five|six|seven|eight|nine|"
                    "ten|eleven|twelve)\\b\\s+(?P<obj>[A-Za-z][A-Za-z\u2019'\\- ]{2,40}?)"
                    "(?=[\\s,.:;)\u2014]|$)")
WORD = re.compile(r'[A-Za-z]{4,}')
STOP = set('''the this that these those with from have been being their there which while what when where into over
under about above below upon then than also such same other others each every neither either none cannot must
should would could might does doing done make makes made take takes taken give gives given using used still even
only just more most less least very much many few both all any can may might not now here'''.split())


def norm(s):
    s = re.sub(r'\$[^$]*\$', ' ', s)
    s = re.sub(r'[*_`#|]', ' ', s)
    return set(w.lower() for w in WORD.findall(s)) - STOP


def content_words(s):
    return norm(s)


def index_deposit(txt):
    """number -> (title, body) for sections; label -> (title, body) for numbered objects"""
    secs, objs = {}, {}
    lines = txt.split('\n')
    for i, l in enumerate(lines):
        m = re.match(r'^(#{1,6})\s+(?:(\d+(?:\.\d+){0,3})[.\s]\s*)?(.*)$', l)
        if m:
            num, title = m.group(2), m.group(3)
            body = '\n'.join(lines[i + 1:i + 14])
            if num:
                secs[num] = (title, body)
            continue
        m = re.match(r'^\s*(?:\*\*)?\s*(Conditional Theorem|Theorem|Lemma|Proposition|Definition|Remark|Corollary|'
                     r'Exhibit|Counterexample|Example|Protocol|Assumption|Construction|Reading note|Table)\s+'
                     r'(\d+)\s*(?:\(([^)]*)\))?([^\n]*)', l)
        if m:
            kind, num, title, rest = m.group(1), m.group(2), m.group(3) or '', m.group(4)
            objs.setdefault(f'{kind.lower()} {num}', []).append(
                (title or rest.strip().strip('*').strip(), '\n'.join(lines[i:i + 10])))
        m2 = re.match(r'^\s*\*\*\s*(Conditional Theorem|Theorem|Lemma|Proposition|Definition|Remark|Corollary|'
                      r'Exhibit|Counterexample|Example|Protocol|Assumption)\s+(\d+)\s*(?:\(([^)]*)\))?', l)
        if m2:
            k, num, t = m2.group(1), m2.group(2), m2.group(3) or ''
            key = f'{k.lower()} {num}'
            if not any(t[:12] in o[0] for o in objs.get(key, [])):
                objs.setdefault(key, []).append((t, '\n'.join(lines[i:i + 10])))
    return secs, objs


def main():
    reuse = json.load(open(SPLIT))['reuse']
    audit = {r['id']: r for r in json.load(open(AUDIT))}
    txt = open(DEPOSIT).read()
    dtxt = open(DRAFT).read()
    secs, objs = index_deposit(txt)
    led = {r['id']: r for r in json.load(open(f'{V48}/claim_ledger_v1.json'))['rows']}
    rows, tally = [], Counter()
    for x in reuse:
        a = audit.get(x['id'], {})
        t = a.get('draft') or x['text']
        seen = []
        for m in POINTER.finditer(t):
            noun, num, thru = m.group('noun').lower(), m.group('num'), m.group('thru')
            base = noun.rstrip('s').lower()
            if base.startswith('section'):
                tgt = secs.get(num)
                seen.append(dict(kind='section', ref=f'Section {num}' + (f'-{thru}' if thru else ''),
                                 exists=bool(tgt) or any(s == num or s.startswith(num + '.') for s in secs),
                                 title=(tgt[0] if tgt else ''), body=(tgt[1] if tgt else '')))
                if not seen[-1]['exists']:
                    tally['missing-section'] += 1
                continue
            key = f'{base} {num}'
            got = objs.get(key) or []
            # the range form: Theorems 7-9
            extra = []
            if thru:
                for k in range(int(num) + 1, int(thru) + 1):
                    extra += objs.get(f'{base} {k}') or []
            if not got and not extra:
                tally['missing-label'] += 1
            seen.append(dict(kind=base, ref=f'{noun.title()} {num}' + (f'-{thru}' if thru else ''),
                             exists=bool(got or extra), title=got[0][0] if got else (extra[0][0] if extra else ''),
                             body=(got or extra or [('', '')])[0][1]))
        for m in SECREF.finditer(t):
            num, thru = m.group('num'), m.group('thru')
            ok = any(s == num or s.startswith(num + '.') for s in secs)
            if not ok:
                tally['missing-§'] += 1
            seen.append(dict(kind='section', ref=f'§{num}' + (f'-{thru}' if thru else ''), exists=ok,
                             title=secs.get(num, ('', ''))[0], body=secs.get(num, ('', ''))[1]))
        for m in COUNTS.finditer(t):
            w, obj = m.group('w'), ' '.join(m.group('obj').split())
            numeral = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                       'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12}[w]
            hit = re.search(r'(?i)\b' + re.escape(obj.split()[-1]) + r'\b', txt)
            # how many of them does the deposit actually show? count table rows / list items carrying the noun
            tail = obj.split()[-1].rstrip('.').lower()
            dep_lines = len(re.findall(r'(?im)^[^\n]*\b' + re.escape(tail) + r'\b[^\n]*$', txt))
            seen.append(dict(kind='count', ref=f'the {w} {obj}', exists=True, title='',
                             body=f'deposit lines naming "{tail}": {dep_lines}', count_word=w, count_n=numeral,
                             obj=tail))
        pas = (led.get(x['id'], {}).get('dep_passage') or '') + ' ' + (led.get(x['id'], {}).get('dep') or '')
        for s in seen:
            if s['kind'] == 'count':
                s['as_deposit'] = bool(re.search(r'(?i)\b' + re.escape(s['ref'].split()[-1]) + r'\b', pas))
                continue
            num = re.search(r'(\d+(?:\.\d+){0,3})', s['ref']).group(1)
            s['as_deposit'] = bool(re.search(r'(?i)(?:§\s*|Sections?\s+|' + s['kind'] + r's?\s+)' +
                                             re.escape(num) + r'\b', pas))
            s['as_draft'] = not s['as_deposit']
            if s['as_draft']:
                tally['pointer-the-deposit-does-not-cite-here'] += 1
        sw = content_words(t)
        for s in seen:
            if s['kind'] == 'count' or not s['body']:
                continue
            ov = len(sw & content_words(s['title'] + ' ' + s['body'][:700]))
            s['overlap'] = ov
            if s['exists'] and ov <= 1:
                tally['pointer-with-no-shared-content'] += 1
        flagged = [s for s in seen if not s['exists']
                   or (s.get('as_draft') and s.get('overlap', 9) <= 1 and s['kind'] != 'count')]
        rows.append(dict(id=x['id'], why=x['why'], sec=x.get('section', ''), sent=t, pointers=seen,
                         flagged=flagged))
    ptr_rows = [r for r in rows if r['pointers']]
    L = ['# The document-pointers in the reused set\n',
         f'''{len(ptr_rows)} of the {len(reuse)} sentences kept for verbatim reuse point at something in the document - a
section, a numbered theorem, a table, or a count ("the three certification layers", "the eight zero entries").
{sum(len(r["pointers"]) for r in ptr_rows)} pointers in all. Two tests per pointer: does the target exist in the
deposited article, and does the *deposit cite that target in the passage behind the sentence* - because a pointer to
a real number that points at the wrong thing is invisible to a numbering check, and a pointer the deposit itself
wrote in the same passage is not the humanizer\u2019s claim to make. {tally["pointer-the-deposit-does-not-cite-here"]}
pointers are the draft\u2019s own; those are the rows below.\n''',
         '\n| what was found | count |', '|---|---|']
    for k in ('missing-section', 'missing-§', 'missing-label', 'pointer-with-no-shared-content',
              'pointer-the-deposit-does-not-cite-here'):
        L.append(f'| {k.replace("-", " ")} | {tally[k]} |')
    L.append('\n## Rows with a pointer to read\n')
    for r in sorted(ptr_rows, key=lambda x: (-len(x['flagged']), x['id'])):
        L.append(f"### {r['id']} · {r['why']} · draft §{r['sec'] or 'front'}"
                 + ('  **[FLAGGED]**' if r['flagged'] else '') + '\n')
        L.append(f"> {r['sent'][:400]}\n")
        for s in r['pointers']:
            tag = ('MISSING' if not s['exists'] else 'ok' if not s.get('as_draft')
                   else 'read - the deposit does not cite this target in the passage behind the sentence')
            L.append(f"- `{s['ref']}` · {tag}" + (f" · target: *{s['title'][:70]}*" if s['title'] else ''))
            if s.get('overlap') is not None and s['kind'] != 'count':
                L.append(f"  content words shared with the target: {s['overlap']}; target opens: "
                         f"\"{re.sub(chr(92)+'s+',' ',s['body'][:220]).strip()}\"")
            if s['kind'] == 'count':
                L.append(f"  {s['body']}")
        L.append('\n**Disposition:** ☐ the pointer is right ☐ the sentence needs regenerating ☐ other: ______\n')
    open(f'{V48}/v48_pointers.md', 'w').write('\n'.join(L) + '\n')
    json.dump(rows, open(f'{V48}/v48_pointers.json', 'w'), indent=1)
    with open(f'{V48}/v48_pointers.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['id', 'why', 'pointer', 'kind', 'exists', 'overlap', 'target_title', 'flagged'])
        for r in rows:
            for s in r['pointers']:
                w.writerow([r['id'], r['why'], s['ref'], s['kind'], s['exists'], s.get('overlap', ''),
                            s['title'][:90], 'yes' if s in r['flagged'] else ''])
    print(f'{len(ptr_rows)} rows with pointers, {sum(len(r["pointers"]) for r in ptr_rows)} pointers · '
          f'{len([r for r in ptr_rows if r["flagged"]])} rows flagged · {dict(tally)}')


if __name__ == '__main__':
    main()

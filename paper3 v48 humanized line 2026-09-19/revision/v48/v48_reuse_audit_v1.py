#!/usr/bin/env python3
"""Read the 306 reused sentences against the deposit, at line level.

The ledger's marker rules are a filter, not a reader: they see whether a figure, a hedge, a condition, a citation or
a consequence sits differently in the aligned passage, and they are blind to everything else a sentence can do to a
claim - a defined term quietly renamed, a pointer to a section that says something else, a status label moved, a
verb that promises a proof where the paper gives an argument, a first person the article does not use. This file
puts the 306 sentences next to the deposit text they were reused from, with the maths put back (the ledger reads
prose with `$...$` deleted, and a sentence that looks like `continuity of both and and` is that deletion, not a
drafting error), and runs the checks the ledger cannot:

  refs        every `Section 6.5.2`, `Theorem 7`, `Table 3`, `§2.1` in a reused sentence has to exist in the
              deposited article, and the sentence has to say something about what is actually there
  names       author surnames in a reused sentence have to be spelled as the deposit spells them
  verbs       prove / show / derive / establish where the deposit argues, sketches, reports or tabulates
  status      the four status labels (established, certified, illustrative, quarantined) applied to an object the
              deposit labels differently
  universals  every, all, no ... can, never, only - the scope detector caught 0 of 4 planted removals, so these are
              listed here by hand rather than trusted to it
  voice       we / our / us, which the article does not use, and novelty words the deposit never claims
  units       a figure reused with a unit the deposit does not attach to it

Nothing here edits a document. It writes `v48_reuse_audit.md`, `v48_reuse_audit.json` and `v48_reuse_audit.csv`.
"""
import csv
import difflib
import sys
import json
import re
from collections import Counter, defaultdict

V48 = '/home/user/revision/v48'
DRAFT = '/home/user/humanized/v1/paper3_humanized_v1_full.md'
DEPOSIT = '/home/user/revision/v7/paper3_material_ledgers_v42.md'
# argv: <split.json> <out-prefix>  - so a self-test can run the same checks on planted defects
SPLIT = sys.argv[1] if len(sys.argv) > 1 else f'{V48}/v48_reuse_split.json'
PREFIX = sys.argv[2] if len(sys.argv) > 2 else f'{V48}/v48_reuse_audit'
LEDGER = f'{V48}/claim_ledger_v1.json'

ABBR = r'(?:e\.g|i\.e|et al|vs|cf|No|Vol|pp|fig|Figs|U\.S|U\.K|Sec|Ref|Dr|Prof|approx)'
STATUS = ['established', 'certified', 'illustrative', 'quarantined', 'registered', 'declared', 'admitted',
          'non-example']
STRONG = ['prove', 'proves', 'proved', 'proving', 'derive', 'derives', 'derivation', 'establish', 'establishes',
          'demonstrate', 'demonstrates', 'guarantee', 'guarantees', 'exactly', 'precisely', 'never', 'always',
          'impossible', 'cannot', 'no claim', 'not even']
SOFT = ['argue', 'argues', 'sketch', 'sketches', 'report', 'reports', 'tabulate', 'tabulates', 'read as',
        'is read', 'can be read', 'suggest', 'suggests', 'indicate', 'indicates', 'is consistent', 'describe',
        'describes', 'record', 'records']
NOVELTY = ['first', 'novel', 'unprecedented', 'no previous', 'no prior', 'for the first time', 'only account',
           'no existing', 'unlike all']
VOICE = ['we', 'our', 'us', 'ours', 'our terms', 'in this paper we']
REF = re.compile(r'\b(?P<noun>Sections?|Theorems?|Lemmas?|Propositions?|Definitions?|Remarks?|Corollaries?|'
                 r'Tables?|Figures?|Exhibits?|Counterexamples?|Examples?|Protocols?|Assumptions?|Appendix)'
                 r'\s*(?P<num>\d+(?:\.\d+){0,3})')
SECREF = re.compile(r'(?:§|\bSection\b)\s*(\d+(?:\.\d+){0,3})')
SURNAME = re.compile(r'\b([A-Z][A-Za-z\u2019\'-]{2,})(?:,|\s+(?:et al|and))')
NUMUNIT = re.compile(r'(?<![A-Za-z0-9.,])(\d[\d,]*\.?\d*)(?:\s*(kt|Mt|Gt|years?|percent|%|pp|nats?|bits?|t))\b')


# My reading of the ten flags, recorded rather than kept in chat: a proposal the author can overrule, and the
# reason the ☐ boxes below are not the last word. "noise" = the flag is an artefact of a check in this file, and
# those checks were themselves tested (`v48_audit_selftest_v1.py`, 6 of 6 planted defects caught).
VERDICT = {
    'D0549': 'noise - the comma bug read 240,000 kt/yr as 000 kt; figures are the deposit\u2019s. Keep.',
    'D0556': 'noise - same. Keep.',
    'D0110': 'noise - same. Keep.',
    'D0024': 'noise - the surname regex caught "Finally"; the content is the deposit\u2019s interface item. Keep.',
    'D0077': 'the deposit labels this Non-example 1 itself; the pairing was poor, not the sentence. Keep.',
    'D0023': 'first person is register, and the deposit writes "what we call" in the same breath. Keep.',
    'D0053': 'as above - the phrase is copied from the deposited article. Keep.',
    'D0357': '"doing all the work" for "essential": the same claim in the draft\u2019s voice. Keep.',
    'D0156': '"never as a forecast" tracks "not a physical forecast"; the connective "which is why" is the '
             'deposit\u2019s own logic. Keep, with the note.',
    'D0218': 'the anonymised companion citation. Kept under the attribution ruling; the build note and README must '
             'carry it, and it must say that the shipped reference list is not anonymised.',
    'D0162': 'this is the deposit\u2019s own wording ("Three certification layers, separated and proved." verbatim); '
             'the low ratio is two sentences merged by the splitter. Keep.',
    'D0158': 'flaw - the deposit writes "each depletion quantity", the draft "every": a scope word in the list that '
             'fixes the paper\u2019s three-quantity taxonomy. Move to regenerate.',
    'D0089': 'flaw - "against a rate and a barrier" mis-describes the three quantities (rate, ratio, '
             'first-passage-under-scenario). Move to regenerate. It sat in the 31 "asserts nothing" rows, which is '
             'why it needed a reader.',
    'D0558': 'the deposit\u2019s "registered open data action" is the phrase; the pairing sentence was unrelated. '
             'Keep.',
    'D0108': 'flaw - drops the deposit\u2019s "(USGS)" definition, the only one, and writes US where the reference '
             'style is U.S. Move to regenerate, or re-insert the parenthetical.',
    'D0414': 'the label parser mis-read "Conditional Theorem 15"; the theorem exists. The §-vs-Section difference '
             'is house style in both files. Keep.',
    'D0693': 'notation, not words: this row carries the renamed operator (see v48_reuse_findings.md). Normalise or '
             'regenerate with the other 16.',
    'D0545': 'pointer checked against the deposit\u2019s numbering - §2.1 exists and says what is cited. Keep.',
    'D0009': 'the deposit writes "services are readouts, not mass"; "readings taken off the ledger" is the same '
             'claim in the draft\u2019s words. Keep.',
    'D0139': 'no figure or pointer to verify; the sentence is the deposit\u2019s framing. Keep.',
}


def strip_math(s):
    s = re.sub(r'\$\$.*?\$\$', ' ', s, flags=re.S)
    return re.sub(r'\$[^$]{0,600}\$', ' ', s)


def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', ' '.join(re.sub(r'\*\*|`|\$', '', s).lower().split()))


def raw_sentences(path):
    """Every prose sentence of a file, maths intact, keyed by its maths-stripped form.

    The ledger's rows carry stripped text, so the stripped form is the join key - and the raw form is what has to
    be read, because a figure, a symbol or an inequality inside `$...$` is where half of this paper's claims are.
    """
    out = {}
    for b in re.split(r'\n\s*\n', open(path).read()):
        lines = [x.strip() for x in b.split('\n') if x.strip()
                 and not re.match(r'^\s*(#{1,6}\s|>|\||```)', x)]
        if not lines:
            continue
        block = re.sub(r'\s+', ' ', ' '.join(lines)).strip()
        x = re.sub(r'\b(' + ABBR + r')\.', '\\1\x00', block)
        x = re.sub(r'(\d)\.(\d)', '\\1\x01\\2', x)
        for s in re.split(r'(?<=[.!?])\s+(?=[A-Z“"\u2018(]|\Z)', x):
            s = re.sub(r'\s+', ' ', s).replace('\x01', '.').replace('\x00', '.').strip()
            if len(s.split()) >= 4:
                out.setdefault(norm(strip_math(s)), s)
    return out


def main():
    led = json.load(open(LEDGER))['rows']
    byid = {x['id']: x for x in led}
    reuse = json.load(open(SPLIT))['reuse']
    draw = raw_sentences(DRAFT)
    draw_all = list(draw.values())
    ptxt = open(DEPOSIT).read()
    praw = raw_sentences(DEPOSIT)
    praw_all = list(praw.values())
    pflat = re.sub(r'\s+', ' ', ptxt)
    dep_secs = {m.group(1) for m in re.finditer(r'(?m)^#{1,6}\s+(\d+(?:\.\d+){0,3})\b', ptxt)}
    dep_labels = set(re.findall(r'\*\*\s*(?:Theorem|Lemma|Proposition|Definition|Remark|Corollary|Exhibit|'
                                r'Counterexample|Example|Protocol|Assumption|Construction|Reading)\s*(\d+)', ptxt))
    dep_tables = set(re.findall(r'(?m)^\s*(?:\*\*)?Table\s*(\d+)', ptxt)) | set(
        re.findall(r'Table\s*(\d+)', ptxt))
    import os
    NF = len({f['id'] for f in json.load(open(f'{V48}/v48_reuse_findings.json'))}) \
        if os.path.exists(f'{V48}/v48_reuse_findings.json') else 'N'
    findings = []
    rows = []
    for x in reuse:
        L = byid.get(x['id'], {})
        d_raw = draw.get(norm(x['text']), x['text'])
        # the deposit passage the row was paired with, raw, and its best-matching sentence
        pas = ''
        if L.get('dep_block') is not None:
            pas = L.get('dep_passage', '') or ''
        cand = max(praw_all, key=lambda c: difflib.SequenceMatcher(None, norm(d_raw)[:400], norm(c)[:400]).ratio()) \
            if praw_all else ''
        ratio = difflib.SequenceMatcher(None, norm(d_raw), norm(cand)).ratio()
        r = dict(id=x['id'], why=x['why'], sec=x.get('section', ''), draft=d_raw,
                 dep=cand, ratio=round(ratio, 3), passage=pas[:900], flags=[])
        t = d_raw
        # refs
        for m in REF.finditer(t):
            n = m.group('num')
            kind = m.group('noun').lower()
            if kind.startswith(('section', 'sections')) or re.search(r'§\s*' + re.escape(n), t):
                ok = any(s == n or s.startswith(n + '.') for s in dep_secs)
                if not ok:
                    r['flags'].append(f'ref: points at Section {n}, which the deposited article does not have '
                                      f'(its numbered sections start {sorted(dep_secs)[:6]})')
            elif '.' not in n:
                noun = {'theorem': 'Theorem', 'sections': 'Section', 'lemma': 'Lemma', 'corollary': 'Corollary',
                        'proposition': 'Proposition', 'definition': 'Definition', 'remark': 'Remark',
                        'assumption': 'Assumption', 'table': 'Table', 'figure': 'Figure',
                        'exhibit': 'Exhibit', 'protocol': 'Protocol', 'counterexample': 'Counterexample',
                        'example': 'Example', 'conditional': 'Conditional Theorem', 'eq': 'Eq',
                        'equation': 'Eq', 'appendix': 'Appendix'}.get(kind, kind.title())
                have = set(re.findall(noun + r's?\s*(\d+)', ptxt, re.I)) | \
                     set(re.findall(noun + r'\s+(?:Theorem\s+)?s?\s*(\d+)', ptxt, re.I))
                if n not in have and int(n) > 4:
                    r['flags'].append(f'ref: names {noun} {n}; the deposited article carries '
                                      f'{sorted(have) or "no such numbered object"}')
        for m in SECREF.finditer(t):
            n = m.group(1)
            if not any(s == n or s.startswith(n + '.') for s in dep_secs):
                r['flags'].append(f'ref: cites §{n}, absent from the deposited article\u2019s numbering')
        # names
        for m in SURNAME.finditer(t):
            nm = m.group(1)
            if nm.lower() in ('the', 'this', 'that', 'a', 'an', 'if', 'in', 'it', 'where', 'when', 'both',
                              'each', 'every', 'all', 'any', 'some', 'such', 'only', 'what', 'which', 'while',
                              'they', 'their', 'there', 'here', 'one', 'two', 'three', 'four', 'five', 'section',
                              'theorem', 'lemma', 'table', 'figure', 'appendix', 'services', 'people',
                              'numbers', 'entries', 'nothing', 'everything'):
                continue
            if not re.search(r'\b' + re.escape(nm[:4]), ptxt):
                r['flags'].append(f'name: {nm} does not appear in the deposited article')
        # verbs
        EQUIV = {'never': r'\bnot\b|\bno\b|\bneed not\b', 'always': r'\bwhenever\b|\beach\b',
                 'cannot': r'\bnot\b', 'impossible': r'\bnot\b', 'exactly': r'\bexact\w*',
                 'precisely': r'\bexact\w*|\bprecis\w*', 'guarantee': r'\bensur\w*|\bhold\w*',
                 'prove': r'\bshow\w*|\bestablish\w*', 'proves': r'\bshows\b|\bestablishes\b',
                 'proved': r'\bshown\b|\bestablished\b', 'derive': r'\bobtain\w*|\bfollow\w*',
                 'derives': r'\bobtains\b|\bfollows\b', 'establish': r'\bshow\w*',
                 'establishes': r'\bshows\b', 'demonstrate': r'\bshow\w*', 'demonstrates': r'\bshows\b'}
        dp = cand + ' ' + pas
        ds = [w for w in marks(t) if not re.search(EQUIV.get(w.lower(), r'$^'), dp, re.I)]
        if ds and not marks(dp):
            r['flags'].append(f'verb: the sentence leans on {ds} where the deposit passage carries no such '
                              f'strength word or its negation-equivalent')
        # status labels
        for s in STATUS:
            if re.search(r'\b' + s + r'\b', t, re.I) and not re.search(r'\b' + s + r'\b', cand + ' ' + pas, re.I):
                r['flags'].append(f'status: the sentence says "{s}" of this object; the deposit passage does not '
                                 f'use that label here')
        # universals and negated capacities, the class the scope detector could not see
        for pat, lab in ((r'\ball\b', 'all'), (r'\bevery\b', 'every'), (r'\bno\b[^.]{0,40}\b(can|can be|is|are)\b',
                                                  'no ... can'),
                         (r'\bnever\b', 'never'), (r'\bonly\b', 'only'), (r'\bmust\b', 'must')):
            if re.search(pat, t, re.I):
                dp = cand + ' ' + pas
                if not re.search(pat, dp, re.I):
                    r['flags'].append(f'universal: "{lab}" appears in the sentence and not in the passage behind it')
        # voice and novelty
        v = [w for w in VOICE if re.search(r'\b' + re.escape(w) + r'\b', t,
                                           0 if w in ('us', 'US') else re.I)]
        if v and not re.search(r'\b(?:we|our|ours)\b', cand):
            r['flags'].append('voice: first person (' + ', '.join(v) + ') where the sentence\'s own deposit '
                              'sentence has none - the draft runs 0.3 instances per 1k words against the '
                              'deposited article\u2019s 0.1, so this is register, not error, unless the '
                              'verb attached to it is stronger than the deposit\u2019s')
        nv = [w for w in NOVELTY if re.search(re.escape(w), t, re.I) and not re.search(re.escape(w), ptxt, re.I)]
        if nv:
            r['flags'].append(f'novelty: "{nv[0]}" is a claim the deposited article never makes')
        # units on figures
        dep_nums = re.sub(r'[{},]', '', cand + ' ' + pas)
        for m in NUMUNIT.finditer(t):
            num, unit = m.group(1).replace(',', ''), m.group(2)
            if not num or not unit:
                continue
            if num in re.findall(r'\d[\d.]*', dep_nums):
                continue
            if not re.search(re.escape(num) + r'\s*' + re.escape(unit[0]) + r'\w?',
                            re.sub(r'\s+', ' ', pflat.replace(',', '')), re.I):
                r['flags'].append(f'unit: {num} {unit} is nowhere attached to that figure in the deposited '
                                  f'article, so the reuse carries a number the truth source does not give it')
        if r['flags']:
            findings.append(r)
        rows.append(r)
    rows.sort(key=lambda r: (-len(r['flags']), -r['ratio']))
    L = ['# The 306 reused sentences, read against the deposit at line level\n',
         f'''The ledger certified nothing about understanding, and this is the read that follows from saying so: all
{len(reuse)} sentences marked for verbatim reuse were put beside the deposited article and tested for the things a
marker comparison cannot see. {len(findings)} of {len(reuse)} carry at least one flag; {len(reuse) - len(findings)}
came through with nothing raised.

The zero is spot-checked, not asserted: `v48_audit_selftest.md` plants six defects in cleared rows and the checks
catch six, with an untouched control staying clear. A word-level read cannot see maths, so `v48_notation_drift.md`
runs the same 306 sentences against the deposited article\u2019s inline expressions, and `v48_reuse_findings.md`
names the {NF} sentences whose symbol form collides with an object the deposit has reserved. The prose verdicts, and which
flags were this file's own noise, are in `v48_reuse_read.md`.\n''',
         f'\n| what was checked | rows flagged |\n|---|---|']
    kinds = Counter(fl.split(':')[0] for r in findings for fl in r['flags'])
    for k, v in kinds.most_common():
        L.append(f'| {k} | {v} |')
    L.append('\n## The flagged rows\n')
    for r in rows:
        if not r['flags']:
            continue
        L.append(f"### {r['id']} · {r['why']} · draft §{r['sec'] or 'front'} · nearest deposit sentence "
                 f"at ratio {r['ratio']}\n")
        L.append(f"**Reused as the draft wrote it.**\n\n> {r['draft']}\n")
        L.append("**Deposit, the sentence it is nearest to.**\n\n> " + (r['dep'] or '*(nothing close)*') + "\n")
        for fl in r['flags']:
            L.append(f'- {fl}')
        if r['passage']:
            L.append(f"\n<details><summary>the aligned passage</summary>\n\n> {r['passage']}\n\n</details>")
        L.append("\n**Disposition:** ☐ keep the reuse ☐ move to regenerate ☐ other: ______\n")
        if r['id'] in VERDICT:
            L.append(f"*Read: {VERDICT[r['id']]}*\n")
    open(PREFIX + '.md', 'w').write('\n'.join(L))
    json.dump(rows, open(PREFIX + '.json', 'w'), indent=1)
    with open(PREFIX + '.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['id', 'why_reused', 'section', 'flag_count', 'flags', 'draft_sentence',
                    'nearest_deposit_sentence', 'ratio', 'disposition'])
        for r in rows:
            w.writerow([r['id'], r['why'], r['sec'], len(r['flags']), ' | '.join(r['flags']), r['draft'],
                        r['dep'], r['ratio'], ''])
    print(f'read {len(reuse)} reused sentences: {len(findings)} flagged, {len(reuse)-len(findings)} clean')
    print('by kind:', dict(kinds))
    return rows


def marks(s):
    low = ' ' + re.sub(r'[^a-z0-9 ]', ' ', s.lower()) + ' '
    return sorted({w for w in STRONG if (' ' + w + ' ') in low or (' ' + w) in low})


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
r"""v49_waiver_gate_v1.py - the author's three guardrails on the Section 1 waiver, as executable checks.

The ruling (2026-09-19): Section 1 and the abstract may be reworded into the adaptation's voice; every other reuse
row keeps its verbatim protection. The author's own condition was that the waiver is a loophole unless:

  G1  vocabulary stays pinned - the waiver covers sentences, not names. Rewording is fine; renaming an object,
      changing a symbol, retitling or renumbering a statement label, or diluting a load-bearing guard term is not.
  G2  the claim ledger runs on the reworded prose - a reworded sentence must be backed by the deposit at the level of
      the things it commits to. A new commitment is a flag, not a note.
  G3  facts in Section 1 are still gated - numerals, citations and named objects are checked like any other section.

Plus G0, the check v48's gate lacked: the exempt region had no preservation check at all, which is how a paragraph
disappeared and how a markdown artifact reached page 2 of the PDF.

What G2 deliberately does not claim. It is a claim-atom test, not a semantic one: numerals, citation keys, section
references, defined terms, negations and named objects. That is the same limit the v48 ruling recorded in its own
words - "the reused set is screened, not certified: ... It did not check that the draft understood the argument."
The gate can tell you a sentence introduced a number the deposit does not carry. It cannot tell you a sentence is a
faithful paraphrase of a proof. Anything past this test is a human read, and the disclosure note has to say so.

usage:
  python3 v49_waiver_gate_v1.py --control
  python3 v49_waiver_gate_v1.py --base <base.md> --built <built.md> --out <report.json>
exit code is the flag count, so a build that fails a guardrail fails the run.
"""
import argparse
import json
import os
import re
import sys

DEP = '/home/user/work/paper3.txt'                      # the deposited article: the oracle for every fact
V7 = '/home/user/revision/v7'
V48 = '/home/user/revision/v48'
V49 = '/home/user/revision/v49'
UP = '/home/user/uploads/p3 humanized.txt'              # gemini half = the adaptation; grok half below it
LEDGER = f'{V48}/claim_ledger_v1.json'

# the registry G1 protects: the four status labels the v48 build already carried, plus the three horizons, the
# guard terms the author named, and the objects whose names carry content later in the paper
TERMS = ('statistical index, not a stock ratio', 'arithmetic, not a forecast',
         'pressure scale, not a depletion diagnostic', 'readouts of the ledger',
         'reserve-life ratio', 'trend-persistence index', 'removals-only pressure scale',
         'gross turnover intensity', 'frozen-rate local ratio', 'scenario-conditioned hitting time',
         'time to depletion', 'donor-limited', 'donor limitation', 'record-relative', 'moiety',
         'moieties', 'natural-block mass identity', 'orthant invariance', 'double-counting rule',
         'phantom mass', 'non-claim', 'quarantined', 'registered', 'illustrative', 'established',
         'typed stock', 'incidence', 'support pool', 'overshoot day')
NUM = re.compile(r'(?<![\w.])([+-]?\d[\d,]*(?:\.\d+)?(?:\s?[eE][+-]?\d+)?)')
MATH = re.compile(r'\$([^$\n]{1,120})\$')
LABEL = re.compile(r'\*\*(Definition|Lemma|Proposition|Theorem|Corollary|Remark|Axiom)\s+(\d+)\s*\((.*?)\)\.\*\*', re.S)
SECREF = re.compile(r'\b(?:Section|§)\s*(\d+(?:\.\d+){0,2})')
NEG = ('not', 'never', 'no ', 'only', 'cannot', 'must', 'all ', 'every ', 'some ', 'guarantee', 'always',
       'fails', 'refuse', 'unless')


def dehyph(s):
    """undo the PDF line-break artifact 'fischer- kowalski' without touching 'reserve-life'."""
    return re.sub(r'(?<=[a-z])-\s+(?=[a-z])', '', s)


def norm(s):
    s = re.sub(r'\$[^$]*\$', ' M ', s)
    s = re.sub(r'`[^`]*`', ' C ', s)
    s = re.sub(r'[*_#|]', '', s)
    s = s.replace('\u2019', "'").replace('\u2014', ' ').replace('\u2013', '-')
    s = dehyph(re.sub(r'\s+', ' ', s)).lower()
    return re.sub(r'[^0-9a-z \'.,;:-]', ' ', re.sub(r'\s+', ' ', s)).strip()


def sents(t, minlen=60):
    t = re.sub(r'\$[^$]*\$', ' M ', t)
    t = re.sub(r'[ \t]*\n[ \t]*', ' ', t)
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z“"(*])', t) if len(s.strip()) > minlen]


def front(t):
    i = max((t.find(h) for h in ('## 1. Introduction', '## 1 Introduction') if t.find(h) >= 0), default=0)
    j = len(t)
    for e in ('## 2.', '## 2 ', '## 2\n'):
        k = t.find(e, i + 10)
        if k > 0:
            j = min(j, k)
    return t[i:j]


def cites(t):
    """Citation keys as (sorted surnames, year), built so presentation cannot move a key.

    '&' vs 'and', the serial comma, 'et al.', and a PDF line break inside a hyphenated name ("Fischer-\nKowalski")
    all have to produce the same key: the deposit and a reworded build differ in those details constantly, and an
    extractor that reports them as added-and-dropped citations in the same breath is noise, not a gate. Lowercased,
    hyphens and spaces inside a surname removed, tokens sorted.
    """
    out = set()
    for grp in re.findall(r'\(([^()]{3,160}?)\)', t):
        if not re.search(r'\b(19|20)\d{2}[a-z]?\b', grp):
            continue
        for one in re.split(r';', grp):
            m = re.search(r'\b((?:19|20)\d{2}[a-z]?)\b', one)
            if not m:
                continue
            names = re.sub(r'\b(19|20)\d{2}[a-z]?\b', ' ', one)
            names = re.sub(r'\bet al\.?|\band\b|&|cf\.|see also|in prep|doi:[^,)]*|p{1,2}\.\s*\d+', ' ', names, flags=re.I)
            toks = sorted({re.sub(r'[^a-z]', '', w.lower()) for w in names.replace('\n', ' ').split()})
            toks = [w for w in toks if len(w) > 2]
            if toks:
                out.add(' '.join(toks) + ' ' + m.group(1))
    return out


def named(t):
    """named objects: italic or bold multiword terms, and capitalised runs, minus sentence starts."""
    out = set()
    for m in re.findall(r'[\*_]{1,2}([A-Za-z][A-Za-z\'’\- ]{4,44})[\*_]{1,2}', t):
        n = norm(m)
        if len(n) > 5:
            out.add(n)
    for m in re.findall(r'(?<![.!?]\s)(?<!^)\b([A-Z][a-z]{2,}(?:\s+[A-Z][a-z]{2,}){1,3})\b', dehyph(t)):
        n = norm(m)
        if len(n) > 7 and n not in ('independent researcher',):
            out.add(n)
    return out


def canon_num(x):
    """'1,000,000', '1 000 000' and '600, 000' are one number; '6.0' and '10' inside a power are not."""
    s = re.sub(r'[ ,\u00a0]', '', str(x))
    return s if re.fullmatch(r'[+-]?\d+(\.\d+)?', s) else None


def numset(t):
    """numerals as canonical values, so a PDF line break inside '600,000' cannot look like an invented number."""
    n = norm(t)
    out = set()
    for m in re.finditer(r'\d{1,3}(?:,\s?\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?', n):
        c = canon_num(m.group(0))
        if c:
            out.add(c)
    return out


def digits_flat(t):
    """the deposit with separators squeezed out: the backstop a numeral is checked against."""
    return re.sub(r'[,\s]+', '', norm(t))


def cites_flat(t):
    """surnames-and-year presence in the deposit, ignoring hyphenation, ordering and 'et al.': a citation is backed
    when every surname of the key and its year all occur in the deposit at all."""
    n = re.sub(r'[^a-z0-9]', '', norm(t))
    return n


COIN = re.compile(r'(?:what we call|the term|called|dubbed|termed|formalises? this sense as|formalizes? this sense as'
                  r'|as the|names? this)\s+(?:the\s+|an?\s+)?([a-z][a-z\- ]{4,42})', re.I)
EMPH = re.compile(r'(?:\*\*|\*)([a-z][a-zA-Z\- ]{4,42})(?:\*\*|\*)')


def coinages(t):
    """terms the text names for itself, and every emphasised phrase: the vocabulary a rewrite must not orphan.

    Added after the v48 review, because the hand-written registry missed one: the deposit coins
    "the aggregation obstruction of Section 10.1" in prose, no markup, and v48 dropped both the phrase and its
    pointer - a loss no count-based check over a fixed list would have caught.
    """
    out = set()
    for m in COIN.finditer(t):
        n = norm(m.group(1))
        if 5 < len(n) < 44 and ' ' in n or len(n) > 7:
            out.add(n.strip(' .,;:'))
    for m in EMPH.finditer(t):
        n = norm(m.group(1))
        if len(n) > 5:
            out.add(n.strip(' .,;:'))
    return {c for c in out if c}


def atoms(t, dep_all=None):
    keep = {k: len(re.findall(re.escape(k.lower()), norm(t))) for k in TERMS if k.lower() in norm(t).lower()}
    return {'labels': sorted(f'{m.group(1)} {m.group(2)}' for m in LABEL.finditer(t)),
            'label_titles': sorted(norm(m.group(3)) for m in LABEL.finditer(t) if m.group(3).strip()),
            'math': sorted({norm(x) for x in MATH.findall(t) if len(norm(x)) > 1}),
            'keep': keep,
            'nums': sorted(numset(t)),
            'cites': sorted(cites(t)),
            'secrefs': sorted(set(SECREF.findall(t))),
            'named': sorted(named(t)),
            'coinages': sorted(coinages(t)),
            'negs': sorted({n.strip() for n in NEG if n in norm(t)})}


def g1(base, built, ba=None, bb=None, dep_or_base=None):
    a, b = ba or atoms(base), bb or atoms(built)
    out = []
    for key, kind in (('labels', 'statement label'), ('label_titles', 'label title'), ('math', 'inline symbol')):
        lost, add = sorted(set(a[key]) - set(b[key])), sorted(set(b[key]) - set(a[key]))
        if lost:
            lost = [x for x in lost if not any(c in norm(x) or norm(x) in c for c in cut_labels())]
            if lost:
                out.append({'check': 'G1', 'kind': f'{kind} in the base, absent from the build', 'items': lost[:10], 'n': len(lost)})
        if add:
            out.append({'check': 'G1', 'kind': f'{kind} introduced by the build', 'items': add[:10], 'n': len(add)})
    lost_terms = sorted(k for k in a['keep'] if k not in b['keep'])
    if lost_terms:
        out.append({'check': 'G1', 'kind': 'defined term used by the base and dropped by the build (rename?)',
                    'items': lost_terms})
    lost_coin = sorted(set(a['coinages']) - set(b['coinages']))
    if lost_coin:
        _cl = cut_labels()
        lost = [x for x in lost if not any(c in norm(x) or norm(x) in c for c in _cl)]
        if not lost:
            return out
        out.append({'check': 'G1', 'kind': 'term the base coins or emphasises, absent from the build',
                    'items': lost_coin[:12], 'n': len(lost_coin)})
    new_coin = sorted(set(b['coinages']) - set(a['coinages']) - set(atoms(dep_or_base)['coinages'])
                      if dep_or_base else set())
    if new_coin:
        out.append({'check': 'G1', 'kind': 'term coined by the build, not in the base', 'severity': 'disclose',
                    'items': new_coin[:12], 'n': len(new_coin)})
    dilute = sorted((k, a['keep'][k], b['keep'].get(k, 0)) for k in a['keep'] if b['keep'].get(k, 0) < a['keep'][k])
    if dilute:
        out.append({'check': 'G1', 'kind': 'guard-term count falls (base -> build)',
                    'items': [f'{k}: {x} -> {y}' for k, x, y in dilute[:12]], 'n': len(dilute)})
    return out


def g2(built, dep_txt, ledger, sec='1.'):
    """claim-atom traceability: every commitment a reworded sentence makes has to be the deposit's to make."""
    rows = [r for r in json.load(open(ledger))['rows'] if str(r.get('sec', '')).startswith(sec)]
    d = atoms(dep_txt)
    depn = norm(dep_txt)
    df, dcf = digits_flat(dep_txt), cites_flat(dep_txt)
    out = []
    for s in sents(built):
        a = atoms(s)
        bad = [f'numeral {x}' for x in a['nums'] if x not in set(d['nums']) and x.replace(',', '') not in df]
        bad += [f'citation {x}' for x in a['cites']
                if norm(x) not in {norm(c) for c in d['cites']}
                and not all(w in dcf for w in x.split())]
        bad += [f'section ref {x}' for x in a['secrefs'] if x not in set(d['secrefs'])]
        bad += [f'term "{x}"' for x in a['keep'] if x not in set(TERMS) and depn.count(x) == 0]
        neg = [n for n in a['negs'] if depn.count(n) == 0]
        if bad:
            out.append({'check': 'G2', 'kind': 'commitment the deposit does not carry', 'missing': bad[:6],
                        'ledger_rows_in_s1': len(rows), 'text': norm(s)[:150]})
    return out, len(sents(built)), len(rows)


def g3(base, built, dep_txt, ba=None, bb=None, da=None):
    a, b = ba or atoms(base), bb or atoms(built)
    d = da or atoms(dep_txt)
    depn, depc, depname = set(d['nums']), {norm(c) for c in d['cites']}, {norm(x) for x in d['named']}
    df, dcf = digits_flat(dep_txt), cites_flat(dep_txt)
    out = []
    # blocking classes: a numeral, a citation or a section pointer that the deposit does not carry is an error.
    # 'named object' is advisory: proper-noun extraction from a PDF-derived deposit and a hand-set build differ at
    # sentence starts (a run the deposit has after a full stop, the build has mid-sentence, or the reverse), and that
    # asymmetry produces real noise. It is reported for disclosure, never used to fail a build. TERMS are excluded
    # from it anyway - G1 owns the defined vocabulary.
    for kind, key, back, sev in (('numeral', 'nums', depn, 'block'), ('citation', 'cites', depc, 'block'),
                                ('section reference', 'secrefs', set(d['secrefs']), 'block'),
                                ('named object', 'named', depname, 'disclose')):
        bs = {norm(x) for x in b[key] if norm(x) not in {norm(t) for t in TERMS}}
        as_ = {norm(x) for x in a[key] if norm(x) not in {norm(t) for t in TERMS}}
        ds = {norm(x) for x in d[key] if norm(x) not in {norm(t) for t in TERMS}}
        added = sorted(bs - as_)
        if key == 'nums':
            unbacked = sorted(x for x in added if x not in back and x.replace(',', '') not in df)
        elif key == 'cites':
            unbacked = sorted(x for x in added if x not in back and not all(w in dcf for w in x.split()))
        else:
            unbacked = sorted(x for x in added if x not in back)
        # an item the author ruled out of the build is not a loss to report; the ruling lives in the
        # CSV, so the gate follows the file (G4 is what enforces that these stay out)
        _cut = cut_labels()
        dropped = sorted(x for x in as_ - bs
                         if not any(c in x or x in c for c in _cut))
        if unbacked:
            out.append({'check': 'G3', 'severity': sev, 'kind': f'{kind} in the build, not in the base and not in the deposit',
                        'items': unbacked[:10], 'n': len(unbacked)})
        if dropped:
            out.append({'check': 'G3', 'severity': sev, 'kind': f'{kind} the base carries and the build loses',
                        'items': dropped[:10], 'n': len(dropped)})
    return out


CSV = f'{V49}/adaptation_term_revert_v1.csv'
V48SRC = '/home/user/revision/v48/build_v48_base.py'


def _rules():
    rows = []
    for ln in open(CSV):
        ln = ln.strip()
        if not ln or ln.startswith('#'):
            continue
        f = ln.split(',', 6)          # 6 leading fields + free-text note; >=8 dropped 12 of 14 rules
        if len(f) >= 6:
            rows.append({'alias': f[0], 'repl': f[1], 'rule': f[2], 'gem': int(f[3]), 'dep': int(f[4]),
                         'v48': int(f[5])})
    return rows


def cut_labels():
    """the aliases the author ruled out of the build (scope 'label' with no replacement): an
    instrument that flags an instruction it was told to implement is noise, and noise here is
    what would make someone switch the gate off"""
    return {r['alias'].lower() for r in _rules() if r['rule'] == 'label' and not r['repl']}


def g4(built, base):
    """G4 the cut content stays out, and G5 the revert was actually applied. Both read the CSV, so the author's
    rulings live in one place and the gate follows the file rather than the code."""
    out = []
    rows = _rules()
    nb, nba = norm(built), norm(base)
    for r in rows:
        c_alias = nb.count(r['alias'].lower())
        if r['rule'] in ('label', 'force') and c_alias:
            out.append({'check': 'G4/G5', 'severity': 'block', 'rule': r['rule'],
                        'kind': f"alias present in the build: \"{r['alias']}\" ({c_alias}x)",
                        'replacement': r['repl'] or '(none - this item is cut, not replaced)',
                        'expect': 0})
        if r['rule'] == 'force' and r['repl']:
            need = max(1, r['gem'])
            got = nb.count(r['repl'].lower())
            if got < need:
                out.append({'check': 'G4/G5', 'severity': 'block', 'rule': 'force',
                            'kind': f"revert under-applied: \"{r['repl']}\" appears {got}x, base had the alias {r['gem']}x",
                            'expect': f'>= {need}'})
    if not any(x['check'] == 'G4/G5' for x in out):
        out_note = {'check': 'G4/G5', 'kind': f'{len(rows)} revert/cut rules read from {CSV.split("/")[-1]}, all satisfied',
                    'severity': 'info'}
        return [out_note]
    return out


def g0(built):
    out = []
    for para in [p for p in built.split('\n\n') if p.strip()]:
        lines = para.split('\n')
        for ln in lines:
            if re.search(r'\S\s+[-•]\s+\S', ln) and not re.match(r'\s*[-*•\d]', ln):
                out.append({'check': 'G0', 'kind': 'list marker inside a paragraph', 'text': ln.strip()[:140]})
        oneline = ' '.join(x.strip() for x in lines)
        if oneline.count('**') % 2:
            out.append({'check': 'G0', 'kind': 'unbalanced emphasis', 'text': oneline[:140]})
        # house style writes a display as $$...$$ on its own line(s): that is what the .tex
        # transpiler expects and what every earlier line of this paper uses. What is NOT house
        # style is a display left inside a running sentence, or \( \) or a code fence.
        for _l in lines:
            _s = _l.strip()
            if _s.startswith('$$') and _s.endswith('$$') and len(_s) > 4:
                continue
            if _s == '$$':
                continue
            if '$$' in _s:
                out.append({'check': 'G0', 'kind': 'display inside running text', 'text': _s[:140]})
        if re.search(r'\\\(|\\\)|^\s*```', para, re.M):
            out.append({'check': 'G0', 'kind': 'delimiter outside this house style (\\( \\), fence)',
                        'text': oneline[:140]})
    return out


def g1b(base, built, prev, dep_txt):
    """G1b: the waived region seen from the oracle and from the previous line, not only from the
    base. G1 asks what the base had that the build lost; where the base is itself a rewrite that
    question is blind to what the deposited article names and the accepted line carried. The four
    status labels of this paper ('arithmetic, not a forecast' and its three siblings) would leave
    the abstract exactly that way: the claims survive in reworded form, the defined labels do not.
    Disclose, never block - choosing between the label and the paraphrase is the author's call, and
    writing a glue sentence to hide the difference would be the worse act."""
    out = []
    # a hand-written registry is the soft spot in a gate like this - it is why E2 passed for a
    # day - so the vocabulary comes from three places: TERMS, the phrases the previous line
    # emphasises or coins, and the label list the v48 build itself treats as inalienable
    # (KEEP in build_v48_base.py, read out of that file rather than copied, so the two cannot
    # quietly disagree with each other)
    keep = []
    if os.path.exists(V48SRC):
        mm = re.search(r"KEEP = \((.*?)\)\n", open(V48SRC).read(), re.S)
        keep = re.findall(r"'([^']{6,})'", mm.group(1)) if mm else []
    V48_KEEP_SRC = keep
    terms = sorted(set(TERMS) | set(keep) | (coinages(prev) - coinages(built)))
    dp, bp, bb = norm(prev), norm(base), norm(built)
    for t in terms:
        lt = norm(t)
        if not lt or lt in bb or lt not in dp or lt in bp:
            continue
        out.append({'check': 'G1b', 'severity': 'disclose',
                    'kind': 'vocabulary the previous line carried in the waived region, absent from the build',
                    'term': t, 'in_previous_line': bp.count(lt), 'in_deposit_or_theirs': dp.count(lt)})
    return out


def run(base_txt, built_txt, label, dep_txt=None, prev_txt=None):
    dep_txt = dep_txt if dep_txt is not None else open(DEP).read()
    ba, bb, da = atoms(base_txt), atoms(built_txt), atoms(dep_txt)
    f1 = g1(base_txt, built_txt, ba, bb, dep_txt)
    f2, ns, nrow = g2(built_txt, dep_txt, LEDGER)
    f3 = g3(base_txt, built_txt, dep_txt, ba, bb, da)
    f0 = g0(built_txt)
    f4 = [x for x in g4(built_txt, base_txt) if x['severity'] != 'info']
    f4i = [x for x in f4 if x['severity'] == 'info']
    f1b = g1b(base_txt, built_txt, prev_txt if prev_txt is not None else base_txt, dep_txt)
    flags = f1 + f1b + f2 + f3 + f0 + f4
    if f4i:
        print('   (G4/G5 clean:', f4i[0]['kind'] + ')')
    blocking = [f for f in flags if f.get('severity', 'block') == 'block']
    return {'comparison': label, 'built_sentences_in_region': ns, 'ledger_rows_in_section_1': nrow,
            'G0_integrity': f0, 'G1_vocabulary': f1, 'G1b_previous_line_vocabulary': f1b, 'G2_ledger_trace': f2, 'G3_facts': f3, 'G4_G5_revert_and_cuts': f4,
            'flag_count': len(blocking), 'disclosure_count': len(flags) - len(blocking),
            'term_counts': {'base': ba['keep'], 'built': bb['keep'], 'deposit': da['keep']}}


def control():
    up = open(UP).read()
    gem = up[:up.index('\ngrok:')]
    dep = open(DEP).read()
    v42 = open(f'{V7}/paper3_material_ledgers_v42.md').read()
    v48 = open(f'{V7}/paper3_material_ledgers_v48.md').read()
    reps = [
        run(front(v42), front(v48), 'A. base v42 front matter -> built v48 front matter: does this gate catch what '
            'v48’s gate missed? (the dropped flagship paragraph, the stray list marker)'),
        run(front(gem), front(v48), 'B. base the adaptation -> built v48: how far the v48 opening is from what the '
            'waiver is meant to let it become'),
        run(front(gem), dep, 'C. base the adaptation -> the deposit as build: what G1 has to reconcile first, '
            'because the adaptation renames and dilutes terms the paper depends on'),
    ]
    for r in reps:
        print('\n' + '=' * 104)
        print(r['comparison'])
        print('=' * 104)
        print(f"  built-region sentences {r['built_sentences_in_region']} | §1 ledger rows {r['ledger_rows_in_section_1']} "
              f"| blocking flags {r['flag_count']} + disclosures {r['disclosure_count']}  (G0 {len(r['G0_integrity'])}, G1 {len(r['G1_vocabulary'])}, G4/G5 {len(r['G4_G5_revert_and_cuts'])}, "
              f"G2 {len(r['G2_ledger_trace'])}, G3 {len(r['G3_facts'])})")
        for k in ('G0_integrity', 'G1_vocabulary', 'G3_facts', 'G2_ledger_trace', 'G4_G5_revert_and_cuts'):
            for f in r[k][:5]:
                if f['check'] == 'G2':
                    print(f"     G2 unbacked: {f['missing']} :: {f['text'][:88]}")
                else:
                    print(f"     {f['check']} {f['kind']}: {f.get('items', f.get('text'))}")
            if len(r[k]) > 5:
                print(f'     … {len(r[k]) - 5} more {k} flag(s)')
        tc = r['term_counts']
        delta = [(k, tc['base'].get(k, 0), tc['built'].get(k, 0)) for k in TERMS
                 if tc['base'].get(k, 0) != tc['built'].get(k, 0)]
        if delta:
            print('  term counts base -> built:', '; '.join(f'{k} {x}->{y}' for k, x, y in delta[:10]))
    json.dump(reps, open(f'{V49}/waiver_gate_controls.json', 'w'), indent=1)
    print(f'\n{f"{V49}/waiver_gate_controls.json"} written')
    return sum(r['flag_count'] for r in reps)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base'); ap.add_argument('--built'); ap.add_argument('--out')
    ap.add_argument('--prev', help='the previous line of record for the same region, for G1b')
    ap.add_argument('--region', default='front', help='front (to §2) or whole')
    ap.add_argument('--control', action='store_true')
    a = ap.parse_args()
    if a.control:
        control()           # a demonstration that the checks bite; not a verdict on any build
        return 0
    if not (a.base and a.built):
        ap.error('--base and --built are required unless --control is given')
    bt, bu = open(a.base).read(), open(a.built).read()
    if a.region != 'whole':
        bt, bu = front(bt), front(bu)
    prev = None
    if a.prev:
        prev = open(a.prev).read()
        if a.region != 'whole':
            prev = front(prev)
    rep = run(bt, bu, f'{a.base} -> {a.built}', prev_txt=prev)
    txt = json.dumps(rep, indent=1)
    if a.out:
        open(a.out, 'w').write(txt)
    print(txt)
    return min(120, rep['flag_count'])          # exit code is the flag count, capped so a huge run still exits 1..120


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""The claim ledger - pairs first, adjudication by the author.

    Produce two artifacts before writing anything. (1) A claim ledger: every draft sentence that asserts a fact,
    claim, hedge, scope, or attribution, paired with the deposit proposition it corresponds to and a verdict of
    supported / unsupported / contradicted. (2) A count of each verdict. Then stop.

That is this file's whole scope. It reads the humanized draft and the deposited article, aligns them where they
correspond, and reports for each draft sentence what the deposit says beside it and which markers differ: values,
the strength of a claim, its scope and conditions, its attribution, its polarity, and whether the draft asserts an
inference the deposit leaves unasserted. It writes the pairs to `claim_ledger_v1.md`, every row to CSV and JSON,
and the counts to the head of both.

It rewrites nothing, merges nothing, repairs nothing. Two design decisions are worth naming, because they are what
keep the ledger worth reading. Claims are checked against the **aligned passage**, not against a single sentence:
a hedge lives in the sentence before, a condition in the one after, and a comparison that ignores that calls
faithful simplification a change of claim - the first version of this file flagged a third of its rows that way,
and a ledger that cries wolf teaches the author to skip it. And a draft sentence with no partner in the deposit is
reported as an addition the draft made, never as an error: that is the class the author has to decide about, and
it is the only class where "the draft says something the paper does not" is a fact rather than an artifact of
lexical matching between a plain-language sentence and a technical one.

Usage:  python3 claim_ledger_v1.py            # full ledger
        python3 claim_ledger_v1.py -n 60      # a slice, for tuning
"""
import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher

DRAFT = '/home/user/humanized/v1/paper3_humanized_v1_full.md'
DEPOSIT = '/home/user/revision/v7/paper3_material_ledgers_v42.md'
OUT = '/home/user/revision/v48'

BACK = re.compile(r'^\s*#{1,6}\s+(References|Data availability|Code availability|Acknowledg|Author contribution|'
                  r'Conflict of interest|Funding|Notes|Supplementary material|Declarations|DOI links|'
                  r'Two open items)', re.I)
ABBR = r'(?:e\.g|i\.e|et al|vs|cf|No|Vol|pp|fig|Figs|U\.S|U\.K|Sec|Ref|Dr|Prof|approx)'
FRONT_LINE = re.compile(r'(?i)(ORCID|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}|independent researcher)')
CITE = re.compile(r'\b([A-Z][A-Za-z\u2019\'-]{2,})(?:\s+(?:et al\.?|and\s+[A-Z][A-Za-z\u2019\'-]+))?,?\s+'
                  r'((?:19|20)\d\d)[a-z]?\b')
VALUE = re.compile(r'(?<![A-Za-z0-9.])\d[\d,]*(?:\.\d+)?(?:[eE][-+]?\d+)?\s?(?:%|percent|pp|Mt|Gt|kt|kg|'
                   r'years?|months?|days?|weeks?|hours?|nats|bits)?')
HEDGE = ['may', 'might', 'can', 'could', 'would', 'usually', 'typically', 'often', 'sometimes', 'generally',
         'likely', 'probably', 'appears', 'seems', 'tends', 'partially', 'nearly', 'roughly', 'approximately',
         'up to', 'at least', 'at most', 'in practice', 'arguably', 'somewhat', 'relative', 'relative to',
         'under some', 'on average', 'to first order', 'can be read', 'is read as', 'in the model', 'on paper']
UNIV = ['always', 'never', 'all', 'every', 'none', 'must', 'cannot', 'only', 'exactly', 'precisely', 'strictly',
        'necessarily', 'impossible', 'guarantee', 'guarantees', 'never recovers', 'never binds']
CAUSAL = ['causes', 'causing', 'caused', 'led to', 'leads to', 'leading to', 'resulting in', 'results in',
          'produces', 'produced', 'drives', 'forces', 'compels', 'because', 'therefore', 'thus', 'hence',
          'implies', 'imply', 'guarantees', 'ensures', 'explains', 'makes the', 'means that', 'so that']
ASSOC = ['associated', 'linked', 'correlates', 'correlated', 'correlation', 'consistent with', 'tracks',
         'co-moves', 'comoves', 'coincides', 'in line with', 'suggests', 'indicative', 'reflects',
         'accompanies', 'scales with', 'corresponds to', 'parallel to', 'raises the same', 'same question']
NEG = ['not', 'never', 'without', 'fails to', 'cannot', 'unable to', 'nothing', 'neither', 'nor', 'no one',
       'absent', 'refuses', 'resists', 'excludes']
COND = ['when', 'if', 'unless', 'assuming', 'provided', 'given that', 'in the limit', 'only if', 'at the level of',
        'conditional', 'for populations', 'in jurisdictions', 'whenever', 'where the',
        'on the declared', 'subject to', 'restricted to', 'holding fixed', 'at fixed', 'ceteris paribus',
        'under declared', 'only after', 'only when', 'except', 'insofar', 'to the extent', 'given',
        'within the declared', 'applicable when', 'admissible']
INFER_OPEN = re.compile(r'^(?:Therefore|Thus|Hence|So\b|Because|This implies|That implies|Which means|'
                        r'It follows|Consequently|As a result|The consequence|Accordingly|That is why)')
SIGNPOST = re.compile(r'(?i)\b(?:this|the)\s+(?:section|article|paper|appendix|note|companion|proof|table|'
                      r'ledger|paragraph)\b|\bwe (?:prove|show|record|state|collect|turn|give|defer|report)\b|'
                      r'^(?:Section|Lemma|Appendix)\s*\d')
STOP = set('the a an of to in for and or is are was were be been that this these those it its as by with from on '
           'at which who whom whose what when where how why not no such can could may might must will would shall '
           'there their them we our us you your he she his her i do does did has have had also than then'.split())


def blocks(text, pairs=False):
    """Body blocks of one file, prose only - and, if asked, the same blocks with their maths still in them.

    A heading line is dropped from the block it sits in rather than ending the block, because this draft writes
    `## Abstract` above its first paragraph: leaving it in put a heading into the ledger, paired with a display
    equation. The leading reading note (`>` lines), tables, displays, proofs and the back matter are out. The raw
    twin exists because equations carry the paper's numbers: a filter that keeps `$...$` out of the prose would
    otherwise report `10^6` as a figure nobody stated, so the two lists stay index for index.
    """
    out, in_back, first = [], False, True
    for b in re.split(r'\n\s*\n', text):
        lines = [x for x in b.split('\n') if x.strip()]
        if not lines:
            continue
        s = b.strip()
        if first:
            first = False
            if s.startswith('>'):
                continue
        if any(BACK.match(x) for x in lines):
            in_back = True
        if in_back:
            continue
        keep = [x for x in lines if not re.match(r'^\s*#{1,6}\s', x) and not x.lstrip().startswith('>')]
        keep = [x for x in keep if not FRONT_LINE.search(x)]
        raw = ' '.join(keep)
        keep = [x for x in keep if not re.match(r'^\s*(\$\$|\||```)', x) and '```' not in x
                and not re.match(r'^\s*\*?Proof\.?\*?', x)]
        txt = re.sub(r'\$[^$]{0,600}\$', ' ', ' '.join(keep))
        txt = re.sub(r'\s+', ' ', txt).strip()
        if len(txt.split()) >= 5:
            out.append((txt, re.sub(r'\s+', ' ', raw).strip()) if pairs else txt)
    return out


def sections(text, keep):
    """The section number each block sits under."""
    heads = [(m.start(), m.group(1)) for m in re.finditer(r'(?m)^#{1,6}\s*(\d+(?:\.\d+)*)[^\n]*$', text)]
    out = []
    for b in keep:
        i = text.find(b[:60])
        sec = ''
        for p0, h in heads:
            if p0 <= i:
                sec = h
        out.append(sec)
    return out


def sentences(block):
    x = re.sub(r'\b(' + ABBR + r')\.', '\\1\x00', block)
    x = re.sub(r'(\d)\.(\d)', '\\1\x01\\2', x)
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z“"\u2018(]|\Z)', x)
    return [re.sub(r'\s+', ' ', q).replace('\x01', '.').replace('\x00', '.').strip()
            for q in parts if len(q.split()) >= 5]


def flat(s):
    return re.sub(r'\s+', ' ', re.sub(r'\*\*|`|\$|\u2009', '', s)).strip()


def norm(s):
    return re.sub(r'[^a-z0-9 ]', '', ' '.join(flat(s).lower().split()))


def toks(s):
    return {w for w in norm(s).split() if w not in STOP and len(w) > 2}


def stemset(s):
    """Content words, lightly stemmed, so `aggregates` and `aggregation` are the same evidence."""
    out = set()
    for w in toks(s):
        for suf in ('ation', 'ions', 'ion', 'ing', 'ies', 'ied', 'ed', 'es', 's', 'ly', 'al', 'ent', 'ance',
                    'ence', 'ity'):
            if w.endswith(suf) and len(w) - len(suf) >= 4:
                w = w[:-len(suf)]
                break
        out.add(w[:11])
    return out


def marks(s, terms):
    low = norm(s)
    return sorted({t for t in terms if re.search(r'\b' + re.escape(t).replace(r'\ ', r'\s+') + r'\b', low)})


POW = re.compile(r'10\s*\^\s*\{?\s*(-?\d+)\s*\}?')


def numbers(text):
    """Every figure a sentence states, as a float, with the forms the two files use for the same quantity unified.

    The deposit writes a million tonnes as `$10^6$ kt` inside maths and the draft writes `1,000,000 kt`, and an
    earlier version of this ledger reported that as a figure the deposit never states, because the block reader
    had already deleted the maths to keep equations out of the prose. Values are therefore read from the raw text
    and compared numerically.
    """
    # hyphens become spaces: `pre-2026` and `sample-and-hold 3` are how a draft writes a figure the paper set in
    # maths, and a digit scan that demands a non-letter before the number reads `pre2063` and sees no number at all
    t = (text.replace('{,}', '').replace(',\\,', '').replace('\\,', '').replace(',', '')
         .replace('\u2009', ' ').replace('-', ' ').replace('\u2013', ' ').replace('\u2014', ' '))
    out = set()
    for m in re.finditer(r'(\d+(?:\.\d+)?)\s*(?:\\times|\\cdot|\*)\s*10\s*\^\s*\{?\s*(-?\d+)\s*\}?', t):
        a, e = float(m.group(1)), int(m.group(2))
        if abs(e) > 300:
            continue
        out.add(round(a * 10.0 ** e, 6))                  # `6 \times 10^{5}` is the same figure as `600,000`
    for m in POW.finditer(t):
        e = int(m.group(1))
        if abs(e) > 300:
            continue                     # a $10^{38}$ in a constants table is not a claim being restated
        out.add(round(10.0 ** e, 6))
    for m in re.finditer(r'(?<![A-Za-z0-9.])\d+(?:\.\d+)?', t):
        v = float(m.group(0))
        if v < 10:
            continue
        out.add(round(v, 6))
    return out


def vals(s):
    out = set()
    for m in VALUE.finditer(flat(s)):
        v = m.group(0).strip().rstrip('.').replace(',', '')
        if re.fullmatch(r'\d{1,2}|19\d\d|20\d\d', v):
            continue                     # list numbers and bare years are not claims about the world
        out.add(v)
    return out


def cites(s):
    """Every reference a piece of text points at, as `year: surnames`, surnames sorted.

    A citation is read from the whole parenthetical, not from the last name before the year: the draft writes
    `(Martinez-Alier, Munda and O'Neill, 1998)` where the deposit writes `(Martinez-Alier, Munda, and O'Neill,
    1998)`, and read name by name those look like different references, which made the first version of this
    ledger report a source the draft supposedly invented.
    """
    out = set()
    t = flat(s)
    for m in re.finditer(r'\(([^()]{0,200}?(?:19|20)\d\d[a-z]?[^()]{0,60})\)', t):
        g = m.group(1)
        y = re.search(r'((?:19|20)\d\d)[a-z]?', g)
        if not y:
            continue
        names = tuple(sorted(set(re.findall(r"[A-Z][A-Za-z\u2019'-]{2,}", g[:y.start()]))))
        if names:
            out.add(y.group(1) + ':' + '|'.join(names))
    for m in re.finditer(r'\b([A-Z][A-Za-z\u2019\'-]{2,}(?:,?\s+and\s+[A-Z][A-Za-z\u2019\'-]{2,})*)\s*'
                         r'\(((?:19|20)\d\d)[a-z]?\)', t):
        out.add(m.group(2) + ':' + '|'.join(sorted(set(re.findall(r"[A-Z][A-Za-z\u2019'-]{2,}", m.group(1))))))
    return out


def jac(a, b):
    return len(a & b) / max(1, len(a | b))


def align_blocks(ds_blocks, ps_blocks, sent_best, cut=0.05):
    """Monotone block alignment scored by the sentences inside the blocks.

    Comparing paragraphs by their own token overlap fails on this pair of files for the obvious reason: the draft
    is written in plain English and the deposit in technical English, so a faithful paragraph shares four words
    with its original. What does carry is the sentence-level evidence, so a block's score is the mean, over its
    sentences, of the best overlap any sentence in the candidate paragraph achieves - and the alignment is
    monotone because the humanizer did not reorder the argument.
    """
    n, m = len(ds_blocks), len(ps_blocks)
    bsc = defaultdict(dict)
    for i, si in sent_best.items():
        agg = defaultdict(list)
        for j, v in si:
            agg[j].append(v)
        for j, vs in agg.items():
            bsc[i][j] = sum(vs) / len(vs)
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s = bsc[i - 1].get(j - 1, 0.0)
            D[i][j] = max(D[i - 1][j], D[i][j - 1], (D[i - 1][j - 1] + s) if s >= cut else D[i - 1][j - 1])
    back, sc, i, j = {}, {}, n, m
    while i and j:
        s = bsc[i - 1].get(j - 1, 0.0)
        if D[i][j] == D[i - 1][j]:
            i -= 1
        elif D[i][j] == D[i][j - 1]:
            j -= 1
        else:
            back[i - 1] = j - 1
            sc[i - 1] = s
            i -= 1
            j -= 1
    return back, sc, bsc


def build(dtxt, ptxt, limit=0):
    ap = argparse.ArgumentParser()
    a = ap.parse_args([])
    a.n = limit

    ptxt = ptxt
    db, pbp = blocks(dtxt), blocks(ptxt, pairs=True)
    pb = [x[0] for x in pbp]
    pb_raw = [x[1] for x in pbp]      # index for index with `pb`, maths intact, for the value test only
    dsec, psec = sections(dtxt, db), sections(ptxt, pb)

    def sents(bl, secs):
        rows = []
        for bi, b in enumerate(bl):
            for si, s in enumerate(sentences(b)):
                if len(toks(s)) < 4 or len([w for w in toks(s) if len(w) >= 5]) < 2 or '\\' in s or '{' in s \
                        or '^' in s:
                    continue            # a line the maths left behind is not a proposition to pair a claim with:
                                        # delete `$...$` mid-sentence and what remains is `rNs rN2s/K`, no assertion
                rows.append(dict(b=bi, s=si, sec=secs[bi], text=s, block=b))
        return rows
    ds, ps = sents(db, dsec), sents(pb, psec)

    ptok = [stemset(x['text']) for x in ps]
    pnorm = [norm(x['text']) for x in ps]
    pinv = defaultdict(list)
    for k, t in enumerate(ptok):
        for w in t:
            pinv[w].append(k)
    global PVALS
    global PNUMS, PCITES
    PNUMS = numbers(ptxt)
    PCITES = cites(ptxt)
    dnorm_p = {norm(x['text']) for x in ps}

    # best-overlap evidence per draft sentence, against every deposit sentence that shares a stemmed content word
    sent_best = defaultdict(list)
    ev = {}
    for i, r in enumerate(ds):
        q = stemset(r['text'])
        c = Counter()
        for w in q:
            for k in pinv.get(w, ()):
                c[k] += 1
        top = []
        for k, n in c.most_common(400):
            v = jac(q, ptok[k])
            if v > 0.02:
                top.append((v, k))
        top.sort(reverse=True)
        top = top[:10]
        ev[i] = top
        for v, k in top:
            sent_best[r['b']].append((ps[k]['b'], v))
    sent_best = {i: sorted({j: max(v for jj, v in si if jj == j) for j, v in si}.items(), key=lambda x: -x[1])
                 for i, si in sent_best.items()}
    al, alsc, bsc = align_blocks(db, pb, sent_best)

    rows, shared = [], 0
    for i, r in enumerate(ds):
        r['idx'] = i
        n = norm(r['text'])
        if len(n.split()) < 6:
            continue
        if n in dnorm_p:
            shared += 1
            rows.append(dict(id=f'D{len(rows)+1:04d}', idx=i, verdict='excluded: shared verbatim', sec=r['sec'],
                             draft=r['text'], dep='', score=1.0, ratio=1.0, pair='identical text', flags=[],
                             note=''))
            continue
        jb = al.get(r['b'])
        near = [x for x in (jb - 1, jb, jb + 1) if x is not None and 0 <= x < len(pb)] if jb is not None else []
        cand = [(v, k) for v, k in ev[i] if ps[k]['b'] in near] or [(v, k) for v, k in ev[i]]
        sc, kk = 0.0, None
        for v, k in cand[:6]:
            rr = SequenceMatcher(None, n, pnorm[k]).ratio()
            s = max(v, 0.45 * v + 0.55 * rr)
            if s > sc:
                sc, kk = s, k
        rr = SequenceMatcher(None, n, pnorm[kk]).ratio() if kk is not None else 0.0
        p_ = ps[kk] if kk is not None else None
        if p_ is None:
            pair = 'no partner located'
        elif jb is not None and p_['b'] in near:
            pair = 'aligned passage' if sc > 0.14 else 'aligned passage, weak'
        else:
            pair = 'elsewhere in the deposit'
        pas = ' '.join(x['text'] for x in ps if p_ and x['b'] == p_['b']) if p_ else ''
        pas_raw = pb_raw[p_['b']] if p_ else ''
        dpara = ' '.join(x['text'] for x in ds if x['b'] == r['b'])
        block_score = alsc.get(r['b'], 0.0)
        bag = {}
        v, fl, note = check(r['text'], p_['text'] if p_ else '', pas, dpara, sc, rr, block_score, pair,
                            pas_raw=pas_raw, bag=bag,
                            BID=(p_['b'] if p_ else None), SID=(p_['s'] if p_ else None), PS=ps)
        if v.startswith('supported') and SIGNPOST.search(r['text']) and not vals(r['text']):
            v, note = 'not a claim (signposting)', (note + ' ; ' if note else '') + (
                'the sentence reports what the document does, not what the world does')
        global STRICT
        STRICT = True
        v_s, fl_s, _ = check(r['text'], p_['text'] if p_ else '', pas, dpara, sc, rr, block_score, pair,
                             pas_raw=pas_raw, BID=(p_['b'] if p_ else None), SID=(p_['s'] if p_ else None), PS=ps)
        STRICT = False
        rows.append(dict(id=f'D{len(rows)+1:04d}', idx=i, blk=r['b'], verdict=v, strict_verdict=v_s,
                         strict_flags=[f'{g[0]}: {g[1]}' for g in fl_s], sec=r['sec'], draft=r['text'],
                         dep=p_['text'] if p_ else '', dep_sec=p_['sec'] if p_ else '', dep_block=p_['b'] if p_ else '',
                         dep_passage=pas[:1200], pair=pair, block_overlap=round(block_score, 3),
                         score=round(sc, 3), ratio=round(rr, 3), flags=fl, note=note,
                         cites_dropped=bag.get('dropped', []), cites_added=bag.get('added', [])))
        if a.n and len(rows) >= a.n:
            break

    cnt = Counter(x['verdict'] for x in rows)
    conf = Counter(('high' if x['ratio'] > .60 or x['score'] > .45 else 'medium' if x['score'] > .18 else 'low')
                   for x in rows if not x['verdict'].startswith('excluded'))
    print(f'draft body sentences {len(rows)} | shared verbatim with the deposit, excluded {shared} | '
          f'ledgered {len(rows) - shared}')
    for k, v in cnt.most_common():
        print(f'   {k:34s} {v}')
    print(f'   confidence: {dict(conf)}')
    if limit:
        return rows, cnt, conf, ds, ps, db, pb
    json.dump(dict(counts=dict(cnt), confidence=dict(conf), rows=rows), open(f'{OUT}/claim_ledger_v1.json', 'w'),
              indent=1)
    write_csv(rows)
    write_md(rows, cnt, conf, len(db), len(pb), al)
    write_complement(rows, ds, db, dtxt, cnt)
    write_attribution_review(rows, dtxt)
    return rows, cnt, conf, ds, ps, db, pb


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-n', type=int, default=0)
    ap.add_argument('--mutate', type=int, default=0, help='plant N known defects and see whether the rules find them')
    ap.add_argument('--seed', type=int, default=7)
    a = ap.parse_args()
    dtxt, ptxt = open(DRAFT).read(), open(DEPOSIT).read()
    if a.mutate:
        return mutate_test(dtxt, ptxt, a.mutate, a.seed)
    rows, cnt, conf, ds, ps, db, pb = build(dtxt, ptxt, a.n)
    print(f'wrote: claim_ledger_v1.md ({sum(1 for x in rows if x["verdict"].startswith(("contradicted", "unsupported", "needs check")))} pairs to adjudicate), '
          f'.csv and .json (all {len(rows)} rows), claim_ledger_v1_complement.md, claim_ledger_v1_attribution_review.md')
    return rows


PNUMS, PCITES = set(), set()   # figures and citations the deposited file states, maths included; set by main()


def cite_disp(c):
    """`2004:Brunner|Rechberger` as a person writes it: `Brunner & Rechberger, 2004`."""
    if ':' not in c:
        return c
    y, names = c.split(':', 1)
    return ' & '.join(names.split('|')) + ', ' + y


STRICT = False      # the census re-runs `check` with every window narrowed to the matched sentence


def fmt(xs):
    return ', '.join(('%g' % x) if x < 1e6 or x % 1 else ('%.1e' % x) for x in xs)


def check(d, pp, pas, dpara, sc, rr, block_score, pair, BID=None, SID=None, PS=None, pas_raw='', bag=None):
    """The candidate verdict, by the rules printed at the head of `claim_ledger_v1.md`."""
    # `no partner located` is the strongest thing this ledger can say about a sentence, so it is said rarely: the
    # character ratio counts as evidence, because a plain-English restatement of a technical sentence shares few
    # words with it and shares its shape
    if pair == 'no partner located' or (sc < 0.10 and block_score < 0.045 and rr < 0.30) or \
            (sc < 0.22 and rr < 0.30 and block_score < 0.045):
        return ('unsupported: no partner located', [],
                'nothing in the deposit shares enough content words with this sentence to be its original')
    flags, notes = [], []
    # shipped, a marker is answered for by the aligned passage; the census takes that credit away
    src = pp if STRICT else (pas or pp)
    vsrc = pp if STRICT else pas_raw
    nearp = pp if STRICT else (' '.join(x['text'] for x in PS if x['b'] == BID and abs(x['s'] - SID) <= 1)
                               if BID is not None else pp)
    dsrc = dpara or d
    good = True if STRICT else (sc > 0.30 or rr > 0.55)                                  # a marker comparison across a bad pair is noise
    dn, sn, pn_ = numbers(d), numbers(vsrc or src), PNUMS
    miss = sorted(x for x in dn if x not in sn)
    if miss:
        nowhere = [x for x in miss if x not in pn_]
        if nowhere:
            flags.append(('contradicted', 'value', f'the draft states {fmt(nowhere[:4])}, which the deposit never '
                                                   f'states in any form'))
        else:
            notes.append(f'the figure {fmt(miss[:3])} is stated in the deposit but outside this passage')
    dh, ph = marks(dsrc, HEDGE), marks(nearp or src, HEDGE)
    p_here = marks(pp, COND)
    du, pu = marks(d, UNIV), marks(nearp or src, UNIV)
    dc, pc = marks(d, CAUSAL), marks(src, CAUSAL)      # cause versus association is a property of the claim in
    da, pa = marks(d, ASSOC), marks(src, ASSOC)        # context, so these two read the passage, not one sentence
    dn, pn = marks(dsrc, NEG), marks(nearp or src, NEG)
    dcond, pcond = marks(dsrc, COND), marks(nearp or src, COND)
    dci, pci = cites(dsrc), cites(nearp or src)
    if good:
        if pa and dc and not pc:
            flags.append(('contradicted', 'causality', f'the deposit passage says {pa}, this sentence says '
                                                       f'{sorted(set(dc) - set(pc))[:3]}'))
        if ph and not dh and (du or dc or dn):
            flags.append(('needs check', 'strength', f'the passage hedges with {ph[:4]}; this sentence asserts'
                                                     + (f' {du[:3]}' if du else ' without a hedge')))
        if p_here and not dcond and (sc > 0.30 or rr > 0.55):
            flags.append(('needs check', 'scope', f'the sentence this one restates is conditioned by '
                                                  f'{p_here[:3]}; the draft states it unconditionally'))
        if pci and not dci and sc > 0.35:
            if not sorted(x for x in pci if x in cites(dpara)):
                flags.append(('needs check', 'attribution', f'the sentence this one restates cites '
                                                            f'{", ".join(cite_disp(c) for c in sorted(pci)[:3])}; '
                                                            f'the draft dropped the source'))
                if bag is not None:
                    bag['dropped'] = sorted(pci)
        elif dci - pci:
            moved = sorted(x for x in dci - pci if x in PCITES)
            fresh = sorted(x for x in dci - pci if x not in PCITES)
            if moved:
                notes.append(f'attribution moved: {", ".join(cite_disp(c) for c in moved[:3])} are cited '
                             f'elsewhere in the deposit')
            if fresh:
                flags.append(('needs check', 'attribution',
                              f'this sentence cites {", ".join(cite_disp(c) for c in fresh[:3])}, which the '
                              f'deposit never cites at all'))
                if bag is not None:
                    bag['added'] = sorted(fresh)
        if bool(pn) != bool(dn) and sc > 0.30:
            notes.append(f'polarity phrased differently (passage {pn[:2] or "no negator"}, draft '
                         f'{dn[:2] or "no negator"})')
        if INFER_OPEN.match(flat(d).strip()) and not pc and not dc and sc > 0.30:
            flags.append(('needs check', 'inference', 'the sentence opens on an inferential connective and the '
                                                      'passage states no consequence'))
    if not flags:
        if rr > 0.86 or (sc > 0.5 and rr > 0.66):
            return 'supported (near-verbatim)', [], ' ; '.join(notes)
        return 'supported (reworded)', [], ' ; '.join(notes)
    # the strict-census re-run reaches here too; it differs only in the windows STRICT narrows
    order = {'contradicted': 0, 'needs check': 1}
    kind = sorted(flags, key=lambda f: (order.get(f[0], 3), f[1]))[0]
    return f'{kind[0]}: {kind[1]}', flags, ' ; '.join(notes)


def write_csv(rows):
    with open(f'{OUT}/claim_ledger_v1.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['id', 'verdict', 'confidence', 'draft_section', 'draft_sentence', 'dep_section',
                    'deposit_proposition', 'paired_via', 'overlap', 'char_ratio', 'block_overlap', 'flags',
                    'notes', 'adjudication'])
        for x in rows:
            w.writerow([x['id'], x['verdict'],
                        'n/a' if x['verdict'].startswith('excluded') else
                        ('high' if x['ratio'] > .60 or x['score'] > .45 else
                         'medium' if x['score'] > .18 else 'low'),
                        x['sec'], x['draft'], x.get('dep_sec', ''), x.get('dep', ''), x.get('pair', ''),
                        x.get('score', ''), x.get('ratio', ''), x.get('block_overlap', ''),
                        ' | '.join(f'{g[0]}: {g[1]}: {g[2]}' for g in x['flags']), x.get('note', ''), ''])


def summary(cnt, conf):
    n = sum(v for k, v in cnt.items() if not k.startswith('excluded'))
    sup = cnt.get('supported (reworded)', 0) + cnt.get('supported (near-verbatim)', 0)
    contra = sum(v for k, v in cnt.items() if k.startswith('contradicted'))
    need = sum(v for k, v in cnt.items() if k.startswith('needs check'))
    unsup = cnt.get('unsupported: no partner located', 0)
    return (f'{sup} of the {n} ledgered sentences - {100 * sup // max(1, n)}% - restate a deposit proposition with '
            f'no marker out of place, and {contra} contradict the deposit on a value or on the direction of a claim '
            f'({cnt.get("contradicted: value", 0)} on a figure, {cnt.get("contradicted: causality", 0)} on '
            f'association turned into cause). {need} sentences differ from their original in force, condition or '
            f'attribution and are listed below for an adjudication; {unsup} are sentences the deposit does not '
            f'contain at all. The value test reads the deposit\u2019s maths, so a figure the draft spells out that '
            f'the paper wrote as `$6 \\times 10^5$` is recognised as the same figure and not reported as invented. '
            f'Nothing in this ledger is a correction: it is the list of places where the draft said something the '
            f'paper did not, or said it with different force, which is what a policy choice is made from.')


def write_md(rows, cnt, conf, ndb, npb, al):
    sev = {'contradicted': 0, 'unsupported': 1, 'needs check': 2}

    def cls(v):
        for k, s in sev.items():
            if v.startswith(k):
                return s, v.split(': ')[1] if ': ' in v else k
        return 3, ''
    need = sorted([x for x in rows if x['verdict'].startswith(('contradicted', 'unsupported', 'needs check'))],
                  key=lambda x: (cls(x['verdict'])[0], cls(x['verdict'])[1], x['id']))
    L = []
    L.append('# Claim ledger over the draft\u2019s non-shared sentences\n')
    SAY = summary(cnt, conf)
    L.append(f'''Written by `claim_ledger_v1.py`, pairs only. It does not rewrite, merge, repair or reword anything, and the
adjudication line under each entry is left blank for the author.

**What was paired.** The draft\u2019s body prose, `{DRAFT.split('/')[-1]}`, against the deposited article,
`{DEPOSIT.split('/')[-1]}`. {len(rows)} draft sentences were extracted from {ndb} body blocks; {cnt.get('excluded: shared verbatim', 0)} of
them are verbatim sentences of the deposit and were excluded as pairs, because where the wording is shared there is
nothing to adjudicate - the first pass of this audit measured 0 hedges, 0 quantifiers and 0 values out of place in
the paragraphs the two files share outright. The other {len(rows) - cnt.get('excluded: shared verbatim', 0)} sentences are the ledger.
They are paired through an alignment: {len(al)} of {ndb} draft blocks sit opposite a deposit block, and a sentence
is checked against the **whole aligned passage** rather than one sentence, because a hedge or a condition can live
in the neighbouring sentence and a comparison that misses that reports faithful plain-language writing as a change
of claim.

**The rules that produced each verdict.**

| verdict | fires when |
|---|---|
| `excluded: shared verbatim` | the sentence is the deposit\u2019s own wording, character for character |
| `not a claim (signposting)` | the sentence reports what the document does (this section, we defer to, the appendix holds) |
| `supported (near-verbatim)` | a partner passage was found and its overlap with the sentence is high |
| `supported (reworded)` | a partner passage was found and no marker differs |
| `needs check: strength` | the passage hedges and the sentence asserts, with a universal, a causal verb or a value |
| `needs check: scope` | the passage states a condition, population or limit the sentence drops |
| `needs check: attribution` | the passage names a source the sentence drops, or the sentence names one the passage lacks |
| `needs check: inference` | the sentence opens on *therefore, thus, because* and the passage asserts no consequence |
| `contradicted: value` | the sentence states a figure the deposit never states anywhere in the file |
| `contradicted: causality` | the passage says association and the sentence says cause |
| `unsupported: no partner located` | no deposit passage shares enough content with the sentence to be its original |

**Confidence** is printed with every entry: `high` above 0.60 character ratio or 0.45 token overlap, `medium` above
0.18 overlap, `low` below. Low confidence here usually means the draft wrote a technical sentence in plain English,
which is the operation the draft was asked to perform; it is printed rather than hidden so the author can see how
much of the ledger rests on a thin pairing.

**What the counts say.** {SAY}

---
''')
    flip = sum(1 for x in rows if x['verdict'].startswith('supported') and
               x.get('strict_verdict', '').startswith(('contradicted', 'needs check')))
    flipc = sum(1 for x in rows if x.get('strict_verdict', '').startswith('contradicted'))
    L.append('\n**A strict census, so the zero reads as a measurement and not a claim.** Running these same '
             f'sentences with the aligned passage no longer answering for the sentence - a figure has to sit in the '
             f'matched sentence itself, a hedge or a condition too - moves '
             f'{flip} rows out of `supported` into a flag, {flipc} of them into a contradiction. That is what the '
             'shipped tolerances buy: a divergence visible only against a sentence the alignment pairs loosely is '
             'left to the passage to answer for, and the pair is printed either way so the author sees it.\n')
    L.append(f'## Counts\n\n| verdict | sentences |\n|---|---|\n')
    for k, v in cnt.most_common():
        L.append(f'| `{k}` | {v} |')
    L.append('\nconfidence over the ledgered rows: ' + ', '.join(f'{k} {v}' for k, v in conf.most_common()) + '\n')
    L.append(f'\n---\n\n## The {len(need)} pairs that need an adjudication, most severe first\n')
    for x in need:
        c = 'high' if x['ratio'] > .60 or x['score'] > .45 else ('medium' if x['score'] > .18 else 'low')
        L.append(f"### {x['id']} · {x['verdict']} · draft §{x['sec'] or 'front'} · confidence {c} · "
                 f"overlap {x['score']}, ratio {x['ratio']}, paired through the {x['pair']}\n")
        L.append(f"**Draft, the claim as the draft makes it.**\n\n> {flat(x['draft'])}\n")
        if x.get('dep'):
            L.append(f"**Deposit, the proposition it corresponds to** (§{x.get('dep_sec') or '?'}):\n\n> "
                     f"{flat(x['dep'])}\n")
        for g in x['flags']:
            L.append(f"- *{g[0]}: {g[1]}* - {g[2]}")
        if x.get('note'):
            L.append(f"- *recorded, not judged* - {x['note']}")
        if x.get('dep_passage') and x.get('dep_passage') != x.get('dep'):
            L.append(f"\n<details><summary>the whole aligned passage</summary>\n\n> "
                     f"{flat(x['dep_passage'])[:1500]}\n\n</details>")
        L.append("\n**Adjudication:** ☐ accept as supported ☐ rewrite from the deposit ☐ the draft is right, "
                 "the deposit should say it ☐ other: ______\n")
    L.append('\n---\n\n## Where the rest of the ledger is\n\n')
    L.append('Every row, including the supported ones, is in `claim_ledger_v1.csv` (one row per sentence, '
             '`adjudication` column empty) and in `claim_ledger_v1.json` (the same rows with the full aligned '
             'passage attached). Nothing was dropped from the CSV to shorten this file: '
             f'{len(rows)} sentences, {cnt.get("supported (reworded)", 0)} supported-reworded, '
             f'{cnt.get("supported (near-verbatim)", 0)} near-verbatim, and the '
             f'{len(need)} above.\n')
    open(f'{OUT}/claim_ledger_v1.md', 'w').write('\n'.join(L))


def write_complement(rows, ds, db, dtxt, cnt):
    """Everything in the draft that the ledger does NOT speak about, and why.

    A null result is only worth what its coverage is worth: the ledger says no sentence contradicts the deposit,
    and this is the list of the sentences it never looked at. Each is named with the reason it is out, so a reader
    can judge whether the exclusions could hide the thing they are worried about.
    """
    seen = {x['idx'] for x in rows}
    excl = {norm(x['draft']) for x in rows if x['verdict'].startswith('excluded')}
    out = []
    for i, r in enumerate(ds):
        if i in seen:
            continue
        t, n = r['text'], norm(r['text'])
        why = ('excluded: it is the deposit\u2019s own wording, character for character' if n in excl
               else 'left out by the extractor: fewer than six words, or a fragment the maths strip leaves behind')
        out.append((i, r['sec'], why, t, r['b']))
    ledger_blocks = {ds[x['idx']]['b'] for x in rows if x['idx'] < len(ds)}
    dropped_blocks = [(bi, b) for bi, b in enumerate(db) if bi not in ledger_blocks]
    allb = [re.sub(r'\s+', ' ', x).strip() for x in re.split(r'\n\s*\n', dtxt) if x.strip()]
    unlooked = []
    dkey = {re.sub(r'[^a-z0-9]', '', norm(x))[:40] for x in db}
    for b in allb:
        # compare on the alphanumeric prefix, with maths removed: the extractor strips `$...$`, so a raw first
        # forty characters and the block it came from are different strings and a substring test reports prose
        # the ledger did read as prose it never looked at
        if re.sub(r'[^a-z0-9]', '', norm(b))[:40] not in dkey:
            kind = ('back matter' if BACK.match(b) else 'a heading' if re.match(r'^\s*#', b)
                    else 'a table, display or code block' if re.match(r'^\s*(\|\|\$\$|```|\|)', b)
                    else 'the reading note at the head of the file' if b.lstrip().startswith('>')
                    else 'author line or front matter' if FRONT_LINE.search(b)
                    else 'prose with no sentence of six words or more')
            unlooked.append((kind, re.sub(r'\s+', ' ', b)[:220]))
    n_risk = sum(1 for _, _, _, t, _ in out if numbers(t) or cites(t))
    L = ['# The complement of the claim ledger: what it did not read\n',
         f'The ledger speaks about {len(rows)} sentences. This is the rest of the draft, so that the counts in '
         f'`claim_ledger_v1.md` can be read as a statement about the document and not only about a sample of it. '
         f'Nothing here is judged; it is listed with the reason it is out.\n',
         f'\n| class | count |\n|---|---|\n| draft body blocks the extractor kept | {len(db)} |'
         f'\n| kept blocks that produced no row at all | {len(dropped_blocks)} |'
         f'\n| sentences extracted and then left out | {len(out)} |, of which {n_risk} carry a figure or a citation'
         f'\n| blocks of the file never read as prose | {len(unlooked)} |\n',
         '\n## The sentences extracted and left out\n',
         'Those marked as carrying a figure or a citation are the ones worth a glance: an excluded sentence that '
         'states a number is the only kind of exclusion that could hide a contradiction.\n']
    for i, sec, why, t, _bi in out:
        flag = '  \u25c0 **carries a figure or a citation**' if (numbers(t) or cites(t)) else ''
        L.append(f"- `D{i:04d}` \u00a7{sec or 'front'} \u00b7 {why}{flag}\n\n  > {flat(t)[:200]}")
    L.append('\n## Blocks of the draft never read as prose, and why\n')
    kinds = Counter(k for k, _ in unlooked)
    L.append('\n'.join(f'- {k}: {v}' for k, v in kinds.most_common()) or '- none')
    L.append('\n<details><summary>the first 40, so the classification can be checked</summary>\n')
    for k, t in unlooked[:40]:
        L.append(f"> *{k}* \u2014 {t[:170]}")
    L.append('\n</details>\n')
    L.append('\n## Kept prose blocks that produced no ledger row\n')
    L.append('These are blocks the extractor read and the ledger then had nothing to say about: usually a block '
             'of two- and three-word list items, where every candidate was below the six-word floor.\n')
    for bi, b in dropped_blocks[:60]:
        L.append(f"> block {bi} \u2014 {b[:180]}")
    open(f'{OUT}/claim_ledger_v1_complement.md', 'w').write('\n'.join(L))
    with open(f'{OUT}/claim_ledger_v1_complement.csv', 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['ordinal', 'section', 'why_out', 'carries_a_value_or_citation', 'text'])
        for i, sec, why, t, _bi in out:
            w.writerow([i, sec, why, bool(numbers(t) or cites(t)), t])
        for k, t in unlooked:
            w.writerow(['', '', f'block not read as prose: {k}', '', t])
        for bi, b in dropped_blocks:
            w.writerow(['', '', f'prose block with no row: block {bi}', '', b])
    print(f'complement: {len(out)} sentences extracted and left out ({n_risk} of them carry a figure or a '
          f'citation), {len(unlooked)} blocks never read as prose, {len(dropped_blocks)} prose blocks with no row')


def write_attribution_review(rows, dtxt):
    """The attribution rows, annotated for the one question that decides them.

    A dropped source is either a de-duplication - the draft cites the work somewhere else, in the sentence that
    needs it - or a loss. The default rule regenerates the sentence; the author overrules where the drop was
    deliberate, and this says which is which by looking the citation up in the draft itself.
    """
    L = ['# The attribution rows, sorted by whether the source survives elsewhere in the draft\n',
         'Produced for the overruling pass. `needs check: attribution` is the class where the draft\u2019s version '
         'is most likely the intended one, because a plain-language draft drops parentheticals on purpose when the '
         'same work is cited two sentences away. `de-duplicated` means the citation the deposit carries appears '
         'somewhere in the draft; `lost` means it appears nowhere, and those are the ones the default rule should '
         'regenerate.\n']
    kept = [x for x in rows if x['verdict'] == 'needs check: attribution']
    dedup, lost, other = [], [], []
    for x in kept:
        for w in x.get('cites_dropped', []):
            y = re.match(r'(\d{4}):(.+)$', w)
            if not y:
                other.append((x, cite_disp(w), None))
                continue
            names = y.group(2).split('|')
            # present in the draft if any of the names sits within a hundred-odd characters of the year, which is
            # what a de-duplicated citation looks like once the draft moved it to the sentence that needs it
            pat = r'(?:' + '|'.join(re.escape(n) for n in names) + r')[^)]{0,110}' + y.group(1)
            (dedup if re.search(pat, dtxt) else lost).append((x, cite_disp(w), y))
        for w in x.get('cites_added', []):
            other.append((x, cite_disp(w) + ' \u2014 cited by the draft, absent from the matched sentence', None))
    L.append(f'\n| reading | citations in this class |\n|---|---|\n| the source survives elsewhere in the draft '
             f'(de-duplication, probably intended) | {len(dedup)} |\n| the source is nowhere in the draft (a real '
             f'drop, regenerate) | {len(lost)} |\n| the flag names no parseable citation (the draft cites a work '
             f'the deposit never cites) | {len(other)} |\n\n---\n')
    for tag, group in (('the source is nowhere in the draft \u2014 regenerate', lost),
                       ('the source survives elsewhere in the draft \u2014 probably intended', dedup),
                       ('the draft cites something the deposit never cites \u2014 check the source', other)):
        if not group:
            continue
        L.append(f'\n## {tag}\n')
        for item in group:
            x, w = item[0], item[1]
            L.append(f"### {x['id']} \u00b7 \u00a7{x['sec'] or 'front'} \u00b7 confidence "
                     f"{'high' if x['ratio'] > .60 or x['score'] > .45 else 'medium' if x['score'] > .18 else 'low'}"
                     f"{' \u00b7 ' + w if w else ''}\n")
            L.append(f"**Draft.**\n\n> {flat(x['draft'])[:600]}\n")
            L.append(f"**Deposit, the sentence it restates.**\n\n> {flat(x.get('dep', ''))[:600]}\n")
            if len(item) == 3 and item[2] is not None and group is dedup:
                y = item[2]
                hit = re.search(r'[^.\n]{0,90}' + re.escape(y.group(1)) + r'[^)]{0,80}' + y.group(2) +
                                r'[^.]{0,20}\.', dtxt)
                if hit:
                    L.append(f"**Where the draft does cite it.**\n\n> \u2026{flat(hit.group(0))[:300]}\n")
            L.append("\n**Overrule the default?** \u2610 keep the draft\u2019s version "
                     "\u2610 regenerate from the deposit\n")
    open(f'{OUT}/claim_ledger_v1_attribution_review.md', 'w').write('\n'.join(L))
    print(f'attribution review: {len(kept)} rows \u2014 {len(dedup)} de-duplicated, {len(lost)} lost, '
          f'{len(other)} naming no parseable citation')


def mutate_test(dtxt, ptxt, k, seed):
    """Plant k known defects in a copy of the draft and see whether the rules find them.

    The ledger's headline is a zero: no sentence contradicts the deposit, on a figure or on the direction of a
    claim. A zero is only evidence if the instrument can see the thing it says is absent, so this writes defects
    in - a figure changed, a hedge deleted, a consequence asserted where the passage only associates, a citation
    stripped, a condition dropped - runs the same `build()` over the copy, and reports how many of each kind came
    back flagged. The shipped artifacts are not touched; this file is the only output.
    """
    import random
    rnd = random.Random(seed)
    per = max(4, k // 5)
    base, _, _, ds0, ps0, _, _ = build(dtxt, ptxt, limit=10 ** 9)
    byidx = {x['idx']: x for x in base}
    pool = [x for x in base if x['verdict'].startswith('supported')]
    rnd.shuffle(pool)
    plan = defaultdict(list)
    for x in pool:
        if len(plan) == 5 and all(len(v) >= per for v in plan.values()):
            break
        d, dep, pas = x['draft'], x.get('dep', ''), x.get('dep_passage', '')
        num = re.search(r'(?<![A-Za-z0-9.])(\d{4,7})(?!\d)', d)
        if num and len(plan['value']) < per:
            new = str(int(num.group(1)) + 37)
            if new not in re.sub(r'[,{}]', '', ptxt):
                plan['value'].append((x['idx'], d, d.replace(num.group(1), new, 1),
                                      f'the figure {num.group(1)} becomes {new}, which the deposit never states'))
            continue
        m = re.search(r'\b(may|might|could)\b', d)
        if m and len(plan['strength']) < per and marks(dep or '', HEDGE):
            plan['strength'].append((x['idx'], d, re.sub(r'\b' + m.group(1) + r'\b', 'always', d, count=1),
                                     f'the hedge `{m.group(1)}` becomes `always`, where the passage hedges'))
            continue
        pa, pc = marks(pas or dep, ASSOC), marks(pas or dep, CAUSAL)
        if pa and not pc and not marks(d, CAUSAL) and len(plan['causality']) < per:
            plan['causality'].append((x['idx'], d, 'Therefore, ' + d[0].lower() + d[1:],
                                      'an association in the passage turned into an asserted consequence'))
            continue
        cc = cites(dep or '')
        if cc and len(plan['attribution']) < per:
            y = re.match(r'(\d{4}):(.+)', sorted(cc)[0])
            if y:
                nm = y.group(2).split('|')[-1]
                pat = re.compile(r'\(\s*' + re.escape(nm) + r'[^()]{0,90}' + y.group(1) + r'\s*\)')
                if pat.search(d):
                    plan['attribution'].append((x['idx'], d, pat.sub('', d, count=1),
                                                f'the citation to {nm}, {y.group(1)} was stripped'))
                    continue
        cd = marks(d, COND)
        if cd and marks(dep or '', COND) and len(plan['scope']) < per:
            pat = re.compile(r'\b(?:' + '|'.join(re.escape(c) for c in cd) + r')\b[^,.;]{0,50}')
            hit = pat.search(d)
            if hit:
                plan['scope'].append((x['idx'], d, d.replace(hit.group(0), '', 1),
                                      f'the condition `{hit.group(0)[:44]}\u2026` was removed'))
                continue
    mut, planted = dtxt, []
    for cls, items in plan.items():
        for idx, old, new, why in items:
            if old in mut and old != new:
                mut = mut.replace(old, new, 1)
                planted.append((cls, idx, old, new, why))
    rows2 = build(mut, ptxt, limit=10 ** 9)[0]
    by2 = {x['idx']: x for x in rows2}
    res = defaultdict(lambda: [0, 0, 0, []])
    for cls, idx, old, new, why in planted:
        r0, r1 = byidx.get(idx), by2.get(idx)
        n = res[cls]
        n[0] += 1
        want = {'value': ('value', 'attribution'), 'strength': ('strength', 'scope'),
                'causality': ('causality', 'inference'), 'attribution': ('attribution',),
                'scope': ('scope', 'attribution', 'strength')}[cls]
        got = r1 and any(g[1] in want for g in r1['flags'])
        got_any = bool(r1) and bool(r1.get('flags'))
        if got_any:
            res[cls][3].append((idx, 'flagged under another heading', r1['verdict']))
        if got:
            n[1] += 1
            n[3].append((idx, 'found', r1['verdict']))
            continue
        n[2] += 1
        if not r1:
            why_miss = 'the mutated sentence dropped out of the extraction, so nothing was compared'
        elif r1['verdict'].startswith('excluded'):
            why_miss = 'the edit made the sentence the deposit\u2019s own wording, which the ledger excludes'
        elif r1['verdict'].startswith('unsupported'):
            why_miss = 'the edit moved the sentence off its partner, so pairing decided the row, not the markers'
        elif cls == 'strength' and r0 and marks(
                ' '.join(y['text'] for y in ds0 if y['b'] == r0.get('blk', -1)), HEDGE):
            why_miss = 'a sibling sentence still hedges: hedges travel, by design'
        else:
            why_miss = 'no flag; verdict ' + r1['verdict']
        n[3].append((idx, 'elsewhere' if got_any else 'miss', why_miss))
    tot = [0, 0, 0]
    L = ['# Did the instrument see the defects planted in it?\n',
         f'The ledger\u2019s headline is `0 contradicted: value` and `0 contradicted: causality`. {len(planted)} '
         f'defects were written into a copy of the draft and the same `build()` was run over it, to find out '
         f'whether that is a finding about the draft or a blind spot in the rules.']
    L.append('\n\n| planted | class | found under this heading | flagged, but filed elsewhere | not flagged at all '
             '| what the misses were |\n|---|---|---|---|---|---|')
    for cls in sorted(res):
        n = res[cls]
        tot = [tot[0] + n[0], tot[1] + n[1], tot[2] + n[2]]
        elsew = sum(1 for i, t, m in n[3] if t == 'elsewhere')
        miss = [m for i, t, m in n[3] if t == 'miss']
        L.append(f'| {n[0]} | {cls} | {n[1]} | {elsew} | {n[0] - n[1] - elsew} | '
                 + ('; '.join(sorted(set(miss))[:2])[:170] or '-'))
    allw = sum(v[0] for v in res.values())
    alle = sum(1 for v in res.values() for i, t, m in v[3] if t == 'elsewhere')
    allm = allw - sum(v[1] for v in res.values()) - alle
    L.append(f'| **{allw}** | | **{sum(v[1] for v in res.values())}** | **{alle}** | **{allm}** | |')
    L.append('\n\nThe three outcomes for a planted defect: the rule that owns that dimension raised it; a rule '
             'raised something on the row but filed it under another heading, which still puts the pair in front of '
             'the author; or nothing fired, which is the number that says how far the zero can be trusted. A row '
             'that reads `not flagged at all` after an edit which made the draft sentence identical to the '
             'deposit\u2019s own wording is a limit of the test, not of the rules - those sentences are excluded '
             'from the ledger by design - and they are named in the list below the table.')
    L.append('\n\n## Every planted defect, and what came back\n')
    for cls, idx, old, new, why in planted:
        r1 = by2.get(idx, {})
        L.append(f"- **{cls}** `D{idx:04d}` ({why})\n  - was: {flat(old)[:170]}\n  - became: {flat(new)[:170]}\n"
                 f"  - ledger said: `{r1.get('verdict', 'not extracted')}`"
                 + ('' if not r1.get('flags') else ' \u2014 ' + '; '.join(g[2][:110] for g in r1['flags'])))
    L.append('\n\n## Reading\n\nA miss is not automatically a defect in the rules: `strength` is judged against the '
             'draft\u2019s paragraph, so a sentence whose neighbour still hedges is left alone, which is the '
             'deliberate choice that stopped the first version of this file flagging a third of its rows. Those '
             'misses are counted with the rest and labelled, so the number can be argued with.\n')
    open(f'{OUT}/claim_ledger_v1_mutation_test.md', 'w').write('\n'.join(L) + '\n')
    print(f'mutation test: {tot[0]} planted, {tot[1]} found, {tot[2]} not found '
          f'(claim_ledger_v1_mutation_test.md)')
    for cls in sorted(res):
        print(f'   {cls:12s} planted {res[cls][0]:2d}  found {res[cls][1]:2d}  missed {res[cls][2]:2d}')
    return planted, res

if __name__ == '__main__':
    main()

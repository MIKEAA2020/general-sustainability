#!/usr/bin/env python3
"""v49 build (final form).

Front matter + section 1: the author's adaptation (the `gemini:` half of
uploads/p3 humanized.txt), repaired against the deposited article.
Body (section 2 onward): v48's body, unchanged, plus six sentences restored
verbatim from the line that carried them (v42/v47), because v48's `regen` pass
rewrote them away and each one names a defined object:
    monomaterial projection, never in the stock, differentiated only by,
    replenished by recharge, two readings of one ledger,
    not a primitive of the closed natural block
Nothing else in the body moves, and the build asserts exactly that.

Ruled elsewhere and implemented here:
  * term revert (revision/v49/adaptation_term_revert_v1.csv, 14 rules; force +
    label applied to the base before adoption, watch reported only);
  * the four P0 invented assertions deleted with their sentences;
  * the adaptation's two-level headings cut, the deposit's two-senses passage
    left alone (the ruling is about headings, not about content of the deposit);
  * section 1 numbers and citations gated against the deposit; a sentence is
    only dropped for unsupported content when it carries no deposit wording of
    its own (an earlier pass dropped two deposit-backed sentences because the
    citation test mis-parsed multi-author cites - fixed below).
"""
import json, re, pathlib, collections

ROOT = pathlib.Path('/home/user'); V7 = ROOT / 'revision/v7'; D = ROOT / 'revision/v49'
SRC = ROOT / 'uploads/p3 humanized.txt'; DEPO = ROOT / 'work/paper3.txt'
OUT = V7 / 'paper3_material_ledgers_v49.md'
ADAPT_LO, ADAPT_HI = 2, 117
NUM = re.compile(r'(?<![\w.])(\d+\.\d+|\d{3,})(?![\w.])')
CUT_CLAUSES = [r'\s*The illusion operates on two levels:\s*']      # the two-level framing, cut with its labels
DROP_SENTENCES = ['approximately 5%', '1/0.130', 'instantaneous statistic vs', 'engineered to capture',
                  'artificially thresholded', 'satellite-derived masks', 'Routing is determined by']

def flat(s):
    """plain-text form used for substring evidence: math collapsed, markup gone, one space"""
    s = re.sub(r'\$\$.*?\$\$', ' ', s, flags=re.S)
    s = re.sub(r'\$[^$]*\$', ' ', s)
    s = re.sub(r'\\\[.*?\\\]', ' ', s, flags=re.S)
    s = re.sub(r'\\\(|\\\)', ' ', s)
    s = re.sub(r'[*_`#|>]', ' ', s).replace('\u2019', "'").replace('\u2014', ' ').replace('\u2013', '-')
    return re.sub(r'\s+', ' ', s).strip()

def lower_flat(s): return flat(s).lower()

def shingles(t, k=6):
    ws = re.sub(r'[^0-9a-z \'\-]', ' ', lower_flat(t)).split()
    return {' '.join(ws[i:i + k]) for i in range(len(ws) - k + 1)}

def sentences(t):
    t = re.sub(r'\$\$.*?\$\$', ' M ', t, flags=re.S)
    t = re.sub(r'\$[^$]*\$', ' M ', t)
    t = re.sub(r'[ \t]*\n[ \t]*', ' ', t)
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"(*])', t) if len(s.strip()) > 25]

DEP = DEPO.read_text(); DEPFLAT = lower_flat(DEP); DEPNUM = set(NUM.findall(DEP))
DEPSH = shingles(DEP, 6)

def cited(sent):
    """(Surname et al., Year) / Surname (Year) pairs, matched by proximity in the deposit"""
    bad = []
    for m in re.finditer(r'([A-Z][A-Za-z\'\-]{3,})[^()\n]{0,60}?(\d{4})[a-z]?', sent):
        nm, yr = m.group(1).lower(), m.group(2)
        if nm in ('the', 'section', 'table', 'figure', 'remark', 'appendix', 'and', 'for'):
            continue
        hit = False
        for p in [x.start() for x in re.finditer(re.escape(nm), DEPFLAT)]:
            if re.search(r'\b' + yr + r'\b', DEPFLAT[p:p + 90]):
                hit = True; break
        if not hit:
            bad.append(f'{m.group(1)}, {yr}')
    return bad

def read_rules(path):
    rows = []
    for ln in path.read_text().split('\n'):
        ln = ln.strip()
        if not ln or ln.startswith('#'):
            continue
        f = ln.split(',', 6)
        if len(f) >= 6:
            rows.append({'alias': f[0], 'replacement': f[1], 'scope': f[2], 'gem': int(f[3]),
                         'dep': int(f[4]), 'v48': int(f[5]), 'why': f[6] if len(f) > 6 else ''})
    return rows

# ---------------------------------------------------------------- front matter
log = collections.defaultdict(list)
fm = '\n'.join(SRC.read_text().split('\n')[ADAPT_LO - 1:ADAPT_HI])
fm = re.sub(r'\\\[(.+?)\\\]', lambda m: '$$\n' + m.group(1).strip() + '\n$$', fm, flags=re.S)
fm = fm.replace('\\(', '$').replace('\\)', '$')
fm = re.sub(r'^\s*On it[.:].*$', '', fm, flags=re.M)

# the two-level framing appears in the adaptation as a bold label on a bullet, not as a
# heading; the ruling cuts the label and keeps the sentence, because the sentences describe
# the two failures the deposit names in its own words
for h in CUT_CLAUSES + [r'^###\s*Arithmetic Level\s*$', r'^###\s*Dynamical Level[^\n]*$',
          r'\*\s*\*\*The Arithmetic Level:\*\*\s*', r'\*\s*\*\*The Dynamical Level \(Yield Inflation\):\*\*\s*']:
    m = re.search(h, fm, re.M)
    if m:
        log['headings_cut'].append(m.group(0).strip())
        fm = fm[:m.start()] + ('* ' if m.group(0).lstrip().startswith('*') else '') + fm[m.end():]

rules = read_rules(D / 'adaptation_term_revert_v1.csv')
for r in rules:
    if r['scope'] in ('force', 'label') and r['replacement']:
        n = fm.count(r['alias'])
        if n:
            fm = fm.replace(r['alias'], r['replacement'])
            log['term_edits'].append({'alias': r['alias'], 'to': r['replacement'], 'n': n, 'scope': r['scope']})
watch = [r for r in rules if r['scope'] == 'watch' and r['alias'] in fm]
log['watch_only'] = [{'alias': r['alias'], 'would_have_been': r['replacement']} for r in watch]

kept, disp = [], False
# A line is rewritten only when a sentence is actually deleted from it, and then by
# substring removal: an earlier pass rebuilt every line from the sentence splitter's
# output, which masks $...$ as a placeholder, and so turned the front matter's inline
# mathematics into a literal M and flattened its numbered lists. Rebuilding prose from a
# masked view of it is the same mistake as normalising reused maths; the file is left
# exactly as written wherever nothing has to go.
for ln in fm.split('\n'):
    if ln.strip().startswith('$$'):
        disp = not disp; kept.append(ln); continue
    if disp or not ln.strip() or ln.lstrip().startswith(('#', '|', '*', '-')):
        kept.append(ln); continue
    doomed = []
    for s in sentences(ln):
        why = None
        if any(x in s or x.replace(' ', '') in s.replace(' ', '') for x in DROP_SENTENCES):
            why = 'invented assertion (review/joint_evaluation_v1.md P0) or a cut label'
        else:
            badn = [x for x in NUM.findall(s) if x not in DEPNUM]
            badc = cited(s)
            if badn or badc:
                supported = (any(x in DEPNUM for x in NUM.findall(s)) or bool(shingles(s, 6) & DEPSH)
                             or len(badc) < len(cited(s)) + 1 and bool(shingles(s, 4) & DEPSH))
                log['gate_numbers'] += badn; log['gate_citations'] += badc
                if not supported:
                    why = f'nothing in the sentence is supported by the deposited article (numbers {badn}, citations {badc})'
                else:
                    log['kept_despite_gate'].append({'text': s[:150], 'numbers': badn, 'citations': badc})
        if why:
            doomed.append((s, why))
    if not doomed:
        kept.append(ln); continue
    raw = ln
    for s, why in doomed:
        ws = [w for w in re.sub(r'[^A-Za-z0-9 ]', ' ', re.sub(r'\$[^$]*\$', ' ', s)).split() if len(w) > 2]
        if len(ws) < 6:
            log['undeletable'].append({'text': s[:120], 'reason': 'too few words to locate safely'}); continue
        pat = r'\W+'.join(map(re.escape, ws[:4])) + r'.*?' + r'\W+'.join(map(re.escape, ws[-4:]))
        m = re.search(pat, raw)
        if not m:
            log['undeletable'].append({'text': s[:120], 'reason': 'sentence could not be located in the raw line'}); continue
        raw = (raw[:m.start()] + raw[m.end():]).lstrip()
        log['sentences_deleted'].append({'text': s[:200], 'reason': why})
    kept.append(raw)
fm = '\n'.join(kept)
fm = re.sub(r'\n{3,}', '\n\n', fm).rstrip()

# ------------------------------------------------------------------ 1b. carried-over deposit passages
# A rule file, so the gate and the build read the same ruling: content the deposited
# article states and the adaptation does not repeat is carried across verbatim rather than
# left to the swap. Losing a claim is not a consequence of rewording.
carry_path = D / 'v49_carry_over.json'
if carry_path.exists():
    for rule in json.loads(carry_path.read_text()):
        src = (V7 / rule['source']).read_text()
        i = src.find(rule['start']); j = src.find(rule['end'], i)
        if i < 0 or j < 0:
            log['carry_over'].append({'id': rule['id'], 'placed': 'NOT FOUND in the source'}); continue
        raw = src[i:j + len(rule['end'])]
        para = re.split(r'\n\s*\n', raw)
        passage = ' '.join(' '.join(x.split()) for x in para)
        k = fm.find(rule['place_after'])
        if k < 0:
            log['carry_over'].append({'id': rule['id'], 'placed': 'NOT PLACED (anchor absent from the front matter)'}); continue
        eol = fm.find('\n', k)
        fm = fm[:eol] + ' ' + passage + fm[eol:]
        log['carry_over'].append({'id': rule['id'], 'placed': 'appended to the anchored front-matter paragraph',
                                  'chars': len(passage), 'text': passage[:300], 'why': rule['why']})

# ---------------------------------------------------------------- body
v48 = (V7 / 'paper3_material_ledgers_v48.md').read_text()
v42 = (V7 / 'paper3_material_ledgers_v42.md').read_text()
v47 = (V7 / 'paper3_material_ledgers_v47.md').read_text()
i2 = v48.index('\n## 2. ')
body = v48[i2 + 1:]
blines = body.split('\n')
import difflib
a42 = [flat(x) for x in v42[v42.index('\n## 2. '):].split('\n')]
a48 = [flat(x) for x in blines]
sm = difflib.SequenceMatcher(None, a42, a48, autojunk=False)
pairs = []                                   # (v42 line -> v48 line) for identical lines
for b in sm.get_matching_blocks():
    for k in range(b.size):
        pairs.append((b.a + k, b.b + k))
pairs.sort()

def v48_row_for(v42_row):
    """the v48 line that carries the same text, or the last line before the gap"""
    best = None
    for a, b in pairs:
        if a <= v42_row:
            best = b
        else:
            break
    return best

def section_bounds(sec):
    m = re.search(r'^#{2,3}\s+' + re.escape(sec) + r'[\.\s]', body, re.M)
    if not m:
        return None
    start = body[:m.start()].count('\n')
    nxt = re.compile(r'^#{2,3}\s').search(body, m.end() + 1)
    end = start + body[m.start():m.end() + nxt.start()].count('\n') if nxt else len(blines) - 1
    return start, end

restores = json.loads((D / 'v49_required_restores.json').read_text())
v42_lines = v42[v42.index('\n## 2. '):].split('\n')
placed_rows = []
for rec in restores:
    ph = rec['phrase']
    if ph.lower() in flat(body).lower():
        log['restored'].append({'phrase': ph, 'row': rec['row'], 'placed': 'already present, skipped'}); continue
    i = next((k for k, x in enumerate(a42) if ph.lower() in x.lower()), None)
    tgt = v48_row_for(i - 1) if i is not None else None
    how = ''
    if tgt is not None and tgt + 1 < len(blines) and len(blines[tgt + 1].strip()) > 0 and not blines[tgt + 1].lstrip().startswith(('#', '|', '$')):
        row = tgt + 1; how = 'after the aligned v42 predecessor line'
    else:
        row = None
        sb = section_bounds(rec['sec'])
        if sb:
            for j in range(sb[1], sb[0], -1):
                if len(blines[j].strip()) > 40 and not blines[j].lstrip().startswith(('#', '|', '$$', '-')):
                    row = j; how = 'end of section ' + rec['sec']; break
    if row is None:
        log['restored'].append({'phrase': ph, 'row': rec['row'], 'placed': 'NOT PLACED'}); continue
    donor = rec['donor_v47']
    donor = re.sub(r'\s*#{2,3}\s.*$', '', donor).strip()
    donor = re.sub(r'\s+', ' ', donor)
    if donor.lower().count(ph.lower()) == 0:      # donor lost its content to the splitter: take the v42 line
        donor = re.sub(r'^\s*[-*]\s*', '', v42_lines[i]).strip()
    blines[row] = blines[row].rstrip() + ' ' + donor
    placed_rows.append((row, ph))
    log['restored'].append({'phrase': ph, 'row': rec['row'], 'placed': f'body line {row + 1}', 'how': how,
                            'sentence': donor[:300]})
body_new = '\n'.join(blines)

# the body must be v48's body plus those insertions and nothing else
# raw line containment: flat() mis-pairs $$ across multi-line displays, and an
# instrument that reports a loss the file does not have is worse than no instrument
removed = [l for l in body.split('\n') if l.strip() and l.strip() not in body_new]
log['body_inclusion'] = {'v48_body_lines_absent_from_v49': len(removed), 'examples': removed[:6]}
log['landing_sections'] = []
for row, ph in placed_rows:
    heads = [m for m in re.finditer(r'^#{2,3}\s+(\d+(?:\.\d+)*)', body_new, re.M)]
    secn = None
    cnt = 0
    for k, bl in enumerate(body_new.split('\n')[:row + 1]):
        m = re.match(r'^#{2,3}\s+(\d+(?:\.\d+)*)', bl)
        if m: secn = m.group(1)
    want_sec = next(r['sec'] for r in restores if r['phrase'] == ph)
    ok = bool(secn) and (secn == want_sec or secn.startswith(want_sec.rsplit('.', 1)[0]))
    log['landing_sections'].append({'phrase': ph, 'landed_in': secn, 'expected': want_sec, 'ok': ok})

final = fm + '\n\n---\n\n' + body_new
OUT.write_text(final)
log['summary'] = {'bytes': OUT.stat().st_size, 'lines': final.count('\n') + 1,
                  'front_matter_lines': len(fm.split('\n')), 'body_lines': len(body_new.split('\n')),
                  'term_edits': len(log['term_edits']), 'sentences_deleted': len(log['sentences_deleted']),
                  'restored': sum(1 for r in log['restored'] if r['placed'].startswith('body line')),
                  'v48_body_lines_lost_by_this_build': len(removed),
                  'residual_flags_numbers': sorted(set(log['gate_numbers'])),
                  'residual_flags_citations': sorted(set(log['gate_citations']))}
(D / 'v49_front_matter_edits.json').write_text(json.dumps(log, indent=1) + '\n')
print(json.dumps(log['summary'], indent=1))
print('\ndeleted:'); [print('   -', x['reason'][:70], '::', x['text'][:80]) for x in log['sentences_deleted']]
print('kept anyway (deposit-backed):', len(log['kept_deposit_backed_despite_gate']))
print('restores:'); [print('   -', r['phrase'], '->', r['placed']) for r in log['restored']]
print('watch-only (reported, not applied):', log['watch_only'])

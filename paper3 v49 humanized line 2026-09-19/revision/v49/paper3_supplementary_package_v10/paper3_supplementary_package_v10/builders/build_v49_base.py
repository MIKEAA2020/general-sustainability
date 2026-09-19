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
CUT_CLAUSES = [r'[ \t]*The illusion operates on two levels:[ \t]*']      # the two-level framing, cut with its labels
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
ADAPT_RAW_FM = fm      # the adaptation as written, before any repair touches it
fm = re.sub(r'\\\[(.+?)\\\]', lambda m: '$$\n' + m.group(1).strip() + '\n$$', fm, flags=re.S)
fm = fm.replace('\\(', '$').replace('\\)', '$')
fm = re.sub(r'^\s*On it[.:].*$', '', fm, flags=re.M)

# the two-level framing appears in the adaptation as a bold label on a bullet, not as a
# heading; the ruling cuts the label and keeps the sentence, because the sentences describe
# the two failures the deposit names in its own words
for h in CUT_CLAUSES + [r'^###\s*Arithmetic Level\s*$', r'^###\s*Dynamical Level[^\n]*$',
          r'\*\*The Arithmetic Level:\*\*[ \t]*', r'\*\*The Dynamical Level \(Yield Inflation\):\*\*[ \t]*']:
    m = re.search(h, fm, re.M)
    if m:
        log['headings_cut'].append(m.group(0).strip())
        # only the label is deleted; the item's own `* ` marker stays, so the author's two-item
        # list survives as a list instead of becoming two prose lines glued together
        fm = fm[:m.start()] + fm[m.end():]

rules = read_rules(D / 'adaptation_term_revert_v1.csv')
for r in rules:
    if r['scope'] in ('force', 'label') and r['replacement']:
        n = fm.count(r['alias'])
        if n:
            fm = fm.replace(r['alias'], r['replacement'])
            log['term_edits'].append({'alias': r['alias'], 'to': r['replacement'], 'n': n, 'scope': r['scope']})
watch = [r for r in rules if r['scope'] == 'watch' and r['alias'] in fm]
log['watch_only'] = [{'alias': r['alias'], 'would_have_been': r['replacement']} for r in watch]

# ------------------------------------------------------------------ 1a. house-form the adaptation's front matter
# Three formatting facts about the manuscript of this line, all read off v48 rather than invented: the
# title/author/ORCID/date block is not in the markdown (it lives in the .tex header), a heading has a
# blank line on both sides of it, and `## Abstract` is the abstract heading's level. The adaptation's
# file violates all three, and the first violation is not cosmetic: with a heading glued to the
# paragraph under it, a block splitter takes the pair as one heading block - which is how five
# paragraphs, the numbered contributions list among them, ended up inside a \subsection*{} argument
# and were typeset as a heading with no spacing.
# ---------------------------------------------------------------- prose repairs, region only
# Two mechanical fixes the rewrite left behind. They are not editorial choices: the strings they
# produce appear in no earlier surface, and the deposit and the frozen body each decide the case.
#   * `an catastrophic deficit` exists only in the adaptation (v48, v42 and the deposit have zero
#     `an`-before-consonant sites), so it is a typo of this line, not the author's prose.
#   * the -ize / -ise mix in the region is NOT repaired here; see the comment inside the function and
#     the open item, because the frozen body mixes them too and there is no convention to match.
_AN_EX = {'hour', 'hours', 'honest', 'honesty', 'honor', 'honour', 'heir', 'heirs', 'hymn', 'hymns'}
_DEP_TXT = DEPO.read_text() if DEPO.exists() else ''
_V48_TXT = (V7 / 'paper3_material_ledgers_v48.md').read_text()
_V48_BODY = _V48_TXT[_V48_TXT.index('\n## 2. '):] if '\n## 2. ' in _V48_TXT else _V48_TXT


def prose_repairs(s):
    """(repaired text, [(kind, before, after)]) for one line"""
    ed = []

    def _an(m):
        w = m.group(1)
        if (not re.fullmatch(r'[A-Za-z]{3,}', w) or w.isupper() or w.lower() in _AN_EX
                or w[0] not in 'bcdfghjklmnpqrstvwxyz'):
            return m.group(0)                      # acronyms, hyphenated forms and vowel sounds pass
        ed.append(('article', 'an ' + w, 'a ' + w))
        return 'a ' + w

    s = re.sub(r'\ban ([A-Za-z][A-Za-z]{2,})', _an, s)
    # the -ize/-ise alignment that stood here was removed after it rewrote the section heading
    # `### 1.3 Organization` into `Organisation` because the OECD's name appears in the reference
    # list. The premise was wrong anyway: v48's body, which this build may not touch, mixes the two
    # (specialization 14, realized, authorized against normalised, mobilised), so there is no single
    # convention to align to and a half-aligned document would be worse than a mixed one. The mix is
    # now an open item with the counts attached, not a repair.
    return s, ed


def house_form(fm, log):
    L = fm.split('\n')
    rep = {'rules': 0, 'level_changes': 0, 'dropped_full': []}
    first_head = next((k for k, x in enumerate(L) if re.match(r'^#{2,4}\s', x)), None)
    if first_head:
        dropped = [x.strip() for x in L[:first_head]
                   if not re.match(r'^#\s', x) and x.strip() not in ('', '---')]
        if dropped:
            rep['dropped_full'] = dropped
            log['preamble_dropped'] = [x[:70] for x in dropped]
            # a rule sitting inside the dropped preamble vanishes with it; count it too, or the
            # character proof below would be missing three characters and would fail for the wrong reason
            rep['rules'] += sum(1 for x in L[:first_head] if x.strip() == '---')
            L = [L[0]] + L[first_head:]
    rep['rules'] = sum(1 for x in L if x.strip() == '---')
    L = [x for x in L if x.strip() != '---']
    L = [x.rstrip() for x in L]
    _lvl_edits = []
    def _lvl(m):
        _lvl_edits.append((m.group(0).strip(), '## Abstract'))
        return '## Abstract'
    L = [re.sub(r'^#{3,4}(\s*Abstract\s*)$', _lvl, x) for x in L]
    rep['level_changes'] = len(_lvl_edits)
    rep['level_edits'] = _lvl_edits
    def is_head(x): return bool(re.match(r'^#{1,6}\s', x))
    def is_list(x): return bool(re.match(r'^\s*([-*]|\d+\.)\s+\S', x))
    def is_disp(x): return x.strip().startswith('$$')
    out = []
    for x in L:
        if out and x.strip() and out[-1].strip():
            if (is_head(x) or is_head(out[-1]) or is_disp(x) or is_disp(out[-1])
                    or (is_list(x) and not is_list(out[-1])) or (is_list(out[-1]) and not is_list(x))):
                out.append('')
        out.append(x.rstrip())
    out2, _pr = [], []
    for x in out:
        _fx, _ed = prose_repairs(x)
        out2.append(_fx)
        _pr += _ed
    rep['prose_repairs'] = _pr
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(out2)).strip(), rep

# The proof is whole-line, not character-counting: what house-forming is allowed to do is drop the
# logged lines, insert blank lines, and change the abstract heading's level - nothing else, and not
# in a different order. A character-compression proof was tried first and was wrong in both
# directions (it counted `---` inside table rules as a dropped rule, and it removed the title's `#`
# instead of the abstract's, because str.replace hits the first match).
_before_lines = fm.split('\n')
fm, _rep = house_form(fm, log)
_after_lines = fm.split('\n')
_dropped = set(x.strip() for x in _rep['dropped_full'])
_exp = []
for _x in _before_lines:
    _s = _x.strip()
    if not _s or _s == '---' or _s in _dropped:
        continue
    _s = re.sub(r'^#{3,4}(\s*Abstract\s*)$', '## Abstract', _s)
    _s = prose_repairs(_s)[0]                      # the same repairs, replayed, or the proof is a lie
    _exp.append(_s)
_got = [x.strip() for x in _after_lines if x.strip()]
log['prose_repairs'] = _rep['prose_repairs']
log['house_form_proof'] = {
    'lines_before': len([x for x in _before_lines if x.strip()]), 'lines_after': len(_got),
    'byline_lines_removed': _rep['dropped_full'], 'rules_removed': _rep['rules'],
    'abstract_heading_level_changes': _rep['level_changes'],
    'only_logged_changes': _exp == _got, 'order_preserved': _exp == _got}
if not log['house_form_proof']['only_logged_changes']:
    _bad = next((i for i, (a_, b_) in enumerate(zip(_exp, _got)) if a_ != b_), min(len(_exp), len(_got)))
    log['house_form_proof']['first_difference'] = {'at_line': _bad, 'expected': _exp[_bad][:200] if _bad < len(_exp) else None,
                                                    'actual': _got[_bad][:200] if _bad < len(_got) else None}
    (D / 'v49_house_form_mismatch.json').write_text(json.dumps(log['house_form_proof'], indent=2))
    raise SystemExit('house-forming changed more than the logged lines -> '
                     'revision/v49/v49_house_form_mismatch.json')
(D / 'v49_house_form_mismatch.json').unlink(missing_ok=True)

# ------------------------------------------------------------------ 1b. the first line of the abstract, as instructed
FIRST = 'Depletion indicators can carry similar units while built to inform distinct questions.'
_m = re.search(r'(^## Abstract[ \t]*\n+[ \t]*)([^\n]+)', fm, re.M)
if _m and not _m.group(2).strip().startswith(FIRST):
    _ss = sentences(_m.group(2)) or [_m.group(2)]
    _rest = ' '.join(_ss[1:]).strip() if len(_ss) > 1 else ''
    fm = fm[:_m.start(2)] + (FIRST + (' ' + _rest if _rest else '')) + fm[_m.end(2):]
    log['first_line'] = {'now_first': FIRST, 'removed_as_duplicate': _ss[0][:240],
                         'note': 'the adaptation opened the abstract on the same point in its own words; the '
                                 'instruction keeps the deposited article\'s sentence as the first line, so the '
                                 'paraphrase is removed rather than left to repeat it'}
else:
    log['first_line'] = {'now_first': FIRST if _m else 'NO ABSTRACT HEADING FOUND', 'removed_as_duplicate': ''}

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
        fm = fm[:eol].rstrip() + '\n\n' + passage + '\n\n' + fm[eol:].lstrip('\n')
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
V42_ALL = v42.split('\n')
placed_rows = []
def _sents(s):
    masked = re.sub(r'\$\$.*?\$\$|\$[^$]*\$', lambda m: '\x00' * len(m.group(0)), s, flags=re.S)
    return [x for x in re.split(r'(?<=[.!?])\s+(?=[A-Z*(])', masked) if x.strip()]

for rec in restores:
    ph = rec['phrase']
    if ph.lower() in flat(body).lower():
        log['restored'].append({'phrase': ph, 'row': rec['row'], 'placed': 'already present, skipped'}); continue
    # the text to insert is re-read from the donor line now, not trusted from the rule file: a rule
    # file that has drifted from its source would otherwise ship the drift
    dl = V42_ALL[rec['donor_line'] - 1]
    ins = rec.get('clause') or rec['donor_sentence']
    assert ins in dl, (f"{rec['row']}: the inserted text is not verbatim in the v42 donor line "
                       f"({rec['donor_line']}); it would be a rewording, not a carry-over")
    assert ins.count('$') % 2 == 0, f"{rec['row']}: the insert has unbalanced $, so a formula was clipped"
    assert not re.search(r'#{2,4}\s|^\s*---\s*$|\n', ins), f"{rec['row']}: the insert crosses a heading or rule"
    i = next((k for k, x in enumerate(a42) if ph.lower() in x.lower()), None)
    tgt = v48_row_for(i - 1) if i is not None else None
    how = ''
    if rec['mode'] == 'extend-final-sentence':
        cand = [k for k, x in enumerate(blines) if rec['target_probe'] in x]
        assert len(cand) == 1, f"{rec['row']}: target probe {rec['target_probe']!r} matched {len(cand)} body lines"
        row = cand[0]; how = 'extended the sentence carrying ' + repr(rec['target_probe'])
        line = blines[row]
        # insert the clause before the full stop that ends the probed sentence, so the article's own
        # sentence grows instead of a second sentence saying it twice
        k = line.find(rec['target_probe'])
        stop = line.find('.', k + len(rec['target_probe']))
        assert stop > 0, f"{rec['row']}: no sentence end found after the probe"
        _ins = ins.strip()
        # the donor's own connector (": " or "; ") belongs to the sentence it continues, so a clause
        # opening with it is glued rather than given a space - `resource :` is not house style
        _join = '' if _ins[0] in ':;,' else ' '
        new_line = line[:stop] + _join + _ins + line[stop:]
        rec_raw = _join + _ins
        assert not re.search(r'\s[:;,.](?=\s|$)', new_line.replace(' .', '.')), \
            f"{rec['row']}: the insertion left a space before punctuation"
    else:
        if tgt is not None and tgt + 1 < len(blines) and len(blines[tgt + 1].strip()) > 0 \
                and not blines[tgt + 1].lstrip().startswith(('#', '|', '$')):
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
        new_line = blines[row].rstrip() + ' ' + ins.strip()
        rec_raw = ' ' + ins.strip()
    # the guard that was missing when this shipped the first time: an insertion must not repeat a
    # sentence the target line already carries, and must be the only change to that line
    for s0 in _sents(blines[row]):
        sim = difflib.SequenceMatcher(None, ' '.join(s0.split()), ' '.join(ins.split())).ratio()
        assert sim < 0.62, (f"{rec['row']}: the insert repeats the target line's own sentence "
                             f'(similarity {sim:.2f}); extend it instead of appending a twin: '
                             + ' '.join(s0.split())[:120])
    ops = [o for o in difflib.SequenceMatcher(None, blines[row], new_line).get_opcodes() if o[0] != 'equal']
    assert len(ops) == 1 and ops[0][0] == 'insert', \
        f"{rec['row']}: the edit to body line {row + 1} is not a single insertion ({[o[0] for o in ops]})"
    blines[row] = new_line
    placed_rows.append((row, ph))
    log['restored'].append({'phrase': ph, 'row': rec['row'], 'placed': f'body line {row + 1}', 'how': how,
                            'mode': rec['mode'], 'oracle': rec['oracle'], 'inserted': ins,
                            'target_probe': rec.get('target_probe', ''),
                            'inserted_raw': rec_raw})

# ------------------------------------------------------------------ 1c. one body repair, from the read
# v48's own repair pass left a sentence in the body twice, once plain and once bolded. Deleting the
# bolded twin is provably content-preserving - the two are the same words - so it is applied here and
# recorded as erratum E10 rather than inherited silently into a new revision.
_rep_path = D / 'v49_body_repairs.json'
log['body_repairs'] = []
if _rep_path.exists():
    for rp in json.loads(_rep_path.read_text()):
        idx = [k for k, x in enumerate(blines) if rp['line_probe'] in x]
        if len(idx) != 1:
            log['body_repairs'].append({'kind': rp['kind'], 'result': f'probe matched {len(idx)} lines, skipped'})
            continue
        k = idx[0]
        # delete the twin together with the single space that joined it, so the line's only change
        # is one contiguous deletion and the paragraph spacing does not have to be cleaned up after
        old_l = blines[k]
        new_l = blines[k].replace(' ' + rp['remove'], '', 1)
        if new_l == old_l:
            new_l = blines[k].replace(rp['remove'], '', 1)
        if rp['remove'] not in blines[k]:
            log['body_repairs'].append({'kind': rp['kind'], 'result': 'the duplicated run is not on that line, skipped'})
            continue
        assert old_l.count(rp['keep']) == 2, f"{rp['kind']}: the sentence does not occur twice, so this is not a duplicate"
        assert new_l.count(rp['keep'].strip('*')) == 1, f"{rp['kind']}: the survivor count is wrong after the deletion"
        blines[k] = new_l
        log['body_repairs'].append({'kind': rp['kind'], 'line': k + 1, 'removed': rp['remove'],
                                    'kept': rp['keep'], 'result': 'the bolded twin deleted, the sentence kept once'})

body_new = '\n'.join(blines)

# the body must be v48's body plus those insertions and nothing else
# raw line containment: flat() mis-pairs $$ across multi-line displays, and an
# instrument that reports a loss the file does not have is worse than no instrument
# every v48 body line must survive as itself or as itself plus one contiguous insertion; the
# three extended sentences ship a clause inside a v48 line, so verbatim containment is the wrong
# test and used to report three losses that were not losses
_olds = body.split('\n')
_news = body_new.split('\n')
assert len(_olds) == len(_news), 'the body changed line count, so a paragraph boundary moved'
# every logged insertion and the one logged deletion, in the shapes the pass actually wrote them
_INS = {' ' + r['inserted'].strip() for r in log['restored'] if 'inserted' in r} | \
       {r['inserted'].strip() for r in log['restored'] if 'inserted' in r}
_DEL = {' ' + r['removed'] for r in log['body_repairs'] if 'removed' in r} | \
       {r['removed'] for r in log['body_repairs'] if 'removed' in r}
removed, extended = [], []
for _o, _n, _k in zip(_olds, _news, range(len(_olds))):
    if not _o.strip():
        continue
    if _o == _n or _o in _news:
        continue
    _ops = [x for x in difflib.SequenceMatcher(None, _o, _n).get_opcodes() if x[0] != 'equal']
    _ok = all((x[0] == 'insert' and _n[x[3]:x[4]] in _INS) or (x[0] == 'delete' and _o[x[1]:x[2]] in _DEL)
              for x in _ops)
    if _ok:
        extended.append({'line': _k + 1,
                         'edits': [f'{x[0]}:{len(_n[x[3]:x[4]] or _o[x[1]:x[2]])} chars' for x in _ops]})
    else:
        removed.append({'line': _k + 1, 'text': _o[:110],
                        'unexplained_edits': [f"{x[0]} {(_n[x[3]:x[4]] or _o[x[1]:x[2]])[:70]!r}"
                                              for x in _ops if not (
                                                  (x[0] == 'insert' and _n[x[3]:x[4]] in _INS) or
                                                  (x[0] == 'delete' and _o[x[1]:x[2]] in _DEL))]})
log['body_inclusion'] = {'v48_body_lines_absent_from_v49': len(removed), 'examples': removed[:6],
                         'v48_lines_carried_by_logged_edits_only': len(extended),
                         'edited_lines': extended,
                         'rule': 'a v48 body line may change only by a logged insertion or the one logged deletion'}
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

# ------------------------------------------------------------------ gate extracts, written every build
# The waiver gate reads three surfaces: the adaptation's raw front matter (the base as adopted, before
# repair), this build's front matter, and the previous line's. They were made by a scratch step once, and
# after the front matter changed under them the gate reported flag_count 0 about a file that was no
# longer the one being shipped. They are outputs of this build now, and the verifier checks the middle one
# against the shipped markdown before it believes the gate.
_cut = lambda s: s[:s.index('\n## 2. ')] if '\n## 2. ' in s else s
(D / 'v49_base_front_matter.md').write_text(ADAPT_RAW_FM)
(D / 'v49_front_matter.md').write_text(fm)
(D / 'v48_front_matter.md').write_text(_cut(v48))
log['gate_extract_bytes'] = {'base_as_adopted': len(ADAPT_RAW_FM), 'built': len(fm),
                             'previous_line': len(_cut(v48))}
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

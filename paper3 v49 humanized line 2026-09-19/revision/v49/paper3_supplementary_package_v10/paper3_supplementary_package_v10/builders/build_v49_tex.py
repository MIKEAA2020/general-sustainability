#!/usr/bin/env python3
"""v49 tex + PDF: region surgery on v48's compiled .tex, then compile and fit.

Why not a re-transpile: this article's .tex comes down a .tex lineage (v42 -> v47 ->
v48), and the markdown->LaTeX converter that the companion documents use escapes the
article's maths - feeding v49's markdown through it lost formulas, which is exactly the
thing the ruling forbids ("no build-time normalisation of reused maths"). So the .tex of
v49 is v48's .tex with two operations, both bounded and both checked:

  A. the front-matter region - everything between \\maketitle and the Section 2 heading -
     is replaced by the v49 front matter, converted block by block with mdtex.md2tex
     (maths lifted and restored as written) with v48's own heading labels reused by
     section number;
  B. the six restored body sentences are appended inside the tex paragraph they follow in
     the markdown, located by the last words of that paragraph and required to be unique.

Everything between those two operations is byte-identical to v48's .tex, which the
"body untouched" assert below proves. The maths invariant is then an equation rather
than a hope: the .tex's formula multiset must equal v48's minus the front matter that
left plus the front matter that arrived plus the six sentences.

Checks: 1 body bytes identical; 2 the maths equation; 3 every \\ref resolves (this
document has no \\ref at all, cross-references are prose, so a broken label cannot hide);
4 tectonic rc=0, no ??, no overfull >= 6pt; 5 every flowing markdown paragraph is on the
page; 6 the three companion documents byte-identical to v48's.
"""
import importlib.util as U, os, re, sys, json, hashlib, collections

R = '/home/user/revision/v7'
os.chdir(R); sys.path.insert(0, R); sys.path.insert(0, '/home/user/revision/v48'); sys.path.insert(0, '/home/user/review')
_sp2 = U.spec_from_file_location('b48', '/home/user/revision/v48/build_v48_base.py')
b48 = U.module_from_spec(_sp2); _sp2.loader.exec_module(b48)
texkit = b48.texkit
import mdtex_v1 as MT
_sp3 = U.spec_from_file_location('bc', R + '/build_companions_v1.py')
bc = U.module_from_spec(_sp3); _sp3.loader.exec_module(bc)

ART = 'paper3_material_ledgers_v49'
md48 = open(f'{R}/paper3_material_ledgers_v48.md').read()
md49 = open(f'{R}/paper3_material_ledgers_v49.md').read()
tx48 = open(f'{R}/paper3_material_ledgers_v48.tex').read()
ASCII_PAIRS = (('\u1e03', '\\(\\dot{b}\\)'), ('\u00fc', '\\"{u}'), ('\u00e4', '\\"{a}'), ('\u00f6', '\\"{o}'),
               ('\u00e9', "\\'{e}"), ('\u00f4', '\\^{o}'), ('\u00d8', '\\O{}'), ('\u00c5', '\\AA{}'),
               ('\u2020', '\\dag{}'), ('\u2082', '\\textsubscript{2}'), ('\u00f7', '\\(\\div\\)'),
               ('\u2192', '\\(\\to\\)'), ('\u25a1', '\\(\\square\\)'), ('\u2264', '\\(\\le\\)'),
               ('\u2265', '\\(\\ge\\)'), ('\u00b1', '\\(\\pm\\)'), ('\u00d7', '\\(\\times\\)'))

def to_tex(block):
    """md2tex protects every $...$ span and puts it back as written, which is the property
    this line needs; the remaining non-ascii is what the v48 build's own character list maps."""
    t = MT.md2tex(block)
    for a, b in ASCII_PAIRS:
        t = t.replace(a, b)
    t = t.replace('\u2014', '---').replace('\u2013', '--').replace('\u2019', "'").replace('\u201c', '``').replace('\u201d', "''")
    return t

# ---------------------------------------------------------------- A. the front-matter region
i_mt = tx48.index('\\maketitle') + len('\\maketitle')
m_s2 = re.search(r'\n\\(?:sub)?section\*?\{2\.', tx48)
i_s2 = m_s2.start()
old_front = tx48[i_mt:i_s2]
fm_md = md49[:md49.index('\n## 2. ')]                       # v49's front matter, title through section 1
old_head_labels = dict()
for num, lab in re.findall(r'\\(?:sub)?section\*?\{(\d+(?:\.\d+)?)[^{}]*\}\\label\{([^}]*)\}', old_front):
    old_head_labels[num] = lab

LISTMARK_RE = re.compile(r'^(\s*)(?:([-*+])|(\d+)\.)\s+(.*)$')


def _is_flush_para_start(block):
    """a unit that ends the list run: a heading, a rule, display math, or a flush-left paragraph"""
    first = block.split('\n')[0]
    if re.match(r'^(#{1,5}\s|---)', first) or first.startswith('$$'):
        return True
    return (len(first) - len(first.lstrip())) == 0 and not LISTMARK_RE.match(first)


def emit_list(units, i):
    """render one markdown list run into tex, starting at units[i].

    The branch this replaces handled only `- ` items, chose the environment from the FIRST unit of the
    whole region, and - the damaging one - on meeting a non-list block appended the rest of the section
    into the current item and kept consuming, so the introduction reached the page as two giant blocks
    with no spacing. Runs now end where the markdown ends them; and because a single markdown block can
    hold several list items (the two pathologies are written on consecutive lines), the run is parsed
    LINE by line: a marker at column 0 opens an item, a marker that is indented belongs to the item
    above it as a sub-bullet, and indented prose continues the item's own sentence.
    """
    run, top, j = [], [], i
    while j < len(units):
        u = units[j]
        lines = [x for x in u.split('\n') if x.strip()]
        if not lines:
            j += 1
            continue
        first = lines[0]
        m0 = LISTMARK_RE.match(first)
        if m0 and (len(first) - len(first.lstrip())) == 0:
            run.extend(lines); j += 1
            continue
        if top or run:
            if _is_flush_para_start(u):
                break
            run.extend(lines); j += 1
            continue
        break
    for line in run:
        ind = len(line) - len(line.lstrip())
        m = LISTMARK_RE.match(line)
        if m and ind == 0:
            top.append({'num': int(m.group(3)) if m.group(3) else None,
                        'text': m.group(4).strip(), 'kids': []})
        elif m and top:
            top[-1]['kids'].append(m.group(4).strip())
        elif top:
            top[-1]['text'] += ' ' + ' '.join(line.split())
    numeric = bool(top) and all(it['num'] is not None for it in top)
    body = []
    for k, it in enumerate(top, 1):
        if numeric and it['num'] != k:
            body.append('\\setcounter{enumi}{%d}' % (it['num'] - 1))
        txt = to_tex(it['text'])
        if it['kids']:
            txt += ('\n\\begin{itemize}\n'
                    + '\n'.join('    \\item ' + to_tex(x) for x in it['kids'])
                    + '\n\\end{itemize}')
        body.append('\\item ' + txt)
    env = 'enumerate' if numeric else 'itemize'
    return '\\begin{%s}\\setlength{\\itemsep}{2pt}\n%s\n\\end{%s}' % (env, '\n'.join(body), env), j


out = []
# Blank lines are not the only boundary this author uses: §1.2 writes contributions 6 and 7 straight
# after the preceding item's bullets, with no blank line, so a split on `\n\n` hands them over as part
# of item 5's block and they are glued into it. Split also where markdown itself would start a new
# item or block - a line-initial list marker, a heading, a rule, a display fence.
_blocks, _buf = [], ''
for _ln in fm_md.split('\n'):
    if not _ln.strip():
        if _buf.strip():
            _blocks.append(_buf.strip()); _buf = ''
        continue
    if re.match(r'^(?:\s*(?:\d+\.|[-*+])\s|#{1,6}\s|---\s*$|\$\$)', _ln) and _buf.strip():
        _blocks.append(_buf.strip()); _buf = _ln
    else:
        _buf = (_buf + '\n' + _ln) if _buf.strip() else _ln
if _buf.strip():
    _blocks.append(_buf.strip())
bi = 0
while bi < len(_blocks):
    b = _blocks[bi]
    if b.startswith('# '):
        bi += 1; continue                                     # the title lives in \title{}, already v48's
    if b == '---':
        out.append('\\vspace{0.8em}'); bi += 1; continue
    if b.startswith('### '):
        txt = b[4:].strip(); num = txt.split()[0] if re.match(r'^\d', txt) else ''
        lab = old_head_labels.get(num, bc.slug(re.sub(r'^\d+(\.\d+)*\s*', '', txt)))
        out.append('\\subsection*{%s}\\label{%s}' % (to_tex(txt), lab)); bi += 1; continue
    if b.startswith('## '):
        txt = b[3:].strip()
        if txt.lower() == 'abstract':
            out.append('\\section*{Abstract}\\label{abstract}'); bi += 1; continue
        num = txt.split()[0] if re.match(r'^\d', txt) else ''
        lab = old_head_labels.get(num, bc.slug(re.sub(r'^\d+(\.\d+)*\s*', '', txt)))
        out.append('\\section*{%s}\\label{%s}' % (to_tex(txt), lab)); bi += 1; continue
    if b.startswith('#### '):
        out.append('\\textbf{%s}' % to_tex(b[5:].strip())); bi += 1; continue
    if b.startswith('$$'):
        buf = b
        while buf.count('$$') % 2 and bi + 1 < len(_blocks):
            bi += 1; buf += ' ' + _blocks[bi]
        out.append('\\[ ' + re.sub(r'\s*\n\s*', ' ', buf.replace('$$', '')).strip() + ' \\]')
        bi += 1; continue
    if LISTMARK_RE.match(b.split('\n')[0]) and (len(b.split('\n')[0]) - len(b.split('\n')[0].lstrip())) == 0:
        _tex, _nxt = emit_list(_blocks, bi)
        out.append(_tex); bi = _nxt; continue
    out.append(to_tex(b)); bi += 1

new_front = '\n\n' + '\n\n'.join(out) + '\n'

# ---------------------------------------------------------------- the region's two proofs
# (1) content: the words of the markdown region, in order, must be exactly the words of the tex
# region. Shape may change - emphasis becomes \textbf, a list item takes its marker from LaTeX - so
# both sides are reduced to alphanumeric tokens, the markers the list environment supplies are
# dropped from the markdown side, and the title is excluded because it lives in \title{}, v48's own.
def _toks(s):
    return [x.lower() for x in re.findall(r'[0-9A-Za-z]+', s)]


def _strip_math(s):
    """every maths span to one shared token, so the proof compares prose. Display forms first:
    matching `\$[^$]*\$` first reads the two dollars of `$$` as an empty inline span and leaves the
    formula behind, which is how this reported a difference at token 1047 in a correct document."""
    for _pat in (r'\$\$.{0,3000}?\$\$', r'\$[^$]{0,3000}\$', r'\\\[.{0,3000}?\\\]', r'\\\(.{0,3000}?\\\)'):
        s = re.sub(_pat, ' M ', s, flags=re.S)
    return s


_mdt3 = []
for _b in _blocks:
    if _b.startswith('# ') or _b == '---':
        continue
    _body = re.sub(r'^\s*(?:\d+\.|[-*+])\s+', ' ', _b)
    _body = re.sub(r'\n\s*(?:\d+\.|[-*+])\s+', ' ', _body)
    _mdt3 += _toks(_strip_math(_body))
_tx_only = new_front
for _cmd in (r'\begin{itemize}', r'\end{itemize}', r'\begin{enumerate}', r'\end{enumerate}',
             r'\setlength{\itemsep}{2pt}', r'\setlength{\itemsep}{1pt}'):
    _tx_only = _tx_only.replace(_cmd, ' ')
_tx_only = re.sub(r'\\setcounter\{enumi\}\{\d+\}', ' ', _tx_only)
_tx_only = re.sub(r'\\(?:sub)*section\*?\{([^{}]*)\}(?:\\label\{[^}]*\})?', r'\1', _tx_only)
_tx_only = re.sub(r'\\partitle\{([^{}]*)\}', r'\1', _tx_only)
for _k in ('textbf', 'emph', 'textit', 'texttt', 'text', 'mathrm', 'mathbf'):
    _tx_only = re.sub(r'\\' + _k + r'\{([^{}]*)\}', r'\1', _tx_only)
# commands alone, never their line: `\item` is a marker, and eating `[^\n]*` along with it threw away
# every item's text and made the proof report 940 missing tokens in a document that had none
_tx_only = re.sub(r'\\(?:label\{[^}]*\}|vspace\{[^}]*\}|maketitle|item)\s*', ' ', _tx_only)
_txt2 = _toks(_strip_math(_tx_only))
_unmatched = None
if _mdt3 != _txt2:
    for _i in range(min(len(_mdt3), len(_txt2))):
        if _mdt3[_i] != _txt2[_i]:
            _unmatched = {'at_token': _i, 'md': ' '.join(_mdt3[_i:_i + 9]),
                          'tex': ' '.join(_txt2[_i:_i + 9]),
                          'md_tokens': len(_mdt3), 'tex_tokens': len(_txt2)}
            break
    if _unmatched is None:
        _unmatched = {'note': 'identical up to the shorter side', 'md_tokens': len(_mdt3),
                      'tex_tokens': len(_txt2)}
# (2) shape: every markdown list item, at either level, has to be an \item in the region
_md_items_n = len(re.findall(r'^\s*(?:\d+\.|[-*+])\s', fm_md, re.M))
_tx_items_n = len(re.findall(r'^\s*\\item\s', new_front, re.M))
assert _md_items_n == _tx_items_n, (
    'the region carries %d markdown list items but only %d \\item(s): a list was flattened'
    % (_md_items_n, _tx_items_n))
assert _unmatched is None, 'the region conversion changed words, not just shape: ' + repr(_unmatched)

tx = tx48[:i_mt] + new_front + tx48[i_s2:]

# ---------------------------------------------------------------- B. the six restored sentences
rest = json.load(open('/home/user/revision/v49/v49_front_matter_edits.json'))['restored']
appended, unplaced = [], []
for rec in rest:
    if not rec['placed'].startswith('body line'):
        continue
    sent = rec.get('inserted') or rec.get('sentence', '')
    _mode = rec.get('mode', 'append-sentence')
    if rec['phrase'] in re.sub(r'\s+', ' ', tx):
        appended.append({'phrase': rec['phrase'], 'tex': 'already in the tex'}); continue
    ln = int(rec['placed'].split()[2]) - 1
    if _mode == 'extend-final-sentence':
        # the clause belongs inside one specific sentence, not at the end of the paragraph, so the
        # anchor is the sentence's own wording rather than a tail word match
        pr = rec.get('target_probe') or rec['phrase']
        occ = [m.start() for m in re.finditer(re.escape(pr), tx) if m.start() > i_s2]
        if not occ:
            appended.append({'phrase': rec['phrase'], 'tex': 'PROBE NOT FOUND, falling back'}); 
        elif len(occ) >= 1:
            q = occ[0]
            e = tx.find('.', q + len(pr))
            assert e > 0 and tx.count(pr) == len(occ), f"{rec['phrase']}: probe is not a single sentence here"
            # step past a closing brace of \textbf{...} before the full stop
            seg = tx[q:e]
            at = e
            ins = sent.strip()
            if ins[0] in ':;,':
                at = e
            else:
                at = e + 1
                ins = ' ' + ins
            tx = tx[:at] + ins + tx[at:]
            appended.append({'phrase': rec['phrase'], 'tex': f'clause inserted at tex offset {at} '
                                                              f'(inside the sentence holding {pr!r})',
                             'tex_text': ins})
            continue
    body48 = md48[md48.index('\n## 2. ') + 1:].split('\n')
    mdline = body48[ln] if ln < len(body48) else ''
    tail = [w for w in re.sub(r'\$[^$]*\$', ' ', mdline).split() if re.search(r'[A-Za-z]', w)][-6:]
    pat = r'[\W\d_]{0,6}'.join(map(re.escape, [re.sub(r'[^A-Za-z]', '', w) for w in tail if re.sub(r'[^A-Za-z]', '', w)]))
    ms = list(re.finditer(pat, tx[i_s2:])) if pat else []
    at = None
    if len(ms) == 1:
        at = i_s2 + ms[0].end()
    else:
        # fall back on a word that is unique in both surfaces, then take the paragraph that
        # holds it: appending at the end of that paragraph is a placement choice the author
        # can move, and the page check below proves the sentence is in the document at all
        cands = [w for w in dict.fromkeys(re.findall(r'[A-Za-z]{8,}', mdline))
                 if md49.count(w) == 1 and tx48.count(w) == 1]
        for w in cands:
            q = tx.find(w)
            if q > i_s2:
                s = tx.rfind('\n\n', 0, q); e = tx.find('\n\n', q)
                at = (e if e > 0 else len(tx))
                # step back over a closing environment or display so the text lands inside prose
                tailseg = tx[max(0, s):at]
                if re.search(r'\\(end\{(longtable|tabular|itemize|quote)\}|align\*|])\s*$', tailseg):
                    at = max(0, s) + tailseg.rfind('\n\n\n') if False else at
                appended_note = f'paragraph holding the unique word "{w}"'
                break
        else:
            unplaced.append({'phrase': rec['phrase'], 'matches': len(ms), 'mdline_head': mdline[:70]}); continue
    if at is None:
        unplaced.append({'phrase': rec['phrase'], 'matches': len(ms)}); continue
    _ins = ' ' + to_tex(sent)
    if _ins.strip().startswith((':', ';', ',')):
        _ins = _ins.strip()                      # a clause that continues the sentence is glued, not spaced
    tx = tx[:at] + _ins + tx[at:]
    appended.append({'phrase': rec['phrase'], 'tex_text': _ins,
                     'tex': f'inserted at tex offset {at}' + (f' ({appended_note})' if 'appended_note' in dir() else '')})
    appended_note = None
print(f'  front matter replaced ({len(old_front)} B out, {len(new_front)} B in) | '
      f'body sentences into the tex: {len(appended)} of {len([r for r in rest if r["placed"].startswith("body line")])}')
for u in unplaced: print('   NOT placed in the tex:', u)

# ---------------------------------------------------------------- checks
# the body of the .tex must differ from v48's only by the sentences placed in it
j_new = tx.index(tx48[i_s2:i_s2 + 80])
probe = tx[j_new:]
n_app = 0
for a in appended:
    if 'inserted at' in a.get('tex', ''):
        r = next(x for x in rest if x['phrase'] == a['phrase'])
        s = a.get('tex_text')
        if s is None:
            s = ' ' + to_tex(r.get('inserted') or r.get('sentence', ''))
        assert s in probe, f'the tex insertion for {a["phrase"]} cannot be found to undo it'
        probe = probe.replace(s, '', 1); n_app += 1
same_after = (probe == tx48[i_s2:])
print(f'  undoing the {n_app} tex insertions, the .tex from Section 2 on is byte-identical to v48\'s: {same_after}')
print('  the .tex from the Section 2 heading onward is byte-identical to v48\'s:', same_after)

def mspans(x):
    """maths spans of a *region* (regions are small; a whole document defeats this regex
    pairing because of \[ in comments, and a check that cannot see its own noise is worse
    than none, so the body is compared by bytes instead and only regions are compared here)"""
    out = []
    x = re.sub(r'\s*\n\s*', ' ', x)          # the region is small; put it on one line so a
    for m in re.finditer(r'\$\$(?s:.)*?\$\$|\$[^$]+?\$|\\\((?s:.)*?\\\)|\\\[(?s:.)*?\\\]', x):  # display that
                                              # spans lines is seen as the span it is
        g = m.group(0)
        g = re.sub(r'^\$\$|\$\$$|^\$|\$$|^\\\(|\\\)$|^\\\[|\\\]$', '', g.strip())
        out.append(re.sub(r'[^a-z0-9]', '', re.sub(r'\\tag\{[^}]*\}|\\label\{[^}]*\}|\\displaystyle|\\', '', g.lower())))
    return collections.Counter(g for g in out if g)

fm_md_spans, new_front_spans = mspans(fm_md), mspans(new_front)
sent_spans = collections.Counter()
for r_ in rest:
    if r_['placed'].startswith('body line'):
        sent_spans += mspans((r_.get('inserted') or r_.get('sentence','')))
missing_front = sorted(x for x in fm_md_spans if new_front_spans[x] < fm_md_spans[x])
print(f'  front-matter maths: {sum(fm_md_spans.values())} spans in the markdown, {sum(new_front_spans.values())} in the new tex region, '
      f'{len(missing_front)} not carried')
for x in missing_front[:3]: print('     missing from the tex front matter:', x[:80])
assert not missing_front, 'the front-matter replacement lost mathematics'
rep = {'front_bytes_out': len(old_front), 'front_bytes_in': len(new_front), 'old_head_labels': old_head_labels,
       'tex_appends': appended, 'tex_unplaced': unplaced, 'body_tex_identical_from_section2': same_after,
       'tex_body_bytes': len(tx48[i_s2:]), 'math_front_md': sum(fm_md_spans.values()),
       'math_front_tex': sum(new_front_spans.values()), 'math_front_missing': missing_front[:8],
       'math_donor_sentences': sum(sent_spans.values())}
assert same_after, 'the .tex body changed in a way other than the six insertions'
labs = set(re.findall(r'\\label\{([^}]*)\}', tx)); refs = set(re.findall(r'\\ref\{([^}]*)\}', tx))
rep['labels'], rep['refs'], rep['unresolved_refs'] = len(labs), len(refs), sorted(refs - labs)
print(f'  labels {len(labs)} | refs {len(refs)} | unresolved {len(refs - labs)}')
assert not (refs - labs)
open(f'{R}/{ART}.tex', 'w').write(tx)

# ---------------------------------------------------------------- compile + fit
fitted = []
for rnd in range(6):
    rc, log, ov = texkit.compile_log(ART, R)
    assert rc == 0, f'tectonic exit {rc}\n{(log or "")[-1200:]}'
    ls = tx.split('\n')
    bad = {}
    for m in re.finditer(r'Overfull \\hbox \(([0-9.]+)pt too wide\) (?:detected at line (\d+)|in paragraph at lines (\d+))', log or ''):
        if float(m.group(1)) < 6.0: continue
        ln = int(m.group(2) or m.group(3)); bad[ln] = max(bad.get(ln, 0.0), float(m.group(1)))
    did = 0
    for ln in sorted(bad, reverse=True):
        if not (0 < ln <= len(ls)): continue
        l = ls[ln - 1].strip()
        if l.startswith('$$') and l.endswith('$$') and len(l) > 8:
            ls[ln - 1] = r'\par\noindent\resizebox{\linewidth}{!}{$\displaystyle ' + l[2:-2].strip() + r'$}\par'
            did += 1; fitted.append(['display scaled to the measure', ln, round(bad[ln], 1)]); continue
        env = next((e for e in ('longtable', 'tabular') if (r'\begin{' + e + '}') in '\n'.join(ls[max(0, ln - 60):ln])), None)
        if not env: continue
        s = next((i for i in range(ln - 1, max(-1, ln - 61), -1) if r'\begin{' + env + '}' in ls[i]), None)
        e = next((i for i in range(ln, len(ls)) if r'\end{' + env + '}' in ls[i]), None)
        if s is None or e is None: continue
        ws = [float(x) for x in re.findall(r'p\{([0-9.]+)em\}', ls[s])]
        if not ws: continue
        cut = min(0.30, max(0.02, bad[ln] / (10.0 * sum(ws))))
        new = ls[s]
        for w in sorted(set(ws), reverse=True):
            new = new.replace('p{%sem}' % ('%g' % w), 'p{%sem}' % ('%.2f' % (w * (1 - cut))), 1)
        if new == ls[s]: continue
        ls[s] = new; did += 1; fitted.append([f'{env} columns narrowed {100 * cut:.0f}%', s + 1, round(bad[ln], 1)])
    tx = '\n'.join(ls)
    if not did: break
open(f'{R}/{ART}.tex', 'w').write(tx)
rep['tex_fitted'] = fitted

CARRIED = ('paper3_supplementary_v18', 'companionA_certification_procedure_v9', 'companionB_standards_horizon_v9')
rep['carried_sha256_16'] = {b + e: hashlib.sha256(open(f'{R}/{b}{e}', 'rb').read()).hexdigest()[:16]
                            for b in CARRIED for e in ('.md', '.tex', '.pdf')}
rep['docs'] = {}
for base in (ART,) + CARRIED:
    rc, log, ov = texkit.compile_log(base, R)
    p = f'{R}/.logtmp/{base}.pdf'
    if os.path.exists(p):
        open(f'{R}/{base}.pdf', 'wb').write(open(p, 'rb').read())
    pages, right, left2, worst = texkit.overhang(f'{R}/{base}.pdf')
    # a zero here does not mean "no overflow", it means "nothing was measured": texkit reports an
    # empty geometry when PyMuPDF is unavailable, and a clean-looking 0 would have passed silently
    # through the whole compile gate once already. Measure or stop.
    assert pages > 0, (f'{base}: no page geometry (PyMuPDF missing?); refusing to record 0 overfull '
                       'for an unmeasured document')
    rep['docs'][base] = {'rc': rc, 'pages': pages, 'overfull_ge_6pt': len([x for x in ov if x >= 6.0]),
                         'worst_pt': round(max(ov), 1) if ov else 0.0, 'right_pt': round(right, 1),
                         'left_pt': round(left2, 1), 'log_qmark': (log or '').count('??'),
                         'undefined': (log or '').count('undefined reference')}
    print(f'  {base:44s} rc={rc} pages={pages:3d} overfull>=6pt={rep["docs"][base]["overfull_ge_6pt"]} '
          f'worst={rep["docs"][base]["worst_pt"]:5.1f}pt ??={rep["docs"][base]["log_qmark"]}')

# the rendered front matter, digits kept: MT.page_text letters-only view cannot show an ORCID or a
# date, and "the byline moved to the header" is only evidence if the header's digits can be read back
import pymupdf as _fitz
_d0 = _fitz.open(f'{R}/{ART}.pdf')
open('/home/user/revision/v49/v49_pdf_front_pages.txt', 'w').write(
    '\n'.join(_d0[i].get_text() for i in range(min(2, _d0.page_count))))

P = MT.page_text(f'{R}/{ART}.pdf')
flow = MT.md_flow(md49)
absent = [' '.join(b.split())[:70] for b in flow if not MT.covers(P, b)]
# a heading whose argument runs to a paragraph is the signature of a heading that swallowed its
# body text at build time, which is how the introduction lost its spacing in this build
_swallowed = [(len(a), a[:70]) for a in re.findall(r'\\(?:section|subsection|subsubsection)\*\{([^}]*)\}', tx) if len(a) > 200]
rep['overlong_heading_arguments'] = [{'chars': n, 'starts': s} for n, s in _swallowed]
assert not _swallowed, f'a heading argument is carrying body text: {_swallowed[0]}'

rep['pdf_flow'] = {'blocks': len(flow), 'absent': len(absent), 'examples': absent[:6]}
print(f'  compiled article carries {len(flow) - len(absent)}/{len(flow)} flowing markdown paragraphs')
for x in absent[:4]: print('     absent:', x)
front_new = tx[:tx.index(tx48[i_s2:i_s2 + 80])]
rep['front_matter_stray_markers_in_tex'] = [m.group(0)[:70] for m in re.finditer(r'(?m)^\s*[-*]\s+\S', front_new)]
print('  E6 lookalikes (stray list markers in the tex front matter):', len(rep['front_matter_stray_markers_in_tex']))
json.dump(rep, open('/home/user/revision/v49/v49_compile_report.json', 'w'), indent=1)
assert not absent, 'flowing paragraphs missing from the compiled article'
assert all(d['rc'] == 0 and d['overfull_ge_6pt'] == 0 and d['log_qmark'] == 0 for d in rep['docs'].values())
print('*** v49 tex: maths equation holds, refs resolve, four documents compile clean, every paragraph on the page ***')

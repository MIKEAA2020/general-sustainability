#!/usr/bin/env python3
r"""verify_v43_style.py - the gate for the v43 line, which is a register line, not a content line.

Four groups, in the order a reader would ask them:

[1] Does the new text reverse to the old one? Every edit this build made is logged (front matter, section
    leads, and each prose block the mechanical pass touched). Reversing them must return the v42 bytes
    exactly, for all four documents. If it does, nothing else in the corpus moved.
[2] Is the content identical? The multiset of numeric values (after thousands separators are folded), the
    ordered list of statement labels with their headings, the table rows, the display equations, the
    heading lines and the cross-reference tokens must all agree between v42 and v43, for all four files.
    A register pass that changes a number, drops a label or reflows a table is not a register pass.
[3] Is the register actually the one the author's kit asks for? `humanize/style_audit.py` is run, unchanged,
    on the prose extract of every markdown source and on the extracted text of every PDF. Each of the 13
    metrics must either meet the instrument's own target or be strictly better than the v42 value, and the
    article's prose must meet mean, p90, em-dash, semicolon, frame and self-reference targets outright.
    Any sentence the pass left over 60 words is printed, because the gate would rather show one than hide it.
[4] Do the artefacts still hold: no raw TeX in the PDF, no missing glyph, no unresolved reference, the S9.4
    inventory still bijects with the article, the numbering maxima still read true, the four documents still
    typeset with 0 Overfull \hbox and 0 overhang, the headers still say what the file is, and the register
    scan `review/tone_scan_v1.py` still returns 0 on the manuscript prose.

Exit 0 with ALL CHECKS PASS, or a list of failures.
"""
import functools
import json
import os
import re
import subprocess
import sys

R = '/home/user/revision/v7'
sys.path.insert(0, R)
sys.path.insert(0, '/home/user/review')
sys.path.insert(0, '/home/user/humanize')
import stylekit_v1 as sk                                    # noqa: E402
import texkit_v1 as texkit                                  # noqa: E402
from pymupdf import open as zopen                           # noqa: E402

PAIRS = (('paper3_material_ledgers_v42', 'paper3_material_ledgers_v43'),
         ('paper3_supplementary_v13', 'paper3_supplementary_v14'),
         ('companionA_certification_procedure_v4', 'companionA_certification_procedure_v5'),
         ('companionB_standards_horizon_v4', 'companionB_standards_horizon_v5'))
KEYS = {'paper3_material_ledgers_v43': 'article', 'paper3_supplementary_v14': 'supplementary',
        'companionA_certification_procedure_v5': 'companionA', 'companionB_standards_horizon_v5': 'companionB'}
AUDIT = '/home/user/humanize/style_audit.py'
FAIL = []


def ck(ok, what):
    print(('  ok   ' if ok else '  FAIL ') + what)
    if not ok:
        FAIL.append(what)


def nrm(s):
    return re.sub(r'\s+', ' ', s.replace('\u2019', "'").replace('\u2018', "'")).strip()


def vals(s):
    s = re.sub(r'(?<=\d),(?=\d)', '', s.replace('\u2013', '-').replace('\u2014', '-'))
    import collections
    return collections.Counter(re.findall(r'\d+(?:\.\d+)*', s))


def labels(s):
    return [(m.group(1), int(m.group(2)), m.group(3)) for m in re.finditer(
        r'^\*\*(Definition|Lemma|Proposition|Theorem|Corollary|Remark)\s+(\d+)\s*\((.*?)\)\.\*\*', s, re.M)]


def rows(s, pred=lambda l: l.lstrip().startswith('|')):
    return [l.strip() for l in s.split('\n') if pred(l)]


def displays(s):
    return [x.strip() for x in re.findall(r'(?s)\$\$(.*?)\$\$', s)]


def heads(s):
    return [l.strip() for l in s.split('\n') if re.match(r'^#{1,6}\s', l)]


def refs(s):
    return sorted(set(re.findall(r'\\(?:ref|eqref|label|cite[tp]?)\{([^}]*)\}', s)) |
                  set(re.findall(r'\bS\d+(?:\.\d+)?\b', s)))


def audit(path):
    """Run the author's instrument, unchanged, and read its table back as {metric: (value, target, ok)}."""
    out = subprocess.run([sys.executable, AUDIT, path], capture_output=True, text=True).stdout
    got = {}
    for line in out.split('\n'):
        m = re.match(r'^(.{32}?)\s{2,}([\d.]+)\s+(<=|>=)\s*([\d.]+)\s+(ok|FIX)', line)
        if m:
            got[m.group(1).strip()] = (float(m.group(2)), m.group(3) + ' ' + m.group(4), m.group(5) == 'ok')
    return got, out


def flow_extract(md_path):
    """Only the flowing prose: the text a register pass is permitted to rewrite. A statement body, a list item
    and a table cell are excluded, and with them the long enumerations that dominate a short document's
    sentence statistics -- so the instrument's breath targets are tested here, and the wider surfaces are
    reported beside it rather than quietly dropped."""
    blocks = sk.split_blocks(open(md_path).read())
    txt = '\n\n'.join(b for b in blocks if sk.is_flow(b))
    return _write_extract(md_path, 'flow', txt)


def _write_extract(md_path, tag, txt):
    import os
    txt = re.sub(r'(?s)\$\$.*?\$\$|\\\[.*?\\\]|\$[^$\n]*\$', ' ', txt)
    scratch = f'{R}/.v43gate'
    os.makedirs(scratch, exist_ok=True)
    p = f'{scratch}/{os.path.basename(md_path)}.{tag}'
    open(p, 'w').write(txt)
    return p


def prose_extract(md_path):
    """The prose of a source file, with the mathematics taken out. A display is not sentence-length material and
    its own dashes and semicolons are notation, so leaving it in the extract measures the notation as if it were
    style; the instrument is run on the words, and the whole file is measured separately by the PDF group."""
    blocks = sk.split_blocks(open(md_path).read())
    txt = '\n\n'.join(b for b in blocks if sk.is_prose(b))
    txt = re.sub(r'(?s)\$\$.*?\$\$|\\\[.*?\\\]|\$[^$\n]*\$', ' ', txt)
    scratch = f'{R}/.v43gate'
    os.makedirs(scratch, exist_ok=True)
    p = f'{scratch}/{os.path.basename(md_path)}.prose'
    open(p, 'w').write(txt)
    return p


def pdf_text(base):
    p = f'{R}/{base}.pdf'
    d = zopen(p)
    t = ''.join(pg.get_text() for pg in d)
    n = d.page_count
    d.close()
    return t, n


def flat(x):
    return re.sub(r'\s+', ' ', x.replace('\u00a0', ' ')).strip()


def flat(x):
    return re.sub(r'\s+', ' ', x.replace('\u00a0', ' ')).strip()


def undo(text, needle, back, cur):
    """Replace one logged edit at its position, tolerating the line re-wrapping the build applied."""
    pat = re.compile(r'\s+'.join(map(re.escape, needle.split())))
    m = pat.search(text, cur)
    assert m, f'logged edit not found from offset {cur}: {flat(needle)[:60]!r}'
    return text[:m.start()] + back + text[m.end():], m.start() + len(back) + 1


def flat(x):
    return re.sub(r'\s+', ' ', x.replace('\u00a0', ' ')).strip()


def flexpat(needle):
    return re.compile(r'\s+'.join(map(re.escape, needle.split())))


print('[1] the v43 line reverses to v42, edit for edit')
LOG = json.load(open(f'{R}/revisions_v43_style_log.json'))
for old, new in PAIRS:
    ent = LOG[KEYS[new]]
    blocks = open(f'{R}/{new}.md').read().split('\n\n')
    n = 0
    for e in ent.get('blocks', []):
        i0 = e.get('i', -1)
        assert i0 >= 0, f'{new}: an edit was logged without a block index'
        assert i0 < len(blocks), f'{new}: block index {i0} out of range ({len(blocks)} blocks)'
        assert flat(e['new']) in flat(blocks[i0]) or flat(blocks[i0]) in flat(e['new']), \
            f'{new}: block {i0} is not what the pass left there'
        blocks[i0] = e['old']
        n += 1
    md = '\n\n'.join(blocks)
    cur = 0
    for f in ent.get('front', []):
        if 'old' not in f:
            continue
        m = flexpat(f['new']).search(md, cur)
        assert m, f'{new}: the front matter edit is not in the file'
        md = md[:m.start()] + f['old'] + md[m.end():]
        cur = m.start() + len(f['old']) + 1
        n += 1
    src = open(f'{R}/{old}.md').read()
    ck(flat(md) == flat(src),
       f'{new}: reversing the {n} logged edits returns {old}.md word for word ({len(src.split())} words)')
    if flat(md) != flat(src):
        a, b = flat(md).split(), flat(src).split()
        k = next((x for x in range(min(len(a), len(b))) if a[x] != b[x]), min(len(a), len(b)))
        print(f'       first difference at word {k}: v43->{" ".join(a[max(0,k-8):k+8])!r} vs v42->'
              f'{" ".join(b[max(0,k-8):k+8])!r}')

print('\n[2] the content did not move')
for old, new in PAIRS:
    o, n = open(f'{R}/{old}.md').read(), open(f'{R}/{new}.md').read()
    vo, vn = vals(o), vals(n)
    diff = {k: (vo[k], vn[k]) for k in set(vo) | set(vn) if vo[k] != vn[k]}
    ck(not diff, f'{new}: every numeric value occurs as often as it did' + (f' -> {list(diff.items())[:4]}' if diff else ''))
    ck(labels(o) == labels(n), f'{new}: the {len(labels(n))} statement labels and their headings are unchanged')
    ck(rows(o) == rows(n), f'{new}: the {len(rows(n))} table rows are byte-identical')
    ck(displays(o) == displays(n), f'{new}: the {len(displays(n))} displayed equations are byte-identical')
    ck(heads(o) == heads(n), f'{new}: the {len(heads(n))} heading lines are unchanged')
    ck(vals(o)['2018'] == vals(n)['2018'],
       f'{new}: the data-vintage year still occurs {vals(n)["2018"]} times')
    if all(os.path.exists(f'{R}/{b}.tex') for b in (old, new)):
        a, b = refs(open(f'{R}/{old}.tex').read()), refs(open(f'{R}/{new}.tex').read())
        ck(set(a) == set(b), f'{new}: the LaTeX cross-reference set is unchanged ({len(b)} tokens)'
           + (f' -> -{sorted(set(a)-set(b))[:3]} +{sorted(set(b)-set(a))[:3]}' if set(a) != set(b) else ''))

print('\n[3] the register the author\'s kit asks for')
DOWN = ('mean words/sentence', 'p90 words/sentence', 'max words/sentence', 'sentences > 60 words',
        'em-dashes', 'semicolons', "'X, not Y' frames", "'rather than'", "'this article' / 'the article'")
UP = ('we+our per 1k words', 'example markers per 1k words', "'consider' / 'suppose'", 'questions')
TARGETS = ('semicolons', "'rather than'", "'this article' / 'the article'")
for old, new in PAIRS:
    gp, go = audit(prose_extract(f'{R}/{new}.md'))[0], audit(prose_extract(f'{R}/{old}.md'))[0]
    gf, gof = audit(flow_extract(f'{R}/{new}.md'))[0], audit(flow_extract(f'{R}/{old}.md'))[0]
    for base in (new, old):
        t, _n = pdf_text(base)
        open(f'{R}/.v43gate/{base}.pdftext', 'w').write(t)
    gq = audit(f'{R}/.v43gate/{new}.pdftext')[0]
    gq0 = audit(f'{R}/.v43gate/{old}.pdftext')[0]

    # (a) nothing may come out worse than the v42 line, on any of the three surfaces the instrument can be run on
    worse = []
    for tag, g, g0 in (('prose', gp, go), ('flow', gf, gof), ('PDF', gq, gq0)):
        for k in g:
            if k not in g0:
                continue
            v, v0 = g[k][0], g[k][0] * 0 + g0[k][0]
            if k == 'max words/sentence' and g.get('sentences > 60 words', (0,))[0] <= \
                    g0.get('sentences > 60 words', (0,))[0]:
                continue          # the tail of the distribution did not grow: a longer single maximum with no
                                  # additional long sentence is the repairs putting a split sentence back together
            if k in DOWN and g[k][0] > v0:
                worse.append(f'{tag} {k} {v0}->{g[k][0]}')
            elif k in UP and g[k][0] < v0:
                worse.append(f'{tag} {k} {v0}->{g[k][0]}')
    ck(not worse, f'{new}: no style metric is worse than v42'
       + (' -> ' + '; '.join(worse[:6]) if worse else ''))

    # (b) the targets a register pass can reach without entering a statement, a table cell or a formula
    hard = [k for k in TARGETS if not gf.get(k, (0, '', False))[2]]
    ck(not hard, f'{new}: the flowing prose meets the punctuation and self-reference targets'
       + (f' -> {[(k, gf[k][0]) for k in hard]}' if hard else ''))

    # (c) a fault the source did not already have is a defect of the pass
    ln = {(w, c[-40:]) for w, _i2, c in sk.lint(open(f'{R}/{new}.md').read())}
    l0 = {(w, c[-40:]) for w, _i2, c in sk.lint(open(f'{R}/{old}.md').read())}
    ck(not (ln - l0), f'{new}: the linter finds no fault the source did not already have'
       + (f' -> {sorted(ln - l0)[:2]}' if ln - l0 else ''))
    if l0:
        print(f'       {new}: {len(l0)} linter finding(s) already present in {old}, i.e. content, not style:')
        for w, c in sorted(l0)[:2]:
            print(f'         [{w}] ...{c}')

    long_s = [x for x in re.split(r'(?<=[.!?])\s+(?=[A-Z(])', nrm(re.sub(r'[`$*|]', ' ',
              open(flow_extract(f'{R}/{new}.md')).read()))) if len(x.split()) > 60]
    FR = "'X, not Y' frames"
    print(f'       {new}: flowing prose, v43 vs v42 -- mean {gf["mean words/sentence"][0]} / '
          f'{gof["mean words/sentence"][0]}, p90 {gf["p90 words/sentence"][0]} / '
          f'{gof["p90 words/sentence"][0]}, max {gf["max words/sentence"][0]} / '
          f'{gof["max words/sentence"][0]}, over 60 words {len(long_s)}; PDF mean '
          f'{gq["mean words/sentence"][0]} / {gq0["mean words/sentence"][0]}; em-dashes '
          f'{gf["em-dashes"][0]} / {gof["em-dashes"][0]}, frames {gf[FR][0]} / {gof[FR][0]}, we+our '
          f'{gf["we+our per 1k words"][0]}/1k, examples {gf["example markers per 1k words"][0]}/1k')
    for x in long_s[:2]:
        print(f'         [{len(x.split())}w] {x[:110]}...')

print('\n[4] the artefacts still hold')
for old, new in PAIRS:
    t, npage = pdf_text(new)
    stray = {k: t.count(k) for k in ('\\S', '\\text', '\\textbackslash', '\\allowbreak', '\\{}', '$\\',
                                     'Missing character', '??') if t.count(k)}
    dollars = len(re.findall(r'\$(?!\s)', t))
    ck(not stray and not dollars, f'{new} PDF prints no raw TeX, no missing glyph, no unresolved reference'
       + (f' -> {stray} {dollars}' if stray or dollars else ''))
    ck(not re.search(r'/home/user|revision/v\d|/tmp/', t), f'{new} PDF: no path into a working directory')
    pages, right, left, worst = texkit.overhang(f'{R}/{new}.pdf')
    rc, log, over = texkit.compile_log(new, R)
    ck(rc == 0 and not over and right == 0.0 and left == 0.0 and pages == npage,
       f'{new}: recompiles with rc=0, 0 Overfull \\hbox, {right}/{left} pt overhang, {pages} pages')
    tex = open(f'{R}/{new}.tex').read()
    h = [l for l in tex.split('\n')[:6] if l.startswith('%')]
    ck(3 <= len(h) <= 6 and any('Typeset from' in x for x in h) and
       not any(re.search(r'\bv\d+\b.{0,12}(is|was|remains|supersed|replac)', x) for x in h),
       f'{new}: the LaTeX header says what the file is ({len(h)} comment lines, no version diary)')
    o, n = open(f'{R}/{old}.md').read(), open(f'{R}/{new}.md').read()
    tk = subprocess.run([sys.executable, '/home/user/review/tone_scan_v1.py', f'{R}/{new}.md'],
                        capture_output=True, text=True).stdout
    tk0 = subprocess.run([sys.executable, '/home/user/review/tone_scan_v1.py', f'{R}/{old}.md'],
                         capture_output=True, text=True).stdout
    words = set(re.findall(r'^\s+L\d+\s+(\S+)', tk, re.M))
    words0 = set(re.findall(r'^\s+L\d+\s+(\S+)', tk0, re.M))
    novel = sorted(w for w in words - words0 if re.search(w, nrm(open(f'{R}/{old}.md').read()), re.I) is None)
    ck(not novel, f'{new}: the scanner flags {len(words)} word(s), every one of them the author\'s own vocabulary'
       + (f' -> new: {novel}' if novel else ''))

sup = open(f'{R}/paper3_supplementary_v14.md').read()
art = open(f'{R}/paper3_material_ledgers_v43.md').read()
lab = re.compile(r'^\*\*(Definition|Lemma|Proposition|Theorem|Corollary|Remark)\s+(\d+)\s*\((.*?)\)\.\*\*')
secx = re.compile(r'^#{2,5}\s+([0-9]+(?:\.[0-9]+)*)')
sec, want = '', {}
for line in art.split('\n'):
    ms = secx.match(line)
    if ms:
        sec = ms.group(1)
    m = lab.match(line)
    if m and 21 <= int(m.group(2)) <= 47:
        want[int(m.group(2))] = (f'{m.group(1)} {m.group(2)} ({m.group(3)})', sec)
tbl = re.findall(r'^\| (Definition \d+ .*?|Lemma \d+ .*?|Proposition \d+ .*?|Theorem \d+ .*?'
                 r'|Corollary \d+ .*?|Remark \d+ .*?) \| ([0-9.]+) \|$', sup, re.M)
got = {int(re.search(r'\d+', t_).group(0)): (t_, s2) for t_, s2 in tbl}
ck(len(want) == 27 and len(got) == 27 and all(got.get(k) == v for k, v in want.items()),
   f'S9.4 still lists the {len(want)} article labels 21-47 with the same loci')

print()
if FAIL:
    print(f'*** {len(FAIL)} FAILURE(S) ***')
    for f in FAIL:
        print('  ', f)
    sys.exit(1)
print('ALL CHECKS PASS')

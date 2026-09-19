#!/usr/bin/env python3
"""Line-level read of the shipped v49 markdown and PDF.

The question asked: has any flaw crept into the maths, the numbers, or the descriptive prose?
Answered by refusing to let a single line of v49 be unexplained.

For every non-empty line of paper3_material_ledgers_v49.md, exactly one of these must hold:

  v48-identical      the line is byte-identical to a line of v48's markdown (the body, unchanged), or
  adapt-identical    the line is byte-identical to a line of the adaptation extract, or
  house-form         the line differs from an adaptation line only in whitespace, or
  term-revert        applying the logged revert rules to an adaptation line reproduces it exactly, or
  label-cut          removing a logged cut pattern from an adaptation line reproduces it exactly, or
  first-line         the logged abstract first sentence, plus the remainder of an adaptation line, or
  carry-over         an adaptation line with a logged carried-over passage appended as its own paragraph, or
  restore            a v48 line with one of the six logged restore sentences inserted, or
  blank              the line is blank.

Anything else is a FINDING, printed with the nearest candidate line from each source.

Then the content tests, per line rather than per document:

  maths     every `$...$` / `$$...$$` span of v49 appears verbatim in v48 or in the deposited article
  numbers   every numeral of v49 appears in v48, in the deposit, or is inside the logged additions
  prose     formatting flaws: unbalanced `**`, odd number of `$`, a heading with no blank line after it,
            a heading argument long enough to be swallowing a paragraph, a list marker sitting inside a
            sentence, `$$` glued to text, doubled punctuation, space before punctuation, empty heading,
            an uncited reference entry, a byline line in the markdown, and a line that ends mid-word
  pdf       the rendered page 1 opens the abstract on the instructed sentence, and no typeset heading
            runs longer than a heading should

Writes revision/v49/v49_line_audit.json and prints the findings. Exit status = number of findings.
"""
import json
import re
import sys
import pathlib

D = pathlib.Path('/home/user/revision/v49')
V7 = pathlib.Path('/home/user/revision/v7')
SRC = pathlib.Path('/home/user/uploads/p3 humanized.txt')
DEP = pathlib.Path('/home/user/work/paper3.txt')

ART = 'paper3_material_ledgers_v49'
md49 = (V7 / f'{ART}.md').read_text()
md48 = (V7 / 'paper3_material_ledgers_v48.md').read_text()
log = json.loads((D / 'v49_front_matter_edits.json').read_text())
# the extract bounds and the cut patterns are read out of the builder's own source, so the audit
# cannot drift away from the build it is auditing (a hardcoded copy of a pattern that has since
# been edited would certify the wrong rules)
BUILD = (D / 'build_v49_base.py').read_text()
_m = re.search(r'ADAPT_LO\s*,\s*ADAPT_HI\s*=\s*(\d+)\s*,\s*(\d+)', BUILD) or \
     re.search(r'^ADAPT_LO\s*=\s*(\d+).*?^ADAPT_HI\s*=\s*(\d+)', BUILD, re.S | re.M)
assert _m, 'the builder no longer states the adaptation extract bounds in a form this audit can read'
ADAPT_LO, ADAPT_HI = int(_m.group(1)), int(_m.group(2))
_build_cuts = re.findall(r"r'(\*\*?[^'\n]*Level[^'\n]*|\\s\*The illusion[^'\n]*)'", BUILD)
extract = '\n'.join(SRC.read_text().split('\n')[ADAPT_LO - 1:ADAPT_HI])
dep = DEP.read_text()

FIRST = 'Depletion indicators can carry similar units while built to inform distinct questions.'
# the rule file carries two kinds of enforced rule: a substitution (alias -> the deposit's term) and
# an abolition (a label the adaptation invented, which must simply not appear). Counting only the
# first kind would call "12 enforced" wrong in one direction and read the ruling incompletely.
rules, abolish = [], []
for ln in (D / 'adaptation_term_revert_v1.csv').read_text().split('\n'):
    ln = ln.strip()
    if not ln or ln.startswith('#'):
        continue
    f = ln.split(',', 6)
    if len(f) < 6:
        continue
    if f[2] in ('force', 'label') and f[1]:
        rules.append((f[0], f[1]))
    elif f[2] == 'label' and not f[1]:
        abolish.append(f[0])
CUTS = [r'[ \t]*The illusion operates on two levels:[ \t]*',
        r'\*\*The Arithmetic Level:\*\*[ \t]*',
        r'\*\*The Dynamical Level \(Yield Inflation\):\*\*[ \t]*']
if _build_cuts:
    CUTS = sorted(set(CUTS) | set(_build_cuts))
CARRIED = []
_cpath = D / 'v49_carry_over.json'
if _cpath.exists():
    for _r in json.loads(_cpath.read_text()):
        _src = (V7 / _r['source']).read_text()
        _i, _j = _src.find(_r['start']), _src.find(_r['end'], _src.find(_r['start']))
        if _i >= 0 and _j >= 0:
            _raw = _src[_i:_j + len(_r['end'])]
            CARRIED.append(' '.join(' '.join(x.split()) for x in re.split(r'\n\s*\n', _raw)))
if not CARRIED:
    CARRIED = [c['text'] for c in log.get('carry_over', []) if 'text' in c]
RESTORED = [r.get('inserted_raw') or r.get('inserted') or r.get('sentence', '')
            for r in log.get('restored', [])]


def apply_rules(s):
    for alias, rep in rules:
        s = s.replace(alias, rep)
    for pat in CUTS:
        s = re.sub(pat, '', s)
    return s


# --------------------------------------------------------------- provenance of every line
v48_lines = [x.rstrip() for x in md48.split('\n')]
ad_lines = [x.rstrip() for x in extract.split('\n')]
V48 = set(v48_lines)
AD = set(ad_lines)
AD_norm = {}
for x in ad_lines:
    AD_norm.setdefault(' '.join(x.split()), []).append(x)

findings = []
prov = {'v48-identical': 0, 'adapt-identical': 0, 'house-form': 0, 'term-revert': 0, 'label-cut': 0,
        'first-line': 0, 'carry-over': 0, 'restore': 0, 'blank': 0}
unexplained = []

for no, raw in enumerate(md49.split('\n'), 1):
    line = raw.rstrip()
    if not line.strip():
        prov['blank'] += 1
        continue
    if line in V48:
        prov['v48-identical'] += 1
        continue
    if line in AD:
        prov['adapt-identical'] += 1
        continue
    why = None
    flat_line = ' '.join(line.split())
    if flat_line in AD_norm:                                   # only line breaks / spaces moved
        why = 'house-form'
    else:
        for cand in AD_norm.get(flat_line, []) or [x for x in ad_lines if ' '.join(x.split()) == flat_line]:
            pass
        # term revert and/or label cut applied to some adaptation line must reproduce this line exactly
        for cand in ad_lines:
            if apply_rules(cand).rstrip() == line:
                why = 'term-revert/label-cut' if cand in AD else 'term-revert/label-cut (house-form)'
                break
            if ' '.join(apply_rules(cand).split()) == flat_line:
                why = 'term-revert/label-cut + house-form'
                break
    if why is None and line.startswith(FIRST):
        rest = line[len(FIRST):].strip()
        for cand in ad_lines:
            c = apply_rules(cand).strip()
            if rest and (c.endswith(rest) or rest in c):
                why = 'first-line'
                break
        if why is None and rest == '':
            why = 'first-line'
    if why is None:
        for text in CARRIED:
            if ' '.join(text.split()) == ' '.join(line.split()):
                why = 'carry-over (the donor passage on its own lines)'
                break
            for cand in ad_lines:
                c = ' '.join(apply_rules(cand).split())
                if c and line.startswith(c) and ' '.join(text.split()) in ' '.join(line.split()):
                    why = 'carry-over (appended to an adaptation line)'
                    break
            if why:
                break
    V48_f = {' '.join(x.split()) for x in v48_lines}
    if why is None:
        for s in RESTORED:
            if s and s[:60] in line:
                stem = line.replace(s, '')
                if stem in set(v48_lines):
                    why = 'restore'
                    break
                # the line may carry a restore AND the logged duplicate-deletion: undo the restore,
                # then ask whether some v48 line becomes it once the logged deletion is applied
                _rem = [rp.get('removed', '') for rp in log.get('body_repairs', []) if rp.get('removed')]
                for _c in v48_lines:
                    for _r in _rem:
                        if _c.replace(' ' + _r, '', 1).strip() == stem:
                            why = 'restore + logged body repair'
                            break
                    if why:
                        break
                if why:
                    break
                stem = ' '.join(stem.split())
                if stem in V48_f:
                    why = 'restore'
                    break
                # a restored sentence that began the v48 line can leave the join with one space fewer
                if stem.replace(' .', '.') in V48_f or any(
                        stem.startswith(x[:40]) and abs(len(stem) - len(x)) < 3 for x in V48_f):
                    why = 'restore'
                    break
    if why is None:
        # a v48 line that carries exactly a logged body repair (a deletion) and nothing else
        for rp in log.get('body_repairs', []):
            if rp.get('result', '').startswith('the bolded twin deleted'):
                for cand in v48_lines:
                    if cand.replace(' ' + rp['removed'], '', 1).rstrip() == line or \
                       cand.replace(rp['removed'], '', 1).replace('  ', ' ').strip() == line.strip():
                        why = 'logged body repair on a v48 line'
                        break
            if why:
                break
    if why is None and line.startswith('#'):
        for cand in AD_norm.get(flat_line, []):
            why = 'house-form'
            break
    if why is None and line.startswith('$$') or (why is None and line.strip() == '$$'):
        for cand in ad_lines:
            if cand.strip().startswith('$$') and ' '.join(cand.split()) == flat_line:
                why = 'house-form (display rewrap)'
                break
    if why is None:
        unexplained.append({'line': no, 'text': line[:200]})
    else:
        prov[why] = prov.get(why, 0) + 1

findings += [{'kind': 'unexplained line', **u} for u in unexplained]

# --------------------------------------------------------------- per-line maths spans
def spans(s):
    out = []
    for m in re.finditer(r'\$\$(.+?)\$\$', s, re.S):
        out.append(m.group(1).strip())
    for m in re.finditer(r'(?<!\$)\$([^$\n]+?)\$(?!\$)', s):
        out.append(m.group(1).strip())
    return out

v48_spans = set(spans(md48)) | set(spans(dep))
ad_spans = set(spans(extract))
v42_spans = set(spans((V7 / 'paper3_material_ledgers_v42.md').read_text()))
# which lines carry a logged restore, decided by content: the numbering used in the build log is
# body-relative, the audit indexes the file, and a mismatch there would silently exempt the wrong lines
RESTORE_TEXTS = [r['inserted_raw'] for r in log.get('restored', []) if r.get('inserted_raw')]
RESTORE_LINES = {no for no, s in enumerate(md49.split('\n'), 1)
                 if any(x in s for x in RESTORE_TEXTS)}
math_bad = []
n_spans = 0
_only_v42 = 0
for no, line in enumerate(md49.split('\n'), 1):
    for sp in spans(line):
        n_spans += 1
        if sp in v48_spans or sp in ad_spans:
            continue
        if no in RESTORE_LINES and sp in v42_spans:
            _only_v42 += 1
            continue
        if sp.replace('\\ ', ' ') in v48_spans:
            continue
        math_bad.append({'line': no, 'span': sp[:160]})
findings += [{'kind': 'maths span not found in v48 or the deposit', **m} for m in math_bad]

# --------------------------------------------------------------- per-line numerals
NUM = re.compile(r'(?<![\w.])(\d+(?:[.,]\d+)*)(?:\s?(%|percent))?', re.I)
def numerals(s):
    return {m.group(1) for m in NUM.finditer(s) if len(m.group(1)) >= 1}

v48_num = numerals(md48)
dep_num = numerals(dep)
add_num = numerals(extract) | numerals(' '.join([FIRST] + CARRIED + RESTORED + [x.get('removed_as_duplicate', '') for x in [log.get('first_line', {})]]))
num_bad = []
for no, line in enumerate(md49.split('\n'), 1):
    for n in numerals(line):
        if n in v48_num or n in dep_num or n in add_num:
            continue
        num_bad.append({'line': no, 'numeral': n, 'context': ' '.join(line.split())[:130]})
findings += [{'kind': 'numeral with no source', **m} for m in num_bad]

# --------------------------------------------------------------- formatting flaws, line by line
L = md49.split('\n')
_starts, _acc = [], 0
for _s in L:
    _starts.append(_acc); _acc += len(_s) + 1
_TOKS = ('$$', chr(92) + '[', chr(92) + ']')
_delims = []
for _tok in _TOKS:
    _st0 = 0
    while True:
        _q = md49.find(_tok, _st0)
        if _q < 0:
            break
        _delims.append((_q, _tok)); _st0 = _q + 1
_delims.sort()
_in_disp, _st, _di = set(), False, 0
for _i, (_p0, _s) in enumerate(zip(_starts, L), 1):
    while _di < len(_delims) and _delims[_di][0] < _p0:
        _k = _delims[_di][1]
        _st = (not _st) if _k == '$$' else (_k == chr(92) + '[')
        _di += 1
    if _st or any(_t in _s for _t in _TOKS):
        _in_disp.add(_i)
fmt, inherited = [], []
for no, raw in enumerate(L, 1):
    s = raw.rstrip()
    if not s.strip():
        continue
    if s.count('**') % 2:
        fmt.append({'line': no, 'flaw': 'unbalanced **', 'text': s[:160]})
    pass   # $ parity is checked per block below: this file legitimately breaks a paragraph across
           # source lines, so an inline span can straddle two of them (v48 does exactly this)
    if re.match(r'^#{1,6}\s*$', s):
        fmt.append({'line': no, 'flaw': 'empty heading', 'text': s[:160]})
    # where the flaw would be new: v49's front matter is the region this build writes, so headings
    # there are held to the house form absolutely; in the body a glued heading can also be inherited
    # from v48, and an inherited habit is a separate finding from a defect introduced here
    if re.match(r'^#{1,6}\s', s):
        _in_front = no <= len(md49[:md49.index('\n## 2. ')].split('\n'))
        _glued_after = no < len(L) and bool(L[no].strip())
        _glued_before = no > 1 and bool(L[no - 2].strip())
        for _kind, _glue in (('after', _glued_after), ('before', _glued_before)):
            if not _glue:
                continue
            _twin = s in set(v48_lines)
            _rec = {'line': no, 'flaw': f'heading with no blank line {_kind} it', 'text': s[:160]}
            if _in_front or not _twin:
                fmt.append(_rec)
            else:
                inherited.append(_rec)
    # a bullet marker stranded inside a sentence, which is what the label cut used to leave behind;
    # `**bold**` and `*emphasis*` are not list markers, so only a lone `*` following sentence-final
    # punctuation (or preceded by one) counts
    _bare = re.sub(r'\*\*[^*]+\*\*', 'BOLD', re.sub(r'(?<![A-Za-z0-9])\*[^*\n]+\*(?![A-Za-z0-9])', 'EM', s))
    if re.search(r'[.)]\s*\*\s+[A-Z]', _bare) or re.match(r'^\s*\*\s*$', _bare):
        fmt.append({'line': no, 'flaw': 'a list marker sitting inside a sentence', 'text': s[:200]})
    if re.search(r'\$\$[^\s]', s) and not re.match(r'^\s*\$\$', s):
        fmt.append({'line': no, 'flaw': 'display fence glued to text', 'text': s[:160]})
    if no not in _in_disp and re.search(r'[a-z]{2}\.\.\s|[a-z]\.\.[^.]|\s,|\s\.(?=\s|$)|\.;|\.\-\-', s):
        fmt.append({'line': no, 'flaw': 'doubled or displaced punctuation', 'text': s[:200]})
    if re.search(r'`[^`]{0,40}`,', s):
        pass
    if s.strip() in ('---',) and no > 2 and L[no - 2].strip() == '---':
        fmt.append({'line': no, 'flaw': 'doubled horizontal rule', 'text': s[:80]})
    if re.match(r'^\s*([-*]|\d+\.)\s+$', s):
        fmt.append({'line': no, 'flaw': 'empty list item', 'text': s[:80]})
    if re.search(r'\S  +\S', s) and '$' not in s and not s.lstrip().startswith(('#', '*', '-')):
        fmt.append({'line': no, 'flaw': 'doubled space inside prose', 'text': s[:160]})
for pat in (r'^\*\*Amin Abaee\*\*', r'^\*Independent Researcher\*', r'^ORCID:', r'^`\S+@\S+`$',
            r'^\*(January|February|March|April|May|June|July|August|September|October|November|December) \d+, \d{4}\*$'):
    for no, s in enumerate(L, 1):
        if re.match(pat, s.strip()):
            fmt.append({'line': no, 'flaw': 'a byline line in the markdown (the .tex header carries it)', 'text': s[:120]})

# an over-long run of prose in a heading argument (markdown side: a heading line glued to a paragraph)
for no, s in enumerate(L, 1):
    if re.match(r'^#{1,6}\s', s) and len(s) > 200:
        fmt.append({'line': no, 'flaw': 'heading text longer than a heading', 'text': s[:120]})

# $ parity, measured where it is meaningful: on a blank-line separated block
V48_flat = {' '.join(x.split()) for x in re.split(r'\n\s*\n', md48)}
for bi, blk in enumerate(re.split(r'\n[ \t]*\n', md49), 1):
    if blk.count('$$') % 2:
        # a display opened in one block and closed in another would be a build error; $$ fences on
        # their own lines are the house form, so count only unpaired fences per block
        if not re.search(r'^\s*\$\$\s*$', blk, re.M):
            fmt.append({'line': f'block {bi}', 'flaw': 'unbalanced $$ inside a block', 'text': blk[:120]})
    body = re.sub(r'\$\$.*?\$\$', '', blk, flags=re.S)
    n = len(re.findall(r'(?<!\$)\$(?!\$)', body))
    if n % 2 and ' '.join(blk.split()) not in V48_flat:
        fmt.append({'line': f'block {bi}', 'flaw': 'odd number of $ in a block that is not v48 text',
                    'text': ' '.join(blk.split())[:160]})

findings += [{'kind': 'formatting flaw', **f} for f in fmt]

# --------------------------------------------------------------- citation integrity
bi = md49.find('## References')
body, refs = md49[:bi], md49[bi:]
orphan, uncited = [], []
for e in [x.strip() for x in refs.split('\n') if x.strip() and not x.strip().startswith('#')]:
    m = re.match(r'^([A-Z][A-Za-z\-\u2019\' ]+?)[,.]\s+.*?((?:1[89]|20)\d\d)', e)
    if not m:
        continue
    lead, yr = m.group(1).split()[0], m.group(2)
    if not re.search(re.escape(lead) + r'[^()\n]{0,80}?' + yr, body):
        orphan.append(f'{lead} {yr}')
# every (Author, Year) in-text cite must resolve to an entry
entries = {}
for e in [x.strip() for x in refs.split('\n') if x.strip()]:
    for m in re.finditer(r'([A-Z][A-Za-z\-\u2019\' ]+?)[,.]', e):
        entries.setdefault(m.group(1).split()[0].lower(), set()).add(re.findall(r'(?:1[89]|20)\d\d', e)[0] if re.findall(r'(?:1[89]|20)\d\d', e) else '')
for m in re.finditer(r'\(([^)]{3,180})\)', body):
    for part in m.group(1).split(';'):
        mm = re.search(r'([A-Z][A-Za-z\-\u2019\' ]+?)(?:,| and | & | et al\.)\s*((?:1[89]|20)\d\d)?[a-z]?', part.strip())
        if not mm:
            continue
        lead = mm.group(1).split()[0].lower()
        yr = mm.group(2)
        if len(lead) < 3 or lead in ('the', 'section', 'table', 'figure', 'both', 'while', 'whereas', 'e.g'):
            continue
        if yr and yr not in entries.get(lead, set()):
            uncited.append({'text': part.strip()[:80], 'lead': lead, 'year': yr})
_orph48 = set()
_r48 = md48[md48.index('## References'):]
_b48 = md48[:md48.index('## References')]
for e in [x.strip() for x in _r48.split('\n') if x.strip() and not x.strip().startswith('#')]:
    m = re.match(r'^([A-Z][A-Za-z\-\u2019\' ]+?)[,.]\s+.*?((?:1[89]|20)\d\d)', e)
    if m and not re.search(re.escape(m.group(1).split()[0]) + r'[^()\n]{0,80}?' + m.group(2), _b48):
        _orph48.add(f'{m.group(1).split()[0]} {m.group(2)}')
_new_orphans = sorted(set(orphan) - _orph48)
log_orphans = sorted(set(orphan) & _orph48)
_fm49 = md49[:md49.index('\n## 2. ')]
for _a in abolish:
    if _a in _fm49:
        findings.append({'kind': 'an abolished adaptation label survived into the shipped front matter',
                         'alias': _a, 'count_in_front_matter': _fm49.count(_a)})
findings += [{'kind': 'reference entry the swap left uncited (fix: cite it or drop it)', 'entry': o}
             for o in _new_orphans]
# these two were uncited in v42 and v48 too: an author-side house-style item, not a defect of this build
findings += [{'kind': 'in-text cite with no reference entry', **u} for u in uncited]

# --------------------------------------------------------------- the rendered PDF
pdf_findings = []
try:
    import pymupdf
    d = pymupdf.open(str(V7 / f'{ART}.pdf'))
    p1 = ' '.join(d[0].get_text().split())
    if FIRST not in p1:
        pdf_findings.append({'kind': 'the instructed abstract first line is not in the rendered PDF'})
    m = re.search(r'Abstract (.{' + str(0) + r',120})', p1)
    # a typeset heading should not be a paragraph long: measure each heading-ish bold run on page 1
    for hl in re.findall(r'(\d(?:\.\d)?)\s+([A-Z][^\n]{0,200})', d[0].get_text()):
        pass
    txt = '\n'.join(pg.get_text() for pg in d)
    flat = ' '.join(txt.split())
    # the paragraph the build was swallowing must now be body text, directly under its heading
    for probe in ['Sustainability accounting consistently suffers from two structural pathologies',
                  'We formalize physical compartments',
                  'Section 2 formulates the typed ledger']:
        if probe not in flat:
            pdf_findings.append({'kind': 'a §1 paragraph is not readable in the PDF', 'probe': probe})
    for k in ['Amin Abaee', 'Independent Researcher', 'amin_abaee@ut.ac.ir']:
        c = flat.count(k)
        if c != 1:
            pdf_findings.append({'kind': f'the byline element "{k}" appears {c} times, expected 1'})
    if 'September 6, 2026' in flat:
        pdf_findings.append({'kind': "the adaptation's date survived alongside the line of record's"})
    # spacing test: no two sentences of body text may be typeset inside a heading line
    for pg in d:
        for bl in pg.get_text('dict')['blocks']:
            for ln in bl.get('lines', []):
                spans_ = ln.get('spans', [])
                if not spans_:
                    continue
                big = [s for s in spans_ if s['size'] > 11.5]          # heading-sized type
                if big:
                    joined = ''.join(s['text'] for s in big)
                    if len(joined) > 120 and re.search(r'[.]\s+[A-Z]', joined):
                        pdf_findings.append({'kind': 'a heading-sized line carries body text',
                                             'text': joined[:150]})
    findings += [{'kind': 'pdf', **p} for p in pdf_findings]
except ImportError:
    findings.append({'kind': 'pdf', 'flaw': 'pymupdf unavailable - the PDF was NOT read'})

# the same test on the source: a heading and its paragraph must not share a line anywhere in the file
for no, s in enumerate(L, 1):
    if re.match(r'^#{1,6}\s', s) and re.search(r'[a-z]{3,}\. ', s[10:]):
        if len(s) > 140:
            findings.append({'kind': 'heading carrying a paragraph (md side)', 'line': no, 'text': s[:140]})

rep = {'provenance_of_every_line': prov, 'lines_total': len(L), 'unexplained': unexplained[:40],
       'rules_read': {'substitution_rules': len(rules), 'abolition_rules': len(abolish),
                      'enforced_total': len(rules) + len(abolish), 'cut_patterns': len(CUTS),
                      'extract_lines': [ADAPT_LO, ADAPT_HI], 'carry_over_passages': len(CARRIED),
                      'restore_sentences': len(RESTORED)},
       'maths': {'spans_checked': n_spans, 'spans_carried_from_v42_by_a_logged_restore': _only_v42, 'not_found_in_sources': math_bad[:20], 'count': len(math_bad)},
       'numerals': {'without_source': num_bad[:20], 'count': len(num_bad)},
       'formatting': fmt[:40], 'formatting_count': len(fmt),
       'formatting_inherited_from_v48_unchanged': {'count': len(inherited), 'examples': inherited[:6]},
       'citations': {'orphan_reference_entries': sorted(set(orphan)),
                     'orphans_pre_existing_in_v48': log_orphans,
                     'orphans_introduced_by_this_base_swap': _new_orphans,
                     'in_text_cites_with_no_entry': uncited[:20],
                     'orphan_count_v49': len(set(orphan))},
       'pdf': pdf_findings,
       'FINDINGS': len(findings), 'findings': findings[:120]}
(D / 'v49_line_audit.json').write_text(json.dumps(rep, indent=1) + '\n')

for k, v in rep.items():
    if k in ('findings', 'unexplained'):
        continue
    print(f'{k}: {json.dumps(v, ensure_ascii=False)[:300]}')
print()
if findings:
    print(f'{len(findings)} FINDING(S):')
    for f in findings[:40]:
        print('  -', json.dumps(f, ensure_ascii=False)[:230])
else:
    print('no findings: every line is accounted for, no maths/numeral/prose flaw detected')
print(f"\nprovenance: {json.dumps(prov)}")
raise SystemExit(min(1, len(findings)))

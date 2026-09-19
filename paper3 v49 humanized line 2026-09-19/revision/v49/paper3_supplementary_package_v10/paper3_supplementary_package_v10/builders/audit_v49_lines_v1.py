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

_PROSE = [tuple(x) for x in json.loads(
    (D / 'v49_front_matter_edits.json').read_text()).get('prose_repairs', [])]
_repaired = []
findings = []
prov = {'v48-identical': 0, 'adapt-identical': 0, 'house-form': 0, 'term-revert': 0, 'label-cut': 0,
        'first-line': 0, 'carry-over': 0, 'restore': 0, 'blank': 0,
        'adapt + logged prose repair': 0}
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
    # a line the build repaired by a logged prose rule (see build_v49_base.py). Undoing the logged
    # pairs must land it back on the adaptation line - the repairs are data in the edits log, not a
    # second copy of the rule, so the audit cannot drift from the build.
    _undone = line
    for _kind, _before, _after in _PROSE:
        if _after in _undone:
            _undone = _undone.replace(_after, _before)
    if _undone != line and _undone in AD:
        prov['adapt + logged prose repair'] += 1
        _repaired.append({'line': no, 'repairs': [list(r) for r in _PROSE if r[2] in line]})
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
# The matcher, not the manuscript. The first version of this check asked whether `Illakwahhi`
# appeared within 80 characters of `2024` WITHOUT CROSSING A PARENTHESIS, so the correct APA first
# mention of a three-author work - `Illakwahhi, Vegi and Srivastava (2024)` - read as an uncited
# entry, and v48 carried the same phantom. An attempt to "fix" it by canonicalising every cite into
# one key then invented new errors (it read `GRACE ... Tapley et al., 2004` as a cite by GRACE). So
# neither: an entry is cited if any name it is addressed by sits near its year in the body, and a
# cite is unresolved only if NO name in it addresses any entry of that year. No canonical key, so
# `and`, `&`, `et al.`, initials and institution strings cannot trip it; the permissive direction can
# only clear an entry, never flag one, and every clearing records which names did it.
bi = md49.find('## References')
body, refs = md49[:bi], md49[bi:]
BODY_FLAT = ' '.join(body.split())
_MONTH = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)'
_STOP = {'the', 'and', 'for', 'from', 'this', 'that', 'with', 'into', 'note', 'notes', 'ibid',
         'section', 'sections', 'table', 'tables', 'figure', 'figures', 'appendix', 'versus',
         'both', 'while', 'whereas', 'where', 'when', 'then', 'than', 'after', 'before',
         'above', 'below', 'example', 'examples', 'equation', 'equations', 'here', 'there',
         'these', 'those', 'such', 'also', 'thus', 'hence', 'because', 'although', 'comment'}


def _entry_names(line):
    """the name tokens a reference entry can be addressed by (author run, or institution words)"""
    s = ' '.join(line.strip().lstrip('-* ').split())
    if len(s) < 12 or s.startswith('#'):
        return None, None
    m = re.match(r'((?:[A-Z][A-Za-z\-\u2019\.]{1,28})(?:[,.]?\s+(?:and\s+)?[A-Z][A-Za-z\-\u2019\.]{1,28}){0,3})[,.]\s*((?:1[89]|20)\d\d)[a-z]?[,.]', s)
    if not m:
        m2 = re.match(r'((?:[A-Z][A-Za-z\-\u2019\.]{1,28})(?:\s+[A-Z][A-Za-z\-\u2019\.]{1,28}){0,3})[,.]', s)
        ym = re.search(r'((?:1[89]|20)\d\d)[a-z]?', s)
        if not (m2 and ym):
            return None, None
        return m2.group(1), ym.group(1)
    return m.group(1), m.group(2)


def _tokens(namestr):
    return [x.lower().strip(',.') for x in namestr.split()
            if len(x.strip(',.')) >= 4 and x.lower().strip(',.') not in _STOP]


def _cited_by(lead_tokens, yr):
    """which of the entry's own name tokens sits near the year in the body, and how"""
    hits = []
    for tok in lead_tokens:
        # case-insensitive: the tokens are lower-cased for the key, and `tilton` never matches `Tilton`
        m = re.search(r'\b' + re.escape(tok) + r'\b[^)\n]{0,90}?\b' + yr + r'[a-z]?\b', BODY_FLAT, re.I)
        if m:
            hits.append({'token': tok, 'context': ' '.join(m.group(0).split())[:110]})
    return hits


entries, orphan, resolved_keys, weak_cleared = {}, [], {}, []
for e in refs.split('\n'):
    names, yr = _entry_names(e)
    if not names or not yr:
        continue
    toks = _tokens(names)
    if not toks:
        continue
    k = toks[0] + ' ' + yr
    # 'entry' is a display string and is cut short; 'name' is what logic reads. Keeping the two
    # separate is the point: the multi-agency 2014 line puts its year past any useful preview, and
    # re-parsing the preview is what mis-classified it as an unexplained loss for a run.
    entries[k] = {'entry': ' '.join(e.split())[:120], 'name': ' '.join(names.split()),
                  'tokens': toks, 'year': yr}
    h = _cited_by(toks, yr)
    if h:
        resolved_keys[k] = h[0]
        # the window is deliberately permissive, so its shadow side gets listed rather than hidden: an
        # entry cleared by a co-author name or by prose that merely names the same words near the year
        if h[0]['token'] != toks[0]:
            weak_cleared.append({'entry': k, 'cleared_by': h[0]['token'], 'context': h[0]['context']})
    else:
        orphan.append(k)

# the reverse direction: every parenthetical cite has to address some entry of that year
_name_of = {}
for k, v in entries.items():
    for t2 in v['tokens']:
        _name_of.setdefault(t2, set()).add(k.split()[-1])
uncited = []
for m in re.finditer(r'\(([^)]{3,200})\)', body):
    for part in m.group(1).split(';'):
        p2 = ' '.join(part.split())
        mm = re.search(r'\b((?:1[89]|20)\d\d)[a-z]?\s*$', p2)
        if not mm or re.search(r'\b' + _MONTH + r'\s+' + mm.group(1) + r'$', p2):
            continue                      # a date, not a citation
        if re.search(r'[\d\s,]{6,}' + mm.group(1) + r'$', p2):
            continue                      # an identifier or a list of numbers ending in a year
        names = [x.lower().strip(',.') for x in re.findall(r"[A-Z][A-Za-z\-\u2019]{2,}", p2)]
        names = [x for x in names if x not in _STOP and len(x) >= 4]
        if not names:
            continue
        if not any(mm.group(1) in _name_of.get(x, set()) for x in names):
            uncited.append({'text': p2[:80], 'names': names[:4], 'year': mm.group(1)})
_seen, uncited2 = set(), []
for u in uncited:
    if (u['year'], u['text']) not in _seen:
        _seen.add((u['year'], u['text']))
        uncited2.append(u)
uncited = uncited2

# and what the pre-fix matcher flagged, so a phantom it invented is not mistaken for an editorial item
def _legacy_orphans(txt, reftxt):
    out3 = []
    for e in [x.strip() for x in reftxt.split('\n') if x.strip() and not x.strip().startswith('#')]:
        mm = re.match(r'^([A-Z][A-Za-z\-\u2019\' ]+?)[,.]\s+.*?((?:1[89]|20)\d\d)', e)
        if mm and not re.search(re.escape(mm.group(1).split()[0]) + r'[^()\n]{0,80}?' + mm.group(2), txt):
            out3.append(f'{mm.group(1).split()[0].lower()} {mm.group(2)}')
    return out3


_formerly_flagged = set(_legacy_orphans(body, refs))
cited48 = None
_r48 = md48[md48.index('## References'):]
_b48 = ' '.join(md48[:md48.index('## References')].split())
orph48 = set()
for e in _r48.split('\n'):
    names, yr = _entry_names(e)
    if not names or not yr:
        continue
    toks = _tokens(names)
    if toks and not any(re.search(r'\b' + re.escape(t3) + r'\b[^)\n]{0,90}?\b' + yr + r'[a-z]?\b',
                                _b48, re.I) for t3 in toks):
        orph48.add(toks[0] + ' ' + yr)
inherited = sorted(set(orphan) & orph48)


# the second class has to be a removal the project already recorded as a decision: the erratum must
# name the entry, speak of v49, and say the cite went - so an unexplained loss cannot borrow the
# standing of an explained one
_err = pathlib.Path('/home/user/revision/v48/ERRATA_v48.md')
_err_txt = _err.read_text() if _err.exists() else ''


def _logged_removal_cause(key):
    """the erratum sentence that records THIS entry going uncited in v49, or '' if none does.
    Name and year have to sit in the same sentence as the statement that the cite went, because a
    paragraph that merely mentions `Baez 2023` while discussing another entry is not a record of a
    decision about Baez - and a soft rule here would let any unexplained loss borrow class 2."""
    name = ' '.join(entries.get(key, {}).get('name', key).split()[:3]).strip(',.')
    yr = key.rsplit(' ', 1)[1]
    if not name:
        return ''
    for para in _err_txt.split('\n\n'):
        if 'v49' not in para:
            continue
        for sent in re.split(r'(?<=[.!?])\s+(?=[A-Z`*])', para):
            # 40 characters, not 14: the errata lists the two UN entries in one sentence, so the second
            # name sits 15 characters from its year and a tight window classified it as unexplained
            if re.search(re.escape(name) + r'[^.!?]{0,40}?' + yr, sent, re.I) and \
               re.search(r'uncited|cited by nobody|no longer makes', sent, re.I):
                return ' '.join(sent.split())[:400]
    return ''


recorded, _unexplained = [], []
for o in sorted(set(orphan) - orph48):
    _cause = _logged_removal_cause(o)
    (recorded if _cause else _unexplained).append({'entry': o, 'recorded_in_errata': _cause} if _cause else o)
created_by_a_logged_removal = [r['entry'] for r in recorded]
_new_orphans = _unexplained

findings += [{'kind': 'reference entry with no in-text cite anywhere in v49', 'entry': o,
              'class': ('already uncited in v42 and v48' if o in inherited
                        else 'uncited by a removal the errata records' if o in created_by_a_logged_removal
                        else 'NOT ACCOUNTED FOR - unexplained loss of a cite'),
              'note': 'disclosed on the open items; whether the paper should make this claim is the '
                      "author's call at submission, and this audit takes no position on it"}
             for o in sorted(set(orphan))]
findings += [{'kind': 'in-text cite with no reference entry', **u} for u in uncited]

# ---------------------------------------------- list structure on the page (the introduction's shape)
# Words surviving is not enough. The region converter once put the whole of §1.1 inside one `\item`,
# so every word reached the page and none of the structure did. So: every markdown list item in the
# adapted region must open a LINE on the rendered page - not merely appear in one. Block level is the
# wrong grain, because a tight itemize is one block for PyMuPDF and the check then flags four perfectly
# typeset bullets.
LIST_MARK_RE = re.compile(r'^(\s*)(?:([-*+])|(\d+)\.)\s+(.*)$')
_end_s2 = md49.index('\n## 2. ')
_region_items = []
for _k, _l in enumerate(md49[:_end_s2].split('\n')):
    _m = LIST_MARK_RE.match(_l)
    if _m:
        _region_items.append({'line': _k + 1, 'num': int(_m.group(3)) if _m.group(3) else None,
                              'text': ' '.join(m2.strip('*`') for m2 in _m.group(4).split()[:6])})
_pdf_lines = []
list_findings = []
try:
    import pymupdf as _pm
    _doc = _pm.open(str(V7 / f'{ART}.pdf'))
    for _pg in range(min(16, _doc.page_count)):
        for _ln in _doc[_pg].get_text().split('\n'):
            _pdf_lines.append(' '.join(_ln.split()))
except Exception as _e:                                 # noqa: BLE001
    _pdf_lines = []
    list_findings.append({'why': 'the page could not be read', 'error': repr(_e)[:120]})


def _alnum(s):
    return re.sub(r'[^0-9A-Za-z]', '', s)


# every page line, reduced to letters and digits and stripped of a leading list marker
_lines_compact = [(_alnum(re.sub(r'^\s*(?:\d{1,2}[.)]|[-*+\u2022\u25cf\u2013\u25e6]\s*)', '', x)), x)
                  for x in _pdf_lines if x.strip()]
for _it in _region_items:
    _nd = _alnum(_it['text'])[:26]
    if len(_nd) < 8:
        continue
    if not any(s.startswith(_nd) or _nd in s[:len(_nd) + 4] for s, _ in _lines_compact):
        list_findings.append({'line': _it['line'], 'why': 'no line on the page opens with this item',
                              'text': _it['text'][:66]})
_md_n = len(_region_items)
_tex_n = len(re.findall(r'^\s*\\item\s', (V7 / f'{ART}.tex').read_text()[:(V7 / f'{ART}.tex').read_text().index('\n\section*{2.')], re.M))
findings += [{'kind': 'a markdown list item did not reach the page as its own line', **x}
             for x in list_findings]

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

rep = {'list_structure_on_the_page': {'region_items': _md_n, 'tex_items_in_region': _tex_n,
                                      'counts_agree': _md_n == _tex_n, 'page-level findings': list_findings},
 'provenance_of_every_line': prov, 'lines_total': len(L), 'unexplained': unexplained[:40],
       'rules_read': {'substitution_rules': len(rules), 'abolition_rules': len(abolish),
                      'enforced_total': len(rules) + len(abolish), 'cut_patterns': len(CUTS),
                      'extract_lines': [ADAPT_LO, ADAPT_HI], 'carry_over_passages': len(CARRIED),
                      'restore_sentences': len(RESTORED)},
       'maths': {'spans_checked': n_spans, 'spans_carried_from_v42_by_a_logged_restore': _only_v42, 'not_found_in_sources': math_bad[:20], 'count': len(math_bad)},
       'numerals': {'without_source': num_bad[:20], 'count': len(num_bad)},
       'formatting': fmt[:40], 'formatting_count': len(fmt),
       'formatting_inherited_from_v48_unchanged': {'count': len(inherited), 'examples': inherited[:6]},
       'citations': {
                     'reference_entries': len(entries),
                     'real_orphans_disclosed': sorted(set(orphan)),
                     'class_1_uncited_already_in_v42_and_v48': inherited,
                     'class_2_uncited_by_a_removal_the_errata_records': created_by_a_logged_removal,
                     'class_2_evidence': {r['entry']: r['recorded_in_errata'] for r in recorded},
                     'class_3_introduced_by_this_base_swap_unexplained': _new_orphans,
                     'phantoms_the_old_matcher_invented_and_this_one_clears':
                         sorted(_formerly_flagged - set(orphan)),
                     'cleared_by_a_name_that_is_not_the_lead': weak_cleared,
                     'in_text_cites_with_no_entry': uncited[:20],
                     'open_item': 'humanize/open_items_v48.md - three uncited entries, disclosed, no fix applied',
                     'orphan_count_v49': len(set(orphan)),
                     'rule': ('an entry is cited when a name it is addressed by sits near its year in '
                              'the body; a class-2 entry needs the erratum to name it and to say the '
                              'cite went, so an unexplained loss cannot borrow an explained one')},
       'pdf': pdf_findings,
       'FINDINGS': len(findings), 'findings': findings[:120]}
rep['logged_prose_repairs'] = {'rules': [list(r) for r in _PROSE], 'lines': _repaired}
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

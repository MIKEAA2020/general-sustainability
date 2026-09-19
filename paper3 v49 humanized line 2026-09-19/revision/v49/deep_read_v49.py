#!/usr/bin/env python3
"""A line-level read of v49 for errors in maths, numbers and prose.

Deliberately NOT re-running the provenance checks (those prove nothing was lost); this one looks
forward instead of backward: for things that are internally wrong in v49 itself, in the surfaces the
earlier passes did not open - every rendered PDF page against the markdown digit by digit, run-on
sentence boundaries, heading and appendix numbering, display-equation labels against the prose that
quotes them, dollar-sign spacing that would print a literal `$`, and cross-references to tables,
figures and appendices that do not exist.

Each check prints what it looked at so an artifact of the check itself can be told apart from a
defect in the document.
"""
import pathlib
import re
import sys
from collections import Counter

V7 = pathlib.Path('/home/user/revision/v7')
MD = (V7 / 'paper3_material_ledgers_v49.md').read_text()
T = (V7 / 'paper3_material_ledgers_v49.tex').read_text()
L = MD.split('\n')
REPORT = {}


def note(k, v):
    REPORT[k] = v
    print(f'{k}: {v if not isinstance(v, list) else str(len(v)) + " -> " + str(v[:6])}')


# ---------------------------------------------------------------- the digit census, md against every PDF page
def numset(s):
    return set(re.findall(r'\d[\d,.\u2212\u2013-]*\d|\d', s))


def numlist(s):
    return Counter(re.findall(r'\d[\d,.\u2212\u2013-]*\d|\d', s))


note('md_numeric_tokens', len(numlist(MD)))
try:
    import pymupdf
    d = pymupdf.open(str(V7 / 'paper3_material_ledgers_v49.pdf'))
    pdftxt = '\n'.join(pg.get_text() for pg in d)
    P = numset(pdftxt)
    # de-TeX the markdown's math so a rendered form is compared with a rendered form
    m2 = MD.replace('{', '').replace('}', '').replace(r'\,', '').replace(r'\!', '').replace(r'\;', '')
    m2 = re.sub(r'\\(?:mathrm|mathbf|mathcal|text|operatorname|left|right)\b', ' ', m2)
    m2 = re.sub(r'\\[a-zA-Z]+', ' ', m2)
    M = numset(m2)
    # a numeral can legitimately change shape: 10^5 prints as 105, a range 1--2 prints as 1–2
    def shape_variants(t):
        out = {t, t.replace(',', '').replace('.', '')}
        if re.fullmatch(r'\d+', t):
            out.add(t)
        return out
    missing = [t for t in sorted(M - P) if not any(v in P for v in shape_variants(t))]
    note('numerals_in_md_not_on_any_pdf_page', missing[:14])
    extra = sorted(P - M)[:14]
    note('numerals_on_pdf_pages_not_in_md', extra)
    note('pdf_pages', len(d))
except Exception as e:                                     # noqa: BLE001
    note('pdf_census_error', repr(e)[:160])

# ---------------------------------------------------------------- run-on and spacing, line by line
runon, dblspace, dolspace = [], [], []
for i, l in enumerate(L, 1):
    s = l.strip()
    if not s or s.startswith(('|', '#', '>', '$$')):
        continue
    plain = re.sub(r'\$[^$]*\$', ' M ', s)
    if re.search(r'[^.!?]\s+\*\*[A-Z]', plain) and not re.search(r'[:;,]\s+\*\*', plain):
        runon.append({'line': i, 'text': plain[-150:]})
    if '  ' in plain.replace('* ', '').replace('- ', ''):
        m = re.search(r'\S {2,}\S', plain)
        if m:
            dblspace.append({'line': i, 'at': m.group(0)[:20]})
    if re.search(r'\$\s|\s\$', s) and '$$' not in s:
        dolspace.append({'line': i, 'text': s[:120]})
note('sentences_ending_without_punctuation_before_bold', runon[:8])
note('double_spaces_inside_a_line', dblspace[:8])
note('dollar_sign_adjacent_to_space_would_print_literally', dolspace[:8])

# ---------------------------------------------------------------- headings: numbering must be a path
heads = []
for i, l in enumerate(L, 1):
    m = re.match(r'^(#{2,5})\s+(?:(\d+(?:\.\d+)*)[.)]?\s*)?(.*)$', l)
    if m:
        heads.append({'line': i, 'depth': len(m.group(1)), 'num': m.group(2) or '', 'text': m.group(3)[:60]})
bad_seq, seen = [], {}
for h in heads:
    if not h['num']:
        continue
    parts = h['num'].rstrip('.').split('.')
    if any(not p.isdigit() for p in parts):
        bad_seq.append({'line': h['line'], 'num': h['num'], 'why': 'not dotted integers'})
        continue
    parent = '.'.join(parts[:-1])
    if parent and parent not in seen and not h['num'].startswith('References'):
        bad_seq.append({'line': h['line'], 'num': h['num'], 'why': 'no parent section ' + parent})
    seen[h['num'].rstrip('.')] = h['line']
note('heading_numbers_that_are_not_a_valid_path', bad_seq[:10])
dupnum = [n for n, c in Counter(h['num'] for h in heads if h['num']).items() if c > 1]
note('duplicate_heading_numbers', dupnum[:8])

# ---------------------------------------------------------------- cross-references resolve to something
refs = Counter()
for m in re.finditer(r'\b(?:Section|Appendix|Table|Figure|Theorem|Corollary|Lemma|Proposition|Equation|Eq\.|Remark|Definition)\s+([A-Z]?\d+(?:\.\d+)*[a-z]?)', MD):
    refs[m.group(1)] += 1
targets = set(seen) | {h['text'] for h in heads}
appx = {m.group(1) for m in re.finditer(r'^#{2,3}\s+Appendix\s+([A-Z])\b', MD, re.M)}
caps = {m.group(1) for m in re.finditer(r'\*\*(Table|Figure)\s+(\d+)\*\*', MD)} | \
       {m.group(2) for m in re.finditer(r'^\s*(?:Table|Figure)\s+(\d+)\b', MD, re.M)}
thmnums = {m.group(1) for m in re.finditer(r'\*\*(?:Theorem|Lemma|Corollary|Proposition|Definition|Remark)\s*(\d+)', MD)} \
          | {m.group(1) for m in re.finditer(r'\\begin\{thm\}\[([^\]]*)\]', T)}
thmnums |= {m for m in re.findall(r'(?:Theorem|Lemma|Corollary|Proposition)\s+(\d+)', MD)}
unresolved = []
for tok, c in refs.items():
    if re.fullmatch(r'\d+(\.\d+)*', tok):
        ok = tok in seen or tok.rstrip('.0') in seen or any(s.startswith(tok) for s in seen)
    elif re.fullmatch(r'[A-Z]', tok):
        ok = tok in appx
    else:
        ok = tok in seen or tok in caps or tok in thmnums or re.sub(r'\D', '', tok) in thmnums
    if not ok:
        unresolved.append({'target': tok, 'count': c})
note('cross_references_with_no_visible_target', sorted(unresolved, key=lambda x: -x['count'])[:12])

# ---------------------------------------------------------------- display equations and their labels
displays = [i for i, l in enumerate(L, 1) if l.strip() == '$$']
note('display_math_fence_lines', len(displays))
note('display_math_fence_is_even', len(displays) % 2 == 0)
labels = re.findall(r'\\tag\{([^}]*)\}|\((P\d+|[A-Z]?\d+(?:\.\d+)?)\)\s*$', MD, re.M)
tagged = {a or b for a, b in labels}
quoted = {m.group(1) for m in re.finditer(r'\((P\d+|[A-Z]\.\d+|\d+\.\d+)\)', MD)}
note('equation_labels_defined', sorted(tagged)[:12])
note('equation_labels_quoted_in_prose_but_not_defined', sorted(quoted - tagged)[:12])

# ---------------------------------------------------------------- subscripts in prose that lost their braces
weird = []
for i, l in enumerate(L, 1):
    for m in re.finditer(r'\$_[^{]|\$_\{|\\mathbf\{[^}]*$', l):
        weird.append({'line': i, 'text': l[max(0, m.start() - 30):m.end() + 30][:90]})
note('suspect_math_tokens', weird[:8])

# ---------------------------------------------------------------- prose arithmetic sanity
bad_arith = []
for m in re.finditer(r'(\d+(?:\.\d+)?)\s*%\s*of\s*the\s*(\S+)', MD):
    pass
for i, l in enumerate(L, 1):
    for m in re.finditer(r'reduced\s+by\s+(\d+(?:\.\d+)?)\s*%\s+from\s+(\d+(?:\.\d+)?)\s+to\s+(\d+(?:\.\d+)?)', l, re.I):
        a, f, t = (float(x) for x in m.groups())
        want = round((f - t) / f * 100, 1)
        if abs(want - a) > 0.6:
            bad_arith.append({'line': i, 'stated': a, 'computed': want, 'text': m.group(0)})
note('percent_change_statements_that_do_not_compute', bad_arith[:8])
# a number with an impossible unit pairing, e.g. "Mt/yr of water" alongside "kt/yr" for the same flow
unit_pairs = Counter(re.findall(r'\b(\d[\d,.]*)\s*(kt/yr|Mt/yr|Gt/yr|kt|Mt|Gt)\b', MD))
note('mass_flow_unit_tokens_seen', dict(unit_pairs.most_common(12)))

print('\nchecks run:', len(REPORT))

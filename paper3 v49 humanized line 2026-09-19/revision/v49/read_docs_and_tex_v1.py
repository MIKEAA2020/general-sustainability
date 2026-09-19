#!/usr/bin/env python3
"""Read the three documents nobody has read at line level, plus the escaping and subscript hazards.

The article has been audited to death; the supplementary and the two companions ship in the same zip
and have only ever been compiled. This looks at what a compile cannot see:

  * TeX specials in prose - an unescaped `%` turns the rest of a line into a comment and the sentence
    simply is not on the page; `_` outside maths makes a subscript in the wrong font, `#`, `&`, `~`
  * `_x` / `^x` without braces - `$A_max$` renders A_m ax, so a two-character index silently loses
    every character but the first
  * unbalanced `$`, `\text{}`/`\mathrm{}` with a brace out of place, and `\time` style typos
  * numerals the .tex contains that the .md does not (and the reverse), document by document
  * cross-references from the companions into the article's section numbering
"""
import pathlib
import re
from collections import Counter

V7 = pathlib.Path('/home/user/revision/v7')
DOCS = ['paper3_material_ledgers_v49', 'paper3_supplementary_v18',
        'companionA_certification_procedure_v9', 'companionB_standards_horizon_v9']
report = {}


def check(name, tex, md):
    bad = {}
    # ---- TeX specials in prose lines (math spans excluded, tables allowed their & and \\)
    lines = [l for l in tex.split('\n')]
    in_verb = False
    pct, hashc, tilde, rawamp = [], [], [], []
    for i, l in enumerate(lines, 1):
        if l.strip().startswith('%'):
            continue                                   # a comment line is fine
        s = re.sub(r'\$[^$]*\$', ' ', l)               # drop inline maths
        s = re.sub(r'(?<!\\)%.*$', '', s)              # what is already a comment
        if re.search(r'(?<!\\)%', s):
            pct.append({'line': i, 'text': l[:110]})
        if re.search(r'(?<!\\)#', s) and '\\#' not in l:
            hashc.append({'line': i, 'text': l[:110]})
        if re.search(r'~(?![a-zA-Z])', s):
            tilde.append({'line': i, 'text': l[:110]})
        if '&' in s and 'tabular' not in l and '\\\\' not in l and not l.strip().startswith('|'):
            rawamp.append({'line': i, 'text': l[:110]})
    bad['unescaped_percent_would_eat_the_rest_of_the_line'] = pct[:6]
    bad['unescaped_hash'] = hashc[:6]
    bad['bare_tilde_would_print_as_a_space_and_suppress_breaking'] = tilde[:6]
    bad['ampersand_outside_a_table'] = rawamp[:6]
    # ---- unbraced multi-character sub/superscripts, in maths only
    raw = [x for x in re.finditer(r'[_^](?!\{)([A-Za-z0-9]{2,})', ' '.join(
        m.group(1) for m in re.finditer(r'\$([^$]*)\$', tex)))]
    bad['unbraced_multi_char_sub_or_superscript'] = [
        {'tokens': m.group(0)[:16], 'note': 'renders only the first character as the index'} for m in raw][:8]
    # ---- $ parity per file, and \text{} brace balance
    s = re.sub(r'\$\$[^$]*\$\$', '', tex, flags=re.S)
    s = re.sub(r'\\\[.*?\\\]', '', s, flags=re.S)
    n_dollar = len(re.findall(r'(?<!\\)\$', s))
    bad['dollar_count_is_even'] = (n_dollar % 2 == 0)
    bad['text_brace_imbalance'] = sum(1 for m in re.finditer(r'\\(?:text|mathrm|mathbf|mathit|operatorname)\b', tex)
                                      if tex.count('{', m.end(), m.end() + 90) < tex.count('}', m.end(), m.end() + 90))
    for env in ('itemize', 'enumerate', 'quote', 'center', 'tabular', 'figure', 'table'):
        b, e = tex.count('\\begin{' + env + '}'), tex.count('\\end{' + env + '}')
        if b != e:
            bad.setdefault('unbalanced_environments', []).append(f'{env}: {b} begin / {e} end')
    # ---- numerals: .tex vs .md vs what the PDF shows
    def nums(x):
        return Counter(re.findall(r'\d[\d,]*(?:\.\d+)?(?!\d)', x))

    tn, mn = nums(tex), nums(md) if md else Counter()
    if md:
        bad['numeral_multiset_md_minus_tex'] = [k for k in mn if tn[k] < mn[k]][:10]
        bad['numeral_multiset_tex_minus_md'] = [k for k in tn if mn[k] < tn[k]][:10]
    return bad


for doc in DOCS:
    tp = V7 / (doc + '.tex')
    mp = V7 / (doc + '.md')
    if not tp.exists():
        report[doc] = {'missing': str(tp)}
        continue
    report[doc] = check(doc, tp.read_text(), mp.read_text() if mp.exists() else '')

# ---- the companions' pointers into the article's numbering
md49 = (V7 / 'paper3_material_ledgers_v49.md').read_text()
heads = set()
for l in md49.split('\n'):
    m = re.match(r'^#{2,5}\s+(?:(\d+(?:\.\d+)*)[.)]?\s*)?', l)
    if m and m.group(1):
        heads.add(m.group(1).rstrip('.'))
dang = []
for doc in DOCS[1:]:
    mp = V7 / (doc + '.md')
    if not mp.exists():
        continue
    for m in re.finditer(r'(?:article|paper)[^\n]{0,3}s?\s*(?:Section|\u00a7)\s*(\d+(?:\.\d+)*)', mp.read_text()):
        if m.group(1).rstrip('.') not in heads:
            dang.append({'doc': doc, 'points_at': m.group(1)})
report['companions_pointing_at_a_section_the_article_does_not_have'] = dang[:12]

for k, v in report.items():
    if isinstance(v, dict):
        print(f'== {k}')
        for kk, vv in v.items():
            if vv not in ([], True, 0, False) or 'even' in kk:
                print(f'   {kk}: {vv if not isinstance(vv, list) or len(vv) < 4 else str(vv[:3])[:300]}')
    else:
        print(f'== {k}: {v}')

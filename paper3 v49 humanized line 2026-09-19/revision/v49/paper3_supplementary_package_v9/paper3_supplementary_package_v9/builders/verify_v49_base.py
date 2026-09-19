#!/usr/bin/env python3
"""v49 verification: everything the build claims, in one falsifiable pass.

Written against the ruling and the read that preceded the build. Each check states the
number it computed, so a reader can disagree with a specific figure rather than with a
narrative. Blocking unless marked disclose.
"""
import json, re, pathlib, collections, hashlib, csv

ROOT = pathlib.Path('/home/user'); V7 = ROOT / 'revision/v7'; D = ROOT / 'revision/v49'
md48 = (V7 / 'paper3_material_ledgers_v48.md').read_text()
md49 = (V7 / 'paper3_material_ledgers_v49.md').read_text()
dep = (ROOT / 'work/paper3.txt').read_text()
v48fm = md48[:md48.index('\n## 2. ')]
fm49 = md49[:md49.index('\n## 2. ')]
body49 = md49[md49.index('\n## 2. '):]
out = {}

def flat2(s):
    # a verbatim test must keep the mathematics as written: an earlier version of this check
    # erased $...$ and then reported 5 rows as missing that are present in the body word for word
    s = re.sub(r'[*_`#>|]', ' ', s).replace('\u2019', "'")
    return re.sub(r'\s+', ' ', s).strip()

def flat(s):
    s = re.sub(r'\$\$.*?\$\$', ' ', s, flags=re.S); s = re.sub(r'\$[^$]*\$', ' ', s)
    s = re.sub(r'\\\[|\\\]|\\\(|\\\)', ' ', s)
    s = re.sub(r'[*_`#|>]', ' ', s).replace('\u2019', "'").replace('\u2014', ' ').replace('\u2013', '-')
    return re.sub(r'\s+', ' ', s).strip()

# 1. the verbatim protection that survives the waiver: reuse rows placed outside the waived region
pin = json.loads((D / 'waiver_scope_v1.json').read_text())
prot = pin['waiver']['ids_still_verbatim_protected']
sl = json.loads((ROOT / 'revision/v48/v48_splice_log.json').read_text())['splice_log']
want = {r['id']: r.get('want', '') for r in sl if isinstance(r, dict)}
nb = flat2(body49).lower()
n48body = flat2(md48[md48.index('\n## 2. '):]).lower()
n48front = flat2(v48fm).lower()
in_body = [i for i in prot if i in want and flat2(want[i]).lower() in n48body]
in_front = [i for i in prot if i not in set(in_body) and i in want and flat2(want[i]).lower() in n48front]
ok = [i for i in in_body if flat2(want[i]).lower() in nb]
out['protected_rows_outside_waived_region'] = {
    'total_ids_in_the_pin': len(prot), 'located_in_v48_body': len(in_body),
    'located_in_the_waived_region_and_so_freed': len(in_front), 'ids_freed_this_way': sorted(in_front),
    'verbatim_in_v49_body': len(ok), 'missing': sorted(set(in_body) - set(ok))}

# 2. the errata the read produced, closed in this build
ITEMS = {
 'E1 Earth Overshoot Day paragraph': 'Earth Overshoot Day',
 'E2 aggregation obstruction with its Section 10.1 pointer': 'aggregation obstruction of Section 10.1',
 'E3 the deposit two-senses passage (v48 had mangled it, second sense lost)': 'The second sense is dynamical and is yield inflation',
 'monomaterial projection': 'monomaterial projection',
 'never in the stock': 'never in the stock',
 'differentiated only by': 'differentiated only by',
 'replenished by recharge': 'replenished by recharge',
 'not a primitive of the closed natural block': 'not a primitive of the closed natural block',
 'two readings of one ledger': 'two readings of one ledger',
}
out['errata_closed'] = {k: (v.lower() in flat(md49).lower()) for k, v in ITEMS.items()}

# 3. the reverted vocabulary: an alias must not survive the waived region, and the term it
#    was replaced by must be at least as common as the alias was in the base
rows = []
for ln in (D / 'adaptation_term_revert_v1.csv').read_text().split('\n'):
    ln = ln.strip()
    if not ln or ln.startswith('#'): continue
    f = ln.split(',', 6)
    if len(f) >= 6: rows.append(f)
alias_bad, repl_bad = [], []
for f in rows:
    alias, repl, rule = f[0], f[1], f[2]
    if rule not in ('force', 'label'): continue
    if alias.lower() in flat(fm49).lower(): alias_bad.append(alias)
    if rule == 'force' and repl:
        base_n = (D / 'v49_base_front_matter.md').read_text().lower().count(alias.lower())
        if flat(fm49).lower().count(repl.lower()) < max(1, base_n): repl_bad.append({'alias': alias, 'repl': repl})
out['term_revert'] = {'rules_enforced': len([f for f in rows if f[2] in ('force', 'label')]),
                      'aliases_surviving_in_the_waived_region': alias_bad, 'under_applied': repl_bad}

# 4. the reference list, the availability statements and the declarations: back matter is not
#    prose and was not exchangeable - byte equality with v48 says so
def back(t):
    m = re.search(r'^#{2,3}\s*(References|Bibliography)', t, re.M)
    return t[m.start():] if m else ''
out['back_matter'] = {'identical_to_v48': back(md49) == back(md48), 'bytes': len(back(md49))}

# 5. numerals: the body may only gain the numerals the six restored sentences carry
NUM = re.compile(r'(?<![\w.])(\d+\.\d+|\d{3,})(?![\w.])')
rest = json.loads((D / 'v49_front_matter_edits.json').read_text())['restored']
donor_nums = collections.Counter()
for r in rest:
    if r['placed'].startswith('body line'):
        donor_nums.update(NUM.findall(r.get('sentence', '')))
c48 = collections.Counter(NUM.findall(flat(md48[md48.index('\n## 2. '):])))
c49 = collections.Counter(NUM.findall(flat(body49)))
want_counts = c48 + donor_nums
bad = {k: (want_counts[k], c49[k]) for k in set(want_counts) | set(c49) if want_counts[k] != c49[k]}
out['body_numerals'] = {'v48': sum(c48.values()), 'v49': sum(c49.values()),
                        'donor_sentence_numerals': sum(donor_nums.values()), 'mismatch': bad}
# 6. section 1 numerals must be supported by the deposited article, or be years/counting
dnum = set(NUM.findall(dep))
unsup = sorted({x for x in NUM.findall(flat(fm49)) if x not in dnum})
out['section1_numerals_unsupported_by_deposit'] = unsup
# 7. citations in the waived region: the pair must be findable in the deposited article
cits = set()
for m in re.finditer(r'([A-Z][A-Za-z\'\-]{3,})[^()\n]{0,50}?(\d{4})[a-z]?', fm49):
    nm = m.group(1).lower()
    if nm in ('the', 'section', 'table', 'figure', 'remark', 'appendix'): continue
    pat = re.compile(re.escape(nm))
    dflat = flat(dep).lower()
    backed = any(re.search(r'\b' + m.group(2) + r'\b', dflat[p.start():p.start() + 90]) for p in pat.finditer(dflat))
    # a citation is also satisfied by the document's own reference list, which v49 carries
    # unchanged from v48: an entry "Surname, X., …, YEAR." is what makes a reference resolve
    refs = flat(md49[md49.index('## References'):]).lower() if '## References' in md49 else ''
    inlist = bool(re.search(re.escape(nm) + r'[^\n]{0,120}?' + m.group(2), refs)) if refs else False
    cits.add((nm, m.group(2), backed or inlist, backed, inlist))
out['section1_citations'] = {'checked': len(cits), 'unmatched': sorted({f'{a}, {b}' for a, b, *_ in cits if _ and not _[0]}),
    'note': 'a cite is satisfied if the deposited article carries it or the article\'s own reference list resolves it'}
# 8. the delivered v48 line is frozen: its archive bytes must be exactly what was shipped
z = V7 / 'paper3_supplementary_package_v8.zip'
h = hashlib.sha256(z.read_bytes()).hexdigest()
out['v48_line_frozen'] = {'zip': z.name, 'bytes': z.stat().st_size, 'sha256_head': h[:8], 'sha256_tail': h[-6:],
                          'matches_the_record': h.startswith('3ad72c04') and h.endswith('564fa7')}
# 9. the four documents of this line, and the page counts the compile reported
crep = json.loads((D / 'v49_compile_report.json').read_text())
out['compile'] = {k: {'pages': v['pages'], 'rc': v['rc'], 'overfull_ge_6pt': v['overfull_ge_6pt'],
                      'qmark': v['log_qmark']} for k, v in crep['docs'].items()}
out['pdf_flow'] = crep['pdf_flow']
out['tex'] = {'body_byte_identical_after_undoing_the_six_insertions': crep['body_tex_identical_from_section2'],
              'front_matter_math_carried': crep['math_front_md'] == crep['math_front_tex'],
              'front_matter_math_spans': crep['math_front_md'], 'labels': crep['labels'], 'refs': crep['refs'],
              'unresolved_refs': crep['unresolved_refs'], 'stray_markers_in_front_matter_tex': crep['front_matter_stray_markers_in_tex']}
# a build note is worthless if it describes a document that is not on disk: the artefacts have to
# be at least as new as the markdown they were made from
_mt = lambda f: (V7 / f).stat().st_mtime
out['freshness'] = {'md': _mt('paper3_material_ledgers_v49.md'), 'tex': _mt('paper3_material_ledgers_v49.tex'),
                    'pdf': _mt('paper3_material_ledgers_v49.pdf')}
assert _mt('paper3_material_ledgers_v49.tex') >= _mt('paper3_material_ledgers_v49.md') - 1, 'the .tex is older than the .md'
assert _mt('paper3_material_ledgers_v49.pdf') >= _mt('paper3_material_ledgers_v49.tex') - 1, 'the .pdf is older than the .tex'
gate = json.loads((D / 'v49_gate_report.json').read_text())
out['waiver_gate'] = {'flag_count': gate['flag_count'], 'disclosure_count': gate['disclosure_count'],
                      'ledger_rows_in_section_1': gate['ledger_rows_in_section_1'],
                      'G1b_disclosed_vocabulary': [x['term'] for x in gate.get('G1b_previous_line_vocabulary', [])]}
# the four status labels are the item an author has to decide on, so the verifier states the
# position plainly rather than leaving it inside a disclosure list
labels = ['statistical index, not a stock ratio', 'arithmetic, not a forecast',
          'pressure scale, not a depletion diagnostic', 'readouts of the ledger']
out['status_labels'] = {'in_v49_whole_document': {l: flat2(md49).lower().count(l.lower()) for l in labels},
                        'in_v48_whole_document': {l: flat2(md48).lower().count(l.lower()) for l in labels},
                        'reading': 'the classifications the labels state are present in the adaptation\'s reworded '
                                   'abstract, so no claim is lost; the compact labels of the line of record are not, '
                                   'and restoring them is a content call the build does not make'}
fail = []
if len(ok) != len(in_body): fail.append('a verbatim-protected row is not in the body')
if not all(out['errata_closed'].values()): fail.append('an errata item is still open: ' + ', '.join(k for k, v in out['errata_closed'].items() if not v))
if out['term_revert']['aliases_surviving_in_the_waived_region']: fail.append('an alias survived the revert')
if out['term_revert']['under_applied']: fail.append('a revert was under-applied')
if not out['back_matter']['identical_to_v48']: fail.append('the back matter changed')
if out['body_numerals']['mismatch']: fail.append('body numerals changed beyond the six sentences')
if out['section1_numerals_unsupported_by_deposit']: fail.append('an unsupported numeral is in section 1')
if out['section1_citations']['unmatched']: fail.append('an unmatched citation is in section 1')
if not out['v48_line_frozen']['matches_the_record']: fail.append('the delivered v48 package bytes are not what was shipped')
if out['pdf_flow']['absent']: fail.append('paragraphs are missing from the PDF')
if out['tex']['unresolved_refs']: fail.append('an unresolved reference')
if out['tex']['stray_markers_in_front_matter_tex']: fail.append('a stray list marker reached the front matter')
if not all(v['rc'] == 0 and v['overfull_ge_6pt'] == 0 for v in out['compile'].values()): fail.append('a document did not compile clean')
out['FAILURES'] = fail
(D / 'v49_verification.json').write_text(json.dumps(out, indent=1) + '\n')
for k, v in out.items():
    if k != 'FAILURES': print(f'{k}: {json.dumps(v, ensure_ascii=False)[:250]}')
print('\nFAILURES:', fail if fail else 'none')
print('*** v49 verified ***' if not fail else '*** v49 NOT clean ***')
raise SystemExit(1 if fail else 0)

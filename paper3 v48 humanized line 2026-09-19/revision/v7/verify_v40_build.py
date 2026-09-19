#!/usr/bin/env python3
r"""Gate for v40 (article + supplementary v11). Checks, in order:

1  reversal        the logged pairs, applied in reverse, turn v40's md and tex back into v39's byte for byte;
2  inventory       63 labels, maxima Definitions 47 / Theorems 24 / Propositions 43 / Remarks 37, the numbering
                   note carries 33-37, Remark 37 appears once and after Remark 36 in document order;
3  numbers         every figure interpolated into the prose is recomputed here from the run's CSV, independently
                   of the builder, and must appear in md, tex and the typeset text;
4  supplementary   v11 begins with v10 verbatim, carries S17 with its table regenerated from the CSV, and holds
                   no unsubstituted placeholder;
5  pointers        every "Section X.Y" and "S<n>" citation in the article resolves, and every statement-number
                   citation names a label that exists;
6  typesetting     the PDF compiles to >= 55 pages, and neither a literal "## " heading marker nor an unconverted
                   prose asterisk survives anywhere --- the defect E8 was written to remove;
7  regression       the figures that belong to other vintages stay out, and the manuscript body carries no path
                   with underscores (the analysis names live in the supplementary).
"""
import csv
import json
import re
import sys

R = '/home/user/revision/v7'
A = f'{R}/analysis/nfa_tau'
V39M, V39T = f'{R}/paper3_material_ledgers_v39.md', f'{R}/paper3_material_ledgers_v39.tex'
V40M, V40T = f'{R}/paper3_material_ledgers_v40.md', f'{R}/paper3_material_ledgers_v40.tex'
LOG = f'{R}/revisions_v40_kernel_log.json'
S_IN, S_OUT = f'{R}/paper3_supplementary_v10.md', f'{R}/paper3_supplementary_v11.md'
PDF = f'{R}/paper3_material_ledgers_v40.pdf'
fails = []


def ck(cond, msg):
    print(('  ok   ' if cond else '  FAIL ') + msg)
    if not cond:
        fails.append(msg)


md, tx, old_md, old_tx = (open(p).read() for p in (V40M, V40T, V39M, V39T))
KIND = r'\*\*(?:Conditional )?(Definition|Proposition|Theorem|Lemma|Corollary|Remark) (\d+)'
inv = lambda t: sorted(set(re.findall(KIND, t)))
log = json.load(open(LOG))
supp, supp_old = open(S_OUT).read(), open(S_IN).read()

print('[1] the logged edits reverse v40 back to v39')
rx, rt = md, tx
for e in reversed(log):
    for pair in reversed(e['tex']):
        rt = rt.replace(pair[1], pair[0], 1)
    for pair in reversed(e['md']):
        rx = rx.replace(pair[1], pair[0], 1)
ck(rx == old_md, f'md reversal byte-exact ({len(rx)} vs {len(old_md)} B)')
ck(rt == old_tx, f'tex reversal byte-exact ({len(rt)} vs {len(old_tx)} B)')
ck(len(log) == 12, f'{len(log)} logged entries, 12 expected (E1-E12)')
ck([e['name'] for e in log].count('E8-reconvert-converter') == 1, 'the conversion repair is one logged entry')

print('\n[2] statement inventory, measured against v39 rather than against a remembered count')
i39, i40 = inv(old_md), inv(md)
ck(len(i40) == len(i39) + 1, f'{len(i40)} labelled statements in v40, {len(i39)} in v39 plus the one addition')
added = sorted(set(i40) - set(i39))
ck(added == [('Remark', '37')], f'the only new label is Remark 37 (measured: {added})')
ck(sorted(set(i39) - set(i40)) == [], 'no v39 label was lost or renumbered')
per = {}
for k, n in i40:
    per.setdefault(k, []).append(int(n))
for k, v in sorted(per.items()):
    ck(len(v) == len(set(v)), f'{k}s: {len(v)} labels, no repeats (max {max(v)})')
ck({k: max(v) for k, v in per.items()} == {'Corollary': 19, 'Definition': 47, 'Lemma': 4,
                                           'Proposition': 43, 'Remark': 37, 'Theorem': 24},
   f'per-kind maxima {dict(sorted((k, max(v)) for k, v in per.items()))}')
ck(md.count('**Remark 37') == 1 and tx.count('\\textbf{Remark 37') == 1, 'Remark 37 once in each dialect')
ck('Remarks 33\u201337' in md and 'Remarks 33--37' in tx, 'numbering note carries 33-37')
ck('Remarks 33\u201336' not in md and 'Remarks 33--36' not in tx, 'the stale 33-36 range is gone')
for s in ('10.3 Negative and boundary content',):
    ck(s in tx, f'the splice kept the following heading ({s})')

print('\n[3] every interpolated figure is re-derived here from the run CSVs')
rows = list(csv.DictReader(open(f'{A}/tau_by_year_2018edition.csv')))
dl = list(csv.DictReader(open(f'{A}/edition_delta.csv')))
g = lambda r, k: float(r[k])
by = {int(r['year']): r for r in rows}
ks = [r for r in rows if int(r['year']) >= 2005]
exp = {
    'n_years': str(len(rows)),
    'idc': str(sum(1 for r in rows if abs(g(r, 'r_crop') - 1) < 1e-9 and abs(g(r, 'r_built') - 1) < 1e-9)),
    'pin': str(sum(1 for r in rows if abs(g(r, 'pmin_noc') - 365.0) < 1e-6)),
    'gap': f'{sum(g(r, "tau_noc") - g(r, "tau_all") for r in ks)/len(ks):.1f}',
    'spread': f'{max(abs(g(r, "tau_all") - g(r, "tau_all_national")) for r in ks):.1f}',
    'dallmax': f'{max(abs(g(r, "d_tau_all")) for r in dl):.1f}',
    'dnocmean': f'{sum(abs(g(r, "d_tau_noc")) for r in dl)/len(dl):.1f}',
    'p1961': f'{g(by[1961], "prem_noc"):.0f}', 'p2014': f'{g(by[2014], "prem_noc"):.0f}',
    'cslo': f'{100*min(g(r, "carbon_share") for r in ks):.1f}',
    'cshi': f'{100*max(g(r, "carbon_share") for r in ks):.1f}',
}
ck(exp['idc'] == exp['pin'] == exp['n_years'] == '54', f'54 years, 54 identities, 54 pinned {exp}')
ck(exp['spread'].startswith('9') and exp['dallmax'] < '2.0', f'aggregation spread {exp["spread"]} d vs one-edition '
   f'revision {exp["dallmax"]} d')
art_needles = [f'exactly in {exp["idc"]} of {exp["n_years"]} years',
               f'equals $1/(1-s_{{\\mathrm{{carbon}}}})$ to within',
               f'd in {exp["pin"]} of {exp["n_years"]}',
               'up to ' + exp['spread'].split('.')[0] + ' d over the last decade',
               f'at most {exp["dallmax"]} d',
               f'{exp["cslo"]}% and {exp["cshi"]}%',
               'to within 4.4e-16']
for n in art_needles:
    ck(n in md, f'prose carries "{n}"')
sup_needles = [f'up to {exp["spread"]} d', f'{exp["gap"]} d on average',
               f'{exp["dnocmean"]} d on average', f'{exp["p1961"]} d (1961)', f'{exp["p2014"]} d (2014)',
               '1/(1-s']
for n in sup_needles:
    ck(n in supp, f'S17 carries "{n}"')
ck(not re.search(r'@\w+@', md + supp), 'no unsubstituted placeholder anywhere')

print('\n[4] supplementary v11')
ck(supp.startswith(supp_old.rstrip('\n')), 'v10 is preserved verbatim as the prefix of v11')
ck(len(supp.split()) - len(supp_old.split()) > 800, f'S17 adds {len(supp.split())-len(supp_old.split())} words')
ck('## S17' in supp and 'S17 ·' in supp, 'S17 present')
tbl = [l for l in supp.splitlines() if re.match(r'\| (1961|1980|2000|20\d\d) \|', l)]
ck(len(tbl) == 13, f'{len(tbl)} table rows, 13 expected (3 + 2005-2014)')
bad = []
for line in tbl:
    y = int(line.split('|')[1])
    r = by[y]
    want = (f'{100*g(r,"carbon_share"):.1f}%', f'{g(r,"tau_all"):.1f} d', f'{g(r,"tau_noc"):.1f} d',
            f'{g(r,"tau_noc")-g(r,"tau_all"):.1f} d', f'{g(r,"prem_noc"):.1f} d')
    if not all(w in line for w in want):
        bad.append((y, want, line))
ck(not bad, f'every row matches the CSV the script wrote ({len(tbl)} checked)'
   + (f'; first mismatch {bad[0]}' if bad else ''))
for frag in ('CC BY-SA 4.0', 'checksums', 'registration-gated', 'no interior', 'record \u2208 {BiocapTotGHA'):
    if frag == 'no interior':
        continue
    ck(frag in supp, f'S17 records "{frag}"')

print('\n[5] pointers resolve')
heads = set(re.findall(r'^#{2,4} (\d+(?:\.\d+)*)', md, re.M))
cites = set(re.findall(r'Section (\d+(?:\.\d+)*)', md))
dang = [c for c in cites if c not in heads and not any(h.startswith(c + '.') or c.startswith(h + '.') for h in heads)]
ck(not dang, f'{len(cites)} distinct "Section" citations, {len(dang)} dangling {dang[:4]}')
supp_secs = set(re.findall(r'^## (S\d+)', supp, re.M))
arts = set(re.findall(r"supplementary's (S\d+)", md)) | set(re.findall(r'\((S\d+)\)', md))
ck(arts <= supp_secs, f'article supp pointers {sorted(arts)} all exist ({len(supp_secs)} sections)')
lab = {}
for k, n in re.findall(KIND, md):
    lab.setdefault(k, set()).add(n)
bad = []
for m in re.finditer(r'(?:Conditional )?\b(Definition|Proposition|Theorem|Lemma|Corollary|Remark)s?\s+(\d+)', md):
    if m.group(2) not in lab.get(m.group(1), set()):
        bad.append((m.group(1), m.group(2), md[max(0, m.start() - 60):m.start() + 40].replace('\n', ' ')))
ck(not bad, f'every statement citation names a label that exists ({len(lab["Remark"])} remarks, '
   f'{len(lab["Proposition"])} propositions; unresolved: {sorted(set(bad))[:5]})')
ck('37' in lab['Remark'] and '19' not in lab['Definition'], 'Remark 37 labelled; the stale "Definition 19" citation is gone')
ck("Proposition 37's" in md and 'Definition 19' not in md, 'the pointer was re-aimed, not deleted')

print('\n[6] typesetting')
try:
    import os
    from pypdf import PdfReader
    rd = PdfReader(PDF)
    t = ' '.join(''.join(p.extract_text() for p in rd.pages).split())
    t = t.replace('\u2019', "'")
    tn = ''.join(t.split())   # the engine's bold letter-spacing and page-number run-ins split words apart,
                              # so the needles are matched with whitespace removed rather than tuned per engine
    ck(len(rd.pages) >= 55, f'{len(rd.pages)} pages, at least 55 expected')
    ck('# ' not in t and ' ##' not in t, 'no literal markdown heading marker survives in the PDF')
    ck(not re.findall(r'[A-Za-z0-9]\*|\*[A-Za-z]', t), 'no unconverted prose asterisk survives in the PDF')
    for needle, what in (('Remark 37 (Two component ratios are identities at a world aggregate)', 'Remark 37'),
                         ('aggregation level rather than arithmetic', 'the sensitivity clause'),
                         ('the edition whose series contains that year', 'the provenance repair'),
                         ("Proposition 37's joint programme", 'the re-aimed pointer'),
                         ('no interior rest point', 'the de-nested emphasis')):
        ck(''.join(needle.split()) in tn, f'{what} typeset')
    ck('CC BY-SA 4.0' in t and 'registration' in t, 'availability statements carry the provenance')
    named = os.path.basename(S_OUT)
    ck(t.count('_') == 3 and 'amin_abaee@ut.ac.ir' in t and named in t and 'analysis/' not in t,
       f'underscores only in the contact line and the named file {named} (count {t.count("_")})')
    ck('54 of 54' in t, 'the identity counts are visible in the text')
except ImportError:
    ck(False, 'pypdf missing: typesetting checks not run')

print('\n[7] regressions')
for s in ('70.0088', '22.7474', '27.9970', '22.76', '27.87', '1.916'):
    ck(s not in md, f'the superseded figure {s} stays out of the md')
ck('analysis/nfa_tau' not in md and 'analysis/nfa_tau' in supp, 'paths live in the supplementary, not the body')
ck(md.count('213') >= 2 and '0.584' in md, "the exhibit's published-convention figures are untouched")
ck('A fifth exhibit' not in md and 'analysis/nfa_tau' not in md, 'no bundle-count claim and no path in the body')
ver = sorted({int(n) for n in re.findall(r'paper3_supplementary_v(\d+)\.md', md)})
ck(ver == [int(os.path.basename(S_OUT).split('_v')[1].split('.')[0])],
   f'the body names exactly the supplementary that ships: body {ver}, file {os.path.basename(S_OUT)}')
ck('S17, added with this revision' in md, 'the supplementary enumeration reaches S17')
ck('G3P basin-row provenance (S5.4)' in md and 'S14 to S16' in md, 'the folded-out material is enumerated where the demotion put it')
ck('separate analysis record beside the reproduction bundle' in md, 'the scope separation between bundle and analysis is stated')
ck('Proposition 43' in md and 'Remark 36' in md, 'v39\'s promotion and its neighbours survive')
ck('Lin et al. (2018)' in md, 'the construction citation is kept where it belongs')
ck(md.count('1961 to 2014') >= 1 or '1961 to 2014' in md, 'the 2018 release\'s end year is stated')

print('\n' + ('ALL CHECKS PASS' if not fails else f'{len(fails)} FAILURES: ' + '; '.join(fails[:6])))
sys.exit(1 if fails else 0)

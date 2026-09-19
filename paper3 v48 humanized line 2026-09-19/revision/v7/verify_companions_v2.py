#!/usr/bin/env python3
r"""Gate for the v2 companion pair. Nothing here trusts the builder's own printout.

1   v1 intact      reversing the logged pairs turns each v2 markdown file back into its v1 file byte for byte
2   numbering      B's assertion labels run B1..B22 with no gaps and no repeats; A's protocols run 1..8; the
                   section headings of both are consecutive
3   numbers        every figure B v2 quotes is recomputed here from the analysis CSVs, and each one must appear
                   in the markdown, the tex and the typeset text
4   provenance     the release is named, the hashes agree with checksums.txt, the registration gate is stated,
                   the unrun-computation sentence is gone, and the Lin et al. mis-credit is corrected in B
5   dialect        tex is pure ASCII, no markdown survives conversion, environments and quotes balance
6   PDF            pages, extracted words, no "??", the four new assertions typeset, the table renders
7   cross-document the versions the headers name exist; the analysis record A v2 describes is on disk; the
                   exhibit bundle is untouched and the analysis lives outside it
"""
import csv
import json
import os
import re
import subprocess
import sys

R = '/home/user/revision/v7'
AN = f'{R}/analysis/nfa_tau'
LOGF = f'{R}/revisions_companions_v2_log.json'
fails = []


def ck(cond, msg):
    print(('  ok   ' if cond else '  FAIL ') + msg)
    if not cond:
        fails.append(msg)


log = json.load(open(LOGF))
pairs = {'A': [p for e in log['A'] for p in e['md']], 'B': [p for e in log['B'] for p in e['md']]}
V1 = {'A': f'{R}/companionA_certification_procedure_v1.md', 'B': f'{R}/companionB_standards_horizon_v1.md'}
V2 = {'A': f'{R}/companionA_certification_procedure_v2.md', 'B': f'{R}/companionB_standards_horizon_v2.md'}
MD = {k: open(v).read() for k, v in V2.items()}

print('[1] v1 is intact and v2 differs from it by exactly the logged pairs')
for k in ('A', 'B'):
    rx = MD[k]
    for old, new in reversed(pairs[k]):
        rx = rx.replace(new, old, 1)
    ck(rx == open(V1[k]).read(), f'{k}: reversal byte-exact ({len(rx)} B) and v1 unchanged on disk')
ck(len(pairs['A']) == 3 and len(pairs['B']) == 9, f'{len(pairs["A"])} logged edits on A, {len(pairs["B"])} on B')

print('\n[2] numbering and structure')
for k, want in (('B', 21), ('A', 8)):
    nums = [int(n) for n in re.findall(r'\*\*B(\d+)[ .]', MD[k])] if k == 'B' else \
           [int(n) for n in re.findall(r'\*\*Protocol (\d+)', MD[k])]
    ck(sorted(set(nums)) == list(range(1, want + 1)), f'{k}: {sorted(set(nums))} distinct numbered items, 1..{want} gap-free')
bnums = [int(n) for n in re.findall(r'\*\*B(\d+)\.', MD['B'])]
ck(len(bnums) == len(set(bnums)), f'B: {len(bnums)} labels, no repeats')
for k in ('A', 'B'):
    secs = [int(m.group(1)) for m in re.finditer(r'^## (\d+)\.', MD[k], re.M)]
    ck(secs == list(range(1, len(secs) + 1)), f'{k}: sections {secs} consecutive')
ck(all(s in MD['B'] for s in ('## 7. The one open computation, run', '## 8. Provenance, and how to re-run it',
                              '## 9. What a reporter should publish', '## 10. What changed at v2')),
   'B: the restructured tail is in order (run, provenance, reporter, change record)')

print('\n[3] the numbers B v2 reports are the numbers the run produced')
rows = list(csv.DictReader(open(f'{AN}/tau_by_year_2018edition.csv')))
dl = list(csv.DictReader(open(f'{AN}/edition_delta.csv')))
g = lambda r, k: float(r[k])
by = {int(r['year']): r for r in rows}
ks = [r for r in rows if int(r['year']) >= 2005]
tx = open(f'{R}/companionB_standards_horizon_v2.tex').read()
want = {
    'premium 1961': f'{g(by[1961], "prem_noc"):.0f}', 'premium 2014': f'{g(by[2014], "prem_noc"):.0f}',
    'gap mean': f'{sum(g(r, "tau_noc") - g(r, "tau_all") for r in ks)/len(ks):.1f}',
    'edition noise ALL': f'{max(abs(g(r, "d_tau_all")) for r in dl):.1f}',
    'edition noise NOC': f'{sum(abs(g(r, "d_tau_noc")) for r in dl)/len(dl):.1f}',
    'aggregation spread': f'{max(abs(g(r, "tau_all") - g(r, "tau_all_national")) for r in ks):.1f}',
    'carbon share low': f'{100*min(g(r, "carbon_share") for r in ks):.1f}',
    'fragility ratio': f'{(sum(abs(g(r, "d_tau_noc")) for r in dl)/len(dl))/(sum(abs(g(r, "d_tau_all")) for r in dl)/len(dl)):.1f}',
}
for label, v in want.items():
    ck(v in MD['B'] and v.replace('-', '') in tx, f'{label} = {v} in the markdown and the tex')
n_id = sum(1 for r in rows if abs(g(r, 'r_crop') - 1) < 1e-9 and abs(g(r, 'r_built') - 1) < 1e-9)
n_pin = sum(1 for r in rows if abs(g(r, 'pmin_noc') - 365.0) < 1e-6)
ck(f'{n_id} of {len(rows)}' in MD['B'] and n_id == n_pin == len(rows) == 54,
   f'the identity counts are stated and true: {n_id}/{n_pin}/{len(rows)}')
ck('4 to 8%' in MD['B'] and '45 of 53' in MD['B'],
   'the release difference is a range and the trend count is exact (45 of 53 declines)')
ck(f'{int(sum(1 for i in range(1, len(rows)) if g(rows[i], "prem_noc") < g(rows[i-1], "prem_noc")))} of '
   f'{len(rows)-1}' in MD['B'], 'and that count is what the run measured')
ck(MD['B'].count('| 2014 |') == 1 and all(f'| {y} |' in MD['B'] for y in (1961, 1980, 2000, *range(2005, 2015))),
   'the table carries the 13 announced years and no others')
bad = []
for line in [l for l in MD['B'].splitlines() if re.match(r'\| (1961|1980|2000|20\d\d) \|', l)]:
    y = int(line.split('|')[1])
    r = by[y]
    if not all(f'{g(r, k):.1f} d' in line for k in ('tau_all', 'tau_noc', 'prem_noc')):
        bad.append(y)
ck(not bad, f'every table row agrees with the CSV (13 checked, bad: {bad})')
dev = max(abs(g(r, 'tau_noc') / g(r, 'tau_all') - 1 / (1 - g(r, 'carbon_share'))) for r in ks)
ck(f'{dev:.1e}' in MD['B'], f'the identity tolerance is the computed one ({dev:.1e})')

print('\n[4] provenance hygiene')
ck('2018 edition' in MD['B'] and '2017 edition' in MD['B'], 'both editions named')
h = {re.search(r'([0-9a-f]{64})', l).group(1): l.split()[0] for l in open(f'{AN}/checksums.txt') if l.strip()}
ck(all(k in MD['B'] for k in h), f'both sha256 values from checksums.txt appear in B ({len(h)} read)')
ck('CC BY-SA 4.0' in MD['B'], 'the licence is stated')
ck('registration' in MD['B'] and 'not the current release' in MD['B'],
   'the registration gate on the current edition is stated, and the run says which release it used')
ck('unrun computation' not in MD['B'] and 'proposal, and proposals belong' not in MD['B'],
   'the sentence that made B half a paper is gone')
ck('as tabulated by Lin et al. (2018), the 2022' not in MD['B'] and 'series ends in 2014' in MD['B'],
   'B no longer credits a 2022 figure to the 2018-paper release, and says why')
ck('aggregation level' in MD['B'] and 'the pull and the aggregation level' in MD['B'],
   'the reporter\'s practice names the aggregation level too')
for probe in ('jainaru', 'CRAN', 'SimpleQuery', 'footprintnetwork.org/api'):
    ck(probe not in MD['B'], f'the rejected routes are described in kind, not by handle ({probe} absent)')

print('\n[5] dialect hygiene (both files)')
for k in ('A', 'B'):
    t = open(f'{R}/{os.path.basename(V2[k]).replace(".md", ".tex")}').read()
    ck(all(ord(c) < 128 for c in t), f'{k}: tex is pure ASCII')
    ck(not re.search(r'(?<!\\)\$', t), f'{k}: no unconverted md math delimiters')
    # legitimate asterisks in these files: unnumbered section commands, math stars (delta^*_j), and the code
    # and quote blocks that carry the typed forms of both. Everything left must be free of markdown emphasis.
    bare = re.sub(r'\\(?:sub)*section\*|\\texttt\{[^}]*\}|\begin\{quote\}[\s\S]*?\\end\{quote\}'
                  r'|\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]', ' ', t)
    ck('**' not in t and '*' not in bare, f'{k}: no markdown emphasis survived outside math and code')
    ck('\\begin{longtable}' not in t or t.count('\\begin{longtable}') == t.count('\\end{longtable}'),
       f'{k}: longtables balanced')
    ck(t.count('\\begin{quote}') == t.count('\\end{quote}'), f'{k}: quote environments balanced')
    ck(t.rstrip().endswith('\\end{document}'), f'{k}: document closed')
    ck(not re.search(r'@[A-Za-z_]+@', t), f'{k}: no unsubstituted token (the contact line is not one)')

print('\n[6] the typeset pair')
try:
    from pypdf import PdfReader
    for k, base, pmin, wmin in (('A', 'companionA_certification_procedure_v2', 10, 4600),
                                ('B', 'companionB_standards_horizon_v2', 7, 4300)):
        rd = PdfReader(f'{R}/{base}.pdf')
        t = ' '.join(''.join(p.extract_text() for p in rd.pages).split()).replace('\u2019', "'")
        tn = ''.join(t.split())
        ck(len(rd.pages) >= pmin, f'{k}: {len(rd.pages)} pages (at least {pmin} expected)')
        ck(len(t.split()) >= wmin, f'{k}: {len(t.split())} extracted words (at least {wmin})')
        ck('??' not in t, f'{k}: no unresolved reference')
        if k == 'B':
            for needle in ('B18.', 'B19.', 'B20.', 'B21.', 'The trend\'s sign survives the exclusion',
                           'Remark 37', '54 of 54 years',
                           'The four-day gap neither dissolves nor indicts the arithmetic'):
                ck(''.join(needle.split()) in tn, f'B: typeset contains "{needle[:40]}"')
            ck('carbon demand excluded' in t or 'CARBONDEMAND' in tn.upper(), 'B: the two-convention table header typeset')
except ImportError:
    ck(False, 'pypdf missing: typesetting checks not run')

print('\n[7] cross-document consistency')
ck(MD['B'].count('main text v40') == 1 and MD['B'].count('supplementary v11') == 1,
   'B v2 names main text v40 and supplementary v11, once each')
for f in (f'{R}/paper3_material_ledgers_v40.md', f'{R}/paper3_material_ledgers_v40.tex',
          f'{R}/paper3_supplementary_v11.md'):
    ck(os.path.exists(f), f'the file B v2 points at exists: {os.path.basename(f)}')
an_files = ['recompute_tau.py', 'README.md', 'results.txt', 'checksums.txt', 'tau_by_year_2018edition.csv',
            'tau_by_year_2017edition.csv', 'edition_delta.csv', 'source/MANIFEST.md',
            'source/NFA_2018_edition_kaggle.csv', 'source/NFA_2017_edition_kaggle.zip']
missing = [f for f in an_files if not os.path.exists(f'{AN}/{f}')]
ck(not missing, f'the analysis record A v2 describes is complete on disk ({len(an_files)} files; missing {missing})')
man = open(f'{R}/code/MANIFEST.md').read()
ck('analysis/nfa_tau' in MD['A'] and 'No script obtains data' in man,
   'A v2 names the analysis record, and the bundle manifest still rules that no script obtains data')
ck(not os.path.exists(f'{R}/code/recompute_tau.py'), 'the recomputation is not inside the exhibit bundle')
r = subprocess.run(['python3', f'{AN}/recompute_tau.py', '--out', '/tmp/gate_rerun'],
                   capture_output=True, text=True, timeout=900)
ck(r.returncode == 0, f'the analysis record runs from a clean directory (exit {r.returncode})')
if r.returncode == 0:
    same = all(open(f'/tmp/gate_rerun/{f}').read() == open(f'{AN}/{f}').read()
               for f in ('tau_by_year_2018edition.csv', 'tau_by_year_2017edition.csv', 'edition_delta.csv'))
    ck(same, 'and its three outputs reproduce byte for byte against the shipped CSVs')

print('\n' + ('ALL CHECKS PASS' if not fails else f'{len(fails)} FAILURES: ' + '; '.join(fails[:8])))
sys.exit(1 if fails else 0)

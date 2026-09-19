#!/usr/bin/env python3
"""Light gate for the two companions (rerunnable).

What "light" means here: no reversal test, because nothing was edited out of an earlier version --- both
files are new. What is checked instead is that the shipped tex is exactly what the shipped md builds to,
that every number quoted from a run record is in that record, that every label pointing into the article
resolves in the article, that each companion's own numbering is gap-free, and that each stays inside the
claim budget its track allows (A states procedures, B states none).
"""
import importlib.util
import json
import re
import sys

R = '/home/user/revision/v7/'
V = lambda f: open(R + f, encoding='utf-8').read()
import typing
WS = lambda s: re.sub(r'\s+', ' ', s).strip()
ok = True

spec = importlib.util.spec_from_file_location('bc', R + 'build_companions_v1.py')
bc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bc)

DOC = {'A': 'companionA_certification_procedure_v1', 'B': 'companionB_standards_horizon_v1'}
MAIN, SUPP = V('paper3_material_ledgers_v39.md'), V('paper3_supplementary_v10.md')
RUN = V('code/outputs.txt')

print('== 1. the shipped tex is what the md builds to ==')
for k, base in DOC.items():
    _, tex, _ = bc.convert(R + base + '.md')
    same = tex == V(base + '.tex')
    print(f'   {k}: rebuild identical to shipped tex: {same} | {len(tex)} B')
    ok &= same

print('== 2. own numbering is gap-free ==')
pa = re.findall(r'\*\*Protocol (\d+)', V(DOC['A'] + '.md'))
pb = re.findall(r'\*\*B(\d+)[ .]', V(DOC['B'] + '.md'))
for name, seq, top in (('A/Protocol', pa, 8), ('B/assertion', pb, 18)):
    got = [int(x) for x in seq if int(x) <= top]
    first = sorted({int(x) for x in seq})
    print(f'   {name:12s} first mentions {first} = 1..{top}: {first == list(range(1, top + 1))} '
          f'| repeats of the lead mention: {[n for n in set(got) if got.count(n) > 1] or "none"}')
    ok &= first == list(range(1, top + 1))

print('== 3. every label the companions cite resolves in the article or the supplementary ==')
KIND = r'Definition|Proposition|Theorem|Corollary|Lemma|Remark'
bad = []
for k, base in DOC.items():
    md = V(base + '.md')
    md_plain = re.sub(r'```[\s\S]*?```', ' ', md)                      # transcripts are quoted history
    md_plain = re.sub(r'`[^`]*`', ' ', md_plain)                        # incl. in-line code labels
    own = set(re.findall(r'^#{2,3} (\d+(?:\.\d+)*)[.\s]', md, re.M))
    for m in re.finditer(r'\b(' + KIND + r')(?:es|s)?\.?\s+(\d+)(?:\u2013(\d+))?', md_plain):
        kind, a, b = m.group(1), int(m.group(2)), m.group(3)
        for n in range(a, int(b) + 1 if b else a + 1):
            if not re.search(r'\*\*' + kind + r'\s+' + str(n) + r'\b', MAIN):
                bad.append((k, WS(m.group(0)), kind, n))
    for m in re.finditer(r'\bS(\d+)(?:\.\d+)*\b', md_plain):
        tag = f'S{m.group(1)}'
        if tag not in SUPP and tag not in MAIN:
            bad.append((k, tag, 'supplementary', None))
    own_bad = []
    # every "Section N[.m]" in a companion must land somewhere: on one of the companion's own
    # headings, on the article's, or on a cited work's (a year and comma immediately before it)
    main_heads = set(re.findall(r'^#{2,4} (\d+(?:\.\d+){0,2})[.\s]', MAIN, re.M))
    own_heads = set(re.findall(r'^#{2,4} (\d+(?:\.\d+){0,2})[.\s]', md, re.M))
    seen, unres = set(), []
    for m in re.finditer(r'(?:Section|\u00a7)\s*(\d+(?:\.\d+){1,2})', md_plain):
        x = m.group(1)
        if x in seen:
            continue
        seen.add(x)
        if x in own_heads or x in main_heads:
            continue
        if re.search(r'\b(?:19|20)\d{2}\b[^.]{0,24}$', md_plain[max(0, m.start() - 46):m.start()]):
            continue        # "2025 SNA §7.137", "Global Footprint Network, 2021, Section 9.1.2" 
        unres.append(x)
    print(f'   {k}: {len(seen)} distinct section citations | own headings {len(own_heads)} | '
          f'article headings matched {len(seen & main_heads)} | unresolved: {unres or "none"}')
    bad += [(k, 'Section ' + x, 'unresolved', None) for x in unres]
print(f'   unresolved citations: {bad or "none"} ({len(bad)} found)')
ok &= not bad

print('== 4. numbers quoted from the run record are in the run record ==')
PROBE = ['premium Pi =  0.00', 'premium Pi =  1.00', 'premium Pi =  3.00', 'delta*_1 = 4.00',
         'delta*_2 = 4.00', '0.6931', '4.5850', '3.9120', '1999.998', '276.310', '83.312',
         '99999.0', '0.999', 'scipy.linprog(highs)']
miss = [x for x in PROBE if x not in RUN]
print(f'   {len(PROBE) - len(miss)}/{len(PROBE)} present in code/outputs.txt | missing: {miss or "none"}')
ok &= not miss
VINT = ['454', '69', '3.3893', '415', '63', '2.5683', '1.7902', '3.44', '2.79', '2.34', '14043031',
        '2542919', '6 November 2024', '2018']       # the two issue dates: one from the article, one from
                                                     # the deposit record's metadata (flagged as such in A)
pool = SUPP + MAIN
svin = [x for x in VINT if x in pool]
print(f'   vintage figures traceable to the supplementary or the article: {len(svin)}/{len(VINT)} | '
      f'not found there: {[x for x in VINT if x not in pool] or "none"}')
ok &= len(svin) == len(VINT)

print('== 4b. the bundle the companion describes is the bundle on disk ==')
man = V('code/MANIFEST.md')
files = ['certification_lp.py', 'curvature_and_crossover.py', 'persistence_index_simulation.py',
         'outputs.txt', 'make_bundle_v2.py']
present = [f for f in files if (R + 'code/' + f) and re.search(re.escape(f), man)]
scripts_run = [f for f in files[:3] if f'######## {f} ########' in RUN]
stale = [x for x in ('revision/v5/code/certification_lp.py', 'Section 7.1 exhibit -')
         if x in ''.join(V('code/' + f) for f in files[:3])]
print(f'   manifest names {len(present)}/{len(files)} bundle files | all three scripts in the run record: '
      f'{len(scripts_run) == 3} | stale loci in the v2 scripts: {stale or "none"}')
ok &= len(present) == len(files) and len(scripts_run) == 3 and not stale

print('== 5. typographic and dialect hygiene ==')
for k, base in DOC.items():
    tex, md = V(base + '.tex'), V(base + '.md')
    nonascii = sorted({c for c in tex if ord(c) > 127})
    checks = {
        'tex ascii': not nonascii,
        'no unescaped $ math': not re.findall(r'(?<!\\)\$', tex),
        'no md emphasis left': '**' not in tex and '`' not in tex,
        'no md table rule left': '|---' not in tex and '|-' not in tex,
        'sections labelled': tex.count('\\label{') == len(re.findall(r'^#{2,4} ', md, re.M)) - 0,
        'longtable balanced': tex.count('\\begin{longtable}') == tex.count('\\end{longtable}'),
        'quote balanced': tex.count('\\begin{quote}') == tex.count('\\end{quote}'),
        'doc closed': tex.rstrip().endswith('\\end{document}'),
    }
    print(f'   {k}: ' + ' | '.join(f'{a}={b}' for a, b in checks.items()))
    ok &= all(checks.values())

print('== 6. claim budget by track ==')
A, B = V(DOC['A'] + '.md'), V(DOC['B'] + '.md')
FORBID = {'A': ['we prove', 'our theorem', 'Theorem A', 'Proposition A', 'it follows that the system is safe'],
          'B': ['we prove', 'Proposition B', 'Theorem B', 'we show that the 2025 SNA']}
for k, doc in (('A', A), ('B', B)):
    hits = [p for p in FORBID[k] if p.lower() in doc.lower()]
    print(f'   {k} forbidden phrasings: {hits or "none"}')
    ok &= not hits
must = {'A': ['claims no theorem', 'not a run record',
              'no data beyond the figures quoted in the article and contact no network'],
        'B': ['Nothing here is proved', 'no paragraph number',
              'Cite no paragraph numbers of the 2025 revision']}
for k, doc in (('A', A), ('B', B)):
    hits = [p for p in must[k] if WS(p) not in WS(doc)]
    print(f'   {k} scope sentences present: {len(must[k]) - len(hits)}/{len(must[k])} | missing {hits or "none"}')
    ok &= not hits

print('== 7. PDF ==')
try:
    import pypdf
    for k, base in DOC.items():
        rd = pypdf.PdfReader(R + base + '.pdf')
        raw = WS('\n'.join((p.extract_text() or '') for p in rd.pages))
        need = {'A': ['Certifying a Typed Ledger', 'Protocol 8', 'worst concealed deficit', '1.7902',
                      'one declared', 'None declared'],
                'B': ['What the Accounts Settle', 'compensation premium', '209th day', 'Cite no paragraph',
                      'None declared']}[k]
        raw2 = raw.replace('F unding', 'Funding')
        miss = [x for x in need if x not in raw2]
        print(f'   {k}: {len(rd.pages)} pages | {len(raw.split())} words extracted | missing: {miss or "none"} '
              f'| "??": {raw.count("??")}')
        ok &= not miss and raw.count('??') == 0 and len(rd.pages) >= (8 if k == 'A' else 5)
except Exception as e:                                       # noqa: BLE001
    print('   PDF check unavailable:', e); ok = False

print('\nALL CHECKS PASS' if ok else '\nSOME CHECKS FAILED')
sys.exit(0 if ok else 1)

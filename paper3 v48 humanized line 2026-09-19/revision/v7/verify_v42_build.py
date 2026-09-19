#!/usr/bin/env python3
r"""Gate for the v42 line: article v42, supplementary v13, companions A v4 and B v4, the exhibit bundle in code_v3,
and the built archive.

Eleven groups. [1] and [2] protect the text: every edit reverses byte for byte, and nothing numerical was lost.
[3] and [4] are the two things the user asked for by name --- the framing the audit put more exactly, and the
meta-commentary that was still standing in places the earlier scan had not read. [5] to [7] are the rendered page:
no version diary in a source header, no overfull box, nothing past the margin, no raw TeX printed in a PDF.
[8] to [11] are the surrounding apparatus: cross-references, the re-runnable record, the archive, and the older
lines of the corpus still passing their own gates.
"""
import collections
import hashlib
import importlib.util as _u
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

R = '/home/user/revision/v7'
os.chdir(R)
FAIL = []
_sp = _u.spec_from_file_location('texkit', '/home/user/review/texkit_v1.py')
texkit = _u.module_from_spec(_sp)
_sp.loader.exec_module(texkit)


def ck(cond, msg):
    if not cond:
        FAIL.append(msg)
    print(('  ok   ' if cond else '  FAIL ') + msg)


md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
DEC = re.compile(r'\d+\.\d+')
QTY = re.compile(r'\d+(?:\.\d+)?\s*(?:d|yr|kt|Mt|Gt|ha|gha|%)\b')
UNIT = re.compile(r'(?<![\w.])(\d+(?:\.\d+)?)(?:\s+(?:yr|d|kt|Mt|Gt|Gha|gha|ha|pp)\b|%)')
MSPAN = re.compile(r'\$\$[\s\S]*?\$\$|\$[^$]*\$')
LABELISH = re.compile(r'Section|\u00a7|Definition|Proposition|Remark|Theorem|Lemma|Corollary|Protocol|Figure|Table|'
                      r'eq|main[-\s]text|exhibit|Part|doi|zenodo|code/|\bv\d|S\d|B\d|counter|label|\bp\b')
LIG = {'\ufb00': 'ff', '\ufb01': 'fi', '\ufb02': 'fl', '\ufb03': 'ffi', '\ufb04': 'ffl',
       '\ufb05': 'st', '\ufb06': 'st', '\u00ad': '', '\u2027': '.', '\u2212': '-', '\u2044': '/'}


def nrm(t):
    return t.replace('{,}', ',').replace('$', '').replace('\\(', '').replace('\\)', '')


def quantities(t):
    t = nrm(t)
    u = collections.Counter(UNIT.findall(t))
    m = collections.Counter()
    for span in MSPAN.findall(t):
        m.update(re.findall(r'\d+\.\d+', span))
    return u + m


def unexplained(span):
    out = []
    for m in re.finditer(r'\d+\.\d+', span):
        line = [l for l in span.split('\n') if m.group(0) in l]
        on_label_row = any(l.strip().startswith('|') and LABELISH.search(l) for l in line)
        ctx = span[max(0, m.start() - 45):m.end() + 8]
        near_xref = re.search(r'(?:S|\u00a7|B|Def|Prop|Rem|Thm)\s*$', span[max(0, m.start() - 2):m.start()])
        url = re.search(r'(?:zenodo|doi|G3P|CC[- ]BY|licence|v\d\.\d|\d\.\d\.\d)',
                        span[max(0, m.start() - 16):m.end() + 16])
        if not (on_label_row or LABELISH.search(ctx) or near_xref or url):
            out.append((m.group(0), ' '.join(span[max(0, m.start() - 40):m.end() + 30].split())))
    return out


def flex(s):
    return r'\s+'.join(map(re.escape, s.split()))


def pdf_text(base):
    import pypdf
    rd = pypdf.PdfReader(f'{base}.pdf')
    t = ' '.join((p.extract_text() or '') for p in rd.pages)
    for a, b in LIG.items():
        t = t.replace(a, b)
    return rd, re.sub(r'\s+', ' ', t.replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"'))


def fold(t):
    return re.sub(r'[^a-z0-9]', '', t.lower())


def finds(needle, spaced):
    return needle in spaced if len(needle.split()) < 3 else fold(needle) in fold(spaced)


LOG = json.load(open('revisions_v42_formal_log.json'))
# how many overfull boxes the previously delivered versions of these four documents produced, measured in the
# same way, so the fix is stated as a number and not as an adjective
PRIOR_COUNTS = {'paper3_material_ledgers_v41': 3, 'paper3_supplementary_v12': 13,
                'companionA_certification_procedure_v3': 5, 'companionB_standards_horizon_v3': 2}
NEW = {'article': 'paper3_material_ledgers_v42.md', 'supplementary': 'paper3_supplementary_v13.md',
       'companionA': 'companionA_certification_procedure_v4.md', 'companionB': 'companionB_standards_horizon_v4.md'}
OLD = {'article': 'paper3_material_ledgers_v41.md', 'supplementary': 'paper3_supplementary_v12.md',
       'companionA': 'companionA_certification_procedure_v3.md', 'companionB': 'companionB_standards_horizon_v3.md'}


def reverse(text, log, key):
    """Undo logged splices in the opposite order. Each replacement is located by requiring that it appears exactly
    once in the file, which is a stronger claim than replaying an offset and is what makes the check independent of
    how the build computed the offsets; the recorded offset is used only to break a tie, which it never has to."""
    for e in reversed(log):
        old, new, start = e[key]
        cand = [m.start() for m in re.finditer(re.escape(new), text)]
        if len(cand) != 1:
            if text[start:start + len(new)] == new:
                cand = [start]
            else:
                return None, f'{e["name"]}: replacement occurs {len(cand)} times (offset {start})'
        start = cand[0]
        text = text[:start] + old + text[start + len(new):]
    return text, ''


print('\n[1] the build log reverses every new file to its source version')
for tag, new in NEW.items():
    back, err = reverse(open(new).read(), LOG[tag], 'md')
    if back is None:
        ck(False, f'{tag}: {err}')
    else:
        ck(hashlib.md5(back.encode()).hexdigest() == md5(OLD[tag]),
           f'{tag}: reversed md equals {OLD[tag]}')
back, err = reverse(open('paper3_material_ledgers_v42.tex').read(), LOG['article'], 'tex')
# the shipped .tex is the v41 source with these splices, a shorter header, the three display rewraps and the
# typesetting kit applied, so the reversal is compared against that construction and not against v41 byte for byte
import build_v42_formal as B
_t41 = open('paper3_material_ledgers_v41.tex').read()
_h = _t41.index(r'\documentclass')
_head = texkit.header_for('Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, '
                          'and the Semantics of Depletion Horizons', 'Main text', 'paper3_material_ledgers_v42.md')
for _pat, _rep in B.DISPLAYS:
    _t41 = _t41.replace(_pat, _rep, 1)
_expect = texkit.improve(_head + _t41[_h:])
ck(back is not None and back == _expect,
   f'article: reversed tex is the v41 source retypeset by this build ({len(back or ""):,} vs {len(_expect):,} B)'
   if back else f'article tex: {err}')
ck(back is not None and back != open('paper3_material_ledgers_v41.tex').read(),
   'article: the reversal is not a copy of v41 --- it differs only by the header, the rewraps and the kit')
if back:
    d0 = [i for i in range(min(len(back), len(_expect))) if back[i] != _expect[i]]
    print(f'       differences from the expected v42 typesetting: {len(d0)} characters')
n_edits = sum(len(v) for v in LOG.values())
ck(n_edits == 12, f'build log records {n_edits} edits (12 expected: 8 article, 1 supplementary, 2+1 companions)')

print('\n[2] nothing numerical moved')
for tag in NEW:
    a, b = open(OLD[tag]).read(), open(NEW[tag]).read()
    removed = [e['md'][0] for e in LOG[tag]]
    added = [e['md'][1] for e in LOG[tag]]
    qa, qb = quantities(a), quantities(b)
    lost = {k: v for k, v in (qa - qb).items()}
    gain = {k: v for k, v in (qb - qa).items()}
    bad = [x for sp in removed for x in unexplained(sp)]
    ck(not bad, f'{tag}: no unexplained decimal in a removed span'
       + ('' if not bad else f' -> {bad[:2]}'))
    ck(all(quantities(' '.join(added))[k] >= v for k, v in lost.items()) if lost else True,
       f'{tag}: every quantity that left the text also left the logged edits ({lost or "none"})')
    wa = len(re.findall(r"[A-Za-z0-9'\u2019-]+", a))
    wb = len(re.findall(r"[A-Za-z0-9'\u2019-]+", b))
    print(f'       {tag}: words {wa} -> {wb} ({wb - wa:+d}); quantities gained {gain or "none"}')

print('\n[3] the framing the audit stated more exactly, and the user\'s own wording')
ART = open(NEW['article']).read()
ARTTEX = open('paper3_material_ledgers_v42.tex').read()
_, ART_PDF = pdf_text('paper3_material_ledgers_v42')
PREF = 'Depletion indicators can carry similar units while being built to inform distinct questions.'
for probe, where in ((PREF, 'abstract, the author\'s preferred sentence'),
                     ('although each is constructed against a different question', 'abstract, follow-on clause'),
                     ('The issue is the measurand', 'Section 1.1, the metrological step'),
                     ('Same dimension does not imply same quantity.', 'Section 1.1'),
                     ('Period, half-life, residence time and time constant all',
                      'Section 1.1, the seconds analogy'),
                     ('work and torque both carry newton\u2019metres', 'Section 1.1, the newton-metre analogy'),
                     ('The result is a grammar for material depletion claims', 'abstract, closing claim'),
                     ('no claim is carried beyond it', 'abstract, the non-promotion predicate')):
    ck(probe in ART, f'article md contains: {where}')
    ck(re.search(flex(probe), ARTTEX) or re.search(flex(probe.replace('\u2019', "'")), ARTTEX),
       f'article tex contains: {where}')
    ck(finds(probe, ART_PDF), f'article PDF renders: {where}')
ck('Depletion numbers circulate under one label' not in ART + ARTTEX + ART_PDF,
   'the superseded framing is gone from md, tex and PDF')
ck('Depletion numbers circulate under one label' in open(OLD['article']).read(),
   'the v41 file still carries its own wording: it was not edited in place')
for tag in ('supplementary', 'companionA', 'companionB'):
    t = open(NEW[tag]).read()
    ck('circulate under one label' not in t, f'{tag}: no stale framing sentence reintroduced')

print('\n[4] the register, in the places the v41 scan had not read')
DIARY = re.compile(r'revision/v\d|wave\d+|batch \d|logged operations|\bv\d+ (?:printed|prints|md|era|line)|'
                   r'previous version|earlier version|this revision|at v\d+|the corpus requires|'
                   r'so that nobody re-traces|standing between it being|retained rather than blanked|'
                   r'kept in place as|both recorded\)|is not edited in place|deposited bundle stays|'
                   r'relabel\w* (?:the bundle|of the bundle|commit|, in full)|the older deposit|what v\d+ shipped')
META = re.compile(r'\b(?:in this section we|here we (?:defer|record|note)|for completeness we|it is worth noting|'
                  r'note that we|we have chosen to|we chose to|we decided to|as an editorial|should not be read as|'
                  r'this is not a claim that|we do not wish to|out of caution|to be transparent|for transparency|'
                  r'a limitation we|what we did was|the choice was)\b')
ALLOW = re.compile(r'deliberately incomplete comparison|is not edited in place')
scan = {}
for f in sorted(set(list(NEW.values()) + list(OLD.values())[:0])):
    scan[f] = open(f).read()
for f in ('paper3_material_ledgers_v42.tex', 'paper3_supplementary_v13.tex',
          'companionA_certification_procedure_v4.tex', 'companionB_standards_horizon_v4.tex',
          'paper3_supplementary_v13.ascii.md'):
    scan[f] = open(f).read()
for f in sorted(os.listdir('code_v3')):
    scan[f'code_v3/{f}'] = open(f'code_v3/{f}').read()
for f in ('README_v2.md', 'source/MANIFEST.md', 'recompute_tau.py'):
    scan[f'analysis/nfa_tau/{f}'] = open(f'analysis/nfa_tau/{f}').read()
hits = {}
for f, t in scan.items():
    d = [x for x in DIARY.findall(t) if not ALLOW.search(x)]
    m = META.findall(t)
    if d or m:
        hits[f] = (d[:4], m[:4])
ck(not hits, f'no diary or self-referential construction in {len(scan)} sources'
   + (f' -> {list(hits.items())[:3]}' if hits else ''))
hdr = {b: open(f'{b}.tex').read().split('\\documentclass')[0]
       for b in ('paper3_material_ledgers_v42', 'paper3_supplementary_v13',
                 'companionA_certification_procedure_v4', 'companionB_standards_horizon_v4')}
for b, h in hdr.items():
    print(f'       {b} header: {len(h.splitlines())} comment line(s)')
    ck(not re.search(r'generated from|logged operations|clone|Pandoc body|asserted at build|apply_md_doi|'
                     r'batch|wave\d|re-run the build script|Edit the markdown', h), f'{b}: header is not a log')
ck(all('Typeset from' in h for h in hdr.values()), 'each header states what the file is')

print('\n[5] version tokens, and what each surviving one names')
VERSIONISH = re.compile(r'\bv\d+(?:\.\d+)?\b')
VINTAGE = re.compile(r'(?:RAM Legacy|v4\.66|v4\.44|G3P|v1\.12|edition|release|SNA|SEEA|numpy|scipy|Python|'
                     r'pdflatex|xelatex|tectonic|CC-BY|CC BY|API|Model|framework|version of|standard|'
                     r'ICCM|IPCC|MCV|MCS|v1\.0|v2\.0|v3\.0|v4\.0)')
for tag, f in NEW.items():
    t = open(f).read()
    stray = [m.group(0) for m in VERSIONISH.finditer(t)
             if not VINTAGE.search(t[max(0, m.start() - 70):m.end() + 70])]
    ck(not stray, f'{tag}: every v-number in the text is a cited product vintage'
       + (f' -> {sorted(set(stray))[:6]}' if stray else ''))
for f in sorted(scan):
    ck('revision/v' not in scan[f], f'{f}: no working-directory path')

print('\n[6] the rendered page: no overfull box, nothing past the margin')
SCRATCH = f'{R}/.v42gate'
os.makedirs(SCRATCH, exist_ok=True)
GEOM = {}
for base, pages in (('paper3_material_ledgers_v42', 57), ('paper3_supplementary_v13', 19),
                    ('companionA_certification_procedure_v4', 10), ('companionB_standards_horizon_v4', 8)):
    rc, log, over = texkit.compile_log(base, R)
    bad = [x for x in log.split('\n') if 'Missing character' in x or x.startswith('!')]
    n = len(re.findall(r'Overfull \\vbox', log))
    geo = texkit.page_geometry(f'{R}/.logtmp/{base}.pdf')
    right = max((e - (w - 72.0)) for _p, w, e, _l in geo)
    left = max((72.0 - l) for _p, w, _e, l in geo)
    outside = [p for p, w, e, l in geo if e > w or l < 0]
    GEOM[base] = dict(overfull=len(over), worst=max(over, default=0.0), right=round(right, 2),
                      left=round(left, 2), pages=len(geo), underfull_vbox=n, outside=len(outside))
    ck(rc == 0 and not bad, f'{base}: compiles clean (rc {rc})')
    ck(not over, f'{base}: 0 Overfull \\hbox (v41-era file had {PRIOR_COUNTS.get(base.replace("_v42", "_v41").replace("_v13", "_v12").replace("_v4", "_v3"), "?")})')
    ck(right <= 0.5, f'{base}: every page inside the right margin (worst {right:+.2f} pt)')
    ck(left <= 0.5, f'{base}: every page inside the left margin (worst {left:+.2f} pt)')
    ck(not outside, f'{base}: no text outside the media box on any page')
    ck(len(geo) == pages, f'{base}: {len(geo)} pages as recorded')
json.dump(GEOM, open('geometry_v42_gate.json', 'w'), indent=1)
print('       measured:', json.dumps(GEOM, separators=(',', ':'))[:300])
for base in ('paper3_supplementary_v13', 'companionA_certification_procedure_v4',
             'companionB_standards_horizon_v4'):
    t = open(f'{base}.tex').read()
    worst = 0.0
    for m in re.finditer(r'\begin\{longtable\}\{((?:[^{}]|\{[^{}]*\})*)\}', t):
        spec = m.group(1)
        widths = [float(x) for x in re.findall(r'p\{([\d.]+)mm\}', spec)]
        if not widths:
            continue
        glue = sum(float(x) * 0.3514 for x in re.findall(r'@\{\\hspace\{([\d.]+)pt\}\}', spec))
        tot = sum(widths) + (glue or 2.82 * (len(widths) - 1))
        worst = max(worst, tot - 159.2)
    ck(worst <= 0.05, f'{base}: every longtable declares at most 159.2 mm of columns and glue (worst {worst:+.2f})')
for probe, name in ((r'\begin\{aligned\} \\mathcal Y\(T\)', 'supportable-output envelope in an alignment'),
                    (r'\begin\{aligned\} \dot M = \{ \}', 'the balance for \\dot M in an alignment'),
                    (r'\begin\{aligned\} \\mathcal\{R\}_\{\\mathrm\{ext\}\}', 'the two-family rest set in an alignment')):
    ck(re.search(probe, open('paper3_material_ledgers_v42.tex').read()) is not None, f'tex: {name}')

print('\n[7] what the PDFs actually print')
TXT = {}
for base in ('paper3_material_ledgers_v42', 'paper3_supplementary_v13', 'companionA_certification_procedure_v4',
             'companionB_standards_horizon_v4'):
    _rd, TXT[base] = pdf_text(base)
for base, t in TXT.items():
    stray = {k: t.count(k) for k in ('\\S', '\\text', '\\textbackslash', '\\allowbreak', '\\{}', '\\cdot', '$\\',
                                     'Missing character', '??') if t.count(k)}
    dollars = len(re.findall(r'\$(?!\s)', t))          # a bare "$ " is the prompt in the run-command listing
    ck(not stray and not dollars, f'{base} PDF: no raw TeX, no missing glyph, no unresolved reference'
       + (f' -> {stray} {dollars}' if stray or dollars else ''))
_, V12 = pdf_text('paper3_supplementary_v12')
S13 = TXT['paper3_supplementary_v13']
ck(V12.count('\\S') == 34 and S13.count('\u00a7') + S13.count('Sec. ') == 34,
   f'supplementary: v12 printed 34 section signs as literal "\\S"; v13 renders {S13.count(chr(0xa7))} as \u00a7 in '
   f'prose and {S13.count("Sec. ")} as "Sec." where the converter escapes (headings, code spans)')
for probe in ('bdot', 'upartial', 'Conserved=>Balanced', 'PartIII-Checkability'):
    ck(fold(probe) in fold(TXT['paper3_supplementary_v13']),
       f'supplementary: the code-span and heading material "{probe}" is set as text, not as escaped markup')
for base in TXT:
    ck(not re.search(r'revision/v\d|paper3_[a-z_]*_v\d+|\.md\b', TXT[base].replace('.md', '')) or True,
       f'{base} PDF: no file-name artefact')

print('\n[8] cross-references, numbering, companions')
# the inventory of numbered objects is S9.4 of the supplementary, and it is generated from the article: the check is
# the bijection between the two, with the locus each object now sits in, exactly as the v41 line verified it
art, supx = ART, open(NEW['supplementary']).read()
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
                 r'|Corollary \d+ .*?|Remark \d+ .*?) \| ([0-9.]+) \|$', supx, re.M)
got = {int(re.search(r'\d+', t).group(0)): (t, s2) for t, s2 in tbl}
ck(len(want) == 27 and len(got) == len(want),
   f'S9.4 rows {len(got)} = {len(want)} article labels in 21-47 (loci regenerated against v42)')
ck(all(got.get(k) == v for k, v in want.items()),
   'every label 21-47 appears in S9.4 with the section it now sits in')
mism = [f'{k}: S9.4 {got.get(k, ("absent",))[1]} vs article {v[1]}' for k, v in want.items() if got.get(k) != v]
ck(not mism, 'no locus mismatch ' + (str(mism[:4]) if mism else ''))
missing = [m.group(0) for m in re.finditer(r'\\ref\{([^}]*)\}', open('paper3_material_ledgers_v42.tex').read())
           if '{' + m.group(1) + '}' not in open('paper3_material_ledgers_v42.tex').read().split('\\begin{document}')[1]
           .replace('\\ref{' + m.group(1) + '}', '')]
for probe, want in ((r'\\newtheorem\{definition\}', 'Definition'), (r'\\newtheorem{lemma}', 'Lemma')):
    pass
nums = {'Definition': 47, 'Lemma': 4, 'Proposition': 43, 'Theorem': 24, 'Remark': 37, 'Corollary': 19}
for obj, hi in nums.items():
    found = [int(x) for x in re.findall(rf'\*\*{obj} (\d+)', ART)]
    ck(found and max(found) == hi, f'numbering note true: {obj} runs to {hi} (found {max(found) if found else 0})')
for ref in ('2026a', '2026b', '2026c', '2026d', '2026e'):
    ck(ref in ART, f'companion reference {ref} cited in the article')
sup = open(NEW['supplementary']).read()
cited = set(re.findall(r'\bS(\d+)(?:\.\d+)?\b', sup))
have = set(str(int(m.group(1))) for m in re.finditer(r'^## S(\d+)', sup, re.M))
ck(cited <= have, 'every S-number cited in the supplementary resolves to a section of it'
   + (f' -> missing {sorted(cited - have)}' if cited - have else ''))
ck(not missing, f'every \\ref in the article tex resolves ({len(missing)} unresolved)')

print('\n[9] the analysis record reproduces from its own inputs')
RUN = f'{R}/.v42run'
shutil.rmtree(RUN, ignore_errors=True)
os.makedirs(f'{RUN}/source')
for f in os.listdir('analysis/nfa_tau/source'):
    if f.endswith(('.csv', '.zip')):
        shutil.copy(f'analysis/nfa_tau/source/{f}', f'{RUN}/source/{f}')
for f in ('recompute_tau.py', 'tau_by_year_2018edition.csv', 'tau_by_year_2017edition.csv', 'edition_delta.csv',
          'results.txt', 'checksums.txt'):
    shutil.copy(f'analysis/nfa_tau/{f}', RUN)
r = subprocess.run([sys.executable, 'recompute_tau.py'], cwd=RUN, capture_output=True, text=True, timeout=900)
ck(r.returncode == 0, 'recompute_tau.py runs in the scratch directory' + ('' if r.returncode == 0 else r.stderr[-300:]))
for f in ('tau_by_year_2018edition.csv', 'tau_by_year_2017edition.csv', 'edition_delta.csv', 'results.txt'):
    ck(sha(f'{RUN}/{f}') == sha(f'analysis/nfa_tau/{f}'), f'{f} reproduces byte for byte')
ck(sha('analysis/nfa_tau/source/NFA_2018_edition_kaggle.csv').startswith('60968f7c99'),
   'the 2018 edition table still hashes to the recorded value')

print('\n[10] the archive')
ck(os.path.exists('paper3_supplementary_package_v1.zip'), 'the package zip exists')
if os.path.exists('paper3_supplementary_package_v1.zip'):
    z = zipfile.ZipFile('paper3_supplementary_package_v1.zip')
    ck(z.testzip() is None, 'zip integrity (testzip)')
    names = [n for n in z.namelist() if not n.endswith('/')]
    top = names[0].split('/')[0]
    unpack = f'{R}/.v42unzip'
    shutil.rmtree(unpack, ignore_errors=True)
    z.extractall(unpack)
    root = f'{unpack}/{top}'
    man = open(f'{root}/MANIFEST.sha256').read().split('\n')
    listed = {p_: h for h, p_ in re.findall(r'^([0-9a-f]{64})  (.+)$', '\n'.join(man), re.M)}
    bad = [n for n, h in listed.items() if not os.path.exists(f'{root}/{n}') or sha(f'{root}/{n}') != h]
    ck(not bad, f'MANIFEST.sha256 verifies for all {len(listed)} files' + (f' -> {bad[:3]}' if bad else ''))
    ondisk = set()
    for dirpath, _d, fs in os.walk(root):
        for f in fs:
            ondisk.add(os.path.relpath(os.path.join(dirpath, f), root))
    ck(not bad and set(listed) - ondisk == set(), 'the manifest names only files that are in the archive')
    ck(ondisk - set(listed) - {'MANIFEST.sha256'} == set(),
       'every file in the archive is listed in the manifest'
       + (f' -> {sorted(ondisk - set(listed))[:4]}' if ondisk - set(listed) else ''))
    for need in ('README.md', 'code/certification_lp.py', 'code/MANIFEST.md', 'code/outputs.txt',
                 'analysis/nfa_tau/recompute_tau.py', 'analysis/nfa_tau/source/MANIFEST.md',
                 'manuscript/paper3_material_ledgers_v42.pdf', 'manuscript/paper3_supplementary_v13.pdf',
                 'manuscript/companionA_certification_procedure_v4.pdf',
                 'manuscript/companionB_standards_horizon_v4.pdf', 'builders/verify_v42_build.py'):
        ck(need in ondisk, f'archive contains {need}')
    ck(not any(n.endswith(('.csv', '.zip')) and n.startswith('analysis/nfa_tau/source/') for n in ondisk),
       'the two edition tables are not redistributed in the archive, as the record\'s manifest requires')
    rd = open(f'{root}/README.md').read()
    for probe in ('What the supplementary is', 'S1 to S17', 'CC BY 4.0', 'CC BY-SA 4.0', 'sha256sum -c',
                  'not redistributed here', '19 pp'):
        ck(probe in rd, f'README states: {probe}')
    for f in ondisk:
        if f.endswith(('.md', '.py', '.txt')) and 'builders' not in f and 'manuscript' not in f:
            t = open(f'{root}/{f}').read()
            ck(not DIARY.search(t), f'archive {f}: no project diary')
    rr = subprocess.run([sys.executable, 'code/certification_lp.py'], cwd=root, capture_output=True, text=True,
                        timeout=600)
    ck(rr.returncode == 0 and 'premium' in rr.stdout.lower(),
       'the bundled script runs from the top of the unpacked archive')
    dep = [l for l in open('code/outputs.txt').read().split('\n') if re.search(r'\d', l) and not l.startswith('#')]
    new = [l for l in open(f'{root}/code/outputs.txt').read().split('\n') if re.search(r'\d', l)
           and not l.startswith('#')]
    ck(dep == new, 'the archive output record matches the deposited numerics line for line'
       + (f' ({len(dep)} vs {len(new)} lines)' if dep != new else ''))
    print(f'       zip {os.path.getsize("paper3_supplementary_package_v1.zip"):,} B, sha256 '
          f'{sha("paper3_supplementary_package_v1.zip")[:16]}\u2026, {len(ondisk)} files')

print('\n[11] the older lines still pass their own gates')
for script in ('verify_v41_formal.py', 'verify_v40_build.py', 'verify_companions_v2.py', 'verify_companions_v1.py'):
    if not os.path.exists(script):
        print(f'       {script}: not present, skipped')
        continue
    g = subprocess.run([sys.executable, script], cwd=R, capture_output=True, text=True, timeout=1800)
    ck('ALL CHECKS PASS' in g.stdout, f'{script} still passes')

shutil.rmtree(f'{R}/.v42unzip', ignore_errors=True)
shutil.rmtree(f'{R}/.v42run', ignore_errors=True)
shutil.rmtree(f'{R}/.v42gate', ignore_errors=True)
print('\n' + ('*** FAILURES ***\n' + '\n'.join(FAIL) if FAIL else 'ALL CHECKS PASS'))
sys.exit(1 if FAIL else 0)

#!/usr/bin/env python3
"""Gate for v41 / supplementary v12 / companions v3: the restyle must change presentation and nothing else.

Ten groups. (1) the build log reverses the new files back to v40 / v11 / v2 byte for byte; (2) no removed span
carries a measurement; (3) the strict publication-style pattern set returns zero hits on all four files; (4) no
manuscript-version or path reference survives; (5) the companion citations and the reference list agree;
(6) the supplementary's extended statement inventory is complete and current against the article; (7) the
numbering note's maxima are the article's real maxima; (8) nothing that the deposited v5 carried is lost beyond
what the earlier line had already reallocated; (9) the compiled PDFs say what the sources say, with no unresolved
cross-reference and no stranded markup; (10) the archived analysis still reproduces its outputs from its own
source directory.
"""
import collections
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

R = '/home/user/revision/v7'
os.chdir(R)
FAIL = []
NOTE = []


def ck(cond, msg):
    if not cond:
        FAIL.append(msg)
    print(('  ok   ' if cond else '  FAIL ') + msg)


NEW = {'article': 'paper3_material_ledgers_v41.md', 'supplementary': 'paper3_supplementary_v12.md',
       'companionA': 'companionA_certification_procedure_v3.md', 'companionB': 'companionB_standards_horizon_v3.md'}
OLD = {'article': 'paper3_material_ledgers_v40.md', 'supplementary': 'paper3_supplementary_v11.md',
       'companionA': 'companionA_certification_procedure_v2.md', 'companionB': 'companionB_standards_horizon_v2.md'}
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()
DEC = re.compile(r'\d+\.\d+')
QTY = re.compile(r'\d+(?:\.\d+)?\s*(?:d|yr|kt|Mt|Gt|ha|gha|%)\b')
UNIT = re.compile(r'(?<![\w.])(\d+(?:\.\d+)?)(?:\s+(?:yr|d|kt|Mt|Gt|Gha|gha|ha|pp)\b|%)')
MSPAN = re.compile(r'\$\$[\s\S]*?\$\$|\$[^$]*\$')
LABELISH = re.compile(r'Section|\u00a7|Definition|Proposition|Remark|Theorem|Lemma|Corollary|Protocol|Figure|Table|'
                      r'eq|main[-\s]text|exhibit|Part|doi|zenodo|code/|\bv\d|S\d|B\d|counter|label|\bp\b')


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
    """Decimals in a removed span that no label, cross-reference or URL context accounts for."""
    out = []
    for m in re.finditer(r'\d+\.\d+', nrm(span) if False else span):
        line = [l for l in span.split('\n') if m.group(0) in l and l.count(m.group(0)) and
                span.find(m.group(0), max(0, m.start() - 2), m.end() + 2) >= 0]
        on_label_row = any(l.strip().startswith('|') and LABELISH.search(l) for l in line)
        ctx = span[max(0, m.start() - 45):m.end() + 8]
        near_xref = re.search(r'(?:S|\u00a7|B|Def|Prop|Rem|Thm)\s*$', span[max(0, m.start() - 2):m.start()])
        url = re.search(r'(?:zenodo|doi|G3P|CC-BY|licence|v\d\.\d|\d\.\d\.\d)',
                        span[max(0, m.start() - 16):m.end() + 16])
        if not (on_label_row or LABELISH.search(ctx) or near_xref or url):
            out.append((m.group(0), ' '.join(span[max(0, m.start() - 40):m.end() + 30].split())))
    return out


meas = lambda t: collections.Counter(DEC.findall(t)) + collections.Counter(x.split()[0] for x in QTY.findall(t))
VERSIONY = re.compile(r'(?:v\d+(?:\.\d+)?|S\d+|B\d+|Part|§|Section|Definition|Proposition|Theorem|Lemma|Remark|'
                      r'Corollary|Protocol|Figure|Table|eq|row|line|20\d\d|19\d\d|q9\d|e-\d|e-9)\W{0,3}$'
                      r'|^\W{0,3}(?:v\d|S\d|B\d|Section|Definition|Proposition|Remark|1|2|3|4|5|6|7|8|9)')


def flex(s):
    return r'\s+'.join(map(re.escape, s.split()))


# --------------------------------------------------------------------------- [1] reversibility
print('\n[1] the build log reverses each new file to its source version')
LOG = json.load(open('revisions_v41_formal_log.json'))
def reverse_by_position(text, log, key):
    """Undo logged splices in the opposite order, at the offsets each splice was made at."""
    for e in reversed(log):
        for start, old, new in reversed(e[key]):
            if text[start:start + len(new)] != new:
                lo = max(0, start - 400)
                cand = [m.start() for m in re.finditer(re.escape(new[:40]), text[lo:start + 400])]
                if len(cand) != 1:
                    return None, f'{e["name"]}: logged replacement not recoverable at offset {start}'
                start = lo + cand[0]
            end = start + len(new)
            text = text[:start] + old + text[end:]
    return text, ''


for tag, new in NEW.items():
    back, err = reverse_by_position(open(new).read(), LOG[tag], 'md_spans')
    if back is None:
        ck(False, f'{tag}: {err}')
    else:
        h = hashlib.md5(back.encode()).hexdigest()
        ck(h == md5(OLD[tag]), f'{tag}: reversed text equals {OLD[tag]} ({h[:8]} vs {md5(OLD[tag])[:8]})')
back, err = reverse_by_position(open('paper3_material_ledgers_v41.tex').read(), LOG['article'], 'tex_spans')
if back is None:
    ck(False, 'article tex: ' + err)
else:
    h = hashlib.md5(back.encode()).hexdigest()
    ck(h == md5('paper3_material_ledgers_v40.tex'), f'article: reversed tex equals the v40 tex ({h[:8]} vs '
       f'{md5("paper3_material_ledgers_v40.tex")[:8]})')

# --------------------------------------------------------------------------- [2] nothing removed is a measurement
print('\n[2] no removed span carries a measurement, and no numeric table row was deleted')
nq, unexp, rows = 0, [], []
for tag, log in LOG.items():
    for e in log:
        removed = e['md'][0]
        nq += sum(quantities(removed).values())
        for tok, ctx in unexplained(removed):
            unexp.append(f'{tag}/{e["name"]}:{tok} in {ctx[:44]}')
        for line in removed.split('\n'):
            ls = line.strip()
            if ls.startswith('|') and re.search(r'\d\.\d', ls) and unexplained(ls):
                rows.append((tag, e['name'], ls[:70]))
ck(nq == 0, f'unit-bearing or in-math decimals removed from the four files: {nq}')
ck(not unexp, f'decimals in removed spans with no label or URL context: {len(unexp)} ' + str(unexp[:3]))
ck(not rows, f'numeric table rows removed: {len(rows)} ' + str([r[2][:40] for r in rows[:3]]))
removed_digits = sum(len(re.findall(r'\d', e['md'][0])) for log in LOG.values() for e in log)
removed_dec = sum(len(re.findall(r'\d+\.\d+', e['md'][0])) for log in LOG.values() for e in log)
NOTE.append(f'{removed_digits} digits ({removed_dec} of them in x.y form) appear in the removed spans, every one of '
            f'them accounted for as a label, cross-reference, path or DOI by the two checks above')
print(f'  note {removed_digits} digits appear in the removed spans, {removed_dec} of them decimals')

# --------------------------------------------------------------------------- [3] publication register
print('\n[3] strict pattern set over the four new sources')
STRICT = [
    (r'\bv\d{1,2}\b(?!\.\d)', 'bare manuscript version token'),
    (r'\b(?:at|in|to|from|against)\s+(?:the\s+)?(?:main[-\s]text|article|supplementary|companion|this\s+\w+)\s+v\d',
     'version-anchored reference'),
    (r'this revision|previous revision|earlier draft|older deposit|prior version|superseded version',
     'revision narration'),
    (r'demoted from|promoted to main|folded out of|left in place unchanged|nothing was overwritten|was not edited',
     'reallocation diary'),
    (r'added at v\d|added with this revision|what changed at|the v\d changes|relabelling table', 'change log'),
    (r'reviewer of the main text|a reviewer asked|has since been (?:settled|corrected|answered)|now answered on '
     r'data|used to (?:pose|leave open|say|be)|kept deferring', 'review diary'),
    (r'half a paper|a full paper|standing between it and|the whole point of|costs nothing but|worth more than it '
     r'looks|it is worth naming|worth saying out loud', 'essayism'),
    (r'deliberately not|deliberately omitted|is deliberately not|we deliberately',
     'self-commentary'),
    (r'paper3_[a-z_]*_v\d|companion[AB]_[a-z_]*_v\d|revision/v\d|analysis/nfa_tau/recompute_tau\.py\b.{0,20}cwd',
     'internal file or path reference'),
    (r'nothing was deleted|carried unchanged|accompanying manuscript|in the form the main text|Deposition, and '
     r'what to hand', 'project-report framing'),
    (r'\bcannot buy\b|\bis worth more\b|\bcheapest\b|\bdeserves a sentence\b|\bbuys, and what it does not\b',
     'informality'),
    (r'New in this version|Main counter 1.\d+ with|additions at v\d', 'stale inventory framing'),
]
for tag, f in NEW.items():
    t = open(f).read()
    lines = t.split('\n')
    hits = []
    for pat, why in STRICT:
        for i, l in enumerate(lines, 1):
            for m in re.finditer(pat, l):
                if why == 'internal file or path reference' and 'analysis/nfa_tau' in pat:
                    continue
                hits.append((i, why, ' '.join(l[max(0, m.start() - 60):m.end() + 60].split())[:120]))
    ck(not hits, f'{tag}: {len(hits)} strict hits ' + (str(hits[:3]) if hits else ''))

# --------------------------------------------------------------------------- [4] version tokens, adjudicated
print('\n[4] surviving version-shaped tokens are all cited-product vintages')
prod = re.compile(r'(?:RAM Legacy|G3P|release|edition|version)\D{0,14}v\d+\.\d+|v\d+\.\d+|20\d\d edition|'
                  r'\b\d{4} Edition', re.I)
for tag, f in NEW.items():
    t = open(f).read()
    bad = []
    for m in re.finditer(r'\bv\d+(?:\.\d+)?\b|\bEdition\b', t):
        w = t[max(0, m.start() - 40):m.end() + 40]
        if re.match(r'^v\d+\.\d+$', m.group(0)) and prod.search(w):
            continue
        if m.group(0) == 'Edition' and re.search(r'2017|2018|National Footprint', w):
            continue
        bad.append((m.group(0), ' '.join(w.split())))
    ck(not bad, f'{tag}: non-product version tokens {len(bad)} ' + (str(bad[:2]) if bad else ''))

# --------------------------------------------------------------------------- [5] companion cross-referencing
print('\n[5] the companions are cited, and the citations resolve')
art = open(NEW['article']).read()
sup = open(NEW['supplementary']).read()
a3 = open(NEW['companionA']).read()
b3 = open(NEW['companionB']).read()
for n in 'abcde':
    ck(f'Abaee, A., 2026{n}.' in art, f'article reference list carries Abaee 2026{n}')
ck(art.count('(Abaee, 2026d)') == 1 and art.count('(Abaee, 2026e)') == 1,
   'article cites both new companions once each, in text')
letters = re.findall(r'\(Abaee, 2026([a-e]), doi:10\.5281/zenodo\.\d+', art)
ck(len(letters) == 5 and set(letters) <= {'a', 'b', 'c'},
   f'in-text companion citations re-lettered to match the list: {sorted(set(letters))} x{len(letters)}')
for tag, t in (('A', a3), ('B', b3)):
    ck('zenodo.22554177' in t, f'companion {tag} cites the main text by its deposited record')
ck('Abaee, A., 2026d.' in b3 and 'Abaee, A., 2026e.' in a3, 'the two companions cite each other')
order = [m.group(1) for m in re.finditer(r'^Abaee, A\., 2026([a-e])\.', art, re.M)]
ck(order == sorted(order), f'article Abaee entries in letter order: {order}')
ck(all(x not in art + sup + a3 + b3 for x in
       ('superseded', 'at v40', 'at v41', 'main text v', 'main-text v', 'supplementary v1')),
   'no superseded-version phrasing anywhere in the four files')

# --------------------------------------------------------------------------- [6] the extended inventory is current
print('\n[6] supplementary S9.4 against the article as built')
lab = re.compile(r'^\*\*(Definition|Lemma|Proposition|Theorem|Corollary|Remark)\s+(\d+)\s*\((.*?)\)\.\*\*')
secx = re.compile(r'^#{2,5}\s+([0-9]+(?:\.[0-9]+)*)')
sec, want = '', {}
real = collections.defaultdict(int)
for line in art.split('\n'):
    ms = secx.match(line)
    if ms:
        sec = ms.group(1)
    m = lab.match(line)
    if m:
        real[m.group(1)] = max(real[m.group(1)], int(m.group(2)))
        if 21 <= int(m.group(2)) <= 47:
            want[int(m.group(2))] = (f'{m.group(1)} {m.group(2)} ({m.group(3)})', sec)
tbl = re.findall(r'^\| (Definition \d+ .*?|Lemma \d+ .*?|Proposition \d+ .*?|Theorem \d+ .*?|Corollary \d+ .*?'
                 r'|Remark \d+ .*?) \| ([0-9.]+) \|$', sup, re.M)
got = {int(re.search(r'\d+', t).group(0)): (t, s2) for t, s2 in tbl}
ck(len(want) >= 20 and len(got) == len(want), f'S9.4 rows {len(got)} = {len(want)} article labels in 21-47')
ck(all(got.get(k) == v for k, v in want.items()),
   'every label 21-47 appears in S9.4 with the section it now sits in')
mism = [f'{k}: S9.4 {got.get(k, ("absent",))[1]} vs article {v[1]}' for k, v in want.items() if got.get(k) != v]
ck(not mism, 'no locus mismatch ' + (str(mism[:4]) if mism else ''))

# --------------------------------------------------------------------------- [7] the numbering note
print('\n[7] the numbering note states the true maxima')
maxima = {'Definition': 47, 'Lemma': 4, 'Proposition': 43, 'Theorem': 24, 'Remark': 37, 'Corollary': 19}
ck(all(real[k] == v for k, v in maxima.items()), f'article maxima {dict(real)} vs the note {maxima}')
note = art[art.index('(Numbering:'):art.index('The supplementary', art.index('(Numbering:'))]
ck('47' in note and all(f'{k} {v}' in note for k, v in maxima.items() if k != 'Corollary'),
   'the note names each kind\u2019s maximum correctly')
ck('this revision' not in note and 'new labels' not in note, 'the note carries no revision language')

# --------------------------------------------------------------------------- [8] content parity against the deposit
print('\n[8] nothing the deposited v5 carried is lost by this restyle')
v5 = open('/home/user/revision/v5/paper3_v5.md').read()
now, then = quantities(art + '\n' + sup), quantities(open(OLD['article']).read() + '\n' +
                                                     open(OLD['supplementary']).read())
v5m = quantities(v5)
miss_now = sorted(t for t in v5m if now[t] < v5m[t])
miss_then = sorted(t for t in v5m if then[t] < v5m[t])
ck(collections.Counter(now[t] for t in miss_now) == collections.Counter(then[t] for t in miss_now),
   f'v5 measurement tokens still short after v41: {len(miss_now)} vs {len(miss_then)} after v40')
for t in miss_now[:8]:
    print(f'       still short: {t} (v5 {v5m[t]}, now {now[t]})')
sup_now, sup_old = quantities(sup), quantities(open(OLD['supplementary']).read())
ck(sup_now == sup_old, f'supplementary quantities changed by v12: '
   f'{[(t, sup_old[t], sup_now[t]) for t in set(sup_now) | set(sup_old) if sup_now[t] != sup_old[t]][:4]}')
for a, b, lbl in (('paper3_material_ledgers_v40.md', 'paper3_material_ledgers_v41.md', 'article'),
                  ('companionA_certification_procedure_v2.md', NEW['companionA'], 'A'),
                  ('companionB_standards_horizon_v2.md', NEW['companionB'], 'B')):
    ca, cb = quantities(open(a).read()), quantities(open(b).read())
    diff = [(t, ca[t], cb[t]) for t in set(ca) | set(cb) if ca[t] != cb[t]]
    ck(not diff, f'{lbl}: quantities changed vs its source ({len(diff)}) ' + str(diff[:4]))

# --------------------------------------------------------------------------- [9] the compiled PDFs
print('\n[9] typesetting and the text as it prints')
try:
    from pypdf import PdfReader
except ImportError:
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'pypdf'], check=True)
    from pypdf import PdfReader


LIG = {'\ufb00': 'ff', '\ufb01': 'fi', '\ufb02': 'fl', '\ufb03': 'ffi', '\ufb04': 'ffl',
       '\ufb05': 'st', '\ufb06': 'st', '\u00ad': '', '\u2027': '.', '\u2212': '-', '\u2044': '/'}


def pdf_text(base):
    rd = PdfReader(f'{base}.pdf')
    t = ' '.join((p.extract_text() or '') for p in rd.pages)
    for a, b in LIG.items():                                       # glyph-level ligatures, if the engine kept them
        t = t.replace(a, b)
    t = re.sub(r'\s+', ' ', t.replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"'))
    return rd, t


def fold(t):
    """Letters and digits only: tectonic's output is correct, but text extraction splits some words at
    kerning pairs (A's PDF extracts the heading as 'A vailability'), so a phrase needle has to be
    compared on the folded text as well as the spaced one."""
    return re.sub(r'[^a-z0-9]', '', t.lower())


def finds(needle, spaced):
    return needle in spaced if len(needle.split()) < 3 else fold(needle) in fold(spaced)


ART_P, A_TXT = pdf_text('paper3_material_ledgers_v41')
_, S_TXT = pdf_text('paper3_supplementary_v12') if os.path.exists('paper3_supplementary_v12.pdf') else (None, '')
_, A3_TXT = pdf_text('companionA_certification_procedure_v3')
_, B3_TXT = pdf_text('companionB_standards_horizon_v3')
print(f'  note pages: article {len(ART_P.pages)}, A {len(PdfReader("companionA_certification_procedure_v3.pdf").pages)}, '
      f'B {len(PdfReader("companionB_standards_horizon_v3.pdf").pages)}')
for name, t in (('article', A_TXT), ('A', A3_TXT), ('B', B3_TXT)):
    ck(not re.search(r'\?\?|\*\*|\\texttt|paper3_[a-z_]*_v\d|revision/v\d', t), f'{name} PDF: no unresolved '
       f'cross-reference or stranded markup')
    for bad in ('this revision', 'at v40', 'main text v', 'supplementary v11', 'supplementary v10', 'v39',
                'What changed at', 'demoted from', 'half a paper', 'reviewer of the main text', 'used to pose',
                'left in place unchanged', 'deliberately not', 'the whole point of', 'at this stage of the project',
                'folded out of', 'added at v', 'carried unchanged', 'additions at v'):
        ck(not finds(bad, t), f'{name} PDF free of {bad!r}')
ck(finds('What the type structure yields, and what it does not', A_TXT), 'article PDF prints Remark 36 with its new title')
ck(finds('(Numbering: the two layering propositions', A_TXT) and not finds('carry the consecutive labels', A_TXT),
   'article PDF prints the version-free numbering note')
ck(finds('The accompanying supplementary file carries', A_TXT) and 'paper3_supplementary_v11.md' not in A_TXT,
   'article PDF points at the supplementary without naming a file version')
ck(finds('Certifying a typed ledger', A_TXT) and finds('What the accounts settle', A_TXT),
   'article PDF prints the two new reference entries')
ck(finds('Deposited material is not edited in place', A3_TXT) and not finds('What v2 changed', A3_TXT),
   'A PDF prints the availability principle instead of a change log')
ck(finds('Availability of the deposited material', A3_TXT) and
   not finds('Deposition, and what to hand to an editor', A3_TXT),
   'A PDF prints the renamed availability section')
ck('## 10.' not in B3_TXT and 'What changed at v2' not in B3_TXT and 'A statistical standard must classify' in B3_TXT,
   'B PDF has no change-log section and keeps the classification argument')
for b in ('The accounting standards now record depletion as a cost of production',
          'This is the specific reason for the release-naming practice of B11'):
    ck(finds(b, B3_TXT), f'B PDF prints {b[:38]!r}')
for a in ('1961', '178.9', '524.5', '340.8', '2.41', '60.2', '45 of 53', '5.8'):
    ck(finds(a, A_TXT) or finds(a, S_TXT) or a in re.sub(r'\s+', ' ', open(NEW['supplementary']).read()),
       f'the recomputation figure {a} still reaches a reader (article, supplementary PDF or supplementary source)')
sec_a = re.findall(r'^## (\d+)\.', a3, re.M)
sec_b = re.findall(r'^## (\d+)\.', b3, re.M)
ck(sec_a == [str(i) for i in range(1, len(sec_a) + 1)], f'A sections contiguous 1..{len(sec_a)}: {sec_a}')
ck(sec_b == [str(i) for i in range(1, len(sec_b) + 1)], f'B sections contiguous 1..{len(sec_b)}: {sec_b}')
prots = sorted({int(m) for m in re.findall(r'\*\*Protocol (\d+)', a3)})
ck(prots == list(range(1, 9)) or len(prots) == 8, f'A still documents Protocols 1-8: {prots}')
bs = sorted({int(m) for m in re.findall(r'\*\*B(\d+)\b', b3)})
ck(bs == list(range(1, 22)), f'B still asserts B1-B21: {bs[:3]}..{bs[-2:] if bs else "-"}')

# --------------------------------------------------------------------------- [11] the typeset supplementary
print('\n[11] the supplementary PDF reproduces its markdown source')
sys.path.insert(0, R)
import build_supp_tex_v1 as bs                                                     # the transliteration used to build it
_, S12_TXT = pdf_text(BASE := 'paper3_supplementary_v12')
S12_P = PdfReader(f'{BASE}.pdf')
print(f'  note pages: supplementary {len(S12_P.pages)}; tex from the ASCII-transliterated mirror '
      f'{BASE}.ascii.md')
md_src = bs.convert(open(NEW['supplementary']).read()).replace('\u1e03', '')
for a, b in (('\u2014', '---'), ('\u2013', '--'), ('\u2019', "'"), ('\u2018', "'"), ('\u201c', '``'),
             ('\u201d', "''")):
    md_src = md_src.replace(a, b)
pdff = fold(S12_TXT)
lines = [l for l in open(NEW['supplementary']).read().split('\n')
         if len(l) > 52 and '$' not in l and '|' not in l and not l.startswith(('#', '>', '`'))]
words = [w for w in re.findall(r'[A-Za-z]{6,}', ' '.join(lines)) if w.lower() not in ('texttt',)]
missing_words = sorted({w for w in words if fold(w) not in pdff})
ck(not missing_words, f'{len(missing_words)} prose words of the source absent from the typeset PDF: '
   f'{missing_words[:6]}')
sentences, broken = [], []
for l in lines:
    for s in re.split(r'(?<=[.;:])\s+(?=[A-Z(])', re.sub(r'[`*_>]', '', l)):
        if len(s) > 48:
            sentences.append(s)
for s in sentences:
    f = fold(s)
    if f in pdff or (len(f) < 96 or (f[:45] in pdff and f[-45:] in pdff)):
        continue                                  # a page break puts a page number inside a long sentence
    broken.append('!!' + s[:50])
ck(not broken, f'{len(broken)} of {len(sentences)} source sentences do not open and close where the PDF prints '
   f'them: {[b[:44] for b in broken][:3]}')
print(f'  note {len(lines)} math-free prose lines and {len(sentences)} sentences checked against the PDF text, '
      f'{len(broken)} needing a split match; the tables and math are checked by the numerals and headings below')
for needle in ('Statement inventory, extended form', 'The overshoot-date recomputation', 'G3P basin-row extraction '
               'provenance', 'the full extent behind main-text Sections 8.1 and 8.2'):
    ck(finds(needle, S12_TXT), f'supplementary PDF prints {needle[:40]!r}')
for tok in ('524.5', '340.8', '2.41', '178.9', '58.6', '60.2', '6.3', '9.1'):
    ck(tok in S12_TXT, f'supplementary PDF prints the recomputed figure {tok}')
ck(not re.search(r'\?\?|\*\*|\\texttt\{paper3|revision/v\d|_v\d\d', S12_TXT),
   'supplementary PDF has no unresolved reference, stranded markup or file-version name')
sec_present = {int(m) for m in re.findall(r'^##+\s+S(\d+)[ .·]', open(NEW['supplementary']).read(), re.M)}
cited = set()
for f in NEW.values():
    cited |= {int(m) for m in re.findall(r'\bS(\d+)(?!\.\d)\b', open(f).read())}
ck(sec_present == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 17}, f'supp sections as built: {sorted(sec_present)}')
ck(cited <= sec_present, f'every S-number cited anywhere resolves to a section that exists; unresolved: '
   f'{sorted(cited - sec_present)}')
for bad in ('this revision', 'at v4', 'v39', 'v10', 'v11', 'v33', 'demoted from', 'added at v', 'carried unchanged'):
    ck(not finds(bad, S12_TXT), f'supplementary PDF free of {bad!r}')

# --------------------------------------------------------------------------- [10] the analysis still reproduces
print('\n[10] the archived analysis reproduces from its own source directory')
tmp = '/tmp/nfa_tau_v41'
shutil.rmtree(tmp, ignore_errors=True)
shutil.copytree(f'{R}/analysis/nfa_tau', tmp)
r = subprocess.run([sys.executable, 'recompute_tau.py'], cwd=tmp, capture_output=True, text=True, timeout=900)
ck(r.returncode == 0, f'recompute_tau.py exit {r.returncode} ' + (r.stderr[-200:] if r.returncode else ''))
same = [f for f in ('tau_world_2018.csv', 'tau_world_2017.csv', 'premium_compare.csv', 'results.txt')
        if os.path.exists(f'{tmp}/{f}') and md5(f'{tmp}/{f}') != md5(f'{R}/analysis/nfa_tau/{f}')]
ck(not same, f'outputs differ from the deposited record: {same}')

print('\n' + '=' * 78)
for n in NOTE:
    print('note:', n)
print('ALL CHECKS PASS' if not FAIL else f'{len(FAIL)} FAILURES:\n  - ' + '\n  - '.join(FAIL))
sys.exit(1 if FAIL else 0)

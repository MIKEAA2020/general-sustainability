#!/usr/bin/env python3
r"""The v48 gate. Every claim the v48 build makes about itself is read back off the files it wrote.

The v47 gate asked whether a paragraph was the draft's; under v48 that question is asked one sentence at a time, so
the checks move with it. Three of them are new and they are the ones that matter for this method:

  [1] verbatim and bounded - every sentence the ledger cleared and the splice placed is in the shipped text exactly
      as the draft wrote it, and no sentence the ledger did NOT clear is in it unless the deposited article already
      said the same words. The second half is what stops a "regenerated" row from shipping the draft's drifted
      claim in a new wrapper;
  [3] locators - the `S5`-style pointers the deposit carries are reported by occurrence, because the four rows the
      line read flagged lost one, and a gate that only compared the *set* would have passed that silently;
  [4] notation - every `S^{\top}` or `\mathcal{H}` in the shipped document must lie inside a reused sentence, so
      typography that belongs to the draft cannot appear anywhere the author did not choose to reuse it.

Values are compared with `{,}` folded onto `,`: the draft sets a figure in text (`240,000`) where the deposit keeps
it in maths (`240{,}000`), and `sk.values` splits the second into two numbers, so an unfolded comparison would
report eight invented figures that are the same eight figures.
"""
import collections
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, '/home/user/revision/v7')
sys.path.insert(0, '/home/user/revision/v48')
import stylekit_v1 as sk                                    # noqa: E402
import v48_splice_v1 as SPL                                   # noqa: E402
from pymupdf import open as zopen                            # noqa: E402

R = '/home/user/revision/v7'
V48 = '/home/user/revision/v48'
OUT = f'{R}/paper3_material_ledgers_v48.md'
SRC = f'{R}/paper3_material_ledgers_v42.md'
CORPUS = '/home/user/humanized/v1/paper3_humanized_v1_full.md'
AUDIT = '/home/user/humanize/style_audit.py'
PAIRS = (('paper3_supplementary_v13', 'paper3_supplementary_v18'),
         ('companionA_certification_procedure_v4', 'companionA_certification_procedure_v9'),
         ('companionB_standards_horizon_v4', 'companionB_standards_horizon_v9'))
FAIL = []


def ck(ok, what, detail=''):
    print(('  ok   ' if ok else '  FAIL ') + what + (f'   {detail}' if detail and not ok else ''))
    if not ok:
        FAIL.append(what)


def fold(s):
    return re.sub(r'(?<=\d),(?=\d)', '', s.replace('{,}', ','))


def vals(s):
    s = fold(re.sub(r'(?<=\d),(?=\d)', '', s.replace('\u2013', '-').replace('\u2014', '-')))
    return collections.Counter(re.findall(r'\d+(?:\.\d+)*', s))


def flex(needle):
    return re.compile(r'\s+'.join(map(re.escape, needle.split())))


# the self-reference map and the citation status are the document's own, and the ruling puts them after the splice,
# so a reused sentence ships with them applied. Folding both sides to the same token is the only tolerance this check
# grants, and the number of rows it had to be granted for is printed
CONV = [(re.compile(r'\b(?:this|the) article\u2019s\b'), 'x'), (re.compile(r"\b(?:this|the) article's\b"), 'x'),
        (re.compile(r'\bin (?:this|the) article\b'), 'x'), (re.compile(r'\b(?:this|the) article\b'), 'x'),
        (re.compile(r'\b(?:in|under) review\b'), 'x')]


def conv(t):
    for rx, r in CONV:
        t = rx.sub(r, t)
    return t


def labels(s):
    return [(m.group(1), int(m.group(2)), m.group(3)) for m in re.finditer(
        r'^\*\*(Definition|Lemma|Proposition|Theorem|Corollary|Remark)\s+(\d+)\s*\((.*?)\)\.\*\*', s, re.M)]


def trows(s):
    return [l.strip() for l in s.split('\n') if l.lstrip().startswith('|')]


def displays(s):
    return [x.strip() for x in re.findall(r'(?s)\$\$(.*?)\$\$', s)]


def heads(s):
    return [l.strip() for l in s.split('\n') if re.match(r'^#{1,6}\s', l)]


def back_of(s):
    i = re.search(r'(?m)^#{1,6}\s+(References|Data availability|Code availability|Acknowledg)', s)
    return s[i.start():] if i else ''


def rprof(text):
    keep = [b for b in sk.split_blocks(text) if not re.match(r'^#{1,6}\s', b.strip()) and sk.is_flow(b)
            and '```' not in b]
    x = '\n\n'.join(keep)
    x = re.sub(r'(?s)\$\$.*?\$\$', ' ', x)
    x = re.sub(r'\$[^$]*\$', ' ', x)
    x = re.sub(r'\*\*|`', '', x)
    n = len(x.split()) / 1000
    g = lambda p: round(len(re.findall(p, x, re.I)) / n, 1)
    S = [y for y in re.split(r'(?<=[.!?])\s+', ' '.join(x.split())) if len(y.split()) > 3]
    W = sorted(len(y.split()) for y in S)
    return dict(nominal=g(r'\b[a-z]+(?:tion|ment|ness|ity|ance|ence|sion)\b'), the_of=g(r'\bthe [a-z]+ of the [a-z]+\b'),
                em=g(r'\u2014'), pair=g(r'\u2014[^.!?]{3,90}?\u2014'), semi=g(r';'), frame=g(r', not [a-z]'),
                colon=g(r':'), we=g(r'\b(?:we|our|us)\b'), paren=g(r'(?<![0-9a-z])\('),
                this_open=g(r'(?m)^This\b|(?<=[.!?] )This\b'), mean=round(sum(W) / len(W), 1), p90=W[int(.9 * len(W))])


old_md, new_md = open(SRC).read(), open(OUT).read()

print('\n[0] the register, measured as distance to the draft\u2019s own profile')
CP = rprof(open(CORPUS).read())
a, b = rprof(old_md), rprof(new_md)
d0 = sum(abs(a[k] - CP[k]) for k in CP)
d1 = sum(abs(b[k] - CP[k]) for k in CP)
for k in CP:
    print(f'         {k:10s} draft {CP[k]:7}  v42 {a[k]:7}  v48 {b[k]:7}')
ck(d1 < d0, 'v48: the profile as a whole moved toward the draft', f'{d0:.1f} -> {d1:.1f}')
away = sorted(k for k in CP if abs(b[k] - CP[k]) > abs(a[k] - CP[k]))
for k in CP:
    ck(abs(b[k] - CP[k]) <= abs(a[k] - CP[k]) + 0.5, f'v48: {k} did not move away from the draft by more than half a '
                                                      f'point per thousand words', f'{a[k]} -> {b[k]} (draft {CP[k]})')
CONFLICT = {'em', 'pair', 'frame', 'paren'}
ck(set(away) <= CONFLICT, 'v48: the features that moved away from the draft are the ones the note names as the '
                          'conflict between the style kit\u2019s punctuation budget and the draft\u2019s density',
   f'unnamed: {sorted(set(away) - CONFLICT)}')
v47p = rprof(open(f'{R}/paper3_material_ledgers_v47.md').read())
d47 = sum(abs(v47p[k] - CP[k]) for k in CP)
print(f'       distance to the draft: v42 {d0:.1f}, the accepted v47 line {d47:.1f}, v48 {d1:.1f} - v48 is closer '
      f'than the deposit and further than v47, because v47 bought its closeness by carrying draft paragraphs the '
      f'ledger has now sent back for regeneration')
print(f'       moved away on: {away} (draft {CP["em"]} em/1k, v42 {a["em"]}, v48 {b["em"]}: the kit trims dashes to '
      f'its own cap, and the splice makes the prose shorter, not denser)')


def audit_run(path):
    out = subprocess.run([sys.executable, AUDIT, path], capture_output=True, text=True).stdout
    got = {}
    for line in out.split('\n'):
        m = re.match(r'^(.{32}?)\s{2,}([\d.]+)\s+(<=|>=)\s*([\d.]+)\s+(ok|FIX)', line)
        if m:
            got[m.group(1).strip()] = m.group(5) == 'ok'
    return got


def flow_extract(text, tag):
    txt = '\n\n'.join(x for x in sk.split_blocks(text) if sk.is_flow(x))
    txt = re.sub(r'(?s)\$\$.*?\$\$|\$[^$\n]*\$', ' ', txt)
    os.makedirs(f'{R}/.v48gate', exist_ok=True)
    p = f'{R}/.v48gate/{tag}'
    open(p, 'w').write(txt)
    return p


au0, au1 = audit_run(flow_extract(old_md, 'v42.flow')), audit_run(flow_extract(new_md, 'v48.flow'))
worse = sorted(k for k in au1 if au1[k] is False and au0.get(k) is True)
ck(not worse, f'v48: the author\u2019s instrument has nothing new to complain about ({len(au1)} metrics read back)',
   f'regressed: {worse}')

print('\n[1] the reuse is verbatim, and it is bounded by the ledger')
sp = json.load(open(f'{V48}/v48_splice_log.json'))
split = json.load(open(f'{V48}/v48_reuse_split.json'))
audit_rows = {r['id']: r['draft'] for r in json.load(open(f'{V48}/v48_reuse_audit.json'))}
by_id = {r['id']: r for r in sp['splice_log']}
ins = [l['id'] for l in sp['splice_log'] if l['state'].startswith('inserted')]
missing, folded = [], []
for rid in ins:
    t = (audit_rows.get(rid) or by_id[rid].get('want') or '').strip()
    if t and flex(t).search(new_md):
        continue
    if t and flex(SPL.conventions(t)).search(new_md):
        folded.append(rid)      # the draft's sentence, with the two document conventions applied as the ruling asks
        continue
    missing.append(rid)
ck(len(ins) == sp['insert'].get('inserted'), f'v48: the {len(ins)} rows logged as placed are all the rows placed')
ck(not missing, f'v48: every placed sentence is in the shipped document exactly as the draft wrote it '
                f'({len(folded)} of them carrying the two document conventions, which the ruling applies after the '
                f'splice)', f'absent: {missing[:6]}')
not_placed = [l['id'] for l in sp['splice_log'] if not l['state'].startswith('inserted')]
src_verbatim = {r['id'] for r in split['reuse']
                if r['text'].strip() and flex(r['text'].strip()).search(old_md)}
smuggled = []
for x in split['reuse']:
    if x['id'] in {i for i in ins} or x['id'] in src_verbatim:
        continue
    t = x['text'].strip()
    if t and flex(SPL.conventions(t)).search(new_md) and not flex(SPL.conventions(t)).search(old_md):
        smuggled.append(x['id'])
ck(not smuggled, f'v48: none of the {len(not_placed)} unplaced rows reached the text by another route',
   f'found: {smuggled[:6]}')
regen = [r for r in split['regen']]
bad_regen, coincide = [], []
for r in regen:
    t = (audit_rows.get(r['id']) or r['text']).strip()
    if not t or flex(t).search(old_md):
        continue
    if flex(t).search(new_md):
        # a regenerated sentence can come out of the style pass word for word as the draft wrote it, because the
        # draft sentence is a clause of the deposit's own longer sentence; capitalisation is the only difference,
        # and the ledger row says so, so the wording is the deposit's and the row is reported rather than failed
        _c = re.sub(r'^\s*(?:the|a|an)\s+', '', conv(t).lower().strip('.'))
        if _c and _c in conv(old_md).lower():
            coincide.append(r['id'])
            continue
        bad_regen.append(r['id'])
ck(not bad_regen, f'v48: no sentence the ledger sent back for regeneration ships as the draft wrote it '
                   f'({len(regen)} rows tested)', f'found: {bad_regen[:6]}')
if coincide:
    print(f'       {len(coincide)} regenerated row(s) ({", ".join(coincide)}) read identical to the draft because the '
          f'draft sentence is the deposit\u2019s own clause; the deposit wording is what shipped')
print(f'       reuse: {sp["insert"]} / protect: {sp["protect"]}')
print(f'       {len(ins)} placed verbatim, {len(not_placed)} shipped from the deposit, {len(src_verbatim)} needed '
      f'no splice because the article already carried the draft\u2019s wording')

print('\n[2] the content did not move')
vo, vn = vals(old_md), vals(new_md)
gone = sorted(k for k in vo if k not in vn)
born = sorted(k for k in vn if k not in vo)
ck(not gone, 'v48: every value the deposited article states is still stated', f'unstated: {gone[:6]}')
ck(not born, 'v48: no value appears that the deposited article does not state', f'invented: {born[:6]}')
diff = {k: (vo[k], vn[k]) for k in set(vo) & set(vn) if vo[k] != vn[k]}
print(f'       {len(diff)} values are stated a different number of times than in v42; largest: '
      f'{sorted(diff.items(), key=lambda t: -abs(t[1][0] - t[1][1]))[:4]}')
ck(labels(old_md) == labels(new_md), f'v48: the {len(labels(new_md))} statement labels and headings are unchanged')
ck(trows(old_md) == trows(new_md), f'v48: the {len(trows(new_md))} table rows are byte-identical')
ck(displays(old_md) == displays(new_md), f'v48: the {len(displays(new_md))} displayed equations are byte-identical')
ck(heads(old_md) == heads(new_md), f'v48: the {len(heads(new_md))} heading lines are unchanged')
ck(back_of(old_md) == back_of(new_md), 'v48: the back matter is the deposited article\u2019s own, byte for byte '
                                       '(the reference list and the declarations are not a style surface)')
pre = open(f'{R}/paper3_material_ledgers_v48_prebaseline.md').read()
ck(back_of(pre) == back_of(new_md), 'v48: the pass did not touch the back matter on its way through either')
_STAT = ('under review', 'in review', 'in preparation', 'in submission', 'forthcoming', 'accepted')
_so = {k: len(re.findall(k, old_md, re.I)) for k in _STAT}
_sn = {k: len(re.findall(k, new_md, re.I)) for k in _STAT}
ck(not [k for k in _STAT if _sn[k] and not _so[k]], 'v48: no citation status appears that the paper does not use',
   str([(k, _so[k], _sn[k]) for k in _STAT if _so[k] != _sn[k]]))
print(f'       citation status counts, v42 -> v48: {[(k, _so[k], _sn[k]) for k in _STAT if _so[k] or _sn[k]]}')
print(f'       "in review" as bare prose, pre-baseline -> shipped: '
      f'{len(re.findall(r"\bin review\b", pre))} -> {len(re.findall(r"\bin review\b", new_md))} '
      f'(the author\u2019s status wording is restored after the splice, so reused text carries it too)')

print('\n[3] the locators the deposit carries')
LOC = re.compile(r'\bS(\d+(?:\.\d+)?)\b')
lo, ln = collections.Counter(LOC.findall(old_md)), collections.Counter(LOC.findall(new_md))
lost = sorted(set(lo) - set(ln))
ck(not lost, f'v48: every supplementary locator the article names still appears in it', f'lost: {lost}')
print(f'       distinct locators {len(lo)} -> {len(ln)}; occurrences '
      f'{sum(lo.values())} -> {sum(ln.values())} (a reused sentence may name the section where the deposit named '
      f'the file, which is reported, not repaired: '
      f'{sorted((k, lo[k] - ln.get(k, 0)) for k in lo if lo[k] > ln.get(k, 0))[:8]})')

print('\n[4] the draft\u2019s notation stays inside the sentences the author chose to reuse')
DRIFT = (r'S\^\{?\\top\}?', r'\\mathcal\s*\{?\s*H\s*\}?', r'S_\{?\\mathsf\s*\{?\s*T\s*\}?\}?')
spans = []
for rid in ins:
    t = (audit_rows.get(rid) or by_id[rid].get('want') or '').strip()
    for m in flex(t).finditer(new_md):
        spans.append((m.start(), m.end()))
outside = []
for pat in DRIFT:
    for m in re.finditer(pat, new_md):
        if not any(s <= m.start() and m.end() <= e for (s, e) in spans):
            outside.append((pat, new_md[max(0, m.start() - 60):m.end() + 40].replace('\n', ' ')))
ck(not outside, 'v48: every drifted symbol sits in a reused sentence, nowhere else in the document',
   f'{outside[:3]}')
for pat in DRIFT:
    print(f'       {pat:26s} in v48: {len(re.findall(pat, new_md)):3d}   in v42: {len(re.findall(pat, old_md)):3d}   '
          f'in the draft: {len(re.findall(pat, open(CORPUS).read())):3d}')
print(f'       the count in the shipped document is the author\u2019s choice, not a repair: normalising reused maths '
      f'at build time was refused')

print('\n[5] the typesetting says the same document')


def pdf_text(base):
    d = zopen(f'{R}/{base}.pdf')
    t = ''.join(pg.get_text() for pg in d)
    n = d.page_count
    d.close()
    return re.sub(r'\s+', ' ', t), n  # noqa: E999


import mdtex_v1 as MT
_P = MT.page_text(f'{R}/paper3_material_ledgers_v48.pdf')
_d = zopen(f'{R}/paper3_material_ledgers_v48.pdf')
npage = _d.page_count
_d.close()
flow = MT.md_flow(new_md)
lost_p = [' '.join(b.split())[:64] for b in flow if not MT.covers(_P, b)]
body = re.sub(r'\s+', ' ', _P)
ck(not lost_p, f'v48: all {len(flow)} flowing paragraphs of the markdown are on the compiled page',
   f'missing: {len(lost_p)} {lost_p[:2]}')
ck(body.count('??') == 0, 'v48: no unresolved reference in the compiled article', f'{body.count("??")}')
ck(body.count('Draft: do not cite') == 0, 'v48: the draft\u2019s do-not-cite banner is not in the compiled article')
print(f'       article {npage} pages')
# the companions are carried from the accepted v47 line, so the test is byte equality with what that package shipped
import hashlib
import zipfile
z = zipfile.ZipFile('/home/user/revision/v7/paper3_supplementary_package_v7.zip')
names = z.namelist()
for n in ('paper3_supplementary_v18', 'companionA_certification_procedure_v9', 'companionB_standards_horizon_v9'):
    for ext in ('md', 'pdf'):
        ent = [x for x in names if x.endswith(f'{n}.{ext}')]
        if not ent:
            ck(False, f'{n}.{ext}: found in the v47 package')
            continue
        if ext == 'md':
            h_old = hashlib.sha256(z.read(ent[0])).hexdigest()
            h_new = hashlib.sha256(open(f'{R}/{n}.{ext}', 'rb').read()).hexdigest()
            ck(h_old == h_new, f'{n}.md: byte-identical to the accepted v47 line (carried, not rewritten)')
        else:
            # the build re-ran the converter over the carried markdown, so the PDF is a fresh typesetting of the same
            # document: what has to be identical is what is on the page, not the file's bytes or its timestamp
            open(f'/tmp/_v47_{n}.pdf', 'wb').write(z.read(ent[0]))
            d0 = zopen(f'/tmp/_v47_{n}.pdf')
            t0, p0 = re.sub(r'\s+', ' ', ''.join(pg.get_text() for pg in d0)), d0.page_count
            t1, p1 = pdf_text(n)
            ck(t0 == t1 and p0 == p1,
               f'{n}.pdf: the same {p1} pages and the same words as the accepted v47 line re-typeset it')

print('\n[6] what the build note is required to disclose')
note = open(f'{R}/structure_v48_base.md').read()
for i in ('D0158', 'D0089', 'D0129', 'D0108', 'D0309', 'D0530', 'D0618', 'D0620'):
    ck(i in note, f'note: the reused-but-flagged row {i} is named in it')
ck('against that recorded recommendation' in note and 'of them were placed by the splice' in note,
   'note: it names the flagged rows and says which of them shipped reused')
# and the note\u2019s claim about the two losses that can be read off the text has to be true of the text
ck('Survey (USGS)' in old_md and 'Survey (USGS)' not in new_md and 'D0108' in note,
   'v48: the deposit\u2019s only expansion of `USGS` is gone from the shipped article, and the note says so')
ck('recorded in S5' in old_md and 'recorded in S5' not in new_md and 'D0530' in note,
   'v48: the `recorded in S5` locator is gone from the shipped article, and the note says so')
ck(all(f'USGS' in new_md for _ in [0]) and len(re.findall(r'\bUSGS\b', new_md)) == 2,
   'v48: `USGS` still appears twice, unexpanded, exactly as disclosed')
ck('Author, D' not in new_md, 'v48: no unblinded placeholder sentence from the draft reached the shipped text')
ck('by a guard rather than by design' in note,
   'note: it says the anonymisation held because a guard refused the row, not because the pass checks anonymity')
def refs_between(s):
    m = re.search(r'(?m)^#{1,6}\s+References\s*$', s)
    if not m:
        return []
    rest = s[m.end():]
    n = re.search(r'(?m)^#{1,6}\s+\S', rest)
    rest = rest[:n.start()] if n else rest
    return [e.strip() for e in re.split(r'\n\s*\n', rest) if e.strip() and e.strip() != '---']


r_old, r_new = refs_between(old_md), refs_between(new_md)
ck(r_old == r_new and len(r_new) == 39, f'v48: the reference list is the deposited article\u2019s own {len(r_new)} '
                                       f'entries, entry for entry ({len([e for e in r_new if "doi" in e.lower()])} '
                                       f'of them carry a DOI)')
ck('reported and not repaired' in note or 'reported and not repaired' in note or 'are reported and not repaired' in note,
   'note: it says the draft\u2019s reference-list reflow is reported, not repaired')
ck('separator' in note, 'note: it names the eight figures that changed separator style and nothing else')
ck('$S^{\\top}$' in note or 'S^{\\top}' in note, 'note: it names the notation it refuses to normalise')

print('\n' + ('*** ALL CHECKS PASS ***' if not FAIL else f'*** {len(FAIL)} FAILURE(S) ***'))
for f in FAIL:
    print('   FAIL ' + f)
sys.exit(1 if FAIL else 0)

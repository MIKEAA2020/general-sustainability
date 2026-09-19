#!/usr/bin/env python3
r"""v42 line: framing accuracy, the register in the places the audit had not read, and the page width.

Four things change, and none of them is decoration.

1. **Framing.** The abstract said depletion "numbers circulate under one label while answering different
   questions". The author's starting point frames the same result more exactly: the quantities share a *unit* and
   not a *measurand*. The abstract now says so, and Section 1.1 gains the metrological step that follows from it ---
   same dimension does not imply same quantity, on the analogy of period, half-life, residence time and time
   constant. No quantity, condition or bound moves.
2. **The register in the places the v41 scan did not read.** The LaTeX header of the manuscript recited the build
   lineage (a batch name, the number of logged operations in a revision script, which directory of a clone was left
   untouched); Sections 6.5.2 and 6.5.3 twice described an editorial decision about a row instead of the row's
   status, and said "both recorded" of two disclosures that are recorded elsewhere in the same document. The code
   bundle and the analysis record are handled by `build_v42_package.py`, which is where the larger part of that
   material sat.
3. **Data availability, made true.** The statement claimed both editions of the accounts were archived with the
   bundle, while the manifest beside them says the bytes are held for re-running and must be re-fetched before any
   onward sharing. The statement now says what the deposit contains, what a reader must fetch, and which checksum
   settles it. Companion B and supplementary S17 carried the same over-statement in their own words.
4. **Geometry.** Three displayed formulas in the main text and several table cells in the companion documents ran
   past the right margin. The displays are broken at their semantic joins; the tables and the monospace spans get
   the shared kit (breaks allowed inside long identifiers, looser tolerance inside table groups, ragged-right
   `p{}` columns). Every document is then measured page by page, not merely compiled.

Every markdown edit is logged so the gate can reverse it byte for byte. Line breaks inside a display are
typesetting, so the markdown mirror keeps each display on one line.

Each edit is addressed by anchors rather than by whole quoted strings: the markdown side and the LaTeX side are
spelled differently at quotes (`"..."` against `` ``...'' ``) and at dashes, so the LaTeX span is located by its own
start and end anchors, and the build asserts that the two spans say the same thing before either is replaced.
"""
import importlib.util as _u
import json
import os
import re
import shutil
import subprocess
import sys

R = '/home/user/revision/v7'
BUILD = f'{R}/build_v42'
sys.path.insert(0, R)
sys.path.insert(0, '/home/user')


def _load(name, path):
    sp = _u.spec_from_file_location(name, path)
    mod = _u.module_from_spec(sp)
    sp.loader.exec_module(mod)
    return mod


texkit = _load('texkit', '/home/user/review/texkit_v1.py')
_k = open(f'{R}/build_v40_kernel.py').read()
_k = _k[:re.search(r'^# -+ numbers read from the run', _k, re.M).start()]
_G = globals()
exec(compile(_k, 'kernel_helpers', 'exec'), _G)
to_tex_f = _G['to_tex_f']
LOGS = {}
EM, RSQ = '\u2014', '\u2019'


def flex(s):
    return r'\s+'.join(map(re.escape, s.split()))


def cut(s, start, end):
    ms = list(re.finditer(flex(start), s))
    assert len(ms) == 1, f'start count {len(ms)} for {start[:44]!r}'
    me = re.search(flex(end), s[ms[0].start():])
    assert me, f'end {end[:44]!r} not found after start'
    return s[ms[0].start():ms[0].start() + me.end()]


def words(s):
    return set(re.findall(r'[A-Za-z]{6,}', re.sub(r'\\[a-zA-Z]+', ' ', s).replace('---', ' ').replace('--', ' ')))


def splice(text, span, new):
    i = text.index(span)
    assert text.count(span) == 1, 'span not unique'
    return text[:i] + new + text[i + len(span):]


def edit_pair(name, mdspan, texspan, new, md, tx):
    """One edit, applied to both mirrors; the LaTeX side gets the converted text, as every build in this line
    does, and the equivalence of the two spans is asserted before either is replaced."""
    a = cut(md, *mdspan)
    b = cut(tx, *texspan) if tx is not None else None
    newtex = to_tex_f(new)
    if b is not None:
        wa, wb = words(a), words(b)
        assert wa and (len(wa & wb) / len(wa) >= 0.8), f'{name}: tex span is not the md span ({sorted(wa - wb)[:4]})'
        assert words(newtex) == words(new), f'{name}: conversion dropped a word'
    rec = dict(name=name, md=[a, new, md.index(a)])
    if tx is not None:
        md = splice(md, a, new)
        tx = splice(tx, b, newtex)
        rec['tex'] = [b, newtex, tx.index(newtex)]
    else:
        md = splice(md, a, new)
    return md, tx, rec


# ===================================================================== the edits
ART_MD = [
    ('F1-abstract-opener',
     ('Depletion numbers circulate under one label', 'behind a positive scalar.'),
     ('Depletion numbers circulate under one label', 'behind a positive scalar.'),
     'Depletion indicators can carry similar units while being built to inform distinct questions. Reserve-life '
     'ratios, trend-persistence indices, and removals-only pressure scales are read as "time to depletion" '
     'although each is constructed against a different question; compensatory aggregation hides a deficit behind a '
     'positive scalar.'),
    ('F2-abstract-closer',
     ('Each depletion claim carries the predicate', 'delay-based institutional dynamics.'),
     ('Each depletion claim carries the predicate', 'delay-based institutional dynamics.'),
     'The result is a grammar for material depletion claims: each claim carries the predicate it actually '
     'establishes and no claim is carried beyond it, with an interface contract fixing the shared object with '
     'delay-based institutional dynamics.'),
    ('F3-measurand',
     ('Each of these quantities is informative about', 'typically taken to be.'),
     ('Each of these quantities is informative about', 'typically taken to be.'),
     'Each of these quantities is informative about something. None is what it is typically taken to be.\n\n'
     'The issue is not the unit. All three constructions return a number in years, and a number in years is not '
     f'yet a time to any event{EM}it is a quotient whose numerator and denominator were chosen for a question. The '
     'issue is the measurand: the quantity a construction is defined on, together with the question it is built to '
     'answer. Same dimension does not imply same quantity. Period, half-life, residence time and time constant all '
     f'carry seconds and are not interchangeable; work and torque both carry newton{RSQ}metres and are different '
     'objects. The promotion the literature records is therefore inferential rather than arithmetical: it happens '
     'when an answer to one question is read as an answer to another, and no correction of the arithmetic prevents '
     'it.'),
    ('F4-cohort-framing',
     ('the archived pull, kept in place as', 'recorded data-vintage decision'),
     ('the archived pull, kept in place as', 'recorded data-vintage decision'),
     'the archived pull, designated the headline cohort under the data-vintage rule recorded in S5'),
    ('F5-disclosures',
     ('Two disclosures accompany the headline value', 'both recorded):'),
     ('Two disclosures accompany the headline value', 'both recorded):'),
     'Two disclosures accompany the headline value:'),
    ('F6-row-status',
     ('retained rather than blanked), kept in place', 'the reserve-life construction;'),
     ('retained rather than blanked), kept in place', 'the reserve-life construction;'),
     'retained at the quoted vintage), kept as worked instances of the reserve-life construction;'),
    ('F7-data-availability',
     ('The two editions used for the sensitivity check', 'No other data were used.'),
     ('The two editions used for the sensitivity check', 'No other data were used.'),
     "The two editions used for the sensitivity check recorded in the supplementary (S17) " + EM + " the 2018 "
     "edition, with series 1961 to 2014, and the 2017 edition, with series 1961 to 2013, both distributed by the "
     "publisher under CC BY-SA 4.0 " + EM + " are held with the analysis record beside the script that computes "
     "both conventions from them and the outputs of that run, so that the computation can be re-run without a "
     "network. The tables themselves are not redistributed with this deposit: the manifest beside them gives the "
     "two retrieval commands, the sizes and the checksums of the bytes as read, and the script records the "
     "checksum it obtained, so that the copy read can be shown to be the copy analysed. The parameter tables of "
     "Section 2 are declared parameterizations. No other data were used."),
    ('F8-code-availability',
     ('The overshoot-date recomputation reported in', 'excludes data ingestion.'),
     ('The overshoot-date recomputation reported in', 'excludes data ingestion.'),
     'The overshoot-date recomputation reported in Remark 37 and in the supplementary (S17) is archived as a '
     'separate analysis record beside the reproduction bundle, whose manifest restricts that bundle to arithmetic '
     'on declared figures and excludes data ingestion.'),
]
SUP_MD = [
    ('G1-s17-notredistributed',
     ('both deposited by the publisher under CC BY-SA 4.0.', 'The current'),
     'both deposited by the publisher under CC BY-SA 4.0. The tables are held with the analysis record so that '
     'the run can be repeated without a network; they are not redistributed with the deposit, whose copy of the '
     'record carries `source/MANIFEST.md` with the two retrieval commands and the hashes that settle what was '
     'read. '),
]
A_MD = [('H1-a-manifest-record',
         ('`code/MANIFEST.md` records the script versions, the run command and', 'the scope limits,'),
         '`code/MANIFEST.md` records the checksums of the files, the run command, the environment of the recorded '
         'run and the scope limits,'),
        ]
B_MD = [('H3-b-nocopy',
         ('a re-run reproduces its three outputs byte for byte from the archived', 'requires no download.'),
         'a re-run reproduces its three outputs byte for byte from the copies archived in the record; those '
         'copies are held there for re-running and are not redistributed with the deposit, which carries the '
         'manifest, the checksums and the two retrieval commands instead.'),
        ('H4-b-examined',
         ('Neither was\nused, and both are named here so that nobody', 'search.'),
         'Neither was used, and both are named.'),
       ]

DISPLAYS = [
    # Definition: the supportable-output envelope, 69.5 pt too wide. The set-builder condition is the part that
    # runs over, so the line is broken after the colon and the rows are centred with an alignment environment:
    # a bare "\\" inside a display has no line to end, which is why a first attempt at this left the width alone.
    ('\\[ \\mathcal Y(T) \\;=\\; \\bigl\\{\\, y \\ge 0 \\;:\\; \\exists\\ \\text{an admissible trajectory on } '
     '[0,T] \\ \\text{with service at least } y \\ \\text{throughout and } x(t) \\in \\mathcal K(t) \\ \\forall t '
     '\\bigr\\} \\]',
     '\\[ \\begin{aligned} \\mathcal Y(T) \\;=\\; \\bigl\\{\\, y \\ge 0 \\;:\\;& \\exists\\ \\text{an admissible '
     'trajectory on } [0,T] \\ \\\\\n  & \\text{with service at least } y \\ \\text{throughout and } x(t) \\in '
     '\\mathcal K(t) \\ \\forall t \\bigr\\} \\end{aligned} \\]'),
    # the four-equation balance for \\dot M, 36.3 pt too wide: the four groups are kept, the sum is moved down
    ('\\[\\dot M = (R - qEN) + (-B + e_{GA} - e_{AG} + \\gamma_U U) + (-e_{GA} + e_{AG} - C^{A,\\mathrm{lim}}) '
     '+ (T - \\gamma_U U) = R - B + T - qEN - C^{A,\\mathrm{lim}},\\]',
     "\\[\\begin{aligned} \\dot M = { }& (R - qEN) + (-B + e_{GA} - e_{AG} + \\gamma_U U) \\\\\n"
     "  { }& + (-e_{GA} + e_{AG} - C^{A,\\mathrm{lim}}) + (T - \\gamma_U U) \\\\[2pt]\n"
     "  ={}& R - B + T - qEN - C^{A,\\mathrm{lim}}, \\end{aligned}\\]"),
    # Theorem: the two families of rest points, 173.1 pt too wide: one family per row, the separator quad dropped
    ('\\[ \\mathcal{R}_{\\mathrm{ext}} = \\bigl\\{ N = 0,\\ U = 0,\\ A^{\\mathrm{act}} = '
     'A^{\\mathrm{eq,intrinsic}}\\,\\sigma(A^{\\mathrm{geo}}),\\ A^{\\mathrm{geo}} \\ge 0 \\bigr\\}, \\qquad '
     '\\mathcal{R}_K = \\bigl\\{ N = K,\\ U = \\kappa_A K s/\\gamma_U,\\ A^{\\mathrm{act}} = '
     'A^{\\mathrm{eq,intrinsic}}\\,\\sigma,\\ A^{\\mathrm{geo}} \\ge 0 \\bigr\\}, \\]',
     "\\[ \\begin{aligned} \\mathcal{R}_{\\mathrm{ext}} &= \\bigl\\{ N = 0,\\ U = 0,\\ A^{\\mathrm{act}} =\n"
     "    A^{\\mathrm{eq,intrinsic}}\\,\\sigma(A^{\\mathrm{geo}}),\\ A^{\\mathrm{geo}} \\ge 0 \\bigr\\}, \\\\[2pt]\n"
     "    \\mathcal{R}_K &= \\bigl\\{ N = K,\\ U = \\kappa_A K s/\\gamma_U,\\ A^{\\mathrm{act}} =\n"
     "    A^{\\mathrm{eq,intrinsic}}\\,\\sigma,\\ A^{\\mathrm{geo}} \\ge 0 \\bigr\\}, \\end{aligned} \\]"),
]

if __name__ == '__main__':
    os.chdir(R)
    print('article v41 -> v42')
    md = open(f'{R}/paper3_material_ledgers_v41.md').read()
    tx = open(f'{R}/paper3_material_ledgers_v41.tex').read()
    log = []
    for name, mds, txs, new in ART_MD:
        md, tx, rec = edit_pair(name, mds, txs, new, md, tx)
        log.append(rec)
        print(f"  {name:22s} md {len(rec['md'][0]):5d} -> {len(new):5d} B | tex {len(rec['tex'][0]):5d} B")
    for i, (pat, rep) in enumerate(DISPLAYS):
        assert len(re.findall(re.escape(pat), tx)) == 1, f'display {i}: count'

        def payload(u):
            """The math with every construct a rewrap may introduce removed: the alignment environment, the
            alignment tab, the line break, the inter-row glue, the spacing overrides and the separator quad."""
            u = u.replace('\\ ', ' ')                     # an escaped space is a space in the source
            u = re.sub(r'\s+', '', u)
            u = re.sub(r'\\(begin|end)\{aligned\}|\\qquad|\\,|\\;|\\\\', '', u)
            return u.replace('[2pt]', '').replace('&', '').replace('{}', '')

        assert payload(pat) == payload(rep), ('display %d: math payload differs\n%s\n%s' % (i, payload(pat), payload(rep)))
        tx = tx.replace(pat, rep, 1)
        print(f'  display {i + 1}: rewrapped, math payload byte-identical')
    head_end = tx.index(r'\documentclass')
    head = texkit.header_for('Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics, '
                             'and the Semantics of Depletion Horizons', 'Main text',
                             'paper3_material_ledgers_v42.md')
    tx = head + tx[head_end:]
    # the header rewrite and the typesetting kit both change lengths above the body, so a recorded offset is not
    # portable across them: the gate therefore reverses the LaTeX side by requiring that each logged replacement
    # occurs exactly once, which is a stronger statement than an offset and cannot go stale
    tx = texkit.improve(tx)
    assert not [c for c in tx if ord(c) > 127], 'tex non-ascii'
    for e in log:                                  # record where each replacement ended up in the file that ships
        n = len(re.findall(re.escape(e['tex'][1]), tx))
        e['tex'][2] = tx.index(e['tex'][1]) if n == 1 else -1
    open(f'{R}/paper3_material_ledgers_v42.md', 'w').write(md)
    open(f'{R}/paper3_material_ledgers_v42.tex', 'w').write(tx)
    LOGS['article'] = log

    print('supplementary v12 -> v13, companions v3 -> v4')
    sup = open(f'{R}/paper3_supplementary_v12.md').read()
    slog = []
    for name, mds, new in SUP_MD:
        sup, _, rec = edit_pair(name, mds, None, new, sup, None)
        slog.append(rec)
        print(f"  {name:16s} md {len(rec['md'][0]):5d} -> {len(new):5d} B")
    open(f'{R}/paper3_supplementary_v13.md', 'w').write(sup)
    LOGS['supplementary'] = slog
    for tag, srcmd, out, pairs in (('companionA', 'companionA_certification_procedure_v3.md',
                                    'companionA_certification_procedure_v4', A_MD),
                                   ('companionB', 'companionB_standards_horizon_v3.md',
                                    'companionB_standards_horizon_v4', B_MD)):
        mds = open(f'{R}/{srcmd}').read()
        recs = []
        for name, span, new in pairs:
            mds, _, rec = edit_pair(name, span, None, new, mds, None)
            recs.append(rec)
        open(f'{R}/{out}.md', 'w').write(mds)
        LOGS[tag] = recs
        print(f'  {tag}: {len(recs)} edit(s), md {len(mds)} B')
    json.dump(LOGS, open(f'{R}/revisions_v42_formal_log.json', 'w'), indent=1)
    print('  total logged edits:', sum(len(v) for v in LOGS.values()))

    import build_companions_v1 as bc
    import build_supp_tex_v1 as bt
    import tablekit_v2
    tablekit_v2.patch(bc)          # the companion tables were sized for a 245 mm text block; A4/1in is 159 mm
    print('  table sizing rule installed in the converter')
    bt.transpile(f'{R}/paper3_supplementary_v13.md', 'paper3_supplementary_v13')
    for base in ('companionA_certification_procedure_v4', 'companionB_standards_horizon_v4'):
        title, text, _l = bc.convert(f'{R}/{base}.md', title_override=None)
        text = texkit.header_for(title, 'Companion paper', f'{base}.md') + text
        open(f'{R}/{base}.tex', 'w').write(texkit.improve(text))
        print(f'  {base}.tex written')

    os.makedirs(BUILD, exist_ok=True)
    print('\ncompiled: (rc, overfull \hbox, worst pt, right overhang pt, left overhang pt, worst page, pages)')
    status = {}
    for base in ('paper3_material_ledgers_v42', 'paper3_supplementary_v13',
                 'companionA_certification_procedure_v4', 'companionB_standards_horizon_v4'):
        r = subprocess.run(['/home/user/tools/tectonic', '--keep-logs', f'{base}.tex', '-o', BUILD],
                           cwd=R, capture_output=True, text=True, timeout=1500)
        shutil.copy(f'{BUILD}/{base}.pdf', f'{R}/{base}.pdf')
        lg = open(f'{BUILD}/{base}.log').read()
        over = [float(x) for x in re.findall(r'Overfull \\hbox \(([\d.]+)pt', lg)]
        bad = [x for x in lg.split('\n') if 'Missing character' in x or x.startswith('!')]
        assert r.returncode == 0 and not bad, f'{base}: {bad[:2] or lg[-400:]}'
        pages, right, left, worst = texkit.overhang(f'{R}/{base}.pdf')
        status[base] = dict(pages=pages, overfull=len(over), worst=max(over, default=0.0),
                            right_overhang=right, left_overhang=left, worst_page=worst)
        print(f'  {base:40s} rc={r.returncode} overfull={len(over):2d} worst={max(over, default=0.0):6.1f}pt '
              f'right={right:6.1f}pt left={left:5.1f}pt page={worst:2d} pages={pages}')
    json.dump(status, open(f'{R}/geometry_v42.json', 'w'), indent=1)
    print('\nnext: build_v42_package.py, then verify_v42_build.py')

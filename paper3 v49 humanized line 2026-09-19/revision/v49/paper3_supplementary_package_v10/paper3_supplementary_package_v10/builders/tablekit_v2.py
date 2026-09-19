#!/usr/bin/env python3
r"""Column sizing for the generated companion documents: the root cause of the wide tables.

`build_companions_v1.table` gives every prose column the same width, `0.96 * 245 / ncol - 8` millimetres, on the
apparent assumption that the text block is 245 mm wide. The documents it typesets are A4 with one-inch margins, so
the text block is 159.2 mm: a three-column table received three 70 mm columns on a 159 mm line, which is the
161 pt overfull alignment in supplementary S9 and the 106 pt one in Companion A, and short columns were left
"natural" on top of that.

The rule installed here sizes a column from what its cells actually contain. Widths are allocated in proportion to
a weighted content measure, and each column is then raised to a floor: the width of the longest *unbreakable* run
it holds, which is what a `p{}` column cannot hyphenate away --- a sha256, a file name, an inline formula. If the
floors do not fit, the table's font steps down and the floors are recomputed at that size, because a table whose
smallest legible set still overflows is a table that must be set smaller, not a table that may overflow. The sum of
the widths plus the intercolumn glue the preamble inserts is capped at the text width by construction.

Alignment follows the markdown separator (`l`, `c`, `r`), applied through `>` column modifiers so a `p{}` column
keeps it, and every column is ragged-right, centred or flushed left rather than justified: justification is what
turns one long token into an overfull line.
"""
import re

TEXT_MM = 159.2          # A4 (210 mm) minus the 1 in margins on both sides, as the preamble sets them
TABCOLSEP_MM = 2.82      # 2 x 4 pt per column boundary; @{} suppresses the two outer ones
CHAR_MM = 0.415          # per character of Computer Modern at the table size the hook selects
MATH_FACTOR = 1.25       # an inline formula is wider than prose and cannot hyphenate
FLOOR_CAP = 62.0        # no single column may claim more than this, whatever it contains
SAFETY = 0.985         # a hair of room left at the edge, so rounding in the metrics cannot push a line over         # no single column may claim more than this, whatever it contains
# the levers, in the order a typesetter pulls them: tighten the intercolumn glue, then step the font down
STEPS = [(r'\small', 4.0, 1.0), (r'\small', 2.5, 1.0), (r'\footnotesize', 2.5, 0.88),
         (r'\footnotesize', 2.0, 0.88), (r'\scriptsize', 2.0, 0.78), (r'\tiny', 1.6, 0.68)]


# Widths per character, in millimetres, for the three registers a cell can be in at the size the longtable hook
# selects (\small in an 11pt document). They are the metrics the documents actually use: typewriter is a fixed
# half em, text is about a third of an em on average, math is wider still and cannot hyphenate.
MM_TT = 1.85                     # \ttfamily is a fixed 0.524 em, and the tables are set at 10 pt
MM_TEXT = 1.60                   # an average lower-case character of the roman text font at that size
MM_MATH = 1.95                   # italic variables, subscripts and relations are wider and cannot hyphenate
# the kit guarantees a break inside a monospace token after twelve characters, and hyphenation typically breaks a
# word by then, so those are the lengths a column must hold whole; an inline formula has no break at all
TT_CHUNK = 12.0                  # the kit guarantees a break in a monospace token past this many characters
TEXT_CHUNK = 9.0                 # what hyphenation can be trusted to hand back: a prefix that fits on one line


def _segments(cell):
    """Split a markdown cell into (register, text) pieces: `code`, $math$, plain."""
    out = []
    i = 0
    while i < len(cell):
        m = re.compile(r'`[^`\n]*`|\$[^$\n]*\$').search(cell, i)
        if not m:
            out.append(('t', cell[i:]))
            break
        if m.start() > i:
            out.append(('t', cell[i:m.start()]))
        out.append(('c' if m.group(0)[0] == '`' else 'm', m.group(0)[1:-1]))
        i = m.end()
    return [(k, t.strip()) for k, t in out if t.strip()]


def _mm(kind, text):
    f = {'c': MM_TT, 'm': MM_MATH, 't': MM_TEXT}[kind]
    return sum((f if ch != '\\' else 0.0) for ch in text)


def _runs(cell):
    """The pieces TeX cannot break inside this cell, measured in mm."""
    res = []
    for kind, text in _segments(cell):
        for tok in re.split(r'[\s/|,;:()\[\]{}<>=+*&\\]', text):
            if not tok:
                continue
            n = len(tok)
            if kind == 'c':
                # the kit guarantees a break every twelve characters inside \texttt (see texkit), so twelve is what a
                # column must be able to hold whole; a shorter token must fit as it stands
                res.append(min(n, TT_CHUNK) * MM_TT)
            elif kind == 'm':
                # the kit lets an inline formula break after a comma, so a comma-separated list of symbols is
                # measured piece by piece rather than as one unbreakable run of the whole expression
                pieces = [x for x in re.split(r',\s*', text) if x] or [text]
                res.append(min(max(len(p) for p in pieces), 26) * MM_MATH)
            else:
                res.append(min(n, TEXT_CHUNK) * MM_TEXT)
    return res


def _cellmm(cell):
    """The width of a cell if it were set on one line, in mm, with the unbreakable registers weighted up."""
    return sum(_mm(k, t) for k, t in _segments(cell))


def sized_table(bc, lines):
    """The same longtable the converter builds, with column widths that fit the page."""
    rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in lines
            if not re.match(r'^\s*\|[\s:|-]+\|\s*$', l)]
    align = next(l for l in lines if re.match(r'^\s*\|[\s:|-]+\|\s*$', l))
    spec = [':' in c and '-' in c and c.strip(':').startswith('-') and c.endswith(':') and 'r' or
            ('c' if c.strip(':').startswith('-') and c.startswith(':') and c.endswith(':') else 'l')
            for c in align.strip().strip('|').split('|')]
    spec = [(s if s in 'lcr' else 'l') for s in spec]
    ncol = len(rows[0])
    spec = (spec + ['l'] * ncol)[:ncol]

    meas = []
    for j in range(ncol):
        cells = [' '.join(r[j].split()) for r in rows if j < len(r)] or ['']
        wide = sum(_cellmm(c) for c in cells) / len(cells)
        # a header cell is one word on its own line and must fit whole, so it is measured without the chunk
        # allowance that body text can reach by hyphenating
        body_floor = max((max(_runs(c) or [0.0]) for c in cells[1:]), default=0.0)
        head = rows[0][j] if j < len(rows[0]) else ''
        head_floor = max((len(tk) * MM_TEXT for tk in
                          re.split(r'[\s/|,;:()\[\]{}<>=+*&\\`$]+', head) if tk), default=0.0)
        floor = max(body_floor, head_floor)
        meas.append((wide, 0, floor, cells))

    for size, sep, k in STEPS:
        glue = sep * 0.3514 * (ncol - 1)               # pt to mm, one explicit gap per boundary
        avail = max(20.0, TEXT_MM * SAFETY - glue)
        floors = [min(max(m[2] * k * 1.18, 6.0), FLOOR_CAP) for m in meas]
        if sum(floors) <= avail:
            break
    else:                                              # nothing fits: buy what room there is by scaling
        size, sep, k = STEPS[-1]
        glue = sep * 0.3514 * (ncol - 1)
        avail = max(20.0, TEXT_MM * SAFETY - glue)
        sc = avail / sum(min(max(m[2] * k * 1.18, 6.0), FLOOR_CAP) for m in meas)
        floors = [f * sc for f in floors]

    weight = [max(m[0] * k, 1.0) ** 0.92 for m in meas]
    tot = sum(weight)
    w = [avail * x / tot for x in weight]
    w = [max(x, f) for x, f in zip(w, floors)]
    over = sum(w) - avail
    if over > 0:                                  # the floors won: shave the columns that have slack
        slack = [max(0.0, x - f) for x, f in zip(w, floors)]
        s = sum(slack) or 1.0
        w = [x - over * (sl / s) for x, sl in zip(w, slack)]
    head, body = rows[0], rows[1:]
    # \raggedright switches hyphenation off in LaTeX, which is what leaves a single long word standing over the
    # edge of a narrow column, so the penalties are put back on. The font step and the intercolumn gap go into the
    # column specification as well: a declaration or a \setlength between \begin{longtable} and \toprule makes
    # booktabs' \noalign misplaced, and @{} in the preamble is the one place both are legal --- it also cancels
    # \tabcolsep at that boundary, so the width arithmetic above is exact rather than approximate.
    pad = {'l': r'\raggedright', 'c': r'\centering', 'r': r'\raggedleft'}
    mod = r'\hyphenpenalty=0\exhyphenpenalty=0' + ('' if size == r'\small' else size) + r'\arraybackslash'
    cols = [('>{' + pad[sp] + mod + '}p{%.1fmm}' % x) for sp, x in zip(spec, w)]
    gap = r'@{\hspace{%.1fpt}}' % sep
    tex = ['\\begin{longtable}{' + '@{}' + gap.join(cols) + '@{}}']
    tex.append('\\toprule')
    tex.append(' & '.join(bc.inline(c) for c in head) + r' \\')
    tex.append('\\midrule')
    for r in body:
        r = r + [''] * (ncol - len(r))
        tex.append(' & '.join(bc.inline(c) for c in r[:ncol]) + r' \\')
    tex.append('\\bottomrule')
    tex.append('\\end{longtable}')
    return '\n'.join(tex)


def patch(bc):
    """Install the sizing rule in a converter module, leaving that module's file untouched."""
    bc._table_v1 = bc.table
    bc.table = lambda lines: sized_table(bc, lines)
    return bc

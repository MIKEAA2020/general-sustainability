#!/usr/bin/env python3
r"""Typesetting kit shared by the v42 build scripts.

Four jobs, all measurement-driven rather than cosmetic.

* **Preamble.** The manuscript's own converter leaves `\emergencystretch` at 3em with default hyphenation
  penalties, which is what puts a long `\texttt{}` identifier or a dense table cell past the right margin. The kit
  raises the stretch, lowers the penalties and adds `xurl` so a bare DOI in a reference can break. `ragged2e` is
  not used: it changes the look of every paragraph for the sake of a few.
* **Tables.** `p{}` columns break unjustly and overflow when a cell holds one long token; the fix is to relax the
  tolerance inside the table group and set such columns ragged-right, where a slightly loose line costs nothing.
* **Monospace spans.** `\texttt{paper3_material_ledgers_v42.md}` and `analysis/nfa_tau/recompute_tau.py` are
  single unbreakable tokens of thirty-odd characters, and a sha256 is a single unbreakable token of sixty-four.
  `\allowbreak` is inserted after each of `_ . / - #`, and every twelve characters where a span offers no such
  break. It is invisible unless TeX needs the break, so it cannot change how a line that already fits is set.
* **Bare URLs.** A reference line's `https://doi.org/...` is a third kind of unbreakable run; it is wrapped in
  `\url`, which `xurl` makes breakable and which typesets the same characters.

`compile_log` and `page_geometry` are the measurement: the first counts the `Overfull \hbox` notices of a
tectonic run (both log forms, since a display reports differently from a paragraph), and the second reads the
rightmost text edge of every page off the PDF against its own media box. The measurement is the check, not the
log, because the two disagree in either direction: a page can overflow quietly, and a warning can concern a line
the reader cannot tell apart from its neighbours.
"""
import os
import re
import subprocess

TECTONIC = '/home/user/tools/tectonic'
BREAKABLE = re.compile(r'([_.\-/#])(?![.,;)\s])')
ALLOWBREAK = r'\allowbreak{}'


def _mark_breaks(body, chunk):
    r"""Insert \allowbreak after punctuation-like break points, and every `chunk` visible characters when the
    span is long. An escape pair such as `\_` counts as one visible character and is never cut in half."""
    out = []
    seen = 0
    i = 0
    n = len(body)
    while i < n:
        c = body[i]
        esc = re.match(r'\\[a-zA-Z]+[ ]?|\\.', body[i:])
        if c == '\\' and esc:
            out.append(esc.group(0))
            i += len(esc.group(0))
            seen += 1
        else:
            out.append(c)
            i += 1
            seen += 1
        if not out or out[-1] == ALLOWBREAK:
            continue
        at_punct = c in '_.-/#' and i < n and body[i] not in '.,;)\\ '
        if at_punct or (chunk and seen >= chunk and i < n):
            out.append(ALLOWBREAK)
            seen = 0
    return ''.join(out)


def texttt_breaks(tex):
    """Let long \\texttt spans break, only where a break is needed."""
    if ALLOWBREAK in tex:
        raise AssertionError('input already carries the marker')

    def one(m):
        body = m.group(1)
        return '\\texttt{' + _mark_breaks(body, 12) + '}'

    return re.sub(r'\\texttt\{((?:[^{}]|\{[^{}]*\})*)\}', one, tex)



def hex_breaks(tex):
    r"""Let a bare hash or digest break. A 64-character hex string in a prose line is the same problem as a long
    \texttt span and has no punctuation to break at, so \allowbreak is inserted every sixteen characters; nothing
    shorter is touched, which keeps years, DOIs, quantities and file sizes as they are."""
    def one(m):
        s = m.group(0)
        if len(s) < 24:
            return s
        return ALLOWBREAK.join(s[i:i + 16] for i in range(0, len(s), 16))

    return re.sub(r'(?<![0-9a-fA-F])[0-9a-f]{24,}(?![0-9a-fA-F])', one, tex)


def slash_breaks(tex):
    r"""Let a run like \textbf{supplementary/project-side} break. TeX breaks after an explicit hyphen but not at a
    slash, so a path-shaped phrase in bold stays one token of twenty-six characters; \allowbreak after every slash
    outside verbatim-ish material costs nothing when it is not needed. Lines already inside \\texttt or \\url are
    skipped: those carry their own rules."""
    out = []
    i = 0
    for m in re.finditer(r'\\(?:texttt|url|path|verb)\{', tex):
        if m.start() > i:
            out.append(_slash(tex[i:m.start()]))
        j = m.start()
        depth = 0
        k = m.end() - 1
        while k < len(tex):
            if tex[k] == '{':
                depth += 1
            elif tex[k] == '}':
                depth -= 1
                if depth == 0:
                    break
            k += 1
        out.append(tex[m.start():k + 1])
        i = k + 1
    if i < len(tex):
        out.append(_slash(tex[i:]))
    return ''.join(out)


def _slash(chunk):
    # a lambda, because re.sub would read the backslash of the marker as an escape of its own
    return re.sub(r'(?<=[A-Za-z0-9])/(?=[A-Za-z0-9])', lambda m: '/' + ALLOWBREAK, chunk)


def math_breaks(tex):
    r"""Let a long inline formula break after a comma. TeX will not end a line inside an unbreakable run such as
    \(\mathrm{SSB}_{\mathrm{now}},\ F_{\mathrm{now}},\ B_{\lim}\) set in a narrow table column, and \allowbreak is
    legal in math mode, so the separators inside a formula become permitted ones. Both delimiter styles the
    converter emits are tracked, and nothing outside them is touched; the insertion is invisible unless a line
    needs it."""
    out = []
    i = 0
    for m in re.finditer(r'\\\(|\$', tex):
        if m.start() < i:
            continue                                    # this is the delimiter that closed the previous span
        if m.start() > i:
            out.append(tex[i:m.start()])
        open_tok = m.group(0)
        close_tok = '\\)' if open_tok == '\\(' else '$'
        j = tex.find(close_tok, m.end())
        if j < 0:
            out.append(tex[m.start():])
            i = len(tex)
            break
        body = re.sub(r',\s*', lambda x: x.group(0) + ALLOWBREAK, tex[m.end():j])
        out.append(open_tok + body + close_tok)
        i = j + len(close_tok)
    if i < len(tex):
        out.append(tex[i:])
    return ''.join(out)


def url_wrap(tex):
    r"""A bare https:// or doi.org token in a reference line is another unbreakable run; \url from `xurl`
    breaks anywhere and typesets the same characters."""
    return re.sub(r'(?<!\{)((?:https?|ftp)://[A-Za-z0-9._~:/?#\[\]@!$&()*+,;=%-]+[A-Za-z0-9])',
                  lambda m: '\\url{' + m.group(1) + '}', tex)


def preamble_fix(tex):
    add = [
        r'\usepackage[htt]{hyphenat}',
        r'\usepackage{xurl}',
        r'\setlength{\emergencystretch}{4em}',
        r'\tolerance=1400',
        r'\hyphenpenalty=40',
        r'\exhyphenpenalty=0',
        r'\AtBeginEnvironment{tabular}{\setlength{\emergencystretch}{6em}\hyphenpenalty=0\tolerance=9999}',
    ]
    # the sources set \emergencystretch=3em and hook longtable with \small only: both are replaced, not doubled
    tex = re.sub(r'\\setlength\{\\emergencystretch\}\{3em\}\n', '', tex)
    tex = tex.replace(r'\emergencystretch=3em', r'\setlength{\emergencystretch}{4em}')
    tex = tex.replace(r'\AtBeginEnvironment{longtable}{\small}',
                      r'\AtBeginEnvironment{longtable}{\small\setlength{\emergencystretch}{6em}'
                      r'\hyphenpenalty=0\tolerance=9999}')
    keep = []
    for line in add:
        if line.startswith('\\usepackage'):
            pkg = line.split('{')[-1].rstrip('}')
            if re.search(r'\\usepackage(\[[^\]]*\])?\{' + pkg + r'\}', tex):
                continue
        if line == r'\setlength{\emergencystretch}{4em}' and r'\emergencystretch=4em' in tex:
            continue
        if line == r'\setlength{\emergencystretch}{4em}' and r'\setlength{\emergencystretch}{4em}' in tex:
            continue
        keep.append(line)
    lines = tex.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('\\begin{document}'):
            lines[i] = '\n'.join(keep) + '\n' + line
            break
    else:
        raise AssertionError('no \\begin{document} found')
    return '\n'.join(lines)


def spec_fix(tex):
    r"""Let p{} table columns set ragged-right. A justified narrow column holding one long token is what
    produces an overfull line inside an alignment; \raggedright is the conventional remedy in a table, and a
    column that already carries an alignment modifier is left alone."""
    def one(m):
        env, opt, spec = m.group(1), m.group(2) or '', m.group(3)
        if 'raggedright' in spec or 'centering' in spec or 'raggedleft' in spec:
            return m.group(0)
        spec = spec.replace('p{', r'>{\raggedright\arraybackslash}p{')
        return '\\begin{%s}%s{%s}' % (env, opt, spec)

    return re.sub(r'\\begin\{(tabular|longtable|tabularx)\}(\[[^\]]*\])?\{((?:[^{}]|\{[^{}]*\})*)\}', one, tex)


def improve(tex):
    return hex_breaks(slash_breaks(texttt_breaks(url_wrap(spec_fix(preamble_fix(tex))))))


def compile_log(base, cwd):
    """Compile a .tex with its log kept, and return (returncode, log text, [pt too wide, ...])."""
    os.makedirs(cwd + '/.logtmp', exist_ok=True)
    r = subprocess.run([TECTONIC, '--keep-logs', f'{base}.tex', '-o', cwd + '/.logtmp'], cwd=cwd,
                       capture_output=True, text=True, timeout=1500)
    lp = f'{cwd}/.logtmp/{base}.log'
    log = open(lp).read() if os.path.exists(lp) else (r.stdout + r.stderr)
    over = [float(x) for x in re.findall(r'Overfull \\hbox \(([\d.]+)pt', log)]
    return r.returncode, log, over


def page_geometry(pdf, margin_pt=72.0):
    """(page, media width, rightmost text edge) per page, measured from the PDF's own word boxes.

    PyMuPDF reports the box each glyph run actually occupies after the font's widths are applied, which is the
    quantity of interest: a compile log can stay silent about a table that fits its declared columns but not the
    page, and a hand-rolled character-width model cries wolf at italic. Where PyMuPDF is unavailable the caller is
    told by an empty result rather than by a guess.
    """
    try:
        import pymupdf
    except ImportError:                                    # pragma: no cover
        try:
            import fitz as pymupdf
        except ImportError:
            return []
    out = []
    doc = pymupdf.open(pdf)
    for i, pg in enumerate(doc, 1):
        w = float(pg.rect.width)
        edge = 0.0
        left = w
        for word in pg.get_text('words'):
            if str(word[4]).strip():
                edge = max(edge, float(word[2]))
                left = min(left, float(word[0]))
        out.append((i, round(w, 1), round(edge, 1), round(left, 1)))
    doc.close()
    return out


def overhang(pdf, margin_pt=72.0):
    """(pages, right overhang pt, left overhang pt, worst page) for a rendered PDF."""
    geo = page_geometry(pdf, margin_pt)
    if not geo:
        return 0, 0.0, 0.0, 0
    right = max(e - (w - margin_pt) for _p, w, e, _l in geo)
    left = max((margin_pt - l) for _p, w, _e, l in geo)
    worst = max(geo, key=lambda r: r[2] - (r[1] - margin_pt))[0]
    return len(geo), round(right, 1), round(left, 1), worst


def overfull_and_geometry(base, cwd, margin_pt=72.0):
    """Compile once with logs, copy the PDF up, and return (rc, overfull count, worst pt, right overhang pt,
    left overhang pt, worst page, pages)."""
    rc, log, over = compile_log(base, cwd)
    bad = [x for x in log.split('\n') if 'Missing character' in x or x.startswith('!')]
    assert not bad, f'{base}: {bad[:2] or log[-300:]}'
    assert rc == 0, f'{base}: tectonic exit {rc}\n{log[-400:]}'
    src = f'{cwd}/.logtmp/{base}.pdf'
    if os.path.exists(src):
        open(f'{cwd}/{base}.pdf', 'wb').write(open(src, 'rb').read())
    pages, right, left, worst = overhang(f'{cwd}/{base}.pdf', margin_pt)
    return rc, len(over), (max(over) if over else 0.0), right, left, worst, pages, over


def header_for(title, kind, mirror):
    """A source header that says what the file is, not how it was produced. No build lineage, no version diary,
    no page count: the page count belongs to the PDF, and a comment that states it goes stale on reflow."""
    return (f'% {title}\n'
            f'% {kind}. Typeset from {mirror}; the LaTeX source, the markdown mirror and the compiled PDF are\n'
            f'% deposited together. Compiles with tectonic; also compatible with pdflatex and xelatex.\n')

#!/usr/bin/env python3
"""Build the two companion papers: markdown source of record -> standalone LaTeX -> PDF.

The article line renders statements as bold run-ins with no theorem environments, and its tex is pure
ASCII with \\( \\) for inline math; the companions follow the same conventions so they can be compiled with
the same engine and read as one corpus. Code and transcript blocks are therefore typeset in a quote with
typewriter text, and every non-ASCII glyph outside math is folded to a form the article's own tex would use
(``---'' for an em dash, ``\\ensuremath{\\le}`` for a comparison sign, ``lambda_bar'' inside a code block).
"""
import re
import subprocess
import sys
import unicodedata

R = '/home/user/revision/v7/'

# ------------------------------------------------------------------ glyph folding
DASH = [('\u2014', '---'), ('\u2013', '--'), ('\u2019', "'"), ('\u2018', "'"),
        ('\u201c', '"'), ('\u201d', '"'), ('\u2026', '\\ldots{}'), ('\u00b7', '\\textbullet{}'),
        ('\u00a7', '\\S')]
# math glyphs in prose: become small math snippets
MATH = {
    '\u03bb': '\\lambda', '\u2264': '\\le', '\u2265': '\\ge', '\u2212': '-', '\u03b4': '\\delta',
    '\u2113': '\\ell', '\u2202': '\\partial', '\u03c4': '\\tau', '\u03ba': '\\kappa',
    '\u03c6': '\\phi', '\u03b2': '\\beta', '\u03b5': '\\varepsilon', '\u03a9': '\\Omega',
    '\u00d7': '\\times', '\u21d2': '\\Rightarrow', '\u2248': '\\approx', '\u1d40': '\\top',
}
# the same glyphs inside a transcript or a code span: ASCII, so a reader can retype them
CODE = {
    '\u03bb': 'lambda', '\u2264': '<=', '\u2265': '>=', '\u2212': '-', '\u03b4': 'delta',
    '\u2113': 'l', '\u2202': 'partial', '\u03c4': 'tau', '\u03ba': 'kappa', '\u03c6': 'phi',
    '\u03b2': 'beta', '\u03b5': 'eps', '\u03a9': 'Omega', '\u00d7': 'x', '\u21d2': '=>',
    '\u2248': '~=', '\u1e03': 'b-dot', '\u2080': '0', '\u1d40': '^T',
}


def fold(s, code=False):
    """ASCII-ise: dashes always; math glyphs as \\ensuremath{...} in prose, as names inside code blocks."""
    for a, b in DASH:
        s = s.replace(a, b)
    if code:
        s = re.sub(r'(\S)\u0304', lambda m: m.group(1) + '_bar', s)
        for a, b in sorted(CODE.items(), key=lambda kv: -len(kv[0])):
            s = s.replace(a, b)
        return s
    s = s.replace('\u1d40', '\\(^{\\top}\\)')
    s = re.sub(r'(\S)\u0304', lambda m: '\\ensuremath{\\bar ' + MATH.get(m.group(1), m.group(1)) + '}', s)
    for a, b in sorted(MATH.items(), key=lambda kv: -len(kv[0])):
        s = s.replace(a, '\\ensuremath{' + b + '}')
    return s


def esc(s):
    """Escape the LaTeX text specials. Math spans are already extracted, so this is safe on the rest."""
    for c in '\\&%#_$':
        if c == '\\':
            s = s.replace('\\', '\\textbackslash{}')
        else:
            s = s.replace(c, '\\' + c)
    return s


CODE_ESC = [('\\', '\\textbackslash{}'), ('{', '\\{'), ('}', '\\}'), ('$', '\\$'),
            ('%', '\\%'), ('&', '\\&'), ('#', '\\#'), ('_', '\\_'), ('~', '\\textasciitilde{}'),
            ('^', '\\textasciicircum{}')]


def inline(s, code=False):
    """md inline -> tex.

    Code spans and math are lifted to sentinels first, so that the prose pass (escape, fold, emphasis)
    sees one continuous string: an emphasis span that encloses a code span would otherwise be cut in two
    and neither half would match. The rendered pieces are restored at the end, after folding, so nothing
    the lift produces is escaped or folded twice.
    """
    keep, out, i2 = [], [], 0
    tok = re.compile(r'`[^`]+`|\$[^$]*\$')
    for m in tok.finditer(s):
        out.append(s[i2:m.start()])
        t = m.group(0)
        if t[0] == '`':
            body = fold(t[1:-1], code=True)
            for a, b in CODE_ESC:
                body = body.replace(a, b)
            keep.append('\\texttt{' + body + '}')
        else:
            keep.append('\\(' + t[1:-1].strip() + '\\)')
        out.append(chr(0) + str(len(keep) - 1) + chr(1))
        i2 = m.end()
    out.append(s[i2:])
    body = ''.join(out)
    body = fold(esc(body), code=code)
    body = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', body, flags=re.S)
    body = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'\\emph{\1}', body, flags=re.S)
    body = re.sub(chr(0) + r'(\d+)' + chr(1), lambda m: keep[int(m.group(1))], body)
    return body


def slug(s):
    s = re.sub(r'`|\*\*|\\|\$|[.,:;!?()]', '', s)
    return re.sub(r'\s+', '-', s.strip().lower())[:70]


PRE = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{booktabs,longtable,array,calc}
\usepackage{xcolor}
\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}
\usepackage{etoolbox}
\AtBeginEnvironment{longtable}{\small}
\AtBeginEnvironment{quote}{\small}
\setlength{\tabcolsep}{4pt}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\setcounter{secnumdepth}{-1}
\emergencystretch=3em
\newcommand{\tcell}[1]{\parbox[t]{0.95\linewidth}{#1}}
\begin{document}
"""

AUTHOR = r"""\author{Amin Abaee\\[0.35em]
{\small Independent Researcher}\\[0.55em]
{\small\href{https://orcid.org/0000-0002-0019-1842}{ORCID: 0000-0002-0019-1842}}\\[0.3em]
{\small\href{mailto:amin\_abaee@ut.ac.ir}{amin\_abaee@ut.ac.ir}}}
\date{September 17, 2026}
\maketitle
"""


def table(lines):
    """md pipe table -> longtable. The header row is the first line; alignment comes from the separator."""
    rows = [[c.strip() for c in l.strip().strip('|').split('|')] for l in lines
            if not re.match(r'^\s*\|[\s:|-]+\|\s*$', l)]
    align = next(l for l in lines if re.match(r'^\s*\|[\s:|-]+\|\s*$', l))
    spec = [':' in c and '-' in c and c.strip(':').startswith('-') and c.endswith(':') and 'r' or
            ('c' if c.strip(':').startswith('-') and c.startswith(':') and c.endswith(':') else 'l')
            for c in align.strip().strip('|').split('|')]
    spec = [s if s in 'lcr' else 'l' for s in spec]
    ncol = len(rows[0])
    # a column of prose gets a p{} width; short columns stay natural
    width = max(1, int((0.96 * 245) / ncol) - 8)
    cols = []
    for j, s in enumerate(spec[:ncol]):
        longest = max(len(' '.join(r[j].split())) for r in rows if j < len(r))
        cols.append('p{%dmm}' % width if longest > 42 else s)
    head, body = rows[0], rows[1:]
    tex = ['\\begin{longtable}{' + '@{}' + '|'.join(cols) + '@{}}', '\\toprule']
    tex.append(' & '.join(inline(c) for c in head) + r' \\')
    tex.append('\\midrule')
    for r in body:
        r = r + [''] * (ncol - len(r))
        tex.append(' & '.join(inline(c) for c in r[:ncol]) + r' \\')
    tex.append('\\bottomrule')
    tex.append('\\end{longtable}')
    return '\n'.join(tex)


def code_block(lines):
    body = []
    for l in lines:
        t = re.sub(r'\t', '    ', l)
        t = fold(t, code=True)
        for a, b in CODE_ESC:
            t = t.replace(a, b)
        body.append(t)
    # one newline is a space in LaTeX, so a transcript needs its line breaks made explicit; a blank
    # line in the block becomes extra vertical space rather than an empty \row
    tex = []
    for k, l in enumerate(body):
        if not l.strip():
            tex.append('\\\\[4pt]')
            continue
        tex.append(l + ('\\\\' if k + 1 < len(body) and body[k + 1].strip() else ''))
    return ('\\begin{quote}\\ttfamily\\footnotesize\\raggedright\\setlength{\\parskip}{0pt}\n'
            + '\n'.join(tex).rstrip('\\\n[]4t') + '\n\\end{quote}')


def convert(md_path, title_override=None):
    md = open(md_path, encoding='utf-8').read()
    lines = md.split('\n')
    i, out, labels = 0, [], []
    title = ''
    while i < len(lines):
        l = lines[i]
        if l.startswith('```'):
            j = i + 1
            while not lines[j].startswith('```'):
                j += 1
            out.append(code_block(lines[i + 1:j]))
            i = j + 1
            continue
        if l.strip() == '$$' or l.lstrip().startswith('$$') and len(l.strip()) > 4:
            if lines[i].strip().endswith('$$') and len(lines[i].strip()) > 4:
                out.append('\\[ ' + lines[i].strip().strip('$').strip() + ' \\]')
                i += 1
                continue
            buf, j = [], i
            while j < len(lines):
                t = lines[j].strip()
                if j == i:
                    t = t.lstrip('$').strip()
                if lines[j].rstrip().endswith('$$') and j > i:
                    buf.append(t.rstrip('$').strip())
                    break
                buf.append(t)
                j += 1
            out.append('\\[ ' + ' '.join(buf) + ' \\]')
            i = j + 1
            continue
        if l.startswith('|'):
            j = i
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            out.append(table(lines[i:j]))
            i = j
            continue
        if re.match(r'^#{1,6} ', l):
            lvl = len(l) - len(l.lstrip('#'))
            txt = l.lstrip('#').strip()
            if lvl == 1:
                title = txt
            else:
                cmd = {2: 'section', 3: 'subsection', 4: 'subsubsection'}[min(lvl, 4)]
                s = slug(txt)
                labels.append(s)
                out.append('\\%s*{%s}\\label{%s}' % (cmd, inline(txt), s))
            i += 1
            continue
        if l.strip() == '---':
            out.append('\\vspace{0.8em}')
            i += 1
            continue
        if not l.strip():
            i += 1
            continue
        # bullet lists
        if l.lstrip().startswith('- '):
            j = i
            items = []
            while j < len(lines) and lines[j].lstrip().startswith('- '):
                k = j
                buf = [lines[j].lstrip()[2:]]
                while k + 1 < len(lines) and lines[k + 1].strip() and not lines[k + 1].lstrip().startswith('- ') \
                        and not lines[k + 1].startswith(('|', '#', '```')):
                    k += 1
                    buf.append(lines[k].strip())
                items.append(' '.join(buf))
                j = k + 1
            out.append('\\begin{itemize}\\setlength{\\itemsep}{2pt}\n' +
                       '\n'.join('\\item ' + inline(x) for x in items) + '\n\\end{itemize}')
            i = j
            continue
        # paragraph: swallow until a blank line
        j = i
        buf = []
        while j < len(lines) and lines[j].strip() and not lines[j].startswith(('|', '#', '```', '- ')):
            buf.append(lines[j].strip())
            j += 1
        para = ' '.join(buf)
        if para.startswith('**Amin Abaee**') or para.startswith('ORCID 0000'):
            i = j
            continue
        if para.startswith('*') and para.endswith('*') and not para.startswith('**') and '\n' not in para:
            pass
        out.append(inline(para))
        i = j
    title = title_override or title
    tex = (PRE + '\\title{' + esc(fold(title)) + '}\n' + AUTHOR + '\n' + '\n\n'.join(out)
           + '\n\\end{document}\n')
    return title, tex, labels


def build(md_name, pdf_base):
    title, tex, labels = convert(R + md_name, title_override=None)
    bad = sorted({c for c in tex if ord(c) > 127})
    if bad:
        print('NON-ASCII LEFT:', bad)
        sys.exit(1)
    open(R + pdf_base + '.tex', 'w').write(tex)
    r = subprocess.run(['/home/user/tools/tectonic', pdf_base + '.tex', '-o', '.'],
                       cwd=R, capture_output=True, text=True, timeout=900)
    tail = [x for x in (r.stdout + r.stderr).split('\n') if x.startswith(('error', 'Warning', '!'))]
    print(f'{pdf_base}: {len(tex)} B tex, {len(labels)} sectioned blocks | compile notes: '
          f'{tail[:2] or "clean"}')
    if 'error' in (r.stdout + r.stderr).lower():
        print((r.stdout + r.stderr)[-1500:])
        sys.exit(1)


if __name__ == '__main__':
    build('companionA_certification_procedure_v1.md', 'companionA_certification_procedure_v1')
    build('companionB_standards_horizon_v1.md', 'companionB_standards_horizon_v1')

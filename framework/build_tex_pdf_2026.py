#!/usr/bin/env python3
"""Build .tex (pandoc LaTeX with journal front matter) and .pdf (pure-python
renderer with clickable ORCID/email links) for the manuscript documents.
Usage: python3 framework/build_tex_pdf_2026.py <md> <out_base> <title_line> [--tex-source X.tex]
--tex-source means: generate the PDF from pandoc's latex->markdown conversion
of X.tex (E1 v51 pipeline); the .tex is left untouched.
2026-09-18. Deterministic renderer, DejaVu fonts, A4.
"""
import os, re, sys, subprocess, unicodedata

ROOT = os.path.dirname(os.path.abspath(__file__)) + '/..'
os.chdir(ROOT)
import pypandoc
from fpdf import FPDF

AUTHOR = ("Amin Abaee", "Independent Researcher",
          "0000-0002-0019-1842", "amin_abaee@ut.ac.ir")
DATE = "September 18, 2026"
ORCID_URL = "https://orcid.org/" + AUTHOR[2]

# ---------------- TeX build ----------------
PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{booktabs,longtable}
\usepackage{graphicx}
\usepackage[hyphens]{url}
\usepackage[colorlinks=true,linkcolor=black,urlcolor=blue,citecolor=blue]{hyperref}
\setlength{\parskip}{0.55em}\setlength{\parindent}{0pt}
\providecommand{\tightlist}{\setlength{\itemsep}{0.2em}\setlength{\parskip}{0pt}}
"""

def build_tex(md_path, out_tex, title):
    body = pypandoc.convert_file(md_path, 'latex', format='markdown+pipe_tables')
    author = (r"\textbf{%s}\\ %s\\[2pt] "
              r"ORCID: \href{%s}{%s}\\ Email: \href{mailto:%s}{%s}"
              % (AUTHOR[0], AUTHOR[1], ORCID_URL, AUTHOR[2], AUTHOR[3], AUTHOR[3]))
    # pandoc image paths are md-relative; keep as-is (paths are repo-relative from doc dir)
    tex = (PREAMBLE + "\n\\title{%s}\n\\author{%s}\n\\date{%s}\n\\begin{document}\n\\maketitle\n\n"
           % (title.replace('%', r'\%'), author, DATE)
           + body + "\n\\end{document}\n")
    open(out_tex, 'w').write(tex)
    print('tex:', out_tex)

# ---------------- markdown -> tolerant text for PDF ----------------
GREEK = {'alpha': 'α', 'beta': 'β', 'gamma': 'γ', 'delta': 'δ', 'varphi': 'φ', 'phi': 'φ',
         'sigma': 'σ', 'rho': 'ρ', 'eta': 'η', 'chi': 'χ', 'varepsilon': 'ε', 'qquad': '', 'quad': '', 'bar': '', 'tilde': ''}
def demath(s):
    s = re.sub(r'\\(begin|end)\{[^}]*\}', ' ', s)
    s = re.sub(r'\b(begin|end)\{[^}]*\}', ' ', s)
    s = re.sub(r'\\(d?frac)\{([^}]*)\}\{([^}]*)\}', r'\2/\3', s)
    s = re.sub(r'\\text\{([^}]*)\}', r'\1', s)
    s = re.sub(r'(?<!\w)(begin|end)(?=\s|$)', ' ', s)
    s = re.sub(r'\\q?qu?a?d\b', ' ', s)
    s = s.replace('\\qquad', ' ')
    s = re.sub(r'\\(mathrm|mathbf|text|operatorname)\{([^}]*)\}', r'\2', s)
    for k, v in GREEK.items():
        s = re.sub(r'\\%s(?![A-Za-z]) ?\{?([A-Za-z])?\}?' % k, lambda m: v + (m.group(1) or ''), s)
    for cmd, rep in [('times', '×'), ('to', '→'), ('rightarrow', '→'), ('pm', '±'), ('approx', '≈'),
                     ('le', '≤'), ('leq', '≤'), ('ge', '≥'), ('geq', '≥'), ('in', '∈'), ('log', 'log'),
                     ('exp', 'exp'), ('min', 'min'), ('max', 'max'), ('cdot', '·'), ('ldots', '…'),
                     ('bigl', ''), ('bigr', ''), ('left', ''), ('right', ''), (';', ' '),
                     ('bar', ''), ('hat', ''), ('tilde', ''), ('frac', '/'), ('sqrt', '√'),
                     ('mathbf 1', '1'), ('mathrm{clip}', 'clip')]:
        s = re.sub(r'\\%s\b ?' % cmd, rep, s)
    s = s.replace('$', ' ')
    s = s.replace('_{t+1}', 'ₜ₊₁').replace('_{t−1}', 'ₜ₋₁').replace('_{t-1}', 'ₜ₋₁')
    s = re.sub(r'_\{([^}]*)\}', r'[\1]', s)
    s = re.sub(r'\^\{([^}]*)\}', r'^(\1)', s)
    for k,v in {'Delta':'Δ','mathbf 1':'1','mathrm{LRP}':'LRP','mathrm{clip}':'clip','mathrm{log}':'log','leq':'≤','geq':'≥','neq':'≠','left{':'','right{':'','mathfrak':'','mathsf':'','mathcal':''}.items():
        s=s.replace('\\'+k,v)
    s=re.sub(r'\\([A-Za-z]+)', r'\1', s)   # residual \command -> command
    s = re.sub(r'[{}]', '', s)
    s = s.replace('\\\\',' ').replace('\\','')
    s = s.replace('\\[','[').replace('\\]',']')
    return re.sub(r'\s+', ' ', s).strip()

def strip_inline(t):
    """[[text]](url) -> text ; `code` -> code ; **b** -> b ; *i* -> i ; $m$ -> demath"""
    def _link(m):
        return m.group(1)
    while True:
        t2 = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', _link, t)
        if t2 == t:
            break
        t = t2
    t = re.sub(r'\$\$([^$]*)\$\$', lambda m: demath(m.group(1)), t)
    t = re.sub(r'\$([^$\n]{1,200}?)\$', lambda m: demath(m.group(1)), t)
    t = t.replace('---', '\u2014').replace('--', '\u2013')
    t = t.replace('**', '').replace('\\(', '(').replace('\\)', ')').replace('\\_', '_')
    t = re.sub(r'(?<![\w' + "'" + r'])_([^_]+)_', r'\1', t)
    t = t.replace('`', '')
    return t

def norm(s):
    return unicodedata.normalize('NFC', s.encode('utf-8').decode())

class Doc(FPDF):
    def __init__(self, doc_title):
        super().__init__(format='A4', unit='mm')
        self.set_margins(22, 20, 22)
        self.set_auto_page_break(True, margin=20)
        self.doc_title = doc_title[:70]
        S = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
        SB = '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf'
        M = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
        for name, path in [('Serif', S), ('SerifB', SB), ('Mono', M)]:
            self.add_font(name, '', path)
            self.add_font(name, 'B', {'Serif': SB, 'SerifB': SB, 'Mono': M}[name])
        self.add_page()
    def footer(self):
        self.set_y(-12)
        self.set_font('Serif', '', 8)
        self.set_text_color(90, 90, 90)
        self.cell(0, 5, '- %d -' % self.page_no(), align='C')

def para(pdf, text, sz=10.5, style='', h=None, font='Serif', center=False):
    pdf.set_font(font, style if font != 'Mono' else '', sz)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, (h or sz) * 0.55, norm(text), align='C' if center else 'J' if font != 'Mono' else 'L')
    pdf.ln(0.8)

def table_block(pdf, rows):
    """rows: list of list[str]; first is header."""
    nrow = len(rows)
    ncol = max(len(r) for r in rows)
    avail = pdf.w - pdf.l_margin - pdf.r_margin
    lens=[]
    for ci in range(ncol):
        mx=max([len(re.sub(r'\*\*|\*','',r[ci] if ci<len(r) else '')) for r in rows]+[1])
        lens.append(min(mx,60)+6)
    tot=float(sum(lens))
    widths=[max(11.0, avail*L/tot) for L in lens]
    sc=min(1.0, avail/sum(widths)); widths=[w*sc for w in widths]
    pdf.set_font('Serif', '', 8.6)
    for ri, r in enumerate(rows):
        pdf.set_font('SerifB', 'B' if ri == 0 else '', 8.6)
        cells = [norm(strip_inline(c).strip()) for c in r] + [''] * (ncol - len(r))
        heights = [pdf.multi_cell(w, 6.2, c, dry_run=True, output='HEIGHT')
                   if hasattr(pdf, 'multi_cell') else 6.2 for c, w in zip(cells, widths)]
        try:
            hs = [pdf.multi_cell(w, 6.2, c, border=0, dry_run=True, output='HEIGHT') for c, w in zip(cells, widths)]
            hrow = max(hs)
        except Exception:
            hrow = 6.2
        if pdf.get_y() + hrow > pdf.h - 22:
            pdf.add_page()
        x0 = pdf.get_x()
        y0 = pdf.get_y()
        for ci, (c, w) in enumerate(zip(cells, widths)):
            pdf.set_xy(x0 + sum(widths[:ci]), y0)
            pdf.rect(x0 + sum(widths[:ci]), y0, w, hrow)
            pdf.multi_cell(w, 6.2, c, border=0, align='L')
        pdf.set_xy(x0, y0 + hrow)
    pdf.ln(2.5)

def _html_tables_to_pipes(md):
    """Convert raw <table>…</table> blocks (pandoc html passthrough) into
    pipe tables; strip residual inline tags and heading/image attribute
    braces."""
    import html as _htmlmod
    def strip_tags(x):
        x = re.sub(r'<[^>]+>', ' ', x)
        x = _htmlmod.unescape(x)
        x = re.sub(r'\s+', ' ', x)
        x = demath(x).strip()
        x = re.sub(r' +', ' ', x)
        x = re.sub(r'\s*([\[\],;:+\-–])', r'\1', x)
        return x
    def conv(m):
        body = m.group(0)
        rows = []
        for row in re.split(r'<tr[^>]*>', body, flags=re.S)[1:]:
            cells = re.findall(r'<t[hd][^>]*>(.*?)</t[hd]>', row, flags=re.S)
            if cells:
                rows.append(' | '.join(strip_tags(c) for c in cells))
        if not rows:
            return '\n'
        pipes = ['| ' + r + ' |' for r in rows]
        ncol = pipes[0].count('|') - 1
        sep = '| ' + ' | '.join(['---'] * ncol) + ' |'
        return '\n' + '\n'.join([pipes[0], sep] + pipes[1:]) + '\n'
    md = re.sub(r'<table[^>]*>.*?</table>', conv, md, flags=re.S)
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S)
    md = md.replace('{=html}', '')
    md = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', md, flags=re.S)
    md = re.sub(r'<div[^>]*>(.*?)</div>', r'\1', md, flags=re.S)
    md = re.sub(r'<p[^>]*>(.*?)</p>', r'\1', md, flags=re.S)
    md = re.sub(r'(?m)(\S)[ \t]*\{(?!gathered|aligned|array|eqnarray|cases|dcases|split|matrix|pmatrix|bmatrix|vmatrix|center|tabular|align)[#!.\w][^}\n]*\}[ \t]*$', r'\1', md)
    md = re.sub(r'(?m)^\s*\{[#!.\w][^}\n]*\}\s*$', '\n', md)
    return md

def _join_images(md):
    pat = re.compile(r'!\[((?:[^\[\]]|\[[^\]]*\])*?)\]\(([^)\s]+)\)(?:\{[^}]*\})?[ \n]', re.S)
    def rep(m):
        alt = re.sub(r'\s+', ' ', m.group(1)).strip()
        return '\n![' + alt + '](' + m.group(2) + ')\n'
    return pat.sub(rep, md)

def md_preprocess(md):
    md = _html_tables_to_pipes(md)
    md = re.sub(r'\$\$(.+?)\$\$', lambda m: ' ' + demath(m.group(1)) + ' ', md, flags=re.S)
    md = re.sub(r'\$([^$]{1,500}?)\$', lambda m: ' ' + demath(m.group(1)) + ' ', md, flags=re.S)
    md = re.sub(r'\\\((.{1,500}?)\\\)', lambda m: ' ' + demath(m.group(1)) + ' ', md, flags=re.S)
    md = re.sub(r'\\\[(.{1,500}?)\\\]', lambda m: '\n' + demath(m.group(1)) + '\n', md, flags=re.S)
    md = _join_images(md)
    """Clean pandoc-latex-conversion artefacts: minipage multi-row pipe
    tables (merge continuation rows, drop ::: junk), fixed-width columnar
    blocks (wrap into code fences), -- -> en-dash in prose."""
    lines = md.split('\n')
    return '\n'.join(_md_preprocess_core(lines))

def _md_preprocess_core(lines):
    res = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        # ---- pipe table block with ::: junk / continuation rows ----
        if line.strip().startswith(':::') or ('minipage' in line and line.strip().startswith('|')):
            i += 1
            continue
        if line.strip().startswith('|'):
            block = []
            while i < n and lines[i].strip().startswith('|'):
                if ':::' in lines[i]:
                    i += 1
                    continue
                block.append(lines[i])
                i += 1
            if block:
                res.extend(_merge_pipe_continuations(block))
            continue
        # ---- fixed-width columnar block (>=3 consecutive aligned lines) ----
        if line.startswith(' ') and len(line.strip()) > 0 and not line.lstrip().startswith(('$$', '|', '-', '*')):
            blk = []
            while i < n and lines[i].startswith(' ') and lines[i].strip() and not lines[i].lstrip().startswith(('|', '- ', '* ')):
                blk.append(lines[i])
                i += 1
            if len(blk) >= 3 and sum(1 for b in blk if re.search(r'\S\s{4,}\S', b)) >= 2:
                res.append('```')
                res.extend(blk)
                res.append('```')
                continue
            res.extend(line.replace('--', '\u2013') for line in blk)
            continue
        res.append(line)
        i += 1
    out=[]
    incode=False
    for ln in res:
        if ln.strip().startswith('```'):
            incode=not incode; out.append(ln); continue
        out.append(ln if incode else ln.replace('---', '\u2014').replace('--', '\u2013'))
    return out

def _merge_pipe_continuations(block):
    """Minipage tables: each logical row spans several physical rows, with
    continuation cells in later rows; merge them."""
    merged = []
    for ln in block:
        cells = ln.strip().strip('|').split('|')
        if all(set(c.strip()) <= set('-: ') for c in cells):
            continue
        if merged and (cells[0].strip() == '' ):
            prev = merged[-1]
            trgt = prev.split('|')
            trgt = trgt[1:-1]
            for k, c in enumerate(cells):
                c = c.strip()
                if c and k < len(trgt):
                    trgt[k] = (trgt[k].strip() + ' ' + c).strip()
                elif c:
                    trgt.append(c)
            merged[-1] = '| ' + ' | '.join(t.strip() for t in trgt) + ' |'
        else:
            merged.append(ln)
    return merged

def render_pdf(md, out_pdf, title, is_supp=False):
    md = md_preprocess(md)
    pdf = Doc(title)
    pdf.set_title(title)
    lines = md.split('\n')
    # ---- title page ----
    pdf.set_font('SerifB', 'B', 15)
    pdf.multi_cell(0, 8, norm(strip_inline(title)), align='C')
    pdf.ln(2)
    para(pdf, AUTHOR[0], sz=12, font='SerifB', center=True)
    para(pdf, AUTHOR[1], sz=10, center=True)
    pdf.set_font('Serif', '', 10)
    y = pdf.get_y()
    t1 = 'ORCID: ' + AUTHOR[2]
    w1 = pdf.get_string_width(norm(t1))
    x = (pdf.w - w1) / 2
    pdf.set_xy(x, y)
    pdf.set_text_color(0, 0, 200)
    pdf.write(5, t1, link=ORCID_URL)
    pdf.ln(5)
    t2 = 'Email: ' + AUTHOR[3]
    w2 = pdf.get_string_width(norm(t2))
    pdf.set_xy((pdf.w - w2) / 2, pdf.get_y())
    pdf.write(5, t2, link='mailto:' + AUTHOR[3])
    pdf.ln(6)
    para(pdf, DATE, sz=10, center=True)
    pdf.ln(3)

    in_code = False
    in_tab = False
    tab_rows = []
    doc_dir = os.path.dirname(md_path_current)

    def flush_table():
        nonlocal tab_rows, in_tab
        tab_rows = [r for r in tab_rows if r != ['-'] * len(r)]
        if tab_rows:
            table_block(pdf, tab_rows)
        tab_rows, in_tab = [], False

    i = 0
    for raw in lines:
        line = raw.rstrip('\n')
        if line.strip().startswith('```'):
            flush_table()
            in_code = not in_code
            continue
        if in_code:
            cleaned = strip_inline(line) if ('$' in line or '\\' in line) else line
            para(pdf, cleaned, sz=7.6, font='Mono', h=7.6)
            continue
        if line.strip().startswith('|') and line.strip().endswith('|'):
            cells = [c for c in line.strip().strip('|').split('|')]
            if not any(re.sub(r'[:\\-]', '', c.strip()) for c in cells):
                continue
            tab_rows.append([c.strip() for c in cells])
            in_tab = True
            continue
        if in_tab and not (line.strip().startswith('|')):
            flush_table()
        s = line.strip()
        if not s:
            pdf.ln(1.2)
            continue
        m = re.match(r'^(#{1,4})\s+(.*)$', s)
        if m:
            lvl = len(m.group(1))
            para(pdf, m.group(2), sz={1: 14, 2: 12.5, 3: 11.5, 4: 11}.get(lvl, 11), font='SerifB')
            continue
        im = re.match(r'^!\[([^\]]*)\]\(([^)\s]+)\)(?:\{[^}]*\})?\s*$', s)
        if im:
            rel = im.group(2)
            cands = [os.path.join(doc_dir, rel),
                     os.path.join(doc_dir, re.sub(r'^figs_\w+/', 'figs/', rel)),
                     os.path.join(doc_dir, 'figs', os.path.basename(rel))]
            imgpath = next((c for c in cands if os.path.exists(c)), None)
            if imgpath:
                try:
                    pdf.image(imgpath, w=pdf.w - 2 * pdf.l_margin - 10)
                    pdf.ln(1.0)
                    if im.group(1).strip():
                        cap = strip_inline(im.group(1)).replace('\n', ' ')
                        para(pdf, cap[:400], sz=8.6, center=True)
                except Exception:
                    para(pdf, '[figure: ' + rel + ']', sz=8.5, center=True)
            else:
                para(pdf, '[figure: ' + rel + ']', sz=8.5, center=True)
            continue
        if s.startswith('$$') and s.endswith('$$') and len(s) > 4:
            para(pdf, demath(s.strip('$')), sz=10, center=True)
            continue
        if s.startswith('- ') or s.startswith('* '):
            para(pdf, '• ' + strip_inline(s[2:]), sz=10.2)
            continue
        m2 = re.match(r'^(\d+)\.\s+(.*)$', s)
        if m2 and len(s) < 500:
            para(pdf, m2.group(1) + '. ' + strip_inline(m2.group(2)), sz=10.2)
            continue
        if s == '---':
            pdf.ln(2)
            continue
        para(pdf, strip_inline(s), sz=10.2)
    flush_table()
    pdf.output(out_pdf)
    print('pdf:', out_pdf)

def title_of(md):
    for ln in md.split('\n'):
        if ln.startswith('# '):
            return ln[2:].strip()
    return 'Document'

md_path_current = ''
if __name__ == '__main__':
    md_in = sys.argv[1]
    out_base = sys.argv[2]
    src_tex = None
    if '--tex-source' in sys.argv:
        src_tex = sys.argv[sys.argv.index('--tex-source') + 1]
    if src_tex:
        body_md = pypandoc.convert_file(src_tex, 'markdown+pipe_tables', format='latex')
        t = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].startswith('-') else 'Manuscript'
        md_path_current = src_tex
        render_pdf(body_md, out_base + '.pdf', t)
        tex_out = out_base + '.tex'
        if os.path.abspath(src_tex) != os.path.abspath(tex_out) and not os.path.exists(tex_out):
            import shutil as sh
            sh.copyfile(src_tex, tex_out)
    else:
        md = open(md_in).read()
        t = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].startswith('-') else title_of(md)
        md_path_current = md_in
        build_tex(md_in, out_base + '.tex', t.replace(' (v2)', '').replace(' (v1)', ''))
        render_pdf(md, out_base + '.pdf', t)

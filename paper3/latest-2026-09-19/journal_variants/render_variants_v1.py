#!/usr/bin/env python3
"""Render the compact journal cuts to simple submission PDFs.

This is a deliberately small markdown surface renderer for the journal drafts, not a replacement for
the full v49 build chain. The journal cuts are authored in Markdown; this renderer handles their headings,
paragraphs, lists, displays, tables and the embedded PNG figure, then compiles with the workspace's
Tectonic binary. The word-limit gate remains independent of typesetting.
"""
from __future__ import annotations
import re, subprocess
from pathlib import Path
import sys

ROOT = Path('/home/user')
JV = ROOT/'revision/journal_variants'
sys.path.insert(0, str(ROOT/'revision/v7'))
from mdtex_v1 import md2tex

PREAMBLE = r'''\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath,amssymb,mathtools}
\usepackage{booktabs,tabularx,array}
\usepackage{graphicx}
\usepackage[margin=1in]{geometry}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{xcolor}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\setlist[itemize]{leftmargin=1.4em,itemsep=2pt,topsep=2pt}
\setlist[enumerate]{leftmargin=1.7em,itemsep=2pt,topsep=2pt}
\renewcommand{\arraystretch}{1.18}
\emergencystretch=3em
\sloppy
\allowdisplaybreaks
'''

def inline(s):
    return md2tex(s)

def is_table_start(lines, i):
    """Accept only a pipe row followed immediately by a Markdown separator row.

    A leading vertical bar also occurs in multiline mathematics, e.g. ``|pi|``. Treating
    that as a table is a renderer bug, not a manuscript defect.
    """
    if i >= len(lines) or not lines[i].startswith('|') or i + 1 >= len(lines):
        return False
    sep = lines[i + 1].strip()
    return bool(re.fullmatch(r'\|\s*:?-{2,}:?\s*(?:\|\s*:?-{2,}:?\s*)+\|?', sep))

def table_tex(rows):
    # rows are raw markdown table rows; first row is header and second separator is skipped
    vals=[]
    for line in rows:
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        vals.append(cells)
    if len(vals) >= 2 and all(re.fullmatch(r':?-{2,}:?', c) for c in vals[1]):
        vals.pop(1)
    n=max(len(x) for x in vals)
    col='X'*n
    out=[r'\begin{tabularx}{\linewidth}{'+col+'}',r'\toprule']
    for i,r in enumerate(vals):
        r=r+['']*(n-len(r))
        out.append(' & '.join(inline(x) for x in r)+r' \\\\')
        if i==0: out.append(r'\midrule')
    out += [r'\bottomrule',r'\end{tabularx}',r'\medskip']
    return '\n'.join(out)

def render(md, image_rel='assets/typed_ledger_readout.png'):
    lines=md.splitlines(); out=[PREAMBLE]
    in_abstract=False; in_list=None; i=0
    while i < len(lines):
        line=lines[i]
        if not line.strip():
            if in_list:
                out.append(r'\end{'+in_list+'}'); in_list=None
            i+=1; continue
        if line.startswith('!['):
            m=re.match(r'!\[([^]]*)\]\(([^)]+)\)', line.strip())
            if m:
                img_path = m.group(2)
                if not img_path.startswith('/'):
                    img_path = '../' + img_path
                out += [r'\begin{figure}[htbp]',r'\centering',r'\includegraphics[width=\linewidth]{'+img_path+r'}',r'\caption{'+inline(m.group(1))+r'}',r'\end{figure}',r'\medskip']
            i+=1; continue
        # display math can be one line in these drafts
        if line.strip().startswith('$$'):
            block=line.strip()
            if block.count('$$')>=2:
                content=block[2:-2].strip(); out.append(r'\['+content+r'\]')
                i+=1; continue
            math=[block[2:]]; i+=1
            while i<len(lines) and '$$' not in lines[i]: math.append(lines[i]); i+=1
            if i<len(lines): math.append(lines[i].replace('$$','')); i+=1
            out.append(r'\['+'\n'.join(math)+r'\]'); continue
        mh=re.match(r'^(#{1,4})\s+(.*)$',line)
        if mh:
            lev=len(mh.group(1)); title=inline(mh.group(2).strip())
            if lev==1: out += [r'\title{'+title+r'}',r'\author{}',r'\date{}',r'\begin{document}',r'\maketitle']
            elif lev==2: out.append(r'\section{'+title+r'}')
            elif lev==3: out.append(r'\subsection{'+title+r'}')
            else: out.append(r'\subsubsection{'+title+r'}')
            if mh.group(2).strip().lower()=='abstract':
                in_abstract=True; out.append(r'\begin{abstract}')
            elif in_abstract:
                out.append(r'\end{abstract}'); in_abstract=False
            i+=1; continue
        if is_table_start(lines, i):
            rows=[]
            while i<len(lines) and lines[i].startswith('|'):
                rows.append(lines[i]); i+=1
            out.append(table_tex(rows)); continue
        m=re.match(r'^\s*([-*])\s+(.*)$',line)
        if m:
            if in_list!='itemize':
                if in_list: out.append(r'\end{'+in_list+'}')
                out.append(r'\begin{itemize}'); in_list='itemize'
            out.append(r'\item '+inline(m.group(2))); i+=1; continue
        m=re.match(r'^\s*(\d+)\.\s+(.*)$',line)
        if m:
            if in_list!='enumerate':
                if in_list: out.append(r'\end{'+in_list+'}')
                out.append(r'\begin{enumerate}'); in_list='enumerate'
            out.append(r'\item '+inline(m.group(2))); i+=1; continue
        # gather flowing paragraph until a structural line
        para=[line]; i+=1
        while i<len(lines) and lines[i].strip() and not re.match(r'^(#{1,4})\s|^\s*[-*]\s|^\s*\d+\.\s|^!\[|^\s*\$\$', lines[i]) and not is_table_start(lines, i):
            para.append(lines[i]); i+=1
        out.append(inline(' '.join(para)))
    if in_list: out.append(r'\end{'+in_list+'}')
    if in_abstract: out.append(r'\end{abstract}')
    out += [r'\end{document}']
    return '\n'.join(out)+'\n'


def main():
    outdir=JV/'rendered'; outdir.mkdir(exist_ok=True)
    for name in ('paper3_JIE_submission_v1','paper3_EE_submission_v1'):
        md=(JV/f'{name}.md').read_text()
        tex=outdir/f'{name}.tex'; tex.write_text(render(md))
        cmd=[str(ROOT/'tools/tectonic'), '--keep-logs', '--outdir', str(outdir), str(tex)]
        r=subprocess.run(cmd,cwd=outdir,text=True,capture_output=True,timeout=600)
        print(name,'tectonic rc',r.returncode)
        if r.returncode:
            print(r.stdout[-2500:]); print(r.stderr[-2500:]); raise SystemExit(r.returncode)
        print('  pdf',outdir/f'{name}.pdf')

if __name__=='__main__': main()

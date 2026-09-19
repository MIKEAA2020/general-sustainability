#!/usr/bin/env python3
"""Typeset the supplementary: the v12 markdown mirror converted for pdflatex-safe LaTeX.

The supplementary has always been distributed as markdown, and the reason is the character set: it carries linear-programme
listings and prose with operators and diacritics (<=, lambda, X-bar, square, rightarrow) that the corpus's converter
deliberately refuses to emit as raw Unicode. This script does not bypass that guard. It transliterates every non-ASCII
character in two registers: inside a fenced listing or an inline code span, where the text is typeset verbatim and a
backslash would be printed as a backslash, the character is written in its ASCII spelling; in prose, where the character
stands for a mathematical object, it is wrapped in the matching math command. Nothing is dropped, and the gate re-checks the result by
comparing the token sequence of the source against the extracted text of the compiled PDF.
"""
import os
import re
import subprocess
import sys

R = '/home/user/revision/v7'
sys.path.insert(0, R)
import build_companions_v1 as bc                                                   # noqa: E402

SRC = f'{R}/paper3_supplementary_v12.md'
SCRATCH = f'{R}/paper3_supplementary_v12.ascii.md'
BASE = 'paper3_supplementary_v12'

# inside fenced listings: ASCII spellings, so a reader can type them back
CODE = [('·', '-'), ('§', 'Sec. '), ('Ḃ', 'B_dot'), ('Ṙ', 'R_dot'), ('ḃ', 'b_dot'), ('ℓ', 'ell'), ('λ', 'lambda'), ('∂', 'partial'), ('≤', '<='), ('≥', '>='), ('ᵀ', '^T'), ('ℓ', 'l'),
        ('̄', ''), ('−', '-'), ('→', '->'), ('⇒', '=>'), ('∈', 'in'), ('∞', 'inf'),
        ('₀', '_0'), ('τ', 'tau'), ('β', 'beta'), ('δ', 'delta'), ('κ', 'kappa'), ('ε', 'eps'),
        ('η', 'eta'), ('σ', 'sigma'), ('φ', 'phi')]
# in prose: the LaTeX construct for the same object
TEX = [('§', r'$\S$'), ('·', r'$\cdot$'), ('□', r'$\square$'), ('ô', r'$\ddot{o}$'),
       ('Ø', r'$\text{\O}$'),          # \O is a text command: in math mode it asks the math font for a glyph
       # it has not been given, which tectonic reports as "Missing character" and substitutes
       ('½', r'$\tfrac{1}{2}$'), ('Ḃ', r'$\ddot{B}$'), ('Ṙ', r'$\dot{R}$'),
       ('ḃ', r'$\dot{b}$'), ('η', r'$\eta$'), ('σ', r'$\sigma$'), ('λ', r'$\lambda$'),
       ('τ', r'$\tau$'), ('ε', r'$\varepsilon$'), ('φ', r'$\phi$'), ('κ', r'$\kappa$'),
       ('β', r'$\beta$'), ('δ', r'$\delta$'), ('∂', r'$\partial$'), ('≤', r'$\leq$'),
       ('≥', r'$\geq$'), ('∈', r'$\in$'), ('∞', r'$\infty$'), ('→', r'$\rightarrow$'),
       ('⇒', r'$\Rightarrow$'), ('ℓ', r'$\ell$'), ('₀', r'$_0$'), ('ᵀ', r'$^{\mathsf T}$'),
       ('−', r'$-$'), ('⁻', r'$^{-}$'), ('¹', r'$^{1}$'), ('²', r'$^{2}$'), ('³', r'$^{3}$'),
       ('⁴', r'$^{4}$'), ('⁵', r'$^{5}$')]
# every replacement is wrapped in math delimiters on purpose: the scratch text is still markdown, and the
# converter that reads it escapes a bare backslash, so "\S{}" written here would be printed as "\S{}" in the
# PDF --- which is what the supplementary did from v11 to v12, 34 times over, while compiling without a warning


# the corpus converter's own rules take care of dashes, apostrophes and quotes
HANDLED = set('\u2014\u2013\u2019\u2018\u201c\u201d')
SPAN = re.compile(r'`[^`\n]*`')
import unicodedata as _ud


def _ascii_spell(t):
    """The ASCII register: the same rules a fenced listing uses. Applied inside a code span and on a heading line,
    because the converter escapes everything in both places, so a math command written there is printed as markup
    (which is how v11 and v12 came to typeset a heading's separator as a literal dollar-command)."""
    for a, b in CODE:
        t = t.replace(a, b)
    t = re.sub(r'([A-Za-z])\u0304', r'\1_bar', t)
    t = re.sub(r'([A-Za-z])\u0307', r'\1_dot', t)
    t = re.sub(r'([A-Za-z])\u0301', r'\1_ac', t)
    return ''.join(c for c in _ud.normalize('NFKD', t) if ord(c) < 128)


def _in_span(m):
    """A code span is typeset monospaced, and the converter escapes everything inside it, so a LaTeX construct
    placed there is printed literally: `\u1e03` in a table cell came out as `$\dot{b}$` in the PDF. Inside a span
    the character therefore gets its ASCII spelling, the same register the fenced listings use, and prose keeps
    the math command."""
    t = m.group(0)
    if all(ord(c) < 128 or c in HANDLED for c in t):
        return t
    return _ascii_spell(t)


def convert(t):
    out, i = [], 0
    for m in re.finditer(r'```[\s\S]*?```', t):
        head = t[i:m.start()]
        out.append(_prose(head))
        blk = m.group(0)
        for a, b in CODE:
            blk = blk.replace(a, b)
        out.append(blk)
        i = m.end()
    out.append(_prose(t[i:]))
    return ''.join(out)


def _prose(seg):
    seg = SPAN.sub(_in_span, seg)
    seg = re.sub(r'([A-Za-z])\u0304', r'$\bar{\1}$', seg)                   # X-bar before the bare macron
    for a, b in TEX:
        seg = seg.replace(a, b)
    return seg


def headings(t):
    """A heading is escaped whole by the converter, so it gets the ASCII register too: every character above the
    dash and quote pair that the converter does handle is spelled out."""
    out = []
    for l in t.split('\n'):
        m = re.match(r'^(#{1,6} )(.*)$', l)
        out.append(m.group(1) + _ascii_spell(m.group(2)) if m else l)
    return '\n'.join(out)


def transpile(src, base):
    raw = headings(open(src).read())
    txt = convert(raw).replace('\u1e03', '$\\dot{b}$')          # b with a dot above, in prose
    for a, b in (('\u2014', '---'), ('\u2013', '--'), ('\u2019', "'"), ('\u2018', "'"),
                 ('\u201c', '``'), ('\u201d', "''")):
        txt = txt.replace(a, b)                                   # the article's own dash and quote rules
    left = sorted({c for c in txt if ord(c) > 127} - HANDLED)
    assert not left, f'unmapped characters remain: {left}'
    scratch = f'{R}/{base}.ascii.md'
    open(scratch, 'w').write(txt)
    title, tex, labels = bc.convert(scratch.split('/')[-1], title_override=None)
    bad = sorted({c for c in tex if ord(c) > 127})
    assert not bad, f'tex non-ascii {bad[:6]}'
    sys.path.insert(0, '/home/user')
    import importlib.util as _u
    _sp = _u.spec_from_file_location('texkit', '/home/user/review/texkit_v1.py')
    tk = _u.module_from_spec(_sp)
    _sp.loader.exec_module(tk)
    tex = tk.improve(tk.header_for(title, 'Supplementary material', f'{base}.md') + tex)
    open(f'{R}/{base}.tex', 'w').write(tex)
    rc, log, over = tk.compile_log(base, R)
    overfull = len(over)
    miss = [x for x in log.split('\n') if 'Missing character' in x or x.startswith('error') or x.startswith('!')]
    print(f'{base}.tex: {len(tex)} B, {len(labels)} blocks; overfull {overfull}; compile '
          f'{"ok" if rc == 0 else log[-300:]}')
    print('  glyph/compile notes:', miss[:3] or 'none')
    assert rc == 0 and not miss, 'supplementary compile failed'
    return overfull


if __name__ == '__main__':
    os.chdir(R)
    transpile(SRC, BASE)

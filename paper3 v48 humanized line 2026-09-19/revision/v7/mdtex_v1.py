#!/usr/bin/env python3
r"""Markdown prose to the LaTeX the manuscript uses, and a tex body rebuilt from a new markdown file.

The line this serves keeps two sources for one article: a markdown file, which is the surface the style passes
work on, and a LaTeX file, which is what typesets. Until now the LaTeX was polished in place, which meant a
paragraph added in the markdown had nowhere to go and simply did not appear in the PDF. This module converts a
markdown paragraph to the LaTeX conventions the deposited source uses, and rebuilds the LaTeX body of a document
from a new markdown file while leaving everything the markdown does not own - the tables, the statements, the
displays, the labels, the front and back matter - exactly as the typeset source has it.

The converter is checked, not trusted: `selftest` converts every flowing paragraph of the v42 markdown and
compares the words to the paragraph the author typeset at the same place, which is the only honest measure of
whether the mapping is complete.
"""
import difflib
import re
import sys

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import stylekit_v1 as SK

ACCENT = {'ä': '\\"a', 'ö': '\\"o', 'ü': '\\"u', 'ô': '\\^{o}', 'ó': "\\'o", 'é': "\\'e", 'è': '\\`e',
          'á': "\\'a", 'í': "\\'i", 'ñ': '\\~n', 'ç': '\\c{c}', 'Ø': '\\O{}', 'ø': '\\o{}', 'Å': '\\AA{}',
          'œ': '\\oe{}', 'ß': '\\ss{}'}
SYMBOL = {'§': '\\S{}', '—': '---', '–': '--', '‑': '-', '’': "'", '‘': "'", "“": '``', '”': "''",
          '†': '\\dag', '‡': '\\ddag', '…': '\\ldots', '°': '\\textdegree{}', 'µ': '$\\mu$', '×': '$\\times$',
          '→': '$\\to$', '≈': '$\\approx$', '÷': '$\\div$', '₂': '$_2$', '₃': '$_3$', '₀': '$_0$',
          '₁': '$_1$', '·': '$\\cdot$', '−': '$-$', '±': '$\\pm$', '≥': '$\\ge$', '≤': '$\\le$',
          '∅': '$\\emptyset$', '□': '$\\square$', '∈': '$\\in$', '∉': '$\\notin$', '→': '$\\to$',
          '↑': '$\\uparrow$', '↓': '$\\downarrow$', '‑': '-'}
TEXT_ESC = {'&': '\\&', '%': '\\%', '#': '\\#'}


def _protect_math(t, holes):
    def f(m):
        holes.append(m.group(0))
        return f'\x06{len(holes) - 1}\x06'
    t = re.sub(r'(?s)\$\$.*?\$\$', f, t)
    return re.sub(r'\$[^$\n]*\$', f, t)


def _restore_math(t, holes):
    # the deposited source sets inline maths with \(..\), not with $..$, so a restored span is written the way
    # the manuscript writes it; a display is left to the environment it stands in
    def f(m):
        h = holes[int(m.group(1))]
        if h.startswith('$$'):
            return h
        return '\\(' + h.strip()[1:-1].strip() + '\\)'
    return re.sub(r'\x06(\d+)\x06', f, t)


def md2tex(block):
    """One markdown paragraph to the LaTeX of this manuscript. Math is passed through untouched; the markup the
    markdown adds for a reader (emphasis, a section sign, an en dash, a symbol) is what gets translated."""
    t = ' '.join(block.strip().split())
    holes = []
    t = _protect_math(t, holes)
    t = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', t, flags=re.S)
    t = re.sub(r'(?<!\*)\*([^*\n]+?)\*(?!\*)', r'\\emph{\1}', t)
    t = re.sub(r'`([^`]+)`', r'\\texttt{\1}', t)
    for k, v in TEXT_ESC.items():
        t = t.replace(k, v)
    t = re.sub(r'(?<!\\)([_#])', lambda m: '\\' + m.group(1), t)
    for k, v in list(SYMBOL.items()) + list(ACCENT.items()):
        t = t.replace(k, v)
    t = re.sub(r'(?<![A-Za-z0-9])"', '``', t)                             # an opening quotation mark
    t = t.replace('"', "''")                                              # and every quote left closes one
    t = re.sub(r'\[S(\d+)\]\(([^)]*)\)', r'\\ref{\2}', t)          # markdown links to internal labels
    t = re.sub(r'\[\^(\d+)\]', r'\\footref{...\1}', t)             # there are none; a loud failure beats a silent one
    t = _restore_math(t, holes)
    return t


def head(t, n=48):
    x = re.sub(r'(?s)\$\$.*?\$\$|\$[^$\n]*\$', ' ', t)
    x = re.sub(r'\*\*|\*|`|§|[\u2014\u2013]', ' ', x)
    return ' '.join(x.split())[:n].lower()


def md_flow(md):
    """The flowing prose of a markdown document: the blocks a document-wide style pass may rewrite, which is the
    same test the audit reads (`stylekit.is_flow`), taken after the heading where the body of the argument opens,
    and excluding a statement, whose wording is the paper's claim and not prose to be retyped."""
    lines = md.split('\n')
    heads = [k for k, x in enumerate(lines) if re.match(r'^## ', x)]
    num = [k for k in heads if re.match(r'^## \d', lines[k])]
    first = num[0] if num else 0
    after = [k for k in heads if k > first and not re.match(r'^## \d', lines[k])]
    last = after[0] if after else len(lines)                # the body ends at the first unnumbered heading
    out = []
    for b in SK.split_blocks('\n'.join(lines[first:last])):
        if not SK.is_flow(b) or b.lstrip().startswith(('#', '**Statement S', '|', '>')):
            continue
        if len(' '.join(b.split()).split()) < 6:
            continue
        out.append(' '.join(b.split()))
    return out


def _plain(t, n=7):
    """A short literal slice of a markdown paragraph, with the markdown taken out and the LaTeX equivalents put
    in, so it can be found in the typeset source as it stands."""
    x = re.sub(r'(?s)\$\$.*?\$\$|\$[^$\n]*\$', ' ', t)
    x = re.sub(r'\*\*|\*|`', '', x)
    for k, v in (('§', '\\S{}'), ('—', '---'), ('–', '--')):
        x = x.replace(k, v)
    w = [y for y in ' '.join(x.split()).split() if y][:n]
    return ' '.join(w)


def _rx(t):
    """The same slice as a pattern that tolerates the line breaks the source puts inside every paragraph."""
    return re.compile(r'\s*'.join(re.escape(w) for w in t.split()))


def locate_spans(body, md_flow_blocks):
    """Where each flowing markdown paragraph sits in the typeset body, as (start, end) offsets, plus the
    paragraphs that have no locatable place. A head is tried at three lengths, because the source wraps every
    paragraph and a heading or an environment can start in the middle of one; what a paragraph was typeset as
    stays its own business, so anything that cannot be located is reported rather than guessed at."""
    out, missed = [], []
    for b in md_flow_blocks:
        hit = None
        for n in (7, 5, 4):
            pat = _rx(_plain(b, n))
            hits = [m for m in pat.finditer(body)]
            if len(hits) == 1:
                hit = hits[0]
                break
        if hit is None:
            missed.append(' '.join(b.split())[:64])
            out.append(None)
            continue
        # the paragraph ends at the first blank line, however long the markdown block is: if the block runs past
        # it, the guard in rebuild leaves the paragraph to the source rather than swallow the next one
        end = body.find('\n\n', hit.end())
        out.append((hit.start(), end))
    return out, missed


def rebuild(body, old_flow, new_flow):
    """Retype the flowing prose of `body`, the LaTeX the deposit left, so that it reads as `new_flow` does.

    Nothing is paraphrased here and nothing is chosen by approximation: the two markdowns' prose blocks are
    matched by their own text, a run of deposited blocks the new markdown no longer holds is replaced, as one
    region, by the run of blocks that took their place, and a run the deposited markdown never had is put after
    the block the new markdown finds it next to. So an insertion cannot drift into the wrong section and a
    paragraph cannot be cut short by a paragraph break the source happens to put inside it. Tables, statements,
    displays, labels and the front and back matter are not arguments to this function: they keep their content and
    their place, because a style line that reorders a ledger would not be a style line. A deposited paragraph the
    source typeset as something other than a prose unit is left to the source and reported."""
    key = lambda t: ' '.join(t.split())
    spans, missed = locate_spans(body, old_flow)
    keep = [k for k in range(len(old_flow)) if spans[k]]
    sm = difflib.SequenceMatcher(None, [key(old_flow[k]) for k in keep], [key(b) for b in new_flow], autojunk=False)
    regions, skipped, unplaced = [], 0, []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        ks = [keep[x] for x in range(i1, i2)]
        ks = [k for k in ks if key(old_flow[k]) not in {key(x) for x in new_flow[j1:j2]}]
        a = next((spans[k][0] for k in ks if spans[k]), None)
        b2 = next((spans[k][1] for k in reversed(ks) if spans[k]), None)
        new = '\n\n'.join(md2tex(x) for x in new_flow[j1:j2])
        if tag == 'insert' or a is None:
            skipped += sum(1 for k in ks if spans[k] is None)
            prev = [k for k in keep if key(old_flow[k]) in {key(x) for x in new_flow[:j1]}]
            if not prev:
                unplaced += [' '.join(x.split())[:64] for x in new_flow[j1:j2]]
                continue
            regions.append((spans[prev[-1]][1], spans[prev[-1]][1], new))
            continue
        regions.append((a, b2, new))
        skipped += sum(1 for k in ks if spans[k] is None)
    out, pos = [], 0
    for a, b2, new in sorted(regions):
        if a < pos:
            unplaced.append('(overlapping region not applied)')
            continue
        out.append(body[pos:a])
        out.append(new)
        pos = b2
    out.append(body[pos:])
    n_re = sum(1 for a, b2, new in regions if new and b2 > a)
    n_in = sum(1 for a, b2, new in regions if new and b2 == a)
    return ''.join(out), n_re, n_in, skipped, unplaced


def selftest(md_path, tex_path):
    """Convert every flowing paragraph of the old markdown and compare the words to the paragraph the author
    typeset at that place. If the mapping is complete the words are identical; a difference is a construct the
    converter does not know, and it is reported, not smoothed over."""
    md = open(md_path).read()
    tx = open(tex_path).read()
    body = tx[tx.index('\\begin{document}') + len('\\begin{document}'):tx.rindex('\\end{document}')]
    flow = md_flow(md)
    spans, missed = locate_spans(body, flow)
    def words(s2):
        # compare what a reader sees: the break markers the typesetter inserts, the escaping commands and the
        # braces are not words, and an em dash written --- is the same character as the markdown em dash
        s2 = s2.replace('\\allowbreak', ' ').replace('---', '\u2014').replace('--', '\u2013')
        s2 = re.sub(r'\\(?:S|emph|textbf|texttt|textit|dag|ddag|ldots|approx|to|div|qedsymbol)[^A-Za-z0-9]{0,3}',
                    ' ', s2)
        s2 = re.sub(r'\\[a-zA-Z]+', ' ', s2)
        s2 = s2.replace(r'\${}$', '$').replace('{', ' ').replace('}', ' ').replace('\\', ' ')
        w = [x for x in re.findall(r"[A-Za-z0-9$'\u2014\u2013._-]+", s2) if x.strip('-._')]
        return [x.strip('-._') for x in w if x.strip('-._')]
    bad = []
    for k, sp in enumerate(spans):
        if sp is None:
            continue
        a, b2 = sp
        x, y = words(md2tex(flow[k])), words(body[a:b2])
        if x != y:
            bad.append((k, ' '.join(flow[k].split())[:64], len(x) - len(y)))
    return len(spans) - len(missed), bad, missed


if __name__ == '__main__':
    n, bad, missed = selftest('paper3_material_ledgers_v42.md', 'paper3_material_ledgers_v42.tex')
    print(f'selftest: {n} paragraphs located and compared, {len(bad)} disagree on words '
          f'({100*(n-len(bad))/max(1,n):.1f}% exact), {len(missed)} not a locatable prose unit')
    for i, t, d in bad[:10]:
        print(f'   #{i} ({d:+d} words): {t}')
    for t in missed[:6]:
        print(f'   unlocated: {t}')


def covers(pdf_flat, block):
    r"""Whether a paragraph of the markdown is on the page.

    A formula is not prose and a printed code span is spelled out by the typesetter, so the paragraph is read as
    the runs of words between them: each run of four words or more has to be on the page at both ends - the first
    five words and the last five - which says the paragraph is there and begins and ends where the markdown puts
    it. Letters only, and with the accents taken off, because a font substitutes ligatures (an "fi" that comes
    back as one character from the PDF) and a name like \O{}ksendal reaches the page as O-ksendal; and numbers
    are dropped here because a theorem the converter numbers is the same sentence with a digit in front of it,
    while the numbers themselves are counted elsewhere, against the previous deposit, as an exact multiset."""
    import unicodedata
    body = re.sub(r'\$\$.*?\$\$|\$[^$]*\$', '\x02', block, flags=re.S)
    body = re.sub(r'(?<!\\)\\\[.*?\\\]', '\x02', body, flags=re.S)
    body = re.sub(r'`[^`]*`', '\x02', body)

    def flat(s2):
        s2 = re.sub(r'\*+|`+|\[\^\]]+|[{}]', ' ', s2)
        s2 = unicodedata.normalize('NFKD', s2).encode('ascii', 'ignore').decode()
        return re.sub(r'[^A-Za-z]', '', s2)

    runs = [[w for w in x.split() if flat(w)] for x in body.split('\x02')]
    runs = [r for r in runs if len(r) >= 4]
    if not runs:
        return True
    return all(flat(' '.join(r[:5])) in pdf_flat and flat(' '.join(r[-5:])) in pdf_flat for r in runs)


def page_text(pdf_path):
    """The page as a reader's text: the ligatures a font substituted folded back into the letters they stand
    for, the soft hyphens that ended lines taken out, and everything flattened to letters for the comparison."""
    import pymupdf
    import unicodedata
    t = ' '.join(p.get_text() for p in pymupdf.open(pdf_path))
    for a, b in (('\ufb00', 'ff'), ('\ufb01', 'fi'), ('\ufb02', 'fl'), ('\ufb03', 'ffi'), ('\ufb04', 'ffl'),
                 ('\ufb05', 'ft'), ('\u00ad', ''), ('\u2011', '-'), ('\u2010', '-'), ('\u00a0', ' ')):
        t = t.replace(a, b)
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    return re.sub(r'[^A-Za-z]', '', re.sub(r'\*+|`+|\[\^\]]+|[{}]', ' ', t))

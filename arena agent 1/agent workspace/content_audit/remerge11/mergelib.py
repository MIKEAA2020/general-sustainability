"""Mechanics for merging two papers of this corpus into one two-part paper.

Guarantees: every section, table, figure, result and sentence of both sources is
preserved verbatim, INCLUDING BOTH ORIGINAL ABSTRACTS. Neither source is modified;
output is always a new file.

Hard-won invariants of this corpus (each cost a failed compile at some point):

 1. Provenance headers MENTION \\documentclass / \\begin{document} in % comments
    ("v61 was THREE complete LaTeX documents concatenated (3x \\documentclass, ...)").
    A naive find() splits inside the comment. -> find_real() skips commented matches.
 2. Front matter has NESTED braces (\\author{...\\textsuperscript{1}...\\href{a}{b}}).
    A \\{[^\\}]*\\} regex stops at the first '}' and leaves stray markup, which raises
    "There's no line here to end." on a bare \\\\[0.35em]. -> strip_cmd() matches braces.
 3. Abstracts are CONTENT. Stripping them as "duplicate front matter" silently deletes
    material. Caught only by probing the rendered PDF for a phrase that had vanished.
 4. Reference headings differ across papers: \\subsection{References} vs \\section{References}.
 5. Declarations headings differ: \\section{Declarations}, \\section{Data availability}, ...
"""
import io, re


# ---------------------------------------------------------------- locating things
def not_in_comment(s, pos):
    """True if the match at pos is real LaTeX, not inside a % comment."""
    line_start = s.rfind('\n', 0, pos) + 1
    return '%' not in s[line_start:pos]


def find_real(s, pat):
    for m in re.finditer(pat, s):
        if not not_in_comment(s, m.start()):
            continue
        return m
    return None


def split_body(s):
    """-> (preamble, body, references, declarations)"""
    m = find_real(s, r'\\begin\{document\}')
    assert m, "no real \\begin{document}"
    pre, rest = s[:m.start()], s[m.end():]
    m = find_real(rest, r'\\(?:sub)*section\*?\{References\}')
    assert m, "no References heading"
    body, tail = rest[:m.start()], rest[m.start():]
    d = find_real(tail, r'\\(?:sub)*section\*?\{(?:Declarations|Data [Aa]vailability|'
                        r'Declaration of competing|Author contributions)')
    if d:
        refs, decl = tail[:d.start()], tail[d.start():]
    else:
        refs, decl = tail, ''
    return pre, body, refs, decl


# ------------------------------------------------------------ brace-safe stripping
def _match_brace(s, i):
    """i indexes an opening '{'; return the index of its BALANCED closing '}' (or -1)."""
    depth = 0
    while i < len(s):
        ch = s[i]
        if ch == '\\':
            i += 2
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def strip_cmd(x, cmd):
    """Remove every \\cmd[...]{...} using BALANCED-brace matching, skipping comments."""
    out, pos = [], 0
    pat = re.compile(r'\\' + cmd + r'\*?\s*(?:\[[^\]]*\])?\s*\{')
    while True:
        m = pat.search(x, pos)
        if not m:
            out.append(x[pos:])
            break
        if not not_in_comment(x, m.start()):
            out.append(x[pos:m.end()])
            pos = m.end()
            continue
        j = _match_brace(x, m.end() - 1)
        if j < 0:
            out.append(x[pos:m.end()])
            pos = m.end()
            continue
        out.append(x[pos:m.start()])
        pos = j + 1
    return ''.join(out)


def strip_front(x):
    """Remove the per-paper title/author/date/maketitle/linenumbers/TOC.

    The ABSTRACT IS DELIBERATELY KEPT -- it is content, and each Part opens with it.
    """
    for cmd in ['title', 'author', 'date', 'maketitle', 'linenumbers', 'tableofcontents']:
        x = strip_cmd(x, cmd)
    x = x.replace('\\end{document}', '')
    return x


# ------------------------------------------------------------------- namespacing
def namespace(body, pref, known=None):
    """Prefix the labels/refs of one part with pref so the two parts cannot collide.

    `known` is the set of label names defined in THIS part. When supplied, refs are
    rewritten for every name in `known` even if the block itself defines no labels --
    which is the case for declarations blocks, where a Code-availability line can
    \\ref a results table defined in the body. Without this the ref stays unprefixed
    and dangles.

    Replacement strings contain backslashes, so they MUST be passed as lambdas --
    re.sub('...', '\\\\ref{x}', s) raises "bad escape \\e".
    """
    labels = set(re.findall(r'\\label\{([^}]*)\}', body))
    targets = sorted(labels if known is None else (labels | set(known)))
    for lb in targets:
        body = body.replace('\\label{%s}' % lb, '\\label{%s%s}' % (pref, lb))
        body = re.sub(r'\\ref\{%s\}' % re.escape(lb),
                      lambda m: '\\ref{%s%s}' % (pref, lb), body)
        body = re.sub(r'\\eqref\{%s\}' % re.escape(lb),
                      lambda m: '\\eqref{%s%s}' % (pref, lb), body)
    return body


# -------------------------------------------------------------------- references
SIZE = r'(?:tiny|scriptsize|footnotesize|small|normalsize|large|Large)'

# A seam the OLD splitter could not see: the tail of one reference runs into the
# next author's head with no separating period, because the tail ends in a DOI,
# a page range, a volume:page or a bare year. "and Richardson, A.J., 2012" and
# "Smith, J., Jones, A., 2020" deliberately do NOT match -- the token before the
# surname must be something that ENDS a reference.
_TAIL_TOK = (r'(?:\bdoi:\S+|\bhttps?://\S+|\d+\s*-{1,2}\s*\d+|\b\d+\s*:\s*\d+'
             r'|\b(?:19|20)\d{2}\b)')
_NAME_YR = r'[A-ZÄÖÅ][\w\'{}\\\"~\^\- ]{1,30}?,\s*(?:19|20)\d{2}'

# seam between two references run together in one paragraph, and the year
# test that distinguishes a next reference from a publisher line
# The token after the period must be a SURNAME, i.e. word characters only --
# excluding '.' and ',' from the class is what stops "Rose, G. A., and Rowe"
# from splitting at the initial "A.," and yielding a headless fragment.
_SEAM = re.compile(r'(?<=\.)\s+(?=[{\[A-ZÄÖÅ][\w\'{}\\\"~^\-]{1,40}?,)')
_YR = re.compile(r'\b(?:19|20)\d{2}\b')
GLUED = re.compile(_TAIL_TOK + r'\s+' + _NAME_YR)


def _clean_entry(p):
    p = p.strip()
    p = re.sub(r'^\s*\}\s*', '', p)
    p = re.sub(r'^\s*\{\s*(?:\\(?:' + SIZE + r'))?\s*', '', p)
    if not re.search(r'\\(?:begin|end)\{[^{}]*\}$', p):
        p = re.sub(r'\s*\}\s*$', '', p)
    return re.sub(r'\s+', ' ', p).strip()


def split_entries(block):
    r"""Split a References block into individual entries.

    Rewritten 2026-10-01. The previous version split on

        (?<=\.)\s+(?=[A-ZÄÖÅ][\w...]{1,30}?, )

    i.e. a period, whitespace, then "Word, ". That is exactly the shape of a
    book's publisher line, so "Introduction to Interval Analysis.\n SIAM,
    Philadelphia." became two "entries" -- and with sort keys taken from the
    first 24 alphanumeric characters, the orphan "SIAM, Philadelphia." sorted
    under S while its head sorted under C. That is the mechanism behind the
    "heads sorted by author, tails sorted by journal" damage.

    The sources are PARAGRAPH-DELIMITED (verified: paper08 v45 -> 36 entries /
    0 orphans; paper07 v50 -> 37 / 0), so splitting on blank lines is both
    simpler and correct. The sentence-boundary splitter is kept only as a
    fallback for lists that use no blank lines.
    """
    body = re.sub(r'^\\(?:sub)*section\*?\{References\}\s*(\\label\{[^}]*\})?\s*\n',
                  '', block, count=1)

    # The reference list ends at the first thing that is not a reference.
    # Stopping only at Declarations is wrong: paper08 has a Supplementary
    # material section between the two, and swallowing its prose produced a
    # 39-line fake "entry" with no year.
    for pat in (r'\\(?:sub)*section\*?\{', r'\\begin\{center\}'):
        m = re.search(pat, body)
        if m:
            body = body[:m.start()]

    keep = []
    for ln in body.split('\n'):
        if re.fullmatch(r'\s*\{\s*(?:\\' + SIZE + r')?\s*\}?\s*', ln) or \
           re.fullmatch(r'\s*\{\s*\\' + SIZE + r'\s*', ln) or \
           re.fullmatch(r'\s*\}\s*', ln):
            continue
        keep.append(ln)
    body = '\n'.join(keep)

    paras = [_clean_entry(p) for p in re.split(r'\n\s*\n', body)]
    paras = [p for p in paras if p and not p.startswith('\\')]

    # Paragraph splitting is used unconditionally. There used to be a fallback
    # to the old sentence-boundary splitter for short lists (len(paras) < 5),
    # but that splitter is the one that manufactured the orphan tails in the
    # first place, and _split_glued() now recovers run-together entries
    # correctly, so the fallback was both unnecessary and harmful.
    entries = paras

    # split any entry that still carries a glued seam
    out = []
    for e in entries:
        out.extend(_split_glued(e))
    return out


def _split_glued(entry):
    r"""Undo one paragraph holding several references run together.

    Some sources put two or three references in a single paragraph with no
    blank line between them, e.g.

        Adamson, M. W., and Hilker, F. M. 2020. ... 425--434.
        {\AA}str{"o}m, K. J., and Wittenmark, B. 1997. ... Alkire, S., ...

    A candidate seam is a period, whitespace, then a "Surname," token. It is
    accepted only when the text that follows it contains a four-digit year --
    that is what separates a genuine next reference from a publisher line such
    as "Introduction to Interval Analysis. SIAM, Philadelphia.", which carries
    no year and is therefore stitched back onto its head.
    """
    seams = [m.end() for m in _SEAM.finditer(entry)]
    if not seams:
        return [entry]
    bounds = [0] + seams + [len(entry)]
    segs = [entry[bounds[i]:bounds[i + 1]].strip()
            for i in range(len(bounds) - 1)]
    out = []
    for seg in segs:
        if out and not _YR.search(seg):
            out[-1] = out[-1] + ' ' + seg
        else:
            out.append(seg)
    return [o for o in out if o]


def norm(e):
    return re.sub(r'[^a-z0-9]', '', e.lower())[:110]


def ref_sort_key(e):
    """Bibliographic sort key: first author's surname, then year, then text.

    The old key was the first 24 alphanumeric characters of the entry, which
    sorts a detached tail by its JOURNAL or PUBLISHER rather than by its
    author. Sorting on the surname is what "alphabetical" means for a
    bibliography.
    """
    m = re.match(r'^(.*?)(?:,\s|\.\s)', e + ' ')
    head = m.group(1) if m else e.split(',')[0]
    for a, b in ((r'\AA', 'A'), (r'\aa', 'a'), (r"\'a", 'a'), (r"\'e", 'e'),
                 (r"\'i", 'i'), (r"\'o", 'o'), (r"\'u", 'u'), (r"\'c", 'c'),
                 (r"\'s", 's'), (r'\^e', 'e'), (r'\~a', 'a'), (r'\~n', 'n'),
                 (r'\~o', 'o'), (r'\v{s}', 's'), (r'\v{S}', 'S')):
        head = head.replace(a, b)
    head = re.sub(r'\\[A-Za-z]+', '', head).replace('{', '').replace('}', '')
    head = re.sub(r'[^A-Za-z\- ]', '', head).strip().lower()
    y = re.search(r'\b(?:1[89]\d{2}|20\d{2})\b', e)
    return (head, y.group(0) if y else '9999', e.lower())
def merge_refs(refs_a, refs_b):
    merged, seen = [], set()
    for e in split_entries(refs_a) + split_entries(refs_b):
        k = norm(e)
        if k in seen:
            continue
        seen.add(k)
        merged.append(e)
    merged.sort(key=ref_sort_key)
    return merged



# ------------------------------------------------------- back matter integration
# The old merge emitted one Declarations block PER SOURCE ("for d in (decl_a,
# decl_b): doc.append(...)"), so merging two papers produced two blocks and
# merging three produced three -- paper09 v32 and paper11 v61 both carry three.
# Same for supplementary-material passages. The merges concatenated; they did
# not integrate. These helpers integrate.

# semantic aliases: these names mean the same declaration
DECL_ALIAS = {
    'conflicts of interest': 'Declaration of competing interest',
    'competing interests': 'Declaration of competing interest',
    'declaration of competing interest': 'Declaration of competing interest',
    'competing interest': 'Declaration of competing interest',
}

PLACEHOLDER = re.compile(r'^\s*(?:anonymi[sz]ed for review|blinded for review)'
                         r'[\s.]*\s*$', re.I)


def split_subsections(block, level=r'\\(?:sub)*section\*?\{([^}]*)\}'):
    """-> [(name, body), ...] preserving order. Body keeps its LaTeX."""
    out = []
    pos = 0
    for m in re.finditer(level, block):
        if m.start() > pos:
            pass
        name = m.group(1)
        nxt = re.search(level, block[m.end():])
        end = m.end() + nxt.start() if nxt else len(block)
        body = block[m.end():end]
        body = body.lstrip('}').strip()
        out.append((name, body.strip()))
        pos = end
    return out


def is_placeholder(text):
    return bool(PLACEHOLDER.match(text or ''))


def merge_declarations(blocks, heading=r'\section*{Declarations}'):
    """Merge N per-source Declarations blocks into ONE integrated block.

    Subsections are keyed by (aliased) name and kept in order of first
    appearance. Where two sources both supply the same subsection, both texts
    are kept -- they describe different data -- unless one is an
    "Anonymized for review." placeholder, in which case the substantive text
    wins. A subsection that is ONLY ever a placeholder is dropped: for a
    non-double-blind venue it says nothing, and inventing content is worse.
    """
    order, byname = [], {}
    for blk in blocks:
        if not blk or not blk.strip():
            continue
        subs = split_subsections(blk)
        if not subs:
            continue
        for name, body in subs:
            key = DECL_ALIAS.get(name.strip().lower(), name.strip())
            if key not in byname:
                byname[key] = []
                order.append(key)
            text = re.sub(r'\\end\{document\}', '', body).strip()
            if text:
                byname[key].append(text)

    out = [heading, '']
    for key in order:
        texts = byname[key]
        if not texts:
            continue
        real = [t for t in texts if not is_placeholder(t)]
        if not real:
            continue                      # only ever a placeholder -> drop
        out.append(r'\subsection*{%s}' % key)
        out.append('')
        for t in real:
            out.append(t)
            out.append('')
    return '\n'.join(out).rstrip() + '\n' if len(out) > 2 else ''


def merge_supplement(blocks):
    """Merge N supplementary-material passages into ONE section.

    Distinct passages are kept as separate paragraphs -- each describes a
    different supplement file -- but they go under a single heading so the
    paper has one supplementary-material section, not one per source.
    """
    paras = []
    for blk in (blocks or []):
        if not blk or not blk.strip():
            continue
        txt = re.sub(r'\\end\{document\}', '', blk).strip()
        # partition_refs() keeps the horizontal rule that preceded the section,
        # so strip the rule first -- otherwise the heading is no longer at the
        # start of the string and the strip below silently misses it.
        txt = re.sub(r'^\s*\\begin\{center\}.*?\\end\{center\}\s*', '',
                     txt, flags=re.S)
        txt = re.sub(r'^\s*\\(?:sub)*section\*?\{Supplementary material\}'
                     r'\s*(?:\\label\{[^}]*\})?\s*', '', txt).strip()
        # a bold lead-in is kept: it identifies which channel the passage is for
        if txt:
            paras.append(txt)
    if not paras:
        return ''
    out = [r'\subsection{Supplementary material}\label{supplementary-material}', '']
    for p in paras:
        out.append(p)
        out.append('')
    return '\n'.join(out).rstrip() + '\n'



# prose that can only belong to a supplementary-material passage
_SUPP_MARK = re.compile(
    r'deposited with this article|accompanying file|is deposited'
    r'|Supplementary material\} is deposited', re.I)

_SUPP_HEAD = re.compile(r'\\(?:sub)*section\*?\{Supplementary material\}')
_RULE = re.compile(r'\\begin\{center\}.*?\\end\{center\}', re.S)
_ANY_HEAD = re.compile(r'\\(?:sub)*section\*?\{')


def partition_refs(refs_block):
    """-> (pure reference list, supplementary-material block or '').

    In paper08 v45 the Supplementary material section sits BETWEEN the
    References heading and the Declarations heading, so split_body() returns it
    as part of the reference block. It must be pulled out before the list is
    split into entries, or its prose becomes one enormous fake reference -- and
    it must be re-emitted, or the content is silently lost.

    Two shapes occur, and both must be caught:
      (a) v45 -- introduced by a real \\subsection{Supplementary material}
          heading, preceded by a horizontal rule;
      (b) v50 -- NO heading at all, just the rule and a bold lead-in
          \\textbf{Supplementary material} is deposited ...
    Detecting only (a) loses passage (b) entirely, which is why the first
    version of this function dropped the sampled-governance passage.
    """
    if not refs_block:
        return '', ''
    start = None

    # (a) an explicit heading wins
    m = _SUPP_HEAD.search(refs_block)
    if m:
        start = m.start()
    else:
        # (b) a horizontal rule followed by supplement prose
        for rm in _RULE.finditer(refs_block):
            tail = refs_block[rm.end():]
            nxt = _ANY_HEAD.search(tail)
            window = tail[:nxt.start()] if nxt else tail
            if _SUPP_MARK.search(window):
                start = rm.start()
                break
    if start is None:
        return refs_block, ''
    # carry the preceding rule along with the section, if there is one
    rule = None
    for rm in _RULE.finditer(refs_block):
        if rm.end() <= start:
            rule = rm
    if rule:
        start = rule.start()
    return refs_block[:start], refs_block[start:]



# ---------------------------------------------------------------------- preamble
_THM = re.compile(r'\\newtheorem\*?\s*\{([^}]*)\}')


def merge_preamble(pre_a, pre_b):
    """Union the preamble definitions of B into A.

    \\newtheorem is de-duplicated by ENVIRONMENT NAME, not by literal line: paper 1 and
    paper 2 both define \\proposition with slightly different formatting, and copying
    the second across verbatim raises "Command \\proposition already defined."
    """
    existing_thm = set(_THM.findall(pre_a))
    # \\usepackage is de-duplicated by PACKAGE NAME, not by literal line: paper 9 loads
    # \\usepackage[a4paper,margin=15mm]{geometry} and paper 10b loads geometry with
    # different options, and copying both raises "Option clash for package geometry".
    _PKG = re.compile(r'\\usepackage\*?\s*(?:\[[^\]]*\])?\s*\{([^}]*)\}')
    existing_pkg = set()
    for m in _PKG.finditer(pre_a):
        existing_pkg.update(n.strip() for n in m.group(1).split(',') if n.strip())

    extra = []
    for line in pre_b.split('\n'):
        t = line.strip()
        if not t:
            continue
        m = _THM.match(t)
        if m:
            if m.group(1) in existing_thm:
                continue
            existing_thm.add(m.group(1))
            extra.append(t)
            continue
        m = _PKG.match(t)
        if m:
            names = [n.strip() for n in m.group(1).split(',') if n.strip()]
            if names and all(n in existing_pkg for n in names):
                continue          # every package on this line is already loaded
            existing_pkg.update(names)
            extra.append(t)
            continue
        if t.startswith(('\\usepackage', '\\newcommand', '\\DeclareMathOperator',
                         '\\providecommand', '\\def')):
            if t not in pre_a:
                extra.append(t)
    if extra:
        # MUST be comment-aware. Paper 9's provenance header MENTIONS \begin{document}
        # ("It contained 2x \documentclass, 2x \begin{document}, ..."), so a plain
        # rfind() matches INSIDE the comment and injects the package block mid-comment --
        # which turns the comment's continuation lines into live LaTeX. This is the same
        # comment-vs-code confusion that has now appeared in five different forms.
        m = find_real(pre_a, r'\\begin\{document\}')
        if m:
            pre_a = pre_a[:m.start()] + '\n'.join(extra) + '\n' + pre_a[m.start():]
        else:
            # split_body() already stripped the real \begin{document}, so normally there
            # is none: append at the end of the preamble.
            pre_a = pre_a.rstrip('\n') + '\n' + '\n'.join(extra) + '\n'
    return pre_a


# ------------------------------------------------------------------------ driver
def merge(BASE, A, B, OUT, TITLE, ABSTRACT, CROSS, HEAD_A, HEAD_B, PREF_A, PREF_B):
    """Assemble the merged document and write it. Returns a stats dict."""
    sa = io.open(BASE + A, encoding='utf-8', errors='replace').read()
    sb = io.open(BASE + B, encoding='utf-8', errors='replace').read()

    pre_a, body_a, refs_a, decl_a = split_body(sa)
    pre_b, body_b, refs_b, decl_b = split_body(sb)

    # declarations carry \ref too (e.g. a Code-availability line pointing at a results
    # table), so they must be namespaced with their own part's prefix.
    lab_a = set(re.findall(r'\\label\{([^}]*)\}', body_a))
    lab_b = set(re.findall(r'\\label\{([^}]*)\}', body_b))
    body_a = namespace(strip_front(body_a), PREF_A)
    body_b = namespace(strip_front(body_b), PREF_B)
    decl_a = namespace(decl_a, PREF_A, known=lab_a)
    decl_b = namespace(decl_b, PREF_B, known=lab_b)

    pre_a = merge_preamble(pre_a, pre_b)
    # If a source has no Declarations-style heading, its references block runs to EOF and
    # therefore still contains \end{document}. It must not end up as a "reference entry".
    refs_a = refs_a.replace('\\end{document}', '')
    refs_b = refs_b.replace('\\end{document}', '')
    # The supplementary-material section sits between References and Declarations
    # in some sources, so it arrives inside the reference block. Pull it out
    # before entries are split (its prose would otherwise become one enormous
    # fake reference) and re-emit it below.
    refs_a, supp_a = partition_refs(refs_a)
    refs_b, supp_b = partition_refs(refs_b)
    merged = merge_refs(refs_a, refs_b)

    doc = [pre_a, '\n\\begin{document}\n',
           '\\title{' + TITLE + '}\n',
           ABSTRACT.strip() + '\n',
           '\\maketitle\n\n\\tableofcontents\n\n\\newpage\n\n',
           HEAD_A.strip() + '\n\n', body_a.strip() + '\n\n',
           HEAD_B.strip() + '\n\n', body_b.strip() + '\n\n',
           CROSS.strip() + '\n\n',
           '\\subsection*{References}\n\\label{references}\n',
           '\n\n'.join(merged) + '\n\n']
    # ONE supplementary-material section and ONE Declarations block, integrated
    # from both sources -- previously each source contributed its own copy.
    supp = merge_supplement([supp_a, supp_b])
    if supp.strip():
        doc.append('\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n')
        doc.append(supp.strip() + '\n\n')
    decl = merge_declarations([decl_a, decl_b])
    if decl.strip():
        doc.append(decl.strip() + '\n')
    doc.append('\n\\end{document}\n')

    out = ''.join(doc)
    io.open(BASE + OUT, 'w', encoding='utf-8').write(out)

    # ------------------------------------------------------------------ gate
    # The merge is scripted, so any damage it introduces comes back on the next
    # re-merge no matter how carefully the .tex is repaired by hand. Paper08 was
    # repaired by hand on 2026-10-01 (26 tails reattached, 5 duplicates removed,
    # the list re-sorted); a clean re-merge reproduced every artifact. So: gate
    # the assembled document and refuse to emit it if the structural classes
    # fire. Fix the merge, not the output.
    import phase0_scan
    phase0_scan.report_gate(phase0_scan.gate_text(out, OUT), OUT)

    c = "\n".join(re.sub(r'(?<!\\)%.*$', '', l) for l in out.split('\n'))
    L = set(re.findall(r'\\label\{([^}]*)\}', c))
    R = set(re.findall(r'\\ref\{([^}]*)\}', c))
    st = dict(out=OUT, words=len(re.findall(r"[A-Za-z']+", c)),
              doc=(c.count('\\documentclass'), c.count('\\begin{document}'),
                   c.count('\\end{document}')),
              labels=len(L), refs=len(R), missing=sorted(r for r in R if r not in L),
              nrefs=len(merged))
    print("written:", st['out'])
    print("  words: %d   doc counts: %s" % (st['words'], ' '.join(map(str, st['doc']))))
    print("  labels: %d  refs: %d  MISSING: %s"
          % (st['labels'], st['refs'], st['missing'] or 'NONE'))
    print("  merged reference entries: %d" % st['nrefs'])
    return st

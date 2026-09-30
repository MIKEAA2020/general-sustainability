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
def split_entries(block):
    """Split a References block into individual entries.

    Some papers wrap the whole list in a size group (paper 1 uses
    `{\\footnotesize ... }`). The opener and closer must be stripped BEFORE entries are
    split and sorted, or the sort scatters them into different entries and the merged
    reference section has an unbalanced group -> "Too many }'s" at the end of the
    document.
    """
    body = re.sub(r'^\\(?:sub)*section\*?\{References\}\s*(\\label\{[^}]*\})?\s*\n',
                  '', block, count=1)
    # Drop size-group delimiter LINES before splitting. Some papers wrap the list -- or
    # several sub-blocks of it -- in { ... } / {\footnotesize ... } with the delimiter on
    # its own line. The entry splitter cannot break across them (there is no ". " to key
    # on), so the opener and closer stay glued to whichever entries were first and last,
    # and an alphabetical sort scatters them -> "Too many }'s" at end of document.
    SIZE = r'(?:tiny|scriptsize|footnotesize|small|normalsize|large|Large)'
    keep = []
    for ln in body.split('\n'):
        if re.fullmatch(r'\s*\{\s*(?:\\' + SIZE + r')?\s*\}?\s*', ln) or \
           re.fullmatch(r'\s*\{\s*\\' + SIZE + r'\s*', ln) or \
           re.fullmatch(r'\s*\}\s*', ln):
            continue
        keep.append(ln)
    body = '\n'.join(keep)

    parts = re.split(r'(?<=\.)\s+(?=[A-ZÄÖÅ][\w\'{}\\\"~\^\- ]{1,30}?, )', body)
    # Clean PER ENTRY, not just at the block ends. A size-group opener/closer can end up
    # attached to whichever entry happened to be first/last in the source, and after an
    # alphabetical sort that entry lands in the middle of the merged list -- leaving an
    # unbalanced group ("Too many }'s"). Strip only brace wrappers that look like size
    # groups, so legitimate braces inside an entry survive.
    out = []
    for p in parts:
        p = re.sub(r'^\s*\}\s*', '', p.strip())
        p = re.sub(r'^\s*\{\s*(?:\\(?:tiny|scriptsize|footnotesize|small|normalsize|large))?\s*',
                   '', p)
        p = re.sub(r'\s*\}\s*$', '', p)
        if p.strip():
            out.append(p.strip())
    return out


def norm(e):
    return re.sub(r'[^a-z0-9]', '', e.lower())[:110]


def merge_refs(refs_a, refs_b):
    merged, seen = [], set()
    for e in split_entries(refs_a) + split_entries(refs_b):
        k = norm(e)
        if k in seen:
            continue
        seen.add(k)
        merged.append(e)
    merged.sort(key=lambda e: re.sub(r'[^a-z]', '', e.lower())[:24])
    return merged


# ---------------------------------------------------------------------- preamble
_THM = re.compile(r'\\newtheorem\*?\s*\{([^}]*)\}')


def merge_preamble(pre_a, pre_b):
    """Union the preamble definitions of B into A.

    \\newtheorem is de-duplicated by ENVIRONMENT NAME, not by literal line: paper 1 and
    paper 2 both define \\proposition with slightly different formatting, and copying
    the second across verbatim raises "Command \\proposition already defined."
    """
    existing_thm = set(_THM.findall(pre_a))
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
        if t.startswith(('\\usepackage', '\\newcommand', '\\DeclareMathOperator',
                         '\\providecommand', '\\def')):
            if t not in pre_a:
                extra.append(t)
    if extra:
        i = pre_a.rfind('\\begin{document}')
        pre_a = pre_a[:i] + '\n'.join(extra) + '\n' + pre_a[i:]
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
    for d in (decl_a, decl_b):
        if d.strip():
            doc.append(d.replace('\\end{document}', '').strip() + '\n')
    doc.append('\n\\end{document}\n')

    out = ''.join(doc)
    io.open(BASE + OUT, 'w', encoding='utf-8').write(out)

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

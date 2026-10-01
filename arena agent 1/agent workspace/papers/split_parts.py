#!/usr/bin/env python3
"""Split the two \\part-structured container sources into standalone papers.

NON-DESTRUCTIVE: containers are left untouched. New numbered versions are written.

  paper05_exact_belief_computation_v15.tex
      Part I  -> paper05_exact_belief_computation_v16.tex        (unit 5)
      Part II -> paper11c_worked_systems_audit_v3.tex            (unit 11)

  paper06_assessment_separation_v66.tex
      Part I  -> paper06_assessment_separation_v67.tex           (unit 6)
      Part II -> paper10_depletion_ledgers_v54.tex               (unit 9)

Both containers are asymmetric, so each is handled explicitly:
  - paper05: umbrella title+abstract+maketitle+toc, then Part I (own abstract),
    then Part II (own abstract).
  - paper06: umbrella title+abstract+maketitle+toc, then Part I (NO own abstract --
    it uses the umbrella's), then Part II (abstract emitted as \\section*{Abstract}).
    Part I therefore RETAINS the umbrella abstract, which is what the source renders.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def balanced(cmd, s, start=0):
    """Return (start, end) of \\cmd{...} with balanced braces, or None."""
    m = re.search(r'\\' + cmd + r'\s*\{', s[start:])
    if not m:
        return None
    i = start + m.end() - 1          # at '{'
    depth, j = 0, i
    while j < len(s):
        if s[j] == '{':
            depth += 1
        elif s[j] == '}':
            depth -= 1
            if depth == 0:
                return (start + m.start(), j + 1)
        j += 1
    return None


def preamble_and_title(s):
    """Return (preamble_incl_begin_document, title_cmd, author_cmd)."""
    m = re.search(r'\\begin\{document\}', s)
    bd_end = s.index('\n', m.end()) + 1
    preamble = s[:bd_end]
    t = balanced('title', s, bd_end)
    title = s[t[0]:t[1]] if t else None
    a = balanced('author', s, bd_end)
    author = s[a[0]:a[1]] if a else None
    return preamble, title, author


def reference_block(s):
    """The shared, hand-formatted reference list.

    Both containers keep ONE bibliography at the very end of the document, inside Part II's
    character range, but it serves BOTH parts. A naive split therefore leaves every part
    without a reference list.

    Note these papers use no \\cite commands -- citations are literal inline text -- so a
    missing list produces no '?' markers and the defect is invisible until the end of the
    document. It is nonetheless fatal for publication, so the list is attached to every part.
    """
    m = re.search(r'\\(?:section|subsection|chapter)\*?\{[^}]*'
                  r'(?:Reference|Bibliograph)[^}]*\}', s, re.I)
    if not m:
        return None
    start = m.start()

    # paper06's list is FRAGMENTED: it runs A..V, is interrupted by a Supplementary material
    # section, then resumes with a SECOND \label{references} block. A naive "stop at the next
    # heading" therefore truncates it. Run to the Declarations section instead, then drop the
    # Supplementary sections that were interleaved.
    decl = re.search(r'\\(?:section|subsection|chapter)\*?\{[^}]*Declarations[^}]*\}',
                     s[start:])
    end = start + decl.start() if decl else s.rindex('\\end{document}')
    block = s[start:end]

    # Rather than stripping the interleaved Supplementary sections wholesale (which also
    # discards the reference entries sitting inside them), keep the heading plus every
    # paragraph that has the shape of a hand-formatted bibliography entry: a paragraph
    # beginning "Surname, X." Supplementary prose does not match and is dropped.
    # A shape test on "Surname, X." alone is too strict: it drops institutional authors with
    # no comma ("DFO. (2016).", "World Bank. (2011)."), lowercase nobiliary prefixes
    # ("von Neumann, J. (1928)."), and LaTeX accents ("Sch\\\"ar, S., ... (2025)."). All of
    # those are cited by Part I and all were verified present in the container list.
    # Bibliography entries essentially always carry a year, so that is the robust test.
    paras = re.split(r'\n\s*\n', block)
    bibpara = re.compile(r'^\s*[A-Z][A-Za-z\-\'\\]+,\s+[A-Z]\.')
    hasyear = re.compile(r'\((?:19|20)\d\d\)')
    kept = [paras[0]] + [p for p in paras[1:]
                         if bibpara.match(p) or hasyear.search(p)]

    # The list carries \label{references} twice; keep only the first.
    block = '\n\n'.join(k for k in kept if k.strip())
    labs = [x.start() for x in re.finditer(r'\\label\{references\}', block)]
    for pos in reversed(labs[1:]):
        block = block[:pos] + block[pos + len('\\label{references}'):]
    return block


def write(out, preamble, title, author, body, note, need_maketitle=False, refs=None):
    parts = [preamble]
    if title:
        parts.append(title + '\n')
    if author:
        parts.append(author + '\n')
    if need_maketitle:
        parts.append('\\maketitle\n')
    parts.append('\n' + body.rstrip() + '\n')
    if refs:
        parts.append('\n' + refs.rstrip() + '\n')
    parts.append('\n\\end{document}\n')
    assembled = ''.join(parts)
    # Fail BEFORE writing. Previously this splitter silently discarded the
    # source's declarations/supplement section and selected bibliography
    # paragraphs by appearance, losing cited works and citation tails. It is
    # unsafe to regenerate a head until those source-specific pieces are
    # explicitly carried over and reconciled. A failing splitter is preferable
    # to another plausible-looking, content-incomplete live manuscript.
    if os.path.basename(out).startswith('paper05_'):
        required = (r'\subsection*{Declarations}', 'Chatterjee, K., Doyen, L., Henzinger, T.A., 2009.',
                    'Chapter 4, The Sperner', 'Operations Research 39, 162--175.')
    elif os.path.basename(out).startswith('paper06_'):
        required = (r'\section*{Supplementary Material}', r'\section*{Declarations}',
                    'Dasgupta, P., and M', 'Net national product, wealth, and',
                    'Springer, New York, 953--986.')
    elif os.path.basename(out).startswith('paper11c_'):
        # The v15 container imported its cited Saint-Pierre (1994) entry
        # after the AI declaration, and this split previously attached no
        # bibliography to Part II. Refuse a citation-incomplete new v3.
        required = (r'\subsection*{References}',
                    'Saint-Pierre, P., 1994. Approximation of the viability kernel.',
                    r'\subsection*{Declarations}')
    else:
        required = ()
    missing = [item for item in required if item not in assembled]
    if missing:
        raise RuntimeError('REFUSE TO WRITE content-incomplete split %s; missing %s. '
                           'Restore from its documented source before splitting.'
                           % (os.path.basename(out), missing))
    open(out, 'w', encoding='utf-8').write(assembled)
    print('  wrote %-46s %7d chars' % (os.path.basename(out),
                                       os.path.getsize(out)))


def main():
    os.chdir(HERE)
    jobs = []

    # ---------------- paper05 : unit 5 (Part I) + unit 11 (Part II) ----------
    f = 'paper05_exact_belief_computation_v15.tex'
    s = open(f, encoding='utf-8', errors='replace').read()
    pre, title, author = preamble_and_title(s)
    refs = reference_block(s)
    assert refs, 'paper05: no reference list found'
    parts = [m.start() for m in re.finditer(r'\\part\*?\{', s)]
    assert len(parts) == 2, 'paper05 expected 2 \\part, got %d' % len(parts)
    enddoc = s.rindex('\\end{document}')
    # Paper05's Part I has its OWN \\title/\\maketitle/\\begin{abstract}. Keeping the umbrella
    # block as well would emit two \maketitle and print the title block twice, so Part I starts
    # AT its \\part and the umbrella \\title is injected instead. Part II has no title of its
    # own, so it starts at its \\part and relies on the injected umbrella \\title.
    jobs.append(('paper05_exact_belief_computation_v16.tex', pre, title, author,
                 s[parts[0]:parts[1]], 'unit 5  (Part I)', False, refs))
    jobs.append(('paper11c_worked_systems_audit_v3.tex', pre, title, author,
                 s[parts[1]:enddoc], 'unit 11 (Part II)'))

    # ---------------- paper06 : unit 6 (Part I) + unit 9 (Part II) ----------
    f = 'paper06_assessment_separation_v66.tex'
    s = open(f, encoding='utf-8', errors='replace').read()
    pre, title, author = preamble_and_title(s)
    refs = reference_block(s)
    assert refs, 'paper06: no reference list found'
    parts = [m.start() for m in re.finditer(r'\\part\*?\{', s)]
    assert len(parts) == 2, 'paper06 expected 2 \\part, got %d' % len(parts)
    enddoc = s.rindex('\\end{document}')
    # Paper06's Part I DOES have its own abstract but emits no \\maketitle of its own -- in the
    # container the umbrella's \\maketitle covers both parts. So Part I starts at its \\part and
    # gets an injected \\title + \\maketitle; its own abstract then follows the Part heading.
    jobs.append(('paper06_assessment_separation_v67.tex', pre, title, author,
                 s[parts[0]:parts[1]], 'unit 6  (Part I)', True, refs))
    jobs.append(('paper10_depletion_ledgers_v54.tex', pre, title, author,
                 s[parts[1]:enddoc], 'unit 9  (Part II)', False, refs))

    for job in jobs:
        out, pre, title, author, body, note = job[:6]
        need_mt = job[6] if len(job) > 6 else False
        refs = job[7] if len(job) > 7 else None
        print('%s' % note)
        write(out, pre, title, author, body, note, need_mt, refs)


if __name__ == '__main__':
    main()

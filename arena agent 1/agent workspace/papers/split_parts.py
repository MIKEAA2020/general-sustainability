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


def write(out, preamble, title, author, body, note, need_maketitle=False):
    parts = [preamble]
    if title:
        parts.append(title + '\n')
    if author:
        parts.append(author + '\n')
    if need_maketitle:
        parts.append('\\maketitle\n')
    parts.append('\n' + body.rstrip() + '\n\n\\end{document}\n')
    open(out, 'w', encoding='utf-8').write(''.join(parts))
    print('  wrote %-46s %7d chars' % (os.path.basename(out),
                                       os.path.getsize(out)))


def main():
    os.chdir(HERE)
    jobs = []

    # ---------------- paper05 : unit 5 (Part I) + unit 11 (Part II) ----------
    f = 'paper05_exact_belief_computation_v15.tex'
    s = open(f, encoding='utf-8', errors='replace').read()
    pre, title, author = preamble_and_title(s)
    parts = [m.start() for m in re.finditer(r'\\part\*?\{', s)]
    assert len(parts) == 2, 'paper05 expected 2 \\part, got %d' % len(parts)
    enddoc = s.rindex('\\end{document}')
    # Paper05's Part I has its OWN \\title/\\maketitle/\\begin{abstract}. Keeping the umbrella
    # block as well would emit two \maketitle and print the title block twice, so Part I starts
    # AT its \\part and the umbrella \\title is injected instead. Part II has no title of its
    # own, so it starts at its \\part and relies on the injected umbrella \\title.
    jobs.append(('paper05_exact_belief_computation_v16.tex', pre, title, author,
                 s[parts[0]:parts[1]], 'unit 5  (Part I)'))
    jobs.append(('paper11c_worked_systems_audit_v3.tex', pre, title, author,
                 s[parts[1]:enddoc], 'unit 11 (Part II)'))

    # ---------------- paper06 : unit 6 (Part I) + unit 9 (Part II) ----------
    f = 'paper06_assessment_separation_v66.tex'
    s = open(f, encoding='utf-8', errors='replace').read()
    pre, title, author = preamble_and_title(s)
    parts = [m.start() for m in re.finditer(r'\\part\*?\{', s)]
    assert len(parts) == 2, 'paper06 expected 2 \\part, got %d' % len(parts)
    enddoc = s.rindex('\\end{document}')
    # Paper06's Part I DOES have its own abstract but emits no \\maketitle of its own -- in the
    # container the umbrella's \\maketitle covers both parts. So Part I starts at its \\part and
    # gets an injected \\title + \\maketitle; its own abstract then follows the Part heading.
    jobs.append(('paper06_assessment_separation_v67.tex', pre, title, author,
                 s[parts[0]:parts[1]], 'unit 6  (Part I)', True))
    jobs.append(('paper10_depletion_ledgers_v54.tex', pre, title, author,
                 s[parts[1]:enddoc], 'unit 9  (Part II)'))

    for job in jobs:
        out, pre, title, author, body, note = job[:6]
        need_mt = job[6] if len(job) > 6 else False
        print('%s' % note)
        write(out, pre, title, author, body, note, need_mt)


if __name__ == '__main__':
    main()

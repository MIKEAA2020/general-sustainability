#!/usr/bin/env python3
"""Extract unit 1 (obstruction calculus) from the paper01_v62 container.

NON-DESTRUCTIVE: writes only paper01_obstruction_calculus_v63.tex.
The container paper01_obstruction_calculus_v62.tex is not touched.

Container layout (verified 2026-09-30):
  L1-67    preamble: comments, \\documentclass, packages, \\AtBeginDocument, \\begin{document}
  L68      \\title{...umbrella, names both parts...}
  L69-122  umbrella abstract (describes Part I and Part II jointly)
  ~L120    \\maketitle, \\tableofcontents, \\newpage
  L124     \\part*{Part I ...}   <- UNIT 1 begins
  L1969    \\part*{Part II ...}  <- UNIT 2 begins
  L3664    \\label{references}   <- shared bibliography
  L3869    \\section*{Declarations}
  end      \\end{document}

Unit 1 output = preamble (title re-scoped to unit 1) + Part I body (its own
\\maketitle and abstract, which Part I already carries) + the shared
bibliography in full + declarations.

The bibliography is shared and is reproduced in full on purpose: an extra
uncited entry is harmless, a missing one is not.
"""

import io, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__)) + '/'
SRC = 'paper01_obstruction_calculus_v62.tex'
OUT = 'paper01_obstruction_calculus_v63.tex'
TITLE = 'Obstruction certificates under incomplete observation'

src = io.open(BASE + SRC, encoding='utf-8', errors='replace').read()
L = src.split('\n')


def find_line(pat, start=0):
    for i in range(start, len(L)):
        if re.search(pat, L[i]):
            return i
    raise SystemExit('FATAL: could not locate %r' % pat)


i_doc = find_line(r'^\\begin\{document\}')
i_part1 = find_line(r'^\\part\*\{Part I')
i_part2 = find_line(r'^\\part\*\{Part II')
i_refs = find_line(r'\\label\{references\}')
i_refs_heading = find_line(r'^\\(?:sub)*section\*?\{References\}')
assert i_refs_heading < i_refs and i_refs - i_refs_heading <= 2, 'FATAL: References heading/label not adjacent'
i_decl = find_line(r'\\section\*\{Declarations')
i_end = find_line(r'^\\end\{document\}')

assert i_doc < i_part1 < i_part2 < i_refs < i_decl < i_end, 'FATAL: unexpected ordering'

# ---- preamble: keep everything up to \begin{document}, drop the umbrella \title --------
pre = L[:i_doc + 1]
pre = [l for l in pre if not l.startswith('\\title{')]
pre.insert(len(pre) - 1, '\\title{%s}' % TITLE)

# ---- Part I body: skip the \part* wrapper, keep \maketitle + abstract + body -----------
body = L[i_part1 + 1:i_part2]
# drop the part-level label / toc lines that belong to the container, not the unit
body = [l for l in body if not re.match(r'^\\(label\{part:|addcontentsline\{toc\}\{part\})', l)]
# trim blank run at the top, then the part title line itself
while body and not body[0].strip():
    body.pop(0)

# ---- shared bibliography + declarations ------------------------------------------------
back = L[i_refs_heading:i_end]  # include References heading; never start at its label

out = '\n'.join(pre + body + [''] + back + ['\\end{document}'])

# ---- verification ----------------------------------------------------------------------
def bal(s):
    return s.count('{') - s.count('}')

print('source          : %s' % SRC)
print('Part I lines    : %d..%d (%d lines)' % (i_part1 + 1, i_part2, i_part2 - i_part1 - 1))
print('references      : from L%d' % (i_refs + 1))
print('output words    : %d' % len(out.split()))
print('braces balance  : %+d   (must be 0)' % bal(out))
for env in ('document', 'abstract', 'enumerate', 'itemize', 'tabular', 'figure', 'table'):
    b = len(re.findall(r'\\begin\{%s\}' % env, out))
    e = len(re.findall(r'\\end\{%s\}' % env, out))
    flag = '' if b == e else '   *** MISMATCH ***'
    print('  %-11s begin=%-4d end=%-4d%s' % (env, b, e, flag))
print('\\part commands  : %d   (must be 0 -- unit is standalone)' % len(re.findall(r'\\part\*?\{', out)))
print('\\maketitle      : %d   (must be 1)' % len(re.findall(r'\\maketitle', out)))
print('\\title          : %d   (must be 1)' % len(re.findall(r'\\title\{', out)))

# dangling \ref check (comments stripped)
nc = re.sub(r'(?<!\\)%.*$', '', out, flags=re.M)
labels = set(re.findall(r'\\label\{([^}]+)\}', nc))
refs = set(re.findall(r'\\ref\{([^}]+)\}', nc))
dangling = sorted(refs - labels)
print('labels=%d refs=%d dangling=%d' % (len(labels), len(refs), len(dangling)))
if dangling:
    print('  dangling:', dangling[:15])

if bal(out) != 0:
    raise SystemExit('FATAL: unbalanced braces; not writing.')

# Fail closed until the v62 shared bibliography is reconstructed from BOTH
# paragraph-delimited sources, and the paper01 v61 byline is carried over.
# The old v62 list interleaves heads and detached publisher/year/page tails;
# copying it intact is NOT equivalent to preserving references. The reviewed
# terminal v63 repair is content_audit/repair_01.py, which reads v61 + paper02
# v12 and compares works semantically. Never overwrite it with the broken list.
required = ('\\author{Amin Abaee',
            'Nagumo, M.:', 'Japan 24, 551--559',
            'LNCS, vol.~2993, pp.~477--492.',
            'Aubin, J.-P.: Viability Theory. Birkh\\"auser, Boston (1991)')
missing = [x for x in required if x not in out]
if missing or not re.search(r'\\(?:sub)*section\*?\{References\}', out):
    raise SystemExit('FATAL: content-incomplete paper01 extraction; missing '
                     + repr(missing) + '. Repair v62 bibliography and source author before regeneration.')
# For entries documented as dislocated, physical proximity matters too.
refs_text = '\n'.join(back)
for head, tail in (('Nagumo, M.:', 'Japan 24, 551--559'),
                   ('Prajna, S., Jadbabaie, A.:', 'LNCS, vol.~2993, pp.~477--492.')):
    segment = refs_text[refs_text.index(head):refs_text.index(tail)] if head in refs_text and tail in refs_text else ''
    if not segment or '\n\n' in segment:
        raise SystemExit('FATAL: detached reference tail after ' + head + '; refusing output')

io.open(BASE + OUT, 'w', encoding='utf-8').write(out)
print('\nwritten: %s' % OUT)

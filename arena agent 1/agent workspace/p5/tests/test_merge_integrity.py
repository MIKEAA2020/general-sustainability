"""Regression test for mergelib.merge(): the generic path used by
merge_01_02 / merge_03_04 / merge_05_11c / merge_06_10 / merge_09_9b_10b."""
import io
import os
import re
import sys

sys.path.insert(0, '/home/user/p5')
import mergelib

PRE = r'''\documentclass{article}
\usepackage{amsmath}
\begin{document}
\title{T}
\maketitle
'''

A = PRE + r'''
\section{Alpha}
Body alpha text.

\subsection{References}
Adams, J. 2001. First paper. Journal One, 1: 1--10.

Baker, K. 2002. Second paper. Journal Two, 2: 20--30.

\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}

\subsection{Supplementary material}
\label{supplementary-material}

Delay-channel material is provided in the accompanying file
\texttt{paper08_supplementary_delay.md}.

\section*{Declarations}

\subsection*{Data availability}

Alpha data statement.

\subsection*{Competing interests}

The author declares no competing interests.

\end{document}
'''

B = PRE + r'''
\section{Beta}
Body beta text.

\subsection{References}
Baker, K. 2002. Second paper. Journal Two, 2: 20--30.

Cross, L. 2003. Third paper. Journal Three, 3: 30--40.

\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}

\textbf{Supplementary material} is deposited with this article (the
accompanying Supplementary file): the governance material in
\texttt{paper08_supplementary_governance.md}.

\section*{Declarations}

\subsection*{Data availability}

Beta data statement.

\subsection*{Ethics approval}

Not applicable.

\end{document}
'''

import tempfile
D = tempfile.mkdtemp()
io.open(D + '/a.tex', 'w', encoding='utf-8').write(A)
io.open(D + '/b.tex', 'w', encoding='utf-8').write(B)
mergelib.merge(D + '/', 'a.tex', 'b.tex', 'out.tex',
               'Test title', 'Test abstract.',
               r'\\section*{Cross}', r'\\section*{Alpha}', r'\\section*{Beta}',
               'a', 'b')
out = io.open(D + '/out.tex', encoding='utf-8').read()

checks = [
    ('Declarations blocks == 1',
     len(re.findall(r'\\section\*\{Declarations\}', out)) == 1),
    ('Supplementary material heading == 1',
     len(re.findall(r'\\subsection\{Supplementary material\}', out)) == 1),
    ('delay supplement passage kept', 'supplementary_delay' in out),
    ('governance supplement passage kept', 'supplementary_governance' in out),
    ('Data availability subsection == 1',
     len(re.findall(r'\\subsection\*\{Data availability\}', out)) == 1),
    ('alpha data statement kept', 'Alpha data statement' in out),
    ('beta data statement kept', 'Beta data statement' in out),
    ('both bodies kept', 'Body alpha text' in out and 'Body beta text' in out),
    ('exactly one \\end{document}', out.count('\\end{document}') == 1),
]

# reference list: 3 unique works, no orphan tails, no glued entries
m = re.search(r'\\subsection\*\{References\}', out)
tail = out[m.start():]
d = re.search(r'\\section\*\{Declarations\}', tail)
ents = mergelib.split_entries(tail[:d.start()] if d else tail)
glued = [e for e in ents
         if any(mergelib._YR.search(e[mm.end():])
                for mm in mergelib._SEAM.finditer(e))]
checks.append(('3 unique references (Adams/Baker/Cross)', len(ents) == 3))
checks.append(('no glued entries', not glued))
checks.append(('no headless fragments',
               not [e for e in ents if re.match(r'^[A-Z]\.,', e)]))

ok = True
for name, passed in checks:
    print('  %-42s %s' % (name, 'PASS' if passed else 'FAIL'))
    ok = ok and passed
print('\nmergelib.merge(): %s' % ('ALL PASS' if ok else 'FAILURES PRESENT'))
sys.exit(0 if ok else 1)

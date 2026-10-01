#!/usr/bin/env python3
"""Restore paper05's documented source back matter and bibliography, idempotent/fail-loud."""
import pathlib,re,difflib
D=pathlib.Path('/home/user/papers')
h=D/'paper05_exact_belief_computation_v16.tex'
s=D/'paper05_exact_belief_computation_v14.tex'
x=h.read_text();src=s.read_text()
assert '\\subsection*{Declarations}' in src and '\\subsection*{Declarations}' not in x
# Restore the source's exact author block (nested braces), as approved by the owner.
import sys
sys.path.insert(0,'/home/user/p5');import mergelib
m=re.search(r'\\author\{',src);assert m
j=mergelib._match_brace(src,m.end()-1);author=src[m.start():j+1]
assert '\\author{' not in x
x=x.replace('\\maketitle\n','% Restored verbatim from paper05 v14 (source author block).\n'+author+'\n\\maketitle\n',1)
# Exact source bibliography entry, missing even though cited in the live body.
a=src.index('Chatterjee, K., Doyen, L., Henzinger, T.A., 2009.')
b=src.index('Engel, K., 1997.',a)
entry=src[a:b].strip()
assert entry.count('Chatterjee, K.')==1
assert 'Chatterjee, K., Doyen, L., Henzinger, T.A., 2009.' not in x
anchor='Engel, K., 1997.';assert x.count(anchor)==1
x=x.replace(anchor,entry+'\n\n'+anchor,1)
# Recover only source-derived extra details; keep the rest of each target entry.
old='Stanley, R.P., 2013. \\emph{Topics in Algebraic Combinatorics}.'
a=src.index(old); full=src[a:src.index('\n}',a)].strip()
assert x.count(old)==1 and 'Chapter 4, The Sperner property' not in x
x=x.replace(old,full.strip(),1)
old=('Lovejoy, W.S., 1991. Computationally feasible bounds for partially\n'
     'observed Markov decision processes.')
assert x.count(old)==1 and 'Operations Research 39, 162--175.' not in x
x=x.replace(old,old+' Operations Research 39, 162--175.',1)
# Declarations: source statements with a narrow verification-scope correction.
# The live paper adds a full five-cube classification AFTER v14; the v13 script
# cannot be claimed to reproduce that new result without a fresh verification.
# The contribution sentence is provided by the owner, not inferred.
decl=src[src.index('\\subsection*{Declarations}'):src.rindex('\\end{document}')].strip()
oldclaim=('(folder \\texttt{arena agent 1/paper rewrites/latex}); it reproduces all bounds, bands, ladder values, pairings,\n'
          'census counts, and thresholds verbatim.')
assert decl.count(oldclaim)==1
decl=decl.replace(oldclaim,
    '(folder \\texttt{arena agent 1/paper rewrites/latex}). The source version '
    'reports that it reproduces the four-parameter bounds, bands, ladder values, '
    'pairings, census counts, and deadline thresholds. The five-parameter '
    'classification added after that version requires a separate verification '
    'record; coverage by this older script is not claimed.',1)
needle='\\subsection*{AI declaration}'
assert decl.count(needle)==1
decl=decl.replace(needle,('\\subsection*{Author contributions}\n'
    'A.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.\n\n'+needle),1)
assert x.count('\\end{document}')==1
x=x.replace('\\end{document}',decl+'\n\n\\end{document}',1)
assert x.count('\\subsection*{Declarations}')==1
assert x.count('\\author{')==1
assert x.count('Chatterjee, K., Doyen, L., Henzinger, T.A., 2009.')==1
h.write_text(x)
print('restored',h.name,'new bytes',h.stat().st_size)

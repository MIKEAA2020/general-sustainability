#!/usr/bin/env python3
"""Source-anchored repair of paper06 v67's split-off back matter and 10 citations."""
import pathlib,re
D=pathlib.Path('/home/user/papers');src=(D/'paper06_assessment_separation_v65.tex').read_text()
p=D/'paper06_assessment_separation_v67.tex';x=p.read_text()
assert '\\section*{Declarations}' in src and '\\section*{Declarations}' not in x
assert '\\section*{Supplementary Material}' in src and '\\section*{Supplementary Material}' not in x
# Restore source-authored attribution in elsarticle frontmatter, as owner approved.
assert '\\author[aff]{' not in x
assert x.count('\\begin{frontmatter}')==1
x=x.replace('\\begin{frontmatter}',
    '\\begin{frontmatter}\n\\author[aff]{Amin Abaee}',1)
# Reattach full bibliography paragraphs rather than printing orphan publishers as
# freestanding entries. These 10 pairs were diffed against the retained v65 source.
keys=['Dasgupta, P., and M','Aubin, J.-P. (1991)','DFO. (2016)',
      'Filippov, A. F. (1988)','Keeney, R. L., and Raiffa',
      'Munda, G. (2005)','Nardo, M., Saisana','Roy, B. (1996)',
      'Warga, J. (1972)','World Bank. (2011)']
for key in keys:
    assert src.count(key)==1,('source key',key)
    assert x.count(key)==1,('target key',key)
    a=src.index(key);b=x.index(key)
    old=x[b:x.index('\n\n',b)]
    full=src[a:src.index('\n\n',a)]
    assert len(full)>len(old) and full.startswith(old), (key,repr(old),repr(full))
    x=x[:b]+full+x[b+len(old):]
# Source Supplementary Material and declarations are distinct sections and must
# survive when a standalone Part is split from a shared container reference list.
a=src.index('\\section*{Supplementary Material}')
z=src.rindex('\\end{document}')
back=src[a:z].strip()
assert back.count('\\section*{Supplementary Material}')==1
assert back.count('\\section*{Declarations}')==1
back=back.replace('accompanying Supplementary Material,',
  'accompanying file \\texttt{paper06\\_assessment\\_separation\\_v67\\_supplementary.md},',1)
# The author supplied the contribution text; do not copy older speculative roles.
old='A.A. conceptualized the entire work, wrote, edited and reviewed the manuscript.'
assert back.count(old)==1
back=back.replace(old,'A.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.',1)
assert x.count('\\end{document}')==1
x=x.replace('\\end{document}',back+'\n\n\\end{document}',1)
for k in ('\\section*{Supplementary Material}', '\\section*{Declarations}',
          'Net national product, wealth, and', 'Springer, New York, 953--986.'):
 assert x.count(k)>=1,k
p.write_text(x)
print('restored',p.name,p.stat().st_size)

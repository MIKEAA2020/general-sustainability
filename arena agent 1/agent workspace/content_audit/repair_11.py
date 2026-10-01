#!/usr/bin/env python3
"""Integrate Edwards declarations + source front matter into merged paper11 v64."""
import pathlib,re,sys
D=pathlib.Path('/home/user/papers');p=D/'paper11_forecasting_baselines_v64.tex'
source=(D/'paper11b_edwards_forecast_v2.tex').read_text();x=p.read_text()
sys.path.insert(0,'/home/user/p5');import mergelib
# Preserve the exact prior source author block, moved to the umbrella's front.
m=re.search(r'\\author\{',x);assert m
j=mergelib._match_brace(x,m.end()-1);author=x[m.start():j+1]
assert x.count('\\title{')==3 and x.count('\\author{')==2 and x.count('\\maketitle')==3
x=x.replace('\\maketitle',author+'\n\\maketitle',1)
# The two source front-matter sets are inside the two Parts; retain their
# original titles/dates as visible provenance and preserve their abstracts.
for i,anchor in enumerate(['\\part*{Part I ---','\\part*{Part II ---'],1):
    a=x.index(anchor);m=re.search(r'\\title\{',x[a:]);assert m
    t=a+m.start();tj=mergelib._match_brace(x,t+len('\\title'))
    title=x[t+len('\\title{'):tj]
    # extract date before author/title changes
    dm=re.search(r'\\date\{([^}]+)\}',x[t:t+1000]);assert dm
    date=dm.group(1)
    am=re.search(r'\\author\{',x[t:t+1000]);assert am
    aj=mergelib._match_brace(x,t+am.end()-1)
    mt=x.find('\\maketitle',aj);assert mt>aj and mt-aj<800
    replaced=x[t:mt+len('\\maketitle')]
    assert replaced.count('\\title{')==1 and replaced.count('\\author{')==1
    provenance='\\noindent\\textbf{Source study:} '+title+'. '+date+'.\n'
    x=x[:t]+provenance+x[mt+len('\\maketitle'):]
assert x.count('\\title{')==1 and x.count('\\author{')==1 and x.count('\\maketitle')==1
assert x.count('\\begin{abstract}')==3
# Read source B back matter; don't copy its duplicate funding/interests/AI
# sections into the merged article. Keep its unique data & verification detail.
a=source.index('\\subsection*{Data Availability Statement}')
b=source.index('\\subsection*{Funding}',a)
data=source[a:b].strip()
c=source.index('\\subsection*{Code availability}',b)
d=source.index('\\subsection*{AI declaration}',c)
code=source[c:d].strip()
data=data.replace('\\subsection*{Data Availability Statement}',
                  '\\paragraph{Edwards Aquifer data availability.}',1)
code=code.replace('\\subsection*{Code availability}',
                  '\\paragraph{Edwards Aquifer code availability.}',1)
code=code.replace('every cell\nof Tables~3, 4 and 7',
  'every cell of the corresponding Edwards-source tables '
  '(numbered 3, 4 and 7 in the standalone source)',1)
assert 'nClimDiv' in data and 'paperE3' in code
assert 'Edwards Aquifer data availability.' not in x
mark='\\subsection*{AI declaration}'
assert x.count(mark)==1
x=x.replace(mark,data+'\n\n'+code+'\n\n'+mark,1)
# CRediT: replace prior source's role list with the exact text the owner supplied
# for this present merged paper. Do not infer additional taxonomy roles.
cred='\\subsection*{CRediT authorship contribution statement}'
assert x.count(cred)==1
cstart=x.index(cred);cend=x.index('\\subsection*{Funding}',cstart)
old=x[cstart:cend]
assert 'Amin Abaee: Conceptualization' in old
x=x[:cstart]+cred+'\n\nA.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.\n\n'+x[cend:]
# A bibliography item added by a later prior-art pass ended up after the AI
# declaration, where reference scans cannot see it. Move, never discard.
ref='White, H., 2000. A reality check for data snooping. \\emph{Econometrica}, 68(5),\n1097--1126. doi:10.1111/1468-0262.00152.'
assert x.count(ref)==1
x=x.replace('\n'+ref+'\n','\n',1)
# Insert near its alphabetical neighbours, not at the top of References.
anchor='Zhu, Q., Zhu, Y., Niu, J., Huang, J., Huang, F., Zhou, X., Liu, D., and'
assert x.count(anchor)==1
x=x.replace(anchor,ref+'\n\n'+anchor,1)
assert len(re.findall(r'^\\end\{document\}',x,re.M))==1
p.write_text(x)
print('repaired',p.name,p.stat().st_size)

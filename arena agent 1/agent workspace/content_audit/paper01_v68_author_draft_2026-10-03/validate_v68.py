#!/usr/bin/env python3
"""Source-structure checks only; this is not TeX compilation or mathematical peer review."""
from pathlib import Path
from collections import Counter
import re,hashlib
ROOT=Path('/home/user/paper 2 family/01_obstruction')
for name in ['paper01_obstruction_calculus_v68.tex','paper01_obstruction_calculus_v68_supplementary.tex']:
    p=ROOT/name
    src=p.read_text()
    # Comments removed without swallowing an escaped percentage sign.
    text='\n'.join(re.split(r'(?<!\\)%',ln,maxsplit=1)[0] for ln in src.splitlines())
    escaped=re.compile(r'\\[{}]')
    braces=escaped.sub('',text)
    depth=0
    for i,c in enumerate(braces):
        if c=='{':depth+=1
        elif c=='}':
            depth-=1
            assert depth>=0,(name,'extra closing brace',braces.count('\n',0,i)+1)
    assert depth==0,(name,'unbalanced braces',depth)
    labels=re.findall(r'\\label\{([^}]+)\}',text)
    refs=re.findall(r'\\(?:eq)?ref\{([^}]+)\}',text)
    missing=sorted(set(refs)-set(labels)); duplicate=[k for k,v in Counter(labels).items() if v>1]
    assert not missing,(name,'unknown refs',missing)
    assert not duplicate,(name,'duplicate labels',duplicate)
    for env in ['theorem','proposition','remark','example','definition','corollary','figure','figure*','table','table*','equation','align','aligned','itemize']:
        assert len(re.findall(r'\\begin\{'+re.escape(env)+r'\}',text))==len(re.findall(r'\\end\{'+re.escape(env)+r'\}',text)),(name,env)
    figs=re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',text)
    for fig in figs:assert (ROOT/fig).exists(),(name,'missing image',fig)
    assert '\\begin{document}' in text and '\\end{document}' in text
    assert 'unrefereed' in text.lower() or 'not been independently reviewed' in text.lower()
    print(name,'SHA256',hashlib.sha256(p.read_bytes()).hexdigest(),'lines',len(src.splitlines()),'labels',len(labels),'refs',len(refs),'figures',len(figs),'STRUCTURE_OK')
print('DISCLAIMER: structure and file checks only; no TeX compiler or outside mathematical referee was used.')

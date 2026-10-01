#!/usr/bin/env python3
"""Source-level declaration census; no Lean build or axiom-footprint claim.
Counts declaration headers with attributes (e.g. @[simp] theorem), Unicode names,
and ignores nested Lean block comments and -- line comments.
"""
import re
from pathlib import Path
root=Path('/home/user')

def strip_comments(s):
 out=[];i=0;depth=0;line=False
 while i<len(s):
  if line:
   if s[i]=='\n': line=False;out.append('\n')
   else:out.append(' ')
   i+=1;continue
  if depth:
   if s.startswith('/-',i):depth+=1;out.extend('  ');i+=2
   elif s.startswith('-/',i):depth-=1;out.extend('  ');i+=2
   else:out.append('\n' if s[i]=='\n' else ' ');i+=1
   continue
  if s.startswith('--',i):line=True;out.extend('  ');i+=2
  elif s.startswith('/-',i):depth=1;out.extend('  ');i+=2
  else:out.append(s[i]);i+=1
 assert not depth
 return ''.join(out)
# Lean declaration attributes on the same line, plus optional visibility modifiers.
HEADER=re.compile(r'(?m)^\s*(?:@\[[^\]\n]+\]\s*)*(?:(?:private|protected|local|noncomputable)\s+)*(theorem|lemma)\s+([^\s(:{]+)')
def items(p):
 s=strip_comments(p.read_text())
 return [(s.count('\n',0,m.start(1))+1,m.group(1),m.group(2)) for m in HEADER.finditer(s)]
mini=root/'latest/lean/Minimax_Dual.lean'
rows=items(mini)
assert len(rows)==22
print('Minimax source',mini,'22 theorem/lemma declarations:')
print('Unicode-named',[(line,name) for line,_,name in rows if not name.isascii()])
print('ASCII-only name filter count:',sum(name.isascii() for _,_,name in rows))
base=root/'content_audit/scientific_validity/ebc'
ps=sorted(base.glob('*.lean'));assert len(ps)==16
flat=[]
for p in ps:
 entries=items(p);flat.extend((p.name,*row) for row in entries)
 plain=len(re.findall(r'(?m)^\s*(?:theorem|lemma)\s+',strip_comments(p.read_text())))
 print(f'{p.name:32s} all={len(entries):2d} no-attribute-prefix={plain:2d}')
assert len(flat)==138,len(flat)
attr=[(fn,line,name) for fn,line,_,name in flat if re.search(r'(?m)^\s*@\[[^\]\n]+\]\s*(?:theorem|lemma)\s+'+re.escape(name)+r'\b',strip_comments((base/fn).read_text()))]
print('EBC full declaration count:',len(flat),'historical line-start bare count:',len(flat)-len(attr))
print('Omitted attribute-prefixed theorem declarations:',attr)
assert len(attr)==4

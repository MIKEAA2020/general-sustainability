#!/usr/bin/env python3
from pathlib import Path
import re,sys,hashlib
R=Path('/home/user')
files=['paper02_probabilistic_sufficiency_v15.tex','paper03_computational_certification_v19.tex','paper03_computational_certification_v19_supplementary.tex','paper04_minimax_dual_certificates_v19.tex','paper05_exact_belief_computation_v19.tex','paper06_assessment_separation_v70.tex','paper09_cod_certification_v35.tex']
errors=[]
for name in files:
 p=R/'papers'/name;s=p.read_text()
 begins=re.findall(r'\\begin\{([^}]+)\}',s);ends=re.findall(r'\\end\{([^}]+)\}',s)
 labels=re.findall(r'\\label\{([^}]+)\}',s); refs=re.findall(r'\\(?:eqref|ref|pageref)\{([^}]+)\}',s)
 # two-stage stack in source order, preliminary because verbatim and comments are not parsed
 stack=[]
 for typ,env in re.findall(r'\\(begin|end)\{([^}]+)\}',s):
  if typ=='begin':stack.append(env)
  elif not stack or stack.pop()!=env:errors.append((name,'misnested environment',env));break
 if stack:errors.append((name,'unterminated environments',stack[-5:]))
 if len(labels)!=len(set(labels)):errors.append((name,'duplicate labels'))
 miss=sorted(set(refs)-set(labels));
 if miss:errors.append((name,'unresolved references',miss))
 print(name,'bytes',p.stat().st_size,'sha256',hashlib.sha256(p.read_bytes()).hexdigest(),'labels',len(labels),'refs',len(refs),'missing',len(miss),'envs',len(begins),'balanced',len(begins)==len(ends) and not stack)
print('RESULT',('PASS' if not errors else 'FAIL'), errors)
sys.exit(bool(errors))

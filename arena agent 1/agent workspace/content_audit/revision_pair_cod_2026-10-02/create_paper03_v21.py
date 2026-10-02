#!/usr/bin/env python3
"""Versioned typesetting repair for the pair proof; does not change its mathematics."""
from pathlib import Path
p=Path('/home/user/papers');src=p/'paper03_computational_certification_v20.tex';out=p/'paper03_computational_certification_v21.tex';si=p/'paper03_computational_certification_v21_supplementary.tex'
assert not out.exists() and not si.exists(), 'Do not overwrite an existing version'
s=src.read_text()
a='''\\[
\\Gamma_B(\\tau;s_*)
=-t\\int_0^\\tau(s_*-s)\\,ds
-\\int_\\tau^{s_*}(s_*-s)\\,ds-\\beta
=-\\frac7{50}+(1-t)\\tau-\\frac{t(1-t)}2\\tau^2.
\\]'''
b='''\\begin{align*}
\\Gamma_B(\\tau;s_*)
&=-t\\int_0^\\tau(s_*-s)\\,ds
  -\\int_\\tau^{s_*}(s_*-s)\\,ds-\\beta\\\\
&=-\\frac7{50}+(1-t)\\tau
  -\\frac{t(1-t)}2\\tau^2.
\\end{align*}'''
assert s.count(a)==1;s=s.replace(a,b)
a='\\texttt{paper03\\_computational\\_certification\\_v20\\_supplementary.tex}'
b='\\path{paper03_computational_certification_v21_supplementary.tex}'
assert s.count(a)==1;s=s.replace(a,b)
out.write_text(s)
si.write_bytes((p/'paper03_computational_certification_v20_supplementary.tex').read_bytes())
print('WROTE',out,si)

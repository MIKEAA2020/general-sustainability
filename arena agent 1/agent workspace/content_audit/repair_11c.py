"""Move the already-cited Saint-Pierre (1994) reference above Declarations.
One-shot source-specific displacement repair; do not rerun on corrected v2.
"""
from pathlib import Path
p=Path('/home/user/papers/paper11c_worked_systems_audit_v2.tex')
s=p.read_text()
entry='Saint-Pierre, P., 1994. Approximation of the viability kernel. \\emph{Applied Mathematics\n\\& Optimization}, 29, 187--209. doi:10.1007/bf01204182.'
assert s.count(entry)==1
assert s.index('\\subsection*{References}')<s.index('\\subsection*{Declarations}')<s.index('\\subsection*{AI declaration}')<s.index(entry)<s.rindex('\\end{document}')
s=s.replace('\n'+entry+'\n','\n',1)
s=s.replace('\\subsection*{Declarations}',entry+'\n\n\\subsection*{Declarations}',1)
assert s.index('Saint-Pierre, P., 1994.')<s.index('\\subsection*{Declarations}')
p.write_text(s)
print('paper11c: existing Saint-Pierre reference moved into References before Declarations')

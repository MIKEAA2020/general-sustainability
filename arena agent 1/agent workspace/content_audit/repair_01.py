"""One-shot source-anchored repair of paper01 v63. Never reparse damaged v62 refs.

v61 is the complete paper01 bibliography; paper02 v12 contributes nine distinct
works to the v62 shared bibliography. The overlapping Astrom, Smallwood,
Cardaliaguet, Doyen and Veliov works are represented by v61, not duplicated
merely because paper02 formats them differently. Do not rerun on repaired v63.
"""
from pathlib import Path
import re

root = Path('/home/user/papers')
head = root/'paper01_obstruction_calculus_v63.tex'
a = (root/'paper01_obstruction_calculus_v61.tex').read_text()
b = (root/'paper02_probabilistic_sufficiency_v12.tex').read_text()
s = head.read_text()
assert '\\author{' not in s and '\\subsection{References}' not in s
assert s.count('\\label{references}') == 1
# Entire author block from this paper's unmerged predecessor, not the other unit.
author = a[a.index('\\author{'):a.index('\\date{', a.index('\\author{'))].rstrip()
s = s.replace('\\begin{document}\n\\maketitle', author + '\n\\begin{document}\n\\maketitle', 1)
assert s.count('\\author{') == 1
# v61's references are paragraph-delimited. Keep each paragraph unaltered.
beg = a.index('\\subsection{References}\\label{references}')
end = a.index('\\section*{Declarations}', beg)
block = a[beg:end].strip()
assert block.startswith('\\subsection{References}\\label{references}')
assert block.endswith('}') and block.count('\\label{references}') == 1
# Cross-unit works that v62's shared reference section introduced are retained,
# excluding overlaps by title/work, NOT byte identity of differently styled entries.
p2 = b[b.index('{\\footnotesize', b.index('\\subsection*{References}'))+len('{\\footnotesize'):b.index('\\subsection*{Declarations}')]
p2 = p2.rsplit('}', 1)[0]
paras = [p.strip() for p in re.split(r'\n\s*\n', p2) if p.strip()]
extra = [p for p in paras if p.startswith(('Abaee, A., 2026.', 'Bertsekas, D.P.',
    'Alshiekh, M.', 'Chatterjee, K.', 'Nakao, H.', 'Papadimitriou, C.H.', 'Lovejoy, W.S.'))]
assert len(extra) == 9, [p[:90] for p in extra]
assert len(paras) == 11
# Keep source formatting of each entry; source-01 paragraph grouping is authoritative.
block = block[:-1].rstrip() + '\n\n' + '\n\n'.join(extra) + '\n}\n'
assert 'Nagumo, M.' in block and 'Japan 24, 551--559' in block
assert 'vol.~2993, pp.~477--492' in block
assert 'Operations Research 39, 162--175.' in block
start = s.index('\\label{references}')
end = s.index('\\section*{Declarations}', start)
s = s[:start] + block + '\n' + s[end:]
# The user explicitly approved this exact contribution statement.
assert s.count('\\section*{Declarations}') == 1 and 'Author contributions.' not in s
s = s.replace('\\end{document}', '\\textbf{Author contributions.} A.A. conceptualized the entire work, wrote, reviewed and edited the manuscript.\n\n\\end{document}', 1)
assert s.count('\\subsection{References}') == 1 and s.count('\\label{references}') == 1
assert s.count('\\end{document}') == 1
head.write_text(s)
print('repaired paper01 v63: original v61 paper bibliography + 9 distinct paper02 works; author and exact approved contribution')

#!/usr/bin/env python3
"""Restore readable S16 lead-in from the archived paper3 supplementary v18 Markdown.

The LaTeX conversion swallowed a whole prose sentence into an inline-code
span after the backtick/curly-quote boundary in “discharged by”. Touch only
the lead-in paragraph: retain heading, four-row table and all other content.
"""
from pathlib import Path
p=Path('/home/user/papers/paper10_depletion_ledgers_v53_supplementary.tex')
s=p.read_text()
md=Path('/home/user/content_audit/unvisited/md/paper3_supplementary_v18.md').read_text()
source=("For example, three of S7’s “discharged by” pointers name sections that no longer carry the statements they\n"
        "cite. None of the three is wrong in substance. The table below gives the labels to read against the main text\n"
        "as it stands. The `Typed` row is corrected in S15 instead of here.")
assert md.count(source)==1, 'markdown source witness changed'
start=s.index("\\section*{S16 - S7's discharge column")
lead=s.index('\n\nFor example, three of S7',start)+2
end=s.index('\n\n\\begin{longtable}',lead)
old=s[lead:end]
assert '\\texttt{discharged b\\allowbreak{}y' in old and '}Typed` row' in old
new=("For example, three of S7's ``discharged by'' pointers name sections that no longer carry the statements they\n"
     "cite. None of the three is wrong in substance. The table below gives the labels to read against the main text\n"
     "as it stands. The \\texttt{Typed} row is corrected in S15 instead of here.")
s=s[:lead]+new+s[end:]
assert s.count('\\begin{longtable}')==p.read_text().count('\\begin{longtable}')
assert s.count('\\end{longtable}')==p.read_text().count('\\end{longtable}')
p.write_text(s)
print('paper10 supplement S16 conversion-corrupted lead-in restored from v18 Markdown')

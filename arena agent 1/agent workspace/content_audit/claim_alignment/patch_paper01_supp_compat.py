#!/usr/bin/env python3
"""Supplement compatibility draft: restore existing sole author's byline; no proof edits."""
from pathlib import Path
from difflib import unified_diff
r=Path('/home/user');b=r/'content_audit/claim_alignment';src=r/'papers/paper01_obstruction_calculus_v63_supplementary.tex';old=src.read_text()
needle='\\title{Supplementary Material: Obstruction certificates under incomplete observation}\n\\maketitle'
assert old.count(needle)==1
s=old.replace(needle,'\\title{Supplementary Material: Obstruction certificates under incomplete observation}\n\\author{Amin Abaee}\n\\maketitle',1)
out=b/'drafts'/src.name;out.write_text(s)
(b/'diffs'/(src.stem+'.diff')).write_text(''.join(unified_diff(old.splitlines(True),s.splitlines(True),fromfile=str(src),tofile=str(out))))
print(out)

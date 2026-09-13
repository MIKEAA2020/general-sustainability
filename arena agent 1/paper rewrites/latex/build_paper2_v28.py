#!/usr/bin/env python3
# Build v28 from v27: fix the orphaned symbol in Section 2.2 and align the
# site-local note with the fix. No other change.
#   (a) Section 2.2 kernel reading defines G = RViab(V) but then writes
#       "points of V \ K"; change K -> G so the symbol matches its definition.
#   (b) The site-local note (Section 2.4) listed "Section 2.2 and Section 5(c)"
#       as places where K denotes the kernel; after (a), K no longer appears in
#       Section 2.2, so the note now cites Section 5(c) only.
import sys

SRC = "/home/user/arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v27.tex"
DST = "/home/user/arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v28.tex"

with open(SRC, encoding="utf-8") as f:
    t = f.read()

edits = []
old_a = "\\mathcal{V} \\setminus K\\) may admit controls that are instantaneously"
new_a = "\\mathcal{V} \\setminus G\\) may admit controls that are instantaneously"
edits.append(("a: stray K -> G (Section 2.2)", old_a, new_a))

old_b = "problems, while in Section 2.2 and Section 5(c) it denotes the kernel"
new_b = "problems, while in Section 5(c) it denotes the kernel"
edits.append(("b: site-local note clause", old_b, new_b))

out = t
for name, old, new in edits:
    n = out.count(old)
    if n != 1:
        print(f"ABORT: anchor '{name}' found {n} times (expected 1)")
        sys.exit(1)
    out = out.replace(old, new)
    print(f"applied {name}")

with open(DST, "w", encoding="utf-8") as f:
    f.write(out)
print(f"wrote {DST} ({len(out)} bytes)")

back = out
for name, old, new in reversed(edits):
    back = back.replace(new, old)
print("v28 reverse-reconstructs v27:", back == t)

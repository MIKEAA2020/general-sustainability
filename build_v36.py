#!/usr/bin/env python3
"""Build paper1_assessment_separation_v36.tex from v35:
point Figure 2 at the re-rendered image (single bottom x-axis label)."""
import sys

src = open('/home/user/paper1_assessment_separation_v35.tex', encoding='utf-8').read()
def rep(old, new, label, expect=1):
    global src
    n = src.count(old)
    if n != expect:
        print(f"FAIL [{label}]: found {n}, expected {expect}")
        sys.exit(1)
    src = src.replace(old, new)
    print(f"ok   [{label}]")

rep(r"fig2_weight_intervals_v31.png", r"fig2_weight_intervals_v35.png", "fig2-file")
rep(r"% Amin Abaee. Revision v35 (JEDC/elsarticle; margin-set notation D->mathD, table label, longtable->tabular so the policy table is Table 1). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Revision v36 (JEDC/elsarticle; Figure 2 re-rendered with a single x-axis label). Compiles with tectonic, pdflatex, or xelatex.",
    "header-rev")

out = '/home/user/paper1_assessment_separation_v36.tex'
open(out, 'w', encoding='utf-8').write(src)
print(f"\nWROTE {out} ({len(src)} bytes)")

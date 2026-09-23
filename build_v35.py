#!/usr/bin/env python3
"""Build paper1_assessment_separation_v35.tex from v34:
disambiguate the finite-menu margin set (D -> mathcal D) from the disturbance set D,
tidy the policy-instruments table, and add a proper table label/reference."""
import sys

src = open('/home/user/paper1_assessment_separation_v34.tex', encoding='utf-8').read()
def rep(old, new, label, expect=1):
    global src
    n = src.count(old)
    if n != expect:
        print(f"FAIL [{label}]: found {n}, expected {expect}")
        sys.exit(1)
    src = src.replace(old, new)
    print(f"ok   [{label}]")

# 1. finite-menu theorem: margin set D -> mathcal{D} (statement)
rep(r"Write \(D = \{d_a : a \in \mathcal{A}\}\).",
    r"Write \(\mathcal{D} = \{d_a : a \in \mathcal{A}\}\).",
    "margin-set-def")

# 2. policy table: replace the bare-D row wording
rep(r"Menu convexification & replace \(D\) by \(\operatorname{conv}(D)\) (the blend family) & closes the gap exactly on the scalarized feasible region \\",
    r"Menu convexification & replace \(\mathcal{D}\) by \(\operatorname{conv}(\mathcal{D})\) (the blend family) & closes the gap exactly on the scalarized feasible region \\",
    "table-conv")

# 3. remaining conv(D) -> conv(mathcal D)  (body x3 + Appendix A proof x3)
rep(r"\operatorname{conv}(D)", r"\operatorname{conv}(\mathcal{D})",
    "conv-D-global", expect=7)

# 4. avoid nonce term "full-cone gap" in the table
rep(r"Reweighting & change the weight \(w\) & does not close the full-cone gap \\",
    r"Reweighting & change the weight \(w\) & does not close the gap \\",
    "table-reweighting")

# 5. add label to the table and make the text reference robust
rep(r"\caption{Policy instruments acting on the acceptance gap.}",
    r"\caption{Policy instruments acting on the acceptance gap.}" + "\n" + r"\label{tab:instruments}",
    "table-label")
rep(r"different ways; Table 1 records them.",
    r"different ways; Table~\ref{tab:instruments} records them.",
    "table-ref")

# 6. longtable -> tabular: longtable silently advances the table counter even
# without a caption, which made the policy table render as "Table 3" with no
# visible Table 1/2. The two small inline tables do not page-break; tabular is
# the correct environment and restores "Table 1".
rep(r"\begin{longtable}[]{@{}", r"\noindent\begin{tabular}{@{}",
    "lt-tabular-open", expect=2)
rep(r"\midrule\noalign{}" + "\n" + r"\endhead" + "\n" + r"\bottomrule\noalign{}" + "\n" + r"\endlastfoot" + "\n",
    r"\midrule\noalign{}" + "\n",
    "lt-headfoot-strip", expect=2)
rep(r"\end{longtable}", r"\bottomrule\noalign{}" + "\n" + r"\end{tabular}",
    "lt-tabular-close", expect=2)

# 7. header rev
rep(r"% Amin Abaee. Revision v34 (JEDC/elsarticle; flow, humanization, displacement). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Revision v35 (JEDC/elsarticle; margin-set notation D->mathD, table label, longtable->tabular so the policy table is Table 1). Compiles with tectonic, pdflatex, or xelatex.",
    "header-rev")

out = '/home/user/paper1_assessment_separation_v35.tex'
open(out, 'w', encoding='utf-8').write(src)
print(f"\nWROTE {out} ({len(src)} bytes)")

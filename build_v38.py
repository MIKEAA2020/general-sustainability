#!/usr/bin/env python3
"""Build paper1_assessment_separation_v38.tex from v37:
(a) point Figure 1 at the re-rendered image (Qwen's four devices),
(b) add the region-dictionary table (Qwen part 1.6) after the witness Example."""
import sys

src = open('/home/user/paper1_assessment_separation_v37.tex', encoding='utf-8').read()
def rep(old, new, label, expect=1):
    global src
    n = src.count(old)
    if n != expect:
        print(f"FAIL [{label}]: found {n}, expected {expect}")
        sys.exit(1)
    src = src.replace(old, new)
    print(f"ok   [{label}]")

# (a) figure file
rep(r"\includegraphics[width=\linewidth]{figs_p1/fig1_witness_v26.png}",
    r"\includegraphics[width=\linewidth]{figs_p1/fig1_witness_v38.png}",
    "fig1-file")

# (a) figure caption
caption_old = (r"\caption{The discrepancy region \(\mathcal{Q}\) in the floor plane: the closed upper-right triangle above \(s_1 + s_2 = 2\), minus the legs \(s_1 = 2\) and \(s_2 = 2\) (boundary conventions as in Section 4.6). \textbf{Panel A (\(x < 1\), shown at \(x = 0\)):} \(\mathcal{Q}\) is the impossibility region \(I = \mathrm{FP}_{\mathrm{agg}}\), with the interior witness \((s_1, s_2) = (6/5, 6/5)\) marked. \textbf{Panel B (\(x \ge 1\), shown at \(x = 1\)):} the same region is the rescue set \(R\), served by STAGED. The threshold curves \(\rho_1, \rho_2\) bound the FAST-only / both / SLOW-only endorsement zones; the point \((x, s_1, s_2) = (\tfrac12, \tfrac1{10}, \tfrac1{10})\), outside the \(s\)-plane section, is annotated in Panel A.}")
caption_new = (r"\caption{The discrepancy triangle \(\mathcal{Q} = \{ s_1 < 2,\; s_2 < 2,\; s_1 + s_2 \ge 2 \}\) in the floor plane (boundary conventions as in Section 4.6). \textbf{Panel A (\(x < 1\)):} \(\mathcal{Q}\) is the impossibility region \(I = \mathrm{FP}_{\mathrm{agg}}\) --- every weighting licenses a plan, no plan satisfies the floors --- and the worst-case dip arrows show FAST (\(s_1 \to s_1 - 2\)) and SLOW (\(s_2 \to s_2 - 2\)) crossing the zero floors from the witness point \((6/5, 6/5)\). \textbf{Panel B (\(x \ge 1\)):} the same triangle is the rescue set \(R\), served by STAGED. Below the diagonal \(s_1 + s_2 = 2\), both assessments reject when \(x < 1\) and both accept when \(x \ge 1\). The reserve bars show the bridge stock \(x\) against the rescue cost \(c = 1\) (Panel A: \(x = 0\); Panel B: \(x = 1\)). The bottom strip records the endorsement zones at the witness point: SLOW-only for \(r < \rho_1 = \tfrac23\), both for \(\rho_1 \le r \le \rho_2 = \tfrac32\), FAST-only for \(r > \rho_2\).}")
rep(caption_old, caption_new, "fig1-caption")

# (b) region-dictionary table after the witness Example
table_tex = (r"\begin{table}[htbp]" + "\n"
    r"\centering" + "\n"
    r"\small" + "\n"
    r"\begin{tabular}{@{}p{0.30\linewidth}p{0.22\linewidth}p{0.22\linewidth}p{0.18\linewidth}@{}}" + "\n"
    r"\toprule" + "\n"
    r"Region (witness datum) & Aggregate (per-weight) verdict & Common-plan (typed) verdict & Why \\" + "\n"
    r"\midrule" + "\n"
    r"$x \ge 1$, all $s$ & accept & accept & STAGED serves every weight \\" + "\n"
    r"$s_1 \ge 2$ or $s_2 \ge 2$ & accept & accept & FAST/SLOW survives its own dip \\" + "\n"
    r"$I$: $x < 1$, $s_1 < 2$, $s_2 < 2$, $s_1 + s_2 \ge 2$ & accept (weight-dependent plans) & reject & dips breach floors; reserve cannot finance phasing \\" + "\n"
    r"$R$: $x \ge 1$, $s_1 < 2$, $s_2 < 2$, $s_1 + s_2 \ge 2$ & accept & accept & reserve finances STAGED \\" + "\n"
    r"$s_1 + s_2 < 2$, $x < 1$ & reject & reject & even the index fails; both doctrines agree \\" + "\n"
    r"\bottomrule" + "\n"
    r"\end{tabular}" + "\n"
    r"\caption{Region dictionary on the witness datum (Theorem 5): the per-weight aggregate verdict and the common-plan (typed) verdict on each salient region of \(X_0\).}" + "\n"
    r"\label{tab:regions}" + "\n"
    r"\end{table}")
rep(r"typed-accepted, as \(R\) promises." + "\n\n" + r"\subsection{Figures}\label{figures}",
    r"typed-accepted, as \(R\) promises." + "\n\n"
    r"Table~\ref{tab:regions} records the two verdicts region by region." + "\n\n"
    + table_tex + "\n\n"
    + r"\subsection{Figures}\label{figures}",
    "region-dict-table")

# header rev
rep(r"% Amin Abaee. Revision v37 (JEDC/elsarticle; removed self-referential meta-commentary). Compiles with tectonic, pdflatex, or xelatex.",
    r"% Amin Abaee. Revision v38 (JEDC/elsarticle; Figure 1 upgraded (Qwen four devices); region-dictionary table added). Compiles with tectonic, pdflatex, or xelatex.",
    "header-rev")

out = '/home/user/paper1_assessment_separation_v38.tex'
open(out, 'w', encoding='utf-8').write(src)
print(f"\nWROTE {out} ({len(src)} bytes)")

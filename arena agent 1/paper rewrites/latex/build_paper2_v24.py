#!/usr/bin/env python3
"""Build paper2 v24 from v23.

v24 adds (all passing the non-decorative bar):
  - a selector-principle Proposition in Section 2.4 (formalizes the
    paper's own organizing claim; forward direction + honest converse
    scope);
  - Figure 5: the obstruction ladder (consolidates Prop 3.5's display,
    the rung bullets, and the "exit below the ladder" remark);
  - Figure 6: the one-step obstruction tree (Section 3.5's named object,
    previously text-only);
and re-points the three places that name the selector principle to the
new Proposition.  No theorem/proof/equation/definition content changes.
"""
import re, sys

SRC = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v23.tex"
DST = "arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v24.tex"

with open(SRC, encoding="utf-8") as f:
    s = f.read()

def sub_once(old, new, tag):
    global s
    assert s.count(old) == 1, f"{tag}: expected 1 occurrence, found {s.count(old)}"
    s = s.replace(old, new)

# ---- 1. selector principle proposition, end of Section 2.4 -------------
sub_once(
    "the\nobstructions are nested (Proposition~\\ref{prop:ladder}).",
    "the\nobstructions are nested (Proposition~\\ref{prop:ladder}). The organizing\nclaim of the calculus is the following, stated once and used implicitly\nby every certificate of Sections 3 and 4.\n\n\\begin{proposition}[selector principle]\\label{prop:selector}\nIf \\(B\\in\\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V})\\) and \\(\\pi\\) is a\npolicy witnessing viability on \\(B\\), then at every review time the\naction \\(a=\\pi(B)\\) selected by \\(\\pi\\) is a response that is\n(i) \\emph{admissible}, \\(a\\in U^B(B)\\); (ii) \\emph{safe}, keeping every\ncompatible trajectory in \\(\\mathcal{V}\\) until the next observation ---\n\\(\\mathrm{Reach}_{[0,\\Delta]}(B,a)\\subseteq\\mathcal{V}\\) at review\nlength \\(\\Delta\\); and (iii) \\emph{recursively viable}, in that every\npost-observation belief reached at the next review is again in\n\\(\\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V})\\) under the continuation\nof \\(\\pi\\). A belief is therefore viable only if each of the response\ncorrespondences of this section --- \\(U^B(B)\\),\n\\(\\mathcal{R}_{\\mathcal{V}}^B(B)\\), \\(\\mathcal{A}_{\\mathrm{tube}}(B,\\Delta)\\),\nand the recursive predecessor of Section 3.5 --- is nonempty along\nevery reachable branch; hence a certificate that any one of them is\nempty at a reachable belief certifies nonviability. In finite systems\nthe converse is exact (Theorem~\\ref{thm:finite-horizon}); in continuous\ntime the converse is the backward-recursion completion noted in\nSection 6.5.\n\\end{proposition}",
    "selector proposition",
)

# ---- 2. Contributions: cite the proposition ----------------------------
sub_once(
    "The calculus is organized by a single selector principle (Section 2.4):",
    "The calculus is organized by a single selector principle (Proposition~\\ref{prop:selector}, Section 2.4):",
    "contributions cite",
)

# ---- 3. Organization paragraph -----------------------------------------
sub_once(
    "information states, and the\nsafe-control correspondence.",
    "information states, the safe-control\ncorrespondence, and the selector principle (Proposition~\\ref{prop:selector}).",
    "organization paragraph",
)

# ---- 4. Conclusion: cite the proposition --------------------------------
sub_once(
    "organized by one selector principle --- observation-based viability",
    "organized by one selector principle (Proposition~\\ref{prop:selector}) --- observation-based viability",
    "conclusion cite",
)

# ---- 5. Figure: obstruction ladder (after Prop 3.5 discussion) ---------
sub_once(
    "strongest form of obstruction and needs no observation-theoretic\nargument.\n\n\\begin{example}[hidden-mode conflict]\\label{ex:hidden-mode}",
    "strongest form of obstruction and needs no observation-theoretic\nargument. Figure~\\ref{fig:ladder} collects the ladder and the position\nof the exit certificate below it.\n\n\\begin{figure}[htbp]\n\\centering\n\\includegraphics[width=0.92\\linewidth]{figs_p2/fig_p2_ladder.png}\n\\caption{The obstruction ladder. The common response sets are nested,\n\\(U^B(B)\\supseteq\\mathcal{R}_{\\mathcal{V}}^B(B)\\supseteq\\mathcal{A}_{\\mathrm{tube}}(B,\\Delta)\\supseteq\\mathcal{A}_N(B)\\),\nand emptiness descends (Proposition~\\ref{prop:ladder}); the finite-time\nexit certificate sits below the ladder, defeating every control under\nfull information (Theorem~\\ref{thm:exit}).}\n\\label{fig:ladder}\n\\end{figure}\n\n\\begin{example}[hidden-mode conflict]\\label{ex:hidden-mode}",
    "ladder figure",
)

# ---- 6. Figure: one-step obstruction tree (Section 3.5) ----------------
sub_once(
    "Theorem~\\ref{thm:common-action} in the finite-horizon language.\n\n\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}",
    "Theorem~\\ref{thm:common-action} in the finite-horizon language; Figure~\\ref{fig:obstruction-tree}\ndraws the tree.\n\n\\begin{figure}[htbp]\n\\centering\n\\includegraphics[width=0.66\\linewidth]{figs_p2/fig_p2_obstruction_tree.png}\n\\caption{The one-step obstruction tree of Example~\\ref{ex:hidden-mode},\nread as a finite system: for each admissible action the adversary has a\ncompatible branch terminating in violation, so \\(B_0\\notin\\mathcal{W}_1\\)\n(Theorem~\\ref{thm:finite-horizon}).}\n\\label{fig:obstruction-tree}\n\\end{figure}\n\n\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}",
    "tree figure",
)

with open(DST, "w", encoding="utf-8") as f:
    f.write(s)

print("wrote", DST, len(s), "bytes")

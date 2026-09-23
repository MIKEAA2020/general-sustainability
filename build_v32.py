#!/usr/bin/env python3
"""Build paper1_assessment_separation_v32.tex (JEDC/elsarticle + proofs-to-appendix)
from v31. Deterministic; every anchor asserted."""
import re, sys

src = open('/home/user/paper1_assessment_separation_v31.tex', encoding='utf-8').read()
asserts = []
def rep(old, new, label, count=1):
    n = src.count(old)
    if n != count:
        print(f"FAIL [{label}]: found {n}, expected {count}")
        sys.exit(1)
    return src.replace(old, new)

# ---------------------------------------------------------------- preamble
src = rep(r"\documentclass[11pt]{article}",
          r"\documentclass[review,11pt]{elsarticle}", "documentclass")
src = rep(r"\usepackage[a4paper,margin=1in]{geometry}" + "\n", "", "geometry")
src = rep(r"\usepackage[mathlines]{lineno}" + "\n", "", "lineno-pkg")
src = rep(r"\linenumbers" + "\n", "", "linenumbers")
src = rep(r"\setcounter{secnumdepth}{-1}" + "\n", "", "secnumdepth")
src = rep(r"\usepackage[font=small,labelfont=bf]{caption}" + "\n", "", "caption-pkg")

# add \jel command to preamble (after hyperref)
src = rep(r"\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}",
          r"\usepackage[colorlinks=true,allcolors=blue!45!black]{hyperref}" + "\n"
          + r"\providecommand{\jel}[1]{\par\noindent\textbf{JEL classification:} #1\par}",
          "jel-cmd")

# header comment
src = rep(r"% The Limits of Compensatory Aggregation: A Formal Separation of Weak and Strong Sustainability Assessment",
          r"% Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility",
          "header-comment")
src = rep(r"% Amin Abaee. Revision v31 (review build with line numbers; retargeted for JEDC). Compiles with tectonic, pdflatex, or xelatex.",
          r"% Amin Abaee. Revision v32 (JEDC/elsarticle; proofs in appendix). Compiles with tectonic, pdflatex, or xelatex.",
          "header-rev")

# ---------------------------------------------------------------- frontmatter
# title: unchanged text, but move into frontmatter
# title: single line in v31; keep text, used inside frontmatter below
title_line = r"\title{Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility}"

author_old = (r"\title{Aggregate Indices and Transition Safety: A Quantifier-Order Separation Between Scalarized and Coordinate-Wise Feasibility}" + "\n"
              r"\author{Amin Abaee\\[0.35em]" + "\n"
              r"{\small Independent Researcher}\\[0.55em]" + "\n"
              r"{\small\href{https://orcid.org/0000-0002-0019-1842}{ORCID: 0000-0002-0019-1842}}\\[0.3em]" + "\n"
              r"{\small\href{mailto:amin\_abaee@ut.ac.ir}{amin\_abaee@ut.ac.ir}}}" + "\n"
              r"\date{September 11, 2026}" + "\n"
              r"\maketitle")
author_new = (r"\begin{frontmatter}" + "\n\n"
              + title_line + "\n\n"
              + r"\author[aff]{Amin Abaee}" + "\n\n"
              + r"\address[aff]{Independent Researcher, \href{https://orcid.org/0000-0002-0019-1842}{ORCID: 0000-0002-0019-1842}, \href{mailto:amin\_abaee@ut.ac.ir}{amin\_abaee@ut.ac.ir}}")
src = rep(author_old, author_new, "author-address")

# keywords / JEL / highlights -> elsarticle environments
kw_old = (r"\textbf{Keywords:} sustainability; viability theory; robust control;" + "\n"
          r"scalarization; multi-criteria decision analysis; quantifier order;" + "\n"
          r"transition safety." + "\n\n"
          r"\textbf{JEL codes:} C61; C62; D81; Q01; Q56." + "\n\n"
          r"\subsection*{Highlights}" + "\n\n"
          r"\begin{itemize}" + "\n"
          r"\tightlist" + "\n"
          r"\item" + "\n"
          r"  Scalarized and coordinate-wise sustainability criteria are compared as robust transition-safety problems on a common datum." + "\n"
          r"\item" + "\n"
          r"  Aggregate certification can fail path-wise floors on a region with nonempty interior." + "\n"
          r"\item" + "\n"
          r"  The gap is identified with the failure of quantifier interchange over plans and weights, and characterized geometrically for any finite plan menu." + "\n"
          r"\item" + "\n"
          r"  Exact per-weight licensing thresholds and a closed-form reserve threshold are derived." + "\n"
          r"\item" + "\n"
          r"  Convexifying the plan menu closes the gap exactly; discrete time-sharing does not." + "\n"
          r"\end{itemize}")
kw_new = (r"\begin{keyword}" + "\n"
          r"sustainability \sep viability theory \sep robust control \sep scalarization \sep multi-criteria decision analysis \sep quantifier order \sep transition safety" + "\n"
          r"\end{keyword}" + "\n\n"
          r"\jel{C61; C62; D81; Q01; Q56}" + "\n\n"
          r"\begin{highlights}" + "\n"
          r"\item Scalarized and coordinate-wise sustainability criteria are compared as robust transition-safety problems on a common datum." + "\n"
          r"\item Aggregate certification can fail path-wise floors on a region with nonempty interior." + "\n"
          r"\item The gap is identified with the failure of quantifier interchange over plans and weights, and characterized geometrically for any finite plan menu." + "\n"
          r"\item Exact per-weight licensing thresholds and a closed-form reserve threshold are derived." + "\n"
          r"\item Convexifying the plan menu closes the gap exactly; discrete time-sharing does not." + "\n"
          r"\end{highlights}" + "\n\n"
          r"\end{frontmatter}")
src = rep(kw_old, kw_new, "keywords-highlights")

# remove the horizontal rule that followed the highlights block (now redundant)
src = rep(r"\end{frontmatter}" + "\n\n" + r"\begin{center}\rule{0.5\linewidth}{0.5pt}\end{center}" + "\n\n" + r"\subsection{1. Introduction}",
          r"\end{frontmatter}" + "\n\n" + r"\section{Introduction}", "drop-rule-before-intro")

# ---------------------------------------------------------------- section renumber
def renumber_subsection(m):
    t = re.sub(r'^\s*\d+\.\s*', '', m.group(1), count=1)
    return '\\section{' + t + '}'
def renumber_subsubsection(m):
    t = re.sub(r'^\s*\d+(?:\.\d+)*\s*', '', m.group(1), count=1)
    return '\\subsection{' + t + '}'

src = re.sub(r'\\subsection\{([^{}]*)\}', renumber_subsection, src, flags=re.S)
src = re.sub(r'\\subsubsection\{([^{}]*)\}', renumber_subsubsection, src, flags=re.S)

# special-case unnumbered sections
src = rep(r"\section{References}\label{references}",
          r"\section*{References}\label{references}", "references-star")
src = rep(r"\section{Supplementary Material}\label{supplementary-material}",
          r"\section*{Supplementary Material}\label{supplementary-material}", "supp-star")

# ---------------------------------------------------------------- content edits
src = rep(r"\textbf{Common-plan acceptance (noncompensatory).}",
          r"\textbf{Common-plan acceptance (noncompensatory, coordinate-wise).}", "gloss-common")
src = rep(r"\textbf{Per-weight acceptance (compensatory).}",
          r"\textbf{Per-weight acceptance (compensatory, scalarized).}", "gloss-perweight")

# conclusion: foreground the general mechanism + finite-menu theorem
concl_old = (r"The weak-sustainability and strong-sustainability traditions are usually"
             "\n" + r"compared as doctrines --- as different normative stances on"
             "\n" + r"substitutability. This paper shows that the divergence of the two"
             "\n" + r"doctrines as formalized here --- the scalarized-aggregate and typed")
concl_new = (r"Scalarized and coordinate-wise feasibility criteria are usually compared"
             "\n" + r"as doctrines --- as different normative stances on substitutability, of"
             "\n" + r"which the weak- and strong-sustainability traditions are the canonical"
             "\n" + r"instances. This paper shows that the divergence between the two criteria"
             "\n" + r"as formalized here --- the scalarized-aggregate and typed")
src = rep(concl_old, concl_new, "conclusion-open")

concl_tail_old = (r"policy dependence of the aggregate-feasible transition." + "\n\n"
                  r"For the construction of composite sustainability indices, the theorem")
concl_tail_new = (r"policy dependence of the aggregate-feasible transition. The"
                  "\n" + r"finite-menu theorem of Section 4.4 states the underlying mechanism in"
                  "\n" + r"full generality: for any finite menu, the acceptance gap is the part of"
                  "\n" + r"the convex hull of the required margins that no single plan dominates,"
                  "\n" + r"so the witness of Section 4.5 is an instance of a geometric fact rather"
                  "\n" + r"than an isolated construction." + "\n\n"
                  r"For the construction of composite sustainability indices, the theorem")
src = rep(concl_tail_old, concl_tail_new, "conclusion-finite-menu")

# limitations: margin-class scope + blended-action availability
lim_old = (r"\item" + "\n"
           r"  The operators cover finite horizons with exact tubes and specified disturbance sets; infinite horizons, partial observation, stochastic chance constraints, and endogenous event times are not treated.")
lim_new = (r"\item" + "\n"
           r"  The operators cover finite horizons with exact tubes and specified disturbance sets; infinite horizons, partial observation, stochastic chance constraints, and endogenous event times are not treated." + "\n"
           r"\item" + "\n"
           r"  The finite-menu theorem of Section 4.4 governs plans whose admissibility is characterized by a required-margin vector; plans outside that class (reserve-financed plans, destination-failing plans) are handled separately, and the geometric form of the gap is established within the margin class." + "\n"
           r"\item" + "\n"
           r"  If a convexified (blended) plan is physically and institutionally available, the gap disappears by Theorem 8; the separation is therefore a statement about certification relative to the available plan menu, not a claim that the gap is unavoidable in every institution.")
src = rep(lim_old, lim_new, "limitations-add")

# ---------------------------------------------------------------- proof extraction
blocks = [
    # (id, start_anchor, sentinel, label, appendix)
    ("P1", r"\emph{Proof.} If \(a \in \bigcap_\lambda E_\lambda(z)\), then each",
           r"The separation in Section 4.5 is a strict instance of this inclusion",
           r"Proof of Remark 1 (Section 4.1).", "A"),
    ("P2", r"\emph{Proof.} (\(\Rightarrow\)) \(w \ge 0\),",
           r"At a \emph{fixed} trajectory the full-cone aggregate",
           r"Proof of Remark 2 (Section 4.2).", "A"),
    ("P3", r"\emph{Proof.} (i) Let \(a \in E_{\mathrm{typ}}(z)\).",
           r"Part (i) is standard constraint-set monotonicity under nested safe sets",
           r"Proof of Proposition 3 (Section 4.3).", "A"),
    ("P4", r"\emph{Proof.} For the second inclusion:",
           r"Proposition 4 makes precise the claim",
           r"Proof of Proposition 4 (Section 4.4).", "A"),
    ("P5", r"\emph{Proof.} (i) is the margin test restated.",
           r"On the witness datum of Section 4.5 the margin class is",
           r"Proof of the finite-menu theorem (Section 4.4).", "A"),
    ("P6", r"\emph{Proof.} \textbf{(1)} Typed admissibility requires",
           r"\emph{Boundary conventions.}",
           r"Proof of Theorem 5 (Section 4.6).", "B"),
    ("P7", r"\emph{Proof.} (i) Backward induction on stages.",
           r"\textbf{Theorem 7 (erasure witness).}",
           r"Proof of Remark 6 (Section 4.8).", "B"),
    ("P8", r"\emph{Datum.} Two capital forms, floors at zero",
           r"The witness datum of Section 4.5 is not subject to this erasure.",
           r"Proof of Theorem 7 (Section 4.8).", "B"),
    ("P9", r"\emph{Proof.} (i) FAST's worst-case tube has",
           r"\emph{Remark.} The collapse is exact and weight-independent",
           r"Proof of Theorem 8 (Section 4.10).", "B"),
    ("P10", r"\emph{Proof.} A sequential policy that spends any positive time",
           r"\emph{Remark.} Together Proposition 9 and Theorem 8 delimit",
           r"Proof of Proposition 9 (Section 4.11).", "B"),
    ("P11", r"\emph{Proof.} Among the augmented menu, only",
           r"On the impossibility region \(I\), \(\kappa^*(z) = 1 - x > 0\)",
           r"Proof of the rescue threshold (Section 5.5).", "C"),
]

appendix = {"A": [], "B": [], "C": []}
for pid, start, sentinel, label, grp in blocks:
    i = src.find(start)
    assert i != -1, f"{pid}: start anchor not found"
    j = src.find(sentinel, i)
    assert j != -1, f"{pid}: sentinel not found"
    chunk = src[i:j].rstrip()
    # strip leading "Proof." / "textbf{Proof.}" opener
    body = chunk
    if body.startswith(r"\emph{Proof.} "):
        body = body[len(r"\emph{Proof.} "):]
    elif body.startswith(r"\textbf{Proof.} "):
        body = body[len(r"\textbf{Proof.} "):]
    entry = r"\textbf{" + label + r"}\ " + body + "\n\n"
    appendix[grp].append(entry)
    # inline pointer
    pointer = r"\emph{Proof.} See Appendix " + grp + "."
    src = src[:i] + pointer + src[j:]
    print(f"ok   extracted {pid} -> Appendix {grp}")

# ---------------------------------------------------------------- appendix insertion
app_text = "\n\\appendix\n\n"
secA = "Proofs of the general results"
secB = "Proofs for the benchmark economy"
secC = "Proof of the rescue threshold"
app_text += "\\section{" + secA + "}\n\n" + "".join(appendix["A"])
app_text += "\\section{" + secB + "}\n\n" + "".join(appendix["B"])
app_text += "\\section{" + secC + "}\n\n" + "".join(appendix["C"])

anchor = r"\section*{References}\label{references}"
i = src.find(anchor)
assert i != -1, "references anchor not found"
src = src[:i] + app_text + "\n" + src[i:]

out = '/home/user/paper1_assessment_separation_v32.tex'
open(out, 'w', encoding='utf-8').write(src)
print(f"\nWROTE {out} ({len(src)} bytes)")

# quick sanity
for probe in [r"\documentclass[review,11pt]{elsarticle}", r"\begin{frontmatter}",
              r"\end{frontmatter}", r"\begin{keyword}", r"\begin{highlights}",
              r"\appendix", r"\section{Proofs of the general results}",
              r"\section{Proofs for the benchmark economy}", r"\section{Proof of the rescue threshold}"]:
    print(("OK  " if probe in src else "MISS"), probe)
print("remaining inline Proof. count:", src.count(r"\emph{Proof.} See Appendix") + src.count(r"\textbf{Proof.} See Appendix"))
print("remaining raw \\emph{Proof.}:", src.count(r"\emph{Proof.}"))
print("remaining raw \\textbf{Proof.}:", src.count(r"\textbf{Proof.}"))

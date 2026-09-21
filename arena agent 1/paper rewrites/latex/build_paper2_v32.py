#!/usr/bin/env python3
# Build the Automatica-format condensed version (v29) of paper 2 plus its
# supplementary, from v28. Two files are produced:
#   - paper2_obstruction_calculus_v29_Automatica_condensed.tex  (main, 2-col)
#   - paper2_obstruction_calculus_v29_supplementary.tex         (full proofs etc.)
#
# Condensation decisions (per user instructions):
#   * two-column, 10pt, A4, 16mm margins (nominally ~12 pages);
#   * full proofs replaced by one-paragraph proof sketches in the main text;
#   * literature review condensed (Section 1.1 lit paragraph, 1.3, and 5);
#   * three figures moved to the supplementary (ladder, obstruction tree, CE trap);
#   * Appendix A (bounded constructions) moved to the supplementary;
#   * Section 6.2 / 6.3 tightened.
# All theorem/proposition/... statements are copied verbatim from v28.

import re, sys

LATEX = "/home/user/arena agent 1/paper rewrites/latex"
SRC = f"{LATEX}/paper2_obstruction_calculus_v28.tex"
MAIN = f"{LATEX}/paper2_obstruction_calculus_v32_Automatica_routes.tex"
SUPP = f"{LATEX}/paper2_obstruction_calculus_v32_Automatica_routes_supplementary.tex"

t = open(SRC, encoding="utf-8").read()
from revisions_v31 import apply_revisions
t = apply_revisions(t)
from revisions_v32 import apply_revisions_v32
t = apply_revisions_v32(t)

# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def span_replace(text, start_sub, end_sub, new, must=True):
    i = text.index(start_sub)
    j = text.index(end_sub, i) + len(end_sub)
    return text[:i] + new + text[j:]

def extract_span(text, start_sub, end_sub):
    i = text.index(start_sub)
    j = text.index(end_sub, i)
    return text[i:j]

# ----------------------------------------------------------------------------
# Proof sketches (in document order of the 10 \emph{Proof} blocks)
# ----------------------------------------------------------------------------
SKETCHES = [
    # thm:exit
    ("\\emph{Proof sketch.} Fix an admissible control. By (1), the adverse-selection "
     "correspondence \\(D_\\varepsilon(x,u)\\) has nonempty values on the strip; its closed graph and "
     "compact values (Section 2.1) yield a measurable selection \\(d(\\cdot)\\), realized in closed loop "
     "by (H1.2). The fundamental theorem of calculus integrates (1) along the resulting trajectory to "
     "\\(q(x(t)) \\le q(x_0) - \\varepsilon t\\), so \\(q\\) attains the strict violation \\(q < 0\\) by "
     "time \\(q(x_0)/\\varepsilon \\le a/\\varepsilon\\)."),
    # prop:emptiness
    ("\\emph{Proof sketch (construction).} Take \\(X = [1,2]\\), \\(\\dot S = u - r(S)\\) with \\(r\\) "
     "continuous and injective, \\(U(S) = \\{0, r(S)\\}\\), \\(\\mathcal{V} = [1,2]\\), and the constant "
     "observation \\(O \\equiv 0\\). Under full information \\(u = r(S)\\) gives \\(\\dot S = 0\\), so every "
     "state is viable. Under \\(O \\equiv 0\\) the common control set over the fibre is \\(\\{0\\}\\) --- "
     "injectivity of \\(r\\) rules out a common \\(r(S)\\) --- so the policy must hold \\(u = 0\\), and "
     "\\(\\dot S = -r(S) < 0\\) drives every compatible trajectory out of \\(\\mathcal{V}\\) in finite time."),
    # thm:common-action
    ("\\emph{Proof sketch.} If the selected action is inadmissible at some compatible state, the policy "
     "fails there outright. Otherwise \\(a \\in U^B(B)\\), and the emptiness of the common safe-action set "
     "is caused by the boundary: some \\(\\bar x \\in B \\cap \\partial\\mathcal{V}\\) has "
     "\\(a \\notin \\mathcal{R}_{\\mathcal{V}}(\\bar x)\\), giving an active constraint \\(j\\) and a "
     "disturbance \\(\\bar d\\) with \\(\\nabla q_j(\\bar x) \\cdot f(\\bar x, a, \\bar d) < 0\\). A "
     "measurable local adverse selection (closed graph of \\(D\\), continuity of the drift; realized by "
     "(H3.3)) then drives \\(q_j\\) strictly downward from \\(q_j(\\bar x) = 0\\) within the first review "
     "period, before any observation can arrive."),
    # prop:uniform-margin
    ("\\emph{Proof sketch.} For fixed \\(a \\in U^B(B)\\), continuity of the drift and the closed graph of "
     "\\(D\\) extend the margin to \\(-\\eta/2\\) on a neighbourhood of \\((x_a, a, d_a)\\), and a "
     "measurable local selection realizes it; the trajectory from \\(x_a\\) under the held action then "
     "satisfies \\(q_j(x(t)) \\le -(\\eta/2) t < 0\\) for small \\(t\\), so "
     "\\(a \\notin \\mathcal{A}_{\\mathrm{tube}}(B, \\Delta)\\) for every \\(\\Delta > 0\\). As \\(a\\) was "
     "arbitrary, the tube-safe action set is empty."),
    # prop:ladder
    ("\\emph{Proof sketch.} The inclusion \\(\\mathcal{R}_{\\mathcal{V}}(x) \\subseteq U(x)\\) gives the "
     "second nesting. For the first, an action outside \\(\\mathcal{R}_{\\mathcal{V}}^B(B)\\) violates "
     "\\(\\nabla q_j(x) \\cdot f(x, a, d) \\ge 0\\) at some active boundary state, and the corresponding "
     "trajectory leaves \\(\\mathcal{V}\\) in arbitrarily small time, so the action is not tube-safe."),
    # thm:delayed
    ("\\emph{Proof sketch.} By (H4.1) the policy's actions on \\([0, T_{\\mathrm{obs}})\\) form one fixed "
     "open-loop control; if it is ever inadmissible at a compatible state the policy fails outright, otherwise (H4.2), applied to this implementable control, supplies a compatible state \\(x^*\\) with "
     "\\(q(x^*) = \\inf_{B_0} q\\) and an admissible disturbance realizing the drift (3); integrating (3) "
     "gives \\(q(x(t)) \\le \\inf_{B_0} q - \\varepsilon t\\), so the violation \\(q < 0\\) occurs by time "
     "\\(\\inf_{B_0} q / \\varepsilon\\), which (4) places strictly before \\(T_{\\mathrm{obs}}\\) --- "
     "before any informative observation, so the policy cannot react in time."),
    # thm:finite-horizon
    ("\\emph{Proof sketch.} Both directions are inductions on the horizon. Necessity: a policy safe for "
     "\\(N\\) steps picks \\(a \\in U^B(B_0)\\), and every possible successor belief is safe for "
     "\\(N - 1\\) steps, so \\(B_0 \\in \\mathrm{Pre}(\\mathcal{W}_{N-1})\\). Sufficiency: choose the "
     "witness action at each step, and every reachable state remains in \\(\\mathcal{V}\\) for \\(N\\) "
     "steps."),
    # prop:fibre
    ("\\emph{Proof sketch.} If \\(C\\) exists and \\(O(z_1) = O(z_2)\\), then "
     "\\(\\mathbf{1}_K(z_1) = C(O(z_1)) = C(O(z_2)) = \\mathbf{1}_K(z_2)\\), so membership is "
     "fibre-constant. Conversely, (5) makes \\(C(y) = \\mathbf{1}_K(z)\\) for any \\(z\\) with "
     "\\(O(z) = y\\) well defined and exact."),
    # cor:certainly-safe
    ("\\emph{Proof sketch.} A fibre containing one state in \\(K\\) and one outside violates (5), so "
     "Proposition~\\ref{prop:fibre} denies the certifier. On \\(\\mathcal{Y}_{\\mathrm{safe}}\\) every "
     "compatible state is safe, so the constant verdict ``safe'' is sound; outside it some compatible state "
     "is unsafe, so no sound ``safe'' verdict exists."),
    # prop:monotone
    ("\\emph{Proof sketch.} A policy viable under the smaller action sets, larger disturbance sets, smaller "
     "policy class, or coarser information structure remains admissible and nonanticipative under the "
     "corresponding enlargement or refinement, while the adversary's options are unchanged or reduced; the "
     "same policy witnesses viability."),
]

# ----------------------------------------------------------------------------
# Extract the 10 proof blocks (full text) and the 10 statement blocks
# ----------------------------------------------------------------------------
proof_re = re.compile(r"\\emph\{Proof[^}]*\}\s*(.*?)\\ensuremath\{\\square\}", re.S)
proof_matches = list(proof_re.finditer(t))
assert len(proof_matches) == len(SKETCHES), f"proof count {len(proof_matches)} != {len(SKETCHES)}"
proof_full = [m.group(0) for m in proof_matches]

RESULTS = [
    ("theorem", "thm:exit"),
    ("proposition", "prop:emptiness"),
    ("theorem", "thm:common-action"),
    ("proposition", "prop:uniform-margin"),
    ("proposition", "prop:ladder"),
    ("theorem", "thm:delayed"),
    ("theorem", "thm:finite-horizon"),
    ("proposition", "prop:fibre"),
    ("corollary", "cor:certainly-safe"),
    ("proposition", "prop:monotone"),
]

def get_env(txt, env, label):
    m = re.search(rf"\\begin\{{{env}\}}(\[[^\]]*\])?\\label\{{{label}\}}(.*?)\\end\{{{env}\}}", txt, re.S)
    assert m, f"env {label} not found"
    return m.group(0)

statement_full = [get_env(t, env, lab) for env, lab in RESULTS]

# extra environments needed in the supplementary so all \ref labels resolve
EXTRA = [
    ("definition", "def:kernel"),
    ("proposition", "prop:selector"),
    ("remark", "rem:comparison"),
    ("example", "ex:hidden-mode"),
    ("remark", "rem:sigma"),
    ("definition", "def:certifier"),
    ("remark", "rem:ce-trap"),
]
extra_full = [get_env(t, env, lab) for env, lab in EXTRA]

# ----------------------------------------------------------------------------
# Build the MAIN file
# ----------------------------------------------------------------------------
main = t

# 1. new preamble
new_preamble = r"""\documentclass[10pt,twocolumn]{article}
\usepackage[a4paper,margin=15mm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{amsthm}
\theoremstyle{definition}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}
\newtheorem{corollary}{Corollary}
\newtheorem{remark}{Remark}
\newtheorem{example}{Example}
\newtheorem{definition}{Definition}
\newtheorem{openproblem}{Open Problem}
\usepackage{graphicx}
\usepackage{booktabs,array,calc}
\usepackage[font=small,labelfont=bf]{caption}
\usepackage[colorlinks=true]{hyperref}
\usepackage{etoolbox}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\setcounter{secnumdepth}{-1}
\emergencystretch=3em
\allowdisplaybreaks
\AtBeginDocument{%
  \BeforeBeginEnvironment{equation}{\small}%
  \BeforeBeginEnvironment{equation*}{\small}%
  \BeforeBeginEnvironment{align}{\small}%
  \BeforeBeginEnvironment{align*}{\small}%
  \BeforeBeginEnvironment{gather}{\small}%
  \BeforeBeginEnvironment{gather*}{\small}%
  \BeforeBeginEnvironment{multline}{\small}%
  \BeforeBeginEnvironment{multline*}{\small}%
  \BeforeBeginEnvironment{flalign}{\small}%
  \BeforeBeginEnvironment{flalign*}{\small}%
}

\begin{document}
"""
main = new_preamble + main[main.index("\\title{"):]

# 2. proofs -> sketches
for m, sk in zip(proof_matches, SKETCHES):
    main = main.replace(m.group(0), sk, 1)

# 3. remove three figures (moved to supplementary)
def remove_figure(txt, filename):
    key = f"figs_p2/{filename}"
    i = txt.index(key)
    s = txt.rfind("\\begin{figure}", 0, i)
    e = txt.index("\\end{figure}", i) + len("\\end{figure}")
    return txt[:s] + txt[e:]

main = remove_figure(main, "fig_p2_ladder.png")
main = remove_figure(main, "fig_p2_obstruction_tree.png")
main = remove_figure(main, "fig_p2_ce_trap.png")

# 4. fix in-text references to the moved figures
main = span_replace(main,
    "argument. Figure~\\ref{fig:ladder}", "below it.",
    "argument; the ladder, and the position of the exit certificate below it, are drawn in the Supplementary Material (Figure~S1).")
main = span_replace(main,
    "; Figure~\\ref{fig:obstruction-tree}", "draws the tree.",
    "; the tree is drawn in the Supplementary Material (Figure~S2).")

# 5. Appendix A -> supplementary; fix its two text mentions
main = span_replace(main, "\\subsection{Appendix A: Bounded Constructions and Scope", "\\subsection{References}",
                    "\\subsection{References}")
main = main.replace("the harvest vector of\nAppendix A is the lowercase", "the harvest vector of\nthe Supplementary Material is the lowercase", 1)
main = main.replace("of Appendix A.2.", "of the Supplementary Material.", 1)

# 6. condense Section 1.1 literature paragraph + missing-instrument paragraph
new_11 = (
    "The question splits naturally. The sufficiency direction has a canonical literature: Veliov (1993) "
    "gives conditions for the existence of an output-feedback regulation map under incomplete and inexact "
    "measurement, reducing under perfect measurement to the classical viability condition (Haddad, 1981); "
    "the estimation-tube programme (Cardaliaguet, Quincampoix, and Saint-Pierre, 2007) absorbs imperfect "
    "information into an estimation space of sets of compatible states with no loss of value; and barrier "
    "certificates certify safety (Prajna and Jadbabaie, 2004; Prajna, Jadbabaie, and Pappas, 2007), with "
    "converse and hybrid necessary-and-sufficient characterizations (Prajna and Rantzer, 2005; Maghenem and "
    "Sanfelice, 2019). What that literature does not supply is the necessity side: a calculus of "
    "obstruction certificates. An obstruction certificate is a checkable witness that no observation-based "
    "policy exists --- finite in the finite-state and polyhedral cases --- and the argument it makes is that "
    "a prescribed class of observation-based policies fails not because a particular policy is bad, but "
    "because the information structure leaves no room for any policy. In the polyhedral common-action and "
    "certification forms (Theorem~\\ref{thm:common-action} and Proposition~\\ref{prop:fibre}) it is a finite, "
    "checkable test; the drift certificates of Theorem~\\ref{thm:exit} and Theorem~\\ref{thm:delayed} are "
    "not finite objects, one exhibiting an enforcement selection and the other bounding the timing "
    "uniformly over every policy. Veliov's condition tells us when output feedback can work; the "
    "obstruction calculus tells us when it cannot, and for the borderline cases it identifies which "
    "quantitative feature of the observation design --- timing, coarseness, bias, aggregation --- is "
    "responsible.")
main = span_replace(main, "The question splits naturally.", "aggregation --- is responsible.", new_11)

# 7. condense Section 1.3
new_13 = (
    "The viability-theory background is Aubin (1991), Aubin, Bayen, and Saint-Pierre (2011), and the "
    "kernel approximation theory of Saint-Pierre (1994); robust viability is Aubin and Frankowska (1990) "
    "and Frankowska (1989). Under incomplete measurement, the sufficiency theorem is Veliov (1993), "
    "viability with a priori unknown but observable parameters is Quincampoix and Veliov (1994), and the "
    "estimation-set reduction is Cardaliaguet, Quincampoix, and Saint-Pierre (2007). On the failure side, "
    "Aubin (2001) characterizes the complement of the kernel --- Poincar\\'e's ``shadow'' --- together with "
    "the capture basins, and Aubin and Catt\\'e (2002) supply the bilateral-fixed-point and "
    "discriminating-kernel calculus; the certificates of Section 3 are one-sided, observation-constrained "
    "analogues of that programme. In verification, barrier certificates originate with Prajna and Jadbabaie "
    "(2004), with worst-case and converse results in Prajna, Jadbabaie, and Pappas (2007) and Prajna and "
    "Rantzer (2005) and hybrid characterizations in Maghenem and Sanfelice (2019). The sustainability "
    "application domain is B\\'en\\'e, Doyen, and Gabay (2001), De Lara and Doyen (2008), Doyen et al. "
    "(2012), and Doyen and Gajardo (2020). To our knowledge, the obstruction certificates of "
    "Theorem~\\ref{thm:common-action}, Theorem~\\ref{thm:delayed}, and Proposition~\\ref{prop:fibre} --- in "
    "particular the certification criterion and the timing bound --- have not been stated in this form; "
    "the elementary facts on which they rest (quantifier commutation and Dini comparison) are classical.")
main = span_replace(main, "\\subsubsection{1.3 Related work}\\label{related-work}", "\\subsubsection{1.4 Organization}\\label{organization}",
                    "\\subsubsection{1.3 Related work}\\label{related-work}\n\n" + new_13 + "\n\n\\subsubsection{1.4 Organization}\\label{organization}")

# 8. update Section 1.4 organization (proofs now in supplementary)
main = span_replace(main, "Section 7 concludes. Proofs are complete in the main text;", "rather than reproduced.",
    "Section 7 concludes. Proof sketches are given in the main text; the complete proofs, the expanded "
    "sufficiency review, and the auxiliary constructions are collected in the Supplementary Material.")

# 9. condense Section 5
new_5 = (
    "\\subsection{5. The Sufficiency Landscape}\\label{the-sufficiency-landscape-cited}\n"
    "\n"
    "For contrast, we record the sufficiency results against which the obstruction calculus is defined; the "
    "proofs are in the cited sources.\n"
    "\n"
    "\\textbf{(a) Veliov's output-feedback condition.} Veliov (1993) gives a sufficient condition for the "
    "existence of an output-feedback regulation map under incomplete and inexact measurement, reducing under "
    "perfect measurement to the classical viability condition (Haddad, 1981). Veliov's theorem certifies "
    "existence; the obstruction calculus certifies nonexistence; a problem satisfying neither requires a "
    "stronger observer or a finer observation structure.\n"
    "\n"
    "\\textbf{(b) The estimation-tube programme.} Cardaliaguet, Quincampoix, and Saint-Pierre (2007) pass "
    "from imperfect information in the measurement space to perfect information in an estimation space of "
    "sets of compatible states, with equality of value functions and a Dini-derivative characterization. "
    "Under the set-membership semantics the estimation-space solution propagates the belief under a single "
    "control signal, so its controls are common controls; the common-action obstruction "
    "(Theorem~\\ref{thm:common-action}) is the certificate that no jointly admissible selection exists at the "
    "information state in question (Section 6.3).\n"
    "\n"
    "\\textbf{(c) Observer-and-buffer transfer.} If a full-information feedback exists with a strict inward "
    "margin and an observer supplies exponentially convergent estimates, output feedback of the estimate "
    "preserves safety on a buffered subset (observer-to-viability transfer with safety buffer; Sontag, 1998), "
    "and eroded kernels remain invariant under bounded estimation and implementation errors (erosion absorbs "
    "the error). Under margins and convergence, output feedback can work; Sections 3--4 state when it "
    "cannot.\n"
    "\n"
    "\\textbf{(d) The linear substitution alternative.} For a finite linear model in which a resource-typed "
    "system must meet a demand vector through specified substitution pathways, exactly one of the following "
    "holds (Farkas, 1902; Gale, 1960): (i) there exists a non-negative pathway vector \\(a \\ge 0\\) "
    "satisfying the linear substitution constraints; or (ii) there exist multipliers "
    "\\(\\alpha, \\beta, \\gamma \\ge 0\\) with\n"
    "\\[\\alpha^\\top R + \\beta^\\top E - \\gamma^\\top Q \\ge 0 \\quad\\text{componentwise},\\qquad "
    "\\gamma^\\top s^{\\mathrm{req}} > \\alpha^\\top x + \\beta^\\top e.\\]\n"
    "The second statement is a separation certificate that the pathways cannot meet demand within the typed "
    "resource and capacity bounds --- the feasibility-side complement of the observation-side obstructions of "
    "Sections 3--4.\n"
    "\\subsection{6. Discussion}\\label{discussion}\n")
main = span_replace(main, "\\subsection{5. The Sufficiency Landscape}\\label{the-sufficiency-landscape-cited}",
                    "\\subsection{6. Discussion}\\label{discussion}", new_5)

# 10. condense 6.2 and 6.3
new_62 = (
    "\\subsubsection{6.2 Relation to barrier\ncertificates}\\label{relation-to-barrier-certificates}\n"
    "\n"
    "Barrier certificates certify safety from a scalar function whose zero level set separates the unsafe "
    "region from all trajectories (Prajna and Jadbabaie, 2004; Prajna, Jadbabaie, and Pappas, 2007); the "
    "converse, under convex-duality conditions on density functions, is Prajna and Rantzer (2005), and "
    "necessary-and-sufficient hybrid characterizations are Maghenem and Sanfelice (2019). "
    "Theorem~\\ref{thm:exit} is the unsafety complement of that converse, not its observation-theoretic "
    "counterpart: a Dini-drift certificate of unsafety needing no observation structure, constructive in the "
    "enforcing disturbance and exit time. The remaining certificates (Proposition~\\ref{prop:emptiness}, "
    "Theorem~\\ref{thm:common-action}, Theorem~\\ref{thm:delayed}, Proposition~\\ref{prop:fibre}) act at the "
    "level of the information set itself: barrier constructions presuppose a state --- or a specified state "
    "estimate --- for feedback, whereas the common-action and timing obstructions certify the emptiness of "
    "the common safe-action set at a given information state, which barrier methods do not address.\n"
    "\n"
    "\\subsubsection{6.3 Relation to estimation\ntubes}\\label{relation-to-estimation-tubes}\n"
    "\n")
main = span_replace(main, "\\subsubsection{6.2 Relation to barrier",
                    "\\subsubsection{6.3 Relation to estimation\ntubes}\\label{relation-to-estimation-tubes}",
                    new_62)

new_63 = (
    "The estimation-tube programme shows that imperfect measurement can be absorbed into set-valued dynamics "
    "on an estimation space with no loss in value (Cardaliaguet, Quincampoix, and Saint-Pierre, 2007); the "
    "present theorems delimit its reach rather than contradict it. The reduction preserves values, and its "
    "belief-state controls are common controls; the obstruction calculus is the local certificate layer of "
    "that programme --- the common-action obstruction certifies that the belief-state predecessor is empty, "
    "the timing bound quantifies when it fails for reasons of information arrival, and the fibre criterion "
    "states when no observation-based verdict can be exact. Belief-space viability answers \\emph{whether}; "
    "the obstruction calculus answers \\emph{why not, and what to change}.\n"
    "\n"
    "\\subsubsection{6.4 Consequences for monitoring and indicator\ndesign}\\label{consequences-for-monitoring-and-indicator-design}\n"
    "\n")
main = span_replace(main, "\\subsubsection{6.3 Relation to estimation\ntubes}\\label{relation-to-estimation-tubes}",
                    "\\subsubsection{6.4 Consequences for monitoring and indicator\ndesign}\\label{consequences-for-monitoring-and-indicator-design}",
                    new_63)

# 11. table -> full width; kept figures -> column width
main = main.replace("\\begin{table}[htbp]", "\\begin{table*}[t]", 1)
main = main.replace("\\end{table}", "\\end{table*}", 1)
main = main.replace("width=0.72\\linewidth]{figs_p2/fig_p2_common_action.png}", "width=0.82\\columnwidth]{figs_p2/fig_p2_common_action.png}", 1)
main = main.replace("width=0.72\\linewidth]{figs_p2/fig_p2_timing.png}", "width=0.82\\columnwidth]{figs_p2/fig_p2_timing.png}", 1)
main = main.replace("width=0.66\\linewidth]{figs_p2/fig_p2_fibre.png}", "width=0.82\\columnwidth]{figs_p2/fig_p2_fibre.png}", 1)

# 12. drop section separators
main = re.sub(r"\\begin\{center\}\s*\\rule\{0\.5\\linewidth\}\{0\.5pt\}\s*\\end\{center\}", "", main)

# 12b. compact references (small size) to keep the page count at the nominal target
main = main.replace("\\subsection{References}\\label{references}", "\\subsection{References}\\label{references}\n{\\footnotesize", 1)
main = main.replace("\\section*{Declarations}", "}\n\n\\section*{Declarations}", 1)

# 12c. compact declarations (bold run-in labels instead of subsection* blocks)
DECL_OLD = (
    "\\section*{Declarations}\n"
    "\n"
    "\\subsection*{Funding}\n"
    "\n"
    "None.\n"
    "\n"
    "\\subsection*{Competing interests}\n"
    "\n"
    "None.\n"
    "\n"
    "\\subsection*{Data availability}\n"
    "\n"
    "No data were used; all constructions are symbolic.\n"
    "\n"
    "\\subsection*{Code availability}\n"
    "\n"
    "No code was used or produced; all constructions are symbolic.\n"
    "\n"
    "\\subsection*{AI declaration}\n"
    "GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review.\n"
)
DECL_NEW = (
    "\\section*{Declarations}\n"
    "\n"
    "\\textbf{Funding.} None.\\quad "
    "\\textbf{Competing interests.} None.\\quad "
    "\\textbf{Data availability.} No data were used; all constructions are symbolic.\\quad "
    "\\textbf{Code availability.} No code was used or produced; all constructions are symbolic.\\quad "
    "\\textbf{AI declaration.} GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and "
    "iterative review.\n"
)
assert DECL_OLD in main, "Declarations block not found"
main = main.replace(DECL_OLD, DECL_NEW, 1)

# 13. re-break the widest display equations for the narrow column
WIDE = [
 (r"\[\mathrm{proj}_{\exists}\big(\mathrm{IRViab}_{\mathcal{J}}(\mathcal{V})\big) \;\subseteq\; \mathrm{proj}_{\exists}\big(\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})\big) \;\subseteq\; \mathrm{RViab}(\mathcal{V}) \;\subseteq\; \mathrm{Viab}(\mathcal{V}),\]",
  r"\["
  "\n\\begin{aligned}"
  "\n\\mathrm{proj}_{\\exists}\\big(\\mathrm{IRViab}_{\\mathcal{J}}(\\mathcal{V})\\big)"
  "&\\;\\subseteq\\; \\mathrm{proj}_{\\exists}\\big(\\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V})\\big) \\\\"
  "\n&\\;\\subseteq\\; \\mathrm{RViab}(\\mathcal{V}) \\;\\subseteq\\; \\mathrm{Viab}(\\mathcal{V}),"
  "\n\\end{aligned}"
  "\n\\]"),
 (r"\[\mathcal{R}_{\mathcal{V}}(x) \;=\; \Big\{ u \in U(x) : \forall d \in D(x),\; \forall j \text{ with } q_j(x) = 0,\; \nabla q_j(x) \cdot f(x, u, d) \ge 0 \Big\},\]",
  r"\["
  "\n\\begin{aligned}"
  "\n\\mathcal{R}_{\\mathcal{V}}(x) \\;=\\; \\bigl\\{ u \\in U(x) : {}& \\forall d \\in D(x),\\; \\forall j \\text{ with } q_j(x) = 0,\\\\"
  "\n& \\nabla q_j(x) \\cdot f(x, u, d) \\ge 0 \\bigr\\},"
  "\n\\end{aligned}"
  "\n\\]"),
 (r"\[B_t \;=\; \left\{ \xi(t) : \xi(0) \in B_0,\ \dot\xi(s) = f(\xi(s), u(s), d(s)),\ d(s) \in D(\xi(s)),\ O(\xi(s)) = y(s) \text{ for all observed } s \le t \right\},\]",
  r"\["
  "\n\\begin{aligned}"
  "\nB_t \\;=\\; \\bigl\\{ \\xi(t) : {}& \\xi(0) \\in B_0,\\\\"
  "\n& \\dot\\xi(s) = f(\\xi(s), u(s), d(s)),\\ d(s) \\in D(\\xi(s)),\\\\"
  "\n& O(\\xi(s)) = y(s) \\text{ for all observed } s \\le t \\bigr\\},"
  "\n\\end{aligned}"
  "\n\\]"),
 (r"\[\mathcal{R}_{\mathcal{V}}^B(B) \;:=\; \bigcap_{x \in B} \mathcal{R}_{\mathcal{V}}(x) \;=\; \varnothing \quad \text{with} \quad U^B(B) \neq \varnothing, \tag{2} \qquad \text{(safety obstruction)}\]",
  r"\begin{gather}"
  "\n\\mathcal{R}_{\\mathcal{V}}^B(B) \\;:=\\; \\bigcap_{x \\in B} \\mathcal{R}_{\\mathcal{V}}(x) \\;=\\; \\varnothing, \\tag{2}\\\\"
  "\n\\text{with } U^B(B) \\neq \\varnothing \\quad \\text{(safety obstruction)} \\notag"
  "\n\\end{gather}"),
 (r"\[U^B(B)=\varnothing \;\Longrightarrow\; \mathcal{R}_{\mathcal{V}}^B(B)=\varnothing \;\Longrightarrow\; \mathcal{A}_{\mathrm{tube}}(B,\Delta)=\varnothing \;\Longrightarrow\; B\notin\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V}).\]",
  r"\["
  "\n\\begin{aligned}"
  "\nU^B(B)=\\varnothing \\;&\\Longrightarrow\\; \\mathcal{R}_{\\mathcal{V}}^B(B)=\\varnothing \\;\\Longrightarrow\\; \\mathcal{A}_{\\mathrm{tube}}(B,\\Delta)=\\varnothing \\\\"
  "\n&\\Longrightarrow\\; B\\notin\\mathrm{ERViab}_{\\mathcal{I}}(\\mathcal{V})."
  "\n\\end{aligned}"
  "\n\\]"),
 (r"\[\mathrm{Post}(B,a,y) = \left\{ x^+\in X : \exists\, x\in B,\ d\in D(x),\ x^+ = F(x,a,d),\ y = O(x,a,d,x^+) \right\},\]",
  r"\["
  "\n\\begin{gathered}"
  "\n\\mathrm{Post}(B,a,y) = \\bigl\\{ x^+\\in X : \\exists\\, x\\in B,\\ d\\in D(x), \\\\"
  "\nx^+ = F(x,a,d),\\ y = O(x,a,d,x^+) \\bigr\\},"
  "\n\\end{gathered}"
  "\n\\]"),
 (r"\[\mathrm{Pre}(\mathcal C) = \left\{ B\subseteq\mathcal V : \exists\, a\in U^B(B)\ \text{such that}\ \mathrm{Post}(B,a,y)\in\mathcal C\ \text{for every possible } y \right\},\]",
  r"\["
  "\n\\begin{gathered}"
  "\n\\mathrm{Pre}(\\mathcal C) = \\bigl\\{ B\\subseteq\\mathcal V : \\exists\\, a\\in U^B(B)\\ \\text{such that}\\\\"
  "\n\\mathrm{Post}(B,a,y)\\in\\mathcal C\\ \\text{for every possible } y \\bigr\\},"
  "\n\\end{gathered}"
  "\n\\]"),
 (r"\[\alpha^\top R + \beta^\top E - \gamma^\top Q \ge 0 \quad\text{componentwise},\qquad \gamma^\top s^{\mathrm{req}} > \alpha^\top x + \beta^\top e.\]",
  r"\["
  "\n\\begin{aligned}"
  "\n&\\alpha^\\top R + \\beta^\\top E - \\gamma^\\top Q \\ge 0 \\quad\\text{componentwise},\\\\"
  "\n&\\gamma^\\top s^{\\mathrm{req}} > \\alpha^\\top x + \\beta^\\top e."
  "\n\\end{aligned}"
  "\n\\]"),
]
for old, new in WIDE:
    assert old in main, f"WIDE target not found: {old[:50]}..."
    main = main.replace(old, new, 1)

# ----------------------------------------------------------------------------
# v30 additions: the three Automatica routes (new sections 7-9, conclusion -> 10)
# ----------------------------------------------------------------------------
NEW_SECTIONS = r"""
\subsection{7. Complete Characterizations and the Residual Gap}\label{complete-characterizations}

The certificates of Section 3 are sound sufficient conditions for nonviability, and Section 6.5 recorded that they do not exhaust the complement of the epistemic kernel. This section makes that gap precise: it exhibits that gap precise: it exhibits two settings in which the viability question admits an exact answer --- the one-step (finite discrete) setting, where the common-action certificate is necessary and sufficient, and the static-observation setting, where the problem reduces exactly to open-loop robust viability --- and states the residual dynamic gap as an open problem.

\begin{theorem}[one-step completeness]\label{thm:onestep}
Let \(X, A, D, Y\) be finite, with transition \(x^{+} = F(x,a,d)\), observation \(y = O(x,a,x^{+})\), and safe set \(\mathcal{V} \subseteq X\). Define the one-step safe set
\[
S_{1}(x) = \bigl\{ a \in U(x) : F(x,a,d) \in \mathcal{V} \text{ for all } d \in D(x) \bigr\}.
\]
A belief \(B \subseteq \mathcal{V}\) is one-step viable under \(\mathcal{I}\) --- some observation-based policy achieves \(x_{1} \in \mathcal{V}\) for every \(x_{0} \in B\) and every admissible disturbance --- if and only if \(\bigcap_{x \in B} S_{1}(x) \neq \varnothing\). Hence \(B \notin \mathcal{W}_{1}\) exactly when the common safe-action set is empty, the discrete reading of Theorem~\ref{thm:common-action}.
\end{theorem}

\emph{Proof.} \((\Rightarrow)\) An observation-based policy depends on the record only, and every \(x \in B\) produced the same record, so the policy plays a single \(a \in U^{B}(B)\); safety of the first step forces \(F(x,a,d) \in \mathcal{V}\) for all \(x \in B\) and \(d \in D(x)\), i.e.\ \(a \in \bigcap_{x \in B} S_{1}(x)\). \((\Leftarrow)\) Playing any \(a\) in the intersection keeps every successor in \(\mathcal{V}\). \hfill\(\square\)

Combined with the backward recursion \(\mathcal{W}_{k+1} = \mathrm{Pre}(\mathcal{W}_{k})\) of Theorem~\ref{thm:finite-horizon}, Theorem~\ref{thm:onestep} shows that the pair \emph{(common-action certificate, recursion)} is a complete characterization at every finite horizon in finite systems: the certificate detects first-step emptiness, and the recursion propagates the obstruction to every later step.

\begin{theorem}[static-observation reduction to open-loop viability]\label{thm:static-complete}
Let \(\mathcal{V}\) be compact with \(C^{1}\) constraint functions \(q_{j}\), \(f\) continuous with \(D\) compact-valued and of closed graph, \(U(x) \equiv U\), and suppose the observation is \emph{static}: \(y(t) = O(x(t))\) is constant along every admissible trajectory, so no information accrues over time. Then every observation-based policy coincides with an \emph{open-loop} control --- a measurable function of time only, \(u(\cdot):[0,\infty)\to U\) --- and \(B_{0} \in \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})\) if and only if there exists an open-loop control under which every trajectory from every \(x_{0} \in B_{0}\) and every admissible disturbance realization stays in \(\mathcal{V}\) for all time. Within the constant-control subclass \(u(\cdot) \equiv u_{0}\), the condition is the robust Nagumo boundary condition
\[
\nabla q_{j}(x) \cdot f(x, u_{0}, d) \;\ge\; 0
\qquad \text{for all } x \in \partial\mathcal{V},\ \text{active } j,\ d \in D(x),
\]
necessary for a constant control to keep \(\mathcal{V}\) invariant and sufficient under the standard regularity assumptions (Aubin, 1991; Frankowska, 1989). A time-varying open-loop control may be viable when no constant control is; the open-loop reduction, not the constant-control condition, is the exact characterization in the static class.
\end{theorem}

\emph{Proof.} A static observation makes the record constant, so a policy's action at time \(t\) can depend on time only --- open-loop; this gives the reduction in both directions (a viable policy yields a viable open-loop control, and every open-loop control is an admissible observation-based policy). The constant-control statement is the robust Nagumo theorem (Aubin, 1991; Frankowska, 1989): \emph{necessary}, because any trajectory leaving \(\mathcal{V}\) under \(u_{0}\) exhibits a boundary point with outward drift, and \emph{sufficient} under the regularity assumptions. \hfill\(\square\)

Theorem~\ref{thm:static-complete} makes the sense of completeness in the static class precise: the obstruction is exactly the nonexistence of a robustly viable open-loop control, and within the constant-control subclass the boundary condition of Theorem~\ref{thm:common-action} is necessary and sufficient. Completeness fails only when information accrues, where the residual modes are post-observation recourse and timing --- the hidden-mode example and the timing bound of Section 3.4.

\begin{openproblem}[dynamic-observation completeness]\label{op:dynamic}
Give a finite, checkable certificate that is necessary and sufficient for membership in \(\mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})\) under dynamic observation beyond the belief-space restatement below, or prove a separation showing that none exists in a natural class. The belief-space restatement is: \(B_{0} \in \mathrm{ERViab}_{\mathcal{I}}(\mathcal{V})\) if and only if \(B_{0}\) belongs to the viability kernel of the set-valued belief dynamics under the observation constraint (Cardaliaguet, Quincampoix, and Saint-Pierre, 2007); this is a complete characterization on the infinite-dimensional space of compact beliefs, and the obstruction calculus of Section 3 is its finite, certifiable layer.
\end{openproblem}

\subsection{8. A Calibrated Case Study and a Coverage Audit}\label{case-study}

We instantiate the three observation-side mechanisms on a concrete resource model and audit the certificates against the exact recursion of Theorem~\ref{thm:finite-horizon}. The model is a single-species stock \(S \in [0,1]\) (fraction of carrying capacity) with discrete dynamics
\[
\begin{gathered}
S^{+} = \mathrm{clip}\bigl(S + S(1-S) - u + w\bigr),\\
u \in [0, 0.3],\quad w \in \{-0.02, 0, +0.02\},
\end{gathered}
\]
harvest \(u\), recruitment noise \(w\) read adversarially, and a sustainability floor \(S_{\min} = 0.3\) (Clark, 1990).

\textbf{The fibre criterion.} The regulator observes a coarse two-bin index, low if \(S < 0.6\) and high if \(S \ge 0.6\). The safe set \(\mathcal{V} = [0.3, 1]\) is not a union of index bins: the low bin contains both \(0.1\) (below the floor) and \(0.4\) (above it). By Proposition~\ref{prop:fibre} no exact observation-only certifier exists, and by Corollary~\ref{cor:certainly-safe} the certainly-safe set is the single bin \(\mathcal{Y}_{\mathrm{safe}} = \{\text{high}\}\). A verdict of ``safe'' on the strength of a low reading is therefore unsound; the index can certify safety only when it reads high.

\textbf{The delayed-information timing bound.} The timing obstruction is sharpest in the hidden-regime system of Section 3.4: regimes \(\theta \in \{-1, +1\}\), dynamics \(z^{+} = z + \theta u\), controls \(u \in \{-1, +1\}\), floor \(z \ge 1\), with \(\theta\) revealed only after a blind window of \(T_{\mathrm{obs}}\) steps. From \(z_{0} = 2\) the drift of \(q(z) = z - 1\) on the declining branch is \(-1\) under every admissible action, so the threshold of Theorem~\ref{thm:delayed} and Remark~\ref{rem:sigma} is \(\sigma^{*}(B_{0}) = z_{0} - 1 = 1\): nonviability is certified for every \(T_{\mathrm{obs}} > 1\), while \(T_{\mathrm{obs}} = 1\) is viable --- the regime is revealed in time, and \(u = \theta\) then restores growth. In the fishery above the same certificate is silent in the normal regime, because \(u_{0} = 0\) keeps every stock above the floor; the bound fires only when no blind action avoids decline, which is precisely its scope.

\textbf{The certainty-equivalence trap.} With a biased index \(\hat{S} = S + 0.1\), \(g(S) = S^{2}\), and \(\mathcal{V} = [1,2]\), the certainty-equivalence policy \(u = g(\hat{S})\) produces \(\dot{S} = g(S+0.1) - g(S) = 0.2S + 0.01 > 0\), which reaches the upper bound from \(S = 1\) in \(\approx 3.3\) time units, while the bias-corrected policy \(u = g(\hat{S} - 0.1)\) keeps \(\dot{S} = 0\) and the kernel nonempty (Remark~\ref{rem:ce-trap}).

\textbf{A reproducible delayed hidden-regime model.} The audit runs on the exact instance specified here. The state is \((z, \theta)\) with \(\theta \in \{-1, +1\}\) a hidden regime and \(z \ge 0\); the action \(u \in \{-1, +1\}\) is common to both regimes; the transition is \(z^{+} = z + \theta u\); the safe set is \(\mathcal{V} = \{ z \ge 1 \}\); and the observation reveals nothing before \(T_{\mathrm{obs}}\) and reveals \(\theta\) exactly at time \(T_{\mathrm{obs}}\). From a known \(z_{0}\) with both regimes possible, the belief after \(k < T_{\mathrm{obs}}\) blind steps contains the two extreme histories \((z_{0} - k, -1)\) and \((z_{0} + k, +1)\), and a blind policy must choose the same \(u\) for both branches at every blind step. The guaranteed blind-window survival time is therefore \(\sigma^{*}(B_{0}) = z_{0} - 1\): the best blind policy drives one branch down at unit rate, so the declining branch reaches the floor \(1\) at time \(z_{0} - 1\), and after the reveal \(u = \theta\) keeps \(z \ge 1\) forever. Hence \(B_{0}\) is robustly epistemically viable if and only if \(z_{0} - 1 \ge T_{\mathrm{obs}}\), i.e.\ \(z_{0} \ge 1 + T_{\mathrm{obs}}\) --- the ground truth against which the certificates are audited. The one-step certificate of Theorem~\ref{thm:common-action} fires exactly when \(z_{0} < 2\) (one blind step already forces \(z_{0} - 1 < 1\)), and the timing bound of Theorem~\ref{thm:delayed} fires exactly when \(z_{0} \ge 2\) and \(T_{\mathrm{obs}} > z_{0} - 1\).


\textbf{A coverage audit.} To quantify the gap conceded in Section 6.5, we audit the certificates against the exact recursion on the delayed hidden-regime system, over the grid \(z_{0} \in \{1.0, 1.1, \dots, 2.5\}\), \(T_{\mathrm{obs}} \in \{1,2,3\}\). Table~\ref{tab:coverage} and Figure~\ref{fig:coverage} report the true verdict, the one-step certificate, and the timing bound.

\begin{table*}[t]
\centering
\footnotesize
\begin{tabular}{@{}l|cccccccccccccccc@{}}
\toprule
\(T_{\mathrm{obs}}\) & \multicolumn{16}{c}{initial position \(z_{0}\)} \\
\cmidrule(lr){2-17}
 & 1.0 & 1.1 & 1.2 & 1.3 & 1.4 & 1.5 & 1.6 & 1.7 & 1.8 & 1.9 & 2.0 & 2.1 & 2.2 & 2.3 & 2.4 & 2.5 \\
\midrule
1 & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\circ\) & \(\circ\) & \(\circ\) & \(\circ\) & \(\circ\) & \(\circ\) \\
2 & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\ast\) & \(\ast\) & \(\ast\) & \(\ast\) & \(\ast\) & \(\ast\) \\
3 & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\bullet\) & \(\ast\) & \(\ast\) & \(\ast\) & \(\ast\) & \(\ast\) & \(\ast\) \\
\bottomrule
\end{tabular}
\caption{Coverage audit on the delayed hidden-regime system: \(\circ\) viable; \(\bullet\) nonviable, certified by the common-action certificate (Theorem~\ref{thm:common-action}); \(\ast\) nonviable, certified only by the timing bound (Theorem~\ref{thm:delayed}). Every nonviable cell is covered by exactly one certificate.}
\label{tab:coverage}
\end{table*}

\begin{figure*}[t]
\centering
\includegraphics[width=0.82\linewidth]{figs_p2/fig_p2_coverage.png}
\caption{The coverage audit of Table~\ref{tab:coverage}: green = viable; red = nonviable, certified by the common-action certificate; orange = nonviable, certified only by the timing bound (the residual gap of Section 6.5). The dashed curve is the true boundary \(z_{0} = 1 + T_{\mathrm{obs}}\) and the solid vertical line the one-step boundary \(z_{0} = 2\).}
\label{fig:coverage}
\end{figure*}

\begin{remark}[joint completeness in the delayed class]\label{rem:coverage}
In every audited cell the true verdict is reproduced by exactly one of the two certificates: of the 42 nonviable cells, 30 are certified by the common-action certificate and the remaining 12 --- precisely those with \(z_{0} \ge 2\) and \(T_{\mathrm{obs}} > z_{0} - 1\) --- by the timing bound; none is uncovered. In this class the two certificates are jointly complete, and the Section 6.5 gap reduces to the timing cells.
\end{remark}

The audit is symbolic and one-dimensional; a multidimensional belief-space
numerical campaign is deferred to future work, and the case study makes
no claim of a general-purpose computational calculus.

\subsection{9. A Probabilistic Development: Belief-State Safety Values}\label{probabilistic-development}

The certificates of Sections 3--4 rest on set-membership semantics: the information state is a set of compatible states. This section records the stochastic counterpart --- the belief-state safety value of partially observable control --- and its obstruction certificate, connecting the calculus to the partially observable literature (\r{A}str\"om, 1965; Smallwood and Sondik, 1973).

Let \(X, A, D, Y\) be finite, with a stochastic transition \(T(x' \mid x, a)\) and an observation likelihood \(g(y \mid x, a, x')\). Augment the state space with an absorbing unsafe state \(\bot\): for \(x \in \mathcal{V}\), \(T(\bot \mid x, a) = 1 - \sum_{x' \in \mathcal{V}} T(x' \mid x, a)\), and \(T(\bot \mid \bot, a) = 1\). A belief is a distribution \(b\) over \(X \cup \{\bot\}\), updated by Bayes' rule \(\tau(b, a, y)\), with \(\mathbb{P}(y \mid b, a) = \sum_{x, x'} b(x)\, T(x' \mid x, a)\, g(y \mid x, a, x')\). The \emph{safety value} is the maximal survival probability
\[
V_{k}(b) = \max_{\pi}\; \mathbb{P}_{\pi}\bigl( x_{t} \in \mathcal{V} \text{ for } t = 0, \dots, k \;\big|\; b \bigr).
\]

\begin{theorem}[belief-state safety value]\label{thm:pomdp}
\(V_{0}(b) = b(\mathcal{V})\) (the horizon counts the current state), and for \(k \ge 0\)
\[
V_{k+1}(b) = \max_{a \in A}\; \sum_{y \in Y} \mathbb{P}(y \mid b, a)\; V_{k}\bigl(\tau(b, a, y)\bigr),
\]
with the time convention that the policy acts, observes \(y\), then acts again. The recursion is exact on every finite horizon; it is the Smallwood--Sondik belief-state value iteration specialized to the absorbing safety reward (Smallwood and Sondik, 1973).
\end{theorem}

\emph{Proof.} Standard value iteration for the belief-state Markov decision process: conditioning on the observation after the action and applying the optimal continuation gives the identity, and the absorbing state makes \(V_{k}\) the \(k\)-step survival probability (Smallwood and Sondik, 1973). \hfill\(\square\)

\begin{proposition}[chance-constrained common-action obstruction]\label{prop:chance}
Let \(b \in \Delta(\mathcal{V})\) (so \(b(\mathcal{V}) = 1\)) and write \(p(x,a) = 1 - \sum_{x' \in \mathcal{V}} T(x' \mid x, a)\). If
\[
\sum_{x \in \mathcal{V}} b(x)\, p(x,a) \;\ge\; \delta \qquad \text{for every } a \in A,
\]
then \(V_{k}(b) \le 1 - \delta\) for every \(k \ge 1\), and the chance constraint \(\mathbb{P}_{b,\pi}(x_{0}, \dots, x_{k} \in \mathcal{V}) \ge 1 - \varepsilon\) is infeasible under every policy whenever \(\varepsilon < \delta\).
\end{proposition}

\emph{Proof.} The one-step survival probability under action \(a\) is \(1 - \sum_{x} b(x)\, p(x,a) \le 1 - \delta\), so \(V_{1}(b) \le 1 - \delta\). Since \(V_{k+1} \le V_{k}\) --- more steps cannot raise the survival probability --- \(V_{k}(b) \le V_{1}(b) \le 1 - \delta\). \hfill\(\square\)

\begin{proposition}[degenerate (deterministic) limit]\label{prop:degenerate}
Let \(X, A, D, Y\) be finite, fix the deterministic maps \(x^{+} = F(x,a,d)\) and \(y = O(x,a,x^{+})\) of Section 3.5, and suppose the stochastic transition and likelihood have supports \(\{F(x,a,d) : d \in D(x)\}\) and \(\{O(x,a,x^{+}) : x^{+} \text{ reachable}\}\), converging to the corresponding Dirac measures uniformly in \((x,a)\). Then, for a belief \(b\) carried by a set \(B \subseteq \mathcal{V}\), \(V_{k}(b) \to 1\) if \(B \in \mathcal{W}_{k}\) and \(V_{k}(b) \to 0\) otherwise.
\end{proposition}

\emph{Proof.} On the finite simplex product, value iteration is continuous in \((T, g)\) uniformly in \((x,a)\). At the limit the posterior support is exactly the set-valued post-state \(\mathrm{Post}(B, a, y)\) of Section 3.5, and the recursion becomes \(V_{k+1}(B) = \max_{a} \min_{y \text{ possible}} V_{k}(\mathrm{Post}(B,a,y))\) with \(V_{0}(B) = 1\); by Theorem~\ref{thm:finite-horizon} its value is the indicator of \(B \in \mathcal{W}_{k}\). \hfill\(\square\)

Proposition~\ref{prop:degenerate} is the sense in which the chance-constrained obstruction degenerates to the common-action obstruction: at the deterministic limit \(V_{1}(b) = 1\) exactly when some action keeps every branch of the support in \(\mathcal{V}\), i.e.\ when the common safe-action set is nonempty. It is a finite-model statement; a continuous-state limit requires uniform concentration of the kernels, which is not developed here.

"""

# insert the new sections before the conclusion and renumber the conclusion
assert "\\subsection{7. Conclusion}\\label{conclusion}" in main
main = main.replace("\\subsection{7. Conclusion}\\label{conclusion}",
                    NEW_SECTIONS + "\\subsection{10. Conclusion}\\label{conclusion}", 1)

# update the organization paragraph
org_old = ("Section 7 concludes. Proof sketches are given in the main text; the complete proofs, "
           "the expanded sufficiency review, and the auxiliary constructions are collected in the "
           "Supplementary Material.")
org_new = ("Sections 7--9 develop the new material: complete characterizations and the residual gap "
           "(Section 7), a calibrated case study with a coverage audit (Section 8), and the probabilistic "
           "belief-state development (Section 9). Section 10 concludes. Proof sketches of the Section 3 "
           "results are given in the main text; the complete proofs, the expanded sufficiency review, and "
           "the auxiliary constructions are collected in the Supplementary Material.")
assert org_old in main, "organization sentence not found"
main = main.replace(org_old, org_new, 1)

# extend the conclusion with a pointer to the three routes
concl_old = "into a design\nspecification."
concl_new = ("into a design\nspecification. Three extensions complete the picture: the certificates are "
             "complete in the one-step and static-observation classes, with the residual dynamic gap stated "
             "as an open problem (Section 7); a calibrated case study and a coverage audit show the "
             "certificates reproducing the exact recursion verdict on a grid of delayed hidden-regime systems "
             "(Section 8); and the probabilistic belief-state lift connects the calculus to the partially "
             "observable control literature (Section 9).")
assert concl_old in main, "conclusion ending not found"
main = main.replace(concl_old, concl_new, 1)

# add the two new references (alphabetically placed)
astr = r"\r{A}str\"om, K.J.: Optimal control of Markov processes with incomplete state information. J. Math. Anal. Appl. \textbf{10}, 174--205 (1965)"
clark = r"Clark, C.W.: Mathematical Bioeconomics: The Optimal Management of Renewable Resources, 2nd edn. Wiley, New York (1990)"
assert "Abaee, A.: The limits of compensatory aggregation" in main
main = main.replace("Abaee, A.: The limits of compensatory aggregation",
                    astr + "\n\nAbaee, A.: The limits of compensatory aggregation", 1)
assert "De Lara, M., Doyen, L.: Sustainable Management" in main
main = main.replace("De Lara, M., Doyen, L.: Sustainable Management",
                    clark + "\n\nDe Lara, M., Doyen, L.: Sustainable Management", 1)

open(MAIN, "w", encoding="utf-8").write(main)
print(f"wrote {MAIN} ({len(main)} bytes)")

# ----------------------------------------------------------------------------
# Build the SUPPLEMENTARY file
# ----------------------------------------------------------------------------
supp_preamble = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{amsthm}
\theoremstyle{definition}
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}
\newtheorem{corollary}{Corollary}
\newtheorem{remark}{Remark}
\newtheorem{example}{Example}
\newtheorem{definition}{Definition}
\usepackage{graphicx}
\usepackage{booktabs,array,calc}
\usepackage[font=small,labelfont=bf]{caption}
\usepackage[colorlinks=true]{hyperref}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\setcounter{secnumdepth}{-1}
\emergencystretch=3em

\begin{document}

\title{Supplementary Material: An Obstruction Calculus for Viability under Incomplete Observation}
\author{Amin Abaee}
\maketitle

"""

supp = supp_preamble
supp += ("This supplement collects the material condensed from the main text: the complete proofs (S1), the "
         "expanded sufficiency review (S2), the bounded constructions and scope remarks (S3), and three "
         "additional figures (S4). Notation and numbering follow the main text.\n\n")

supp += "\\section*{S1. Complete proofs}\n\n"
for (env, lab), st, pf in zip(RESULTS, statement_full, proof_full):
    supp += st + "\n\n" + pf + "\n\n"

supp += "\\section*{S2. The sufficiency landscape (full)}\n\n"
supp += extract_span(t, "\\subsection{5. The Sufficiency Landscape}\\label{the-sufficiency-landscape-cited}",
                     "\\subsection{6. Discussion}\\label{discussion}") + "\n"

supp += "\\section*{S3. Bounded constructions and scope remarks}\n\n"
supp += extract_span(t, "\\subsection{Appendix A: Bounded Constructions and Scope",
                     "\\subsection{References}") + "\n"

supp += "\\section*{S4. Additional figures}\n\n"

def get_figure(txt, filename):
    key = f"figs_p2/{filename}"
    i = txt.index(key)
    s = txt.rfind("\\begin{figure}", 0, i)
    e = txt.index("\\end{figure}", i) + len("\\end{figure}")
    return txt[s:e]

supp += get_figure(t, "fig_p2_ladder.png").replace("width=0.92\\linewidth", "width=0.75\\linewidth") + "\n\n"
supp += get_figure(t, "fig_p2_obstruction_tree.png") + "\n\n"
supp += get_figure(t, "fig_p2_ce_trap.png") + "\n\n"

supp += ("\\section*{Auxiliary definitions and remarks (for reference)}\n\n" +
         "\n\n".join(extra_full) + "\n\n")

supp += "\\subsection{References}\\label{references}\n\n"
refs = t[t.index("\\subsection{References}\\label{references}"):]
refs = refs[:refs.index("\\section*{Declarations}")]
supp += refs + "\n\\end{document}\n"

open(SUPP, "w", encoding="utf-8").write(supp)
print(f"wrote {SUPP} ({len(supp)} bytes)")
print("proof blocks extracted:", len(proof_full))

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
MAIN = f"{LATEX}/paper2_obstruction_calculus_v29_Automatica_condensed.tex"
SUPP = f"{LATEX}/paper2_obstruction_calculus_v29_supplementary.tex"

t = open(SRC, encoding="utf-8").read()

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
     "open-loop control. (H4.2), applied to it, supplies a compatible state \\(x^*\\) with "
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
    "policy exists --- finite in the polyhedral and finite-fibre cases --- and the argument it makes is that "
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

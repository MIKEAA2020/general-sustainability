#!/usr/bin/env python3
"""make_v53_p1.py — build paper1_assessment_separation_v53.tex from v52.

Task 107 / batch 8 / paper 1. The owner-gated v53 implementation wave:
the 42-point queue (BATCH8_PAPER1_ECOLOGICAL_INDICATORS_JOINT_ASSESSMENT.md
§3, as re-verified by QUEUE_REVERIFICATION_AND_PLAN.md Part B and enriched
by BATCH8_PAPER1_CROSS_PAPER_CONSISTENCY_CHECK.md §6), under the standing
rules: new version only (never overwrite), no content removed or condensed,
fail-loud anchored edits, math-span multiset preservation, idempotent.

Exit code 0 on success; any failed gate exits nonzero with a loud message.
"""
import sys
from pathlib import Path
from collections import Counter

HERE = Path(__file__).resolve().parent
LATEX = HERE.parents[1] / "arena agent 1" / "paper rewrites" / "latex"
SRC = LATEX / "paper1_assessment_separation_v52.tex"
DST = LATEX / "paper1_assessment_separation_v53.tex"

def die(msg: str):
    print(f"FAIL: {msg}")
    sys.exit(1)

text = SRC.read_text(encoding="utf-8")
orig = text
PAIRS = []   # (name, pos, anchor, repl) for every operation
STATES = []  # the full text after each edit (drives the inverse gate)

def edit(name: str, anchor: str, repl: str, count: int = 1):
    global text
    n = text.count(anchor)
    if n != count:
        die(f"anchor [{name}] found {n}x (expected {count}):\n---\n{anchor[:200]}\n---")
    pos = text.index(anchor)
    text = text[:pos] + repl + text[pos + len(anchor):]
    PAIRS.append((name, pos, anchor, repl))
    STATES.append(text)
    print(f"  ok  {name}")

def insert_after(name: str, anchor: str, block: str):
    edit(name, anchor, anchor + block)

def insert_before(name: str, anchor: str, block: str):
    edit(name, anchor, block + anchor)

print("== mechanical pass (queue 3.C) ==")
# 28a: one \emergencystretch (keep the operative 3em at line 15)
edit("3.C-28a emergencystretch",
     "\\emergencystretch=2.5em\n\\usepackage{amsmath,amssymb}",
     "\\usepackage{amsmath,amssymb}")
# 28b: mailto underscore unescaped in the URL argument only
edit("3.C-28b mailto",
     "\\href{mailto:amin\\_abaee@ut.ac.ir}{amin\\_abaee@ut.ac.ir}",
     "\\href{mailto:amin_abaee@ut.ac.ir}{amin\\_abaee@ut.ac.ir}")
# 25a: Dasgupta & Mäler before De Lara & Doyen
edit("3.C-25a Dasgupta/De Lara ordering",
     "De Lara, M., and Doyen, L. (2008). \\emph{Sustainable Management of Natural Resources: Mathematical Models and Methods}. Springer, Berlin.\n\nDasgupta, P., and M\\\"aler, K.-G. (2000). Net national product, wealth, and\nsocial well-being. \\emph{Environment and Development Economics}, 5(1),\n69--93.",
     "Dasgupta, P., and M\\\"aler, K.-G. (2000). Net national product, wealth, and\nsocial well-being. \\emph{Environment and Development Economics}, 5(1),\n69--93.\n\nDe Lara, M., and Doyen, L. (2008). \\emph{Sustainable Management of Natural Resources: Mathematical Models and Methods}. Springer, Berlin.")
# 25b: O'Neill before Raworth before Rockström
edit("3.C-25b O'Neill/Rockström ordering",
     "Rockstr\\\"om, J., Steffen, W., Noone, K., et al. (2009). A safe operating\nspace for humanity. \\emph{Nature}, 461, 472--475.\n\nO'Neill, D. W., Fanning, A. L., Lamb, W. F., and Steinberger, J. K. (2018). A good life for all within planetary boundaries. \\emph{Nature Sustainability}, 1(2), 88--95.\n\nRaworth, K. (2012). A safe and just space for humanity: Can we live within the doughnut? \\emph{Oxfam Policy and Practice: Climate Change and Resilience}, 8(1), 1--26.",
     "O'Neill, D. W., Fanning, A. L., Lamb, W. F., and Steinberger, J. K. (2018). A good life for all within planetary boundaries. \\emph{Nature Sustainability}, 1(2), 88--95.\n\nRaworth, K. (2012). A safe and just space for humanity: Can we live within the doughnut? \\emph{Oxfam Policy and Practice: Climate Change and Resilience}, 8(1), 1--26.\n\nRockstr\\\"om, J., Steffen, W., Noone, K., et al. (2009). A safe operating\nspace for humanity. \\emph{Nature}, 461, 472--475.")
# 25c: Saint-Pierre before Schaefer before Schär
edit("3.C-25c Saint-Pierre/Schaefer/Schär ordering",
     "Schaefer, M. B. (1954). Some aspects of the dynamics of populations important to the management of commercial marine fisheries. \\emph{Inter-American Tropical Tuna Commission Bulletin}, 1(2), 23--56.\n\nSaint-Pierre, P. (1994). Approximation of the viability kernel.\n\\emph{Applied Mathematics and Optimization}, 29, 187--209.",
     "Saint-Pierre, P. (1994). Approximation of the viability kernel.\n\\emph{Applied Mathematics and Optimization}, 29, 187--209.\n\nSchaefer, M. B. (1954). Some aspects of the dynamics of populations important to the management of commercial marine fisheries. \\emph{Inter-American Tropical Tuna Commission Bulletin}, 1(2), 23--56.")
# 26: §4.9 proof-list completion
edit("3.C-26 proof-list completion",
     "Proposition 3, Proposition 4, Theorem 5, Remark 7, and Theorems 8--9\nare proved in Appendices A--C.",
     "Proposition 3, Proposition 4, Theorem 5, Theorem 6, Remark 7, Theorems\n8--9, and Proposition 10 are proved in Appendices A--C, and Proposition 11\nin Appendix C.")
# 27: Theorem 9's qed outside the final enumerate item
edit("3.C-27 Thm-9 qed placement",
     "Immediate from the window's state dependence and from typed\n  admissibility implying \\(w\\)-admissibility for every weight. \\ensuremath{\\square}\n\\end{enumerate}",
     "Immediate from the window's state dependence and from typed\n  admissibility implying \\(w\\)-admissibility for every weight.\n\\end{enumerate}\n\n\\ensuremath{\\square}")

print("== precision pass (queue 3.B) ==")
# 16: abstract margin-reducible qualifier
edit("3.B-16 abstract margin-reducible",
     "A general geometric result characterizes the gap for any finite menu of\nplans: it is the part of the convex hull of the plans' required margins\nthat no single plan dominates.",
     "A general geometric result characterizes the gap for any finite menu of\nmargin-reducible plans: it is the part of the convex hull of the plans'\nrequired margins that no single plan dominates.")
# 18: abstract rescuable/impossible append
edit("3.B-18 abstract rescuable/impossible",
     "--- the aggregate alone cannot tell the rescuable from the\nimpossible.\n",
     "--- the aggregate alone cannot tell the rescuable from the\nimpossible without separately checking the floors or verifying a common\nimplementable plan.\n")
# 19: left comparatively open
edit("3.B-19 comparative-open softening",
     "This paper addresses a question that the indicator literature has left\ncomparatively open: the \\emph{dynamic} question.",
     "This paper addresses a question that is less explicit in much of the\ncomposite-indicator literature: the \\emph{dynamic} question.")
# 17: no choice of weights protocol qualifier
edit("3.B-17 weights-repairs qualifier",
     "The stronger possibility, established here, is that no choice of weights repairs the difficulty.",
     "The stronger possibility, established here, is that no choice of weights repairs the difficulty under the per-weight, weight-adaptive certification protocol.")
# 20: index green -> index nonnegative
edit("3.B-20 index nonnegative",
     "hidden collapse zone: index green, floor crossed mid-transition",
     "hidden collapse zone: index nonnegative, floor crossed mid-transition")
# 21: endpoint-operator generalization
edit("3.B-21 endpoint-operator generalization",
     "The endpoint operator represents aggregated accounting evaluated on audited snapshots, while typed floors constrain the whole trajectory:",
     "The endpoint operator represents any assessment architecture that evaluates constraints only at sampled or audited endpoints, while typed floors constrain the whole trajectory:")
# 22: FP_agg first-definition qualifier
edit("3.B-22 FP_agg qualifier",
     "\\(\\mathrm{FP}_{\\mathrm{agg}} = \\mathcal{V}_{\\mathrm{weak}} \\setminus \\mathcal{V}_{\\mathrm{typ}}\\)\n--- the genuine compensatory-versus-noncompensatory acceptance gap.",
     "\\(\\mathrm{FP}_{\\mathrm{agg}} = \\mathcal{V}_{\\mathrm{weak}} \\setminus \\mathcal{V}_{\\mathrm{typ}}\\)\n--- the genuine compensatory-versus-noncompensatory acceptance gap,\nrelative to the typed criterion and the specified menu.")
# 24: critical-zone precision
edit("3.B-24 critical-zone both comparisons",
     "kt) lies inside the\ncritical zone where the stock in fact resided after the collapse --- about a\nthird of the LRP in 2015 (DFO, 2016) --- and the adverse plan's",
     "kt) lies below the LRP while remaining above the stock's 2015\nassessed level of about a third of the LRP (\\(\\approx 295\\) kt; DFO,\n2016) --- the zone between the two levels, in which the stock in fact\nresided after the collapse --- and the adverse plan's")

print("== additive pass (queue 3.A) ==")
# --- 7/13: positioning in-text uses ---
edit("3.A-7/13 Fischer in-text",
     "weights they embed are value judgements presented as measurement\n(Hickel, 2020; Martinez-Alier, Munda, and O'Neill, 1998). The critique",
     "weights they embed are value judgements presented as measurement\n(Hickel, 2020; Martinez-Alier, Munda, and O'Neill, 1998; Fischer et al.,\n2022). The critique")
edit("3.A-7/13 Becker+Nardo in-text",
     "The critique\ntypically targets the \\emph{choice} of weights.",
     "The critique\ntypically targets the \\emph{choice} of weights; the methodology of that\nchoice is itself a developed field (Nardo et al., 2008), and the\nweights-versus-importance distinction it has produced is part of good\ncomposite-indicator practice (Becker et al., 2017). What is established\nbelow is orthogonal to both: even if weights perfectly reflect importance,\nthe quantifier order can still produce the gap.")
edit("3.A-13 De Lara & Doyen + Doyen 2012 in-text",
     "(Aubin, 1991;\nAubin, Bayen, and Saint-Pierre, 2011; Saint-Pierre, 1994; Lygeros,\nTomlin, and Sastry, 1999); the fixed-point and algebraic character of these objects is developed in Aubin and Catt\\'e (2002).",
     "(Aubin, 1991;\nAubin, Bayen, and Saint-Pierre, 2011; Saint-Pierre, 1994; Lygeros,\nTomlin, and Sastry, 1999); the fixed-point and algebraic character of these objects is developed in Aubin and Catt\\'e (2002). Viability methods are likewise developed in natural-resources management, with fisheries a canonical application (De Lara and Doyen, 2008; Doyen et al., 2012).")
edit("3.A-13 Rockström+Raworth in-text",
     "Critical-natural-capital frameworks may use thresholds, safe\noperating spaces, irreversibility, resilience, or minimum-service\nconditions (Ekins et al., 2003; Doyen and Gajardo, 2020).",
     "Critical-natural-capital frameworks may use thresholds, safe\noperating spaces, irreversibility, resilience, or minimum-service\nconditions (Ekins et al., 2003; Rockstr\\\"om et al., 2009; Raworth, 2012;\nDoyen and Gajardo, 2020).")
edit("3.A-13 Raworth at the doughnut sentence",
     "reports that no country satisfies all floors within all ceilings (O'Neill et al., 2018; Fanning et al., 2022).",
     "reports that no country satisfies all floors within all ceilings (Raworth, 2012; O'Neill et al., 2018; Fanning et al., 2022).")
# 29b: PROMETHEE natural use
edit("3.C-29b PROMETHEE natural use",
     "the compensability mapping\nin multi-criteria decision analysis (Cinelli, Coles, and Kirwan, 2014;\nSch\\\"ar, Pohl, and Geldermann, 2025)",
     "the compensability mapping\nin multi-criteria decision analysis --- including the outranking approach\nPROMETHEE, whose compensatory properties the cited analysis dissects\n(Cinelli, Coles, and Kirwan, 2014; Sch\\\"ar, Pohl, and Geldermann, 2025)")
# 29a: MSY natural use
edit("3.C-29a MSY natural use",
     "sustained-yield quota \\(\\sigma(16/5) = 1088/125 \\approx 8.7\\) kt/yr; STAGED",
     "sustained-yield quota \\(\\sigma(16/5) = 1088/125 \\approx 8.7\\) kt/yr ---\nitself below the model's maximum sustainable yield (MSY) of\n\\(\\sigma(K/2) = rK/4 = 10\\) kt/yr at \\(B = K/2\\); STAGED")
# 30: Fig 1 caption consistency sentence
edit("3.C-30 Fig-1 caption sentence",
     "FAST-only for \\(r > \\rho_2\\).}",
     "FAST-only for \\(r > \\rho_2\\). The reserve bars mark representative\nslice values (Panel A: \\(x = 0\\), the impossibility-slice representative;\nPanel B: \\(x = 1\\), at the rescue threshold); the dip arrows are\n\\(x\\)-independent (the floor dynamics do not involve the reserve), and the\ncanonical witness point of Sections 4.6 and 6.3 sits at \\(x = \\tfrac12\\),\nbetween the drawn slices.}")
# 31: presentation note before Theorem 5
insert_before("3.C-31 Thm-5/6 presentation note",
              "\\textbf{Theorem 5 (witnessed separation).}",
              "\\noindent\\textit{Presentation note.} Theorem 6 of Section 4.4 is stated\nbefore the present theorem but carries the larger number: this paper's\nstatements share one counter assigned in citation order, so the numbering\nis non-sequential in presentation order. No content depends on the\nordering; Theorem 6 is the general finite-menu form and Theorem 5 its\nwitness instantiation.\n\n")

# --- 1 + 3: the four-protocol table and the interpretation box (§1.2) ---
PROTOCOLS = """
To isolate this mechanism, the assessment protocols an indicator can serve
must be distinguished from the indicator itself.
Table~\\ref{tab:protocols} collects the four protocols in play; the
separation studied in this paper is specifically Protocol 2 versus
Protocol 4 --- a statement about the certification protocol applied to a
composite index, not an objection to composite indices as such (Protocol
1, at a fixed declared weight, is ordinary fixed-weight assessment, and
Protocol 3 collapses into Protocol 4 by the full-cone identity of
Proposition 3(ii)).

\\begin{table}[htbp]
\\centering
\\small
\\caption{Four assessment protocols for a composite index on a transition
datum. The separation studied in this paper is Protocol 2 versus Protocol
4.}
\\label{tab:protocols}
\\begin{tabular}{@{}p{3.9cm}p{3.4cm}p{6.1cm}@{}}
\\toprule
Protocol & Quantifier form & Reading \\\\
\\midrule
1. Fixed-weight assessment & \\(a \\in E_w(z)\\) at a declared \\(w\\) & one index, one selected plan: ordinary fixed-weight certification \\\\
2. Weight-adaptive (per-weight) acceptance & \\(\\forall w\\; \\exists a_w \\in E_w(z)\\) & every weighting can be paired with some plan, possibly weighting-dependent: the compensatory reading; \\(\\mathcal{V}_{\\mathrm{weak}} = \\bigcap_w \\mathcal{V}_w\\) \\\\
3. Common-plan robustness & \\(\\exists a\\; \\forall w:\\; a \\in E_w(z)\\) & one plan serves every weighting; equals the typed operator on the full cone (Proposition 3(ii)) \\\\
4. Coordinate-wise (typed) acceptance & \\(\\exists a: a \\in E_{\\mathrm{typ}}(z)\\) & separately binding floors enforced path-wise: the noncompensatory reading \\\\
\\bottomrule
\\end{tabular}
\\end{table}

\\medskip

\\noindent\\textbf{Where the failure is not.} Static scalarization is not the
source of the counterexample: at any fixed trajectory the full-cone
aggregate detects every component violation (Remark 2), and on a fixed
action the typed operator is exactly the common-plan set over the full
cone (Proposition 3(ii)). The failure studied here appears one level up
--- between protocols --- because different weights may select different
trajectories: the quantifier order, not the scalarization, is the seat of
the separation (Sections 4.5--4.6).

"""
insert_after("3.A-1+3 protocol table + interpretation box",
             "\\[\\forall w\\; \\exists a_w:\\; a_w \\in E_w(z).\\]\n\\end{itemize}",
             PROTOCOLS)

# --- 2: the evaluation-semantics table (§3.1) ---
SEMANTICS = """

\\medskip

\\noindent The five operators differ along two axes --- what is
constrained, and where it is evaluated --- and the two axes organize them
(Table~\\ref{tab:semantics}). The second axis is what endpoint-only
reporting regimes collapse (the fourth implication of Section 5.6).

\\begin{table}[htbp]
\\centering
\\small
\\caption{Evaluation semantics: constraint structure (rows) by evaluation
locus (columns). The scalarized-endpoint cell is not isolated in this
paper; the endpoint chain of Section 3.1 covers the physical and typed
extremes.}
\\label{tab:semantics}
\\begin{tabular}{@{}p{3.4cm}p{4.6cm}p{4.6cm}@{}}
\\toprule
 & \\textbf{Evaluated on the full tube} & \\textbf{Evaluated at endpoints only} \\\\
\\midrule
\\textbf{Typed floors} & \\(E_{\\mathrm{typ}}\\) --- typed path safety & \\(E_{\\mathrm{end,typ}}\\) --- typed snapshots \\\\
\\textbf{Scalarized floor} & \\(E_w\\) --- scalarized path safety & --- (not isolated here) \\\\
\\textbf{Physical constraints} & \\(E_{\\mathrm{tube,phys}}\\) --- physical viability & \\(E_{\\mathrm{end}}\\) --- audited physical snapshots \\\\
\\bottomrule
\\end{tabular}
\\end{table}
"""
insert_after("3.A-2 evaluation-semantics table",
             "the photograph admits what the trajectory forbids.",
             SEMANTICS)

# --- 15: the pre-Theorem-9 limitation paragraph (§4.10) ---
BLENDLIMIT = """
\\noindent\\textbf{A limitation to state before the theorem.} The blend
family is an explicitly defined convexified control map --- an instrument
of the abstract witness datum, not by itself a claim that fractional plans
are available anywhere. Convexification must be demonstrated from the
model equations (as here, by linearity of the flow map in the control) or
carried explicitly as a management assumption; and a blended control
requires physical and institutional implementability --- fractional
allocation of effort, quota, or seasonal resolution, with monitoring and
enforcement --- before Theorem 9 is applied to a real plan menu. The
theorem is a statement about certification relative to the convexified
menu; the menu's availability is external data (the fourth design test of
Section 5.5 and the instruments of Section 5.6).

"""
insert_before("3.A-15 pre-Thm-9 limitation paragraph",
              "\\textbf{Theorem 9 (blend collapse).}",
              BLENDLIMIT)

# --- 5.1: Rockström/Raworth done above; the CES forward pointer ---
edit("3.A-8 CES forward pointer",
     "Nonlinear aggregate indices --- CES-type substitutability or endogenous,\nstate-dependent weighting of the kind that diverges near zero-stock\nboundaries --- are different assessment operators, and the theorems\nclaim nothing for them.",
     "Nonlinear aggregate indices --- CES-type substitutability or endogenous,\nstate-dependent weighting of the kind that diverges near zero-stock\nboundaries --- are different assessment operators, and the theorems\nclaim nothing for them. Section~\\ref{substitutability-spectrum} begins the\nprogramme of establishing what can be claimed for the CES family on the\nwitness datum.")

# --- 6: the three-regime disturbance table (§5.4) ---
DISTURBANCE = """

\\medskip

\\noindent The disturbance-class scoping, organized
(Table~\\ref{tab:disturbance}): the witness's action-indexed separable
class is one of three regimes; the second is \\emph{not analysed} on this
datum --- its verdict must be computed, not asserted; the third is the
universal-rejection collapse stated above.

\\begin{table}[htbp]
\\centering
\\small
\\caption{Disturbance regimes on the witness datum. The middle row is
honestly open: no verdict is asserted for it in this paper.}
\\label{tab:disturbance}
\\begin{tabular}{@{}p{3.1cm}p{4.0cm}p{6.3cm}@{}}
\\toprule
Regime & Disturbance class & Separation status \\\\
\\midrule
(i) Action-indexed separable & each action's worst case is its own characteristic dip in the coordinate it moves (Section 4.5) & proven: the witness datum exhibits the acceptance gap (Theorem 5) \\\\
(ii) Common biomass shock & one shared shock strikes the same floor coordinate of every plan & \\emph{not analysed on this datum}: the verdict requires its own exact computation --- a common-shock variant of the witness --- not an assertion \\\\
(iii) Coupled all-floor shocks & simultaneous dips across all floors of every action & universal rejection: the per-weight licensing structure degenerates and the compensatory/noncompensatory divergence collapses into common rejection (this section; Lade et al., 2020, on boundary interactions) \\\\
\\bottomrule
\\end{tabular}
\\end{table}
"""
insert_after("3.A-6 three-regime disturbance table",
             "amplify one another (Lade et al., 2020).",
             DISTURBANCE)

# --- 4 + 5: the indicator-validity section and the checklist (new §5.5) ---
VALIDITY = """\\subsection{Indicator validity: four design tests}\\label{indicator-validity}

The separation theorem implies that a composite indicator can be
statically lossless yet dynamically unsound as a
transition-certification device. For indicator developers the theorem
converts into four design tests --- the questions an indicator's
documentation must answer before the index is used to certify a
transition. Each test is a reading of a proved statement; none is a
heuristic.

\\begin{enumerate}
\\tightlist
\\item
  \\textbf{Static losslessness.} Does the aggregate preserve component
  violations at a fixed trajectory for the declared weight family? At the
  full cone, yes (Remark 2); for a restricted family, the test is to
  characterize the component violations the restricted family can miss
  (Proposition 4). An index that fails this test fails statically; the
  separation of Section 4 is the further, dynamic failure.
\\item
  \\textbf{Protocol quantifiers.} Does the certification rule require a
  common plan (\\(\\exists a\\, \\forall w\\)) or permit weight-adaptive plan
  selection (\\(\\forall w\\, \\exists a_w\\))? If the latter --- Protocol 2
  of Table~\\ref{tab:protocols} --- the indicator is exposed to the
  acceptance gap on exactly the region Theorem 5 exhibits.
\\item
  \\textbf{Path-wise observability.} Is the index evaluated along the
  full tube, or only at audited endpoints? Endpoint evaluation is the
  weakest operator of the chain (Section 3.1) and cannot detect transient
  breaches --- mid-interval floor crossings that are invisible at
  snapshots (\\(E_{\\mathrm{end,typ}}\\) versus \\(E_{\\mathrm{typ}}\\) on
  the witness datum).
\\item
  \\textbf{Menu completeness and convexity.} Is the plan menu exhaustive,
  and are blended (convexified) plans implementable? Negative feasibility
  verdicts are menu-relative (Section 5.4), and the gap is a property of
  the deterministic menu that convexification collapses exactly (Theorem
  9, Proposition 10); the availability of the convexified menu is
  external data that the indicator's documentation must declare.
\\end{enumerate}

\\textbf{A consolidated practitioner checklist.} For an agency using a
composite dashboard to certify a sustainability transition, the four
tests and the theorems behind them operationalize as ten audit points:

\\begin{enumerate}
\\tightlist
\\item
  \\textbf{Object of certification:} state what is being certified --- a
  static state, an endpoint, or the existence of a path-wise safe
  management plan.
\\item
  \\textbf{Binding floors:} list the floors that are legally binding,
  irreversible, or lack verified substitutability; these require
  noncompensatory (Protocol 4) treatment.
\\item
  \\textbf{Policy quantifier:} declare whether the approval rule assumes
  one robust plan or lets the plan adapt to the weighting.
\\item
  \\textbf{Weight-dependent plans:} if weight-adaptive, report the
  management plan associated with each relevant weight range (the
  licensing thresholds \\(\\rho_1, \\rho_2\\) of Theorem 5(6) are the
  pattern).
\\item
  \\textbf{Path-wise evaluation:} evaluate the floors along the full
  transition, not only at assessment snapshots (the endpoint operators
  are the weakest of the chain; Section 3.1).
\\item
  \\textbf{Disturbance structure:} specify whether shocks are common to
  all plans, action-indexed, or correlated across floors
  (Table~\\ref{tab:disturbance}); the separation's scope rides on the
  class.
\\item
  \\textbf{Menu completeness:} acknowledge that negative feasibility
  results are menu-relative unless the action space is demonstrably
  exhaustive (Section 5.4).
\\item
  \\textbf{Blended policies:} do not infer convexification from
  mathematical convenience; verify that fractional effort or quota
  allocation is administratively implementable (the limitation stated
  before Theorem 9).
\\item
  \\textbf{Rescue margins:} if a resource-controlled action exists, report
  the minimum increment \\(\\kappa^*\\) that converts impossibility into
  rescue (Section 5.7).
\\item
  \\textbf{Mandatory reporting:} require that component trajectories and
  their minimum margins be reported alongside the aggregate index, so the
  typed verdict can be independently reconstructed (the minimum report of
  Section 5.6).
\\end{enumerate}

"""
insert_before("3.A-4+5 validity section + checklist",
              "\\subsection{Policy implications}\\label{policy-implications}",
              VALIDITY)

# --- section renumbering: 5.6 -> 5.7 (five hardcoded references) ---
edit("renumber rescue ref (§1)",
     "The rescue operation of\nSection 5.6 --- resource augmentation --- acts on the impossibility",
     "The rescue operation of\nSection 5.7 --- resource augmentation --- acts on the impossibility")
edit("renumber rescue ref (contributions)",
     "(Proposition 11, Section 5.6)",
     "(Proposition 11, Section 5.7)")
edit("renumber rescue ref (§5.4 completeness)",
     "(see the completeness requirement in Section 5.6)",
     "(see the completeness requirement in Section 5.7)")
edit("renumber rescue ref (§5.6 policy)",
     "reweighting alone cannot substitute for it on the witness datum (Section 5.6)",
     "reweighting alone cannot substitute for it on the witness datum (Section 5.7)")
edit("renumber rescue ref (App C header)",
     "\\textbf{Proof of the rescue threshold (Section 5.6).}",
     "\\textbf{Proof of the rescue threshold (Section 5.7).}")

# --- 9: the institutional-forms paragraph (§5.7, EMS-aligned) ---
INSTITUTIONAL = """
\\textbf{Institutional forms.} The rescue margin \\(\\kappa^*(z) = 1 - x\\)
maps onto concrete transition-finance instruments: license buy-backs and
vessel decommissioning (the fund spends \\(c = 1\\) to remove effort),
transition assistance protecting the income floor during the staged
draw-down, and quota banking held against the staged rebuild. The
software companion --- the SafeTransition library --- realizes exactly
this menu on the benchmark datum, as a staged rebuild financed by a fund
buy-back with the rescue threshold truncated at zero once the fund covers
the cost (\\(\\kappa^* = \\max(0,\\, 1 - x)\\)). The mapping is a reading
aid, not a theorem: each institution must verify its own physical and
legal feasibility before the threshold is read as a financing requirement.

"""
insert_before("3.A-9 institutional forms",
              "\\textbf{Remark (error-bound modulus).}",
              INSTITUTIONAL)

# --- 10: conservatism-invalidation caveat (§6.1 limitations) ---
edit("3.A-10 conservatism caveat",
     "not a claim that the gap is unavoidable in every institution.\n\\item\n  No empirical claims are made.",
     "not a claim that the gap is unavoidable in every institution.\n\\item\n  Conservatism of the benchmark's certified tubes (Section 6.3) is\n  regime-conditional: the exact inequality that makes the tubes\n  conservative uses the Schaefer surplus's monotonicity below \\(K/2\\).\n  Depensation in the stock--recruitment relationship, or heatwave\n  mortality amplified nonlinearly at low stock, would reduce the recovery\n  surplus, and the certified tubes would then no longer be conservative\n  for the nonlinear realization; the certification statements of\n  Section 4, which concern the datum rather than the realization, are\n  unaffected.\n\\item\n  No empirical claims are made.")

# --- 11: dashboard-only disclaimer (§6.3) ---
edit("3.A-11 dashboard disclaimer",
     "the reviewer checks the dashboard, not the\nfloors.",
     "the reviewer checks the dashboard, not the\nfloors. This is a deliberately adverse reporting architecture, adopted to\nisolate the assessment-operator issue --- not a claim about current\nfisheries assessment practice, in which a limit-reference-point breach\ntriggers a mandatory management response.")

# --- 23 + 14: unit convention + motivation paragraph (§6.3) ---
edit("3.A-23+14 motivation paragraph with exact values",
     "Three qualifications apply.",
     "\\textbf{The motivation, with the assessed numbers.} The anchoring\nstatements of this subsection, made precise: the limit reference point of\nthe assessed NCAM M-shift series is \\(884.6\\) kt --- by construction the\n1983--1989 mean spawning-stock biomass of that series (DFO, 2016, Table\nA2); the stock's assessed 2015 level is \\(33.8\\%\\) of that LRP (the\nadvisory report's ``about a third''), \\(\\approx 299\\) kt; the decline\nfrom the mid-1980s neighbourhood of the benchmark's opening stock\n(\\(\\approx 1.42\\) Mt) to the 2015 level is a swing of \\(\\approx 1.1\\)\nMt, about \\(1.3\\) LRP units; and the benchmark's adverse worst-case\nexcursion --- one full LRP unit --- is therefore of the assessed order,\nwith its trough (\\(0.6\\) LRP) inside the assessed post-collapse band\n\\((0.34, 1)\\) LRP units. The unit convention is explicit throughout:\n\\(s_1\\) is a kt margin above \\(B_{\\mathrm{lim}}\\), so the opening\nstock is \\(B(0) = B_{\\mathrm{lim}} + 6/5 = 16/5\\) kt, the normalized\nstock is \\(b(0) = B(0)/B_{\\mathrm{lim}} = 8/5 = 1.6\\) LRP units, and the\nmargin \\(6/5\\) kt is not itself a biomass ratio.\n\nThree qualifications apply.")

# --- 7: the fisheries translation table (§6.3) ---
FISHERIES = """

\\medskip

\\noindent Table~\\ref{tab:fisheries} completes the translation guide of
Table~\\ref{tab:translation} into the benchmark's own vocabulary: each of
the paper's central objects read as the fisheries quantity of this
section.

\\begin{table}[htbp]
\\centering
\\small
\\caption{The translation guide (Table~\\ref{tab:translation}) extended to
the fishery benchmark's own quantities.}
\\label{tab:fisheries}
\\begin{tabular}{@{}p{4.1cm}p{9.4cm}@{}}
\\toprule
Object & Fisheries reading (this section) \\\\
\\midrule
Typed floors \\(s_i \\ge 0\\) & the spawning-stock margin above the limit reference point (\\(B - B_{\\mathrm{lim}} \\ge 0\\); the LRP convention) and the fleet income margin net of costs \\\\
Scalarized operator \\(E_w\\) & the assessment dashboard \\(w \\cdot (s_1, s_2)\\) the reviewer checks \\\\
Licensing thresholds \\(\\rho_1, \\rho_2\\) & weight-ratio licensing intervals for the pulse (FAST) and gradual (SLOW) quota plans \\\\
Acceptance gap \\(\\mathrm{FP}_{\\mathrm{agg}}\\) & dashboard-certified yet LRP-breaching transitions (the index-blindness zone: trough \\(0.6\\) LRP units while the dashboard reads \\(2/5 > 0\\)) \\\\
Rescue set \\(R\\); threshold \\(\\kappa^*\\) & the adjustment fund financing fleet buy-down (STAGED at cost \\(c = 1\\); the shortfall \\(\\kappa^* = 1 - x\\)) \\\\
Impossibility region \\(I\\) & underfunded transitions: fund \\(x < 1\\), both margins below their plan margins, dashboard still certified \\\\
Blend collapse vs.\\ time-sharing & fractional quota/effort allocation (convexification) vs.\\ pulse/gradual season alternation \\\\
Exact-tube semantics & no transient LRP breach along the transition, the mid-season heatwave included \\\\
\\bottomrule
\\end{tabular}
\\end{table}
"""
insert_after("3.A-7 fisheries translation table",
             "(Figure~\\ref{fig:benchmark}).",
             FISHERIES)

# --- 8: the σ-spectrum labelled-extension subsection (new §5.8) ---
SIGMA = """\\subsection{The substitutability spectrum on the witness datum (a
labelled extension)}\\label{substitutability-spectrum}

Section 5.1 closes by conceding the nonlinear territory: CES-type
substitutability aggregates are different assessment operators, and the
theorems of Section 4 claim nothing for them. This subsection --- a
labelled extension, not a part of the separation theorem --- begins the
programme of establishing what \\emph{can} be claimed, on the witness
datum only, with exact rational witnesses throughout. Its results are
stated on the datum of Section 4.5 and inherit all of its scope
delimitations (Section 5.4); nothing here is an empirical claim.

\\textbf{Notation.} Throughout this subsection \\(\\sigma\\) denotes the
elasticity of substitution of a CES aggregate, \\(\\sigma = 1/(1-\\theta)\\)
with \\(\\theta\\) the CES exponent. This \\(\\sigma\\) is distinct from
the Schaefer surplus \\(\\sigma(B)\\) of Section 6.3, from the weight
ratios \\(\\rho_1, \\rho_2\\) (which are weight quotients, not
elasticities), and from the \\(\\sigma\\)-notations of the companion
papers --- the timing certificate \\(\\sigma^*(B_0)\\) of the
obstruction-calculus companion (Abaee, 2026, \\emph{An Obstruction
Calculus for Viability under Incomplete Observation}) and the flow shares
\\(\\sigma_f, \\sigma_c\\) of the two-land biocapacity companion (Abaee,
2026, \\emph{How Aggregation Can Conceal Composition}).

\\textbf{The family.} Work in floor-referenced indices
\\(\\lambda_i = 1 + s_i\\) --- \\(\\lambda_i = 1\\) exactly at the floor,
\\(\\lambda_i \\le 0\\) a full floor-unit below it --- the currency in
which geometric-mean abundance indices are defined. For weights normalized
to sum to one, consider the CES/power means
\\[M_\\theta(\\lambda; w) = \\Big( \\textstyle\\sum_i w_i \\lambda_i^\\theta \\Big)^{1/\\theta},
\\qquad \\sigma = \\frac{1}{1-\\theta},\\]
and evaluate Protocol 2 of Table~\\ref{tab:protocols} under the
\\(\\theta\\)-aggregate: a state is accepted when, for every weight, some
plan of the Section 4.5 menu keeps \\(M_\\theta \\ge 1\\) along its
worst-case tube (the physical and destination constraints are
aggregator-independent; STAGED needs \\(x \\ge 1\\) and then serves every
weight at every rung). Table~\\ref{tab:sigmafamily} situates the members.

\\begin{table}[htbp]
\\centering
\\small
\\caption{The CES family on floor-referenced indices, on the witness
datum. The linear member is the paper's own engine (Lemma A); the
Leontief member is the typed operator.}
\\label{tab:sigmafamily}
\\begin{tabular}{@{}llp{7.4cm}@{}}
\\toprule
\\(\\theta\\) & \\(\\sigma\\) & reading \\\\
\\midrule
\\(1\\) & \\(\\infty\\) & the linear aggregate --- the paper's own compensatory engine (Lemma A) \\\\
\\(2/3\\) & \\(3\\) & intermediate CES \\\\
\\(1/2\\) & \\(2\\) & intermediate CES \\\\
\\(0\\) & \\(1\\) & the geometric mean --- the Living Planet Index functional structure (the identification, below) \\\\
\\(-1\\) & \\(1/2\\) & the harmonic mean \\\\
\\(-m\\) & \\(1/(m+1)\\) & the power means below the harmonic member \\\\
\\(-\\infty\\) & \\(0\\) & the Leontief minimum --- exactly the typed operator \\\\
\\bottomrule
\\end{tabular}
\\end{table}

\\textbf{Lemma A (the handshake).} \\emph{With weights normalized,
\\(\\sum_i w_i \\lambda_i \\ge 1 \\iff w \\cdot s \\ge 0\\); the
\\(\\theta = 1\\) member therefore reproduces the compensatory engine of
Sections 3--4 exactly --- the same acceptance set at every state and
weight, and at the Section 6.3 datum the same per-weight plan assignment
(the thresholds \\(\\rho_1 = 2/3\\), \\(\\rho_2 = 3/2\\)).} The proof is
the identity \\(\\lambda_i = 1 + s_i\\) and the normalization. The
extension is therefore genuine: it does not move the paper's goalposts;
it interpolates between the paper's operator (\\(\\sigma = \\infty\\))
and the typed operator (\\(\\sigma = 0\\)).

\\textbf{Lemma B (collapse convention).} \\emph{For every \\(\\theta < 1\\)
member, any tube value \\(\\lambda_i \\le 0\\) rejects the plan: a
coordinate at or below the collapse level cannot be compensated by
surpluses elsewhere.} The geometric mean is \\(0\\) there; CES with
\\(\\theta \\le 0\\) is undefined there; for \\(\\theta \\in (0,1)\\) the
convention is the family's defining honesty. The \\(\\theta = 1\\) member
alone compensates across collapse --- in itself an exact statement of the
difference between the doctrines: only the perfectly-substitutable
dashboard can certify through a collapsed coordinate.

\\textbf{The master equation and the exact ladder.} On the gap-region
diagonal \\(z = (x < 1, s, s)\\), \\(s \\in (1, 2)\\) --- the Section 6.3
datum sits on it at \\(s = 6/5\\) --- the cover condition collapses to a
single comparison:

\\begin{itemize}
\\tightlist
\\item
  \\(\\theta > 0\\): accept \\(\\iff (s-1)^\\theta + (s+1)^\\theta \\ge 2\\);
\\item
  \\(\\theta = 0\\): accept \\(\\iff s^2 \\ge 2\\);
\\item
  \\(\\theta < 0\\): accept \\(\\iff (s-1)^\\theta + (s+1)^\\theta \\le 2\\)
  (the inequality flips with the sign of the denominator).
\\end{itemize}

Each rung of the ladder then has an exact rational closed form
(Table~\\ref{tab:sigmaladder}); every decision is a pure rational
comparison, cross-validated by a second independent code path in the
deposited verifier.

\\begin{table}[htbp]
\\centering
\\small
\\caption{The exact closed forms and critical floors of the ladder
(diagonal gap states \\(z = (x < 1, s, s)\\)). The critical floors are
strictly increasing in depth and converge to the typed boundary \\(s = 2\\).}
\\label{tab:sigmaladder}
\\begin{tabular}{@{}lp{4.6cm}p{4.9cm}@{}}
\\toprule
\\(\\theta\\) & accept \\(\\iff\\) & critical floor \\(s^*(\\theta)\\) \\\\
\\midrule
\\(1\\) & \\(s \\ge 1\\) & \\(1\\) (rational) \\\\
\\(2/3\\) & \\(s^2 \\ge 3\\), else \\(27(s^2-1)^2 \\ge (3-s^2)^3\\) & root of \\(27(s^2-1)^2 = (3-s^2)^3\\), in \\((117/100,\\, 59/50]\\) \\\\
\\(1/2\\) & \\(s \\ge 5/4\\) & \\(5/4\\) (rational) \\\\
\\(0\\) & \\(s^2 \\ge 2\\) & \\(\\sqrt{2}\\), in \\((141/100,\\, 142/100]\\) \\\\
\\(-1\\) & \\(s^2 \\ge s + 1\\) & the golden ratio \\(\\varphi = (1+\\sqrt{5})/2\\) (Fibonacci witnesses: \\(8/5\\) rejects, \\(13/8\\) accepts) \\\\
\\(-2\\) & \\(s^2 \\ge 3\\) & \\(\\sqrt{3}\\), in \\((173/100,\\, 174/100]\\) \\\\
\\(-m\\) & \\((s-1)^m + (s+1)^m \\le 2(s^2-1)^m\\) & increasing in \\(m\\), brackets in the verifier \\\\
\\(-\\infty\\) (Leontief) & \\(s \\ge 2\\) & \\(2\\) --- the typed boundary \\\\
\\bottomrule
\\end{tabular}
\\end{table}

The critical floors form a strictly increasing ladder
\\(1 < 5/4 < \\sqrt{2} < \\varphi < \\sqrt{3} < \\cdots \\to 2\\): the
deeper a state sits in the discrepancy region, the lower the
substitutability needed to expose the breach, and the ladder's collapse
point is exactly the typed boundary. The appearance of \\(\\sqrt{2}\\),
\\(\\varphi\\), and \\(\\sqrt{3}\\) as exact critical floors of the
geometric, harmonic, and \\(\\sigma = 1/3\\) aggregators on this datum
is, to our knowledge, a new exact witness for the substitutability
debate.

\\textbf{The critical-elasticity landscape.} For each gap state ---
typed-reject, linear-accept --- the accepted rungs form a prefix of the
ladder (Theorem S1), so there is a critical elasticity \\(\\sigma^*(z)\\):
the \\(\\sigma\\)-aggregator false-certifies \\(z\\) exactly when
\\(\\sigma \\ge \\sigma^*(z)\\). Table~\\ref{tab:sigmastar} lists exact
brackets on the diagonal \\(x = 1/2\\).

\\begin{table}[htbp]
\\centering
\\small
\\caption{The critical elasticity \\(\\sigma^*(z)\\) on diagonal gap
states \\(z = (1/2, s_1, s_2)\\) (exact brackets; strict at both ends
unless noted).}
\\label{tab:sigmastar}
\\begin{tabular}{@{}llp{5.3cm}@{}}
\\toprule
state \\(z = (x, s_1, s_2)\\) & \\(\\sigma^*(z)\\) & note \\\\
\\midrule
\\((1/2,\\, 1,\\, 1)\\) & \\(\\infty\\) exactly & only the linear member certifies \\\\
\\((1/2,\\, 3/2,\\, 1/2)\\) & \\(\\infty\\) exactly & min coordinate \\(\\le 1\\): only-linear \\\\
\\((1/2,\\, 6/5,\\, 6/5)\\) & \\(\\in (2,\\, 3)\\), strict & the Section 6.3 canonical datum \\\\
\\((1/2,\\, 5/4,\\, 5/4)\\) & \\(= 2\\) exactly & the \\(\\theta = 1/2\\) rung's equality state \\\\
\\((1/2,\\, 13/10,\\, 13/10)\\) & \\(\\in (1,\\, 2)\\) & \\\\
\\((1/2,\\, 3/2,\\, 3/2)\\) & \\(\\in (1/2,\\, 1)\\), strict & the LPI-form witness \\\\
\\((1/2,\\, 13/8,\\, 13/8)\\) & \\(\\in (1/3,\\, 1/2)\\) & the harmonic member's false-certification witness \\\\
\\((1/2,\\, 9/5,\\, 9/5)\\) & \\(\\in (1/5,\\, 1/4)\\) & \\\\
\\((1/2,\\, 39/20,\\, 39/20)\\) & \\(\\in (1/17,\\, 1/13)\\) & near the typed boundary: \\(\\sigma^* \\to 0\\) \\\\
\\bottomrule
\\end{tabular}
\\end{table}

The structure on the witness: gap states with \\(\\min(s_1, s_2) \\le 1\\)
are only-linear (\\(\\sigma^* = \\infty\\)); states with both coordinates
\\(> 1\\) have finite \\(\\sigma^*\\), given on the diagonal by the
master-equation root, with \\(\\sigma^*(s) \\to 0\\) as \\(s \\to 2^-\\)
and \\(\\sigma^*(s) \\to \\infty\\) as \\(s \\to 1^+\\).

\\textbf{Theorem S1 (nesting).} \\emph{For every pair of rungs
\\(\\theta > \\theta'\\) and every state \\(z\\), acceptance at
\\(\\theta'\\) implies acceptance at \\(\\theta\\). Consequently the
accepted rungs at each state form a prefix of the ladder;
\\(\\sigma^*(z)\\) is well defined; and it is strictly positive and finite
on every gap state with both coordinates \\(> 1\\).}

\\emph{Proof.} For fixed positive \\(\\lambda\\) and weights,
\\(M_\\theta\\) is nondecreasing in \\(\\theta\\) (the power-mean
inequality); the collapse convention preserves this (acceptance at any
\\(\\theta' < 1\\) forces \\(\\lambda > 0\\) on the serving plan's tube,
where the family is defined). Per plan and weight, hence per weight, hence
for the protocol. Finiteness: on the diagonal, \\((s-1)^\\theta \\to
\\infty\\) as \\(\\theta \\to -\\infty\\) since \\(s - 1 < 1\\), so some
finite \\(\\theta\\) rejects. Positivity: \\(s_1 + s_2 \\ge 2\\) accepts
at \\(\\theta = 1\\). \\ensuremath{\\square}

\\textbf{Theorem S2 (the two-sided Leontief punchline).} \\emph{(i)
Pointwise: every gap state is safe under some strictly positive
elasticity --- full Leontief is never necessary at a fixed state. (ii)
Uniform: for every \\(\\theta < 1\\) the rung false-certifies an exact
rational interval of gap states (the critical floor \\(s^*(\\theta) < 2\\)
strictly; concretely \\(\\sigma = 3\\) certifies \\(s = 6/5\\),
\\(\\sigma = 2\\) certifies \\(s = 13/10\\), \\(\\sigma = 1\\) certifies
\\(s = 3/2\\), \\(\\sigma = 1/2\\) certifies \\(s = 13/8\\), and
\\(\\sigma = 1/4\\) certifies \\(s = 9/5\\)). Hence no positive
\\(\\sigma\\) is uniformly safe on the gap region; the uniform critical
elasticity is \\(\\inf_z \\sigma^*(z) = 0\\); and the only uniformly safe
aggregator is \\(\\sigma = 0\\) --- the Leontief member, which is exactly
the typed operator (\\(\\mathcal{V}^0 = \\mathcal{V}_{\\mathrm{typ}}\\)).}

\\emph{Proof.} (i) is Theorem S1's prefix together with acceptance at
\\(\\theta = 1\\) (every gap state is linear-accepted). (ii) Evaluate the
master comparison at \\(s = 2\\): for \\(\\theta \\in (0,1)\\) the
accepting side is \\(\\ge 2\\) and \\((s-1)^\\theta + (s+1)^\\theta = 1 +
3^\\theta > 2\\) strictly; for \\(\\theta < 0\\) the accepting side is
\\(\\le 2\\) and \\(1 + 3^\\theta < 2\\) strictly --- both strictly
accepting at \\(s = 2\\), so by continuity some \\(\\varepsilon > 0\\)
has every \\(s \\in (2 - \\varepsilon,\\, 2)\\) accepted at that rung, and
these are gap states (typed acceptance needs \\(s \\ge 2\\)). The Leontief
member's acceptance is weight-independent (\\(\\min_i \\lambda_i \\ge 1\\)
does not involve \\(w\\)), so its protocol collapses into the common-plan
criterion --- the typed operator. \\ensuremath{\\square}

\\textbf{The LPI identification, with its caveats.} The \\(\\sigma = 1\\)
member is the Living Planet Index's functional form --- the geometric mean
of abundance indices --- evaluated here on floor-referenced indices
(\\(\\lambda_i = 1 + s_i\\), so \\(\\lambda = 1\\) at the floor) under the
paper's Protocol 2 quantifier structure. Two caveats state the exact
scope: (a) the LPI's inputs are abundance indices relative to a base
year, not floor margins --- the identification is at the level of the
functional form on the ratio scale, with the floor as reference; (b) the
LPI's operational weighting (equal weights on system-level indices,
chained) is a point in the weight cone, whereas Protocol 2 quantifies
over the whole cone --- the rung decision is therefore the adversarial
version of the LPI reading, and over-, not under-states the index's
exposure. No claim is made that the LPI as published implements Protocol
2.

\\textbf{The relevance chain, at the Section 6.3 datum.} The extension
passes the relevance test --- a named decision, a changed indicator
report, a new exact datum, and a changed management action. (1) The
decision: the benchmark's closure decision at the canonical datum, under
a DFO-precautionary-approach-style limit rule. (2) The report flip: at
the canonical trough \\(\\lambda = (1/5,\\, 11/5)\\), the linear dashboard
(equal weight) reports \\(6/5 \\ge 1\\) --- certified --- while the
LPI-structured geometric index reports \\(\\sqrt{11/25} < 1\\) (exactly:
\\(11 < 25\\)) --- a decline signal; the same datum, opposite reports.
(3) The new exact datum: \\(\\sigma^* \\in (2, 3)\\) strict at the
canonical state, the algebraic ladder, and the per-rung
false-certification witnesses of Theorem S2(ii). (4) The action flip: at
the canonical datum, every \\(\\sigma \\ge 3\\) aggregator certifies --- no
mid-transition LRP response --- while every \\(\\sigma \\le 2\\) member
rejects, triggering the mandatory closure and rebuilding response; and at
the witness \\((x, s_1, s_2) = (1/2,\\, 3/2,\\, 3/2)\\) the flip is
sharper --- the linear and the LPI-form both certify (no closure) while
the harmonic form rejects, so an agency that replaced its linear
dashboard with the LPI-structured form would still not trigger the
response at this state; the flip requires \\(\\sigma\\) below the state's
critical elasticity \\(\\sigma^* \\in (1/2,\\, 1)\\), and the triggered
response is concretely the reserve top-up \\(\\kappa^* = 1 - x = 1/2\\)
financing the staged plan (Section 5.7). The aggregator choice --- a
reporting decision, not a management decision --- flips a management
action.

\\textbf{Cross-references within the programme.} Two companion results
bracket this extension. The two-land biocapacity study (Abaee, 2026,
\\emph{How Aggregation Can Conceal Composition}) establishes the
\\emph{composition illusion} --- its continuous-time instance of the
compensatory-aggregation gap, in which a weighted aggregate meets its
floor while the typed floor on ecological capital is violated; Theorems S1
and S2 are the aggregator-side theorems behind that instance. The
obstruction-calculus companion (Abaee, 2026, \\emph{An Obstruction
Calculus for Viability under Incomplete Observation}) states the
feasibility-side complement --- its substitution-pathway certificates are
separation certificates, not universal exchange rates --- of which the
present spectrum is the elasticity-side statement.

\\textbf{Verification and honest limits.} Every number in this subsection
is an exact rational, verified in a dedicated fail-loud exact-arithmetic
verifier (57 checks; standard-library fractions only; deterministic; with
a committed byte-reproducible run log) --- a third check list, separate
from and not pooled with the grid verifier's 25 checks and the software
companion's 24 (the family's non-pooling policy). Two limits are stated.
Off the diagonal, the geometric member's cover comparison is
log-transcendental, and the verifier decides it only on proven sufficient
and necessary rational conditions --- the headline results are diagonal,
so nothing load-bearing rests on the residual undecided cells. And
interior-\\(\\theta\\) values of \\(\\sigma^*(z)\\) are bracketed between
tested rungs --- the brackets are exact and strictness-refined; the
interior value is the master root, transcendental in general.

"""
insert_before("3.A-8 σ-spectrum subsection",
              "\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n\\section{Discussion}\\label{discussion}",
              SIGMA)

# --- 8-pointer: contributions list item (xi) ---
edit("3.A-8 contributions (xi)",
     "(x) A terminology translation guide (Section 5.3)\nmapping the paper's central objects onto the working vocabularies of MCDM\nand operations research, control and viability theory, and environmental\nmodelling and governance.",
     "(x) A terminology translation guide (Section 5.3)\nmapping the paper's central objects onto the working vocabularies of MCDM\nand operations research, control and viability theory, and environmental\nmodelling and governance. (xi) A labelled substitutability-elasticity\nextension on the witness datum (Section~\\ref{substitutability-spectrum}):\nthe linear aggregate and the typed operator as the \\(\\sigma = \\infty\\)\nand \\(\\sigma = 0\\) members of one CES family, an exact critical-floor\nladder with algebraic floors (\\(\\sqrt{2}\\), \\(\\varphi\\),\n\\(\\sqrt{3}\\)), and two machine-anchored theorems (S1 nesting; S2 the\ntwo-sided Leontief punchline).")

# --- 12 + new entries: reference completions ---
edit("3.A-12/7/13 Abaee companion entries (P2 + ECOMOD, by title)",
     "Abaee, A. (2026). \\emph{Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17}. Zenodo. \\url{https://doi.org/10.5281/zenodo.22552680}.",
     "Abaee, A. (2026). \\emph{An Obstruction Calculus for Viability under Incomplete Observation}. Manuscript submitted for publication.\n\nAbaee, A. (2026). \\emph{Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17}. Zenodo. \\url{https://doi.org/10.5281/zenodo.22552680}.")
edit("3.A-7 ECOMOD entry (by title)",
     "Abaee, A. (2026). \\emph{Typed flux ledgers and depletion arithmetic: conservation, componentwise diagnostics, and the semantics of depletion horizons}. Zenodo. \\url{https://doi.org/10.5281/zenodo.22554177}.",
     "Abaee, A. (2026). \\emph{How Aggregation Can Conceal Composition: Aggregate Biocapacity and the Identifiability of Modelled Ecological-Capital Drawdown}. Manuscript submitted for publication.\n\nAbaee, A. (2026). \\emph{Typed flux ledgers and depletion arithmetic: conservation, componentwise diagnostics, and the semantics of depletion horizons}. Zenodo. \\url{https://doi.org/10.5281/zenodo.22554177}.")
edit("3.A-7 Becker entry",
     "Aubin, J.-P., and Catt\\'e, F. (2002). Bilateral fixed-points and algebraic properties of viability kernels and capture basins of sets. \\emph{Set-Valued Analysis}, 10(4), 379--416.",
     "Aubin, J.-P., and Catt\\'e, F. (2002). Bilateral fixed-points and algebraic properties of viability kernels and capture basins of sets. \\emph{Set-Valued Analysis}, 10(4), 379--416.\n\nBecker, W., Saisana, M., Paruolo, P., and Vandecasteele, I. (2017). Weights and importance in composite indicators: Closing the gap. \\emph{Ecological Indicators}, 80, 12--22.")
edit("3.A-7 Doyen et al. 2012 entry",
     "Doyen, L., and Gajardo, P. (2020). Sustainability standards,\nmulticriteria maximin, and viability. \\emph{Natural Resource Modeling},\n33(3), e12250.",
     "Doyen, L., and Gajardo, P. (2020). Sustainability standards,\nmulticriteria maximin, and viability. \\emph{Natural Resource Modeling},\n33(3), e12250.\n\nDoyen, L., Th\\'ebaud, O., B\\'en\\'e, C., Martine\u0074, V., Gourguet, S., Bertignac, M., Fifas, S., and Blanchard, F. (2012). A stochastic viability approach to ecosystem-based fisheries management. \\emph{Ecological Economics}, 75, 32--42.")
edit("3.A-12 Filippov entry",
     "Fanning, A. L., O'Neill, D. W., Hickel, J., and Roux, N. (2022). The social shortfall and ecological overshoot of nations. \\emph{Nature Sustainability}, 5(1), 26--36.",
     "Fanning, A. L., O'Neill, D. W., Hickel, J., and Roux, N. (2022). The social shortfall and ecological overshoot of nations. \\emph{Nature Sustainability}, 5(1), 26--36.\n\nFilippov, A. F. (1988). \\emph{Differential Equations with Discontinuous Righthand Sides}. Mathematics and Its Applications (Soviet Series), vol.~18. Kluwer Academic Publishers, Dordrecht.")
edit("3.A-7/13 Fischer entry",
     "Frankowska, H. (1989). Optimal trajectories associated with a solution\nof contingent Hamilton--Jacobi equations. \\emph{Applied Mathematics and\nOptimization}, 19, 291--311.",
     "Fischer, S. M., Joy, M. K., Abrahamse, W., Milfont, T. L., and Petherick, L. M. (2022). The use and misuse of composite environmental indices. \\emph{bioRxiv}, 2022.03.15.484501. \\url{https://doi.org/10.1101/2022.03.15.484501}.\n\nFrankowska, H. (1989). Optimal trajectories associated with a solution\nof contingent Hamilton--Jacobi equations. \\emph{Applied Mathematics and\nOptimization}, 19, 291--311.")
edit("3.A-13 Nardo entry",
     "Martinet, V. (2011). A characterization of sustainability with\nindicators. \\emph{Journal of Environmental Economics and Management},\n61(2), 183--197.",
     "Martinet, V. (2011). A characterization of sustainability with\nindicators. \\emph{Journal of Environmental Economics and Management},\n61(2), 183--197.\n\nNardo, M., Saisana, M., Saltelli, A., Tarantola, S., Hoffmann, A., and Giovannini, E. (2008). \\emph{Handbook on Constructing Composite Indicators: Methodology and User Guide}. OECD Publishing, Paris.")
edit("3.A-12 Warga entry",
     "von Neumann, J. (1928). Zur Theorie der Gesellschaftsspiele.\n\\emph{Mathematische Annalen}, 100, 295--320.",
     "von Neumann, J. (1928). Zur Theorie der Gesellschaftsspiele.\n\\emph{Mathematische Annalen}, 100, 295--320.\n\nWarga, J. (1972). \\emph{Optimal Control of Differential and Functional Equations}. Academic Press, New York.")

# ============ verification gates ============
print("== verification gates ==")
if text == orig:
    die("no edits applied")
if DST.exists():
    die(f"destination already exists (never overwrite): {DST}")

# gate 1: every original math span preserved verbatim (multiset containment)
import re
def spans(s):
    return Counter(re.findall(r"\$\$.*?\$\$|\\\(.*?\\\)|\\\[.*?\\\]", s, flags=re.S))
o, n = spans(orig), spans(text)
missing = o - n
if missing:
    die(f"original math spans lost/altered: {dict(missing)}")
print(f"  ok  math-span multiset preserved (v52: {sum(o.values())} spans; "
      f"v53 adds {sum((n - o).values())} new spans)")

# gate 2 (the strongest no-removal check): inverse-reconstruction.
# Reverting every enumerated edit, in reverse order at its recorded
# position, must reproduce v52 byte-identically -- proving the diff
# consists of exactly the enumerated edits (the mechanical fixes' line
# rewraps included) and nothing else: no content removed, none altered
# beyond the queue.
t = text
for k in range(len(PAIRS) - 1, -1, -1):
    name, pos, anchor, repl = PAIRS[k]
    if STATES[k] != t:
        i = next((j for j in range(min(len(t), len(STATES[k]))) if t[j] != STATES[k][j]), 0)
        die(f"inverse gate: state mismatch before reverting [{name}] at byte {i}")
    if t[pos:pos + len(repl)] != repl:
        die(f"inverse gate: replacement not at recorded position [{name}]")
    t = t[:pos] + anchor + t[pos + len(repl):]
if t != orig:
    i = next((j for j in range(min(len(t), len(orig))) if t[j] != orig[j]), min(len(t), len(orig)))
    die(f"inverse-reconstruction mismatch at byte {i}:\n  orig: {orig[i:i+120]!r}\n  rev : {t[i:i+120]!r}")
print(f"  ok  inverse-reconstruction: reverting all {len(PAIRS)} enumerated edits "
      f"reproduces v52 byte-identically (the diff is exactly the queue)")

# gate 3: the renumbering is complete and consistent
for pat in ["Section 5.6 --- resource augmentation", "Proposition 11, Section 5.6",
            "completeness requirement in Section 5.6", "witness datum (Section 5.6)",
            "rescue threshold (Section 5.6)"]:
    if pat in text:
        die(f"stale Section 5.6 reference remains: {pat}")
n57 = text.count("Section 5.7")
if n57 != 7:  # 5 renumbered refs + 2 refs inside the new content
    die(f"expected 7 'Section 5.7' refs (5 renumbered + 2 new), found {n57}")
print("  ok  renumbering complete (5 renumbered refs + 2 new-content refs to Section 5.7)")

# gate 4: the standing exclusions are honored — none of the overridden
# removals/rejections are present as actions
for bad in ["emergencystretch=2.5em"]:
    if bad in text:
        die(f"forbidden content present: {bad}")
print("  ok  standing exclusions honored")

# gate 5: new-content sanity markers
for marker in ["tab:protocols", "tab:semantics", "tab:disturbance",
               "tab:sigmafamily", "tab:sigmaladder", "tab:sigmastar",
               "tab:fisheries", "Theorem S1", "Theorem S2", "Lemma A",
               "substitutability-spectrum", "indicator-validity",
               "Filippov, A. F. (1988)", "Warga, J. (1972)",
               "Becker, W.", "Nardo, M.", "Fischer, S. M.",
               "Doyen, L., Th", "margin-reducible plans",
               "maximum sustainable yield (MSY)", "index nonnegative"]:
    if marker not in text:
        die(f"expected new-content marker missing: {marker}")
print("  ok  all new-content markers present")

# gate 6: reference alphabetization sanity (Abaee block order, references only)
refs = text[text.index("\\section*{References}"):]
i_an = refs.find("An Obstruction Calculus")
i_one = refs.find("Does a one-pool")
i_sup = refs.find("Does a surplus-production")
i_how = refs.find("How Aggregation Can Conceal")
i_typ = refs.find("Typed flux ledgers and depletion arithmetic: conservation")
for name, i in [("An Obstruction", i_an), ("Does a one-pool", i_one),
                ("Does a surplus", i_sup), ("How Aggregation", i_how),
                ("Typed flux", i_typ)]:
    if i < 0:
        die(f"Abaee entry missing: {name}")
if not (i_an < i_one < i_sup < i_how < i_typ):
    die("Abaee entries out of alphabetical order")
print("  ok  Abaee reference block alphabetized")

DST.write_text(text, encoding="utf-8")
print(f"\nWROTE {DST}")
print(f"v52: {len(orig.splitlines())} lines -> v53: {len(text.splitlines())} lines "
      f"(+{len(text.splitlines()) - len(orig.splitlines())})")

#!/usr/bin/env python3
"""
v45 — layout, accessibility, and data-anchoring pass for paper 1.

1. Figure 4: "index stays certified" annotation moved up-left into the
   whitespace above the green line, below the legend (fig script updated).
2. Layout switched to elsarticle 3p (single-column, single-spaced, full
   journal text width) to reduce page count.
3. Large single-block paragraphs split at natural points: the blend/time-
   sharing delimitation remark, and three benchmark paragraphs (datum, exact
   schedule, reader takeaways).
4. Data anchoring (audit item, scoped honestly): new closing block of the
   benchmark section anchoring the datum's units to the DFO 2016 Northern cod
   assessment (SSB LRP = 884.6 kt, NCAM M-shift series; 34% of LRP in 2015)
   and to the companion scored test's negative certificate. No estimation is
   claimed; the paper's "no empirical result" scope is preserved.
5+6. New subsection 5.3 "A translation guide for readers from neighbouring
   fields": an explicit terminology map (table) from the paper's objects to
   MCDM/OR, control/viability, and environmental-modeling/governance
   vocabulary. Subsequent subsection numbers shift (5.3->5.4, 5.4->5.5,
   5.5->5.6) and all cross-references are updated.

v44 is left untouched.
"""

LATEX = "/home/user/arena agent 1/paper rewrites/latex"
SRC = f"{LATEX}/paper1_assessment_separation_v44.tex"
DST = f"{LATEX}/paper1_assessment_separation_v45.tex"

OLD_HEADER = "% Amin Abaee. Revision v44 (readership augmentation: Section 4.12 resource-transition benchmark with machine-verified fishery instantiation; interdisciplinary bridge in 1.1; venue-agnostic master deposit DOI 10.6084/m9.figshare.33764023). Compiles with tectonic, pdflatex, or xelatex."
NEW_HEADER = "% Amin Abaee. Revision v45 (layout and accessibility pass: wider text block, paragraph breaks, Fig. 4 annotation fix, terminology translation table 5.3, benchmark units anchored to DFO 2016 Northern cod LRP; master deposit DOI 10.6084/m9.figshare.33764023). Compiles with tectonic, pdflatex, or xelatex."


def replace_once(text, old, new, what):
    n = text.count(old)
    assert n == 1, f"{what}: expected exactly 1 occurrence, found {n}"
    return text.replace(old, new)


DATA_ANCHOR = r"""\textbf{A data anchor on a real stock.} The benchmark's units are not chosen in a
vacuum: they are anchored to a real, regulated floor. For Northern cod
(\emph{Gadus morhua}, NAFO Divisions 2J3KL), the assessed spawning-stock
series (NCAM M-shift, 1983--2015) carries a limit reference point (LRP) of
\(884.6\) kt (DFO, 2016) --- the biomass below which recruitment is judged
impaired; the same series underlies the companion scored test of
surplus-production forecasters on this stock (Abaee, 2026, \emph{Does a
Surplus-Production Ladder Improve Forecasts of Northern Cod?}). Reading the
benchmark's floor as this LRP fixes the dashboard arithmetic: the witness's
opening stock (\(1.6\) floors, \(1.6 \times 884.6 \approx 1.42\) Mt) is the
neighbourhood of the assessed mid-1980s Northern cod spawning biomass, the
adverse plan's trough (\(0.6\) floors, \(\approx 531\) kt) lies inside the
critical zone where the stock in fact resided after the collapse --- about a
third of the LRP in 2015 (DFO, 2016) --- and the adverse disturbance's
worst-case depth (one full floor) is the order of the LRP crossing itself.
Three caveats keep the claim honest. This is an anchoring of units, not a
fitted case study: no parameter of the rational witness is estimated from
data. The paper's theorems therefore say nothing predictive about this or any
other stock. And the companion scored test adds a caution of exactly the
discipline this paper practises: on the same series, no structural
surplus-production model in the scored ladder beat last-value persistence
(one-year RMSE \(98\) kt versus \(115\)--\(206\) kt), and every model missed
the collapse window --- what survives institutional scrutiny on such a stock
is the menu and the floors, both of which are set by management and both of
which this paper's datum takes as given, rather than a predictive fit of the
dynamics."""

TRANSLATION = r"""\subsection{A translation guide for readers from neighbouring
fields}\label{translation-guide}

Because the paper sits at a confluence --- multi-criteria decision analysis
and operations research, control theory and viability, environmental
modelling and governance --- Table~\ref{tab:translation} translates its
central objects into each neighbouring literature's working vocabulary. The
readings are exact correspondences of mathematical role, not analogies: the
theorems are venue-neutral, and a reader may enter through any column.

\begin{table}[htbp]
\centering
\small
\caption{Terminology map: this paper's objects read from three neighbouring
vocabularies.}
\label{tab:translation}
\begin{tabular}{@{}p{2.55cm}p{3.85cm}p{3.55cm}p{4.55cm}@{}}
\toprule
 & \textbf{MCDM / operations research} & \textbf{Control / viability theory} & \textbf{Environmental modelling / governance} \\
\midrule
Typed floors \(s_i \ge 0\), enforced path-wise &
coordinate-wise (vector) criteria; per-criterion lower bounds along the whole path &
state constraints; safe set \(\mathcal{V}\); path (tube) constraints &
planetary boundaries; safe operating spaces; regulatory floors (e.g., a biomass limit reference point) \\
\addlinespace
Scalarized operator \(E_w\) &
weighted-sum acceptance; weight space \(W_+\) &
scalarized robust constraint on an aggregate output &
composite sustainability index; the assessment dashboard \\
\addlinespace
Licensing thresholds \(\rho_1, \rho_2\) &
weight intervals of acceptance; weight-space robustness of a recommendation &
parameter-dependent feasibility margins &
indicator weighting schemes; stakeholder weight elicitation \\
\addlinespace
Acceptance gap \(\mathrm{FP}_{\mathrm{agg}}\) &
scalarization error: accepted by some weighted sum, infeasible coordinate-wise &
gap between the scalarized program and the viability kernel &
the aggregation illusion: an index certifying what the floors reject \\
\addlinespace
Rescue set \(R\); threshold \(\kappa^*\) &
alternatives repairable by a budgeted side payment &
reachability under an auxiliary resource input &
transition finance: adjustment funds, fleet buy-backs \\
\addlinespace
Impossibility region \(I\) &
robust infeasibility: rejected at every weighting &
empty common safe-action set over the belief; kernel exclusion &
hidden collapse zone: index green, floor crossed mid-transition \\
\addlinespace
Blend collapse (Thm 8) vs.\ time-sharing (Prop 9) &
randomized (mixed) strategies vs.\ deterministic sequencing &
relaxed (convexified) controls vs.\ chattering &
blended policy portfolios vs.\ alternating policies \\
\addlinespace
Exact-tube semantics &
robust path-wise feasibility over a scenario set &
viability tubes; worst-case reachability &
avoiding transient breaches (e.g., extinction vortices during a transition) \\
\bottomrule
\end{tabular}
\end{table}

"""


def main():
    import shutil
    shutil.copy("/home/user/fig_benchmark_v44.png",
                f"{LATEX}/figs_p1/fig_benchmark_v44.png")

    t = open(SRC, encoding="utf-8").read()

    t = replace_once(t, OLD_HEADER, NEW_HEADER, "header comment")

    # 2. wider text block: elsarticle 3p (single-column, single-spaced,
    #    full journal text width) instead of the double-spaced review layout;
    #    \\emergencystretch absorbs the few unbreakable lines (inline math,
    #    DOI URLs) that the wider measure exposes
    t = replace_once(t,
        "\\documentclass[review,11pt]{elsarticle}",
        "\\documentclass[3p,11pt]{elsarticle}\n\\emergencystretch=2.5em",
        "documentclass layout")

    # 3. paragraph splits
    t = replace_once(t,
        "\\(s_1 \\ge 2\\) and \\(s_2 \\ge 2\\). On the regime",
        "\\(s_1 \\ge 2\\) and \\(s_2 \\ge 2\\).\n\nOn the regime",
        "converse remark split")
    t = replace_once(t,
        "to it. \\textbf{SLOW} mirrors the exposure onto the income floor",
        "to it.\n\n\\textbf{SLOW} mirrors the exposure onto the income floor",
        "benchmark datum split")
    t = replace_once(t,
        "conservative for the Schaefer realization. The remaining plans",
        "conservative for the Schaefer realization.\n\nThe remaining plans",
        "benchmark schedule split")
    t = replace_once(t,
        "index alone. The reserve threshold is the operational number:",
        "index alone.\n\nThe reserve threshold is the operational number:",
        "benchmark takeaway split")

    # 4. data anchor (end of Section 4.12)
    t = replace_once(t,
        "financing gap, not the weighting, is what separates them\n(Figure~\\ref{fig:benchmark}).\n",
        "financing gap, not the weighting, is what separates them\n(Figure~\\ref{fig:benchmark}).\n\n" + DATA_ANCHOR + "\n",
        "data anchor")

    # 6. renumber 5.3-5.5 -> 5.4-5.6 BEFORE inserting the new 5.3
    n55 = t.count("Section 5.5")
    assert n55 in (7, 8), f"unexpected 'Section 5.5' count {n55}"
    t = t.replace("Section 5.5", "Section 5.6")
    t = replace_once(t, "used in Section 5.4", "used in Section 5.5", "5.4 ref")
    assert t.count("Section 5.5") == 1  # exactly the corrected former-5.4 ref

    # 6. translation guide subsection (new 5.3), before Scope delimitations
    t = replace_once(t,
        "\\subsection{Scope delimitations}\\label{scope-delimitations}",
        TRANSLATION + "\\subsection{Scope delimitations}\\label{scope-delimitations}",
        "translation guide")

    # contribution item (x): announce the translation guide
    t = replace_once(t,
        "machine-verified and the certified tubes shown to be conservative for the\nnonlinear realization.",
        "machine-verified and the certified tubes shown to be conservative for the\nnonlinear realization. (x) A terminology translation guide (Section 5.3)\nmapping the paper's central objects onto the working vocabularies of MCDM\nand operations research, control and viability theory, and environmental\nmodelling and governance.",
        "contribution (x)")

    # DFO reference (alphabetical: after Dasgupta, before Doyen)
    t = replace_once(t,
        "Doyen, L., and Gajardo, P. (2020). Sustainability standards,",
        "DFO. (2016). \\emph{Stock Assessment of Northern Cod (NAFO Divs. 2J3KL) in 2016}. Canadian Science Advisory Secretariat, Science Advisory Report 2016/026. Fisheries and Oceans Canada, Ottawa.\n\nDoyen, L., and Gajardo, P. (2020). Sustainability standards,",
        "DFO reference")

    # layout-exposed fixes: separate the claim-layer tabular from the
    # preceding paragraph (it is \columnwidth wide and must not share a
    # line), and make reference-list DOI URLs breakable
    t = replace_once(t,
        "enumerated in the Supplementary Material (S8).\n\\noindent\\begin{tabular}",
        "enumerated in the Supplementary Material (S8).\n\n\\noindent\\begin{tabular}",
        "claim-layer tabular separation")
    for zid in ("22552680", "22553609", "22554177"):
        t = replace_once(t,
            f"https://doi.org/10.5281/zenodo.{zid}.",
            f"\\url{{https://doi.org/10.5281/zenodo.{zid}}}.",
            f"zenodo url {zid}")
    t = replace_once(t,
        "https://doi.org/10.6084/m9.figshare.33764023.",
        "\\url{https://doi.org/10.6084/m9.figshare.33764023}.",
        "figshare ref url")

    assert "tab:translation" in t and "A data anchor on a real stock" in t
    assert "DFO. (2016)" in t and "documentclass[3p,11pt]{elsarticle}" in t
    assert "Section 5.5" not in t.replace("used in Section 5.5", "")  # old refs gone

    open(DST, "w", encoding="utf-8").write(t)
    print(f"wrote {DST} ({len(t)} bytes)")


if __name__ == "__main__":
    main()

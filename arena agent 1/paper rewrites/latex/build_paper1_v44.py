#!/usr/bin/env python3
"""
v44 — readership augmentation for paper 1 (post-EMA rejection).

Cures the "too abstract for an interdisciplinary readership" verdict while
keeping the theorem spine intact for control/OR venues:

1. New Section 4.12 "A resource-transition benchmark": the manuscript's
   rational witness datum realized as a Schaefer (1954) stock-specific fishery
   transition — ecological floor = spawning biomass limit, income floor =
   fleet income margin, reserve = adjustment fund, plans = pulse-plus-closure
   / sustained-yield / reserve-financed staged transition. States that every
   number is machine-verified by the deposited benchmark script (24 exact
   checks) and that the piecewise-linear tubes are conservative for the
   nonlinear logistic realization (exact inequality).
2. New benchmark figure (figs_p1/fig_benchmark_v44.png): index vs floor under
   the licensed plan; the plan menu as management schedules.
3. Section 1.1 bridging paragraph: what the abstraction buys for anyone
   modelling a real transition (readership answer up front).
4. Contribution item (ix): the benchmark.
5. The blend-collapse/time-sharing delimitation is named in the language of
   relaxed controls vs chattering (one sentence; prominence already present).
6. Four references added (De Lara and Doyen 2008; Rockström et al. 2009;
   Raworth 2012; Schaefer 1954) — first use: Section 4.12.

Abstract, theorems, and all prior content: unchanged. v43 untouched.
"""

LATEX = "/home/user/arena agent 1/paper rewrites/latex"
SRC = f"{LATEX}/paper1_assessment_separation_v43.tex"
DST = f"{LATEX}/paper1_assessment_separation_v44.tex"

OLD_HEADER = "% Amin Abaee. Revision v43 (EMA/elsarticle; Declarations per journal technical requirements; data availability: figshare DOI 10.6084/m9.figshare.33764023). Compiles with tectonic, pdflatex, or xelatex."
NEW_HEADER = "% Amin Abaee. Revision v44 (readership augmentation: Section 4.12 resource-transition benchmark with machine-verified fishery instantiation; interdisciplinary bridge in 1.1; venue-agnostic master deposit DOI 10.6084/m9.figshare.33764023). Compiles with tectonic, pdflatex, or xelatex."

BRIDGE = r"""\medskip

\noindent\textbf{What the abstraction buys a modeller.} For a reader whose
primary interest is a specific managed system --- a fishery, a forest, an
aquifer --- the value of carrying the comparison at the level of operators,
weights, and tubes is that the resulting statements transfer between systems
without re-derivation. Whatever the stocks and whatever the plan menu, the
statements have the same form: an aggregate criterion can license, at every
weighting, a transition that no weighting licenses safely path-wise; the
licensed set decouples into a reserve-financed part and an impossible part
with an explicit resource threshold; and blending plans, rather than
alternating them, is what erases the artifact. Section 4.12 makes the
translation concrete on a standard biomass-yield model, and every number
displayed in the main text is re-derivable by exact rational arithmetic from
the deposited verification code.
"""

CONTRIB_IX = """ (ix) A resource-transition benchmark
(Section 4.12): the witness datum realized as a Schaefer-type fishery
transition --- pulse-plus-closure, sustained-yield, and reserve-financed
staged plans as management schedules --- with all quoted values
machine-verified and the certified tubes shown to be conservative for the
nonlinear realization."""

CONV_ADD = """In the language of relaxed controls, the collapse theorem is a statement
about the convexified (relaxed) action program and the converse a statement
about chattering: sliding among plans at full strength does not buy what
fractional allocation does.

\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}"""

FIG_BENCH = r"""\begin{figure}[htbp]
\centering
\includegraphics[width=0.98\linewidth]{figs_p1/fig_benchmark_v44.png}
\caption{The witness datum realized as a fishery-transition benchmark
(Section 4.12). (a) Under the pulse-and-closure plan, the composite index
\(s_1 + s_2\) at \(w = (1, 1)\) remains certified at every instant (minimum
\(2/5\)), while the ecological margin breaches its floor mid-transition
(\(-4/5\) under the heatwave strike, \(-3/10\) without it): the
accepted-at-every-weighting reading is blind to the breach. (b) The plan menu
as management schedules: pulse plus closed season; sustained-yield status
quo; and the reserve-financed staged transition, which rebuilds the stock
while improving both margins (the rescue set). All quota, stock, margin, and
fund values are the exact rational values verified in Section 4.12.}
\label{fig:benchmark}
\end{figure}

"""

SECTION_BENCH = r"""\subsection{A resource-transition benchmark}\label{resource-transition-benchmark}

The witness datum of Section 4.5 is deliberately spare: a fund, two typed
floors, four plans, and a tube semantics. This section realizes the same
datum as a standard biomass--yield resource model, so that the reader can
read every symbol as a quantity a resource agency actually monitors, and so
that the theorems can be seen to bite on a textbook dynamical system rather
than on a discrete datum alone. We emphasize what the instantiation is and is
not: it is an exact rational re-reading of the witness datum in the
domestic language of a Schaefer (1954) production model --- every number
below is verified symbolically by the deposited benchmark script, twenty-four
checks reproducing the figures quoted here --- and the certified tubes are
shown to be conservative for the nonlinear realization by an exact
inequality; it is not a calibrated case study of a specific fishery, and no
empirical claim is made.

\textbf{The system.} Let \(B(t)\) denote spawning biomass (kt) in a
stock-specific fishery over one annual review period \(t \in [0, 1]\), with
logistic surplus production
\(\sigma(B) = r B (1 - B/K)\) at \(r = 4\), \(K = 10\), and a biomass limit
\(B_{\mathrm{lim}} = 2\) kt below which the spawning stock is judged unable
to sustain recruitment. The ecological floor is the margin
\(s_1(t) = B(t) - B_{\mathrm{lim}} \ge 0\); the income floor
\(s_2(t) \ge 0\) is the fleet income margin net of costs, maintained by the
quota and by the transition reserve \(x(t)\), an adjustment fund financing
fleet draw-down. Four plans are available, standard in transition management:
\textbf{NO-SWITCH} (status-quo harvest), \textbf{FAST} (an immediate large
quota cut --- a pulse season followed by a closure --- accepting a mid-season
income trough), \textbf{SLOW} (a gradual reduction), and \textbf{STAGED} (a
below-sustained-yield quota while the reserve finances the fleet transition,
after which both margins improve). Disturbances are environmental shocks: a
mid-season heatwave strike (\(t = 1/2\)) imposing an excess mortality
\(\delta_0 = 1/2\) kt on the stock, present or absent. The state is observed
only through the institutional dashboard, the weighted aggregate
\(w \cdot (s_1, s_2)\), and the reviewer checks the dashboard, not the
floors.

\textbf{The datum, domesticated.} At the datum's initial state
\((x, s_1, s_2) = (1/2, 6/5, 6/5)\) --- a half-financed fund, a stock
\(B = B_{\mathrm{lim}} + 6/5 = 16/5\) kt (\(3.2\) kt above the limit), and a
healthy income margin --- the plan menu of Section 4.5 reads: \textbf{FAST}
cuts the quota hard for half a season; with the income floor protected by its
quota schedule, FAST's exposure is the ecological floor, whose worst-case
(dip \(2\)) trajectory is \(s_1\): \(6/5 \to -4/5 \to 6/5\) --- a mid-season
stock trough \(6/5\) kt above the limit, that is \(6/5 - 2 = -4/5\) relative
to it. \textbf{SLOW} mirrors the exposure onto the income floor
(\(s_2: 6/5 \to -4/5 \to 6/5\)). \textbf{STAGED} spends the fund at the
buy-back cost \(c = 1\) while both margins improve by the destination gain
\(e = 1/4\). These are exactly the tube tables verified in Section 4.5 and
in the deposited artifact; the interpretation is new, the arithmetic is not.

\textbf{The benchmark schedule, exactly.} The FAST plan is realized by the
announced quota \(H^*(t)\) that makes the benign margin line
\(s_1\): \(6/5 \to 6/5 - 3/2 \to 6/5\) of the tube table an exact trajectory
of \(\dot B = \sigma(B) - H^*(t)\): on \((0, 1/2)\),
\(H^* = 3 + \sigma(B_{\mathrm{line}}(t))\) (a pulse declining from
\(\tfrac{1463}{125} \approx 11.7\) to \(\tfrac{2161}{250} \approx 8.6\) kt/yr
--- admissible against the fleet capacity \(H_{\max} = 13\)), and on
\((1/2, 1)\) a closure, \(H^* = 0\). The benign branch then tracks the tube
line exactly. The heatwave strike at \(t = 1/2\) drops the stock by
\(\delta_0\), from the trough \(17/10\) to \(6/5\) --- the adverse tube's
value --- and the closure lets the surplus rebuild the stock: on the adverse
recovery leg the surplus is at least \(\sigma(6/5) = 528/125 > 4\) kt/yr,
while the certified recovery needs only \(4\), so the realized nonlinear
trajectory lies on or above the certified tube throughout; the certified
tubes are conservative for the Schaefer realization. The remaining plans are
read off the same model: NO-SWITCH and SLOW hold \(B = 16/5\) at the
sustained-yield quota \(\sigma(16/5) = 1088/125 \approx 8.7\) kt/yr; STAGED
(entered at the rescue witness, fund \(x = 3/2\)) taxes the sustained yield
by the margin improvement, rebuilding the stock
\(16/5 \to 69/20\) while the fund draws down \(3/2 \to 1/2\) and both typed
margins improve by \(e = 1/4\).

\textbf{What the reader should see.} Under the heatwave branch of the
licensed plan, the composite index at the equal weighting, \(s_1 + s_2\),
has the tube values \((12/5, 2/5, 12/5)\): the dashboard never drops below
\(2/5\), and the transition is certified at \emph{every} weighting
(Section 4.5's per-weight thresholds \(\rho_1 = 2/3\), \(\rho_2 = 3/2\) place
FAST inside every assessor's acceptance set at income-heavy weights and SLOW
inside every assessor's at biomass-heavy weights, with their overlap
containing \(r = 1\)). The floor itself, meanwhile, is breached
mid-transition on both branches (\(-4/5\) with the strike, \(-3/10\)
without), and no plan in the menu keeps both floors path-wise --- the
aggregate dashboard certifies a transition that violates the biomass limit
whenever the strike arrives, and no weighting can detect this from the
index alone. The reserve threshold is the operational number: a fund below
the buy-back cost \(c = 1\) makes the staged transition
unfinanceable (\(\kappa^*(z) = 1 - x\) at the stricken states), so the
impossibility region is exactly the set of shortfall states a modest
top-up of the adjustment fund would convert into rescue states. In
management language: the dashboard is structurally unable to distinguish a
transition that survives the heatwave from one that does not, and the
financing gap, not the weighting, is what separates them
(Figure~\ref{fig:benchmark}).

"""

NEW_REFS = [
    ("Dasgupta, P., and M\\\"aler, K.-G. (2000). Net national product, wealth, and",
     "De Lara, M., and Doyen, L. (2008). \\emph{Sustainable Management of Natural Resources: Mathematical Models and Methods}. Springer, Berlin.\n\nDasgupta, P., and M\\\"aler, K.-G. (2000). Net national product, wealth, and"),
    ("Neumayer, E. (2013). \\emph{Weak versus Strong Sustainability: Exploring\nthe Limits of Two Opposing Paradigms}, 4th ed.~Edward Elgar, Cheltenham.",
     "Neumayer, E. (2013). \\emph{Weak versus Strong Sustainability: Exploring\nthe Limits of Two Opposing Paradigms}, 4th ed.~Edward Elgar, Cheltenham.\n\nRockstr\\\"om, J., Steffen, W., Noone, K., et al. (2009). A safe operating\nspace for humanity. \\emph{Nature}, 461, 472--475."),
    ("O'Neill, D. W., Fanning, A. L., Lamb, W. F., and Steinberger, J. K. (2018). A good life for all within planetary boundaries. \\emph{Nature Sustainability}, 1(2), 88--95.",
     "O'Neill, D. W., Fanning, A. L., Lamb, W. F., and Steinberger, J. K. (2018). A good life for all within planetary boundaries. \\emph{Nature Sustainability}, 1(2), 88--95.\n\nRaworth, K. (2012). A safe and just space for humanity: Can we live within the doughnut? \\emph{Oxfam Policy and Practice: Climate Change and Resilience}, 8(1), 1--26."),
    ("Saint-Pierre, P. (1994). Approximation of the viability kernel.",
     "Schaefer, M. B. (1954). Some aspects of the dynamics of populations important to the management of commercial marine fisheries. \\emph{Inter-American Tropical Tuna Commission Bulletin}, 1(2), 23--56.\n\nSaint-Pierre, P. (1994). Approximation of the viability kernel."),
]

TAIL_ANCHOR = "\\begin{center}\\rule{0.5\\linewidth}{0.5pt}\\end{center}\n\n\\section{Conclusions}\\label{conclusions}"


def replace_once(text, old, new, what):
    n = text.count(old)
    assert n == 1, f"{what}: expected exactly 1 occurrence, found {n}"
    return text.replace(old, new)


def main():
    import shutil
    shutil.copy("/home/user/fig_benchmark_v44.png",
                f"{LATEX}/figs_p1/fig_benchmark_v44.png")

    t = open(SRC, encoding="utf-8").read()

    t = replace_once(t, OLD_HEADER, NEW_HEADER, "header comment")

    t = replace_once(
        t,
        "operators formalized in\nSection 3.1 and read doctrinally in Section 5.1.\n",
        "operators formalized in\nSection 3.1 and read doctrinally in Section 5.1.\n\n" + BRIDGE,
        "1.1 bridge")

    t = replace_once(
        t,
        "dominates, subsuming Theorem 5's gap and Theorem 8's collapse as\ninstances.",
        "dominates, subsuming Theorem 5's gap and Theorem 8's collapse as\ninstances." + CONTRIB_IX + ".",
        "contribution (ix)")

    t = replace_once(
        t,
        "the structural character of the gap is a property of\nthe \\emph{convexity of the action space}, not of the assessment doctrine\nand not of temporal sharing as such.\n",
        "the structural character of the gap is a property of\nthe \\emph{convexity of the action space}, not of the assessment doctrine\nand not of temporal sharing as such. In the language of relaxed controls,\nthe collapse theorem is a statement about the convexified (relaxed) action\nprogram and the converse a statement about chattering: sliding among plans\nat full strength does not buy what fractional allocation does.\n",
        "relaxed-controls naming")

    t = replace_once(
        t,
        TAIL_ANCHOR,
        FIG_BENCH + SECTION_BENCH + TAIL_ANCHOR,
        "Section 4.12 + figure")

    for anchor, entry in NEW_REFS:
        t = replace_once(t, anchor, entry, f"ref: {entry[:40]}")

    assert "resource-transition benchmark" in t and "fig_benchmark_v44" in t
    assert "Schaefer, M. B. (1954)" in t and "Rockstr" in t and "Raworth" in t and "De Lara" in t

    open(DST, "w", encoding="utf-8").write(t)
    print(f"wrote {DST} ({len(t)} bytes)")


if __name__ == "__main__":
    main()

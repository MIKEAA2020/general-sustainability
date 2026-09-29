#!/usr/bin/env python3
"""v29 coherence pass 3: figures, the declared convention, and provenance.

Three requirements from the ratified migration:

  R-A  The figures must be cited from the v3 provenance chain. make_figs_v16.py
       imports run_intervention_srcyear.py, whose docstring is a verbatim copy
       of the v2 runner's and which writes to results_srcyear/; make_figs_v17.py
       imports run_intervention_v3.py and reads results_srcyear_v3/. The two
       runners are functionally identical (they differ only in output paths),
       so the seven figures come out BIT-IDENTICAL (md5 verified) -- the change
       is provenance, not pixels. The tex is repointed at figs_e2_v3/.

  R-B  The catch-timing convention must be documented in the paper, including
       the honest admission that nothing in the repo says whether ssb_kt is
       pre- or post-fishery, and the grounds for choosing source-year.

  R-C  Data availability must name the v3 scripts. It currently names
       rerun_campaigns/campaign_e2_elevation.py and campaign_e2_fox_form.py --
       both of which are the registered/hybrid-basis campaigns that produced
       the numbers this version no longer reports.

Also: "fully deterministic (no random components)" is false of a paper whose
Sections 3.8 and 3.10 are Monte Carlo with fixed seeds; and Section 3.11 says
the xteNCAM row was "refitted in the registered convention", which after the
migration reads as the destination-year convention. It means "the same
convention as the registered object", i.e. source-year -- its own source says
so ("the committed fit_params convention ... transition t->t+1 uses catch at
t").
"""
from pathlib import Path

P = Path("/home/user/fam/e2/paperE2_cod_intervention_v29.tex")
t = P.read_text(encoding="utf-8")


def rep(old, new, n=1):
    global t
    assert t.count(old) == n, (t.count(old), old[:90])
    t = t.replace(old, new)


# ------------------------------------------------------------------ R-A
assert t.count("figs_e2/") == 7
t = t.replace("figs_e2/", "figs_e2_v3/")

# ------------------------------------------- determinism claim (Section 2.1)
rep("All inputs are public and the analysis is deterministic. The stock\n"
    "series is the Northern cod",
    "All inputs are public and the analysis is reproducible: every stochastic\n"
    "layer uses a fixed seed and a fixed draw budget (Sections 3.8 and 3.10),\n"
    "and every deterministic layer is a closed-form or fixed-point\n"
    "computation. The stock\nseries is the Northern cod")

# ------------------------------------------------------- R-B: new Section 2.3
SEC23 = r"""
\subsubsection{2.3 The catch-timing convention}\label{the-catch-timing-convention}

One modelling choice has to be declared explicitly, because it moves the
reported numbers. Write the one-step residual of the governed map as

\[e_t = S_{t+1} - \bigl(S_t + g(S_t) - C_{t+\delta}\bigr),\qquad
\delta \in \{0, 1\},\]

so that \(\delta = 0\) pairs the transition \(t \to t+1\) with the catch
of the year the transition leaves (\emph{source-year}) and \(\delta = 1\)
pairs it with the catch of the year it enters
(\emph{destination-year}). The two are different residual distributions
on one and the same fitted map: at the committed \((r, K)\) the
source-year pool has mean \(-10.9\) kt, SD \(114.9\) kt and lag-1
autocorrelation \(0.554\), against \(-20.4\) kt, \(135.0\) kt and
\(0.652\) for the destination-year pool, and the classes of Definition 2.3
move with them (\(-329.0\)/\(-287.4\)/\(-80.9\) kt against
\(-460.0\)/\(-318.8\)/\(-114.9\) kt).

\textbf{Convention (adopted).} Every kernel, boundary, floor, replay,
figure and table of this paper is computed in the source-year convention
(\(\delta = 0\)).

It is adopted on three grounds, none of them provenance. \emph{(i)
Coherence.} The committed parameters are the minimisers of the
source-year loss. The estimation routine regresses the increment
\(S_{t+1} - S_t\) on the catch of year \(t\), so \(r = 0.2369\) and
\(K = 5000\) kt minimise the mean squared source-year residual:
\(12{,}772\) kt\(^2\), against \(17{,}873\) kt\(^2\) for the
destination-year pool at those same parameters (\(28.5\%\) lower).
Scoring those parameters against destination-year residuals would report
classes drawn from a loss the fit never minimised. \emph{(ii) Fit.} The
source-year pool is the better-fitting and the less serially correlated
of the two, as tabulated above. \emph{(iii) No interior alternative.}
Refitting \((r, K)\) freely against the blended catch
\(w\,C_t + (1-w)\,C_{t+1}\) gives a mean squared error monotone
decreasing in \(w\) over the whole unit interval, with the optimum at the
boundary \(w = 1\): \(17{,}713\) kt\(^2\) at \(w = 0\) (where the refit
gives \(r = 0.2084\)), \(15{,}026\) kt\(^2\) at \(w = 0.5\), and
\(12{,}772\) kt\(^2\) at \(w = 1\); the out-of-sample error over
2008--2015 moves the same way (\(834.9\) to \(783.1\) kt\(^2\), eight
one-step transitions). There is no interior optimum, so a half-and-half
compromise is not supported by the data.

\textbf{Limitation, stated because a referee will ask.} Nothing in the
archived source documentation records whether the spawning-stock column of
DFO (2016) Table A2 is measured before or after the calendar year's
removals, and the biology does not settle it either: Northern cod spawn in
March--May, so an SSB observation sits mid-year while landings are
calendar-year totals, and the interval between two SSB observations spans
the back half of one year's catch and the front half of the next. On that
reading neither pure convention is mechanistically exact and the truth is
a blend --- which is exactly why ground (iii) is needed. The convention is
therefore declared on statistical and coherence grounds rather than
derived from provenance, and it is stated here rather than left implicit.
The sensitivity is not suppressed: the whole analysis was also computed
under \(\delta = 1\), and those artifacts are archived with the superseded
runner rather than overwritten, so every affected number can be read off
the archive instead of taken on trust. Four quantities move materially ---
the constructive bound (\(91.59\) kt against \(57.61\) kt), the number of
vacuous floor classes (one against two), the certified horizon (\(6\)/7
years against \(5\)/6), and the 60-kt rules' \(T=\infty\) boundary
(\(884.6\) kt against \(900.3\) kt). No parameter estimate, no form
comparison and no certificate direction changes.

"""
rep("\\subsection{3. Results}\\label{results}\n", SEC23.lstrip("\n") + "\\subsection{3. Results}\\label{results}\n")

# --------------------------------- Section 3.11: "registered convention" fix
rep("refitted in the registered convention on 1954--2007 with the same box\n"
    "rule and the safe set written against its own reference point.",
    "refitted in the same source-year convention as the primary object\n"
    "(Section 2.3) on 1954--2007, with the same box rule and the safe set\n"
    "written against its own reference point.")

# --------------------------------------------------------- R-C: availability
rep("The analysis is fully deterministic (no random components). All input\n"
    "data, analysis scripts, and result files are archived in the public\n"
    "repository at https://github.com/MIKEAA2020/general-sustainability.\n"
    "Re-executing the source-year intervention runner regenerates both output\n"
    "files (the results archive and the kernel-boundary table); a\n",
    "The analysis is reproducible: the deterministic layers are closed-form or\n"
    "fixed-point computations and every stochastic layer uses a fixed seed and a\n"
    "fixed draw budget (Section 3.8 uses \\(N = 20{,}000\\) trajectories per cell,\n"
    "Section 3.10 \\(B = 2000\\) bootstrap refits). All input data, analysis\n"
    "scripts, and result files are archived in the public repository at\n"
    "https://github.com/MIKEAA2020/general-sustainability. The primary kernel\n"
    "tables (Tables 1 and 2, Sections 3.1--3.5) are produced by\n"
    "\\texttt{wave\\_e\\_cod/src/run\\_intervention\\_v3.py}, which writes\n"
    "\\texttt{results/intervention\\_results\\_v3.json} and\n"
    "\\texttt{results/intervention\\_boundaries\\_v3.csv}; the two post-freeze\n"
    "reactive families of Definition 2.4 (Table 1) by\n"
    "\\texttt{wave\\_e\\_cod/src/run\\_families\\_v3.py}, which writes\n"
    "\\texttt{results/e2\\_families\\_v3.csv}. Re-executing either runner\n"
    "regenerates its output files; a\n")

rep("""The critical-zone
rule and cascade vocabulary follows the DFO precautionary-approach
framework (DFO, 2009); the SSB series and LRP are DFO (2016) Table A2;
the catch series is Schijns et al.~(2021). The elevation layers of
Sections 3.7--3.10 (carrying-capacity grid, stochastic viability,
finite-duration floors, bootstrap bands, and Figures 1--7) are produced
by the repository script rerun\\_campaigns/campaign\\_e2\\_elevation.py
with fixed seeds, and their outputs are archived alongside it;
re-execution regenerates them exactly. The Section 3.6 Fox form, the
Section 3.11 xteNCAM row, and the Section 3.8 1992 one-off sensitivity
are produced by rerun\\_campaigns/campaign\\_e2\\_fox\\_form.py,
campaign\\_e2\\_xteNCAM\\_row.py, and e2\\_breakpoint\\_1992.py, likewise
archived and deterministic.
""",
    """The critical-zone
rule and cascade vocabulary follows the DFO precautionary-approach
framework (DFO, 2009); the SSB series and LRP are DFO (2016) Table A2;
the catch series is Schijns et al.~(2021). The elevation layers of
Sections 3.7--3.10 (carrying-capacity grid, stochastic viability,
finite-duration floors, bootstrap bands) are produced by
\\texttt{wave\\_e\\_cod/src/campaign\\_e2\\_elevation\\_v3.py} with fixed
seeds, its outputs archived in \\texttt{src/results\\_srcyear\\_v3/}, and
re-execution regenerates them exactly. Figures 1--7 are produced by
\\texttt{wave\\_e\\_cod/src/make\\_figs\\_v17.py}; it supersedes
\\texttt{make\\_figs\\_v16.py} only in provenance --- it imports the v3
runner and reads the v3 elevation outputs --- and its output is
identical. The three Section 3.6 form rows are produced by
\\texttt{campaign\\_e2\\_depensation\\_v3.py} (free-\\(s_0\\) Allee refit),
\\texttt{campaign\\_e2\\_allee\\_declared\\_v3.py} (declared-strength refit)
and \\texttt{campaign\\_e2\\_fox\\_form\\_v3.py} (Fox form), with outputs in
\\texttt{src/results\\_forms\\_v3/}; the Section 3.11 xteNCAM row by
\\texttt{arena agent 1/other documents/rerun\\_campaigns/campaign\\_e2\\_xteNCAM\\_row.py};
and the Section 3.8 one-off treatment of the 1992 draw by
\\texttt{e2\\_breakpoint\\_1992.py} in the same directory. Every script
named above implements the source-year convention of Section 2.3. The
registered-convention counterparts are retained rather than overwritten
(\\texttt{run\\_intervention\\_v2.py} and its outputs, and
\\texttt{wave\\_e\\_cod/src/superseded\\_v2/}), so the convention sensitivity
listed in Section 2.3 can be recomputed from the archive rather than
taken on trust.
""")

P.write_text(t, encoding="utf-8")
print("v29e pass 1 ok (placeholder assertion will fail here by design)")

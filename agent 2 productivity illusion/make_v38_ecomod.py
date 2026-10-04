#!/usr/bin/env python3
"""make_v38_ecomod.py — ECOMOD v37 -> v38 submission-repair round.

Executes the line-level-review fix register (Task 122 deliverable, Part 3)
plus the owner's 2.1-table question, as anchored, exact-match operations
(family discipline: every op asserted to occur exactly the stated number of
times; the builder fails loudly rather than guessing).

Fix register:
  F1  four math-mode double-backslash defect sites (lines 69, 611 x2, 695 —
      the last missed by the original register)
  F2  debt-equation cross-pointer Eq. 11 -> Eq. 12
  F3  restoration notation unified on R_rc = chi_r A_r (B-E)_+ with chi_r in
      gha^-1 (the form the registry, the SI S5.4 tables and the code all use);
      rho_r / Psi / Phi retired; the Recovery-dynamics sentence recast
  F4  the +464%/-364% contribution shares qualified as shares of d ln B in
      the Fig. 1 caption and the Conclusions
  F5  both overfull hboxes repaired (symbol-table floors row broken over
      lines; proxy-decomposition table: tabcolsep + wrapped header)
  F6  the six never-cited references cited at their natural homes
      (FAO 2023, FAO 2020, Monfreda, ESA 2017, Copernicus 2019, Galli 2016)
  F7  reference list re-sorted — four faults, incl. the Calvin/Carvalhais
      inversion missed by the original register
  F9  "set is set by demand" garble; SI-summary bullet S5 range/list; the
      References section made unnumbered
  N1  (new, owner question) the 2.1 symbol table's "State?" column relabelled
      "Role" with normalised, grammatical entries
  P1  (portal-safety) preamble made engine-adaptive via iftex (pdfLaTeX
      branch: fontenc/inputenc/lmodern; Lua/Xe branch: unchanged fontspec +
      unicode-math), and the source converted to pure ASCII (literal
      section/x/approx/minus/Greek glyphs replaced by macros or ASCII names,
      the verbatim equation block ASCII-fied and realigned) so journal-portal
      pdfLaTeX servers can compile the .tex themselves.

No mathematical content changed; all numbers, tables, figures and the
abstract are byte-identical in intent and value.
"""
import re
import sys

SRC = "manuscript_ECOMOD_v37.tex"
DST = "manuscript_ECOMOD_v38.tex"

# ---------------------------------------------------------------- verbatim ---
VERB_ROWS = [
    (None, "QUALITY (per-ha capacity, a state; NOT land area):"),
    ("(1)", "  G_c(q) = rho_c q (1 - q/q_max)"),
    ("(2a)", "FAST YIELD:   Y_f = b_f A_f"),
    ("(2b)", "CAPITAL YIELD: Y_c = [b_c + b_G,c G_c(q)] A_c"),
    ("(2c)", "BIOCAPACITY:  B = Y_f + Y_c"),
    ("(3)", "FOOTPRINT:    E = e P"),
    ("(4)", "DEFICIT:      S = [E - sigma_f Y_f - sigma_c Y_c]_+"),
    ("(5)", "CAPITAL AREA: dA_c/dt = -u_c + R_fc + R_rc"),
    ("(6)", "FAST AREA:    dA_f/dt = +u_c + mu A_r - eta_f A_f - R_fc"),
    ("(7)", "RESERVE:      dA_r/dt = -mu A_r + eta_f A_f - R_rc"),
    ("(8)", "QUALITY:      dq/dt = G_c(q(t-tau_g))"),
    ("(9)", "POPULATION:   dP/dt = r P [1 - P / K(t-tau_p)],  K = B/e"),
    ("(10)", "CARRYING CAP: K = B / e  [algebraic]"),
    ("(11)", "DEGRADATION:  b_f = (b_f0 + T_b(t)) e^{-alpha D(t)}"),
    ("(12)", "DEBT:         dD/dt = [E - B]_+ - eta D"),
    ("(13)", "TECHNOLOGY:   T_b = deltab / (1 + e^{-kappa_w (t-t_wave)})"),
    (None, "CONVERSION RATE (dimensionally ha/yr):"),
    ("(14)", "  u_c = min(S/b_f, A_c - A_c,min) / tau_conv"),
]
COL = 59  # column at which the equation markers start (max line 64 chars)


def build_verbatim():
    out = []
    for marker, text in VERB_ROWS:
        assert len(text) <= COL, f"verbatim line too wide: {text!r}"
        if marker is None:
            out.append(text)
        else:
            out.append(text.ljust(COL) + marker)
    return "\n".join(out)


NEW_VERB = ("\\begingroup\\small\\begin{verbatim}\n" + build_verbatim()
            + "\n\\end{verbatim}\\endgroup")

# ------------------------------------------------------------------- ops ----
# (name, old, new, expected_count)
OPS = [
# ---- P1: header provenance + engine note -----------------------------------
("P1a engine line",
r"""% Compiled with LuaLaTeX (fontspec + unicode-math).""",
r"""% Compiles under LuaLaTeX/XeLaTeX (fontspec branch) and pdfLaTeX (lmodern
% branch); the preamble is engine-adaptive via iftex, the source is ASCII.
% v38 (2026-10-04): submission-repair round per the line-level review ---
% F1 the four math-mode double-backslash defects fixed; F2 debt-equation
% pointer Eq. 11 -> Eq. 12; F3 restoration notation unified on
% R_rc = chi_r A_r (B-E)_+ with chi_r in gha^-1 (rho_r, Psi, Phi retired;
% registry unit corrected); F4 the +464%/-364% shares qualified as shares
% of d ln B (Fig. 1 caption + Conclusions); F5 both overfull boxes
% repaired; F6 six never-cited references cited at their homes; F7 the
% reference list re-sorted (four faults); F9 minor items (threshold
% garble, SI-summary range, References unnumbered); the 2.1 symbol
% table's "State?" column relabelled "Role" with normalised entries.
% Preamble made engine-adaptive (iftex) and the source made pure ASCII so
% journal-portal pdfLaTeX servers can compile the .tex. No mathematical
% content changed.""", 1),
# ---- P1: engine-adaptive preamble -------------------------------------------
("P1b preamble branch",
r"""\usepackage[a4paper,margin=1in]{geometry}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{unicode-math}""",
r"""\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{iftex}
\ifPDFTeX
  % pdfLaTeX branch (journal-portal servers): no fontspec/unicode-math.
  \usepackage[T1]{fontenc}
  \usepackage[utf8]{inputenc}
  \usepackage{lmodern}
\else
  % LuaLaTeX/XeLaTeX branch (authoritative build): fontspec + unicode-math.
  \usepackage{fontspec}
  \usepackage{unicode-math}
  \setmainfont{DejaVu Serif}
  \setmonofont{DejaVu Sans Mono}
  \setmathfont{Latin Modern Math}
\fi""", 1),
("P1c remove old font block",
r"""{hyperref}

\setmainfont{DejaVu Serif}
\setmonofont{DejaVu Sans Mono}
\setmathfont{Latin Modern Math}
""",
r"""{hyperref}
""", 1),
("P1d date bump",
r"\date{September 26, 2026}", r"\date{October 4, 2026}", 1),
# ---- ASCII conversions (portal safety) --------------------------------------
("A1 section sign in thanks",
r"see SI~§S5.3b.}}", r"see SI~\S S5.3b.}}", 1),
("A2 section sign in footnote",
r"calibration in SI~§S5.3b reads)", r"calibration in SI~\S S5.3b reads)", 1),
("A3 em-dash",
r"a \emph{stock} in $\text{ha}$ — the area that would close the shortfall",
r"a \emph{stock} in $\text{ha}$ --- the area that would close the shortfall", 1),
("A4 conclusions change ratios",
r"grew 2.85×, area 1.17×, per-ha yield 2.43×",
r"grew $2.85\times$, area $1.17\times$, per-ha yield $2.43\times$", 1),
("A5 conclusions approx ratios",
r"flat as an endpoint change, ≈1.008×, its intra-period index reaching ≈1.024×",
r"flat as an endpoint change, $\approx1.008\times$, its intra-period index reaching $\approx1.024\times$", 1),
# ---- F1: math-mode double-backslash defects ---------------------------------
("F1a intro 2.85x",
r"grew 2.85$\\times$,", r"grew 2.85$\times$,", 1),
("F1b identifiability 6.4e8",
r"$6.4\\times10^8$", r"$6.4\times10^{8}$", 1),
("F1c identifiability approx 8.6x",
r"an $\\approx8.6\\times$ increase", r"an $\approx8.6\times$ increase", 1),
("F1d conclusions parameter list",
r"($b_c,\\ b_{G,c},\\ \\rho_c$)", r"($b_c,\ b_{G,c},\ \rho_c$)", 1),
# ---- F2: debt equation pointer ----------------------------------------------
("F2 debt eq pointer",
r"(Eq.~11)", r"(Eq.~12)", 1),
# ---- F3: restoration notation unification -----------------------------------
("F3a retire rho_r row",
r"""$\rho_r$ & reserve-scaled restoration rate (in $R_{rc}=\rho_r A_r \Psi$) & yr$^{-1}$ & param \\
""", "", 1),
("F3b retire Psi/Phi row",
r"""$\Psi,\Phi$ & restoration gates (surplus-gated $\Psi(B-E)_+$; deficit-gated $\Phi(E-B)_+$) & --- & extension \\
""", "", 1),
("F3c R_rc row canonical form",
r"$R_{rc}$ & reserve$\to$capital restoration flow ($A_r\to A_c$) & ha$\cdot$yr$^{-1}$ & param \\",
r"$R_{rc}$ & reserve$\to$capital restoration flow, $R_{rc}=\chi_r A_r(B-E)_+$, surplus-gated ($A_r\to A_c$; the deficit-gated variant uses $(E-B)_+$) & ha$\cdot$yr$^{-1}$ & gated flow \\", 1),
("F3d chi_r row",
r"$\chi_r$ & reserve$\to$capital restoration gate & yr$^{-1}$ & param \\",
r"$\chi_r$ & surplus-gated reserve$\to$capital restoration coefficient (in $R_{rc}=\chi_r A_r(B-E)_+$) & gha$^{-1}$ & parameter \\", 1),
("F3e chi row",
r"$\chi$ & fast$\to$capital restoration rate (in $R_{fc}=\chi A_f\Phi$; extension) & yr$^{-1}$ & extension \\",
r"$\chi$ & fast$\to$capital restoration coefficient (in $R_{fc}=\chi A_f(B-E)_+$; stated extension) & gha$^{-1}$ & coefficient (extension) \\", 1),
("F3f registry chi_r unit",
r"$\chi_r$ & $0.10\,\text{yr}^{-1}$ & surplus-gated",
r"$\chi_r$ & $0.10\,\text{gha}^{-1}$ & surplus-gated", 1),
("F3g recovery-dynamics sentence",
r"""Recovery of capital land requires an explicit restoration flow --- e.g. $R_{rc}=\rho_rA_r\Psi(\text{restoration})$ ($A_r\to A_c$), where $\rho_r$ (yr$^{-1}$) scales the reserve and $\Psi$ is the gate --- with the land equations modified consistently. An $A_f\to A_c$ variant $R_{fc}=\chi A_f\Phi(\cdot)$ requires $\chi$ in yr$^{-1}$ to give ha$\cdot$yr$^{-1}$; we treat $R_{rc}$ as the base-model restoration and relegate $R_{fc}$ to a stated variant.""",
r"""Recovery of capital land requires an explicit restoration flow --- e.g. the surplus-gated $R_{rc}=\chi_rA_r(B-E)_+$ ($A_r\to A_c$), where $\chi_r$ (gha$^{-1}$) scales the flow and the positive part $(B-E)_+$ is the gate --- with the land equations modified consistently. An $A_f\to A_c$ variant $R_{fc}=\chi A_f(B-E)_+$ (likewise surplus-gated; $\chi$ in gha$^{-1}$) is a stated extension; we treat $R_{rc}$ as the base-model restoration and relegate $R_{fc}$ to a stated variant.""", 1),
# ---- N1: "State?" -> "Role" --------------------------------------------------
("N1a role header",
r"Symbol & Meaning & Unit & State? \\", r"Symbol & Meaning & Unit & Role \\", 2),
("N1b state rows",
r" & yes \\", r" & state \\", 5),
("N1c dependent balance",
r" & balance (not independent) \\", r" & dependent balance \\", 1),
("N1d G_c rate function",
r"per-ha regeneration of capital-land quality & yr$^{-1}$ & no \\",
r"per-ha regeneration of capital-land quality & yr$^{-1}$ & rate function \\", 1),
("N1e B aggregate",
r"$B$ & biocapacity $=b_f A_f+b_c A_c+b_{G,c}G_c(q)\,A_c$ & gha$\cdot$yr$^{-1}$ & no \\",
r"$B$ & biocapacity $=b_f A_f+b_c A_c+b_{G,c}G_c(q)\,A_c$ & gha$\cdot$yr$^{-1}$ & aggregate \\", 1),
("N1f E aggregate",
r"$E$ & footprint $=eP$ & gha$\cdot$yr$^{-1}$ & no \\",
r"$E$ & footprint $=eP$ & gha$\cdot$yr$^{-1}$ & aggregate \\", 1),
("N1g R_fc role",
r"($A_f\to A_c$, stated extension, not base) & ha$\cdot$yr$^{-1}$ & extension \\",
r"($A_f\to A_c$, stated extension, not base) & ha$\cdot$yr$^{-1}$ & flow (extension) \\", 1),
("N1h L_c role",
r"off in the base model) & ha$\cdot$yr$^{-1}$ & extension \\",
r"off in the base model) & ha$\cdot$yr$^{-1}$ & flow (extension) \\", 1),
("N1i H_c role",
r"$H_c$ & capital-land timber flow target (off in the base model) & gha$\cdot$ha$^{-1}\cdot$yr$^{-1}$ & extension \\",
r"$H_c$ & capital-land timber flow target (off in the base model) & gha$\cdot$ha$^{-1}\cdot$yr$^{-1}$ & parameter (extension) \\", 1),
("N1j param -> parameter",
r" & param \\", r" & parameter \\", 17),
# ---- F4: qualify the contribution shares ------------------------------------
("F4a figure caption qualifier",
r"(c) The exact identity $d\ln B=d\ln(B/P)+d\ln P$: population $+0.959$ ($+464\%$) and per-capita $-0.752$ ($-364\%$).",
r"(c) The exact identity $d\ln B=d\ln(B/P)+d\ln P$: population $+0.959$ and per-capita $-0.752$ (contribution shares of $d\ln B$: $+464\%$ and $-364\%$).", 1),
("F4b conclusions qualifier",
r"population $+464\%$, per-capita $-364\%$, $R_B$ crossing $1$ in 1971",
r"population $+464\%$ of $d\ln B$, per-capita $-364\%$, $R_B$ crossing $1$ in 1971", 1),
# ---- F5: overfull repairs ----------------------------------------------------
("F5a symbol-table floors row break",
r"$A_r^{\min}, A_f^{\max}, K_{\min}$ & reserve floor, arable ceiling, carrying-capacity floor",
r"$A_r^{\min},$\newline$A_f^{\max},$\newline$K_{\min}$ & reserve floor, arable ceiling, carrying-capacity floor", 1),
("F5b decomposition table colsep",
r"""\begin{center}
\small
\begin{tabular}{llll}""",
r"""\begin{center}
\small
\setlength{\tabcolsep}{4pt}
\begin{tabular}{llll}""", 1),
("F5c decomposition table header wrap",
r"Share weight ($\bar s$ or $w$) & \textbf{Contribution to $d\ln B$} \\",
r"Share weight ($\bar s$ or $w$) & \textbf{\parbox[t]{8.5em}{\raggedright Contribution to $d\ln B$}} \\", 1),
# ---- F6: cite the six never-cited references ---------------------------------
("F6a FAO 2023 at FAOSTAT area",
r"""element \emph{Area},
world, 1961--2022.""",
r"""element \emph{Area},
world, 1961--2022 (FAO, 2023).""", 1),
("F6b FAO 2020 at FRA forest area",
r"$A_c(t)=\text{FAO/FRA forest area}$, with the natural grassland",
r"$A_c(t)=\text{FAO/FRA forest area}$ (FAO, 2020), with the natural grassland", 1),
("F6c Monfreda at EarthStat",
r"or EarthStat/MapSPAM. This is precisely why",
r"or EarthStat (Monfreda et al., 2008)/MapSPAM. This is precisely why", 1),
("F6d ESA + Copernicus at hierarchy tier 3",
r"""(3) remote-sensing /
historical land cover plus EarthStat/MapSPAM/GAEZ, for validation or extension.""",
r"""(3) remote-sensing land cover (ESA CCI, ESA, 2017; Copernicus LC100, Copernicus, 2019) or the
historical reconstructions above, plus EarthStat/MapSPAM/GAEZ, for validation or extension.""", 1),
("F6e Galli in the critique sentence",
r"and are criticised by Blomqvist et al. (2013), Giampietro \& Saltelli (2014), and van den Bergh \& Grazi (2015).",
r"and are examined critically by Blomqvist et al. (2013), Giampietro \& Saltelli (2014), Galli et al. (2016), and van den Bergh \& Grazi (2015).", 1),
# ---- F7: reference list re-sorting -------------------------------------------
("F7a Calvin before Carvalhais",
r"""\item Carvalhais, N., Forkel, M., Khomik, M., Bellarby, J., Jung, M., Migliavacca, M., Mu, M., Saatchi, S., Santoro, M., Thurner, M., Weber, U., Ahrens, B., Beer, C., Cescatti, A., Randerson, J. T. \& Reichstein, M. (2014). Global covariation of carbon turnover times with climate in terrestrial ecosystems. \emph{Nature}, 514(7521), 213--217.
\item Calvin, K. \& Bond-Lamberty, B. (2018). Integrated human--Earth system modeling --- state of the science and future directions. \emph{Environmental Research Letters}, 13(6), 063006.""",
r"""\item Calvin, K. \& Bond-Lamberty, B. (2018). Integrated human--Earth system modeling --- state of the science and future directions. \emph{Environmental Research Letters}, 13(6), 063006.
\item Carvalhais, N., Forkel, M., Khomik, M., Bellarby, J., Jung, M., Migliavacca, M., Mu, M., Saatchi, S., Santoro, M., Thurner, M., Weber, U., Ahrens, B., Beer, C., Cescatti, A., Randerson, J. T. \& Reichstein, M. (2014). Global covariation of carbon turnover times with climate in terrestrial ecosystems. \emph{Nature}, 514(7521), 213--217.""", 1),
("F7b Copernicus out from under N",
r"""\item Nardo, M., Saisana, M., Saltelli, A., Tarantola, S., Hoffmann, A. \& Giovannini, E. (2008). \emph{Handbook on Constructing Composite Indicators: Methodology and User Guide.} Paris: OECD Publishing.
\item Copernicus (2019). \emph{Global Land Cover LC100.} European Commission, Land Copernicus.
\item Neubauer, P., Jensen, O. P., Hutchings, J. A. \& Baum, J. K. (2013). Resilience and recovery of overexploited marine populations. \emph{Science}, 340(6130), 347--349.""",
r"""\item Nardo, M., Saisana, M., Saltelli, A., Tarantola, S., Hoffmann, A. \& Giovannini, E. (2008). \emph{Handbook on Constructing Composite Indicators: Methodology and User Guide.} Paris: OECD Publishing.
\item Neubauer, P., Jensen, O. P., Hutchings, J. A. \& Baum, J. K. (2013). Resilience and recovery of overexploited marine populations. \emph{Science}, 340(6130), 347--349.""", 1),
("F7c Copernicus under C (after Cohen)",
r"""\item Cohen, J. E. (1995). Population growth and Earth's human carrying capacity. \emph{Science}, 269(5222), 341--346.
\item Dasgupta, P. (2021). \emph{The Economics of Biodiversity: The Dasgupta Review.} London: HM Treasury.""",
r"""\item Cohen, J. E. (1995). Population growth and Earth's human carrying capacity. \emph{Science}, 269(5222), 341--346.
\item Copernicus (2019). \emph{Global Land Cover LC100.} European Commission, Land Copernicus.
\item Dasgupta, P. (2021). \emph{The Economics of Biodiversity: The Dasgupta Review.} London: HM Treasury.""", 1),
("F7d FAO 2023 before Fischer",
r"""\item Fischer, S. M., Joy, M. K., Abrahamse, W., Milfont, T. L. \& Petherick, L. M. (2022). The use and misuse of composite environmental indices. \emph{bioRxiv}, 2022.03.15.484501. \url{https://doi.org/10.1101/2022.03.15.484501}.
\item FAO (2023). \emph{FAOSTAT: Land Use; Crops and Livestock Products.} Rome: Food and Agriculture Organization.
\item Galli, A., Giampietro, M., Goldfinger, S., Lazarus, E., Lin, D., Saltelli, A., Wackernagel, M. \& M\"uller, F. (2016). Questioning the ecological footprint. \emph{Ecological Indicators}, 69, 224--232.""",
r"""\item FAO (2023). \emph{FAOSTAT: Land Use; Crops and Livestock Products.} Rome: Food and Agriculture Organization.
\item Fischer, S. M., Joy, M. K., Abrahamse, W., Milfont, T. L. \& Petherick, L. M. (2022). The use and misuse of composite environmental indices. \emph{bioRxiv}, 2022.03.15.484501. \url{https://doi.org/10.1101/2022.03.15.484501}.
\item Galli, A., Giampietro, M., Goldfinger, S., Lazarus, E., Lin, D., Saltelli, A., Wackernagel, M. \& M\"uller, F. (2016). Questioning the ecological footprint. \emph{Ecological Indicators}, 69, 224--232.""", 1),
("F7e Klein Goldewijk before Krausmann",
r"""\item Krausmann, F., Erb, K.-H., Gingrich, S., Haberl, H., Bondeau, A., Gaube, V., Lauk, C., Plutzar, C. \& Searchinger, T. D. (2013). Global human appropriation of net primary production doubled in the 20th century. \emph{PNAS}, 110(25), 10324--10329.
\item Klein Goldewijk, K., Beusen, A., Doelman, J. \& Stehfest, E. (2017). Anthropogenic land use estimates for the last 12,000 years --- HYDE 3.2. \emph{Earth System Science Data}, 9(2), 927--953.""",
r"""\item Klein Goldewijk, K., Beusen, A., Doelman, J. \& Stehfest, E. (2017). Anthropogenic land use estimates for the last 12,000 years --- HYDE 3.2. \emph{Earth System Science Data}, 9(2), 927--953.
\item Krausmann, F., Erb, K.-H., Gingrich, S., Haberl, H., Bondeau, A., Gaube, V., Lauk, C., Plutzar, C. \& Searchinger, T. D. (2013). Global human appropriation of net primary production doubled in the 20th century. \emph{PNAS}, 110(25), 10324--10329.""", 1),
# ---- F9: minor items ----------------------------------------------------------
("F9a threshold garble",
r"Consistent with the flat-in-$\tau_g$ boundary: the set is set by demand, not the lag",
r"Consistent with the flat-in-$\tau_g$ boundary: the threshold is set by demand, not the lag", 1),
("F9b SI-summary bullet range/list",
r"""SI \S S5.1--S5.5 (proxy-$\alpha$ sensitivity; spectral robustness of the composition diagnostic and conversion-loop eigenvalue; recovery metric $\mathcal{R}_c(T)$ and gate-sign asymmetry; $\tau_p$-extended delay scan to $\tau_p=2000$\,yr; prediction-to-section map).""",
r"""SI \S S5.1--S5.5 (proxy-$\alpha$ sensitivity; spectral robustness of the composition diagnostic and conversion-loop eigenvalue; empirical anchoring of the regeneration timescale and the provisioning book; recovery metric $\mathcal{R}_c(T)$ and gate-sign asymmetry; $\tau_p$-extended delay scan to $\tau_p=2000$\,yr), together with the prediction-to-section map in \S S6.""", 1),
("F9c references unnumbered",
r"\section{References}", r"\section*{References}", 1),
]


def main():
    src = open(SRC, encoding="utf-8").read()
    out = src
    for name, old, new, count in OPS:
        found = out.count(old)
        if found != count:
            print(f"FAIL [{name}]: expected {count} occurrence(s), found {found}")
            print("--- expected pattern (first 200 chars) ---")
            print(old[:200])
            sys.exit(1)
        out = out.replace(old, new)
        print(f"ok   [{name}] x{count}")

    # verbatim block: regex replace, assert exactly one match
    pat = re.compile(r"\\begingroup\\small\\begin{verbatim}.*?\\end{verbatim}\\endgroup",
                     re.DOTALL)
    matches = pat.findall(out)
    if len(matches) != 1:
        print(f"FAIL [verbatim]: expected 1 block, found {len(matches)}")
        sys.exit(1)
    out = pat.sub(lambda _: NEW_VERB, out)
    print("ok   [verbatim ASCII-ification + realignment] x1")

    # ---- final assertions -----------------------------------------------------
    non_ascii = [(i + 1, ln) for i, ln in enumerate(out.split("\n"))
                 if any(ord(c) > 127 for c in ln)]
    if non_ascii:
        print("FAIL [pure ASCII]: non-ASCII remains on lines:",
              [n for n, _ in non_ascii])
        sys.exit(1)
    print("ok   [pure-ASCII source]")

    # no math-mode double backslash may remain
    for bad in (r"$\\", r"\\times", r"\\approx", r"\\rho_c$", r"\\ "):
        if bad in out:
            i = out.index(bad)
            print(f"FAIL [double-backslash residue]: {bad!r} at ...{out[i-60:i+60]!r}...")
            sys.exit(1)
    print("ok   [no double-backslash math residue]")

    # engine branch sanity
    assert out.count(r"\ifPDFTeX") == 1 and out.count(r"\fi") == 1
    assert out.count(r"\setmainfont{DejaVu Serif}") == 1
    print("ok   [engine-adaptive branch structure]")

    if out == src:
        print("FAIL: output identical to input?")
        sys.exit(1)

    open(DST, "w", encoding="utf-8").write(out)
    print(f"\nwrote {DST}: {len(src)} -> {len(out)} chars")
    # print a unified diff summary
    import difflib
    diff = list(difflib.unified_diff(src.split("\n"), out.split("\n"),
                                     lineterm="", n=0))
    adds = sum(1 for l in diff if l.startswith("+") and not l.startswith("+++"))
    dels = sum(1 for l in diff if l.startswith("-") and not l.startswith("---"))
    print(f"diff: +{adds} / -{dels} lines")


if __name__ == "__main__":
    main()

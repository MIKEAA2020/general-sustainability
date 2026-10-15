#!/usr/bin/env python3
"""Generate every LaTeX table of paper09 v44 (main + SI) from results.json."""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R = json.load(open(HERE / "results.json"))
COD, EDW, AR = R["cod"], R["edwards"], R["archive"]
MAIN = HERE.parent / "parts"
SI = HERE.parent / "si_parts"
MAIN.mkdir(exist_ok=True)
SI.mkdir(exist_ok=True)


def f(x, n=1, none="--"):
    if x is None:
        return none
    if isinstance(x, str):
        return x
    return f"{x:.{n}f}"


def fi(x, none="--"):
    return none if x is None else f"{int(round(x))}"


def pct(x, n=1):
    return "--" if x is None else f"{100*x:.{n}f}\\%"


def esc(s):
    return s.replace("%", "\\%").replace("_", "\\_")


def table(label, caption, colspec, header, rows, notes="", small=True, placement="[t]", width=None, colsep=None):
    out = [f"\\begin{{table}}{placement}", "\\centering", f"\\caption{{{caption}}}", f"\\label{{{label}}}"]
    if small:
        out.append("\\small")
    if colsep:
        out.append(f"\\setlength{{\\tabcolsep}}{{{colsep}}}")
    if width:
        out.append(f"\\resizebox{{{width}}}{{!}}{{%")
    out.append(f"\\begin{{tabular}}{{{colspec}}}")
    out.append("\\toprule")
    if header:
        out.append(header + " \\\\")
        out.append("\\midrule")
    for r in rows:
        if r == "MIDRULE":
            out.append("\\midrule")
        else:
            out.append(" & ".join(r) + " \\\\")
    out.append("\\bottomrule")
    out.append("\\end{tabular}")
    if width:
        out.append("}")
    if notes:
        out.append(f"\\par\\smallskip\\begin{{minipage}}{{0.97\\linewidth}}\\footnotesize {notes}\\end{{minipage}}")
    out.append("\\end{table}")
    return "\n".join(out) + "\n"


def longtable(label, caption, colspec, header, rows, notes="", size="\\footnotesize", colsep="3pt"):
    out = ["\\begingroup" + size + "\\setlength{\\tabcolsep}{" + colsep + "}", f"\\begin{{longtable}}{{{colspec}}}",
           f"\\caption{{{caption}}}\\label{{{label}}}\\\\", "\\toprule", header + " \\\\", "\\midrule", "\\endfirsthead",
           f"\\multicolumn{{{colspec.count('l')+colspec.count('r')+colspec.count('c')}}}{{l}}{{\\emph{{(continued)}}}}\\\\", "\\toprule",
           header + " \\\\", "\\midrule", "\\endhead", "\\bottomrule", "\\endfoot"]
    for r in rows:
        if r == "MIDRULE":
            out.append("\\midrule")
        else:
            out.append(" & ".join(r) + " \\\\")
    out.append("\\end{longtable}")
    if notes:
        out.append(f"\\par\\noindent\\begin{{minipage}}{{0.97\\linewidth}}\\footnotesize {notes}\\end{{minipage}}")
    out.append("\\endgroup")
    return "\n".join(out) + "\n"


def w(path, text):
    Path(path).write_text(text)


cf, cc, ef = COD["fit"], COD["constants"], EDW["fit"]
cls = cc["classes_abs"]
POL_NAMES = {"BAU": "BAU (5 kt)", "flat_0": "zero catch", "flat_25": "flat 60 kt", "flat_50": "flat 120 kt",
             "flat_75": "flat 180 kt", "flat_100": "flat 240 kt", "S1": "S1 (60 kt above LRP, 0 below)",
             "cpm": "cascade (60/30/5/0)", "graded2": "graded 60/90", "graded3": "graded 30/60/90"}
SPOL = dict(POL_NAMES, S1="S1 (staged 60 kt)")
EPOL = {"BAU": "BAU ($\\bar P$)", "flat_90": "flat 90\\%", "flat_80": "flat 80\\%", "flat_70": "flat 70\\%", "flat_60": "flat 60\\%",
        "flat_50": "flat 50\\%", "flat_0": "zero pumping", "S1": "Stage I ($-20\\%$ below 660 ft)", "cpm": "CPM cascade"}
ESPOL = dict(EPOL, S1="Stage I")
CLS = {"UC_min": "worst", "UC_q05": "q05", "UC_q10": "q10"}

# ------------------------------------------------------------------ main: inputs
rows = [
    ["state $x$", "SSB $S$ (kt), NCAM 2016", "J-17 annual mean head $H$ (ft AMSL)"],
    ["control $u$", "annual catch $C$ (kt)", "annual pumping $P$ ($10^3$ ac-ft)"],
    ["exogenous driver", "none (residual only)", "recharge $R$ ($10^3$ ac-ft), floor-classed"],
    ["one-step map", "$S' = S + rS(1-S/K) - C + e$", "$H' = aH + \\alpha + \\beta R + \\gamma P + e$"],
    ["threshold(s)", f"LRP $\\theta = {COD['K_star']:.1f}$ kt", "618 ft (physical), 660 ft (institutional)"],
    ["ceiling $x_{\\mathrm{hi}}$", "10\\,000 kt", "710 ft"],
    ["fit window / transitions", f"1983--2007 / {cf['n_train']}", f"1934--1990 / {ef['n_train']}"],
    ["out-of-sample audit", f"2008--2015 / {cf['n_oos']}", f"1991--2023 / {ef['n_oos']}"],
    ["parameters", f"$r={cf['r']:.4f}$, $K={cf['K']:.0f}$ (box edge)", f"$a={ef['a']:.4f}$, $\\alpha={ef['alpha']:.2f}$, $\\beta={ef['beta']:.4f}$, $\\gamma={ef['gamma']:.5f}$"],
    ["slope at threshold", f"$F'(\\theta)={cc['Fp_Kstar']:.4f}$ (expansive)", f"$a={ef['a']:.4f}$ (contracting)"],
    ["residual SD (fit / OOS)", f"{cf['train_sd']:.1f} / {cf['oos_sd']:.1f} kt", f"{ef['train_sd']:.2f} / {ef['oos_sd']:.2f} ft"],
    ["declared defect $\\varepsilon$ (fit max)", f"{cf['train_abs_max']:.1f} kt ({cf['train_abs_max_year']})", f"{ef['train_abs_max']:.2f} ft ({ef['train_abs_max_year']})"],
    ["OOS max $|$residual$|$", f"{cf['oos_abs_max']:.1f} kt ({cf['oos_abs_max_year']}); within $\\varepsilon$", f"{ef['oos_abs_max']:.2f} ft ({ef['oos_abs_max_year']}); exceeds $\\varepsilon$"],
    ["floor classes (worst / q05 / q10)", f"$|e| = {cls['UC_min']:.1f}$ / {cls['UC_q05']:.1f} / {cls['UC_q10']:.1f} kt",
     f"$R \\ge {EDW['floors']['UC_min']:.1f}$ / {EDW['floors']['UC_q05']:.1f} / {EDW['floors']['UC_q10']:.1f}"],
    ["reference control level", "$\\bar C = 240$ kt (pre-1992 directed fishery)", f"$\\bar P = {EDW['P_bar']:.2f}$ (1934--1990 mean)"],
]
w(MAIN / "gen_tab_inputs.tex", table("tab:inputs", "Certification inputs for the two systems. Every quantity is fixed by the two intervention protocols frozen on 2026-08-26 and re-derived from the data files by the exact core (Section~\\ref{sec:verification}). Floor classes are the minimum, 5th and 10th percentiles (linear interpolation) of the fitted residuals (cod) or of the fit-window recharge (Edwards).",
                                        "lll", "Quantity & Northern cod (2J3KL) & Edwards Aquifer (J-17)", rows, small=True, width="\\textwidth"))

# ------------------------------------------------------------------ main: cod kernels
kern = COD["kernels"]


def bnd(v):
    if v is None:
        return "$\\emptyset$"
    if isinstance(v, list):
        v = v[1]
    return f"{v:.1f}"


rows = []
for pid in ("flat_0", "BAU", "flat_25", "flat_50", "flat_75", "flat_100", "S1", "cpm", "graded2", "graded3"):
    r = [POL_NAMES[pid]]
    for cid in ("UC_min", "UC_q05", "UC_q10"):
        k = kern[pid][cid]
        r += [bnd(k["1"]), bnd(k["5"]), bnd(k["inf"])]
    rows.append(r)
notes = ("Lower boundary $b_T$ (kt) of the nominal closed-loop kernel $W_T=[b_T,10\\,000]$ of the safe set $[\\theta,10\\,000]$, $\\theta=884.6$ kt, under the three floor classes; "
         "$\\emptyset$: empty. Rules that coincide with a flat catch on the safe set (S1 and the cascade with flat 60 kt) have identical kernels there (Proposition~\\ref{prop:stage}). "
         f"Closed forms: $b_\\infty=\\theta$ iff $C+|e|\\le g(\\theta)={cc['g_Kstar']:.1f}$ kt; $W_\\infty\\neq\\emptyset$ iff $C+|e|\\le g_{{\\max}}={cc['g_max']:.1f}$ kt (Corollary~\\ref{{cor:cod}}). Full horizon grid in SI Section~S3.")
w(MAIN / "gen_tab_cod_kernels.tex", table("tab:cod-kernels", "Northern cod: nominal kernel boundaries at horizons $T=1$, $5$ and $\\infty$.",
                                             "lrrrrrrrrr", "Policy & \\multicolumn{3}{c}{worst ($|e|=329.0$)} & \\multicolumn{3}{c}{q05 ($|e|=287.4$)} & \\multicolumn{3}{c}{q10 ($|e|=80.9$)} \\\\ & $b_1$ & $b_5$ & $b_\\infty$ & $b_1$ & $b_5$ & $b_\\infty$ & $b_1$ & $b_5$ & $b_\\infty$",
                                             rows, notes, width="\\textwidth"))

# ------------------------------------------------------------------ main: Edwards kernels / attractors
att = EDW["attractors"]
kn = EDW["kernels_nominal"]
sup = EDW["supply_open_loop"]
rows = []
for pid in ("BAU", "flat_90", "flat_80", "flat_70", "flat_60", "flat_50", "flat_0", "S1", "cpm"):
    a = att[pid]
    k618 = kn["K_phys_618"][pid]["UC_min"]
    k660 = kn["K_inst_660"][pid]["UC_min"]
    w618 = "whole" if k618["inf" if "inf" in k618 else "20"] is not None and abs(k618["20"] - 618.0) < 1e-6 else (f"$\\emptyset$ ($T\\ge{k618['first_empty']}$)" if k618.get("first_empty") else "--")
    if a["UC_min"]["self_consistent"] >= 618.0:
        w618 = "whole safe set"
    else:
        w618 = f"empty from $T={k618['first_empty']}$"
    w660 = f"{k660['1']:.1f} / {bnd(k660['2'])} / {bnd(k660['3'])}"
    rows.append([EPOL[pid], f"{a['UC_min']['self_consistent']:.1f}", f"{a['UC_q05']['self_consistent']:.1f}", f"{a['UC_q10']['self_consistent']:.1f}",
                 w618, w660, f"{sup[pid]['train_mean_P']:.1f}", pct(sup[pid]["train_cut_active"], 0)])
notes = ("Attractor $H^*=(\\alpha+\\beta F+\\gamma P)/(1-a)$ of the stage that contains it (self-consistent fixed point of the closed loop) under the three recharge floors $F$. "
         "618-ft kernel under the worst floor: whole safe set iff $H^*\\ge 618$ (Corollary~\\ref{cor:edw}); otherwise empty beyond $T_{\\mathrm{empty}}$. 660-ft column: lower boundary at $T=1/2/3$ under the worst floor; "
         f"zero pumping is the only rule whose 660-ft kernel survives to $T=3$, and none survives $T=\\infty$ because $H^*_0=(\\alpha+\\beta F)/(1-a)={EDW['zero_pumping_attractor']['UC_min']:.1f}$ ft $<660$ (Theorem~\\ref{{thm:margin}}). "
         "Supply: mean prescribed pumping on the observed 1934--1990 heads ($10^3$ acre-ft yr$^{-1}$) and share of years with the cut active.")
w(MAIN / "gen_tab_edw.tex", table("tab:edw", "Edwards Aquifer: attractors, kernels and open-loop supply by policy.",
                                    "lrrrllrr", "Policy & \\multicolumn{3}{c}{attractor $H^*$ (ft)} & 618-ft kernel & 660-ft $b_1/b_2/b_3$ & supply & cut active \\\\ & worst & q05 & q10 & (worst floor) & (worst floor) & & ",
                                    rows, notes, width="\\textwidth"))

# ------------------------------------------------------------------ main: certified horizons
ex = COD["exact_bounded_defect"]
hz = COD["certified_horizon"]
rows = []
for pid, ckey in (("flat_0", "0.0"), ("BAU", "5.0"), ("flat_25", "60.0"), ("S1", None), ("cpm", None), ("flat_50", "120.0"), ("flat_75", "180.0"), ("flat_100", None)):
    r = ["cod: " + POL_NAMES[pid]]
    for cid in ("UC_min", "UC_q05", "UC_q10"):
        lip = hz[ckey][cid]["last_nonempty"] if ckey else (hz["60.0"][cid]["last_nonempty"] if pid in ("S1", "cpm") else None)
        if pid == "flat_100":
            lip = ex[pid][cid]["lipschitz_last_nonempty"]
        exv = ex[pid][cid]["last_nonempty"]
        r += [fi(lip) if lip is not None else "--", str(exv)]
    rows.append(r)
rows.append("MIDRULE")
kc = EDW["kernels_certified"]["K_phys_618"]
be = EDW["bounded_error"]
for pid in ("BAU", "flat_90", "flat_80", "S1", "cpm", "flat_0"):
    r = ["Edwards: " + EPOL[pid]]
    for cid in ("UC_min", "UC_q05", "UC_q10"):
        lip = kc[pid][cid]["last_nonempty"]
        fe = be[pid][f"{cid}|train"]["first_empty"]
        exv = (fe - 1) if fe else ">8"
        r += [str(lip), str(exv)]
    rows.append(r)
notes = ("Last horizon $T$ (years) at which the certified kernel of the threshold (cod: LRP; Edwards: 618 ft) is non-empty, for the declared uniform defect $\\varepsilon$ (cod 329.0 kt, Edwards 15.41 ft) on top of the floor class. "
         "`Lip.': the registered Lipschitz-inflation certificate, nominal kernel of $\\theta+r_T$ with $r_T=\\varepsilon(a^T-1)/(a-1)$ (Proposition~\\ref{prop:lip}). `Exact': the exact robust kernel of the bounded-defect class, "
         "$W^\\varepsilon_{t+1}=\\{x: [F(x)-\\varepsilon,F(x)+\\varepsilon]\\subset W^\\varepsilon_t\\}$ (Theorem~\\ref{thm:exact}). For the affine aquifer map the two coincide wherever the backward recursion binds (Proposition~\\ref{prop:lip}(ii)); "
         "for the expansive cod map the Lipschitz certificate is conservative in horizon and, unlike the exact kernel, is insensitive to the catch level. With the out-of-sample Edwards defect (21.81 ft), positive-pumping rules have a two-year exact horizon and zero pumping retains three years.")
w(MAIN / "gen_tab_horizons.tex", table("tab:horizons", "Certified horizons under the declared defect: Lipschitz certificate versus exact bounded-defect kernel.",
                                         "lrrrrrr", "System: policy & \\multicolumn{2}{c}{worst floor} & \\multicolumn{2}{c}{q05 floor} & \\multicolumn{2}{c}{q10 floor} \\\\ & Lip. & exact & Lip. & exact & Lip. & exact",
                                         rows, notes))

# ------------------------------------------------------------------ main: cod uncertainty
cr = AR["stochastic_crossings"]
st = AR["stochastic"]
bf, bj = AR["bootstrap_fixedK"], AR["bootstrap_joint"]
pr = COD["profile"]
bi = COD["bootstrap_independent_fixedK"]
rows = [
    ["\\multicolumn{4}{l}{\\emph{Stochastic layer: 20-year survival from the LRP, $N=20\\,000$ trajectories per cell}}"],
    ["scheme", "BAU (5 kt)", "flat 60 kt", "flat 120 kt"],
    ["i.i.d. residuals", f(st["iid|BAU|S0=884.6|T=20"], 3), f(st["iid|flat_25|S0=884.6|T=20"], 3), f(st["iid|flat_50|S0=884.6|T=20"], 3)],
    ["4-year blocks", f(st["block4|BAU|S0=884.6|T=20"], 3), f(st["block4|flat_25|S0=884.6|T=20"], 3), f(st["block4|flat_50|S0=884.6|T=20"], 3)],
    ["i.i.d., 1992 removed", f(st["iid_no1992|BAU|S0=884.6|T=20"], 3), f(st["iid_no1992|flat_25|S0=884.6|T=20"], 3), f(st["iid_no1992|flat_50|S0=884.6|T=20"], 3)],
    ["independent re-run (seed 20261015)", f(COD["stochastic_independent"]["iid|C=5|S0=LRP|T=20"], 3), f(COD["stochastic_independent"]["iid|C=60|S0=LRP|T=20"], 3), f(COD["stochastic_independent"]["iid|C=120|S0=LRP|T=20"], 3)],
    ["catch at which survival crosses 0.9 / 0.8 (kt)", f"i.i.d.: {f(cr['iid']['0.9'])} / {f(cr['iid']['0.8'])}", f"blocks: none / {f(cr['block4']['0.8'])}", f"no-1992: {f(cr['iid_no1992']['0.9'])} / {f(cr['iid_no1992']['0.8'])}"],
    "MIDRULE",
    ["\\multicolumn{4}{l}{\\emph{Identification of $C^*=g(\\theta)-|e_{q10}|$ (kt)}}"],
    ["source", "median", "90\\% interval", "share $C^*\\le 0$"],
    [f"fixed-$K$ residual bootstrap ($B={bf['B']}$, archived)", f(bf["Cstar_median"]), f"[{f(bf['Cstar_q05_q95'][0])}, {f(bf['Cstar_q05_q95'][1])}]", f"{bf['n_nonpositive']}/{bf['B']}"],
    [f"same design, independent seed", f(bi["frozen_floor"]["Cstar_median"]), f"[{f(bi['frozen_floor']['Cstar_q05_q95'][0])}, {f(bi['frozen_floor']['Cstar_q05_q95'][1])}]", pct(bi["frozen_floor"]["share_nonpositive"])],
    [f"joint $(r,K)$ refit ($B={bj['B']}$, archived)", f(bj["Cstar_median"]), f"[{f(bj['Cstar_q05_q95'][0])}, {f(bj['Cstar_q05_q95'][1])}]", f"{bj['n_nonpositive']}/{bj['B']}"],
    [f"\\quad conditional on $K\\ge 2\\theta$ ({pct(bj['share_K_ge_2Kstar'])} of refits)", f(bj["Cstar_median_given_2Kstar"]), f"[{f(bj['Cstar_q05_q95_given_2Kstar'][0])}, {f(bj['Cstar_q05_q95_given_2Kstar'][1])}]", f"{bj['n_nonpositive_given_2Kstar']}/{bj['n_K_ge_2Kstar']}"],
    [f"profile set in $K$, one-parameter cut ({pr['F_cut_ratio_1par']:.3f})", "--", f"[{f(pr['C_star_range_1par'][0])}, {f(pr['C_star_range_1par'][1])}]", f"$K\\ge{pr['K_set_1par'][0]:.0f}$"],
    [f"profile set in $K$, two-parameter cut ({pr['F_cut_ratio']:.3f})", "--", f"[{f(pr['C_star_range'][0])}, {f(pr['C_star_range'][1])}]", f"$K\\ge{pr['K_set'][0]:.0f}$"],
]
notes = ("Survival: fraction of trajectories that never fall below the LRP within 20 years when the fitted residuals are resampled (schemes as labelled); the ceiling under i.i.d. resampling is "
         f"{f(cr['iid']['ceiling'],3)} because any draw of the 1992 residual ($-329.0$ kt) from the LRP is fatal and $(23/24)^{{20}}=0.427$ would be the ceiling if the 1992 draw were the only hazard. "
         "Bootstraps resample fit residuals along the registered map from the 1983 state with the observed catches and refit $r$ (and $K$ in the joint design); the floor is held at its declared value. "
         f"Profile sets: $K$ is unidentified from above (the sets run to the top of the 50\\,000-kt grid); the SSE at the box edge exceeds the profile minimum by {100*(pr['sse_box_edge_ratio']-1):.1f}\\%.")
w(MAIN / "gen_tab_cod_unc.tex", table("tab:cod-unc", "Northern cod: stochastic and identification layers around the constructive bound.", "lrrr", "\\multicolumn{4}{l}{}", rows, notes, width="\\textwidth"))

# ------------------------------------------------------------------ main: Edwards uncertainty / supply
cl = EDW["closed_loop"]
ab = {d["policy"]: d for d in AR["edw_audit_bootstrap"]["per_policy"]}
bi_e = EDW["bootstrap_independent"]["P_attractor_ge_618"]
rows = [
    ["\\multicolumn{5}{l}{\\emph{Mean annual supply $P$ ($10^3$ acre-ft yr$^{-1}$) and $P(H^*\\ge618)$}}"],
    "MIDRULE",
    ["policy", "\\shortstack{open loop\\\\1934--90}", "\\shortstack{closed loop\\\\fit 1934--90}",
     "\\shortstack{closed loop OOS\\\\1991--2023}", "\\shortstack{$P(H^*\\ge618)$\\\\archived / rerun}"],
    "MIDRULE",
]
for pid, key in (("BAU", "BAU"), ("flat_90", "flat-90%"), ("flat_80", "flat-80%"), ("flat_60", "flat-60%"), ("flat_0", "flat-0%"), ("S1", "S1"), ("cpm", "CPM")):
    rows.append([EPOL[pid], f(sup[pid]["train_mean_P"], 2), f"{f(cl[pid]['train_1934_1990']['mean_P'],2)} ({pct(cl[pid]['train_1934_1990']['cut_active'],0)})",
                 f"{f(cl[pid]['oos_1991_2023']['mean_P'],2)} ({pct(cl[pid]['oos_1991_2023']['cut_active'],0)})",
                 f"{f(ab[key]['p_attractor_ge_618'],2)} / {f(bi_e.get(pid), 2) if pid in bi_e else '--'}"])
rows.append("MIDRULE")
rows.append(["\\multicolumn{5}{l}{\\emph{Exact-kernel supremum defect $\\bar\\varepsilon_T$ (ft) by horizon}}"])
rows.append("MIDRULE")
rows.append(["policy", "$T=2$", "$T=3$", "$T=4$", "$T=5$"])
rows.append("MIDRULE")
for pid in ("BAU", "flat_90", "flat_80", "S1", "cpm", "flat_0"):
    s = be[pid]["sup_eps_UC_min"]
    rows.append([EPOL[pid], f(s["2"], 2), f(s["3"], 2), f(s["4"], 2), f(s["5"], 2)])
notes = ("Closed-loop replays use observed recharge and rule-based pumping, starting from 1934 (fit) or 1990 (out of sample); percentages in parentheses are years with the cut active. "
         "$P(H^*\\ge618)$ is the share of 5,000 bootstrap refits whose worst-floor attractor clears 618 ft (archived / independent seeds 20260905 / 20261015). "
         "At the declared 15.41-ft defect, every rule certifies three years and only zero pumping lasts four; at the out-of-sample 21.81-ft defect, only zero pumping certifies three years.")
w(MAIN / "gen_tab_edw_unc.tex", table("tab:edw-unc", "Edwards Aquifer: supply, protection and the bounded-defect audit.", "lrrrr", "", rows, notes, colsep="4pt"))

# ------------------------------------------------------------------ main: resolution table
zp = EDW["zero_pumping_attractor"]
rows = [
    ["Is the reference point self-viable under some constant control?", f"yes under q10 ($C^*={cc['C_star']['UC_q10']:.1f}$ kt); no under q05/worst ($C^*<0$)", f"yes at 618 ft (any cut $\\ge 7.2\\%$); no at 660 ft under any floor ($H^*_0={zp['UC_min']:.1f}$--{zp['UC_q10']:.1f} ft)"],
    ["Is any non-empty $T=\\infty$ kernel available?", f"q10: for $C\\le C_{{\\mathrm{{vac}}}}={cc['C_vac']['UC_q10']:.1f}$ kt; q05: $C\\le {cc['C_vac']['UC_q05']:.1f}$ kt; worst: none", "618 ft: yes for every cut $\\ge 7.2\\%$; 660 ft: none"],
    ["Does a staged rule beat the flat cap it coincides with at the threshold?", "no (S1, cascade $\\equiv$ flat 60 kt on the safe set)", "no in protection; yes in supply (S1 $+3.3\\%$ over flat 90\\%, CPM $+50.6\\%$ over flat 60\\%)"],
    ["Horizon certified under the declared defect (exact kernel)", "8--13 yr (worst/q05), 12--28 yr (q10); Lipschitz: 5--7 yr", "3 yr positive-pumping (4 zero); 2 yr OOS positive-pumping (3 zero)"],
    ["Is the horizon policy-sensitive?", "exact: yes (zero catch 12 vs 240 kt 8 yr, worst floor); Lipschitz: no", "weakly (3 vs 4 yr)"],
    ["What sets the horizon?", f"local expansion at the LRP, $F'(\\theta)={cc['Fp_Kstar']:.3f}$", f"defect-to-contraction ratio $\\varepsilon/(1-a)={EDW['r_inf']:.1f}$ ft against a 92-ft band to the ceiling"],
    ["Is the key constant identified?", "$g(\\theta)$ and $C^*$ yes (profile), $K$ no", "$a$, $H^*$ yes (bootstrap SD 10--13 ft on $H^*$)"],
    ["Stochastic (non-worst-case) reading", "20-yr survival from the LRP 0.90 (BAU) to 0.65 (120 kt)", "$P(H^*\\ge618)$: 0.41 (BAU), 0.53 (flat 90\\%), 0.65 (S1), 0.99 (zero)"],
]
w(MAIN / "gen_tab_resolved.tex", table("tab:resolved", "What the frozen protocols resolve, and what they do not, in the two systems.", "p{0.27\\textwidth}p{0.32\\textwidth}p{0.32\\textwidth}",
                                         "Question & Northern cod & Edwards Aquifer", rows, small=True))

# ======================================================================= SI tables
# S1 data: cod
rows = []
yrs, ssb, cat = COD["data"]["years"], COD["data"]["ssb_kt"], COD["data"]["catch_kt"]
res_tr, res_oos = cf["residuals_train"], cf["residuals_oos"]
for i, y in enumerate(yrs):
    e = res_tr.get(str(y), res_oos.get(str(y)))
    rows.append([str(y), f(ssb[i], 2), f(cat[i], 3), f(e, 2) if e is not None else "--", "fit" if 1984 <= y <= 2007 else ("OOS" if y > 2007 else "--")])
w(SI / "gen_si_cod_data.tex", longtable("tab:si-cod-data", "Northern cod data (NCAM 2016 Table A2 SSB; Schijns et al. 2021 landings) and one-step residuals $e_{t+1}=S_{t+1}-[S_t+g(S_t)-C_t]$ of the registered source-year fit (residual listed under its destination year).",
                                         "rrrrl", "year & SSB (kt) & catch (kt) & residual (kt) & role", rows))
# S1 data: Edwards
rows = []
ey, eH, eR, eP = EDW["data"]["years"], EDW["data"]["H"], EDW["data"]["R"], EDW["data"]["P"]
etr, eoos = ef["residuals_train"], ef["residuals_oos"]
for i, y in enumerate(ey):
    e = etr.get(str(y), eoos.get(str(y)))
    rows.append([str(y), f(eH[i], 2), f(eR[i], 1), f(eP[i], 1), f(e, 2) if e is not None else "--", "fit" if 1935 <= y <= 1990 else ("OOS" if y > 1990 else "--")])
w(SI / "gen_si_edw_data.tex", longtable("tab:si-edw-data", "Edwards Aquifer annual panel 1934--2023 (J-17 mean head, ft AMSL; total recharge and well pumping, $10^3$ acre-ft) and residuals of the registered affine fit (destination year).",
                                         "rrrrrl", "year & $H$ & $R$ & $P$ & residual (ft) & role", rows))
# S2 quantile conventions
q = COD["quantiles"]
rows = []
for meth, lab in (("linear", "linear interpolation (declared)"), ("lower", "lower order statistic"), ("inverted_cdf", "inverted CDF"), ("hazen", "Hazen"), ("weibull", "Weibull")):
    e05, e10 = q["q05"][meth], q["q10"][meth]
    rows.append([lab, f(e05, 2), f(e10, 2), f(cc["g_Kstar"] - abs(e10), 2), f(cc["g_max"] - abs(e10), 2), f(cc["g_max"] - abs(e05), 2)])
notes = ("Sorted fit residuals (kt): " + ", ".join(f"{x:.1f}" for x in q["sorted_train"]) + ". The two collapse residuals (destination years 1992 and 1993) are the only ones below $-172.5$ kt; the declared q10 floor sits between the second and third order statistics, which is why the convention matters for q10 and not for q05.")
w(SI / "gen_si_quantiles.tex", table("tab:si-quantiles", "Cod floor classes under alternative quantile conventions ($n=24$ fit residuals) and the implied constants.", "lrrrrr",
                                      "convention & $e_{q05}$ & $e_{q10}$ & $C^*$ (q10) & $C_{\\mathrm{vac}}$ (q10) & $C_{\\mathrm{vac}}$ (q05)", rows, notes, placement="[H]"))
# S3 full cod kernels
rows = []
Ts = ["1", "2", "3", "5", "8", "10", "15", "20", "inf"]
for pid in ("flat_0", "BAU", "flat_25", "flat_50", "flat_75", "flat_100", "S1", "cpm", "graded2", "graded3"):
    for cid in ("UC_min", "UC_q05", "UC_q10"):
        k = kern[pid][cid]
        rows.append([SPOL[pid], CLS[cid]] + [bnd(k[t]) for t in Ts])
w(SI / "gen_si_cod_kernels.tex", longtable("tab:si-cod-kernels", "Northern cod: nominal kernel lower boundaries $b_T$ (kt) for every policy, floor class and horizon (exact backward recursion; $\\emptyset$ = empty).",
                                            "llrrrrrrrrr", "policy & class & $T{=}1$ & 2 & 3 & 5 & 8 & 10 & 15 & 20 & $\\infty$", rows))
# S3b exact bounded-defect boundaries
rows = []
for pid in ("flat_0", "BAU", "flat_25", "flat_50", "flat_75", "flat_100", "S1", "cpm", "graded2", "graded3"):
    for cid in ("UC_min", "UC_q05", "UC_q10"):
        d = ex[pid][cid]
        bb = d["boundaries_T1_20"]
        rows.append([SPOL[pid], CLS[cid], str(d["last_nonempty"])] + [bnd(bb[t - 1]) if t - 1 < len(bb) else "$\\emptyset$" for t in (1, 2, 3, 5, 8, 10, 12, 15, 20)])
w(SI / "gen_si_cod_exact.tex", longtable("tab:si-cod-exact", "Northern cod: exact bounded-defect kernel boundaries (kt) with $\\varepsilon=329.0$ kt on top of the floor class, and the last non-empty horizon $T^{\\mathrm{ex}}$.",
                                          "llrrrrrrrrrr", "policy & class & $T^{\\mathrm{ex}}$ & $T{=}1$ & 2 & 3 & 5 & 8 & 10 & 12 & 15 & 20", rows, size="\\scriptsize"))
# S4 family A regimes
rows = []
for phi, d in COD["family_A_q10"].items():
    rows.append([phi, f(d["C_at_LRP"], 2), f(d["margin"], 2), bnd(d["b_inf"]), d["regime"]])
notes = (f"Proportional rules $C=\\phi\\,g(S)$ above the LRP. Whole safe set iff $\\phi\\le\\phi^*_{{\\mathrm{{safe}}}}=1-|e|/g(\\theta)={cc['phi_star_safe']['UC_q10']:.4f}$; non-empty iff $\\phi\\le 1-|e|/g_{{\\max}}={cc['phi_star_nonempty']['UC_q10']:.4f}$ (q10 class). "
         "Earlier editions printed the second threshold (0.727) for the first claim; the structural campaign corrected it. "
         "$b_\\infty$ is the smallest fixed point $s_-$ of the worst-floor map (Theorem~\\mref{thm:kernel} of the main text); the archived structural campaign reports the "
         "finite-horizon proxies 1074.8 and 1568.4 kt for $\\phi=0.6$ and $0.7$, which lie below $s_-$ because the backward recursion of a "
         "proportional rule converges to $s_-$ only geometrically with ratio $1/F'(s_-)\\approx0.95$ and $0.98$.")
w(SI / "gen_si_family.tex", table("tab:si-family", "Cod proportional-harvest family under the q10 floor: catch at the LRP, margin $C^*-C(\\theta)$, $b_\\infty$ and regime.", "lrrrl",
                                   "$\\phi$ & $C(\\theta)$ & margin & $b_\\infty$ & regime", rows, notes, placement="[H]"))
# S5 finite floors cod
rows = []
for key, d in COD["finite_floors"].items():
    cid, pid = key.split("|")
    nm = {"BAU": "BAU (5 kt)", "flat_60": "flat 60 kt", "S1": "S1", "cpm": "cascade", "flat_120": "flat 120 kt"}[pid]
    rows.append([nm, CLS[cid]] + [bnd(d[n]) for n in ("5", "10", "15", "20")])
notes = "Lower boundary of the set of states from which $n$ consecutive floor years can be absorbed and the nominal (zero-residual) map then holds the safe set. For $C<g(\\theta)$ this coincides with the $n$-step kernel boundary $b_n$."
w(SI / "gen_si_cod_floors.tex", table("tab:si-cod-floors", "Cod: finite-duration floors.", "llrrrr", "policy & class & $n=5$ & 10 & 15 & 20", rows, notes, placement="[H]"))
# S6 profile grid (subset) + k-grid archived
rows = []
for row in pr["grid"]:
    Kv = row[0]
    if Kv in (1000.0, 1275.0, 1500.0, 1769.2, 1775.0, 2000.0, 2500.0, 3000.0, 4000.0, 5000.0, 7000.0, 10000.0, 20000.0, 50000.0):
        rows.append([f"{Kv:.0f}", f(row[1], 4), f(row[2] / pr["sse_min"], 4), f(row[3], 2), f(row[4], 4), f(row[3] - cls["UC_q10"], 2)])
notes = (f"Closed-form $r(K)$ at each $K$; SSE ratio relative to the profile minimum (attained at the top of the grid). Cuts: one-parameter {pr['F_cut_ratio_1par']:.4f}, two-parameter {pr['F_cut_ratio']:.4f}. "
         f"Expansion $F'(\\theta)>1$ iff $K>2\\theta=1769.2$ kt. Zero-budget point $(r,K)=({pr['zero_budget_point']['r_crit']:.5f},5000)$: SSE ratio {pr['zero_budget_point']['sse_ratio']:.4f} to the profile minimum ({pr['zero_budget_point']['sse_ratio_vs_committed']:.4f} to the committed fit) -- inside the two-parameter region, outside the one-parameter cut.")
w(SI / "gen_si_profile.tex", table("tab:si-profile", "Cod: profile of the one-step least-squares fit over $K$.", "rrrrrr", "$K$ (kt) & $r(K)$ & SSE ratio & $g(\\theta)$ & $F'(\\theta)$ & $C^*$", rows, notes, placement="[H]"))
# S7 bootstraps and obs-error
idn = AR["ident"]
rows = [
    ["fixed-$K$ (archived, $B=2000$)", f(bf["r_median"], 4), f"[{f(bf['r_q05_q95'][0],4)}, {f(bf['r_q05_q95'][1],4)}]", f(bf["Cstar_median"], 2), f"[{f(bf['Cstar_q05_q95'][0],2)}, {f(bf['Cstar_q05_q95'][1],2)}]", f"{bf['n_nonpositive']}/2000"],
    ["fixed-$K$ (independent seed, frozen floor)", f(bi["r_median"], 4), f"[{f(bi['r_q05_q95'][0],4)}, {f(bi['r_q05_q95'][1],4)}]", f(bi["frozen_floor"]["Cstar_median"], 2), f"[{f(bi['frozen_floor']['Cstar_q05_q95'][0],2)}, {f(bi['frozen_floor']['Cstar_q05_q95'][1],2)}]", pct(bi["frozen_floor"]["share_nonpositive"])],
    ["fixed-$K$ (independent seed, floor re-estimated)", f(bi["r_median"], 4), "--", f(bi["reestimated_floor"]["Cstar_median"], 2), f"[{f(bi['reestimated_floor']['Cstar_q05_q95'][0],2)}, {f(bi['reestimated_floor']['Cstar_q05_q95'][1],2)}]", pct(bi["reestimated_floor"]["share_nonpositive"])],
    ["joint $(r,K)$ (archived, $B=2000$)", f(bj["r_median"], 4), f"[{f(bj['r_q05_q95'][0],4)}, {f(bj['r_q05_q95'][1],4)}]", f(bj["Cstar_median"], 2), f"[{f(bj['Cstar_q05_q95'][0],2)}, {f(bj['Cstar_q05_q95'][1],2)}]", f"{bj['n_nonpositive']}/2000"],
    [f"joint, $K\\ge 2\\theta$ ({bj['n_K_ge_2Kstar']} refits)", "--", "--", f(bj["Cstar_median_given_2Kstar"], 2), f"[{f(bj['Cstar_q05_q95_given_2Kstar'][0],2)}, {f(bj['Cstar_q05_q95_given_2Kstar'][1],2)}]", f"{bj['n_nonpositive_given_2Kstar']}/{bj['n_K_ge_2Kstar']}"],
]
notes = (f"Joint design: median $K$ {bj['K_median']:.0f} kt, {pct(bj['share_pinned'])} of refits pinned at 5000 kt, {pct(bj['share_Fp_gt_1'])} expansive. "
         "Observation-error sensitivity (archived identification campaign; a share $\\lambda$ of residual variance attributed to measurement error and removed before the floor is taken): "
         + "; ".join(f"$\\lambda={l}$: {idn[f'obs-error|lambda = {l}'].replace('C* = ', '$C^*=$')}" for l in ("0.0", "0.1", "0.2", "0.3", "0.4", "0.5")) + " kt.")
w(SI / "gen_si_boot.tex", table("tab:si-boot", "Cod: residual bootstraps of the fit and of the constructive bound.", "lrrrrr", "design & $r$ median & $r$ 90\\% & $C^*$ median & $C^*$ 90\\% & $C^*\\le0$", rows, notes, placement="[H]", width="\\textwidth"))
# S8 forms + recent windows
rows = []
for fr in AR["fox"]:
    rows.append([esc(fr["form"]), fr["r"], fr["K"], fr["MSE_kt2"], fr["g_max"] or "--", fr["g_Kstar"] or "--", fr["Fp_Kstar"] or "--", fr["constructive_q10"] or "--"])
notes = ("Archived forms campaign (source-year basis). The Allee refit is a boundary solution ($r$ at its box edge of 2.0) and defines no admissible constants; the declared-$s_0$ Allee row and the data-preferred row give $C^*=123.3$ and $115.2$ kt and $C_{\\mathrm{vac}}=802.8$ and $291.5$ kt respectively (cadence campaign). "
         "Fox kernels under the worst floor: BAU $b_1=1047.7$, $b_5=1640.8$ kt, $T=\\infty$ empty, as for Schaefer.")
w(SI / "gen_si_forms.tex", table("tab:si-forms", "Cod: alternative surplus forms on the frozen window.", "lrrrrrrr", "form & $r$ & $K$ & MSE (kt$^2$) & $g_{\\max}$ & $g(\\theta)$ & $F'(\\theta)$ & $C^*$ (q10)", rows, notes, placement="[H]", width="\\textwidth"))
rows = []
rw = COD["recent_windows"]
for lab in ("NCAM 1995-2015", "NCAM 1995-2007"):
    d = rw[lab]
    rows.append([lab + " (exact profile minimiser)", str(d["n"]), f(d["r"], 4), f(d["K"], 1), f(d["g_LRP"], 1), f(d["e_q10"], 1), f(d["e_min"], 1), f(d["C_star"], 1), f(d["C_star_worst"], 1), f(d["Fp"], 3), f(d["sd"], 1)])
    k5 = d["at_K_5000"]
    rows.append([lab + " ($K$ held at 5000)", str(d["n"]), f(k5["r"], 4), "5000.0", f(k5["g_LRP"], 1), f(k5["e_q10"], 1), "--", f(k5["C_star"], 1), "--", f(k5["Fp"], 3), "--"])
for lab2, rr in AR["recent"].items():
    if lab2.startswith("xte"):
        rows.append([lab2 + " (archived; LRP 276 kt)", fi(rr["n"]), f(rr["r"], 4), f(rr["K"], 1), f(rr["g_LRP"], 1), f(rr["e_q10"], 1), f(rr["e_min"], 1), f(rr["Cstar"], 1), f(rr["Cstar_worst"], 1), f(rr["Fp"], 3), f(rr["sd"], 1)])
notes = ("Refits on post-moratorium windows (source-year convention). For 1995--2015 the SSE profile is flat to within 0.001\\% between $K=4317$ (exact minimiser) and the box edge where the archived optimiser stopped; both rows are shown. "
         "xteNCAM rows use the 2024 assessment series (Regular et al. 2025) with its own LRP of 276 kt; $K$ sits at the lower bound of the box and the reference point is not self-viable under either floor.")
w(SI / "gen_si_windows.tex", table("tab:si-windows", "Cod: refits on recent windows.", "lrrrrrrrrrr", "window & $n$ & $r$ & $K$ & $g(\\theta)$ & $e_{q10}$ & $e_{\\min}$ & $C^*$ & $C^*_{\\mathrm{worst}}$ & $F'(\\theta)$ & SD", rows, notes, placement="[H]", width="\\textwidth"))
# S9 stochastic grid
rows = []
for scheme in ("iid", "block4", "iid_no1992"):
    for S0 in ("884.6", "861.9", "1000", "1500"):
        for T in ("5", "10", "20"):
            r = [scheme.replace("_", "-"), S0, T]
            ok = False
            for pid in ("BAU", "flat_0", "flat_25", "flat_50", "S1", "cpm"):
                k = f"{scheme}|{pid}|S0={S0}|T={T}"
                if k in st:
                    r.append(f(st[k], 4))
                    ok = True
                else:
                    r.append("--")
            if ok:
                rows.append(r)
w(SI / "gen_si_stoch.tex", longtable("tab:si-stoch", "Cod stochastic layer (archived campaign, $N=20\\,000$ per cell): probability of staying at or above the LRP through $T$ years from $S_0$.",
                                      "llrrrrrrr", "scheme & $S_0$ & $T$ & BAU & zero & 60 kt & 120 kt & S1 & cascade", rows,
                                      "Constructive-bound scan (flat catch $C$ from the LRP, 20 years): survival crosses 0.9 at " + f"{f(cr['iid']['0.9'])} kt (i.i.d.), never (blocks), {f(cr['iid_no1992']['0.9'])} kt (no 1992); 0.8 at {f(cr['iid']['0.8'])} / {f(cr['block4']['0.8'])} / {f(cr['iid_no1992']['0.8'])} kt; at 92.5 kt survival is {f(cr['iid']['P_at_92.5'],3)} / {f(cr['block4']['P_at_92.5'],3)} / {f(cr['iid_no1992']['P_at_92.5'],3)}."))
# S10 Edwards kernels full
rows = []
for thr in ("K_phys_618", "K_inst_660"):
    for pid in ("BAU", "flat_90", "flat_80", "flat_70", "flat_60", "flat_50", "flat_0", "S1", "cpm"):
        for cid in ("UC_min", "UC_q05", "UC_q10"):
            d = kn[thr][pid][cid]
            dc = kc[pid][cid] if thr == "K_phys_618" else EDW["kernels_certified"]["K_inst_660"][pid][cid]
            rows.append([thr.split("_")[-1], ESPOL[pid], CLS[cid], bnd(d["1"]), bnd(d["2"]), bnd(d["3"]), bnd(d["5"]), bnd(d["8"]), bnd(d["10"]), str(d["first_empty"]) if d["first_empty"] else "never",
                         bnd(dc.get("1")), bnd(dc.get("2")), bnd(dc.get("3")), bnd(dc.get("4")), bnd(dc.get("5"))])
w(SI / "gen_si_edw_kernels.tex", longtable("tab:si-edw-kernels", "Edwards Aquifer: nominal kernel boundaries (ft) by threshold, policy, floor and horizon, first empty horizon, and Lipschitz-certified boundaries at $T=1$--$5$ ($\\varepsilon=15.41$ ft).",
                                            "lllrrrrrrlrrrrr", "thr. & policy & floor & $T{=}1$ & 2 & 3 & 5 & 8 & 10 & empty & cert.\\,1 & 2 & 3 & 4 & 5", rows, size="\\scriptsize", colsep="2.5pt"))
# S11 bounded error
rows = []
for pid in ("BAU", "flat_90", "flat_80", "S1", "cpm", "flat_0"):
    for lab in ("train", "oos"):
        d = be[pid][f"UC_min|{lab}"]
        bb = d["boundaries"]
        rows.append([EPOL[pid], "15.41 (fit)" if lab == "train" else "21.81 (OOS)"] + [bnd(bb[t]) if t < len(bb) else "$\\emptyset$" for t in range(5)] + [str(d["first_empty"]) if d["first_empty"] else "$>8$"])
dep = [r for r in EDW["lipschitz_vs_exact_identity"]["rows"] if not r["equal"]]
PN = {"BAU": "BAU", "flat_90": "flat 90\\%", "flat_80": "flat 80\\%", "flat_60": "flat 60\\%", "S1": "Stage I", "cpm": "cascade", "flat_0": "zero pumping"}
be_notes = ("Fit-window defect $\\varepsilon=15.41$ ft; out-of-sample defect $21.81$ ft; threshold 618 ft, ceiling 710 ft, recharge pinned at the 1956 floor. "
            "For positive flat-cap rules the fit-window rows coincide with the Lipschitz-certified boundaries of Table~\\ref{tab:si-edw-kernels} at every reported horizon; zero pumping coincides from $T=3$ onward (Proposition~\\mref{prop:lip}(ii)). "
            "Departures (exact vs certified, ft): " + "; ".join(f"{PN[r['policy']]} $T={r['T']}$: {r['exact']:.1f} vs {r['inflated']:.1f}" for r in dep) + ". "
            "For zero pumping the certificate's inflated initial-state constraint binds at $T=1,2$; for the staged rules the closed-loop map is piecewise affine. These boundary departures do not change a horizon.")
w(SI / "gen_si_edw_be.tex", table("tab:si-edw-be", "Edwards: exact bounded-defect kernel boundaries at 618 ft (worst floor) for the fit-window and out-of-sample defects.", "llrrrrrr",
                                   "policy & $\\varepsilon$ (ft) & $T{=}1$ & 2 & 3 & 4 & 5 & first empty", rows, be_notes, placement="[H]"))
# S12 replays etc.
rows = []
rep = EDW["replay_1950s"]
for pid in ("BAU", "flat_90", "flat_80", "flat_70", "flat_60", "flat_50", "flat_0", "S1", "cpm"):
    rows.append([EPOL[pid], f(rep[pid]["min_head"], 2), f(cl[pid]["train_1934_1990"]["min_head"], 2) if pid in cl else "--", f(cl[pid]["train_1934_1990"]["end_head"], 2) if pid in cl else "--",
                 f(cl[pid]["oos_1991_2023"]["end_head"], 2) if pid in cl else "--", f(EDW["floor_class_supply"].get(pid, {}).get("mean_P"), 2) if pid in EDW["floor_class_supply"] else "--"])
dg = EDW["fit_diagnostic_1950s"]
notes = ("1950s replay: model from the observed 1950 head with actual 1951--1956 recharge and the rule's pumping (minimum head reached; observed 1956 minimum 623.15 ft). Closed loop: observed recharge, rule pumping, from the 1934 head (fit) or 1990 head (OOS); observed end heads 645.8 (1990) and 635.7 (2023) ft. "
         f"Floor-class supply: 57 closed-loop years with recharge pinned at the worst floor from the 1934 head. Open-loop fit diagnostic with actual pumping: maximum absolute error {dg['max_abs_error']:.1f} ft (1956: model {dg['model_1956']:.1f}, observed {dg['observed_1956']:.1f}). "
         f"Stage occupancy of observed heads below 660/650/640/630 ft: fit window {EDW['occupancy']['train']['counts']} of 57; out of sample {EDW['occupancy']['oos']['counts']} of 33. "
         f"Finite-duration floors at 618 ft (worst floor then mean recharge {EDW['R_bar_train']:.1f}): BAU $n=5$: {f(EDW['finite_floors']['BAU|UC_min']['5'])} ft, $n=10$: {f(EDW['finite_floors']['BAU|UC_min']['10'])} ft, $n=15$: empty; every cut policy: whole safe set.")
w(SI / "gen_si_edw_replays.tex", table("tab:si-edw-replays", "Edwards: replays, closed-loop end heads and floor-class supply.", "lrrrrr", "policy & 1950s min. head & closed-loop min. 1934--90 & end 1990 & end 2023 & floor-class supply", rows, notes, placement="[H]", width="\\textwidth"))
# S13 attractor bootstrap
rows = []
for d in AR["edw_audit_bootstrap"]["per_policy"]:
    rows.append([esc(d["policy"]), f(d["attractor_point"], 2), f(d["boot_mean"], 2), f(d["boot_sd"], 2), f"[{f(d['boot_q05_q50_q95'][0],2)}, {f(d['boot_q05_q50_q95'][1],2)}, {f(d['boot_q05_q50_q95'][2],2)}]", f(d["p_attractor_ge_618"], 4)])
gap = EDW["bootstrap_independent"]["gap_flat90_minus_BAU_q05_q50_q95"]
notes = (f"Archived audit layer, 5000 replications, seed 20260905, no non-contractive replicate. Independent re-run (seed 20261015): $P(H^*\\ge618)$ BAU {f(bi_e['BAU'],3)}, flat 90\\% {f(bi_e['flat_90'],3)}, flat 80\\% {f(bi_e['flat_80'],3)}, flat 60\\% {f(bi_e['flat_60'],3)}, zero {f(bi_e['flat_0'],3)}; "
         f"the flat-90\\% minus BAU attractor gap has 90\\% interval [{gap[0]:.1f}, {gap[2]:.1f}] ft (point value 3.16 ft).")
w(SI / "gen_si_edw_boot.tex", table("tab:si-edw-boot", "Edwards: residual bootstrap of the worst-floor attractors.", "lrrrlr", "policy & $H^*$ & mean & SD & [q05, q50, q95] & $P(H^*\\ge618)$", rows, notes, placement="[H]"))
# S14 verification record
chk = R["archive_checks"]
groups = {}
for cck in chk:
    g = cck["check"].split(" ")[0] + " " + cck["check"].split(" ")[1]
    groups.setdefault(g, [0, 0])
    groups[g][0] += 1
    groups[g][1] += int(cck["ok"])
rows = [[esc(g), str(v[0]), str(v[1])] for g, v in sorted(groups.items())]
rows.append(["MIDRULE"][0] if False else "MIDRULE")
rows.append(["total", str(len(chk)), str(sum(int(c["ok"]) for c in chk))])
w(SI / "gen_si_checks.tex", table("tab:si-checks", "Agreement of the independent core with the registered artefacts, by group.", "lrr", "group & checks & passed", rows,
                                   "Tolerances: closed-form constants $10^{-3}$--$10^{-6}$; kernel boundaries 0.05 kt / 0.01 ft (0.2 kt at $T=20$); Monte-Carlo and bootstrap quantities re-run with an independent seed, tolerances 0.015--0.02 in probability and 3 kt in the bootstrap median.", placement="[H]"))
print("tables written")

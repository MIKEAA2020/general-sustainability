#!/usr/bin/env python3
"""Figures for paperE1 v69 (main Figs 1-6, SI Figs S1-S3), regenerated from the
archived data and per-origin result files. Deterministic; no refitting except
the Schaefer curves drawn from the archived fitted parameters.

Run from anywhere:  python3 make_figures.py
Outputs:            ../figs/fig*.pdf and .png
"""
import json, os, numpy as np, pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

HERE = os.path.dirname(os.path.abspath(__file__))
RERUN = os.path.join(HERE, "rerun")
DATA = os.path.join(RERUN, "data")
RES = os.path.join(RERUN, "results")
import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
# repo root: set GS_REPO, or rely on the standard location  <repo>/arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v69_src/work/
_REPO = _os.environ.get('GS_REPO', _os.path.abspath(_os.path.join(_HERE, '..', '..', '..', '..', '..')))
ARCH = _os.path.join(_REPO, "wave_e_cod", "results")
DMCSV = _os.path.join(_REPO, "batch 7 (audits of agent arena 1 paper rewrites)", "results", "e1_dm_uncertainty_regime.csv")
FIGS = os.path.join(HERE, "..", "figs")
os.makedirs(FIGS, exist_ok=True)

plt.rcParams.update({
    "font.size": 9, "axes.titlesize": 9.5, "axes.labelsize": 9, "legend.fontsize": 8,
    "xtick.labelsize": 8, "ytick.labelsize": 8, "axes.spines.top": False,
    "axes.spines.right": False, "figure.dpi": 150, "savefig.dpi": 300,
    "pdf.fonttype": 42, "lines.linewidth": 1.4,
})
COL = {"persist": "#111111", "M1": "#b2182b", "M1b": "#ef8a62", "M2": "#2166ac",
       "M3": "#1b7837", "M4": "#d8a200", "mean": "#999999"}
LBL = {"M1": "M1 autonomous", "M1b": "M1b Allee", "M2": "M2 stock-flow",
       "M3": "M3 residual", "M4": "M4 lagged start", "persist": "persistence"}
MODELS = ["M1_autonomous_Schaefer", "M1b_autonomous_Allee", "M2_stockflow_regimeC",
          "M3_AR_residual", "M4_delayed_info"]
SHORT = {m: m.split("_")[0] for m in MODELS}


def save(fig, name):
    for ext in ("pdf", "png"):
        fig.savefig(os.path.join(FIGS, f"{name}.{ext}"), bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)


a2 = pd.read_csv(os.path.join(DATA, "ncam_2016_table_a2.csv"))
xte = pd.read_csv(os.path.join(DATA, "xtencam_table17_ssb.csv"))
cat = pd.read_csv(os.path.join(DATA, "catch_schijns_2021.csv"))
LRP_A = float(a2.loc[(a2.year >= 1983) & (a2.year <= 1989), "ssb_kt"].mean())
LRP_B = 276.0
assert abs(LRP_A - 884.58) < 0.01

# ---------------------------------------------------------------- Fig 1
fig, axes = plt.subplots(2, 1, figsize=(6.6, 5.6), gridspec_kw={"height_ratios": [1, 1.15]})
ax = axes[0]
ax.axvspan(1991, 1995, color="#fddbc7", alpha=0.7, lw=0, label="collapse test window 1991–1995")
ax.axvspan(2008, 2015, color="#d1e5f0", alpha=0.8, lw=0, label="recovery test window 2008–2015")
ax.axhline(LRP_A, color="#b2182b", ls="--", lw=1, label=f"LRP, 1983–1989 mean = {LRP_A:.1f} kt")
ax.axvline(1992.5, color="#762a83", ls=":", lw=1, label="moratorium, July 1992")
ax.plot(a2.year, a2.ssb_kt, "-o", color="#1f3b5c", ms=3.2, lw=1.5, label="NCAM M-shift SSB (Table A2)")
ax.set_ylabel("SSB (kt)")
ax.set_xlim(1982.5, 2015.5); ax.set_ylim(0, 1100)
ax.set_title("(a) Specification A: NCAM M-shift SSB, 1983–2015", loc="left")
ax.legend(loc="upper right", frameon=False, ncol=1)
ax = axes[1]
ax.fill_between(xte.year, xte.ssb_lo, xte.ssb_hi, color="#4393c3", alpha=0.18, lw=0, label="xteNCAM 95% interval")
ax.plot(xte.year, xte.ssb_kt, color="#1f3b5c", lw=1.6, label="xteNCAM SSB (Table 17)")
ax.plot(a2.year, a2.ssb_kt, "--", color="#b8860b", lw=1.1, label="NCAM 2016 (Specification A), not pooled")
ax.axhline(LRP_A, color="#b2182b", ls=":", lw=1, label="884.6 kt (Specification A threshold)")
ax.axhline(LRP_B, color="#b2182b", ls="--", lw=1, label="$B_{\\mathrm{lim}}$ = 276 kt (Specification B threshold)")
ax.axvspan(1990, 1995, color="#fddbc7", alpha=0.7, lw=0)
ax.axvspan(2013, 2024, color="#d1e5f0", alpha=0.8, lw=0)
ax.set_xlim(1953, 2025); ax.set_ylim(0, 1850)
ax.set_ylabel("SSB (kt)"); ax.set_xlabel("Year")
ax.set_title("(b) Specification B: xteNCAM SSB, 1954–2024 (test windows 1990–1995 and 2013–2024 shaded)", loc="left")
ax.legend(loc="upper right", frameon=False)
fig.tight_layout()
save(fig, "fig1_series")

# ---------------------------------------------------------------- Fig 2 (gap vs persistence, % of persistence RMSE, with CIs)
dm = pd.read_csv(DMCSV)
dm["mod"] = dm.A.str.split().str[0]
fig, axes = plt.subplots(1, 4, figsize=(7.2, 2.9), sharey=False)
panels = [("A", 1), ("A", 5), ("B", 1), ("B", 5)]
for ax, (spec, h) in zip(axes, panels):
    sub = dm[(dm.spec == spec) & (dm.horizon == h) & (dm.B == "naive persist")].copy()
    sub = sub.set_index("mod").loc[["M1", "M1b", "M2", "M3", "M4"]]
    base = sub.RMSEb.iloc[0]
    x = np.arange(5)
    y = 100 * sub.gap_kt / base
    lo = 100 * sub.ci95_lo / base; hi = 100 * sub.ci95_hi / base
    ax.axhspan(-5, 0, color="#eeeeee", lw=0)
    ax.axhline(0, color="k", lw=0.8)
    ax.axhline(-5, color="#555555", lw=0.8, ls="--")
    for i, m in enumerate(sub.index):
        ax.errorbar(i, y.iloc[i], yerr=[[y.iloc[i] - lo.iloc[i]], [hi.iloc[i] - y.iloc[i]]],
                    fmt="o", color=COL[m], ms=5, capsize=2.5, lw=1.1)
    ax.set_xticks(x); ax.set_xticklabels(sub.index, rotation=0)
    ax.set_title(f"Spec. {spec}, $h={h}$ ($n={int(sub.n.iloc[0])}$)\npersistence {base:.0f} kt", loc="left")
    ax.set_xlim(-0.6, 4.6)
    ymax = max(hi.max() * 1.08, 30)
    ax.set_ylim(min(lo.min() * 1.15, -12), ymax)
axes[0].set_ylabel("RMSE gap, module − persistence\n(% of persistence RMSE)")
fig.tight_layout()
save(fig, "fig2_gaps")

# ---------------------------------------------------------------- Fig 3 (fixed-window trajectories, primary pass)
with open(os.path.join(RES, "paths.json")) as f:
    paths = json.load(f)
fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0))
for ax, (wname, title, train_end_year) in zip(axes, [("collapse", "(a) Collapse window: train 1983–1990, test 1991–1995", 1990),
                                                     ("recovery", "(b) Recovery window: train 1995–2007, test 2008–2015", 2007)]):
    S_origin = float(a2.loc[a2.year == train_end_year, "ssb_kt"].iloc[0])
    first = True
    for m in MODELS:
        p = paths["regime"][f"{wname}:{m}"]
        yrs = [train_end_year] + p["year"]; pred = [S_origin] + p["pred"]
        ls = "-"
        if wname == "recovery" and m == "M2_stockflow_regimeC":
            ls = (0, (4, 2))  # coincides with M1 on this window
        ax.plot(yrs, pred, ls=ls, color=COL[SHORT[m]], label=LBL[SHORT[m]], lw=1.3)
        if first:
            obs_y = [train_end_year] + p["year"]; obs = [S_origin] + p["obs"]
            first = False
    ax.plot(obs_y, [S_origin] * len(obs_y), color=COL["persist"], ls=":", lw=1.2, label="persistence")
    ax.plot(obs_y, obs, "-o", color="k", ms=3.5, lw=1.6, label="observed SSB")
    ax.axhline(LRP_A, color="#b2182b", ls="--", lw=0.8)
    ax.set_title(title, loc="left", fontsize=8.5)
    ax.set_xlabel("Year"); ax.set_ylabel("SSB (kt)")
axes[0].set_ylim(0, 1150); axes[1].set_ylim(0, 1000)
axes[0].legend(frameon=False, loc="center right", fontsize=7)
fig.tight_layout()
save(fig, "fig3_windows")

# ---------------------------------------------------------------- Fig 4 (period structure of the one-step error)
regA = pd.read_csv(os.path.join(ARCH, "rolling_forecasts_regime.csv"))
rollB = pd.read_csv(os.path.join(RES, "xte_rolling_forecasts.csv"))
SA = dict(zip(a2.year, a2.ssb_kt)); SB = dict(zip(xte.year, xte.ssb_kt))
fig, axes = plt.subplots(2, 1, figsize=(6.8, 5.8))
for ax, df, S, spec, band, xlim in [(axes[0], regA, SA, "A", (1990, 1995), (1989.3, 2014.7)),
                                    (axes[1], rollB, SB, "B", (1991, 1995), (1964.3, 2023.7))]:
    sub = df[df.horizon == 1]
    origins = np.array(sorted(sub.origin.unique()))
    pe = np.array([abs(S[o] - S[o + 1]) for o in origins])
    ax.axvspan(band[0] - 0.5, band[1] + 0.5, color="#fddbc7", alpha=0.7, lw=0)
    ax.axvspan(1995.5, 2012.5, color="#f0f0f0", lw=0)
    ax.plot(origins, pe, "-", color="k", lw=1.8, label="persistence")
    for m, mk in [("M1_autonomous_Schaefer", "s"), ("M2_stockflow_regimeC", "^"), ("M3_AR_residual", "o")]:
        mm = sub[sub.model == m].sort_values("origin")
        err = np.abs(mm.pred.values - mm.obs.values)
        floor = mm.pred.values < 1e-2
        ax.plot(mm.origin, err, "-", color=COL[SHORT[m]], lw=1.0, alpha=0.9, label=LBL[SHORT[m]])
        ax.plot(mm.origin[~floor], err[~floor], mk, color=COL[SHORT[m]], ms=3.2, lw=0)
        ax.plot(mm.origin[floor], err[floor], mk, mfc="white", mec=COL[SHORT[m]], ms=3.6, lw=0)
    ax.set_yscale("log"); ax.set_ylim(1.0, 1500); ax.set_xlim(*xlim)
    ax.set_ylabel("|one-step error| (kt)")
    ax.set_title(f"Specification {spec}: one-step absolute error by forecast origin", loc="left")
axes[1].set_xlabel("Forecast origin")
h, l = axes[0].get_legend_handles_labels()
h += [Patch(color="#fddbc7", label="collapse band"), Patch(color="#f0f0f0", label="1996–2012 band"),
      plt.Line2D([], [], marker="s", mfc="white", mec="#555", ls="", label="open marker: forecast at the numerical floor")]
fig.legend(handles=h, frameon=False, ncol=4, fontsize=7.5, loc="lower center", bbox_to_anchor=(0.5, -0.02))
fig.tight_layout(rect=(0, 0.05, 1, 1))
save(fig, "fig4_period")

# ---------------------------------------------------------------- Fig 5 (apparent net production)
yrs = a2.year.values; S = a2.ssb_kt.values
c_reg = np.where(yrs <= 1991, 240.0, np.where(yrs == 1992, 120.0, 5.0))
c_ann = cat.set_index("year").loc[yrs, "catch_kt"].values
P_reg = S[1:] - S[:-1] + c_reg[:-1]; P_ann = S[1:] - S[:-1] + c_ann[:-1]
fig, ax = plt.subplots(figsize=(6.4, 3.9))
grid = np.linspace(0, 1100, 400)
for (r, K, lab, ls) in [(1.9350, 1032.7, "collapse-window fit ($r=1.935$, $K=1032.7$ kt)", "-"),
                        (0.4581, 500.0, "recovery-window fit, coarse regime ($r=0.458$, $K=500$ kt)", "--"),
                        (0.3697, 5000.0, "recovery-window fit, annual landings ($r=0.370$, $K=5000$ kt)", ":")]:
    ax.plot(grid, r * grid * (1 - grid / K), ls=ls, color="#2166ac" if ls == "-" else ("#1b7837" if ls == "--" else "#762a83"), lw=1.4, label=lab)
ax.axhline(0, color="k", lw=0.7)
ax.plot(S[:-1], P_reg, "o", mfc="none", mec="#333", ms=5, label="observed, coarse regime")
ax.plot(S[:-1], P_ann, "^", color="#d6604d", ms=4.5, label="observed, annual landings")
for y in (1991, 1992, 1993):
    i = int(np.where(yrs == y)[0][0])
    ax.annotate(str(y), (S[i], P_reg[i]), xytext=(6, -3), textcoords="offset points", fontsize=7.5, color="#b2182b")
ax.set_xlabel("SSB $S_t$ (kt)"); ax.set_ylabel("apparent net production $P_t=S_{t+1}-S_t+C_t$ (kt)")
ax.set_ylim(-650, 560); ax.set_xlim(-20, 1120)
ax.legend(frameon=False, loc="lower left", fontsize=7.2)
fig.tight_layout()
save(fig, "fig5_production")

# ---------------------------------------------------------------- Fig 6 (operating characteristics, 7 processes)
rows = ["D1 autonomous, collapse fit (truth M1)", "D2 autonomous, recovery fit (truth M1)",
        "D3 stock-flow (truth M2)", "D4 depensation, $\\mathfrak{s}=15$ kt (truth M1b)",
        "D5 persistence-true (no structure)", "D6 drifting productivity (outside class)",
        "D7 smooth path + observation error (outside class)"]
vals = np.array([[0.965, 0.985], [0.710, 0.130], [0.090, 0.110], [0.005, 0.015],
                 [0.015, 0.030], [0.680, 0.760], [0.975, 0.925]])
good = np.array([[1, 1], [0, 0], [0, 0], [0, 0], [1, 1], [0, 0], [0, 0]])  # meets pre-declared bar
fig, ax = plt.subplots(figsize=(7.2, 3.5))
cmap = plt.get_cmap("Blues")
im = ax.imshow(vals, cmap=cmap, vmin=0, vmax=1, aspect="auto")
for i in range(vals.shape[0]):
    for j in range(2):
        txt = f"{vals[i, j]:.3f}"
        if i <= 3:
            mark = "✓" if vals[i, j] >= 0.80 else ("~" if vals[i, j] >= 0.30 else "✗")
        else:
            mark = "✓" if vals[i, j] <= 0.10 else "✗"
        ax.text(j, i, f"{txt}  {mark}", ha="center", va="center", fontsize=8.5,
                color="white" if vals[i, j] > 0.55 else "black")
ax.set_xticks([0, 1]); ax.set_xticklabels(["$\\sigma=11.8$ kt", "$\\sigma=33.8$ kt"])
ax.set_yticks(range(7)); ax.set_yticklabels(rows, fontsize=8)
ax.axhline(3.5, color="k", lw=0.8); ax.axhline(4.5, color="k", lw=0.8)
ax.text(1.62, 1.5, "power\nP(true module retained)\npre-declared bar: ≥ 0.80\n✓ met, ~ 0.30–0.80, ✗ < 0.30", va="center", fontsize=7.5)
ax.text(1.62, 4.0, "false retention, in-class null\nP(any module retained)\nbar: ≤ 0.10", va="center", fontsize=7.5)
ax.text(1.62, 5.5, "false retention, truth outside the class\nP(any module retained)\nbar: ≤ 0.10", va="center", fontsize=7.5)
ax.set_xlim(-0.5, 3.4)
ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
ax.tick_params(length=0)
fig.tight_layout()
save(fig, "fig6_operating")

# ---------------------------------------------------------------- Fig S1 (Allee profile)
prof = pd.read_csv(os.path.join(ARCH, "allee_profile.csv"))
fig, axes = plt.subplots(1, 2, figsize=(6.8, 2.8))
for tr, c in [("coarse regime", "#2166ac"), ("annual landings", "#d6604d")]:
    p = prof[prof.treatment == tr]
    axes[0].plot(p.s_kt, p.profile_mse, color=c, label=tr)
    axes[1].plot(p.s_kt, p.K_kt, color=c, label=tr)
axes[0].set_xlabel("fixed Allee threshold $\\mathfrak{s}$ (kt)"); axes[0].set_ylabel("profile one-step MSE (kt$^2$)")
axes[0].set_title("(a) Profile objective, recovery window 1995–2007", loc="left", fontsize=8.5)
axes[1].set_xlabel("fixed Allee threshold $\\mathfrak{s}$ (kt)"); axes[1].set_ylabel("re-optimised $K$ (kt)")
axes[1].set_title("(b) Compensating carrying capacity ($r$ at its bound of 2 throughout)", loc="left", fontsize=8.5)
axes[0].legend(frameon=False)
fig.tight_layout()
save(fig, "figS1_allee_profile")

# ---------------------------------------------------------------- Fig S2 (three vintages of the same years)
ram = pd.read_csv(_os.path.join(_REPO, "arena agent 1", "paper rewrites", "latex", "paperE1_calibration_data_v1_ram_timeseries.csv"))
ram = ram[ram.SSB.notna()][["year", "SSB"]]; ram["SSB"] = ram.SSB / 1000.0
fig, ax = plt.subplots(figsize=(6.4, 3.2))
ax.plot(a2.year, a2.ssb_kt, "-o", ms=2.8, color="#b8860b", label="NCAM 2016 vintage (Table A2), 1983–2015")
ax.plot(ram.year, ram.SSB, "-s", ms=2.8, color="#1b7837", label="RAM Legacy v4.66 (2021 vintage, same model family), 1983–2021")
ax.plot(xte.year, xte.ssb_kt, "-", color="#1f3b5c", lw=1.4, label="xteNCAM (2024 vintage, revised framework)")
ax.axhline(LRP_A, color="#b2182b", ls=":", lw=1, label="884.6 kt (1983–1989 mean, 2016 vintage)")
ax.axhline(790.0, color="#b2182b", ls="-.", lw=1, label="790.0 kt (1983–1989 mean, 2021 vintage)")
ax.axhline(LRP_B, color="#b2182b", ls="--", lw=1, label="$B_{\\mathrm{lim}}$ = 276 kt (2024 framework)")
ax.axvspan(2015.5, 2021.5, color="#d1e5f0", alpha=0.8, lw=0)
ax.set_xlim(1982, 2025); ax.set_ylim(0, 1050)
ax.set_xlabel("Year"); ax.set_ylabel("SSB (kt)")
ax.legend(frameon=True, framealpha=0.95, edgecolor="none", fontsize=6.6, loc="upper right", bbox_to_anchor=(1.0, 0.86))
fig.tight_layout()
save(fig, "figS2_vintages")

# ---------------------------------------------------------------- Fig S3 (fixed windows, annual landings pass)
fig, axes = plt.subplots(1, 2, figsize=(7.0, 3.0))
for ax, (wname, title, train_end_year) in zip(axes, [("collapse", "(a) Collapse window, annual landings", 1990),
                                                     ("recovery", "(b) Recovery window, annual landings", 2007)]):
    S_origin = float(a2.loc[a2.year == train_end_year, "ssb_kt"].iloc[0])
    first = True
    for m in MODELS:
        p = paths["annual"][f"{wname}:{m}"]
        yrs_ = [train_end_year] + p["year"]; pred = [S_origin] + p["pred"]
        ax.plot(yrs_, pred, color=COL[SHORT[m]], label=LBL[SHORT[m]], lw=1.3)
        if first:
            obs_y = [train_end_year] + p["year"]; obs = [S_origin] + p["obs"]; first = False
    ax.plot(obs_y, [S_origin] * len(obs_y), color="k", ls=":", lw=1.2, label="persistence")
    ax.plot(obs_y, obs, "-o", color="k", ms=3.5, lw=1.6, label="observed SSB")
    ax.set_title(title, loc="left", fontsize=8.5); ax.set_xlabel("Year"); ax.set_ylabel("SSB (kt)")
axes[0].set_ylim(0, 1150); axes[1].set_ylim(0, 1600)
axes[0].legend(frameon=False, loc="center right", fontsize=7)
fig.tight_layout()
save(fig, "figS3_windows_annual")

# ------------------------------------------------- numeric cross-checks printed for the record
r, K = 1.9350300501986595, 1032.716564304809
Sm = lambda C: (K / 2) * (1 - np.sqrt(1 - 4 * C / (r * K)))
Sp = lambda C: (K / 2) * (1 + np.sqrt(1 - 4 * C / (r * K)))
print("repeller at C=240/120/5:", [round(Sm(c), 1) for c in (240, 120, 5)], " attractor at 240:", round(Sp(240), 1))
print("F'(S*) at attractor:", round(1 + r * (1 - 2 * Sp(240) / K), 3), " map maximum at:", round(K / 2 * (1 + 1 / r), 1))
print("rK/4 =", round(r * K / 4, 1))
print("persistence errors in outcome years from RAM 2015 origin (277):", [abs(v - 277) for v in (340, 433, 394, 419, 440, 411)])

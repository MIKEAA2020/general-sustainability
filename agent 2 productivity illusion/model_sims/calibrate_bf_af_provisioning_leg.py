"""
Provisioning-book leg: calibrate the fast-book yield b_f and fast provisioning area
A_f, and evaluate the composition-diagnostic sign.

This is a DIFFERENT object from the regeneration-timescale legs (S5.3a: forest +
fishery, which estimate rho / tau_g, the ecological recovery of capital land).  Here
we calibrate the food-supply / provisioning subsystem of the model -- the fast
provisioning area A_f and its flow yield b_f.

The manuscript's observation operator (Section 12.3) is:

    A_f(t) = FAOSTAT arable + permanent crops (element Area, world, 1961-2022)
    b_f(t) = crop production / A_f(t), normalised to the base year

Two measures of the yield channel are reported, because they answer the same
question (does intensification dominate land expansion?) from independent data:

  (1) CEREM SENTINEL (physical).  FAOSTAT cereal yield (t/ha), world, continuous,
      no splicing.  This is the numerator used to reproduce the manuscript's
      Section 12.3 decomposition (d ln b_f = +1.128, d ln A_f = +0.160, weighted to
      d ln B = +0.207).

  (2) NFA CROPLAND BIOCAPACITY (model units).  The National Footprint & Biocapacity
      Accounts world cropland biocapacity (gha) -- b_f = CroplandBiocap / A_f --
      in the model's own units (gha*ha^-1*yr^-1), fully measured, no unidentified
      share alpha.  Source: the NFA country/land-type trends file (Country_Trends.csv,
      Record = 'BiocapTotGHA', column = 'Cropland'), world, 1961-2022.  This pins the
      ABSOLUTE b_f(1961) = 0.93 gha*ha^-1*yr^-1, which the alpha-anchored route could
      not (the cropland biocapacity IS the cropland share of B).

The two measures differ in level (physical t/ha vs. gha*/ha, which embeds the
cropland equivalence factor ~2.5) and in growth (3.09x vs 2.43x), but agree on the
qualitative conclusion: d ln b_f >> d ln A_f, i.e. intensification dominates.

Caveat on units: only the INDEX / sign of the yield channel and the composition-premium
sign are robust; the absolute b_f now comes from the measured cropland biocapacity and
no longer depends on the unidentified share alpha.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
EMP = os.path.join(ROOT, "data", "empirical")
NFA = os.path.join(ROOT, "data", "nfa", "NFA_world_landtype_biocapacity_footprint_1961_2023.csv")
OUT = os.path.join(ROOT, "scans")

def world_series(path, value_col, name):
    df = pd.read_csv(path)
    df = df[df["Entity"] == "World"].copy()
    df = df.rename(columns={value_col: name})
    return df[["Year", name]].sort_values("Year").reset_index(drop=True)

area = world_series(os.path.join(EMP, "cropland_area_owid.csv"),
                    "Cropland - Area (hectares)", "A_f_ha")
yld = world_series(os.path.join(EMP, "cereal_yield_owid.csv"),
                   "Cereals - Yield (tonnes per hectare)", "yield_t_ha")

# measured NFA world cropland biocapacity (gha), year-indexed
nfa = pd.read_csv(NFA)
nfa = nfa[nfa["Record"] == "BiocapTotGHA"].set_index("year")
crop_biocap = nfa["Cropland"]          # gha, world

BASE = 1961
def interp(df, col, year): return np.interp(year, df["Year"].values, df[col].values)

A_f0 = interp(area, "A_f_ha", BASE)
b_f0_phys = interp(yld, "yield_t_ha", BASE)
C0 = crop_biocap.loc[BASE]
b_f_gha0 = C0 / A_f0            # absolute, measured, gha*ha^-1*yr^-1

print("=== base year %d (measured absolute anchor) ===" % BASE)
print("  Cropland biocapacity(1961) = %.4e gha  [measured NFA]" % C0)
print("  A_f (cropland area)        = %.4e ha" % A_f0)
print("  b_f(1961) ABSOLUTE         = %.4f gha*ha^-1*yr^-1" % b_f_gha0)
print("  b_f(1961) physical         = %.3f t/ha" % b_f0_phys)

# index series over 1961-2022 (NFA crop biocapacity available; area/yield to 2022)
years = np.arange(1961, 2023)
rows = []
for yr in years:
    if yr not in crop_biocap.index: continue
    a = interp(area, "A_f_ha", yr)
    b = interp(yld, "yield_t_ha", yr)
    C = crop_biocap.loc[yr]
    rows.append({
        "Year": yr,
        "A_f_ha": a,
        "A_f_index": a / A_f0,
        "b_f_t_ha": b,
        "b_f_index_cereal": b / b_f0_phys,
        "crop_biocap_gha": C,
        "b_f_gha_per_ha_per_yr": C / a,
        "b_f_index_nfa": (C / a) / (C0 / A_f0),
    })
ser = pd.DataFrame(rows)

i0, i1 = 0, len(ser) - 1
dlnA = float(np.log(ser["A_f_index"].iloc[i1] / ser["A_f_index"].iloc[i0]))
dlnb_cereal = float(np.log(ser["b_f_index_cereal"].iloc[i1] / ser["b_f_index_cereal"].iloc[i0]))
dlnb_nfa = float(np.log(ser["b_f_index_nfa"].iloc[i1] / ser["b_f_index_nfa"].iloc[i0]))
dlnBf = float(np.log(ser["crop_biocap_gha"].iloc[i1] / ser["crop_biocap_gha"].iloc[i0]))

print("\n=== decomposition, %d-%d ===" % (years[0], years[-1]))
print("  A_f (area):        %.2fx   d ln A_f = %+.4f" % (ser["A_f_index"].iloc[i1], dlnA))
print("  b_f (cereal):      %.2fx   d ln b_f = %+.4f   [physical sentinel]" % (ser["b_f_index_cereal"].iloc[i1], dlnb_cereal))
print("  b_f (NFA, gha/ha): %.2fx   d ln b_f = %+.4f   [measured, model units]" % (ser["b_f_index_nfa"].iloc[i1], dlnb_nfa))
print("  B_f (cropland bio):%.2fx   d ln B_f = %+.4f   [= b_f + A_f]" % (ser["crop_biocap_gha"].iloc[i1]/crop_biocap.loc[BASE], dlnBf))

print("\n>>> composition-premium sign (yield >> area) for BOTH numerator measures:")
print("    d ln b_f %+.4f (cereal) / %+.4f (NFA)  >>  d ln A_f %+.4f" % (dlnb_cereal, dlnb_nfa, dlnA))

# aggregate attribution: how much of total world biocapacity growth is the cropland book?
# (two NFA vintages in the repo give slightly different totals; report the range)
C0t = crop_biocap.loc[BASE]; C1t = crop_biocap.loc[2022]
B0 = nfa.loc[BASE, "Total"]; B1 = nfa.loc[2022, "Total"]          # land-type file total
g = pd.read_csv(os.path.join(ROOT, "data", "nfa", "GFN_world_biocapacity_footprint_population_1961_2022.csv")).set_index("Year")
Gb0 = g.loc[BASE, "Biocapacity_gha"]; Gb1 = g.loc[2022, "Biocapacity_gha"]  # aggregate series total
print("\n=== aggregate composition attribution (measured NFA, two vintages) ===")
for label, (A0, A1) in {"land-type file total": (B0, B1), "aggregate series total": (Gb0, Gb1)}.items():
    dlnB_agg = np.log(A1/A0)
    dlnncn = np.log((A1-C1t)/(A0-C0t))
    shar = 100*(C1t-C0t)/(A1-A0)
    print("  %-26s total %.1f%% (d ln B %+.4f);  cropland book d ln %+.4f (%.2fx);  non-crop d ln %+.4f;  cropland = %.0f%% of net growth"
          % (label, 100*(A1/A0-1), dlnB_agg, np.log(C1t/C0t), C1t/C0t, dlnncn, shar))
print("  => the cropland (fast) book accounts for essentially all of the net aggregate")
print("     biocapacity growth; the non-cropland book is flat in both vintages.")

print("\n  b_f(2022) absolute (NFA, measured): %.4f gha*ha^-1*yr^-1" % ser["b_f_gha_per_ha_per_yr"].iloc[-1])

ser.to_csv(os.path.join(OUT, "bf_af_calibration_series.csv"), index=False)
print("\nwrote:", os.path.join(OUT, "bf_af_calibration_series.csv"))

# --- figure ---
fig, axes = plt.subplots(1, 4, figsize=(17, 4.2), dpi=400)
axes[0].plot(ser["Year"], ser["A_f_index"], color="#1f77b4", lw=2)
axes[0].set_title("Fast provisioning area $A_f$ (index, 1961=1)", fontsize=9, fontweight="bold")
axes[0].set_ylabel("index (1961=1)")
axes[1].plot(ser["Year"], ser["b_f_index_cereal"], color="#d62728", lw=2)
axes[1].set_title("$b_f$ — cereal yield (index, 1961=1)", fontsize=9, fontweight="bold")
axes[2].plot(ser["Year"], ser["b_f_index_nfa"], color="#2ca02c", lw=2)
axes[2].set_title("$b_f$ — NFA cropland bio. (index, 1961=1, gha/ha)", fontsize=9, fontweight="bold")
axes[3].bar(["area $A_f$", "yield $b_f$", "yield $b_f$\\n(NFA)"],
            [dlnA, dlnb_cereal, dlnb_nfa],
            color=["#1f77b4", "#d62728", "#2ca02c"], width=0.6)
axes[3].axhline(0, color="k", lw=0.8)
axes[3].set_title("$d\\ln$ contribution (yield vs area)", fontsize=9, fontweight="bold")
axes[3].set_ylabel("log contribution")
for ax in axes: ax.grid(alpha=0.25)
fig.suptitle("Provisioning-book yield $b_f$ and area $A_f$ — FAOSTAT/OWID + NFA, world 1961–2022",
             fontsize=11, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.92])
fig.savefig(os.path.join(OUT, "S1d_bf_af_calibration.png"), dpi=400)
print("wrote:", os.path.join(OUT, "S1d_bf_af_calibration.png"))

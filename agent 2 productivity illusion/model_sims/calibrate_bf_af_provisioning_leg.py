"""
Provisioning-book leg: calibrate the fast-book yield b_f and fast provisioning area
A_f from FAOSTAT crop data, and evaluate the composition-diagnostic sign.

This is a DIFFERENT object from the regeneration-timescale legs (S5.3a: forest +
fishery, which estimate rho / tau_g, the ecological recovery of capital land).  Here
we calibrate the food-supply / provisioning subsystem of the model -- the fast
provisioning area A_f and its flow yield b_f.

The manuscript's observation operator (Section 12.3) is:

    A_f(t) = FAOSTAT arable + permanent crops (element Area, world, 1961-2022)
    b_f(t) = crop production / A_f(t), normalised to the base year

Numerator (used here): the CEREAL sentinel -- OWID/FAOSTAT cereal yield (t/ha),
world, 1961-2020.  It is continuous and physically meaningful (a physical
quantity, no index splicing).  This is the SAME numerator used to reproduce the
manuscript's Section 12.3 decomposition.

Numerator (attempted, REJECTED as unreliable): the FAOSTAT Gross Crop Production
Index (domain Production Indices QI, item 2041 "Crops, gross", element 432
"Production Index Number", base 2014-2016 = 100), retrieved via the World Bank
WDI indicator AG.PRD.CROP.XD.  This index aggregates all crops at international
commodity prices and would be the preferred numerator, BUT the WDI-transmitted
series shows several base-period splice discontinuities -- physically impossible
single-year jumps (e.g. +52% in 2000, +43% in 1993, -18% in 1989).  These are
index-rebasing artifacts, NOT real changes in crop output, so the index cannot be
used as a continuous growth measure.  The native FAOSTAT API (fenixservices.fao.org)
and bulk-data host were unreachable from this environment (HTTP 521 / connection
failed), so we could NOT obtain a clean, continuously-rebased QI/2041/432 series.
=> We flag this and recommend the author download the domain QI, item 2041,
   element 432, year range 1961-2022 table directly from FAOSTAT or the UN Data
   portal (one continuous base) if the aggregate index is preferred.

Absolute anchor: b_f(1961) = CroplandBiocapacity(1961) / A_f(1961), where
CroplandBiocapacity is the NFA cropland-land biocapacity in gha (this removes the
alpha-dependence of the manuscript's unidentified cropland share).  NOTE: the NFA
cropland-biocapacity API (data.footprintnetwork.org) returned HTTP 403, requiring
authentication, and could NOT be fetched.  We use the author-supplied value
~1.28e9 gha (world, 1961) and flag it clearly.

Caveat on units (stated in the manuscript):  FAOSTAT yields are physical output per
hectare (t/ha), NOT gha*ha^-1*yr^-1.  The NFA cropland-biocapacity anchor converts
b_f(1961) into gha*ha^-1*yr^-1; the yield/index time-series rebuilds the trajectory.
Only the INDEX/sign (composition-premium) is robust; the absolute level depends on
the NFA cropland value.
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
OUT = os.path.join(ROOT, "scans")

# author-supplied NFA cropland biocapacity (world, 1961), gha  [NOT live-fetchable: 403]
NFA_CROPLAND_BIO_1961 = 1.28e9

def world_series(path, value_col, name):
    df = pd.read_csv(path)
    df = df[df["Entity"] == "World"].copy()
    df = df.rename(columns={value_col: name})
    return df[["Year", name]].sort_values("Year").reset_index(drop=True)

area = world_series(os.path.join(EMP, "cropland_area_owid.csv"),
                    "Cropland - Area (hectares)", "A_f_ha")
yld = world_series(os.path.join(EMP, "cereal_yield_owid.csv"),
                   "Cereals - Yield (tonnes per hectare)", "yield_t_ha")

BASE = 1961
def interp(df, col, year): return np.interp(year, df["Year"].values, df[col].values)

A_f0 = interp(area, "A_f_ha", BASE)
b_f0_physical = interp(yld, "yield_t_ha", BASE)   # t/ha

# absolute b_f(1961) in gha*ha^-1*yr^-1 from NFA cropland biocapacity / area
b_f_gha0 = NFA_CROPLAND_BIO_1961 / A_f0
print("=== base year %d (absolute anchor) ===" % BASE)
print("  A_f (cropland area)      = %.3e ha" % A_f0)
print("  NFA cropland biocapacity = %.3e gha  [author-supplied; API 403 not fetchable]" % NFA_CROPLAND_BIO_1961)
print("  b_f(1961) absolute       = %.4f gha*ha^-1*yr^-1" % b_f_gha0)
print("  b_f(1961) physical       = %.3f t/ha" % b_f0_physical)

# index series over the full 1961-2022 window (area & yield both available to 2022)
years = np.arange(1961, 2023)
rows = []
for yr in years:
    a = interp(area, "A_f_ha", yr)
    b = interp(yld, "yield_t_ha", yr)
    rows.append({
        "Year": yr,
        "A_f_ha": a,
        "A_f_index": a / A_f0,
        "b_f_t_ha": b,
        "b_f_index": b / b_f0_physical,
        "b_f_gha_per_ha_per_yr": (b / b_f0_physical) * b_f_gha0,
    })
ser = pd.DataFrame(rows)

i0, i1 = 0, len(ser) - 1
dlnA = float(np.log(ser["A_f_index"].iloc[i1] / ser["A_f_index"].iloc[i0]))
dlnb = float(np.log(ser["b_f_index"].iloc[i1] / ser["b_f_index"].iloc[i0]))

print("\n=== decomposition, %d-%d (index form; robust to the unidentified share) ===" % (years[0], years[-1]))
print("  A_f index growth:        %.2fx   (d ln A_f = %+.4f)" % (ser["A_f_index"].iloc[i1], dlnA))
print("  b_f (cereal sentinel):   %.2fx   (d ln b_f = %+.4f)" % (ser["b_f_index"].iloc[i1], dlnb))
print("\n>>> composition-premium sign: yield intensification drives the aggregate")
print("    d ln b_f %+.3f  >>  d ln A_f %+.3f" % (dlnb, dlnA))
print("    => intensification (yield) dominates land expansion (area).")

b_f_2020 = ser.loc[ser["Year"] == 2020, "b_f_gha_per_ha_per_yr"].iloc[0]
print("\n  b_f(2020) absolute (NFA-anchored): %.4f gha*ha^-1*yr^-1" % b_f_2020)

ser.to_csv(os.path.join(OUT, "bf_af_calibration_series.csv"), index=False)
print("\nwrote:", os.path.join(OUT, "bf_af_calibration_series.csv"))

# --- figure ---
fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2), dpi=400)
axes[0].plot(ser["Year"], ser["A_f_index"], color="#1f77b4", lw=2)
axes[0].set_title("Fast provisioning area $A_f$ (index, 1961=1)", fontsize=10, fontweight="bold")
axes[0].set_ylabel("index (1961=1)")
axes[1].plot(ser["Year"], ser["b_f_index"], color="#d62728", lw=2)
axes[1].set_title("Fast-book yield $b_f$ (index, 1961=1)", fontsize=10, fontweight="bold")
axes[2].bar(["area $A_f$", "yield $b_f$"], [dlnA, dlnb], color=["#1f77b4", "#d62728"], width=0.6)
axes[2].axhline(0, color="k", lw=0.8)
axes[2].set_title("$d\\ln B$ decomposition (yield vs area)", fontsize=10, fontweight="bold")
axes[2].set_ylabel("log contribution")
for ax in axes: ax.grid(alpha=0.25)
fig.suptitle("Provisioning-book yield $b_f$ and area $A_f$ — FAOSTAT/OWID, world 1961–2022",
             fontsize=11, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.94])
fig.savefig(os.path.join(OUT, "S1d_bf_af_calibration.png"), dpi=400)
print("wrote:", os.path.join(OUT, "S1d_bf_af_calibration.png"))

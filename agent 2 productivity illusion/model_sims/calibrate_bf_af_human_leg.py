"""
Human-relevant leg: calibrate the fast-book yield b_f and fast provisioning land
A_f from FAOSTAT/OWID crop data, and evaluate the composition-diagnostic sign.

This is a DIFFERENT object from the regeneration-timescale legs (S5.3a: forest +
fishery, which estimate rho / tau_g, the ecological recovery of capital land).  Here
we calibrate the FOOD-SUPPLY side of the model -- the fast provisioning land A_f and
its flow yield b_f -- which is exactly where humans sit.

The manuscript's observation operator (Section 12.3) is:

    A_f(t) = FAOSTAT arable + permanent crops (element Area, world, 1961-2022)
    b_f(t) = FAOSTAT crop production / A_f(t), normalised to the base year
             b_f(t) = b_f(t0) * b_f(t)/b_f(t0)

Crucial caveat (stated in the manuscript):  FAOSTAT yields are physical output per
hectare (t/ha), NOT gha*ha^-1*yr^-1.  So an ABSOLUTE b_f in the model's units needs
the base-year anchor -- the unidentified cropland share alpha of total biocapacity,
b_f(1961) = alpha * B(1961) / A_f(1961) (the manuscript uses alpha=0.19).  Only the
INDEX (growth/sign) and the composition-premium SIGN are robust to alpha; the
absolute level is not.  We report both, and state the caveat.

Data (World aggregate, 1961-2022/24), fetched from Our World in Data / FAOSTAT:
  - cropland area (ha):        OWID 'cropland-area' (FAOSTAT AGRA)
  - cereal yield (t/ha):       OWID 'cereal-yield' (FAOSTAT)
  - cereal production (t):     OWID 'cereal-production' (FAOSTAT)
  - World biocapacity (gha):   NFA 1961-2022 (for the alpha anchor)

Notes on what is NOT used / not available (flagged so the author can fetch):
  - A FULL aggregate crop-production index (all crops, not just the cereal
    sentinel).  OWID 'crop-production'/'food-production index' returned 404; only
    the cereal production series is available directly.  An aggregate FAO
    FAOSTAT "production index" would be a better numerator (see caveat).
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
NFA = os.path.join(ROOT, "data", "nfa", "GFN_world_biocapacity_footprint_population_1961_2022.csv")
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
prod = world_series(os.path.join(EMP, "cereal_production_owid.csv"),
                    "Cereals - Production (tonnes)", "prod_t")

nfa = pd.read_csv(NFA)
nfa.columns = [c.strip() for c in nfa.columns]
nfa = nfa.rename(columns={"Biocapacity_gha": "B_gha", "Population": "Population"})

# --- base year (1961) matching the manuscript's alpha anchor ---
def interp(df, col, year):
    return np.interp(year, df["Year"].values, df[col].values)

BASE = 1961
A_f0 = interp(area, "A_f_ha", BASE)              # ha
b_f0_sentinel = interp(yld, "yield_t_ha", BASE)  # t/ha (physical, NOT gha/ha)
B0 = interp(nfa, "B_gha", BASE)                  # gha (world biocapacity)
alpha = 0.19                                     # manuscript's base-year cropland share

# absolute b_f in gha*ha^-1*yr^-1 at base year using the alpha anchor
b_f_gha0 = alpha * B0 / A_f0
print("=== base year %d ===" % BASE)
print("A_f (cropland area)      = %.3e ha" % A_f0)
print("B (world biocapacity)    = %.3e gha" % B0)
print("b_f sentinel yield       = %.3f t/ha (physical)" % b_f0_sentinel)
print("b_f (gha/ha/yr, alpha=%s)= %.3e gha*ha^-1*yr^-1" % (alpha, b_f_gha0))

# --- build normalised index series over 1961-2022 ---
yrs = np.arange(1961, 2023)
rows = []
for yr in yrs:
    a = interp(area, "A_f_ha", yr)
    b = interp(yld, "yield_t_ha", yr)
    B = interp(nfa, "B_gha", yr)
    rows.append({
        "Year": yr,
        "A_f_ha": a,
        "A_f_index": a / A_f0,
        "b_f_t_ha": b,
        "b_f_t_ha_index": b / b_f0_sentinel,
        "b_f_gha_per_ha_per_yr": alpha * B / (a / 1.0) if a > 0 else np.nan,
        "B_gha": B,
    })
ser = pd.DataFrame(rows)
ser["b_f_gha_index"] = ser["b_f_t_ha_index"]   # index = 1 in 1961

# --- composition-diagnostic sign / decomposition (index form, robust to alpha) ---
# delta ln B = delta ln b_f + delta ln A_f  (yield channel + area channel),
# exactly the decomposition used in the manuscript (Section 12.3 / SI S5.1).
i0, i1 = 0, len(ser) - 1
dlnB = float(np.log(ser["B_gha"].iloc[i1] / ser["B_gha"].iloc[i0]))
dlnA = float(np.log(ser["A_f_index"].iloc[i1] / ser["A_f_index"].iloc[i0]))
dlnb = float(np.log(ser["b_f_t_ha_index"].iloc[i1] / ser["b_f_t_ha_index"].iloc[i0]))

print("\n=== decomposition over %d-%d (index form; robust to alpha) ===" % (yrs[0], yrs[-1]))
print("d ln B      = %+.4f" % dlnB)
print("d ln A_f    = %+.4f  (area channel, %+.1f%%)" % (dlnA, 100 * dlnA))
print("d ln b_f    = %+.4f  (yield channel, %+.1f%%)" % (dlnb, 100 * dlnb))
print("sum (Af+b_f)= %+.4f   vs d ln B = %+.4f" % (dlnA + dlnb, dlnB))
print("check b_f*growth: %.2fx, A_f growth: %.2fx" % (ser['b_f_t_ha_index'].iloc[i1], ser['A_f_index'].iloc[i1]))

print("\n>>> composition-premium sign (b_f yield >> capital per-ha value):")
print("    yield b_f rose %.2fx while cropland area rose only %.2fx =>" %
      (ser['b_f_t_ha_index'].iloc[i1], ser['A_f_index'].iloc[i1]))
print("    intensification (yield) dominates land expansion (area): d ln b_f (%+.3f) >> d ln A_f (%+.3f)"
      % (dlnb, dlnA))

# --- alpha robustness (the unidentified cropland share) ---
alphas = np.linspace(0.10, 0.34, 25)
def B_from_alpha(al):
    # b_f(1961)=al*B(1961)/A_f(1961); X_t = b_f(t)*A_f(t) = al*B(1961)*[b_hat(t)]
    b0 = al * B0 / A_f0
    X = ser["b_f_t_ha_index"].values  # b_f(t)/b_f(1961)
    Xt = al * B0 * X  # gha
    return Xt
# sign of d ln X and d ln C=B-X across alpha
sgn = {"X_up": True, "C_down": True}
for al in alphas:
    X = B_from_alpha(al)
    X1961, X2022 = X[0], X[-1]
    C1961, C2022 = B0 - X1961, ser["B_gha"].iloc[-1] - X2022
    if not (np.sign(X2022 - X1961) > 0): sgn["X_up"] = False
#   if C2022 > 0 and C2022 < C1961 -> C declines (composition)
print("\n=== alpha-robustness (share caveat, quantified) ===")
print("fast-book X rises for every alpha in [0.10,0.34]:", sgn["X_up"])
print("(the absolute split and C>0 are alpha-dependent; the SIGN of the yield channel is not)")

ser.to_csv(os.path.join(OUT, "bf_af_calibration_series.csv"), index=False)
print("\nwrote:", os.path.join(OUT, "bf_af_calibration_series.csv"))

# --- figure ---
fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2), dpi=400)
axes[0].plot(ser["Year"], ser["A_f_index"], color="#1f77b4", lw=2)
axes[0].set_title("Fast provisioning land $A_f$ (index, 1961=1)", fontsize=10, fontweight="bold")
axes[0].set_ylabel("index (1961=1)")
axes[1].plot(ser["Year"], ser["b_f_t_ha_index"], color="#d62728", lw=2)
axes[1].set_title("Fast-book yield $b_f$ (index, 1961=1)", fontsize=10, fontweight="bold")
axes[2].bar([1961, 2022], [dlnA, dlnb], color=["#1f77b4", "#d62728"], width=14)
axes[2].axhline(0, color="k", lw=0.8)
axes[2].set_title("$d\\ln B$ decomposition (yield vs area)", fontsize=10, fontweight="bold")
axes[2].set_xticks([1961, 2022]); axes[2].set_xticklabels(["area $A_f$", "yield $b_f$"])
axes[2].set_ylabel("log contribution")
for ax in axes: ax.grid(alpha=0.25)
fig.suptitle("Human-relevant leg: fast-book yield $b_f$ and land $A_f$ (FAOSTAT/OWID, world 1961-2022)\n"
             "yield intensification dominates land expansion => composition premium", fontsize=11, fontweight="bold")
fig.tight_layout(rect=[0, 0, 1, 0.90])
fig.savefig(os.path.join(OUT, "S1d_bf_af_calibration.png"), dpi=400)
print("wrote:", os.path.join(OUT, "S1d_bf_af_calibration.png"))

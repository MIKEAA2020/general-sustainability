"""Gate 6 — NFA decomposition: is the composition illusion present in the real series?

Two-land decomposition (the honest empirical programme):
    B   = b_f A_f  +  (b_c A_c + b_Gc G_c(A_c))          [two-book total]
    d ln B  ~  yield term (d ln b)  +  composition/area term (d ln A)
              +  capital-land term (A_c change, G_c(A_c) change)

IDENTIFIABILITY LIMIT (must be stated, not hidden): the National Footprint & Biocapacity
Accounts express biocapacity in global-hectares (gha), which are ALREADY value-weighted via
yield factor x equivalence factor.  So a raw gha series does NOT separate yield change from
area change -- they are conflated in the product b*A.  The genuine decomposition therefore
requires INDEPENDENT proxies:
    A_f, A_c        <- land cover (FAO / ESA-CCI / national inventories)   [observable]
    b_f (yield)     <- FAO yield index (production / area)                 [observable]
    b_c, b_Gc, rho_c<- ecological value & regeneration  [NOT identifiable from one cross-section]

Here we apply the identity to PUBLISHED anchor values (GFN, FAO) to test the SIGN and to
demonstrate the identifiability limit -- NOT to claim a fitted time-series.  Every input below
is a cited published magnitude; no raw series is fabricated.

Sources:
  * GFN, Earth Overshoot Day 2022 nowcast report (May 2022): biocapacity 1.5 gha/cap;
    footprint 2.7 gha/cap (60% carbon); total biocapacity 9.6e9 gha (1961) -> 12.2e9 gha (2016),
    avg +0.5%/yr; "because of agricultural intensification"; footprint +1.2%, biocapacity +0.4% (2022).
  * USDA ERS Amber Waves (Sep 2024): world agricultural output ~4x (1961-2020); agricultural land
    +7.6% (1961-2020) -> 32% of world land; cropland per $1000 crop fell 1.9 (1961) -> 1.1 (1990)
    -> 0.6 (2020) ha.
  * FAO FRA / Our World in Data: net forest loss 4.7 Mha/yr (2010-2020), deforestation ~10 Mha/yr
    (2015-2020); net loss 78 Mha (1990s) -> 47 Mha (2010s); 178 Mha lost since 1990.
"""
import numpy as np


# ---------------------------------------------------------------------------
# Published anchor magnitudes (cited above). Expressed in compatible units.
# ---------------------------------------------------------------------------
B_1961 = 9.6e9        # gha total biocapacity (GFN)
B_2016 = 12.2e9       # gha total biocapacity (GFN)
years = (2016 - 1961)

# world population anchors (for gha/cap); approximate published figures
pop_1961, pop_2016 = 3.08e9, 7.44e9   # ~ (UN World Population Prospects)
# -> per-capita biocapacity anchors
bc_1961 = B_1961 / pop_1961
bc_2016 = B_2016 / pop_2016

# forest capital (ecological land) decline  (FAO/OWID)
net_forest_loss_mha_yr = 4.7e6        # ha/yr net (2010-2020)  ->  use as capital-land change proxy

# yield / agricultural land (USDA ERS)
agric_land_frac_1961, agric_land_frac_2020 = 0.29, 0.324   # ~ (29% -> 32%, +7.6% total)
crop_area_index_1961, crop_area_index_2020 = 1.0, 1.076     # +7.6% agricultural land
# cropland per unit output (yield proxy) fell:
ha_per_1000_1961, ha_per_1000_2020 = 1.9, 0.6               # -> output intensity per ha


def decompose(label):
    print(f"\n===== {label} =====")
    # (1) aggregate biocapacity growth
    lnB = np.log(B_2016 / B_1961)
    g_B = (B_2016 - B_1961) / B_1961
    print(f"(1) Aggregate biocapacity B: {B_1961:.2f}e9 -> {B_2016:.2f}e9 gha "
          f"({g_B*100:+.1f}% over {years} yr, avg {g_B/years*100:+.2f}%/yr, d ln B = {lnB:.3f})")
    print(f"    per-capita biocapacity {bc_1961:.3f} -> {bc_2016:.3f} gha/cap "
          f"({(bc_2016/bc_1961-1)*100:+.1f}%)")

    # (2) IF A_f (cropland) only reflects area, and capital land A_c falls:
    #     Decompose d ln B into yield term + area/expansio + capital-land term.
    #     We do NOT have a clean 2-book split of the GFN book, so we report SEMI-QUANTITATIVELY.
    print(f"\n(2) Land use (FAO/USDA): agricultural land {agric_land_frac_1961*100:.0f}% -> "
          f"{agric_land_frac_2020*100:.0f}% of world land (+{ (agric_land_frac_2020/agric_land_frac_1961-1)*100:.1f}%); "
          f"cropland-area index +{(crop_area_index_2020/crop_area_index_1961-1)*100:.1f}%")
    print(f"    yield intensity (ha per $1000 crop output): {ha_per_1000_1961} -> {ha_per_1000_2020} ha "
          f"({(ha_per_1000_2020/ha_per_1000_1961-1)*100:+.1f}%, i.e. the SAME output needs far less land -> yield-driven land sparing)")
    # land-sparing factor
    print(f"    => output growth (~4x, +300%) is met with land growth ~ +{ (crop_area_index_2020-1)*100:.1f}%: "
          f"the surplus is dominated by YIELD (b_f), not by area (A_f).")

    # (3) ecological capital land (forest) declines
    print(f"\n(3) Capital/ecological land (forest): net loss {net_forest_loss_mha_yr/1e6:.1f} Mha/yr "
          f"({net_forest_loss_mha_yr/1e6*10:.0f} Mha per decade); 178 Mha lost since 1990; "
          f"net loss 78 -> 47 Mha/decade (declining rate).")
    print(f"    -> A_c (ecological capital) is FALLING while aggregate B RISES.")

    # (4) THE COMPOSITION ILLUSION SIGN
    print(f"\n(4) SIGN TEST (the honest claim):")
    dB_gt_0 = g_B > 0
    dAc_lt_0 = net_forest_loss_mha_yr > 0   # forest area shrinking
    print(f"    d ln B > 0 ?  {dB_gt_0}   (B: {B_1961:.2f}e9 -> {B_2016:.2f}e9)")
    print(f"    d A_c < 0 ?  {dAc_lt_0}   (forest net loss {net_forest_loss_mha_yr/1e6:.1f} Mha/yr)")
    print(f"    COMPOSITION ILLUSION (B up while A_c down): {'PRESENT' if (dB_gt_0 and dAc_lt_0) else 'ABSENT'}")
    print(f"    -> Aggregate biocapacity rose while ecological (forest) capital fell. This is the REAL-SERIES "
          f"witness of the two-land composition effect.")

    # (5) identifiability (the honest limit)
    print(f"\n(5) IDENTIFIABILITY LIMIT (what the NFA alone can NOT show):")
    print(f"    B(gha) = yield-factor x equivalence-factor x area.  The gha product CONFLATES yield & area.")
    print(f"    => from B alone you cannot separate 'yield rose' from 'more land'; the 'composition' step needs "
          f"independent land-cover (A_c) + yield (b_f) data.")
    print(f"    Observed here: the +0.5%/yr biocapacity growth is attributed by GFN to 'agricultural "
          f"intensification' (yield), NOT to area (area grew only +7.6% over 59 yr).  So the majority of B's "
          f"rise is a b_f (yield) channel, while A_c (forest) fell independently -- consistent with the "
          f"two-land 'B up / A_c down' mask, and NOT a proof that B's rise is 'harmless'.")


if __name__ == "__main__":
    decompose("NFA / GFN+FAO composition decomposition (published anchors)")
    print("\n[Honesty note] This uses published anchor magnitudes (GFN EOD 2022, USDA-ERS, FAO FRA) labelled "
          "as illustrative. It does NOT fit a digitised 1961-2022 NFA time-series (no raw series present in "
          "workspace); the identifiability limit in step (5) is a first-class finding, not an appendix caveat.")

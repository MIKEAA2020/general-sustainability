#!/usr/bin/env python3
"""
Consolidation (superset) audit for the two Wave E forecast-ladder manuscripts.

On 2026-08-26 the two version pairs were consolidated into single canonical
files, at the owner's instruction ("the two wave e papers can be made into one,
if one version strictly supersedes (is a superset) of the other"):

  wave_e_cod/manuscript/wave_E_cod_forecast_ladder.md
  wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder.md

The consolidated file is the version-2 rewrite with every substantive fact of
the version-1 working manuscript that the rewrite had dropped restored into it
(the same discipline as the d844e0a restorations).  This script machine-checks
the superset claim at the fact level: every fact string below — drawn from BOTH
predecessor versions, including the facts that only v1 carried and the facts
that only v2 carried — must appear in the consolidated file.  It also checks
the structural invariants: the *2.md files are gone, all referenced figures
exist, and the F1 pinned phrases survive.

Exit 0 => the consolidated manuscripts strictly supersede both predecessors
at the audited fact level.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FAIL = []


def check(name, cond, detail=""):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}{(' :: ' + str(detail)) if detail else ''}")
    if not cond:
        FAIL.append(name)


def norm(s):
    return re.sub(r"\s+", " ", s)


COD = norm((REPO / "wave_e_cod/manuscript/wave_E_cod_forecast_ladder.md").read_text())
EDW = norm((REPO / "wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder.md").read_text())

# ------------------------------------------------------------------ structure
print("[0] structure")
check("cod v2 file removed", not (REPO / "wave_e_cod/manuscript/wave_E_cod_forecast_ladder2.md").exists())
check("edwards v2 file removed", not (REPO / "wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder2.md").exists())
check("cod manuscript references the specification sheet",
      "wave_e_cod/SPECIFICATION.md" in COD)
check("edwards manuscript references the specification sheet",
      "wave_e_edwards/SPECIFICATION.md" in EDW)

for tree, figs in (("wave_e_cod", ["fig1_series", "fig2_windows", "fig3_rmse", "fig4_xtencam"]),
                   ("wave_e_edwards", ["fig1_series", "fig2_windows", "fig3_rmse",
                                       "fig4_fibre", "fig5_pass2"])):
    for f in figs:
        check(f"{tree}: {f}.png present", (REPO / tree / "manuscript" / f"{f}.png").exists())
        check(f"{tree}: {f}.svg present", (REPO / tree / "manuscript" / f"{f}.svg").exists())

# F1 pinned phrases (verify_wave_e.py check [5] reads the same file)
check("F1 phrase 'not extra structure' survives in Edwards manuscript",
      "not extra structure" in EDW)
check("F1 phrase 'do not constitute additional forecast structure' survives in Edwards manuscript",
      "do not constitute additional forecast structure" in EDW)

# ------------------------------------------------------------------ cod facts
print("\n[1] cod: v1-only facts restored into the consolidated file")
cod_v1_only = [
    ("series lock line", "DFO SAR 2016/026 Table A2 (1983–2015)"),
    ("two scored specifications status", "two scored specifications"),
    ("A005/A004 conditional admissibility + blocking lists", "blocking lists V-A005-04"),
    ("A004 blocking list id", "V-A004-03"),
    ("groundwater/phosphorus not used", "are not used here"),
    ("groundwater/phosphorus opening condition", "after the R04 blocking lists close and a basin series exists"),
    ("A014-L4/L5/L6 defect-list respect", "A014-L4, L5, L6"),
    ("food-web spec row (capelin excluded)", "Capelin excluded from the primary pass"),
    ("norm spec row (not the 2023 LRP)", "not the 2023 40% $B_{\\mathrm{MSY}}$ LRP"),
    ("regime coarseness declared limitation", "declared limitation"),
    ("M4 information cost", "the information cost of the one-year delay"),
    ("Figure 2 AR-underprediction caption", "Recovery is under-predicted when an AR residual"),
    ("Allee = A014 Prop 2 conditional form", "Proposition 2 in conditional form"),
    ("2015 Schijns catch matches DFO", "4.436 kt, matching DFO reported landings"),
    ("dS far larger than C", "observed $\\Delta S$ is far larger than $C_t$"),
    ("checkpoint CI 2005", "22--31"),
    ("checkpoint CI 2017", "381--534"),
    ("checkpoint CI 2024", "246--475"),
    ("no splicing of the two columns", "does not warrant splicing the two columns"),
    ("34% of the old LRP", "34% of the old LRP"),
    ("second independent negative certificate", "second independent negative certificate"),
    ("A014-L4 tightens", "tightens A014-L4 rather than relaxing it"),
    ("R03 descriptive clause", "descriptive unless the certificate hypotheses hold (R03)"),
    ("M3-M4 not inner certificates", "not inner certificates here"),
    ("H8 kernel framing", "empty viability kernel (H8)"),
    ("2023 LRP rerun needs new admission row", "requires the xteNCAM series and a new admission row"),
    ("computational protocol disclosure", "a fixed computational protocol rather than a prospective clinical-style registration"),
    ("E5 template disambiguation", "E5 is a linear $(S,K)$ template, not this SSB series"),
    ("A012 delay not RFDE", "not as an RFDE"),
    ("A016 unarchived CSD extract", "A016 community margins are not used (the CSD extract is unarchived)"),
    ("Wave E support rule", "specification matching and independent verification"),
    ("identified-modules conclusion", "modules that are not identified on the training data do not reduce forecast error"),
    ("abstract A014 incompatibility", "incompatible with the observed path (A014)"),
    ("abstract three-part negative certificate", "(iii) extra modules that are not identified"),
]
for name, s in cod_v1_only:
    check(f"cod v1 fact: {name}", norm(s) in COD, s[:60])

print("\n[2] cod: v2 rewrite facts retained in the consolidated file")
cod_v2 = [
    ("naive baselines wording", "Nested surplus-production models and two naive baselines"),
    ("F/M not drivers", "not used as exogenous drivers"),
    ("claim-type taxonomy", "D, data; E, empirical construct; M, model; N, normative threshold"),
    ("four typed fields", "differ in four typed fields"),
    ("R04 forbids transfer", "R04 forbids judgment transfer. Both fail."),
    ("fitting bounds", "$r\\in(0.001,2]$, $K$ above the training maximum"),
    ("survey-start definition", "training-window median of $\\mathrm{SSB}/I$"),
    ("no interpolation across 1991", "Pre-1991 acoustic values are not carried across 1991"),
    ("fixed windows", "collapse, train 1983--1990, test 1991--1995; recovery, train 1995--2007, test 2008--2015"),
    ("xte collapse window", "train 1954--1989, test 1990--1995"),
    ("2024 catch persisted", "2024 persisted from 2023"),
    ("STATLANT clause", "STATLANT matches Schijns on 1983--1993"),
    ("1956 discrepancy", "236,210 t versus 263,210 t"),
    ("LRP interval at first mention", "95% interval 180--423 kt; 40% of $B_{\\mathrm{MSY}}$"),
    ("2021 checkpoint", "2021 $\\approx 400$ kt (NCAM and xteNCAM said to agree)"),
    ("sample-size clause", "rolling $n=25$ at $h=1$ and $n=21$ at $h=5$"),
    ("disclaimer sentence", "does not conclude that the stock is unsustainable"),
    ("reproducibility statement", "every archived result file was regenerated byte for byte"),
    ("reproduce commands", "run_capelin_regime.py && python3 src/run_capelin_index.py"),
    ("DFO 2024/050 reference", "2024/050"),
]
for name, s in cod_v2:
    check(f"cod v2 fact: {name}", norm(s) in COD, s[:60])

print("\n[3] cod: headline numbers (both versions) present")
cod_numbers = ["884.6", "98", "115--206", "160", "265", "289--488", "694--819", "90",
               "88", "318", "120", "152", "166", "1059", "127", "930", "1031", "449",
               "8.02", "8.70", "0.59", "3.39", "0.76", "424", "375", "2.35", "507",
               "694", "638", "2.73", "819", "751", "2.85", "220", "214", "0.61",
               "0.49 versus persist 0.52", "331 versus persist 265", "821", "817", "1898",
               "126", "299", "273", "25.18", "1.24", "3704", "174", "107", "331.3",
               "262 versus 265", "154", "334", "894", "172--269", "41 kt", "11 kt", "0.4--1.3"]
for n in cod_numbers:
    check(f"cod number {n}", norm(n) in COD)

# ------------------------------------------------------------- edwards facts
print("\n[4] edwards: v1-only facts restored into the consolidated file")
edw_v1_only = [
    ("series lock line", "TWDB 6837203 / EAA AY-68-37-203, 1934–2023"),
    ("status line (not retained)", "causal stock-flow is not retained, causal recharge forecasts are not retained"),
    ("oracle is a diagnostic certificate", "diagnostic certificate excluded from retention"),
    ("R04 prefers groundwater", "R04 prefers groundwater unless the readiness matrix fails"),
    ("phosphorus not opened", "Phosphorus is not opened."),
    ("ENSO/precipitation not substitutes", "ENSO and last year's precipitation are not substitutes"),
    ("F1 phrase M2m class", "A numerical advantage for M2m is not extra structure"),
    ("F1 phrase pass-2 structure clause", "do not constitute additional forecast structure"),
    ("M2m demotion structure sentence", "does not constitute additional structure"),
    ("M1 retention margin", "retained (margin 0.39 ft)"),
    ("cod LRP parallel", "just as the 2016 cod LRP was the wrong leading indicator for 1983--90"),
    ("A005 parameterization", "$q_{\\mathrm{rel}}$ is removed, leakage is not applicable, and no $B_k$ or $\\chi$ term is fitted"),
    ("declared approximation defect", "declared approximation defect"),
    ("E5 not this specification", "E5 is not this specification"),
    ("Wave E support rule", "specification matching and independent verification"),
    ("identified-modules conclusion", "modules that are not identified on the training data, or whose drivers arrive too late to be causal at the annual origin, do not reduce forecast error"),
    ("fibre caption role", "The fibre is a measured service, not an independent information source"),
    ("next-article discipline (PDO/AMO)", "PDO, AMO"),
    ("mid-year nowcast protocol", "a mid-year nowcast would require a new evaluation protocol"),
]
for name, s in edw_v1_only:
    check(f"edw v1 fact: {name}", norm(s) in EDW, s[:60])

print("\n[5] edwards: v2 rewrite facts retained in the consolidated file")
edw_v2 = [
    ("claim-type taxonomy", "D, data; E, empirical construct; M, model; N, normative threshold"),
    ("not-z list", "not a GRACE or G3P storage reconstruction, a MODFLOW or GWSIM inversion"),
    ("two thresholds", "Stage I at 660 ft is a 2007 institutional rule"),
    ("coverage rule", "Years with fewer than 240 observations are dropped"),
    ("1935/1939 coverage", "1935 ($n=258$) and 1939 ($n=242$)"),
    ("Beverly Lodges", "Beverly Lodges"),
    ("provisional R", "provisional TWDB status `R`"),
    ("recharge definition", "Puente (1978) stream-loss method"),
    ("climate predictors", "September--November Niño 3.4 (HadISST, anomaly relative to 1991--2020)"),
    ("clip range", "$[610,710]$ ft"),
    ("protocol-before-scores", "Windows and scores were specified before the corresponding RMSE tables were computed"),
    ("computational protocol disclosure", "a fixed computational protocol rather than a prospective clinical-style registration"),
    ("panel rebuild notes", "leaves the fixed twenty-column panel in place"),
    ("nino34 source file", "nino34.long.data"),
    ("nclimdiv file", "climdiv-pcpndv-v1.0.0-20260806"),
    ("disclaimer sentence", "does not conclude that the aquifer is unsustainable"),
]
for name, s in edw_v2:
    check(f"edw v2 fact: {name}", norm(s) in EDW, s[:60])

print("\n[6] edwards: headline numbers (both versions) present")
edw_numbers = ["13.23", "12.84", "14.70", "7.55", "0.39", "21.11", "16.17", "16.80",
               "12.28", "17.44", "33.49", "14.46", "14.30", "10.87", "5.79",
               "623.15", "691.96", "635.68", "612.51", "703.31", "31 of 90",
               "23.75", "30.94", "18.11", "27.44", "19.69", "43.62", "56.24", "55.32",
               "37.74", "12.26", "30.13", "20.02", "16.67", "23.47", "7.18", "27.41",
               "15.62", "23.37", "14.79", "8.70",
               "0.64", "0.66", "0.17", "0.74", "0.78", "(0.017,-0.026)",
               "13.09", "12.16", "13.31", "8.03", "0.31", "0.25", "0.19",
               "702", "561", "528", "545", "538", "556", "354", "25.38", "24.42", "26.88",
               "12.82", "12.80", "12.71", "13.25", "10.56", "16.91",
               "0.02, 0.04, and 0.13 ft", "43.7", "1142.6", "1143", "48.8", "33.7", "-0.92",
               "0.986", "-2876", "4.77", "71.9 cfs", "69.0", "68.7", "74.8", "45.3",
               "32 cfs", "321 kaf", "618", "660"]
for n in edw_numbers:
    check(f"edw number {n}", norm(n) in EDW)

# ------------------------------------------------------------------ verdict
print("\n" + "=" * 72)
if FAIL:
    print(f"{len(FAIL)} check(s) did not reproduce: {FAIL}")
    sys.exit(1)
print("Consolidation superset audit PASSED: each Wave E manuscript now strictly "
      "supersedes both predecessor versions at the audited fact level.")
sys.exit(0)

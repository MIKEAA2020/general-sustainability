#!/usr/bin/env python3
"""V11 (humanized rewrites) merge — v24_restructured -> v25_restructured.

Base: the Grok humanized rewrite of v24 (frozen source
v25_source_grok_rewrite.md; verified: every numeric token exists in v24, zero
fabrications, all 20 content headers present). Patches (adjudicated in the
merged plan, venue V11):

  1. Front matter (author + ORCID) restored from v24.
  2. Abstract: Gemini's forward-reference clause (consistent with the O9
     co-primary check, Section 6.5).
  3. Section 2.3: Gemini's pedagogical derivation — constant training-mean
     fluxes fold into a single intercept (no numbers added).
  4. References restored from v24 with the M4 method count corrected
     (54 methods -> 61 forecasting methods; NEW-5, verified against the
     published IJF 36(1) title).

Gemini's unarchived numbers (M1 CI [-0.954, +0.180], oracle 10.865, 612.5 ft
historical low), its fabricated companion titles/DOI labels, its swapped
Carvalho/Kell references, and its M5 title are rejected (NEW-6..9).
"""
import hashlib
import sys

SRC = "framework/v25_source_grok_rewrite.md"
DST = "framework/paperF1_retention_framework_v25_restructured.md"

t = open(SRC).read()
assert hashlib.sha256(t.encode()).hexdigest().startswith("19510826bf68f834"), "source checksum changed"
applied = []

def rule(no, old, new):
    n = t.count(old)
    if n != 1:
        print(f"FAIL {no}: anchor occurs {n} times")
        sys.exit(1)
    globals()['t'] = t.replace(old, new, 1)
    applied.append(no)
    print(f"ok {no}")

title = "# When a model is not retained, what must be reported? A retention rule, an information-set audit, and operating characteristics — a minimum reporting standard worked on three scored objects in two domains"
rule("V11-01", title,
     title + "\n\n**Amin Abaee** \nIndependent Researcher \nORCID: 0000-0002-0019-1842")

rule("V11-02",
 "The criterion scores one-step accuracy and does not encode the decision-relevant requirement that a module beat persistence at the multi-year horizon, which the rule does.",
 "The criterion scores one-step accuracy and does not encode the decision-relevant requirement that a module beat persistence at the multi-year horizon, which the rule does; applied alone, it would retain the structurally redundant module the standard withholds.")

rule("V11-03",
 "Groundwater M2m, the training-mean balance (climatological-flux map), beats persistence at both horizons yet collapses to AR(1) when fluxes are held constant: it wins on score while adding nothing beyond the simpler member.",
 "Groundwater M2m, the training-mean balance (climatological-flux map), beats persistence at both horizons yet collapses to AR(1) when fluxes are held constant — the constant training-mean recharge and pumpage fold into a single intercept, leaving an affine autoregression — so it wins on score while adding nothing beyond the simpler member.")

refs = """## References

Abaee, A., 2026a. Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. Zenodo. https://doi.org/10.5281/zenodo.22552680.

Abaee, A., 2026b. Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL. Zenodo. https://doi.org/10.5281/zenodo.22553609.

Carvalho, F., et al., 2021. A cookbook for using model diagnostics in integrated stock assessments. Fisheries Research 240, 105959.

Chambers, C.D., 2013. Registered Reports: A new publishing initiative at Cortex. Cortex 49, 609–610.

DFO, 2016. Stock assessment of Northern cod (NAFO Divs. 2J3KL). DFO Can. Sci. Advis. Sec. Sci. Advis. Rep. 2016/026.

Hyndman, R.J., Koehler, A.B., 2006. Another look at measures of forecast accuracy. International Journal of Forecasting 22, 679–688.

Kell, L.T., et al., 2016. Evaluation of the prediction skill of stock assessment using hindcasting. Fisheries Research 183, 119–127.

Kell, L.T., et al., 2021. Validation of stock assessment methods: is it me or my model talking? ICES Journal of Marine Science 78, 2244–2255.

Künsch, H.R., 1989. The jackknife and the bootstrap for general stationary observations. Annals of Statistics 17, 1217–1241.

Makridakis, S., Spiliotis, E., Assimakopoulos, V., 2020. The M4 Competition: 100,000 time series and 61 forecasting methods. Int J Forecasting 36, 54–74.

Makridakis, S., Spiliotis, E., Assimakopoulos, V., 2022. The M5 accuracy competition: results, findings, and conclusions. International Journal of Forecasting 38, 1346–1364.

Regular, P.M., et al., 2025. Assessment of the Northern cod stock in NAFO Divisions 2J3KL in 2024. DFO Can. Sci. Advis. Sec. Res. Doc. 2025/048.

Scanlon, B.R., et al., 2003. Barton Springs segment Edwards. Groundwater.

---

"""
rule("V11-05",
 "No Spec A margin against persistence has an interval excluding zero, though several Spec B margins do.",
 "No Spec A interval excludes zero, though several Spec B intervals do.")

rule("V11-06",
 "The predictand is retrospectively reconstructed and catch is supplied along the horizon — a conditional hindcast, not an operational forecast — and total landings are not age-structured removals, so failure to reproduce the collapse with the supplied catch does not test whether fishing caused it.",
 "The predictand is retrospectively reconstructed and catch is supplied along the horizon — a conditional hindcast, not an operational forecast — and total landings are not age-structured removals, so the failed collapse reproduction does not test whether fishing caused it.")

rule("V11-07",
 "is accordingly ≈ 25 CPU-hours and remains a registered longer campaign",
 "is accordingly ≈25 CPU-hours and remains a registered longer campaign")

rule("V11-08",
 "Uncertainty is reported via Diebold–Mariano HAC and moving-block bootstrap per Künsch (1989).",
 "Uncertainty is reported via Diebold-Mariano HAC and moving-block bootstrap per Künsch (1989).")

rule("V11-04",
 "- `batch 7 (audits of agent arena 1 paper rewrites)/results/e3_dm_uncertainty.csv` (10 rows)",
 "- `batch 7 (audits of agent arena 1 paper rewrites)/results/e3_dm_uncertainty.csv` (10 rows)\n\n" + refs)

open(DST, "w").write(t)
print(f"\n{len(applied)} rules applied: v24 {71} refs -> v25 {len(t)} chars")

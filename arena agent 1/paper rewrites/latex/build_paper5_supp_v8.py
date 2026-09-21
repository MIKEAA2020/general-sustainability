#!/usr/bin/env python3
"""Build paper5 supplementary v8 from v7: SOI-block repair + A6 discharge.

Asserted substitutions only. S4: artifact-free SOI values, Chile->global-taxon
label correction, |r|~0.31 pipeline documentation, era-split/collapse-exclusion/
reported-only/registration cuts. S8: screen/power requirements discharged +
certification-tier upgrades. NOT touched: S1-S3, S5-S7 (out of scope).
"""
import os
import sys

SRC = "/home/user/paper5_v29/paper5_supplementary_v7.md"
DST = "/home/user/paper5_v30/paper5_supplementary_v8.md"

SUBS = [
("S4-fig031-pipeline",
"cross-correlation gives $|r|\\approx0.31$ with ENSO leading catch.",
"cross-correlation gives $|r|\\approx0.31$ with ENSO leading catch (detrended log catch against NINO1 at one-year lead, r = -0.31, p = 0.009)."),

("S4-series-labels",
"(Peru entity 604 taxon 87, `shortened.txt`, and Chile `SAU Taxa 600004 v50-1.csv`, both 1950\u20132019; NOAA PSL ERSSTv5 NINO1/NINO3/NINO3.4/NINO4 and PSL SOI, annual means; artifacts under `analysis/anchoveta_enso/`)",
"(Peru entity 604 taxon 87, `shortened.txt`, and the global taxon-600004 aggregate, `SAU Taxa 600004 v50-1.csv`, both 1950\u20132019; NOAA PSL ERSSTv5 NINO1/NINO3/NINO3.4/NINO4 and PSL SOI, annual means over available months (1950 SOI absent); artifacts and verification record under `analysis/anchoveta_enso/`)"),

("S4-clean-soi",
"Peru\u2013SOI r = +0.513 (lag 0, p < 0.0001), +0.419 (lag 1), +0.396 (lag 2); Chile\u2013SOI r = +0.390 (lag 2, p = 0.001) and +0.417 (lag 4); ten of ninety index\u2013lag cells significant at BH-FDR 0.05, all of them SOI cells.",
"Peru\u2013SOI r = +0.073 (lag 0), +0.158 (lag 1), +0.014 (lag 2), all n.s.; global-series\u2013SOI r = +0.052 (lag 0), -0.047 (lag 2), +0.007 (lag 4), all n.s.; zero of ninety index\u2013lag cells significant at BH-FDR 0.05."),

("S4-family",
"The ninety index\u2013lag cells are the BH family; the Granger and split-half tests are confirmatory and outside it.",
"The ninety index\u2013lag cells are the BH family; the Granger tests are confirmatory and outside it."),

("S4-granger-era-cut",
"Granger one-sided ENSO\u2192catch in both stocks (Peru p = 0.00009, Chile p = 0.00016, at lag 2; reverse directions p \u2265 0.19); split-half confines the association to 1950\u20131984 (lag-one r = +0.42, p = 0.013; after 1985 r = +0.13, n.s., with the lag-two cell reversing sign), and the early-period strength survives exclusion of the three collapse years (r = +0.46, p = 0.010) and a reported-catches-only sensitivity on the Chilean series (r = +0.39, p = 0.024), so the post-1985 attenuation is not a reconstruction artefact.",
"Granger one-sided ENSO\u2192catch in both series (Peru p = 0.00009, global-taxon p = 0.00016, at lag 2; reverse directions p \u2265 0.19)."),

("S4-registration-cut",
" Registered strengthening tests (\u00a73.6): the era-split attribution as focal test, the pathway model, and the fixed SOI index\u2013lag specification.",
""),

("S8-unreproduced-scope",
"and the retrospective computational and data results remain unreproduced.",
"and the other retrospective computational and data results remain unreproduced."),

("S8-discharge",
"The registration requirements not yet discharged are: the legacy stage registration's initial histories and solver configuration; the RAM stock identifiers and eligibility table; the processed series and spectral routines; the power-simulation code and seeds; and the case-screening table and query log.",
"The registration requirements not yet discharged are: the legacy stage registration's initial histories and solver configuration; and the case-screening table and query log. Discharged with the deposited material: the RAM stock identifiers and eligibility table; the processed series and spectral routines; and the power-simulation code and seeds."),

("S8-tiers",
"Nothing reported in this article reaches beyond the nominal tier except the logistic crossing record, which S1 reports as re-execution-verified on the companion hold map (independent crossing-scan and exact-hold monodromy implementations, each with validation gates).",
"Nothing reported in this article reaches beyond the nominal tier except the logistic crossing record, which S1 reports as re-execution-verified on the companion hold map (independent crossing-scan and exact-hold monodromy implementations, each with validation gates); the spectral-screen zero count, re-execution-verified by bit-exact re-execution of the deposited screen with deterministic multiplicity reconstruction; and the power values, independently re-executed by a driver reimplementation reproducing the reported values within fixed-seed Monte Carlo noise."),
]

def main():
    s = open(SRC, encoding="utf-8").read()
    for name, old, new in SUBS:
        n = s.count(old)
        if n != 1:
            print(f"FAIL {name}: count={n}")
            sys.exit(1)
        s = s.replace(old, new)
        print(f"ok {name}")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    open(DST, "w", encoding="utf-8").write(s)
    print("wrote", DST, len(s), "bytes")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Phase D pass (v17 -> v18): remnant/redundancy fixes + the prospective-registration
subsection (register item claude 4.10, pairing with AD4). One coordinated pass, asserted rules.
"""
import sys

SRC = "framework/paperF1_retention_framework_v17.md"
DST = "framework/paperF1_retention_framework_v18.md"

s = open(SRC).read()
RULES = []
def rule(old, new, label, n_expected=1):
    RULES.append((old, new, label, n_expected))

# ---------------- redundancy / remnant fixes ----------------
rule("Even with future catch supplied — an advantage no operational forecast has — structural modules still lose to persistence, which turns the conditional-hindcast caveat from a limitation into evidence.",
     "The supplied future catch — an advantage no operational forecast has — does not change the outcome, which turns the conditional-hindcast caveat from a limitation into evidence.",
     "D01 Section 1 catch-supplied sentence rephrased")

rule("Even with future catch supplied — an advantage no operational forecast has — structural modules still lose to persistence, which strengthens the negative result.",
     "Structural modules still lose to persistence despite the supplied future catch, which strengthens the negative result.",
     "D02 Section 7 catch-supplied sentence rephrased")

rule("depensation D4); M3 and M4 were never simulated as generating truth, so no power estimate exists for them.",
     "depensation D4).",
     "D03 Section 4.3 M3/M4 clause dropped (stated in 4.2)")

rule(" unexplained term dwarfs catch treatment difference. Total landings is not age-structured removal, so null does not test whether fishing caused collapse. The Rose stall overlaps",
     " unexplained term dwarfs catch treatment difference. The Rose stall overlaps",
     "D04 Section 5.1 duplicate removal sentence dropped")

rule("predictand retrospectively reconstructed catch supplied along horizon — conditional hindcast not operational forecast, total landings not age-structured removal, C_t total landings while S_t SSB so removal term not SSB-equivalent failing to reproduce collapse with supplied catch path does not test whether fishing caused collapse.",
     "predictand retrospectively reconstructed and catch supplied along the horizon — a conditional hindcast, not an operational forecast; total landings are not age-structured removals, so failure to reproduce the collapse with the supplied catch does not test whether fishing caused it.",
     "D05 Section 8 collapse clause compressed")

rule("Post-2007 h=5 reversal M1 17.16 vs persist 25.10 reported without changing one-year retention statement. h=5 compares no-change forecast with iterated trajectories, iterated affine analogue M2m 17.44 ft (rolling h=5) and 17.64 ft (fixed-window h=5, n=12), each near the corresponding training mean.",
     "Post-2007 h=5 reversal M1 17.16 versus persist 25.10 reported without changing the one-year retention statement. h=5 compares the no-change forecast with iterated trajectories.",
     "D06 Section 5.2 duplicate estimation sentences compressed")

rule("The same five-rung ladder and the same estimation functions are used across both domains and in the simulation (Section 4.2). Post-2007 h=5 reversal M1 17.16 vs persist 25.10 reported without changing one-year retention statement.",
     "The same five-rung ladder and the same estimation functions are used across both domains and in the simulation (Section 4.2).",
     "D07 Section 2.1 post-2007 sentence dropped (kept in 5.2)")

rule("MAE tie (10.72 vs 10.73 ft)",
     "MAE tie (10.72 versus 10.73 ft)",
     "D08 prose vs -> versus (abstract, Table 4, Sections 5.2, 8)", 4)

rule("(12.71 ft vs 12.84 ft)",
     "(12.71 versus 12.84 ft)",
     "D09 prose vs -> versus (abstract + Section 5.2)", 2)

rule("| Simulation power context | D1 0.965/0.960 high at T=33 low/high σ — non-retention strong evidence against autonomous at collapse-window parameters and low noise; D2 high-noise power 0.060 shows strength conditioned on noise regime | D3 0.090/0.110 and D4 0.005/0.015 low — non-retention weak evidence for stock-flow/depensation, identification limit 3.8%/25.8% versus 62.7%/64.5% |",
     "| Simulation power context | D1 0.955/0.960 high at T=33 low/high σ — non-retention strong evidence against autonomous at collapse-window parameters and low noise; D2 high-noise power 0.060 shows strength conditioned on noise regime | D3 0.110/0.100 and D4 0.010/0.010 low — non-retention weak evidence for stock-flow/depensation, identification limit 1%/11% and 37%/18% versus 61% |",
     "D10 Section 6 table row synced to pinned-seed numbers")

rule("At T=71 (10 replicates per cell): D1 power 0.900/1.000, D5 false retention 0.000/0.000; the 200-replicate T=71 design remains a registered longer campaign (Section 4.2).",
     "At T=71 (10 replicates per cell): D1 power 0.900/1.000, D5 false retention 0.000/0.000; the 200-replicate T=71 design remains a registered longer campaign (Section 4.2). The locked length-sensitivity rule (Amendment 1: |Δ| ≤ 0.15) is satisfied — D1 power differs between T = 33 and T = 71 by 0.055 (low σ) and 0.040 (high σ).",
     "D11 Section 4.3 length-sensitivity result appended")

rule("Power map heatmap (archived as figure, data in sim_retention_power.csv) power by DGP×σ with thresholds marked shows D1 high, D3/D4 low.",
     "A power map (power by DGP × σ with the adequacy thresholds marked; archived as a figure) shows D1 high and D3/D4 low.",
     "D12 Section 4.3 heatmap sentence formalized")

rule("The T=71 extension (10 replicates per cell) gives D1 power 0.900/1.000 and D5 false retention 0.000/0.000; the full 200-replicate T=71 design remains a registered longer campaign.",
     "The T=71 extension (10 replicates per cell) gives D1 power 0.900/1.000 and D5 false retention 0.000/0.000 (Section 4.3).",
     "D13 Section 7 T=71 repetition trimmed")

rule("M3 and M4 were never simulated as generating truth, so non-retention of the residual and delay modules has no estimated power.",
     "Non-retention of M3 and M4 has no estimated power, because the residual and delay modules were never simulated as generating truth.",
     "D14 Section 7 M3/M4 sentence rephrased")

rule("Climate modules three of four within 0.13 ft of AR(1), R-AR variant 0.41 ft worse, none retained, M2_Rprecip and M2_Rar edge past M1, all lose to climatological fluxes.",
     "No climate module is retained; three of four lie within 0.13 ft of the autoregression and all lose to the climatological-flux map.",
     "D15 Section 8 climate sentence compressed")

# ---------------- Phase D: prospective registration ----------------
rule("---\n\n## 5. Applications — verified numbers",
     "### 4.7 Prospective registration\n\nNothing in the preceding sections commits the standard to a future evaluation. This subsection fixes the elements of that evaluation in advance, so that the next applications of the standard are commitments, fixed before their data are seen.\n\n**Model set.** The seven-member ladder of Section 2.1 (five structural modules plus the persistence and training-mean baselines), the horizons h = 1 and h = 5, the one-step least-squares estimator with expanding training windows (minimum eight years), and the class-grounds pre-gate are carried forward unchanged. Additions to the ladder require a pre-registered amendment of the kind that introduced D6 and D7 (Amendment 1).\n\n**Next origins.** Edwards J-17: the ten annual origins 2024–2033, each scored once with the recharge and pumpage available at that origin. Northern cod: Specification B origins from 2025 onward, re-scored as each new xteNCAM vintage is published (Regular et al. 2025 line); Specification A is closed, because its predictand is the fixed 2016 assessment vintage and no further origins exist. Archived origins are never re-scored for a published verdict; new origins are scored once, and the archived forecast files are appended.\n\n**Prospective band.** For future applications the 5% band is replaced by the simulation-calibrated band registered in Section 4.5: before any new origin is scored, the object's own ladder is simulated at its own series length and noise scale, with each in-class member as generating truth and the persistence-true null for specificity, and the smallest band attaining power ≥ 0.80 and specificity ≥ 0.90 is adopted; if no band attains both targets, the attainable frontier is reported and the 5% band is retained. The calibration applies to future applications only and does not re-open any verdict reported here.\n\nWith these elements fixed, the reporting obligations of Sections 2 and 3 and the operating-characteristic discipline of this section extend unchanged to every future verdict.\n\n---\n\n## 5. Applications — verified numbers",
     "D16 Section 4.7 Prospective registration inserted")

rule("it never re-opens the verdicts reported here, which remain decided by the pre-registered 5% band.",
     "it never re-opens the verdicts reported here, which remain decided by the pre-registered 5% band (the calibration procedure is specified in Section 4.7).",
     "D17 Section 4.5 AD4 sentence cross-referenced to 4.7")

rule("Climate modules: three of four lie within 0.13 ft of AR(1), the R-ENSO variant is 0.41 ft worse, none retained; M2_Rprecip and M2_Rar edge past M1 at h=1 (12.71 versus 12.84 ft) while M2_Renso and combo do not; all lose to climatological fluxes and training mean (16.80 ft versus 21.11 ft at h=5, interval excluding zero).",
     "Climate modules are never retained; three of four stay within 0.13 ft of the autoregression, all lose to the climatological-flux map, and the training mean beats persistence at h=5 (16.80 ft versus 21.11 ft, interval excluding zero).",
     "D20 abstract climate sentence compressed (was verbatim with Section 5.2)")

rule("120.5095 vs 120.5406", "120.5095 versus 120.5406",
     "D21a Section 2.1 archived-values vs -> versus")
rule("114.8024 vs 114.7665", "114.8024 versus 114.7665",
     "D21b Section 2.1 archived-values vs -> versus")

rule("Sections 5 and 6 apply the rule to three scored objects and compare. Section 7 states what the standard extracts from the pair, and what it does not license.",
     "Sections 5 and 6 apply the rule to three scored objects and compare. Section 7 states what the standard extracts from the pair, and what it does not license. Section 4.7 registers the standard's next applications prospectively.",
     "D18 Section 1 components list mentions 4.7")

rule("All input data, analysis scripts, result files, and the pre-registered specifications are archived at https://github.com/MIKEAA2020/general-sustainability/tree/edwards-framework-e1 and https://zenodo.org/records/22553609 (E1) and 22552680 (E3).",
     "All input data, analysis scripts, result files, and the pre-registered specifications are archived at https://github.com/MIKEAA2020/general-sustainability/tree/edwards-framework-e1 and https://zenodo.org/records/22553609 (E1) and 22552680 (E3); the prospective registration of Section 4.7 is filed with the specification sheets.",
     "D19 Data availability points to the prospective registration")

# ---------------- apply ----------------
counts = {}
for old, new, label, n_exp in RULES:
    n = s.count(old)
    counts[label] = n
    if n != n_exp:
        print(f"FAIL {label}: '{old[:70]}...' occurs {n} times (expected {n_exp})")
        sys.exit(1)
    s = s.replace(old, new)

open(DST, "w").write(s)
print(f"applied {len(RULES)} rules (each asserted, expected counts met)")
print(f"v17: {len(open(SRC).read())} chars -> v18: {len(s)} chars, {s.count(chr(10))} lines")
for label, n in counts.items():
    print(f"  ok  {label}")

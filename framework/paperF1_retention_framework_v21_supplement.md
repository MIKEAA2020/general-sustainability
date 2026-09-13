# Supplement S1 — moved verification and sensitivity detail

*Companion to paperF1_retention_framework_v21_restructured.md. Numbering below follows the companion main text: “Section 4.5” reads as Section 6.5, and “Section 4.6” as its open-problem summary.*

## S1.1 Uncertainty-robust variants (from Section 6.5 of the main text)

**Uncertainty-robust variants (sensitivity analyses, run after the pre-registered campaign).** Re-scoring the same replicates with a gate that requires each RMSE margin's 95% moving-block-bootstrap interval to lie entirely below zero (block 4, 999 resamples, fixed seed) gives D1 power 0.64/0.64 (n=25 per cell) versus 0.92/1.00 under the 5% band, D2 0.24/0.00, D3 and D4 0.00/0.00, and D5 specificity 1.00/0.96; a hybrid rule (band and uncertainty gate) inherits the uncertainty-gate rows, which dominate it. A Hansen–Lunde–Nason model confidence set (α = 0.10, block bootstrap, 499 resamples, six candidates at h=1) never eliminates persistence in any replicate; the true module never enters the 90% set in D1/D2, and enters in 12%/32% of D3 and 8%/24% of D4 replicates. Two readings follow. First, the pre-registered 5% band is the deliberately lenient tolerance; the uncertainty-aware gate strengthens specificity but empties the retained set everywhere, so the reported verdicts are unchanged in direction. Second, the confidence set independently agrees with the negative result: persistence lies inside the 90% set in every replicate, so the non-retention verdicts are not artefacts of the fixed band. The pre-registered rule is unchanged; these variants are reported as sensitivity analyses.
## S1.2 Open problem — pre-check diagnostic (from Section 6 of the main text)

Diagnostic identifying in advance where rule has power would be more useful than any variant. Two candidates examined. Dispersion of scores across modules correlates weakly with power (Spearman 0.52). Margin of best-scoring module over baseline correlates strongly (0.88) but fails on two grounds: computed from same out-of-sample scores rule consumes, so cannot gate decision, and thresholding at tie band misclassifies both stock-flow cells — flagging apply exactly where generating module wins less often than chance. Pre-check must use training-window information only and must separate D3 from D1. Neither candidate does. Identifying when rule has power remains open, stated as open problem with two failed candidates and D3 counterexample, rather than proposing diagnostic that does not work.

A third candidate uses the per-origin archive: training-window profile curvature. Mean one-step squared error by origin year is flat and 2–4× below persistence for M1 in D1, but M2's error spikes 33-fold above persistence exactly at the catch-regime transition inside the forecast path (origin 1991: 14,802 versus 446 kt²) — a flag computable from training-window information alone, since the catch schedule is known ex ante. The flag separates D3 from D1; it does not fire for D4 (constant catch), whose power loss has a different cause. The diagnostic is therefore partially successful: D3's failure is pinned to the regime transition, D4 remains unexplained, and the open problem stands.

## S1.3 Verification appendix (from the pre-restructure manuscript)

```
COD Spec A coarse-regime:
 h=5 M1b 288.58 vs persist 264.72 +9.01%
 h=5 M1 288.72 vs persist 264.72 +9.07%
 h=1 M1b 114.80 vs persist 98.05 +17.09% (comparator M1b vs persistence Spec A h=1 17.09%)

COD Spec B mixed-origin:
 h=5 M1 431.90 vs persist 317.71 +35.94%
 h=1 M1 119.47 vs persist 87.65 +36.30%
 h=5 M1b 445.48 vs persist 317.71 +40.22%

COD Spec B origin-matched:
 h=5 M1 431.90 vs persist 299.98 +43.98%
 h=1 M1 119.47 vs persist 84.43 +41.50%

COD capelin module origin-matched:
 Spec A 150.02/262.34 vs persist 97/193 loses every cell
 Spec B 132.02/491.74 vs persist 79/288 loses every cell

EDWARDS:
 h=5 M2m 17.4449 vs persist 21.1056 -17.34%
 h=1 M2m 12.2832 vs persist 13.2301 -7.16% only separated
 h=1 M1 12.8391 vs persist 13.2301 -2.96% tie
 h=1 oracle 7.5467 vs persist 13.2301 -42.96% under fitted map
 h=5 oracle 10.8645 vs persist 21.1056 -48.52%

EDWARDS gate decomposition:
 M2m h=1: 12.2832 vs persist 13.2301 (band 12.5686) -> H2 pass | vs M1 12.8391 -> H1 FAIL (4.33%)
 M2m h=5: 17.4449 vs persist 21.1056 (band 20.0503) -> H2 pass | vs M1 21.2514 -> H1 pass
 M1 h=1: 12.8391 vs persist 13.2301 (band 12.5686) -> H2 FAIL
 M1 h=5: 21.2514 vs persist 21.1056 (band 20.0503) -> H2 FAIL
 Post-2007 h=5 reversal M1 17.16 vs persist 25.10 reported without changing one-year retention
 h=5 compares no-change forecast with iterated trajectories, iterated affine analogue M2m 17.44 ft (rolling h=5) and 17.64 ft (fixed-window h=5, n=12), each near the corresponding training mean
 h>1 climate scores reuse the one-step forecast held constant — no h-year-ahead recharge or pumpage forecast is available at the origin, and the one-step forecast is the only origin-available flux estimate
 Fixed-window pre-permit pass uses its declared train 1980–1990 (11 yr); the 15-year floor applies to rolling origins only — fixed windows use their declared training sets
 No year falls below 240-observation floor minimum n=242 1939 rule vacuous on this panel
 Q = -2876+4.77H implies Q=0 near 603 ft below ≈618 reference predicts 1956 tail failure

SIMULATION:
 D1 0.955/0.960 power exceeds 80% bar
 D2 0.780/0.060 near bar / below
 D3 0.110/0.100 below bar <20% chance
 D4 0.010/0.010 below bar
 D5 specificity 0.995/0.950
 False retention: 0.034 per module-replicate pair D1-D4 wrong-module,
 0.005/0.050 per replicate D5, 0.0055 per module-replicate null
 D6 0.633/0.733 D7 0.933/0.867 vs 0.10 threshold — specificity conditional
 Power map figure heatmap power by DGP×σ with thresholds marked
 Pre-check open problem with two failed candidates and D3 counterexample; a third candidate (training-window profile curvature) flags D3 but not D4
 Rule comparison from archived output — information criterion n log MSE + 2k (AIC-style), MASE, bare beat-persistence, 0%/10% band variants, no refitting
```

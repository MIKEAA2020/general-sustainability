# Broader-fishery analysis — full public RAM cohort vs the archived 43-stock class cohort (2026-09-03)

**Directive.** Evaluate, verify, improve and augment if applicable, before implementing;
run the broader fishery analysis — full public RAM Legacy v4.66 ADH cohort (all assessed
stocks) under the recovered zeros-included protocol, with composition comparison against
the 43-stock small-pelagic class cohort; results computed locally; **main-vs-supplementary
placement decision deferred until results are in (owner instruction)**. No paper edit is
made in this record; placement options are listed at the end.

## 1. Protocol recovery — the earlier numbers are now re-executable

The supplementary's version-sensitivity table quoted v4.66 = 454 stocks / 69 zeros /
median 3.39 yr and v4.44 = 415 / 63 / 2.57, computed in an earlier turn without a
recorded micro-specification. A protocol grid over the two public releases
(2 last-year rules × 2 B_lim bases × 2 F-handlings × 2 zero definitions) against both
targets recovers the exact specification:

- qualifying: stocks with ≥ 1 finite SSB and ≥ 1 finite F;
- SSB_now = last finite SSB value; **F_now = last finite F value of its own series**
  (not carried back to the SSB year); stocks with F_now ≤ 0 are dropped;
- B_lim = 0.2 · max(SSB) over all SSB-finite years;
- ADH = max(0, F_now⁻¹ · ln(SSB_now / B_lim)); median over all qualifying stocks,
  zeros included.

Under this pinned protocol both anchors reproduce to the printed precision:
**v4.66: 454 / 69 / 3.3893 (≈ 3.39); v4.44: 415 / 63 / 2.5683 (≈ 2.57)**.
Every variant tested nearby gives medians in 2.5–3.9 — the broad-vs-class gap is not a
protocol artifact. (Computed on the assessment-data RData of Zenodo 14043031 and
2542919, exported via the release's own R loader.)

## 2. Broad v4.66 cohort

n = 454; zeros = 69 (15.2%); median 3.3893 yr (positives-only 4.1301); quartiles
0.7951 / 3.3893 / 10.0813; max 1555.9 (an elasmobranch); F quartiles 0.080 / 0.214 /
0.464; log(SSB/B_lim) quartiles 0.398 / 0.947 / 1.374.

## 3. Composition comparison (taxGroup, v4.66)

| group | n | zeros | median ADH | median (positives) | max |
|---|---:|---:|---:|---:|---:|
| elasmobranchs | 19 | 2 | 11.51 | 12.96 | 1555.9 |
| sebastids | 33 | 1 | 9.03 | 9.13 | 163.8 |
| pleuronectids | 59 | 8 | 5.99 | 7.40 | 517.9 |
| other scorpaenids | 11 | 0 | 3.99 | 3.99 | 16.1 |
| crabs-lobsters | 22 | 3 | 3.90 | 5.48 | 40.0 |
| other marine fish | 39 | 7 | 3.73 | 4.88 | 87.7 |
| other marine percoidids | 60 | 7 | 2.87 | 3.40 | 53.8 |
| **forage fish** | 64 | 12 | **2.69** | 3.63 | 718.7 |
| tuna-billfish | 16 | 4 | 2.57 | 3.17 | 42.5 |
| bivalves-gastropods | 5 | 2 | 2.57 | 3.20 | 65.2 |
| gadids | 83 | 16 | 2.17 | 3.48 | 50.7 |
| carangids-mackerels | 20 | 5 | 1.62 | 3.46 | 65.5 |
| shrimps | 23 | 2 | 1.08 | 1.34 | 7.3 |
| **overall** | 454 | 69 | 3.39 | 4.13 | 1555.9 |
| **archived 43 (class cohort)** | 43 | 8 | **1.79** | 2.86 | 201.2 |

The life-history gradient is clean: long-lived groups (elasmobranchs 11.5, sebastids
9.0, pleuronectids 6.0) sit far above fast-turnover groups (shrimps 1.1, carangids 1.6,
forage fish 2.7). The broad median of 3.39 is carried by the long-lived groups, exactly
as the directive's memo expected.

## 4. Overlap and vintage decomposition

33 of the 43 archived ids exist in current v4.66; 10 are gone (dropped or merged:
HERR2532/HERR30/HERR31 → HERR30-31; HERRVIa → HERRVIaVIIbc; ANCHMEDGSA17 →
ANCHMEDGSA17-18; ANCHMEDGSA9, PANCHCHVX, PANCHNCH, PANCHSCH, SPRATNS absent). Among
the 33 shared ids, per-stock ADH deltas (current minus archived) have mean |Δ| = 3.44 yr;
11 are unchanged, 22 differ materially (HERRVIaVIIbc 13.17 → 0; SPRBLKGSA29 4.82 →
25.29; ANCHMEDGSA16 0 → 3.18; HERR4RFA 21.97 → 10.45).

**Vintage counterfactual.** The archived-vintage median over the 33 extant ids is 2.79 yr,
and their current-vintage median is 2.34 yr. The full-43 archived median of 1.79 is
therefore pulled down substantially by the 10 since-dropped ids, which carried the low
end of the archived distribution — the archived cohort's lowness is a property of its
extract-time stock list and series, not of the small-pelagic class alone (the current
forage-fish group median is 2.69).

## 5. Random-draw null (directive option 3)

10,000 draws of 43 stocks (without replacement) from each pool; distribution of the
sample median:
- broad 454 pool: median-of-medians 3.354; [2.5%, 97.5%] = [1.852, 5.480];
  **2.12% of draws have median ≤ 1.7902**;
- current forage-fish pool (64): median-of-medians 2.790; [2.5%, 97.5%] =
  [2.308, 3.565]; **0.29% of draws have median ≤ 1.7902**.

The archived 1.79 is unusually low even against its own life-history group in the
current release. Honest scope: the class cohort is not a random sample from either
pool (it is a dated extraction with a selection rule), so these percentiles are a
descriptive benchmark, not a selection-bias hypothesis test.

## 6. Verdict on the directive memo's expectations

| Expectation | Result |
|---|---|
| Broad median ≈ 3.4, above the class cohort's 1.8 | Confirmed: 3.3893 vs 1.7902 (≈ 1.9×) |
| Larger share of long-lived species in the broad sample | Confirmed: 83 gadids + 59 pleuronectids + 33 sebastids + 19 elasmobranchs + others vs zero in the class cohort |
| Fewer zero entries relative to size | Confirmed but small: 15.2% vs 18.6% |
| Difference mostly cohort composition, not error | Confirmed and refined: the broad-vs-class gap decomposes into (i) life-history composition (long-lived groups dominate the upper end), (ii) the archived stock list itself (the 10 dropped ids carried the low end), (iii) series revisions among the 33 shared ids (mean \|Δ\| = 3.4 yr) |
| "1.8 is not a general fisheries statistic" | Confirmed at every level tested |
| Vintage-mismatch caveat (label the comparison) | Confirmed necessary and now quantified (Section 4) |
| Protocol-consistency caveat | Resolved stronger than asked: the exact protocol is recovered and both earlier anchors reproduce to printed precision |

## 7. Placement options (decision deferred to the owner, per instruction)

- **Supplementary (recommended by the directive memo):** extend S5 of
  `paper3_supplementary_v5.md` with the group table, the null-draw record, and the
  vintage decomposition; the main-text class-scope sentence already present in P3 v15
  stays as is (optionally citing 3.4).
- **Main text:** a one-sentence addition to P3's fisheries paragraph citing the broad
  3.4 median and the class-scope statement (the class-scope sentence is already in
  P3 v15; the only new main-text content would be the broad-median number itself).
- **Hybrid:** supplementary table + main-text citation.

Nothing is edited until the owner chooses. Artifacts:
`analysis/ram_adh_fisheries/{v466_broader_cohort.csv, v444_adh_cohort.csv,
broader_results.json, random_draw_results.json, overlap.json}` (local-only, outside the
two GitHub folders).

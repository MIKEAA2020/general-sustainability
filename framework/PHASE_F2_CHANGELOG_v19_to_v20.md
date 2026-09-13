# Phase F2 changelog — v19 → v20 (2026-09-13)

Phase F2 = the second journal-fit text pass from the merged plan (O8, O12). 6
asserted rules; v19 frozen.

- **O8 — the information criterion as a co-primary instrument.** §4.5 gains a
  post-freeze check block written from the archived O9 computation
  (`phase_c/results/o9_ic_coprimary_20260913.json`, Phase G), with the instrument
  disclosed in full (IC = n ln(RMSE²) + 2k, one-step, fitted-scalar-parameter
  counts). Results: the penalty moves identification toward the simpler model
  (D1 0.51→0.87 / 0.565→0.86, D2 0.81→0.94 / 0.70→0.87) and lowers it where the
  truth itself carries the extra parameter (D4 0.37→0.06 / 0.18→0.07; D3
  0.01→0.01 / 0.11→0.19); false identification under persistence truth
  0.5%/3.5% versus the rule's 0.5%/5.0%. On the scored objects the check is
  decisive: cod Spec A and B — the criterion selects persistence, agreeing with
  the empty retained set; Edwards — it selects M2m, the class-grounds-declined
  climatological-flux map (IC 455.5 vs M1 463.5 vs persistence 464.9), the one
  module whose retention the standard withholds on the comparator gate (4.33%
  inside the 5% band) and class grounds. Conclusion: the criterion's dominance
  does not carry the decision-relevant edge case; verdicts unchanged; the
  divergence is exactly the case where §5.2 shows the gates to be load-bearing.
  Archive path added to Data availability.
- **O12 — parenthetical density unpacked.** The four densest passages are now
  narrated in plain sentences with the numbers retained in Table 2 / Section 6:
  the abstract's Spec B chain, §5.1's capelin chain, and §8's cod and
  groundwater chains.

## Verification

Idempotent byte-for-byte re-apply; formalization 0 flags; redundancy 0 findings;
style PASS; content coverage vs v0/v13 clean. v20: 76,179 bytes / 75,393 chars.

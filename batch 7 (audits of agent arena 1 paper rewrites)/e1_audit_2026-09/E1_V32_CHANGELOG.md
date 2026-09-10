# E1 v32 — round-6 correction pass

**Base:** v31. Corrections only. Every item verified by grepping the compiled manuscript
(25-point removed/present check, all pass).

## Tier 1

| # | Change |
|---|---|
| **H1** | **M1b comparator restated.** The retention rule listed "M1b against M1" among "the nested steps", while Definition 2.1 and SI-2 prove `𝔰→0` gives the cubic factor `a(S)=S/K`, not Schaefer. M1b's comparator is now declared by **complexity ordering, not nesting**; only M3-against-M2 is a strict nesting. |
| **H2** | **Abstract interval claim corrected.** "Intervals excluding zero only on Specification B" is false — the archived DM file shows A/M4-vs-M3/h=1 at [+4.7, +144.7]. Replaced with the verified statement: no Specification A margin **against persistence** has an interval excluding zero (0 such rows), though several on B do. |
| **H3** | **𝔰 = 0 is an unattained infimum.** The objective rejects `𝔰 ≤ 0` (`0 < 𝔰 < 0.8K`), so `2.1×10⁻²³` is a numerical approach, not an attained boundary estimate. At such values the object is the **zero-threshold cubic branch**, so M1b's lower error is not evidence for depensation. |
| **H4** | **Abstract range made one pass.** 115–206 is Table 5 (annual landings); the primary coarse pass is **115–196**. The abstract now quotes the primary pass throughout. |
| **H5** | **My v31 catch-drop sentence scoped.** "Every module … when the prescribed catch falls" was wrong for M1/M1b, which use a training-mean constant. Now split: M2–M4 respond to the prescribed drop; M1/M1b turn upward because their constant is smaller than the recorded losses. |

## Tier 2

- **H6** five specification fields (was "four", five listed). **H7** "two of the five structural modules (M2 and M4)".
- **H8** "pooled score" → *rolling RMSE pooled over origins within each specification and horizon*.
- **H9** M4 relabelled **lagged initialisation** in Table 2 and the complexity ordering. **H10** the delay/structure split stated as an arithmetic decomposition, not a causal attribution.
- **H11** `K = 105.8` kt described as settling just above the training predictor range, not "collapsing to" it.
- **H13** "Table 1 landings" → Regular et al. (2025) Table 1. **H17** "unbeatable" → none below persistence, which scores zero by construction.
- **H14** eight training years supply **seven** one-step transitions.
- **H25** M1/M1b catch-treatment invariance is **rounding**, not exact: archived values differ by ≤0.04 kt.
- **H26** "M1 and M2 coincide" qualified to the coarse regime (annual: 264 vs 303 kt).
- **H27** smallest deficit given unrounded with its comparator: M1b vs persistence, Spec A h=1, (114.80−98.05)/98.05 = **17.1%**.
- **H28** bootstrap intervals stated as conditional on archived forecast paths, propagating no parameter, revision, catch or covariate uncertainty. **H29** DM relabelled descriptive loss-differential statistics.
- **H30** the `p` column defined as the percentile-tail fraction `2·min{#(Δ*≤0), #(Δ*≥0)}/B`; the six `<0.001` cells replaced by the exact archived **0.000**.
- **H31** the four disagreement rows named in text. **H32** catch–SSB ontology: total landings is not an age-structured removal, so the null does not test whether fishing caused the collapse. **H33** fixed-origin scoping swept into the highlights.

## Guard

**0 blockers**, 7 warnings. The guard caught one real regression here — the
scope phrase "on these two" was dropped while trimming the abstract to 250 words, and was
restored with the length paid for elsewhere.

## Deferred with reasons

- **H34/H35** formal information-set table and canonical origin list (gpt §5, §6): the most
  useful remaining additions, but each is a table assembled from code, not prose. Logged for v33.
- **H36** one-decimal main tables: declined for the tables (high transcription risk on a
  large diff), accepted for individual claims that turn on small differences.
- **H37** Proposition 4.1 tightening, merged with round-5 G17: state for the zero-clipped
  map or on `[ε, S₋)`, and drop the unspecified single-equilibrium case.
- Primary-pass per-origin uncertainty: still a rerun, not a revision.

# E1 v30 — correction pass (round-4 audit)

**Base:** v29. **Nature of the pass:** corrections only. No new ecological content was
added, because round 4 established that the material added in v27–v29 was written faster
than it was checked.

## Tier 1 (correctness)

| # | Change | Source |
|---|---|---|
| F1 | **Identification ridge recomputed with the registered estimator.** The v28/v29 figures (`r` 1.76, RMSE 60.7→74.9, "factor of 5.7") came from a hand-rolled objective on levels. Replicating `run_ladder.fit_params` reproduces the published fit exactly (`r=1.9350, K=1032.72`). Corrected: training RMSE **31.3 → 56.3 → 67.0 kt** at K = 1032.7 / 1500 / 5000, with `r` 1.935 → 0.674 → 0.331. The corrected result **weakens** the earlier claim: a more than twofold rise in training error is not a flat ridge. | grok 1.2 |
| F2 | **Allee bound disambiguated.** The *scored* fit bounds 𝔰 ∈ (0, max_train S] = [0, 81.10] kt; the *profile* uses [0, min_train S] = [0, 9.68] kt. v29 called the minimum "the bound imposed in the code", which is true only of the profile. The boundary estimate is now read as the objective declining to place a threshold it could have placed. | gpt 1.2, grok 1.3 |
| F3 | **"Coverage" recast as a descriptive scale ratio.** Renamed, nominal-95% comparison removed, and two defects disclosed: the published bounds are right-skewed on the biomass scale (67 of 71 asymmetric by >10%, near-symmetric only in logs), and re-centring a target-state interval on a hindcast establishes no coverage. The robustness inference is withdrawn. | gpt 1.1, grok 2.2 |
| F7 | **Headline rescoped** in four places (intro, highlight, abstract, collapse claim) to *pooled rolling-origin RMSE at the two evaluated horizons*, with the regime split flagged and the collapse failure scoped to the **fixed pre-collapse origin**. | gpt 1.4, grok 2.1 |

## Tier 2

- **F8** M3 reads marginally above persistence (59% vs 56%) on the descriptive statistic; now stated rather than passed over.
- **F4** "settles near a fifth of its pre-collapse value at any K" **withdrawn** — true at the fitted K (0.20) but false at K = 5000 (1.12). Only the sign reversal is robust.
- **F5** "undefined for K below the stock size" corrected: undefined only at S=0 and S=K.
- **F6** Period convention stated (transition-start years); counts given; last usable transition begins **2014**, so the final band has 7 transitions.
- **F22** M4 now described as a perturbed initialisation taking **h+1 updates**, verified in `run_ladder.py` (`lead0 = i_te[0] − start_idx`).
- **F23** `r ≈ 2` implausibility claim repaired: in a discrete annual map the multiplier is `1+r = 2.94`, continuous-equivalent `log(1+r) = 1.08` — not comparable to a continuous intrinsic rate as written.
- **F24** MSY/B_MSY relabelled *formal maxima of the fitted curves*, not sustainable yields.
- **F25** "no information about K" → "weakly constrain", with `∂g/∂K = rS²/K²`.
- **F10** Table 7 Specification B baseline replaced with the **origin-matched 84/300**, recomputed from source; mixed-origin 88/318 retained in the caption.
- **F12/F28** Table 3 Direction column now **NA** for both baselines, matching the text.
- **F11** "five consecutive years, 1999–2004" → five consecutive annual decreases.
- **F30/F31** Persistence gloss corrected: beating it needs useful prediction of change, not turning points specifically; the age-at-maturity/generation-time conflation removed.

## Guard override, recorded

`tier3_guard.py` reports 4 B1 blockers: `60.7`, `74.9`, `1.76`, `5.7`. All four belong to
the single erroneous sentence retracted under F1 and are replaced by verified values
(31.3, 56.3, 67.0, 0.674, 0.331). **This is a deliberate retraction of wrong numbers, not
content loss**, and is the one case where B1 is correctly overridden. Every other gate
passes: register 0/0, self-test 5/5, title and thanks byte-identical, abstract 250/250,
highlights ≤85.

## Infrastructure

`tier3_guard_selftest.sh` fixtures moved from `/tmp` to `tools/selftest_fixtures/` after
`/tmp` was cleared twice mid-session and the suite silently degraded to 3/5.

## Not done, deliberately

Primary-treatment (coarse-regime) per-origin uncertainty (gpt 8.4, grok 3.5) requires
archiving forecasts that were never written out — a rerun, not a revision. Recorded as a
prerequisite in the programme document.

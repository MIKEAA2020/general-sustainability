# E1 v34 — information-set and origin tables (H34, H35)

**Base:** v33. Adds the two structural tables deferred since round 6. Both are built from
the scored code and archived per-origin files, not from prose.

## H34 — Table 2b, information set at forecast origin

One table replacing information scattered across many paragraphs. Rows distinguish
**available** (dated at or before the origin) from **supplied** (dated after the origin
and provided anyway):

- target series — available, but a **single retrospective vintage**, not the vintage
  current at each origin;
- origin state, lagged state (M4's start), expanding training transitions, fitted residual;
- catch at or before the origin (training mean for M1/M1b; path for M2–M4);
- **catch after the origin — supplied**, which is the single row that makes this a
  conditional hindcast;
- prey index at or before the origin, carried forward; **future index not used**;
- reference point, entering only the secondary Brier score.

The accompanying sentence names the consequence directly: M2, M3 and M4 receive a realised
catch path no operational forecast would have, while M1 and M1b do not — which is why
their scores are nearly invariant to the catch treatment.

## H35 — Table 2c, canonical rolling-origin sets

Twelve rows giving \(n\) and the origin range for every rolling experiment, with the
minimum-training rule stated: **eight years for the naive baselines throughout, eight for
the Specification A ladder, twelve for the Specification B ladder**. That difference is
the origin-set mismatch behind the matched-baseline corrections in v29–v32, now stated
once in a table rather than repaired in prose each time it surfaces.

The table also documents why the index experiments begin later than the ladder, and why
Specification B admits three pre-break origins (1988–1990) — the point gpt raised as G2 in
round 5, now visible rather than inferred.

## Verification

Every row of Table 2c was **machine-checked against the archived per-origin files**
(`rolling_forecasts.csv`, `xte_rolling_forecasts.csv`, `capelin_index_forecasts.csv`,
`capelin_regime_forecasts.csv`): 10 of 12 rows match archived counts and ranges exactly.
The two baseline rows are not in a per-origin file and were derived independently by
replaying the code's own construction (`range(7, n-1)` against the xteNCAM year vector),
giving 63/1961–2023 and 59/1961–2019 — matching `xte_rolling_summary.csv`.

Information-set facts in Table 2b were each traced to source: `tr[: origin + 1] = True`
(expanding window), `C_path = C_all[start_idx + 1 : origin + h + 1]` (catch supplied along
the horizon), `if not np.isfinite(I[origin])` and the comment `do not use I[origin+1+k]`
(prey known at origin only), and the single `read_csv` of the reconstruction (fixed
vintage).

## Gates

Compile clean; register 0/0; content guard **0 blockers**, 3 warnings; self-test 5/5;
title and `\thanks` byte-identical; abstract 250/250.

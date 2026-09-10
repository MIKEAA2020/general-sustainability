# E1 v20 — Changelog

Implements every surviving item from the round-2 joint audit
(`E1_AUDIT2_JOINT_EVALUATION.md`, main document + addendum). v19 preserved unchanged.
Compiles clean (497,395 B). Scanner: **0 blockers**. Title, author/thanks block, and all
content locks verified byte-identical to v19.

## Tier 1 — correctness

| # | Fix | Source |
|---|---|---|
| A3 | Deleted the false square-root/"different estimands" mechanism. Replaced with the identity √ā−√b̄=(ā−b̄)/(√ā+√b̄), noting the two measures share a sign and a zero null and that what differs is the *variance approximation* (HAC-asymptotic vs block resampling). | gpt |
| A1+A2 | "five of the thirty-two rows" → **"Four of the twenty-eight"**, with all four now named in text. | both (denominator); **mine** (numerator) |
| A4 | M4 delay decomposition recomputed on **matched origins** from the archived per-origin files. Spec B now reads persistence 84.4/300.0, stale control 158.0/337.4, M4 205.7/1030.7; delay 73.6 of 121.3 kt at h=1, model cost 693.3 of 730.8 kt at h=5. Reproduces Table 9's own gap column exactly. | qwen |
| A5 | "negative certificate" → "non-retention outcome"; dropped "M3 and M4 are not certificates here". | qwen |
| A6 | K-bound wording now states the maximum is over **predictor states of the training transitions**, excluding the terminal state — the ambiguity that produced the 81.1-vs-40.8 error earlier in this project. | qwen |
| A8 | "K at bound" → "K resting at the 500-kt multi-start initialiser". | qwen |
| A9 | Prop 4.1: "fixed catch sequence" → **constant catch C_t≡C**; invariant region (0,S_-) → **[0,S_-)** with the clipping justification; **M2 explicitly removed from formal coverage** (time-varying catch ⇒ F_t, not F). | gpt + qwen |
| G1 | "most annual increments are positive" → **"seven of the twelve"**, noting the five negatives form one consecutive run (1999–2004). | gpt |
| G2 | Profile likelihood **reframed as descriptive**. Statistic now written explicitly as n·log{SSE(𝔰)/SSE(𝔰̂)}, n=12. Dropped "settles the identification question" and "confidence set = whole admissible interval". States the four reasons a χ²₁ reference is unjustified (no declared error model, boundary estimate, r at its own bound, 12 transitions, reconstructed states). Conclusion preserved: the objective is flat, 𝔰 is not located. | gpt |

## Tier 2 — completeness / reproducibility

- **G4** M3/M4 residual recursion written out, read off `run_ladder.py`: e_u=ΔS_u−[g(S_u)−C_u] pre-clipping; no-intercept lag-one φ̂=Σe_ue_{u−1}/Σe²_{u−1}, zeroed if denominator ≤0 or <4 residuals, clipped to [−0.95,0.95]; projected residual φ̂^k·e_last added inside the update before clipping to [10⁻³,10⁶] kt. **Not** gpt's guessed indexing.
- **A7** All remaining bounds declared: 𝔰∈[0,max_train S] with 0<𝔰<0.8K enforced in-objective; φ clipped ±0.95; b unbounded. Profile's tighter [0,min_train S] flagged as an estimation bound, not a mathematical admissibility region.
- **G5** M4 relabelled a **stale-start experiment**, not a delayed information set — its parameters are M3's, fitted on transitions ending at S_t, so the later state still reaches the forecast. A true delayed variant would truncate training and is explicitly not scored.
- **G3** "Except in M3." fragment merged; **M4 added** to the exception.
- **G6** "byte for byte" qualified by the pinned environment in both abstract and methods; ±17-kt M1b environment sensitivity disclosed; cross-environment identity not claimed.
- **G7** Score definitions: h=5 is endpoint RMSE (not trajectory-average); log-RMSE natural log with 10⁻³ floor; sign-hit rate adjacent-year, n−1 comparisons.
- **G8** Brier → "threshold misclassification rate (equivalently Brier for a deterministic binary forecast)".
- **G9** Persistence sign-hit rate reported **NA**, not 0.00.
- **C3** DM lag sensitivity now stated as two-sided (A crosses upward 1.14→2.30, B downward 2.81→1.70).
- **C4** "retention turns on H2 alone" → "H2 and H3".
- **C6** Table 10 now carries the two recovery-window 𝔰 values (2.1e−23, 9.4e−6) with r=2.000, as its own claim requires.
- **C2** `DFO 2024b` cited at the capelin index; `Abaee 2026c` cited at the viability question. No uncited references remain.
- **H4** No-transfer rationale restated on trajectory/formulation/coverage/catch grounds; LRP correctly confined to the secondary diagnostic. **The no-pooling rule itself is unchanged** (frozen-spec commitment).
- **B2** Prey-module claim softened: "weakly constrained … and they fail the retention score", with explicit note that no profile was computed for them.
- Block-length robustness scoped to the M1 comparison actually tested.
- "no vintage archive exists" → "assessment vintages were not available for this evaluation".
- "registered alternative" → "untested alternative".

## Overclaim verbs removed (gpt §6, §10)

"driven hard against the upper bound" → "close to but not at"; "surplus production does not
identify the mortality pulse" → "the fitted model does not reproduce the decline"; "evidence
against a catch-regime reading" → "did not improve this implementation's hindcast"; "which
is what the scored comparison then confirms" → deleted; "a more accurate C_t" → "substituting
annual recorded landings"; "that the optimiser does not move K is itself a measure" → the
*profile*, not optimiser behaviour, measures flatness; "slack near zero by construction" →
mean deviation zero over reference years, annual deviations not; leading-indicator
"circular" → retrospective definition does not establish prospective performance.
Final discussion and conclusions matched to the H1/H2 distinction.
**B4:** the "evidentiary standing" ranking against the groundwater paper is gone; the
factual disclosure ("no dated pre-scoring protocol file exists for this study") remains.
Companion citations retained by DOI.

## Not implemented (rejected in the audit)

- **H1** gpt's #1 blocker — "prose and Table 10 reverse the catch labels" — **verified false**; acting on it would have introduced an error.
- **B1** deleting the bootstrap p column (fix the prose, not the procedure).
- **B3** adding a regularized-AR/local-trend comparator — new rung on a frozen ladder; needs a spec amendment.
- **B4/H3** cutting companion citations; restoring "in review".
- **H2** the 34%/1.24 LRP comparison — already correctly dated.
- grok's Tier-3 restructuring (lead with the result, §1 rewrite, demote Def 2.3/2.5 and Prop 3.1 from theorem environments, split 80-word sentences, matched-baseline table promotion) — presentational, deferred, tracked in §J of the evaluation.

**No retention verdict changes.** Persistence still wins on both specifications at both horizons.

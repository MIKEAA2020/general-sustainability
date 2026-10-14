# ECOMOD manuscript — change log v41 → v42

Scope of v42: a research-article rewrite of the v41 technical manuscript. No model, parameter or result was
changed; the registry (Table 1), the demonstration run, the eigenvalues, the ceiling, the drawdown thresholds and
the empirical numbers are identical to v41 and were re-executed (not copied) from the deposited solver before
being typeset. What changed is what the paper claims, in what order, with what evidence in the main text, and
what moved to the supplementary file.

## 1. Framing and contribution (new)

* **Title** → *How aggregation can conceal composition: aggregate biocapacity and the identifiability of modelled
  ecological-capital drawdown.* The v41 title stated a mechanism; the v42 title states the result (an
  identifiability result about an indicator) and the object it applies to.
* **One stated contribution with three parts**, each a proposition with a proof in the main text:
  * Proposition 1 (composition identity, non-identifiability, two discriminating observables);
  * Proposition 2 (balance point, demand ceiling, affine deficit-side dynamics, no fold);
  * Proposition 3 (continuity of the drawdown depth in initial demand — the "no cliff" result, previously only
    numerical).
* **Abstract rewritten** around the identifiability claim; the empirical paragraph now reports what the two
  readings (composition mask / liquidation mask) do and do not allow one to conclude from the NFA series.
* **Introduction rewritten** as a research-question introduction (indicator aggregation → composition → what a
  model can and cannot say → the three questions → contributions), with the literature positioned in one
  paragraph instead of a list. The one-stock history that opened v41 is gone from the main text (now SI S7).
* **New Discussion** structured as: what the result is; what it is not (explicit list of non-claims, including
  that nothing here demonstrates measured capital decline); relation to the earlier one-stock formulation
  (superseded quantities named once); limits of the proxy; implications for indicator reporting and policy
  design; three falsifiable predictions table (Table 4).

## 2. Structure

| v41 | v42 |
|---|---|
| 1 Introduction (long, history-first) | 1 Introduction (question-first, 4 paragraphs + contributions) |
| 2 Model (equations, extensions, registry, numerics, data all mixed) | 2 Model and methods (2.1 equations; 2.2 registry; 2.3 observation operator; 2.4 numerics) |
| 3 Results (12 subsections including the one-stock comparison, the long robustness ladders, gate tables) | 3 Results (3.1 composition identity; 3.2 demand ceiling; 3.3 continuity of drawdown; 3.4 restoration gate sign; 3.5 empirical) |
| 4 Discussion (mostly caveats) | 4 Discussion (6 subsections, see above) |
| 5 Conclusions (restated results) | 5 Conclusions (3 short paragraphs) |
| Appendix-like material in main text | Supplementary Information S1–S7 (separate compiled document, 17 pp) |

Moved to the supplementary file (nothing deleted): the full symbol table and stated extensions (S1); the
derivations behind Propositions 1–3 and the debt fixed points, the boundedness asymmetry, the macro-ratio
identities and the characteristic-equation structure of the full DDE (S2); the numerical protocol, the delayed-
versus-current-quality check and the recompute-then-assert record (S3); the b_f sweep, the drawdown-depth ladder
(new table), the recovery metric (new table), the gate-sign phase-dependence table and the regime table (S4);
the data vintages, the α-robustness table, the level fallback, the cropland calibration, the observation-
operator hierarchy, the regeneration anchors and the recursive identifiability note (S5); the policy extensions
(S6); the one-stock comparator with its equations, superseded quantities and four comparator figures (S7).

## 3. New material

* **Figure 1** (new, three panels): (a) the composition mask at frozen demand; (b) the monotone balance branch
  B_eq(A_c) with the five verified balance points and the floor; (c) drawdown depth versus initial demand for
  four initial capital stocks. Panel (c) is the first graphical statement of the continuity result.
* **Drawdown-depth sweep** (`drawdown_depth.py`, `si_drawdown_depth.csv`): min A_c(t) over a P₀ grid for
  A_c0 ∈ {0.40, 0.70, 1.00, 1.18}; also the final capital with and without restoration and the recovery metric.
* **Table 2** (main) now combines the b_f sweep with the tolerance ladder; **Table 3** (main) gives the NFA
  diagnostics; **Table 4** (main) lists the predictions with their discriminating observables.
* **τ_g inertness of the threshold** re-verified with the corrected (delayed-quality) solver variant and
  reported in SI S3 (Table S2) with the window and endpoint comparison.
* **Explicit statement of what is and is not identified** (Proposition 1(iii), Table S6).

## 4. Writing and presentation

* Author-year citations through natbib (`\citep`/`\citet`); 56 references; all cited works are in the list.
* Theorem environments for the three propositions; proofs in the main text are short (the full derivations are
  in S2).
* Numbers appear once in the main text with their provenance; sweeps live in tables.
* Removed: "Disposition of earlier claims" paragraphs inside Results; repeated caveats; registry values repeated
  in prose; comparisons against the superseded area-based formulation inside the model section.
* Highlights (`HIGHLIGHTS_v42.md`) rewritten to the journal format (≤ 85 characters each).

## 5. Verification

* Both documents compile with `tectonic` (elsarticle preprint, 33 pp main; article 11 pt, 17 pp SI); no
  undefined references or citations; no cell overlaps in tables; floats placed near first reference.
* Numeric-token audit: every number in v41 appears in v42 main or SI, except column widths, citation years
  (now in the reference list) and the `0.0000` conservation residual (now stated as machine precision).
* The demonstration run, the balance points, the ceiling and the eigenvalues are recomputed by
  `make_fig_model.py` with asserts before the figure is written.

## 6. Known items for the author

* Table 1 lists t_wave = 30 yr (v41 text) while the deposited code defaults to 40 yr; the wave is off in every
  reported run, so no result depends on it, but the registry and the code default should be aligned.
* The threshold values at tolerance 10⁻⁶ (2.41/2.70/2.98/3.14) are carried from the deposited verification at
  Δt = 0.05; the v42 sweep used Δt = 0.1 and gives 2.39/2.68/2.96/3.12, consistent with the quoted bands.

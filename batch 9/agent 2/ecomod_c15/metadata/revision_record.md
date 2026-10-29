# External author-facing revision record

This record is separate from the article and SI. Earlier packages are preserved; this is a new C15 package.

## Restored exactly

- C13 abstract, including the 46.16% figure and explicit imposed-quality-bound distinction.
- Introductory exposition, both orchard/elevator analogies and the three research questions.
- The concluding orchard paragraph, including “A harvest total is not a census of the orchard.”
- Author acknowledgments.
- The original author-supplied AI declaration, verbatim: “DeepSeek AI and Claude (Anthropic) assisted with computational-reproducibility checks under the author's supervision; the author reviewed and edited the content and takes full responsibility for the publication.”

## Scientific corrections and clarifications

- Main identification bound uses total area L, not an undefined T. The numerical example, SI derivation and implementation now use the same notation; numerical CSV values are unchanged.
- The worked 0.7 ha reporting-cut illustration is retained in main and SI.
- Policy exposition retains the rate-law floor guarantee, distinguishes area constraints, and explains the difference between a safe constant stop and a provision objective without discussing old drafting errors.
- SI explains continuous-time quadrature versus a telescoping discrete identity. It retains scientific numerical diagnostics without production history.
- Terminology-related grammatical/duplication regressions and the stale simulator invocation are corrected.
- The previously unresolved population-refinement discrepancy is reconciled for the explicitly stated fixed-demand case with P0 = 1.5: maximum differences are 0.000244933842 and 0.000114441482 persons, displayed as 0.000245 and 0.000114 rather than 0.000252 and 0.000118. The exact quality-contact interpolation error at dt = 0.0125 is rounded to 8.9e-6 rather than truncated to 8.8e-6. These are numerical-reporting corrections; the model trajectory/budget CSVs are unchanged. A dedicated verification script and metadata record reproduce them.
- The selected projected model, scoped equilibrium/stability results, corrected recovery/debt comparisons, sharp bounds and contribution budgets remain. No new delay/history experiment or empirical analysis was added.

## Kept outside journal prose

Implementation origin, figure recovery, assistant checking scope, source hashes, compilation status and revision comparisons remain in supporting documentation. No production-history footnote or revision-status box has been added to the article.

## Author-controlled disclosure

The quoted original declaration has been restored rather than replaced with another statement on the author's behalf. Arena.ai assistance with the later derivation/code/manuscript work is documented in the external research record. The author should determine any accurate additional disclosure required for the final submission; no new author review or approval is asserted by this record.

The accompanying source patch files show the exact main/SI changes relative to C14. Integrity, transcription, numerical and compilation checks are separately scoped; none certifies every scientific claim or constitutes journal acceptance.

# C12 → C13 change log

**Working revision: 29 October 2026. Scope: user-selected M1 + M2 only.**

## Baseline and preservation

- Derived from exact C12 main/SI sources at commit `65c8464a3cf83d9aef525cb6695668898de18ac6`, working branch `arena/6dc29c9a-general-sustainability`.
- No earlier/submitted source is overwritten. No working branch is merged.
- Two unified patches identify the exact text changes. Provenance records original source hashes and Git blob IDs.

## Main manuscript

1. Mark C13 explicitly as an AI-assisted working revision requiring author verification before submission.
2. Extend abstract and core contribution wording to mention the new quantitative bounds and computed budgets.
3. Add Section 3.5 / Proposition 4 / equations (20)–(21): exact static identification intervals under independent yield/area restrictions; add a nested-observation numerical example and Table 3.
4. Add Section 3.6 / equation (22): full five-channel identity with restoration and varying fast yield; report genuinely integrated F100/R400 budgets in Table 4 and numerical closure errors.
5. Link methods and recovery text to the independent reconstruction and refined R400 values. Retain the earlier recovery values with their stated 0.1 yr step; do not disguise refinement differences as a new intervention.
6. Update conclusions with the bounded identification and budget results and their limits.
7. Replace prospective GitHub/Zenodo deposition wording with the supplied package's actual availability and explicit inherited-analysis limitations. Do not claim a Zenodo deposit or unperformed author approval.
8. Original equations (1)–(19), Propositions 1–3, figures and earlier references retain their numbers. Later result subsections move from 3.5/3.6 to 3.7/3.8; the two later original tables move from 3/4 to 5/6. References are recompiled, not hand-renumbered.

## Supplementary Information

1. Add C13 date/scope note; preserve S1–S8 and all 45 preexisting SI label numbers.
2. Add S9 with a full static feasibility proof, endpoint constructions/witnesses, non-injective quality-readout qualification, and joint-uncertainty caveat. Table S14 gives witnesses.
3. Add S10 with the exact selected case definitions, C12-compatible time/history convention, independent quadrature, fast-yield split, all seven refinement levels, closure and bounded-state diagnostics. Tables S15–S17 give budgets, fast-yield subterms and refinement.
4. Clarify the inherited recovery table's 0.1 yr step and distinguish its printed values from the refined R400 result.
5. Supply a freshly rendered version of the existing S8 wave illustration, using its stated 0.05 yr step, matching both printed six-decimal debt peaks and peak times. This is not M3 and is not a new delay experiment.

## Code, outputs, and build

- Supply `compute_c13.py`, `verify_c13.py`, `build.sh`, requirements, CSV/JSON outputs, six generated TeX row fragments, all eight figure dependencies, both compiled PDFs, provenance, validation report and manifest.
- Run seven timesteps on four existing cases: 28 integrations. Recompute all 28 in memory with `verify_c13.py --full`; all recorded scalar outputs agree within the verification tolerance.
- Do not force closure. At the finest step the largest relative discrepancy is 0.0628%, below the chosen 0.1% closure check. Publish every refinement level, including the initial ladder that did not meet the tolerance in two cases.
- Resolve seven inherited figure dependencies with exact origin metadata; they are not represented as newly regenerated or comprehensively revalidated. Only the existing wave figure is freshly rendered.
- Compile complete main/SI PDFs and compare auxiliary labels to separately compiled, unchanged C12 sources. Final build: no unresolved citations/references, no missing figures, and no overfull boxes. Four inherited nonfatal author-metadata warnings remain in the main build.

## Explicitly not done

- No M3 delay/history experiment, no new controller, no parameter/history robustness claim.
- No new empirical proxy or global physical-stock result, calibration, or empirical causal attribution.
- No exhaustive rerun of the inherited NFA/OWID work, parameter grids, comparator, or other restoration scenarios.
- No alteration to the user’s separate submitted v76 Figure 2 labels; that standing task is outside this C12-derived revision.
- No journal submission, author approval, branch merge, destructive overwrite, or force push.

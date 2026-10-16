# Paper10b v2 lineage, source-location, and scope audit (2026-10-16)

## Version lineage

The all-branch/tag scan found Paper10b v1 as the latest edition at `arena agent 1/agent workspace/papers/paper10b_edwards_aquifer_v1.tex`; no Paper10b v2 existed. A same-study renamed lineage is present as `paperE4_edwards_intervention_v16.tex` in `arena agent 1/paper rewrites/latex/` (also carried on the `lean-audit-v4` line). The E4 v16 and Paper10b v1 have the same title, abstract, and substantive model/results body. A line-level comparison gives 0.9452 similarity: Paper10b v1 is the later split edition and adds the related-work section and verified bibliography records absent from E4 v16. V2 is therefore based on v1, while preserving v1 and the E4 lineage unchanged.

## Analysis-source locations

The Paper10b paper directory does not contain a dedicated `push_src` bundle. The analysis record is stored elsewhere on the same branch:

- `arena agent 1/agent workspace/comp/wave_e_edwards/protocol_intervention.md` — dated frozen protocol;
- `arena agent 1/agent workspace/comp/wave_e_edwards/src/run_intervention.py` and `run_intervention_v2.py` — intervention analyses;
- `arena agent 1/agent workspace/comp/wave_e_edwards/src/e4_audit_layer.py` and `results/e4_audit_layer.json` — audit layer and output;
- `arena agent 1/agent workspace/comp/wave_e_edwards/data/` — annual panel and source extracts (including J-17, EAA discharge, and USGS recharge inputs);
- `arena agent 1/paper rewrites/latex/paperE4_edwards_intervention_v16_verification.py` — paper-specific verification runner.

A copy of the wave-E Edwards sources is also present under the Paper09 v44 source archive. The cited root `comp/wave_e_edwards/` paths are the direct working package; the Paper10b v2 audit does not claim that the article-specific paper folder itself contains the complete code/data package.

## V2 changes

- Replaces the stale “under separate review / in review” status of the J-17 forecast companion with its published Zenodo citation (record `22552680`); disambiguates the two 2026 Abaee references as 2026a/2026b.
- Reclassifies the 7.55-ft result based on realized annual fluxes as a conditional diagnostic, not a forecast, and distinguishes it from the persistence and AR(1) one-year forecast RMSEs.
- Keeps the 660-ft level's institutional relevance but states that the evaluated policy is an annual-mean 20%-at-660 sketch, not the operational 10-day CPM algorithm. The no-invariance result is bounded to the fitted one-pool map and persistent drought-of-record floor; no live-rule or springflow effect is inferred.
- Revises the abstract, impact statement, practical reading, and conclusion to preserve the nominal/hybrid status of the 618-ft supply margins and avoid reading the 660-ft model result as a field-policy verdict.
- No numerical result was re-estimated; v1's related-work additions and substantive results are retained.

## Verification/build

- Static checks pass: single document skeleton, balanced environments/braces, 18 unique labels, resolved explicit references, balanced inline/display delimiters, and paired dollar delimiters.
- No TeX engine is installed in this workspace; no compiled v2 PDF is claimed.
- Intended destination: branch `e2-v3-source-year`, `arena agent 1/agent workspace/papers/paper10b_edwards_aquifer_v2.tex`.

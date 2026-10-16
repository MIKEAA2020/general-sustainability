# Paper10 v54 lineage and build audit (2026-10-16)

## Version lineage

A fresh scan of all six repository branches and both tags found Paper10 v53 as the latest edition on `e2-v3-source-year`; no v54 existed on any scanned ref. The local v53 main source and supplementary source matched their remote blobs exactly before revision. The repository v53 main-file header incorrectly labeled itself `v52 (2026-09-30)` even though its path and companion SI identify the later edition. V53 and its SI are preserved unchanged. V54 is a new sibling version on the same branch and in the same papers directory.

## Scientific changes in v54

- Reframes depletion arithmetic around four non-interchangeable constructions: static reserve/production quotients; reference-period anomaly-trend extrapolations; frozen-rate local ratios; and model-conditioned barrier-hitting times. Gross-turnover and removals-only pressure scales remain separate rate-based diagnostics.
- Corrects the G3P interpretation: it is a gridded, reference-period groundwater-storage anomaly product, not absolute aquifer volume and not an index-well measurement. Removes the false implication that it measures storage at a well.
- Refreshes phosphate examples to the USGS MCS 2026 vintage. In thousand metric tons of marketable product, estimated 2025 world production is 250,000 kt/yr and reported world reserves are 73,000,000 kt; the quotient is 292 years. The U.S. snapshot is 1,000,000/20,000 = 50 years. Australia is shown under both MCS table reserves (5,800,000 kt) and the JORC/equivalent footnote basis (120,000 kt), rather than silently reconciling them. The world-resource threshold calculation is kept distinct from R/P.
- Corrects Proposition 28's crossover from a small-growth approximation incorrectly applied at `g tau = 8.76` to the exact threshold `eta_c = 1 - x/(exp(x)-1)`. With the 292-year snapshot used only as a scale input and illustrative `g=0.03/yr`, the threshold is 0.998625; these parameters are not estimated and the calculation is not a forecast.
- Corrects the monotonicity inequality in the proof of Proposition 26. The prior text had the conclusion in the right direction but reversed the intermediate inequality.
- Preserves the superseded U.S. historical-reserve sentence in the SI as an explicitly non-current, unaudited draft-era note; v54 does not rely on that longitudinal claim.

## Verification and build status

- Static checks pass for one document structure, balanced environments/braces, unique labels, balanced inline/display delimiters, and paired dollar delimiters in both v54 TeX sources.
- `verify_mcs2026_snapshot.py` runs successfully and reproduces the displayed R/P values, resource-threshold lower bound, and exact illustrative crossover table.
- No TeX engine is installed in the workspace; no compiled v54 PDF is claimed.
- Intended branch/path: `e2-v3-source-year`, `arena agent 1/agent workspace/papers/`; source package: `paper10_depletion_ledgers_v54_src/`.

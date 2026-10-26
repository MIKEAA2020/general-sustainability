# Paper06 v71 → v72 audit and change log

**Revision date:** 2026-10-26

**Disposition:** new derivative only; Paper06 v71 remains unchanged.

**Authorized title:** “Transition Certification with Composite Indices: The Acceptance Gap Between Compensatory and Noncompensatory Rules.”

## Changes made in v72

- Replaced the title with the authorized title and shortened the abstract. The full abstract and all keywords now fit on page 1; page 2 begins the Introduction. The earlier v71 page-2 text was the abstract continuing, not a duplicate Introduction.
- Made the Protocol 3/Protocol 4 relationship explicit in §1.2 and Table 1: common-plan robustness and typed acceptance have the same accepted-plan/state sets on the full cone by Proposition 1(ii). The paper's separation is Protocol 2 against either equivalent formulation.
- Reworded Table 1's weight-adaptive row so that `a_w` is plainly the plan selected for weight `w`; clarified the caption without duplicating the table.
- Clarified the sum/mean convention: for normalized equal weights, the floor-margin mean is `w·s = (s₁+s₂)/2`; the fishery dashboard reports twice that value, `s₁+s₂`, at the correspondingly scaled zero threshold. The floor-shifted equal-weight index is `(λ₁+λ₂)/2 = 1+(s₁+s₂)/2` at threshold 1. These are equivalent verdicts, not conflicting calculations.
- Reframed the DFO Northern-cod figures as a limited scale/context anchor only. The manuscript now distinguishes the exact-rational illustrative datum from empirical calibration, fit, forecast, validation, and performance claims; data-availability wording no longer says that no published data were consulted. Defined **kilotonnes (kt)** at first use in both the main article and SI.
- Clarified Table 6's monotonicity statement: restricting the weight family can only expand `V_W`; `V_typ` is unchanged, so their difference can only expand.
- Expanded the finite-menu proof's separator explanation: a negative coordinate would make the separating right-hand side unbounded below along the positive-cone direction, contradicting strict separation. No theorem or numerical result changed.
- Labeled NO-SWITCH as the status-quo/non-transition baseline: it keeps `q=0`, misses destination set `G`, and remains in the four-action menu to make that failure explicit.
- Replaced “even the index fails” with “even the aggregate rejects” in the region table.
- Scoped every positive-elasticity CES interval claim to the witness-defined **diagonal gap slice**, as Theorem 4(iii) requires. Updated the abstract, contributions, related-work claim, theorem wording, and conclusion. The exact 1/2-cut shared-shock result is now explicitly distinguished from the replace reading with identical plan- and weight-independent dips, under which the typed/weak distinction collapses (SI S4).
- Corrected the ECOMOD companion reference to the exact c10 title and pinned source/PDF at commit `6f626ee48b2a3a59282b5df5adda76c8d5993fdc`. Verified source and PDF titles match: **“A rising biocapacity total can mask ecological-capital land drawdown: a two-land model.”**
- Version-pinned the code references to Figshare `10.6084/m9.figshare.33764023.v3` and the SafeTransition software release `10.6084/m9.figshare.33971389.v1`; stated which artifacts those records actually contain. Pinned the Lean formalization link to the exact repository commit and file.
- Updated the SI title and edition map to v72.

## Audit disposition by claim

| Audit item | Independent source check | v72 disposition |
|---|---|---|
| Alleged duplicate Introduction header / stray paragraph | `00_front.tex` contains one `\section{Introduction}`. The v71 PDF's page 2 continued the abstract; it did not contain a second Introduction header. | **Not applied as alleged.** Abstract shortened to end on page 1. |
| Alleged duplicate or raw Table 1 | Source contains one `tabularx` for Table 1. Extraction/layout artifacts did not correspond to a second source table or a malformed source row. | **Not applied as alleged.** Caption and weight-adaptive row clarified; no duplicate table added or removed. |
| Protocols 3 and 4 / §1.2 | Proposition 1(ii) establishes equivalence on the full cone; v71 caption already said they coincide, while the surrounding prose described Protocol 2 against Protocol 4 only. | **Applied.** The full-cone equivalence and comparison are explicit. |
| Sum versus mean | Main text used the floor-shifted mean `(1/5+11/5)/2=6/5` at threshold 1; the benchmark/SI used the unshifted sum `s₁+s₂` at threshold 0. | **Applied.** The shift, factor of two, and equivalent thresholds are stated. |
| Fishery “no empirical claim” / availability statements | Main and SI quote published DFO LRP/biomass values as scale context while describing the witness as exact-rational and unfit. | **Applied.** Anchor-only role and no-fit/no-forecast/no-validation scope are explicit. |
| Table 6 weight-family row | Proposition 2 implies `V_W` can only expand when `W` is restricted; `V_typ` does not depend on `W`. | **Applied.** The table states both monotonicities and their effect on the difference. |
| Theorem 1 separator detail | Existing strict-separation inequality was correct; its implication `w ≥ 0` was compressed. | **Applied.** Added the contradiction along a positive-cone coordinate. |
| NO-SWITCH role | The table already states its successor misses `G`; the source did not label its status-quo role in the lead-in. | **Applied.** Labeled as the status-quo/non-transition baseline while retaining it in the menu. |
| “Even the index fails” phrasing | The row tests the aggregate condition `s₁+s₂<2`. | **Applied.** Changed to “even the aggregate rejects.” |
| Common shock versus replace reading | Main text already states the replace-reading collapse in SI S4, but the abstract and summary of the CES/common-shock results did not carry the qualification. | **Applied.** The surviving shared-shock result and the distinct replace-reading collapse are separated. |
| First use of `kt` | `kt` appeared in both main and SI benchmark sections before definition. | **Applied.** First use now expands “kilotonnes (kt).” |
| Citation / commit specificity | The c10 source and PDF at the pinned commit carry the title cited here; v71's ECOMOD entry had an older title and a generic repository link. | **Applied.** Exact c10 PDF and TeX links now point to commit `6f626ee…`; DOI records use versioned DOIs. |
| Formula and notation | Source formula `σ=1/(1−θ)` is correct. `a_w` denotes a plan selected for a given weight. | **Formula retained.** No notation/math change; the Table 1 prose now states the meaning of `a_w`. |
| CES scope | The exact interval in Theorem 4(iii) is on the witness-defined diagonal gap slice, not a claim that the same exact interval holds everywhere off-diagonal. | **Applied.** All summary claims state this scope. |
| Empirical limitations | The DFO figures are published scale/context inputs; no model parameter is estimated from them. | **Applied.** Limitations and declarations say so directly. |

## Figshare/DOI artifact inspection and residual availability limit

The related-deposit check is **not** an exhaustive proof that no other DOI exists. The two inspected records do not contain the exact Paper06 v71 PDF (and neither claims the new v72 PDF):

1. **Figshare `10.6084/m9.figshare.33764023.v3`.** The API lists `paper1_figshare_deposit.zip` (425,911 bytes; MD5 `31406e8d5094d3b26d1fafa963061bee`) and `paper1_figshare.zip` (1,654,504 bytes; MD5 `4a793787238bcc358ce0cb8a8b19bfa0`). The latter contains `paper1_assessment_separation_v42.pdf` and `.tex`; the former contains the 25-check exact-integer verifier/results/report, three figure scripts and their figures, and preserved novelty searches. It is an earlier Paper1 edition in the same research line, not the exact Paper06 v71 PDF.
2. **Figshare `10.6084/m9.figshare.33971389.v1`.** The verification ZIP downloaded from Figshare matches the API MD5 `d37134984105f6c97f7dadc223871faa` (3,295,590 bytes; SHA-256 `c9efc4b9565c1ffdbc1ec66eda87f6c7b8d1bcfe8c9b39acc6243a22facc9ddb`). It contains the SafeTransition 1.3.0 software/tests/benchmark artifacts, `paper1_safetransition_master_v4.pdf/.tex`, and Paper1 verification material; it contains no Paper06 v71 PDF or source.

The ladder, off-diagonal, continuum, and common-shock script/log files described in SI S7 were not present in those two DOI packages or in the inspected v71 source bundle. v72 records that availability limit rather than describing those check lists as reproducible from the inspected deposits alone. The grid and benchmark artifacts, the Lean source, and the exact manuscripts are separately identified.

## Verified c10 pin (read-only inspection)

- Commit: `6f626ee48b2a3a59282b5df5adda76c8d5993fdc`
- Main source: `agent 2 productivity illusion/output_v45_ecomod_continued_10_gemini38_v4base_si_review_20261026/ecomod_continued_10.tex` — blob SHA `7640f70e1b15a7f8a0e8675781b74c2303178d42`.
- Main PDF: same directory, `ecomod_continued_10.pdf` — blob SHA `7dc17580aca353a136b799ea45b014e77b77d827`; downloaded PDF title agrees with source title.
- ECOMOD c10, its pins, c8/c9, `main`, checksums, and DOI deposits were **not modified**. The existing cross-companion mapping is left intact.

## Build and integrity checks

- Built with Tectonic 0.17.0 from the assembled TeX and editable parts. Main PDF: **48 pages**; SI PDF: **40 pages**. v71 rebuilt with the same engine measured 47/39 pages. This page-count difference is not treated as content loss; the edits are prose/source changes and the PDF text was inspected.
- The full abstract and keywords are on page 1; the main PDF has one Introduction heading. No unresolved citation/reference warnings or `??` markers were found.
- The overfull-box warnings match the same-engine v71 baseline (main: 2.43 pt front-matter and 7.11 pt equation; SI: 2.43 pt front-matter and 1.73 pt existing paragraph). The build adds underfull-box warnings from revised prose but no new overfull box.
- Figures, figure scripts, model parameters, theorem formulas, and numerical results are unchanged. The source formula `σ=1/(1−θ)` is preserved. No DOI was created or refreshed, no checksum/package manifest was regenerated, and v71 was not overwritten.

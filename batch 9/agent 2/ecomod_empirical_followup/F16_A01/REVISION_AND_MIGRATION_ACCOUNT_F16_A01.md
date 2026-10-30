# Revision, migration and deletion account — F16_A01

## Parent and preservation

F16 is a new additive root built from published F15. Parent package commit: `b65d73674070208b5957a18f53dce8bc226b09fd`; parent receipt commit: `d42447586513c408fb8bb035d3743ec1bacb2c2b`. The parent receipt is vendored as `inputs/F15_PUBLICATION_RECEIPT.json`.

No F15 publisher or earlier publisher/verifier was rerun. F15 is protected by 70 path-level SHA-256 records in `metadata/protected_F15_identity.json`; 597 F11–F14 records are inherited in `metadata/protected_prior_identity_F15.json`. C17 and unrelated companions are untouched. No branch merge, force-push, overwrite or prior-path deletion is permitted.

## Additions

1. Added 21 annual Cameroon forest-area rows, 21 annual reported net-CO₂e-flux rows and Table 31/37 rounding checks.
2. Added Australian ABARES-adjusted annual area (1989–2021), separate NIR2021 stock/gain/loss rows (1989–2021), NIR2023 forest-land totals (1988–89 to 2022–23), NIR2023 clearing/regrowth (1989–90 to 2022–23), and Forests of Australia (2023) category/jurisdiction aggregates.
3. Added one three-panel main figure, three linked SI tables, five bibliography records, SI source attribution and explicit carry-forward/rounding protocols.
4. Added ten workbook sheets. The 31 F15 sheets and all 60,336 inherited cells are preserved in value.
5. Added source hashes, retrieval accounting, tests, QA, reproduction and verification code.

## Editorial changes and compression disclosure

- Main figures: 6 → 7. Main tables remain 2. SI tables: 25 → 28; SI figures remain 2.
- Main pages: 16 → 18. SI pages: 25 → 27.
- The abstract remains within the journal limit: 250 → 243 whitespace-delimited words. Its wording was compressed to admit the Cameroon/Australia results and carry-forward qualification. All inherited abstract conclusions—account counts, mapped declines, Indonesian cohort range, inventory qualifications, local map cancellation/allocation results, information narrowing and the eight incomplete calibrated AGB targets—remain. No result was removed.
- Cameroon and Australia's “No completed physical numerical module” cells were replaced by their new source-specific results. The separate statement that none completes calibrated national 2015–2023 forest-AGB analysis is retained.
- A hard-coded SI reference to “main Figure 5” was made semantic (“main endpoint-cohort figure”) because the new main figure shifts subsequent numbering.
- SI provider references received a page-break guard to prevent an orphaned `.pdf.` fragment. Cameroon/Australia source attribution was added. No specialist protocol was deleted.

## Rounding and source-fidelity decisions

- Cameroon class sums exceed reported totals by 1 ha in 2011, 2012, 2015, 2016 and 2019. Both classes and totals are retained.
- Four ABARES difference-from-2016 cells differ by 0.01 Mha from subtraction of displayed areas; six NIR2021 gain/loss identities have ±1 kha residuals; NIR2023 clearing identities have residuals within ±0.1 kha. Reported fields are not silently repaired.
- The exact ABARES attribute sum is 5,200 ha below the adjusted 2021 value when the latter is expressed as 133.57 Mha × 10⁶. They remain separate source representations.
- A blank-state group of 5,875 nonforest ha is retained and labelled `Unallocated`.

## Omissions and deletions

**No files were deleted and no inherited numerical result was omitted.** Provider PDFs, the 130,761,002-byte CRT ZIP and other raw source payloads were never included in the new package. The CRT central directory was read using four HTTP-range requests totalling 6,160 bytes. Selective member extraction was not performed because the required annual physical values were already available in the official NIR tables; this is a redundancy decision, not missing evidence. ABARES's original XLSX binary was not needed after all five public sheets were retrieved as a complete text extraction; the extraction hash and original URL are recorded.

Provider-held Cameroon workbooks/raw CEO/Monte-Carlo inputs remain necessary only for stronger independent reproduction and calibrated endpoint/uncertainty analyses. Their absence does not invalidate or pause the completed reported-aggregate module. No new calibrated AGB estimate, confidence interval, causal conversion association or reporting-accuracy claim was added.

# Claim-to-section crosswalk: Paper07 v52 main text vs historical Paper5 v19 supplement

- **Prepared:** 2026-10-16, follow-up retrieval review
- **Purpose:** map v52 main-text claims and SI pointers to the recovered old-numbered supplement `paper5_supplementary_v19_NatSustain.md` without relabeling that file as “Paper07 v52 SI.”
- **Review provenance:** incorporates the Task 127 retrieval finding relayed by the user; branch/blob identity and section correspondence were independently rechecked for this map.
- **Conclusion:** the section names, substantive contents, direct v52 pointers, and article title give strong evidence that v19 is a historical companion candidate. The available repository record does not bind this exact v19 file revision to the particular v52 main-source/PDF build; exact version attribution therefore remains unverified.

## Source identity and scope

The v52 main source is `arena agent 1/agent workspace/papers/paper07_sampled_governance_v52.tex` on `e2-v3-source-year` (Git blob `5e55af0f006eb28789ac29bc70bf000dcdf88843`, 141,759 bytes). The corresponding main PDF is 36 pages; it is the main article, not a verified complete article-plus-SI package.

The recovered historical supplement is `arena agent 1/paper rewrites/paper5_supplementary_v19_NatSustain.md`. It is present on both `main` (`217d110f006ec4b6b43755e53350d7043b0d1ddc`) and `e2-v3-source-year` (`9c86c7553b979abe8b00e1255dda2179cd517bd8`) under that path, with the same Git blob `607659d5ad60e17a3ccecdeffbe87aa60dda2719` (77,327 bytes; SHA-256 `fbfe648c7ed4d7c749463925d17b14812275d369a03db8e0f777ed08d3627d21`). The e2 branch also carries the same blob at `arena agent 1/agent workspace/content_audit/seeds/08sg19_paper5_supplementary_v19_NatSustain.md`.

Its front matter says it accompanies **“The decision clock: review intervals as a design lever for stable resource governance,”** the exact title of the v52 main source. It describes S1–S13 and contains S13.1–S13.3. This title and structure are strong linkage evidence, but the filename/version is v19 and no v52-specific checksum, manifest, deposit record, or source-to-PDF build record was found to establish that this precise revision was the SI attached to the v52 PDF.

## Claim-to-section map

Line numbers below refer to the tracked v52 TeX source identified above. “Strong content match” means the main-text pointer/claim and the v19 section topic align; it does **not** certify that v19 is the exact SI revision compiled with v52 or independently validate the scientific claim.

| v52 main-text claim or pointer | Corresponding section/content in historical v19 | Match assessment and limit |
|---|---|---|
| Statement inventory and evidential status (lines 33, 1477, 2061–2063) | S1, “Statement inventory” | Strong content match. The v19 inventory indexes the same main-text structure, including §§4.4–4.8. The match does not supply a version binding. |
| Remaining proofs and identification results; dimensionless-identifiability chart (closing inventory, lines 2062–2064); Appendix A fixed-point row explicitly points to the closed form in S2.3 (line 1773) | S2.1–S2.3, especially S2.3, “The dimensionless identifiability chart” and Theorem S2.3 | Strong, direct match. The v19 theorem gives the dimensionless groups and the baseline fixed point `(89.55188, δ, 2.08962)` also reported in v52. The v19 text identifies the chart as a companion-delay-study record (Abaee, 2026, §9.5) and explains why it is proved in this supplement; that origin note is compatible with, but does not prove, the exact v52 attachment. The chart content is recovered; it is not an unrecovered item. |
| Epistemic-layer results (closing inventory, lines 2064–2065) | S3.1–S3.8, including observation-fibre certification, information monotonicity, hidden-mode conflict, and delayed-information obstruction | Inventory-level and topic match. The v52 closing inventory names S3; no distinct in-body pointer to every S3 result was required for this map. Exact edition pairing remains unverified. |
| Case-screening records and query log (lines 554, 1358–1378) | S4, “Case-screening records at full detail” | Strong, direct match: the v52 case-search and named-system discussion points to S4; v19 S4 supplies the detailed case records. |
| Ecosystem context and toy tests (line 1466; closing inventory line 2065) | S5, “Ecosystem context and toy tests” | Strong, direct match for the background-only ecosystem record and toy simulations. |
| Distributive-layer detail and community-level measures (lines 1614, 1917; closing inventory line 2066) | S6, “Distributive-layer detail” | Strong, direct match for constituency, measured floors, instruments, community-data limitations, and the anti-domination boundary. |
| Empirical hypotheses with specified tests (closing inventory lines 2066–2067; main-text prospective/falsification discussion) | S7, “Empirical hypotheses with declared tests” | Strong structural/topic match. V19 S7 records the declared hypotheses and their tests; it does not turn prospective tests into executed results. |
| Reproducibility register and discharge status (line 1724; closing inventory line 2067) | S8, “Reproducibility register” | Strong, direct match for the archive-status and execution records. |
| Screen-sensitivity battery and stage-scan decomposition (lines 509, 849, 1627; closing inventory lines 2068–2069) | S9.1 screen-sensitivity battery; S9.2 stage-scan decomposition tables | Strong, direct numbering and content match. |
| `T_r`-ranked cross-sectional test (line 1588; closing inventory line 2069) | S10, `T_r`-ranked cross-sectional test | Strong, direct numbering and content match. |
| Crossing sensitivity, equilibrium-`F` grid, Neimark–Sacker record, alternative bands, and cod periodogram (lines 1187–1191, 1320, 1581, 1727, 1778–1780) | S11.1–S11.5 | Strong, direct topical match. This map records where v52 points; it does not validate the historical computations or restore v52 claims later qualified in v53/v54. |
| F-calibration/placement, ADH cross-system result, and precision certificate (lines 1189, 1320, 1492; Table 3 note at line 1782) | S12.1–S12.4, including the fifty-digit precision certificate in S12.4 | Strong content match. There is a pointer ambiguity in the v52 Table 3 row at line 1782: the row text calls the certificate “(S12)” but its final-column pointer says “Supplementary S11.” The v19 section structure places the precision certificate in S12.4. This supports a likely correction, not proof of which numbered revision accompanied v52. |
| Power-grid configuration, cod crash-window ledger detail, and prospective-design specifications (lines 518, 1404, 1348, 1592–1601) | S13.1–S13.3 | Strong, direct match for each of the three in-body pointers. The v52 closing inventory does not mention S11–S13.3, but its body does; v19 contains those sections. |

## What this establishes—and what it does not

- **Recovered:** a historical supplement with the exact v52 article title in its front matter; the v52-referenced section structure S1–S13.3; and the named dimensionless-identifiability chart in v19 S2.3.
- **Strongly supported:** the v19 document is a content-matched historical companion candidate for the v52 main article. The discrepancy is that the v52 closing inventory stops at S10 while the body cites S11–S13.3; that omission in the inventory is not evidence that those sections were absent.
- **Still unverified:** whether this exact v19 file revision was the supplement compiled/deposited with the specific v52 main PDF. No version-bound package, checksum, or deposit record connecting the v19 blob to that v52 build was located. Therefore do not rename, label, or describe v19 as the verified “Paper07 v52 SI.”
- **Not a substitute:** v53/v54’s joint-box sensitivity figure is not the S2.3 identifiability chart. The chart itself is present in the historical v19 candidate; the separate question is version attribution.
- **Separate current deliverable:** v54’s 29-page, 14-section SI is a reconstructed Supplementary Information for v54. Its completeness as a v54 package does not retroactively establish which historical SI revision accompanied v52.

## Paper08 lineage cross-check

The e2 branch also contains `arena agent 1/agent workspace/papers/paper08_governance_delay_v48_supplementary_governance.md` (Git blob `70f8f78b384b6059b0c89531c81ed270dbdc5c0e`, 77,351 bytes; SHA-256 `fd6854e66ae0d6b8e77f7c9a5c22634243d1136321b1d2a42a3c823a504871a3`). Its S2.3 block is text-identical to v19 S2.3. The Paper08 version changes the accompanying-title line, the introductory S13 description, and the S11.1 section reference (`§3.4` to `§3.4.1`). This corroborates a shared historical content lineage, but the Paper08 title and those edits mean it is not evidence that v48—or v19—was the exact v52 SI build.

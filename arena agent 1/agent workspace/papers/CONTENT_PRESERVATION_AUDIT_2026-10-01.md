# Content preservation audit — all 15 live papers and their source lineages

**Date:** 2026-10-01. **Status: audit, not a repair. No manuscript or merge script was changed, and nothing from this audit was pushed.**

## Executive finding

The earlier blanket assertion that the mergers/splits preserved *everything* is **false**. The main mathematical/prose bodies are largely carried through, but that statement concealed lost **post-reference material** and bibliographic damage. A structural gate and the report-only tail detector both currently say 0 on live heads; neither tests for a missing References heading, an absent Declarations block, a cited source missing from the bibliography, or the loss of one source's data/code disclosures.

**Confirmed and actionable:**

1. **Paper05 v16:** the entire unit-5 Declarations block vanished (funding, competing interests, data, code/verification-script provenance, AI declaration); a cited Chatterjee–Doyen–Henzinger 2009 reference vanished; Stanley 2013 lost chapter/link and Lovejoy 1991 lost venue/volume/pages.
2. **Paper06 v67:** its Supplementary Material pointer and *entire* Declarations block vanished despite the actual supplement existing. The bibliography lost the **whole title/journal/pages** of Dasgupta–Mäler 2000 and at least nine publisher/location/page tails. The omitted data statement explicitly distinguishes this paper's **25** verifier checks and SafeTransition's separate **24**, and names the figshare data/code deposit; the 25-vs-24 distinction also survives elsewhere in the body. Do not copy the authorship assertion back automatically: owner review is required.
3. **Paper11 v64:** the Edwards source's ~498-word declaration (data provenance, nClimDiv reproducibility caveat, two independent uncertainty implementations, scripts, verification) was **not merged**; only the cod declaration was appended. About **422 contiguous words** from the Edwards declaration are absent even from the merged declaration; some general provenance appears elsewhere, but the detailed caveats and filenames do not. The Edwards standalone paper still has them. The `White (2000)` entry is stranded **after** the AI declaration rather than in References.
4. **Paper01 v63:** the `References` *heading* was lost on split, leaving `\label{references}` and roughly 66 bibliography paragraphs as unheaded text after the conclusion. Many entries are fragments or misordered; `Nagumo (1942)`'s journal/year/pages and `Prajna–Jadbabaie (2004)`'s LNCS pages are physically detached from their heads, though the text still exists. The older v61 already had some fragmentation; the v62 merger added more and the v63 splitter removed the heading. The reference-based gate sees **no reference block at all** in v63. Also the source's explicit author block was not carried into the merged/split article; do not populate a new byline without owner approval.
5. **Paper07 v50 / paper08 v46:** redactions persist even though an earlier **unblinded** `paper5_sampled_governance_v46_NatSustain.tex` exists in the repository. Paper07 still has `\author{Anonymous}` and 22 blinding/anonymization matches; paper08 inherited 17 (in-text citations, table provenance `@ [blinded]`, and `Author. 2026. [Blinded for review.]` in References). These are lost attribution and reproducibility details, not evidence that a cited work never existed. The v46→v47 diff identifies the source citation, actual reference and revision hash `24c980cd` without inference. Whether to publish any personal identity or to apply old contributions to a **new merged work** remains an owner decision.
6. **Paper11c v2:** `Saint-Pierre (1994)` is cited in the prior-art text but its bibliography entry sits *after* the AI declaration rather than under References. Its text exists; this is displacement, not deletion.

**Other structural risk:** paper08 v46 has three active `\maketitle` calls; paper09 v32 has two; paper11 v64 has three `\title`, two `\author`, three `\maketitle` calls. The source abstracts were retained, which is good, but repeated title blocks are not an integrated article. Paper01/05/08/09 merged heads have zero active `\author` at the front; papers 01/05/08/09 do have explicit author information in their **earlier seed**, which corrects the earlier claim that no manuscript asserted any name form. A seed's name is evidence, **not** permission to invent contributions or assume the chosen byline for the merged work.

## Scope and method — what was actually checked

- Enumerated all **15** current `.tex` heads (paper01–11 including 09b, 10b, 11b, 11c) and all **five** accompanying supplement files (paper01, paper06, paper08 ×2, paper10).
- Downloaded and SHA/byte-verified **22** documented seeds / supplement ancestors from the repository tree of branch `e2-v3-source-year`; tree was **not truncated**. An additional explicitly **unblinded** paper07 ancestor (v46) was checked separately. Sources, hashes and local copies: `../content_audit/seed_manifest.json`, `../content_audit/seeds/`. Corrected one near-miss before drawing a conclusion: `paper1_safetransition_ems_supplementary_v7.md` was the **wrong lineage** for paper06; the actual ancestor is `paper1_supplementary_v12.md` (36,553 bytes). The wrong-seed 0.18% comparison was discarded.
- Performed **39** reproducible comparisons: each head against its documented seed and immediate pre-merge/pre-split predecessor(s), plus supplement ancestors. `../content_audit/scan_content.py` uses normalized eight-word windows over comment-stripped text **before References** (label/citation IDs normalized), and independently compares heading names, labels, figures and formal-environment counts. Raw evidence: `../content_audit/comparisons.json`, `../content_audit/summary.txt`. A match only establishes near-verbatim carry-over; it cannot establish claim correctness or detect every short changed phrase.
- Conducted **a separate back-matter audit**, because the body scan intentionally stops at References: `../content_audit/backmatter_scan.py` and `../content_audit/backmatter_comparisons.json` compare Declarations word sequences. Inspected every paper's post-reference headings; paper05 and 06 have **none** despite both predecessors having substantive sections; paper11's Edwards source declaration is omitted.
- Conducted **a separate reference audit** (`../content_audit/ref_scan.py`, `../content_audit/ref_comparisons.json`), including fallback to `\label{references}` when a heading is missing; manually checked low-similarity matches against literal article text to discard false positives. The matcher initially miscalled several paper08 and paper11 sources as missing because a source entry was glued or a citation style changed; direct searches show those works present. Do not use the raw suspect count as a defect count.
- Compared the repo's unblinded sampled-governance v46 to blinded v47 **line by line**. No seed identity or CRediT roles were inferred from a git account.
- **Named-check cross-check:** `phase0_scan.py --gate` → `LIVE HEADS failing: 0 file(s), 0 finding(s)`; `scan_continuations.py --live-only` → `ON LIVE HEADS: 0 candidate fragment(s)`. Both are true for their named checks and plainly **not** a content-preservation verdict. The gate misses paper01 because it requires an exact `References` heading; it misses full-section omissions everywhere.

### Body-only coverage by seed (8-word windows, *not* a completeness percentage)

| Live head | Documented seed | Body 8-gram match | Reading verdict on long-form body |
|---|---|---:|---|
| paper01 v63 | `obstr_v57` | 99.78% | Main body carried; front author and reference heading not preserved |
| paper02 v12 | `probabilistic_sufficiency_v14` | 100.00% | No long-body omission found |
| paper03 v16 | `computational_certification_v20` | 99.31% | No long-body omission found; source-v14 → v16 99.95% |
| paper04 v16 | `minimax_v11` | 100.00% | No long-body omission found |
| paper05 v16 | `exact_belief_computation_v13` | 97.10% | Enlargement/reworked conclusion, not evidence of loss; **back matter and refs lost** |
| paper06 v67 | `assessment_separation_v63` | 99.96% | Main body carried; **post-reference loss** |
| paper07 v50 | `p5_v47` | 99.89% | Body carried *from blinded seed*; unblinded v46 proves attribution loss |
| paper08 v46 | `p4_v41` | 98.24% | 6.5-year false-robustness claim corrected, source body substantially retained; **masked sampled-source facts** |
| paper09 v32 | `E2_cod_intervention_v29` | 99.60% | All three merge inputs independently 99.5%+; duplicated front matter |
| paper09b v2 | `applied_regime_viability_v9` | 99.81% | No long-body omission found |
| paper10 v53 | `material_ledgers_v50` | 99.94% | No long-body omission found; original uses `\section*{Abstract}`, not `abstract` env |
| paper10b v1 | `E4_edwards_intervention_v16` | 99.93% | No long-body omission found |
| paper11 v64 | `E1_cod_forecast_v60` | 99.90% | Main bodies retained; **Edwards declaration lost**, front matter triplicated |
| paper11b v2 | `E3_edwards_forecast_v17` | 99.07% | Short conclusion editing; no long-result loss found; declaration intact here |
| paper11c v2 | `ws_v17` | 99.89% | No long-body omission found; cited reference misplaced |

**Supplement ancestors:** paper01 99.94%; paper06 **99.60% against the correct `paper1_supplementary_v12`**; paper08 delay 99.55% against `paper4_supplementary_v8`; paper08 governance 99.80% against unblinded `paper5_supplementary_v19` (98.76% against blinded v20); paper10 LaTeX **100.00%** against `paper3_supplementary_v18.tex`. Residuals are primarily retitles and accompanying-metadata changes; the sections and labels were checked independently. The **paper06 supplement file exists**, but its main-paper pointer was lost.

## Evidence and provenance, by confirmed defect

| Priority | Live location | Earlier material / counterexample | What is missing or displaced | Likely producer |
|---|---|---|---|---|
| Critical | paper05 v16 after References (ends at `\end{document}`) | v14 **L835–end**, seed `paper2_exact_belief_computation_v13.tex` | All six declarations; v14 code availability names `paper2_exact_belief_computation_v13_verification.py`. Neither heading nor content survives. | `papers/split_parts.py`: `reference_block()` stops at `Declarations`, and `write()` never appends the declaration tail for Part I. |
| Critical | paper06 v67 after References | v65 **L3432** Supplementary Material; **L3436–end** Declarations | Supplement pointer to actual `paper06_..._supplementary.md` lineage; availability statement with figshare DOI `10.6084/m9.figshare.33764023`, separate 25-vs-24 check lists, funding/competing/AI statements. | Same `split_parts.py` extraction; it filters paragraphs that look like references and then stops before declarations. |
| High | paper11 v64 **L3793–end** | paper11b v2 **L1193–end** | Edwards-specific data and code provenance and reproducibility caveat absent from merged declarations; only cod source tail appended. | `p5/merge_11_11b.py` appends `decl_a` only; `decl_b` is read but not emitted. |
| High | paper01 v63 **L1912** | v61 **L1917** has `\subsection{References}` | Exact bibliography heading removed, 66 reference paragraphs rendered as untitled prose; gate sees no list. Earlier v61 had fragmented entries, but v62 created more. | `papers/split_paper01_unit1.py` slices at `\label{references}` and contains a no-op (`... if False else None`) where it claims to back up to the heading. |
| High | paper05 v16 **L679 citation; References L871–end** | v14 **L800–802** | Chatterjee, Doyen & Henzinger 2009 is cited in the body but not listed. Stanley v14 L812 lost chapter/link; Lovejoy v14 L832 lost journal/volume/pages. | `split_parts.reference_block()` selects fragments by paragraph-shape/year, not by work identity, then the merged output is split without a source-vs-head bibliography reconciliation. |
| High | paper06 v67 **L3345** | v65 **L3323** | Dasgupta & Mäler 2000 reduced to `Dasgupta, P., and Mäler, K.-G. (2000).`; title, journal and pages no longer appear anywhere in v67. | Same paragraph-shape extraction. |
| Medium | paper06 v67 References **L3284, L3468, L3508**, etc. | v65 corresponding entries | At least **nine** source tails dropped from matched references: Aubin 1991 publisher/location; DFO 2016 agency/place; Filippov 1988 publisher; Keeney–Raiffa 1976 publisher; Munda 2005 publisher and pp. 953–986; Nardo 2008 publisher; Roy 1996 publisher; Warga 1972 publisher; World Bank 2011 imprint. Scripted prefix-comparison and manual spot-check both agree. | Split/rebuild of fragmented reference block, not a decision to abbreviate each item. |
| Medium | paper07 v50 **L58 + refs**; paper08 v46 **L3827 etc., L5228–L5250, L5474** | Repo `paper5_sampled_governance_v46_NatSustain.tex` → blinded `p5_v47` | Source v46 has actual author, `Abaee, 2026` citations, bibliographic DOI `10.5281/zenodo.22554217`, and source revision `24c980cd`. Blinded v47 replaced those with `Anonymous`, `citation blinded for review`, `Author. 2026. [Blinded for review.]` and `@ [blinded]`. Current standalone and merge retain many redactions. | Version-choice/blinding inherited from seed; NOT created by the last repair. Owner must choose publication-safe restoration. |
| Medium | paper11 v64 **L3886**; paper11c v2 **L1419** | Body cites White 2000 / Saint-Pierre 1994 | Both full entries exist **after the final AI declaration**, not in the bibliography. They therefore evade reference-block-only checks. | Post-merge prior-art insertion at file tail; trace exact edit before changing. |

**Source vs merged-work authorship:** `paper01`, `paper05`, `paper08`, and `paper09` seeds explicitly have `\author{Amin Abaee...}`; their live merged heads do not. In paper01/05 this is removed when the source front matter is replaced; in paper08/09 when parts are assembled. paper06's documented seed has no active author. paper07's immediate seed is deliberately Anonymous, while its unblinded v46 ancestor names an author. This evidence corrects the old statement that no manuscript asserts a name form, **but it does not fill the CRediT template or establish the desired byline/contributions for a newly merged paper**. Ask the owner.

## By-paper disposition (15 of 15)

| Paper | Verdict from this audit |
|---|---|
| 01 | Main body present; **heading missing** and damaged/displaced references; source byline not carried. |
| 02 | Seed, previous version, references and declarations compared; no significant loss identified. |
| 03 | Same; no significant loss identified. |
| 04 | Same; a Sion journal abbreviation differs, same work, not a lost result. |
| 05 | **Declarations absent; Chatterjee reference absent; two other citations shortened.** |
| 06 | **Supplement pointer, declarations, a full citation title and nine tails absent.** |
| 07 | Body carried from blinded source, but **recoverable unblinded attribution** was not restored. Inherited Statistics Canada bibliography paragraph in v50 is glued to a Shertzer citation; the v46 merger repaired it, standalone did not. |
| 08 | Delay+sampled bodies and two actual supplement files retained. **Seventeen blinding matches persist**, and front matter repeats `\maketitle` three times. No claim that the supplements never existed survives this audit. |
| 09 | All three bodies and most per-system data/code prose carried; **two** active `\maketitle`s, four abstracts (the source abstracts were intentionally kept). CRediT template remains deliberately blank. |
| 09b | Seed, previous version, references and declarations compared; no significant loss identified. |
| 10 | Seed and previous version, body and supplement compared; no significant loss identified. |
| 10b | Seed, references, declarations checked; no significant loss identified. |
| 11 | Main bodies intact; **Edwards data/code disclosure dropped** from merged head. Three active title calls, two authors, three `\maketitle`s; White reference displaced below AI statement. |
| 11b | Self-contained standalone retains Edwards disclosure; no long-body omission identified. |
| 11c | Main body/declarations retained; Saint-Pierre citation displaced below AI statement. |

## Why the earlier checks said “clean”

- Gate `ref_block()` searches for a `\section{References}` or `\subsection{References}` heading. Paper01 v63 has only `\label{references}`, so **all reference checks become vacuous** there.
- Both the gate and the continuation detector test **fragment patterns**, not seed-to-output coverage; whole-section deletion leaves no fragment to flag. A citation shortened to `Dasgupta ... (2000).` is author+year and may pass a split-reference heuristic, but it is not a valid complete reference.
- Body-only n-grams were exceptionally high even on the worst affected paper: paper06 99.96%; paper05's *declarations* were outside the checked body. Publication/compile success is irrelevant to missing data-availability statements.
- `split_parts.py` calls a bibliography “shared” and filters paragraphs by shape; it does not conserve tail sections or reconcile source entries. Assertions based only on brace/label counts certify LaTeX structure, not preserved content.

## Repair protocol (not executed)

1. Review **one artifact at a time**, starting with paper05 v16, paper06 v67, paper11 v64, paper01 v63. For any future split/merge fix the **script** (`split_parts.py`, `split_paper01_unit1.py`, `merge_11_11b.py`) before regenerating; do not overwrite existing live heads. For terminal heads, make a *new* version or a tightly reviewed repair, with an explicit source→output content ledger and diff before any push.
2. Restore objectively documented non-personal back matter, citations and heading only from the correct source; **do not infer authorship or fill CRediT roles**. The paper06 source's `A.A. conceptualized...` and paper07 v46's contribution sentence require owner confirmation in the present merged context. Do not import a declaration from a different system as though it described the whole paper.
3. For paper07/08, use the unblinded v46→blinded v47 diff as the literal restoration map, then verify each citation/revision identifier against the actual matching file. The repository's existence is not a substitute for an actual deposited publication claim.
4. Add tests that reject a missing References heading, an empty or absent Declarations block when inputs have one, dropped supplement pointers, source references without retained title/venue/pages, and reference entries occurring **after** the final declaration. Exercise them on live heads and fresh merge output; separately keep reading plus report-only detectors. New rules must be measured report-only across the corpus before fatal promotion.
5. Re-run the named checks **and** a full source-versus-new-head back-matter/bibliography comparison after every repair. A 0 exit code alone cannot close this audit.

## Confidence and limits

**High confidence** in exact missing sections, missing headings, absent literal citation/reference fields, missing Edwards declaration and observed redaction diff; every cited source was retrieved or is a retained local predecessor. **No assertion of total semantic equivalence** for the remaining content: normalized 8-gram preservation can miss a short negation, altered number, a deleted line shorter than the run threshold, a paragraph rephrased to a different claim, or lost external computational artifacts. The 39 comparisons cover the **documented lineage** and five supplement files, not every file in the 7,291-entry repository tree or every historical draft. The `ref_scan` raw suspect pairs contain confirmed false positives from run-together old entries; conclusions here are **human-triaged**, not the raw algorithmic labels. Nothing was silently auto-merged, restored or pushed.

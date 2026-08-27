# Canonical Concordance A001–A025 — Coverage and Closure Status

- Schema: `TCS-1.0`
- Inventoried rows: **409** (407 at intake; +2 repair rows from the 2026-08-26 row-verification pass — see below)
- Sources represented: **25/25**
- Missing source inventories: `none`

## Rows by source

| Source | Rows |
|---|---:|
| A001 | 99 |
| A002 | 53 |
| A003 | 15 |
| A004 | 3 |
| A005 | 6 |
| A006 | 16 |
| A007 | 2 |
| A008 | 8 |
| A009 | 10 |
| A010 | 15 |
| A011 | 24 |
| A012 | 14 |
| A013 | 12 |
| A014 | 15 |
| A015 | 10 |
| A016 | 12 |
| A017 | 10 |
| A018 | 18 |
| A019 | 9 |
| A020 | 9 |
| A021 | 8 |
| A022 | 8 |
| A023 | 11 |
| A024 | 9 |
| A025 | 13 |

## Review state

| State | Rows |
|---|---:|
| `adjudicated_rejected_or_negative_only` | 28 |
| `row_verified` (A001 scientific pass, 2026-08-27) | 99 |
| `mapped_requires_final_citation_check` | 27 |
| `requires_row_level_verification` | 255 |

## Destination routing (Wave-0 completion pass, 2026-08-26)

All 409 rows now carry a `destination_paper` + `monograph_chapter` assignment. The 156 rows previously holding `manual destination review` were routed by content review against `revised_optimal_publication_architecture_A001_A025.md` (source→paper mapping), the PUBLICATION_STRATEGY session-additions table, and the routed-row precedents already present in this concordance. Row-level content verification (`requires_row_level_verification` / `proposed_not_yet_interface_proved`) is unchanged and remains pending — this pass assigns publication destinations only; it promotes no theorem status.

| Destination | Rows |
|---|---:|
| Paper 2 | 128 |
| Paper 5 | 56 |
| Paper 4 | 54 |
| Paper 3 | 54 |
| negative/counterexample register or conditional redesign docket | 43 |
| Paper 7 conditional | 20 |
| Paper 1 or monograph introduction | 18 |
| Paper 4 appendix or compendium | 13 |
| conditional docket (open problem) | 12 |
| Paper 6 conditional | 8 |
| Paper 1 if independent-result gate; otherwise Paper 2 | 3 |

Routing vocabulary note: this pass introduced one new `destination_paper` value — `conditional docket (open problem)` — for unproved conjectures, open research hypotheses, and unreproduced/pending-correction artifacts (A001 Conjectures 17.1/18.2; the A002 research-programme items; A014 open hypotheses and the unreproduced computational object; A016 pending-correction and unreproduced data pipelines). It is distinct from the negative/counterexample register: those rows record refuted or defective claims, not open ones.

## Row-level content verification — machine layer (2026-08-26)

Executed as `reaudit/verify_concordance_rows.py` (exit 0, 11/11 checks):

1. **Structure:** concordance_ids unique and well-formed; source_ids consistent with the inventory paths; zero unrouted rows.
2. **Quote verification:** every row's `source_item` is verifiably present in its source inventory (normalized 40-char prefix, with the item_type fallback for the intake's auto-generated `Untitled …` rows).
3. **Coverage at raw-entry level:** every inventory entry — counted BEFORE the intake builder's dedup-by-(type,title) — has a row. This check found **two silent intake collisions**, now repaired:
   - **A002:** the inventory carries two Remark rows with empty opening descriptions (`Typed conservation and physical admissibility`; `Substitution as pathway feasibility`); the intake dedup dropped the second. Restored as **CC-A002-053** (routed Paper 2 by the sibling-Remark precedent; CC-A002-009's notes now name its item).
   - **A025:** two items share the status text `Not obtained` (`Converged Moore–Spence zero`; `Fold certificate`); the Fold-certificate row was dropped. Restored as **CC-A025-013** (routed Paper 4 appendix or compendium per the A025 sibling rule; notes record the post-Task-31 rebuilt-nominal fold state — the certificate itself remains NOT OBTAINED).
4. **Vocabulary:** destinations, review states, primary mappings, and mapping statuses all come from the documented controlled sets.

Honest boundary: this is the **machine layer** (quotes, coverage, vocabulary). The scientific row-closure states are unchanged — 336 `requires_row_level_verification`, 45 `mapped_requires_final_citation_check` — and no theorem status is promoted. The pre-repair release snapshot (407 rows) remains the v1.0 record; historical references to 407 in frozen documents describe that snapshot correctly.

## Scientific row-closure — first complete source (A001, 2026-08-27)

Executed as `research_program/close_concordance_rows_A001.py` (decision table encoded in the script; full report `concordance_row_closure_A001.md`). The complete A001 source (`uploads/topdown.txt`) was read end to end; all 99 A001 rows — 81 `requires_row_level_verification` and 18 `mapped_requires_final_citation_check` — closed to `row_verified`: item existence + kind + proof presence verified in the source (the deferred line check); canonical module assigned or corrected; mapping type verified per TCS-1.0 §7; `mapping_status` → `accepted_mapping` **at the content level only** (no theorem status promoted; the §8 interface contract for cross-module transfer remains open in `interface_dependency`; the paper-time citation match rides the Part III paper-support discipline).

Findings of the pass (all repaired and machine-verified):

- **Five corrupted intake rows** (CC-A001-061..064, -088): the intake builder's naive pipe split turned the Theorems 11.1–11.4 and 16.1 rows into fragment garbage (`item_type='F_0\'`, `source_item='$ strict rounds.'`); the machine layer had passed them because the quote check compared corrupted row against identically-split inventory line. Repaired from the source; two inventory lines also restored to source-faithful norm notation; the suite's raw-entry extraction now honours escaped pipes, so this defect class is machine-caught for every future pass.
- **Nine module corrections** (Thm 4.4, Def 4.4, Thm 4.8, Thm 4.9, Cor 12.1, Thm 13.5, Thm 13.6, Conj 17.3, Conj 18.3 — the observation/institution channel), **four mapping-type corrections** (Cor 3.1, Thm 4.2, Ex 4.1, Thm 14.2 → COUNTEREXAMPLE_OR_LIMIT), **three evidence kind-corrections** (two definitions mis-flagged empirical; Cor 13.1 carries its proof on the line), and **one destination correction** (Thm 4.8 → Paper 5: observation-interval timing, not RFDE dynamics — hence Paper 5 55→56, Paper 4 55→54).

After this pass: 409 rows — 99 `row_verified`, 255 `requires_row_level_verification`, 27 `mapped_requires_final_citation_check`, 28 `adjudicated_rejected_or_negative_only`. The remaining open rows are the 21 non-A001 sources listed above.

## Interpretation

The inventory-coverage gate is closed: every item present in the registered A001–A025 formal-content inventories has a stable concordance row. The destination-routing gate is now also closed: every row has a publication destination (paper, conditional docket, negative register, or compendium appendix). The scientific closure gate is closing source by source: **A001 is the first complete source closure** (99 rows `row_verified`, 2026-08-27); the other 21 sources remain at their conservative intake states. Rows conservatively preserve source status and remain blocked where exact assumptions, proof line, mapping proof, or artifact must be checked. `accepted_mapping` after closure is a content-level acceptance, not an accepted theorem transfer — the §8 interface contract is still required. Rejected sources remain visible as negative/limit records.

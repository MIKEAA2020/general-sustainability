# Canonical Concordance A001–A025 — Coverage and Closure Status

- Schema: `TCS-1.0`
- Inventoried rows: **407**
- Sources represented: **25/25**
- Missing source inventories: `none`

## Rows by source

| Source | Rows |
|---|---:|
| A001 | 99 |
| A002 | 52 |
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
| A025 | 12 |

## Review state

| State | Rows |
|---|---:|
| `adjudicated_rejected_or_negative_only` | 28 |
| `mapped_requires_final_citation_check` | 45 |
| `requires_row_level_verification` | 334 |

## Destination routing (Wave-0 completion pass, 2026-08-26)

All 407 rows now carry a `destination_paper` + `monograph_chapter` assignment. The 156 rows previously holding `manual destination review` were routed by content review against `revised_optimal_publication_architecture_A001_A025.md` (source→paper mapping), the PUBLICATION_STRATEGY session-additions table, and the routed-row precedents already present in this concordance. Row-level content verification (`requires_row_level_verification` / `proposed_not_yet_interface_proved`) is unchanged and remains pending — this pass assigns publication destinations only; it promotes no theorem status.

| Destination | Rows |
|---|---:|
| Paper 2 | 127 |
| Paper 5 | 55 |
| Paper 4 | 55 |
| Paper 3 | 54 |
| negative/counterexample register or conditional redesign docket | 43 |
| Paper 7 conditional | 20 |
| Paper 1 or monograph introduction | 18 |
| conditional docket (open problem) | 12 |
| Paper 4 appendix or compendium | 12 |
| Paper 6 conditional | 8 |
| Paper 1 if independent-result gate; otherwise Paper 2 | 3 |

Routing vocabulary note: this pass introduced one new `destination_paper` value — `conditional docket (open problem)` — for unproved conjectures, open research hypotheses, and unreproduced/pending-correction artifacts (A001 Conjectures 17.1/18.2; the A002 research-programme items; A014 open hypotheses and the unreproduced computational object; A016 pending-correction and unreproduced data pipelines). It is distinct from the negative/counterexample register: those rows record refuted or defective claims, not open ones.

## Interpretation

The inventory-coverage gate is closed: every item present in the registered A001–A025 formal-content inventories has a stable concordance row. The destination-routing gate is now also closed: every row has a publication destination (paper, conditional docket, negative register, or compendium appendix). The scientific closure gate is not automatically closed. Rows conservatively preserve source status and remain blocked where exact assumptions, proof line, mapping proof, or artifact must be checked. `proposed_not_yet_interface_proved` is not an accepted theorem transfer. Rejected sources remain visible as negative/limit records.

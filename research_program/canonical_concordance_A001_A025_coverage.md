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
| `row_verified` (A001+A002+A011 scientific passes, 2026-08-27) | 176 |
| `mapped_requires_final_citation_check` | 13 |
| `requires_row_level_verification` | 192 |

## Destination routing (Wave-0 completion pass, 2026-08-26)

All 409 rows now carry a `destination_paper` + `monograph_chapter` assignment. The 156 rows previously holding `manual destination review` were routed by content review against `revised_optimal_publication_architecture_A001_A025.md` (source→paper mapping), the PUBLICATION_STRATEGY session-additions table, and the routed-row precedents already present in this concordance. Row-level content verification (`requires_row_level_verification` / `proposed_not_yet_interface_proved`) is unchanged and remains pending — this pass assigns publication destinations only; it promotes no theorem status.

| Destination | Rows |
|---|---:|
| Paper 2 | 128 |
| Paper 5 | 58 |
| Paper 4 | 54 |
| Paper 3 | 52 |
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

## Scientific row-closure — the first three complete sources (A001, A002, A011; 2026-08-27)

Executed as `research_program/close_concordance_rows_A001.py`, `close_concordance_rows_A002.py`, and `close_concordance_rows_A011.py` (decision tables encoded in the scripts; full report `concordance_row_closure_A001_A002_A011.md`). All three sources (`uploads/topdown.txt`, 2038 lines; `uploads/general_theory.txt`, 2424 lines; `uploads/paper3_empirical.txt`, 296 lines) were read end to end; all 99 A001 rows (81 `requires_row_level_verification` + 18 `mapped_requires_final_citation_check`), all 53 A002 rows (41 + 12), and all 24 A011 rows (22 + 2) closed to `row_verified`: item existence + kind + proof presence (or, for A011's computational/empirical records, the source's own exploratory-status discipline as the evidence witness) verified in the source; canonical module assigned or corrected; mapping type verified per TCS-1.0 §7; `mapping_status` → `accepted_mapping` **at the content level only** (no theorem status promoted; the §8 interface contract for cross-module transfer remains open in `interface_dependency`; the paper-time citation match rides the Part III paper-support discipline).

Findings of the A001/A002 passes (all corrected and machine-verified):

- **A001 — five corrupted intake rows** (CC-A001-061..064, -088): the intake builder's naive pipe split turned the Theorems 11.1–11.4 and 16.1 rows into fragment garbage (`item_type='F_0\'`, `source_item='$ strict rounds.'`); the machine layer had passed them because the quote check compared corrupted row against identically-split inventory line. Repaired from the source; two inventory lines also restored to source-faithful norm notation; the suite's raw-entry extraction now honours escaped pipes, so this defect class is machine-caught for every future pass.
- **A002 — substring keyword false-positives** (a new defect class): the intake heuristic read 'open' inside **'clopen'** (mis-flagging two PROVED finite-clopen kernel theorems as conditional_or_open — both carry complete proofs and Theorem status lines; corrected) and 'limit' inside **'donor limitation'** (mis-mapping an exact sufficiency corollary as APPROXIMATION; corrected to EXACT_SPECIALIZATION). One definition was mis-flagged with empirical-check evidence. Conversely, the sampled-RFDE kernel's `conditional_or_open` was CONFIRMED correct — the source's own status macro declares it Conditional theorem despite the theorem environment.
- **Fourteen module corrections across the two sources** (A001: nine — the observation/institution channel; A002: five — invariance theory to formal foundations, the observation-fibre family to observation_governance, the justice programme to architecture), **five mapping-type corrections** (A001: four → COUNTEREXAMPLE_OR_LIMIT; A002: one APPROXIMATION → EXACT), **evidence kind-corrections** (A001: three; A002: three), and **one destination correction** (A001 Thm 4.8 → Paper 5: observation-interval timing, not RFDE dynamics — hence Paper 5 55→56, Paper 4 55→54). 51 previously unclassified rows received their scientific module (A001: 33; A002: 18 — both sources now 0 unclassified).
- The A002 restored repair row CC-A002-053 (the second untitled Remark) was verified as the substitution-section remark, distinct from the conservation remark CC-A002-009.

### The A011 pass — the first empirical/computational source closure (24 rows)

- **No intake row corruptions** in A011 (all 24 rows quote-check cleanly). **Two module + destination corrections** (CC-A011-012, CC-A011-020: the 42-stock RAM cohort and its eligibility table — `ledger_diagnostics` → `observation_governance_empirics`, Paper 3 → Paper 5): the cohort is the spectral screen's input layer, defined by an analysis-side annual-review eligibility criterion (per the source itself, not a RAM classification), not a worked ledger example; Paper 3's fisheries examples are the worked ledger cases (A013/A014). **Eighteen module classifications** (A011 unclassified 18 → 0; 23 rows `observation_governance_empirics` + 1 `nonlinear_dynamics`). The artifact-obligation rows (017–024) close as **registered obligations, not discharged artifacts** (the source declares the computational record incomplete); CC-A011-024 registers that the shared bibliography dependency is declared but NOT committed (no `uploads/shared/` directory).
- **A011 inventory-level omissions flagged** (per the A001 unnumbered-remarks precedent — no rows created): the source's ONLY complete formal result — the forward-invariance proposition of §3.2, with proof, verified after the τ_m > 0 and effort-wording fixes — has **no concordance row** (an inventory-format outlier: A012/A013 inventory every formal result; A011's inventory carries its formal results in prose sections). Likewise the governance-time ontology (§2), the prospective identification designs (§6), the closed-loop MSE design (§7), and the falsification criteria (§8). The rapid-review consistency remark (§3.3) is covered at the theorem level by CC-A002-034. All flagged in the closure report as paper-wave non-loss obligations; the forward-invariance proposition is the campaign's first theorem-tier intake-extension candidate.

After these passes: 409 rows — 176 `row_verified`, 192 `requires_row_level_verification`, 13 `mapped_requires_final_citation_check`, 28 `adjudicated_rejected_or_negative_only`. The remaining open rows are the 19 non-closed sources listed above.

## Interpretation

The inventory-coverage gate is closed: every item present in the registered A001–A025 formal-content inventories has a stable concordance row. The destination-routing gate is now also closed: every row has a publication destination (paper, conditional docket, negative register, or compendium appendix). The scientific closure gate is closing source by source: **A001, A002, and A011 are the first three complete source closures** (176 rows `row_verified`, 2026-08-27 — the two largest formal sources covering the theorem atlas's Paper 2 core and the observation-governance content of Papers 2 and 5, plus Paper 5's empirical core: the A011 sampled-governance records, spectral screen, power analysis, and case search); the other 19 sources remain at their conservative intake states. Rows conservatively preserve source status and remain blocked where exact assumptions, proof line, mapping proof, or artifact must be checked. `accepted_mapping` after closure is a content-level acceptance, not an accepted theorem transfer — the §8 interface contract is still required. Rejected sources remain visible as negative/limit records.

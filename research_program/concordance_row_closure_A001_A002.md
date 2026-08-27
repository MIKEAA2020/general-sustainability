# Concordance Scientific Row-Closure — Sources A001 and A002

**Executed:** 2026-08-27. **Scope:** (1) all 99 concordance rows of source A001 (`uploads/topdown.txt`, *A Viability Theory of Constrained Sustainability under Uncertainty, Coupling, and Recoverability*): 81 rows in `requires_row_level_verification` and 18 in `mapped_requires_final_citation_check`; (2) all 53 concordance rows of source A002 (`uploads/general_theory.txt`, *A Typed Flux–Observation–Governance Theory of Sustainability*): 41 + 12. All closed to `row_verified`. **Method:** both source articles read end to end (2038 + 2424 lines); every inventoried item located in its source; each row's kind, proof presence, canonical module, mapping type, and evidence status verified against the source text — for A002 with special attention to the source's own claim-status macro (which self-declares Theorem vs Conditional theorem). **Executed by:** `research_program/close_concordance_rows_A001.py` and `close_concordance_rows_A002.py` (idempotent; the decision tables are encoded there). **Machine verification:** `reaudit/verify_concordance_rows.py` (12 checks, exit 0), including the closure layer.

**State after both passes:** 409 rows total — 152 `row_verified` (A001 + A002), 214 `requires_row_level_verification`, 15 `mapped_requires_final_citation_check`, 28 `adjudicated_rejected_or_negative_only`.

## What closure verifies — and what it does not

For each row, closure verifies: (1) the item exists in the source at the claimed kind with the claimed content (the deferred line check — every A001 theorem, proposition, corollary, and lemma was confirmed to carry its proof on the line, with the three exceptions noted below); (2) the canonical module assignment; (3) the primary mapping type per TCS-1.0 §7 semantics; (4) the proof/evidence status where the intake heuristic mis-typed the item's kind; (5) the item_type/source_item pair (five rows were corrupted at intake and repaired).

Closure does **not**: promote any theorem status (TCS-1.0 §6 statuses are untouched — the source's proofs remain at their registered reconstruction/verification level); prove any TCS-1.0 §8 interface contract (the producer/consumer obligation for cross-module theorem transfer remains in `interface_dependency`); or perform the paper-time citation match (Part III paper-support discipline owns that). `mapping_status` moves to `accepted_mapping` **at the content level only**: the mapping *type* and the exact source assumptions are verified; theorem transfer still requires the §8 contract.

## Classification principles used

- `formal_foundations` — viability operators, kernels, capture basins, barrier/obstruction calculus, substitution thresholds, invariance theory (Operator I territory), cascade containment (discrete-event invariance).
- `observation_governance_empirics` — the information/observation/belief/estimation channel and institutions-as-implementation-operators (the canonical 𝖮_q/𝖡_q/𝖨_q chain).
- `nonlinear_dynamics` — delay/RFDE characteristic-equation and bifurcation-adjacent content.
- `ledger_diagnostics` — mass balance and conservation under a declared closure.
- `architecture_transformation_composition` — multi-agent/game composition, intergenerational structure, the constructor algebra, and the compositional-viability (small-gain) theorem.
- Mapping type: an item that *establishes a boundary or impossibility* (including witness constructions) is `COUNTEREXAMPLE_OR_LIMIT`; an item that *instantiates the canonical types with no loss* is `EXACT_SPECIALIZATION`.

## Defects found and repaired (5 + 2 + 1)

1. **Five corrupted intake rows (pipe-split corruption).** The intake builder (`build_canonical_concordance.py`) split inventory lines naively on `|`, so every line whose description contains LaTeX norm notation (`$\|V\|$`) produced garbage cells. The A001 rows for **Theorems 11.1, 11.2, 11.3, 11.4, and 16.1** (CC-A001-061..064, -088) carried fragments like `item_type='F_0\'`, `source_item='$ strict rounds.'`. The machine layer had passed them because the quote check compared the corrupted row against the identically-split inventory line. Repairs: the five rows' item_type/source_item restored to the true labels and descriptions; the A001 inventory lines 72 and 97 were also repaired to the source-faithful single-backslash norm notation (they had a stray double backslash); and `reaudit/verify_concordance_rows.py`'s raw-entry extraction now honours escaped pipes (`_table_cells`), so this defect class is machine-caught for every future pass. Row counts were re-verified identical across all 25 inventories under the escape-aware extraction.
2. **One destination correction.** CC-A001-028 (Theorem 4.8, Delayed-information obstruction): routed to Paper 4 by the 2026-08-26 keyword-based routing; the verified content is the *observation interval* T_obs (information timing — "information may be accurate but arrive too late"), which is Paper 5's review-interval/observation-delay territory, not Paper 4's RFDE dynamics. Destination corrected to **Paper 5**. Distribution after correction: P2 128 / **P5 56** / **P4 54** / P3 54 / neg-counter 43 / P7-cond 20 / P1-or-monograph 18 / P4-appendix 13 / open-docket 12 / P6-cond 8 / P1-gate 3.
3. **Evidence-status corrections (kind errors only).** CC-A001-012 and -077 are *definitions* the intake had flagged `source_specific_empirical_status_check_required` → `defined_source_object`. CC-A001-081 (Corollary 13.1) carries a proof on the line in §13.6 → `proof_inventory_present_line_check_required` (the intake's `conditional_or_open` was a kind error). The five repaired rows likewise carry `proof_inventory_present_line_check_required`.

## Module corrections (9 rows)

| Row | Item | Intake module | Verified module | Reason |
|---|---|---|---|---|
| CC-A001-022 | Thm 4.4 (Observer-to-viability transfer) | formal_foundations | observation_governance_empirics | observer/estimation channel = the assessment operator of the canonical execution chain |
| CC-A001-025 | Def 4.4 (Safely informative action) | formal_foundations | observation_governance_empirics | belief-size reduction through actions is the information channel |
| CC-A001-028 | Thm 4.8 (Delayed-information obstruction) | nonlinear_dynamics | observation_governance_empirics | observation timing, not an RFDE |
| CC-A001-029 | Thm 4.9 (Observer safety buffer) | formal_foundations | observation_governance_empirics | output-feedback/observer-error family (with Thm 4.4, Prop 4.1) |
| CC-A001-070 | Cor 12.1 (Quota rescue) | formal_foundations | observation_governance_empirics | quotas/sanctions are institutional implementation operators (§13 family) |
| CC-A001-075 | Thm 13.5 (Ostrom sufficiency) | formal_foundations | observation_governance_empirics | Ostrom principles are mechanisms on the implementation operator |
| CC-A001-076 | Thm 13.6 (Ostrom obstruction) | formal_foundations | observation_governance_empirics | same family as Thm 13.5 |
| CC-A001-094 | Conj 17.3 (Adaptive management) | formal_foundations | observation_governance_empirics | adaptive observers/parameter learning are the assessment channel |
| CC-A001-099 | Conj 18.3 (Ostrom necessity) | formal_foundations | observation_governance_empirics | same Ostrom family |

## Mapping-type corrections (4 rows + 1 in repair)

| Row | Item | Intake | Verified | Reason |
|---|---|---|---|---|
| CC-A001-008 | Cor 3.1 | EXACT_SPECIALIZATION | COUNTEREXAMPLE_OR_LIMIT | recovery-into-K-while-staying-in-V is identically impossible outside the kernel — a boundary result |
| CC-A001-020 | Thm 4.2 | EXACT_SPECIALIZATION | COUNTEREXAMPLE_OR_LIMIT | impossibility witness: EViab = ∅ despite Viab = V ≠ ∅ |
| CC-A001-027 | Ex 4.1 (Hidden-mode conflict) | EXACT_SPECIALIZATION | COUNTEREXAMPLE_OR_LIMIT | explicit witness of common-action impossibility |
| CC-A001-084 | Thm 14.2 | EXACT_SPECIALIZATION | COUNTEREXAMPLE_OR_LIMIT | nonexistence of intergenerationally viable paths under nested-empty constraints |
| CC-A001-064 | Thm 11.4 | UNRESOLVED (corrupted) | COUNTEREXAMPLE_OR_LIMIT | the nilpotent-chain construction refutes finite spectral-radius bounds |

## Per-row closure summary

All 99 rows: item + kind + proof verified in the source; module classified/confirmed/corrected as above; mapping type confirmed/corrected as above; assumptions retained exactly. The per-row record (kind, anchor, verdicts, corrections) is in each row's `notes` field and encoded in the closure script. Notable per-row findings:

- **CC-A001-018** (Cor 4.1) and **CC-A001-083** (Thm 14.1): no separate proof on the line — they follow immediately from Theorem 4.1 (causal inverse) and Definition 14.1 respectively; recorded as such.
- **CC-A001-026** (Thm 4.7): no separate proof block; the argument is inline and Example 4.1 is the witness; recorded as such.
- **CC-A001-057** (Prop 10.1, generic non-polyhedrality): proved for an open dense parameter set under stated transversality/nondegenerarity conditions; the intake's `conditional_or_open` flag reflects the genericity qualification and is retained with that reading.
- **CC-A001-058** (Ex 10.2): the frontier numerical bracket Γ(0.12) ∈ (0.25, 0.38) is a source-stated sample check, not a validated computation — no artifact status is created by closure.
- **CC-A001-093** (Conj 17.2): the source itself **demoted** the conjecture (Remark 17.1: the infinite-horizon "→ 1" claim is false; only the finite-horizon part stands, as Theorem 17.1). The row title already carries the corrected finite-horizon-only form; the demotion is recorded in the closure note.
- **CC-A001-021** (Thm 4.3, delay margin): module `nonlinear_dynamics` **confirmed** and destination Paper 4 confirmed — this is the scalar RFDE characteristic-equation result (Hayes), genuinely delay dynamics, unlike its neighbour Thm 4.8.
- **Unnumbered remarks are not concordance rows** (the inventory covers labelled formal items only). Four substantive remarks — Remark 4.1 (certainty-equivalence obstruction: policy-class restriction, not information loss), Remark 12.1 (Clark under-extraction / rent dissipation / golden rule / harvest-tax instrument), Remark 17.1 (the stochastic-viability horizon split), and Remark 17.2 (myopic common-property OLG) — carry real content that the paper wave must not lose. They remain in the source and in the article-level integration record; no concordance row is created for them by this pass (creating rows would change the 409-row registered base; if the paper wave needs them as rows, that is a deliberate intake-extension decision with its own register entry).

## Distribution effects

- Review states: `requires_row_level_verification` 336 → **214**; `mapped_requires_final_citation_check` 45 → **15**; `row_verified` 0 → **152** (99 A001 + 53 A002).
- Destinations: Paper 5 55 → **56**; Paper 4 55 → **54** (the single documented correction, A001 Thm 4.8).
- A001 module distribution after closure: formal_foundations 54, observation_governance_empirics 30, architecture_transformation_composition 12, nonlinear_dynamics 2, ledger_diagnostics 1, unclassified 0 (was 33); mappings: EXACT_SPECIALIZATION 89, COUNTEREXAMPLE_OR_LIMIT 10.
- A002 module distribution after closure: observation_governance_empirics 16, formal_foundations 14, architecture_transformation_composition 8, ledger_diagnostics 8, nonlinear_dynamics 6, stage_spatial_extension 1, unclassified 0 (was 18); mappings: EXACT_SPECIALIZATION 46, COUNTEREXAMPLE_OR_LIMIT 2, PROJECTABLE_REDUCTION 1, APPROXIMATION 3, TRANSFORMATION 1.

## Source A002 — the second complete closure (53 rows)

Same procedure as A001. The notable A002 findings:

- **The source's own claim-status discipline governs.** A002 carries an explicit status macro per result (Theorem / Conditional theorem / Conjecture / Empirical hypothesis / Research programme). The closure used it as the primary evidence-status witness. In one important case it OVERRIDES the theorem environment: the sampled-RFDE knowledge kernel (CC-A002-027) is typeset as a theorem with a complete proof, but the source's own status line declares it *Conditional theorem, compact single-delay history model* — the intake's `conditional_or_open` is therefore CORRECT (confirmed, with the reason recorded), while the two sibling finite-clopen kernel theorems (CC-A002-023, -026) whose status lines declare *Theorem* were mis-flagged `conditional_or_open` by the intake heuristic and are corrected.
- **A new intake-defect class: substring keyword false-positives.** (i) The heuristic read **'open' inside 'clopen'**, mis-flagging the two proved finite-clopen kernel theorems (rows 023, 026) as conditional; both carry complete proofs and Theorem status lines — corrected to `proof_inventory_present_line_check_required`. (ii) It read **'limit' inside 'donor limitation'**, mis-mapping the donor-limitation corollary (row 012 — an exact sufficiency result) as APPROXIMATION — corrected to EXACT_SPECIALIZATION. (iii) A definition (row 002, hybrid specialization data) flagged with empirical-check evidence — corrected to `defined_source_object`.
- **Five module corrections:** CC-A002-011 (non-negative invariance) nonlinear_dynamics → formal_foundations (positive-cone invariance theory; the RFDE case is one of three modes, not the subject); CC-A002-012 (donor limitation) ledger_diagnostics → formal_foundations (kept with its parent theorem); CC-A002-016/018 (exact safety certifier; safety-crossing fibres) formal_foundations → observation_governance_empirics (the observation-fibre family); CC-A002-050 (justice and multiscale viability programme) formal_foundations → architecture_transformation_composition (the normative/multiscale-composition extension).
- **The mapping correction:** CC-A002-012 APPROXIMATION → EXACT_SPECIALIZATION (above).
- **Classifications:** 18 previously unclassified A002 rows received their scientific module (→ 0 unclassified), including the spatial/stage/polycentric programme (row 048) to `stage_spatial_extension` and the structural-uncertainty programme (row 052) to `observation_governance_empirics`.
- **The restored repair row verified:** CC-A002-053 (the 2026-08-26 machine-pass restoration of the second untitled Remark) is confirmed as the substitution-section remark (after the Farkas theorem: multipliers are separation certificates, not universal exchange rates), distinct from CC-A002-009 (the conservation moiety-scope remark).
- **Destination check:** no A002 destination corrections — the routing pass's assignments (conservation family → Paper 3; RFDE/hybrid/small-gain/conjecture family → Paper 4; hypotheses → Paper 5; programmes → docket/Paper 1-or-monograph/Paper 2) all verified against the content.
- **Notable confirmations:** the projectability criterion (row 036) keeps PROJECTABLE_REDUCTION (self-describing); the support-saturated logistic limit (row 038) and coarse-graining theorem (row 039) keep APPROXIMATION (genuine explicit-error-bound results — contrasted with row 012's false positive in the notes); the three conjectures (rows 042–044) and three empirical hypotheses (rows 045–047) verified with their declared missing-proof/disproof routes and test requirements.

## Honest boundary and next passes

These are the **first two complete source closures** of the scientific row-closure campaign; the procedure is now established (full source read → per-row verification against the source's own status discipline → corrections recorded → machine-checked closure layer). The remaining open rows: A003 (15), A004 (3), A005 (6), A006 (16), A007 (2), A010 (14+1), A011 (22+2), A012 (10+4), A013 (12), A014 (15), A016 (12), A017 (10), A018 (15+3), A019 (9), A020 (9), A021 (7+1), A022 (7+1), A023 (10+1), A024 (9), A025 (11+2). The paper wave (Papers 1–5) can now draw on the 152 closed A001+A002 rows as content-verified routing entries — this covers the two largest formal sources (the theorem atlas's Paper 2 core and the observation-governance content of Papers 2 and 5); closed rows still require the §8 interface contract before any cross-module theorem transfer, and the Part III paper-support gates remain NOT CONFIRMED by design.

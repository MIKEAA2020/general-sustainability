# Concordance Scientific Row-Closure — Source A001

**Executed:** 2026-08-27. **Scope:** all 99 concordance rows of source A001 (`uploads/topdown.txt`, *A Viability Theory of Constrained Sustainability under Uncertainty, Coupling, and Recoverability*): 81 rows in `requires_row_level_verification` and 18 rows in `mapped_requires_final_citation_check`, both closed to `row_verified`. **Method:** the full source article (2038 lines) was read end to end; every inventoried item was located in the source; each row's kind, proof presence, canonical module, mapping type, and evidence status were verified against the source text. **Executed by:** `research_program/close_concordance_rows_A001.py` (idempotent; the decision table below is encoded there). **Machine verification:** `reaudit/verify_concordance_rows.py` (12 checks, exit 0), including the new closure layer.

**State after this pass:** 409 rows total — 99 `row_verified` (A001), 255 `requires_row_level_verification`, 27 `mapped_requires_final_citation_check`, 28 `adjudicated_rejected_or_negative_only`.

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

- Review states: `requires_row_level_verification` 336 → **255**; `mapped_requires_final_citation_check` 45 → **27**; `row_verified` 0 → **99**.
- Destinations: Paper 5 55 → **56**; Paper 4 55 → **54** (the single documented correction).
- Module distribution within A001 after closure: formal_foundations 54, observation_governance_empirics 30, architecture_transformation_composition 12, nonlinear_dynamics 2, ledger_diagnostics 1, unclassified 0 (was 33); mappings: EXACT_SPECIALIZATION 89, COUNTEREXAMPLE_OR_LIMIT 10.

## Honest boundary and next passes

This is the **first complete source closure** of the scientific row-closure campaign; it establishes the procedure (full source read → per-row verification → corrections recorded → machine-checked closure layer). The remaining open rows: A002 (41+12), A003 (15), A004 (3), A005 (6), A006 (16), A007 (2), A010 (14+1), A011 (22+2), A012 (10+4), A013 (12), A014 (15), A016 (12), A017 (10), A018 (15+3), A019 (9), A020 (9), A021 (7+1), A022 (7+1), A023 (10+1), A024 (9), A025 (11+2). The paper wave (Papers 1–5) can now draw on the 99 closed A001 rows as content-verified routing entries; closed rows still require the §8 interface contract before any cross-module theorem transfer, and the Part III paper-support gates remain NOT CONFIRMED by design.

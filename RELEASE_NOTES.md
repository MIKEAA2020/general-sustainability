# Release Notes — v1.0 (26 August 2026)

This release publishes the programme's **versioned compendium archive** and the **monograph working preprint v1.0** together, on the journal-first strategy (five planned papers; monograph deferred and optional). Tag: `compendium-v1.0`.

## 1. Release contents

1. **Monograph working preprint v1.0** — `revised_sustainability_manuscript.md`, relabeled from "Working manuscript" to a clearly labeled working preprint with a preprint-status block (citable record of the architecture ahead of peer review; no mathematical content beyond the proof corpus; will be updated or superseded by the definitive Wave-3 monograph if one is written) and a suggested-citation block. The `.docx` was regenerated from the updated text.
2. **Compendium archive** — the full proof corpus, registers, corrected articles, validated computations, and scored trees, with this README as the public face and `PROOF_MANIFEST.md` as the register of record.

## 2. Clean-up tasks completed in this pass

### 2.1 Concordance destination routing (Wave-0 completion)

All 156 rows of `research_program/canonical_concordance_A001_A025.csv` that held `manual destination review` were routed by content review against `revised_optimal_publication_architecture_A001_A025.md`, the PUBLICATION_STRATEGY session-additions table, and the routed-row precedents. **All 407 rows now carry a publication destination.** Distribution: Paper 2 (127), Paper 5 (55), Paper 4 (55), Paper 3 (54), negative/counterexample register (43), Paper 7 conditional (20), Paper 1 or monograph introduction (18), conditional docket open problem (12), Paper 4 appendix or compendium (12), Paper 6 conditional (8), Paper 1 if independent-result gate (3). One new destination value was introduced — `conditional docket (open problem)` — for unproved conjectures, open research hypotheses, and unreproduced/pending-correction artifacts, distinct from the negative/counterexample register. Row-level content verification is unchanged and remains pending; no theorem status was promoted. Details: `research_program/canonical_concordance_A001_A025_coverage.md`.

### 2.2 E1/E2 direct publication destinations

The two elevations that previously had only consumer-mediated destinations now carry direct ones, recorded in the elevation files and in the Paper 2 session-additions row of `PUBLICATION_STRATEGY.md`: **E1 (language-completeness calculus)** → Paper 2 (atlas language layer) + Paper 1 scope statements via C-a; **E2 (selectors and certificates)** → Paper 2 (selection-and-certificate machinery chapter), with downstream consumers in Papers 1, 3, and 5.

### 2.3 Public-release curation

Removed from the release tree as working notes (all retrievable in git history at commit `270f5f7`):

| Category | Files | Reason |
|---|---|---|
| AI-commissioning prompts | `research_program/prompts/` (7 files), `research_program/general_theory_computation_closure_packet/prompts/` (4 files) | Working notes — AI repair/novelty/crosswalk commissioning documents |
| Raw AI transcripts (registered review sources ER001–ER005) | `uploads/{gemini,grok,qwen,qwen2–6,gpt1,1–5,glm 5.3,glm 5.3_2}.txt`, `uploads/external_review_response.md` | Raw AI transcripts; the processed point inventories and normalized captures in `research_program/external_reviews/` remain the citable review record; the registry's SHA-256 pins remain verifiable against history |
| Raw AI transcripts (unregistered) | `uploads/corrected_report.md`, `batch 3/` (five audit transcripts) | Same category; `JOINT_AUDIT_ASSESSMENT.md` and the audits index document their content |
| Disclosure working note | `research_program/validated_computations/HONEST_DISCLOSURE.md` | Working note; content consolidated into `PROOF_MANIFEST.md` → "Reproducibility status" (§ Disclosure consolidation), and all seven live references were updated to point there |

**Retained by design:** the original source manuscripts in `uploads/` (provenance layer referenced by the claim ledger, the formal supplement, and the article inventories); the packets' own `10_MASTER_*_PROMPT.md` files (they define the frozen review instruments); the external-review registry and processed ER captures; `batch 3`'s processed summaries already live in the audits index and joint assessment; the session worklogs (repair audit trail).

**Bookkeeping consequences (known and accepted):** `research_program/file_manifest.csv` and the packet manifests describe the pre-curation tree and were left unchanged as point-in-time records; the computation packet's README carries a curation note; the two `wave_e_*` working manuscripts had their HONEST_DISCLOSURE pointers replaced (reference-pointer updates only), and their SHA-256 pins in `PROOF_MANIFEST.md` Part VI were updated accordingly.

## 3. Verification

The reaudit suites were re-run on the release tree: the 13 numerical suites exit 0 with all assertions passing; `verify_consistency.py` shows exactly the documented post-repair reading; `verify_wave_e.py` passes with the pinned hashes matching (30/30 after the two manuscript pin updates). See `reaudit/README.md` for the layout note on `REPO`/`BASE` overrides.

## 4. Known limitations (unchanged by this release)

- Independent rerun: NONE for all computational artifacts (the single gating item before submission).
- Wave E specification matching: NOT CONFIRMED (no specification frozen).
- Papers 6/7 gates unclosed (A021 NAIM theorem unproved; A022 stage modal theorem false as stated) — the "five assured papers" architecture stands.
- The A025 fold pipeline is a committed script with the computation incomplete.

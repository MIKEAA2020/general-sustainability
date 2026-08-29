# Deep Scan of Residual Audit Points — All Audits and Joint Assessments (2026-08-29)

**Scope:** a systematic, deeper-than-prior pass over every audit and joint-assessment record in the repository for points worth implementing in the final papers — either as-is or after correction — plus the external style review read this session (the shared DeepSeek conversation containing a full-paper rewrite of Paper 1's second edition and three rounds of parallel audits, evaluated jointly there). **Method:** full reads of `BATCH5_JOINT_AUDIT_EVALUATION.md` (§§1–7), `FINAL_EDITIONS_CONSOLIDATION_SCAN.md` (§§1–7), `JOINT_AUDIT_ASSESSMENT.md`, `TRANSFER_AUDIT_RESPONSE.md`, the batch-5 auditor documents, `research_program/remaining_obstacles_to_general_theory.md`, `research_program/pending_separate_publications_register.md`, `PROOF_MANIFEST.md`, `RELEASE_NOTES.md`, `external_review_packet/README_v2.md`, and the per-paper verification scripts; every residual point re-verified against the current repository state before disposition. This document is the record; the adjudication of the external review's points is in `research_program/paper_types_and_venues_decision.md` §2.

---

## 1. The residual inventory and its disposition

### 1.1 Implemented this session (as new versions; no previous version touched)

| Point | Source | Disposition |
|---|---|---|
| The external review's framing, ledger, research-architecture, and process-vocabulary findings for Paper 1 (adjudicated in the venue memo §2) | DeepSeek conversation (2026-08-29), msgs 2–15 | **Implemented** as `papers/paper1_general_theory/manuscript_v3.md` (journal-facing edition), built by `reaudit/build_paper1_v3.py` with byte-preserved §§2–9; verified by new checks 9a–9t in `reaudit/verify_batch5_editions.py` |
| The venue/type decision across the whole programme | Owner's request; open in `remaining_obstacles` item 7 and the P2 venue memo | **Evaluated and recorded** in `research_program/paper_types_and_venues_decision.md` (paper types §3; venues §4; edition architecture §5) |
| The venue-pass trigger | Consolidation scan §7 (register items 1–8) | **Triggered for Paper 1** (its v3 executes the applicable items: edition-note handling, apparatus relocation, process-vocabulary removal, no publication roadmap); the register remains open for the other papers at their venue passes |
| Verification coverage of the new edition | — | `verify_batch5_editions.py` extended (9a–9t) and re-pinned; the full standing battery re-run at its documented baseline |

### 1.2 Registered for execution at the per-paper venue passes (not defects; deliberate deferral, now with the genre items added)

1. Strip header edition notes; convert companion file-path references to formal citations (all papers).
2. Resolve the Wave E papers' programme-source identifiers (`general theory §15`, R03, R04, A014) to the published sibling anchors at publication — standing publication-time obligation; implementing now would fabricate citation standing.
3. Shared companion-layer apparatus: cite the canonical carrier or vary (P1↔P3↔P4↔P5).
4. E-pair shared protocol sentences: cite the companions explicitly.
5. Cross-paper house style: Northern/northern cod; E2's Ω notation; the Edwards z/H notation; en-dash normalization; E4's math delimiters; E1's three uncited DFO entries (anchor or drop); the Cadigan 2016 rendering.
6. G13 orthography and the archival symbol renames (standing).
7. Numbering/style harmonizations: P1's three-operator numbering (cross-paper; deliberately not changed in v3 to avoid breaking sibling cross-references); P2's "Section N"/"§N"; P4's appendix abbreviation and "certificate … for an interval" rewording; P3's ADH expansion and H^win display; P5's MS-Native wording; E1's "Edwards J-17" naming.
8. **New (from this session's venue evaluation):** each remaining paper's journal-facing edition (P2's together with its SVVA template and ESM packaging); E3/E4's engagement with the peer-reviewed forecasting/groundwater literature (their reference lists are currently exclusively data agencies); P5's computational-tier strengthening (commit the screen code and outputs or restate the tier).
9. PROOF_MANIFEST Part VI re-pin (owner-gated; standing; behind acceptance of the v2 editions and later the v3 submission editions).

### 1.3 Declined or out of scope for the papers (with reasons)

| Point | Source | Reason |
|---|---|---|
| Archival-file edits (arena agent 2 findings F3/F4/F5/F9/F10; GT-04/G11 symbol renames) | BATCH5 evaluation §6.2 | Superseded archival files; editing them has no downstream value and risks divergence from the byte-verified lineage (standing decline) |
| Adding cross-citations between the nine papers beyond the existing fabric | Consolidation scan §5 | The citation fabric is already substantive and bidirectional; additional citations would be decorative (the scan's no-fabrication verdict stands) |
| Citing unpublished sibling files to resolve the E-paper identifiers now | Consolidation scan §5; BATCH5 evaluation §7.4 | Fabricates citation standing; the architecture forbids it |
| Unilateral closure of B-1 in `pending_separate_publications_register.md`, the PROOF_MANIFEST re-pin, or the obstacles-document venue clause | P2 venue memo §6; worklog Task 57 | Owner-gated; the packet pins these files; this session's decision memo supplies the recommendation they await |
| Rewriting any paper "from scratch" per the external review's strongest reading | DeepSeek msg 15 | Violates the non-loss rule and the provenance discipline; the transformation route (v3 build with byte-preserved bodies) implements the accepted substance without loss |

### 1.4 Substantive open items found by the scan that are NOT paper edits (next-step recommendations, in priority order)

1. **The interval Krawczyk stage of the A025 fold pipeline** — the single remaining unrebuilt certification stage (`PROOF_MANIFEST.md` "Reproducibility status"; `RELEASE_NOTES.md` §5(i); obstacles priority-5 residue). Well-specified computational work; no owner gate.
2. **Wave E Part III paper-support verification** — extending the spec-match pattern from artifact level to the papers' claimed numbers, upgrading the standing "every Wave E support row is NOT CONFIRMED" as evidence is earned.
3. **Figure determinism** — the F5 remedy (`SOURCE_DATE_EPOCH` + `svg.hashsalt`) documented in the manifest; small and mechanical; pin lands at the next manifest edition.
4. **The owner-gated bundle, prepared as one change-set when accepted**: PROOF_MANIFEST Part VI re-pin **plus** the manifest's two stale Part V rows (L194–195: the "continuum orbit" and "bunching" rows' stated reasons are contradicted by Part II's own executed/closed records — documentation drift, not substance) **plus** B-1 register closure **plus** the obstacles item-7 venue clause **plus** the coupled packet pin refresh.
5. **Stale documentation refreshes** (safe, unpinned files): `TRANSFER_AUDIT_RESPONSE.md` L102 (A1 and B4 have since been executed/closed — the "not changed" list was never refreshed) and `RELEASE_NOTES.md` L45 (the m=96/128 cross-checks are rerun-verified per the manifest and `reaudit/postv10_rerun/`). Recorded here rather than edited: both are historical audit-response records, and this scan's record is the cleaner correction vehicle.
6. **Cross-toolchain rerun** of the post-v1.0 fold/monodromy computations and both intervention legs (environment-gated; the manifest records the standard as unmet).
7. **G-MATH residuals toward the Paper 6 gate**: binding-channel operator-level continuum lift, H2 tubular chart, A2 coupling declaration.
8. **The independent line-by-line re-verification of the reconstructed proofs** before any Wave E submission (external-party-gated; standing).

### 1.5 Verification of previously claimed implementations (all confirmed)

The scan re-verified every "discharged" claim it found: the SPECIFICATION second editions (both exist, dated, pinned); the v1.1 monograph build (script + docx committed, pinned); the consolidation-scan fixes (present in the v2 files); the wave/spec/concordance/consistency battery at its documented baseline (re-run this session: `verify_batch5_editions` 175/175 before this session's extension; review packet INTACT; validated computations, wave_e 42/42, spec match 36/36, concordance 409 rows/354 closed, consolidation, manuscript sweep, findings, joint disputes — all PASS; `verify_consistency` at exactly its 13 documented defect-gone failures). One inconsistency confirmed and registered: `external_review_packet/README_v2.md` L93 describes B-1 as resolved while the pinned register still shows it open (owner-gated; §1.3 above).

## 2. Answer to the question asked

**Are there remaining points from any audit or joint assessment worth implementing in the final papers?** Yes, in three classes: (i) the external style review's Paper 1 findings — implemented now as the journal-facing third edition with the accepted subset, the rejected subset documented with reasons; (ii) the venue-pass register — not paper defects, but triggered for Paper 1 by the venue decision and executed for it, with the remaining papers' executions scheduled at their venue passes; (iii) the E3/E4 literature-engagement and P5 computational-tier strengthening registrations — new, substantive, and necessary for the chosen venues, but belonging to the venue passes rather than to the science. Everything else the audits left open is either owner-gated (the manifest/register/obstacles bundle), deliberately declined with recorded reasons, or not a paper edit at all (the computational campaigns of §1.4).

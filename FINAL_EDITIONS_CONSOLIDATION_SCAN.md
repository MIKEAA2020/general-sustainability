# Final Editions Consolidation Scan — Remnants, Redundancy, Terminology, Cross-Citation, and Overlap Audit of the Nine Final Papers

**Date:** 2026-08-29 (third session of the batch-5 response series). **Scope:** the nine final papers — the five core papers' second editions (`papers/paper{1..5}_*/manuscript_v2.md`) and the four Wave E second editions (`wave_e_{cod,edwards}/manuscript/*_v2.md`). **Method:** three independent full reads of all nine papers (one read per paper pair/triple), scripted remnant-vocabulary scans (18 pattern classes), within-paper duplication scans (normalized-line and 12-gram), pairwise 12-gram overlap scans across all 36 paper pairs, and verification of every load-bearing finding against the source articles (`revised_articles/`, `uploads/`), the 409-row concordance, the frozen Wave E protocols, and the sibling papers before acceptance. **Adjudication record for the implemented changes:** `BATCH5_JOINT_AUDIT_EVALUATION.md` §7. This document is the audit record itself.

---

## 1. Remnants (editing-process leftovers in the final versions)

**Clean in the main.** The bodies of all nine papers are free of batch/auditor/task/TODO vocabulary; `BATCH5_JOINT_AUDIT_EVALUATION.md` appears only inside the deliberate header edition notes (stripped at the registered venue pass); every cited repository path resolves to a committed file. The terms that a keyword scan surfaces — "audit template", "model-audit", "admissibility audit", "audited out of sample" — are the A010 source's own scientific vocabulary; "naive baselines" is standard forecasting terminology; "adjudicate" in the scientific sense ("field spectral nulls cannot adjudicate the mechanism") is ordinary English; the mathematical gate vocabulary (gated/ungated, 124 uses, concentrated in Paper 4) is the sources' own and is retained by standing instruction; "fixpoint" survives only inside the Tarski (1955) title (a reference title, immutable) and the E2 header note.

**Remnants found and removed (the adjudicated list is evaluation §7.1):**

| Paper | Remnant | Disposition |
|---|---|---|
| P2 ×3 | Edition/changelog vocabulary in body prose: "supplied in this edition", "supplied in the second edition", "discharged in this edition" | Reworded to manuscript-relative forms |
| P3, P5 | Stale pre-intervention inventory: "two scored-forecast papers exist in the programme" (P5 added "referenced once") | Corrected to the four scored Wave E manuscripts (batch 5 had corrected the same count in Papers 1 and 5 §9 but missed these two instances) |
| E1 | "(the companion governance paper states the same correction)" — changelog vocabulary | "makes the same point" |
| E2 | "printed at the exact operand values" — print-process meta | Removed |
| E4 | Duplicated re-execution sentence in §6 (Limitations) | Removed (§7's availability statement is its home) |
| P1 | "the atlas's Definition 2.3" — a statement number that exists in no sibling paper | "the atlas's §2.3" |
| E1 | One "pre-registered" among uniform "preregistered" | Normalized |
| E1 | Capelin reference out of alphabetical order | Reordered |

**Registered for the venue pass (deliberate design, not defects):** the header edition notes themselves; E1's "corrected … status" provenance sentence (§1); E4's "in-repo-verified reduction" (§2, to become source-relative); the E2 data-availability section's edition-record sentence (appropriate for a reproducibility statement).

## 2. Redundancy (within-paper)

**Within-paper duplication is now zero at sentence level across all nine papers** (normalized-line and 12-gram scans; the one Task-59 edit-induced duplication in Paper 1 §2.2 was already removed by the residual pass). Three genuine within-paper redundancies in Paper 2 were condensed to pointers, and one E4 duplication removed:

- P2's Remark A.3 was stated twice (main text + Appendix A.3, verbatim, with the main-text copy admitting it) → main-text instance is now a pointer.
- P2's Programme 13.3 restated §2.6's intergenerational recursive criterion verbatim inside a parenthesis (the source's row carries only a short reference) → replaced by the §2.6 reference.
- P2's Theorem 5.5 scope note restated Appendix A.4's two sentences verbatim → condensed.
- E4's §6 repeated §7's re-execution sentence verbatim → removed from §6.

**Kept as legitimate structure (not redundancy):** Abstract↔body summaries; §1 roadmaps vs §1.5 ownership paragraphs; status-ledger tables vs prose (the programme's table-plus-prose discipline); Paper 4's §2.4↔§9 declared seam restatement; Papers 3/4's near-identical boundary-invariance argument (each paper's self-containedness, with P4 crediting the row to Paper 3); the deliberate no-pooling refrain in E1 (the discipline is the paper's point); the certification-prose overlap between Paper 4's §10 and its bounded appendices (self-containedness by design). The remaining compression opportunities (P3's §2.2 forward pointer, P4's §1.1/§6 fold-status refrain, P5's §6.3 caveat pair) are registered as venue-pass polish, not defects.

## 3. Terminology consistency

**Verified consistent across the nine papers:** the gate vocabulary (P4's gated/ungated pairs M3-U/M3-B, gated/ungated C3, Candidates A/B — 99 uses, no variants); the atlas/architecture/MWR/concordance/claim-status/no-transfer-rule vocabulary; "preregistered" (now uniform); "negative certificate"; "retention rule/decision"; the model identifiers (M1/M1b/M2/M2m/M3/M4; the E-papers' back-references "the ladder's M2"); LRP defined at first use in both cod papers; T=∞ notation; UC class names; K* safe-set notation; the Cor2/Cor5 erosion vocabulary with the contraction (Edwards) / expansive (cod) forms correctly opposed; S1 = the reactive rule in both intervention papers (parallel by design); 2J3KL forms; figure references.

**Inconsistencies found and fixed:**

| Item | Disposition |
|---|---|
| P1 §2.2's canonical-tuple glosses shifted one slot against the A002 source and the atlas (V carried Γ's gloss, Γ the observation gloss, … D a gloss found in no source) — the batch-5 reconciliation had been implemented at letter level only | Corrected to the source mapping (evaluation §7.1, P1-C1) |
| P1 §2.3's four uncertainty levels diverged from the source's four under the same row id (CC-A002-004) | Corrected to the source's levels |
| P1 §2.4's five diagnostic types (conservation check, positivity check, deficit diagnostic, first-passage diagnostic, horizon diagnostic) appear in no committed source and contradicted the atlas's §2.5 rendering of the same row (CC-A002-005) | Corrected to the source's five types; the commentary kept |
| E4 mixed CPM (7 prose uses) with cpm (10 uses incl. tables) | CPM everywhere, defined at first use in the abstract |
| E2 used the protocol's cpm label without introducing it | Introduced at the family declaration |
| P5's single "Northern cod" among lowercase uses | Lowercased |
| P2 §14's "§8 interface contract" (in-paper §8 is a different section) | "cross-module interface contract" (the name used by P3/P4 and the concordance) |
| P1 §10.2's closed-source enumeration "A010–A020" included the negative-register source A015 | Corrected enumeration (19 = A001–A007, A010–A014, A016–A020, A024, A025) |

**Registered for the venue pass:** "Northern cod" vs "northern cod" across papers (each paper now internally consistent; the cross-paper house style is a venue decision — the reference titles keep the capitalized form); E2's plain-text Ω notation vs E1's math mode; the Edwards pair's z/H dual notation; en-dash/"--" mixing; E4's \(...\) delimiters; E1's three uncited DFO entries (anchor or drop); the Cadigan 2016 rendering difference between P5 and E1; P1's three-operator numbering (I/II/…, Observation unnumbered — matches the programme registry; harmonize at venue).

## 4. Duplication and self-plagiarism across papers

**Measured:** pairwise 12-gram overlap across all 36 pairs of the nine final papers: 0.01–1.55% of each paper's n-grams. The shared material decomposes into five classes:

1. **Shared bibliography entries** (the largest class for E-pairs and P5↔E1/E2) — standard and legitimate.
2. **The companion-layer apparatus** (P1↔P3↔P4↔P5, ~100–174 12-grams per pair): the series header, the provenance paragraph ("409-row concordance inventory (source location, canonical module, mapping type, evidence status, destination)"), and the claim-status preamble ("two rules govern this article. No promotion: …"). Identical by design — this is the claim-status discipline's carrier text, ~150–250 words per paper.
3. **Bidirectionally attributed theorem restatements** (P2↔P3/P4): the atlas states the canonical form and marks the primary destination; the application paper states the named instantiation and credits "canonical statement in the atlas"/"proofs owned by Paper 2". Each side carries its CC identifier. This is the concordance discipline working as designed, not duplication.
4. **Sibling Wave E protocol sentences**: E1↔E3 share their opening rationale sentence and closing scope discipline (both attributing "general theory §15"); E2↔E4 share their abstract architecture sentence (the scored-intervention requirement) and data-availability boilerplate. Each pair declares the companion and the shared frozen protocol.
5. **Data/code availability boilerplate** (one shared repository).

**Verdict:** no scientific content — no theorem, proof, result, discussion, or conclusion — is duplicated across papers without attribution. The only unattributed verbatim sharing is class 2 (infrastructure text, identical by design) and class 4's two protocol sentences (attributed to the same source, but not cross-citing the companion). **Both classes are registered for the venue pass:** at submission, shared apparatus should cite the programme's canonical carrier (Paper 1 / the companion repository) rather than repeat verbatim, and the E-pair shared sentences should cite the companion paper explicitly. No action now: the texts are pinned, the corrections are diffable, and the repetition is the documented design's cost.

## 5. How the papers strengthen, lend to, and cite each other (the cross-citation audit)

The honest answer has two parts: the citation fabric **already exists and is unusually rigorous**, and the one genuine gap is a **publication-time resolution obligation**, not a missing citation to add now.

**The verified real dependency graph (all already implemented in the texts):**

- **Paper 1 (architecture) ← everyone.** Each application paper's §1.5 declares the ownership boundary ("Paper 1 owns the typed canonical architecture, including the diagnostic types and their no-transfer rule"). This is architectural citation, load-bearing by construction: the type system, the four model maps, and the no-transfer rule govern what the application papers are allowed to claim.
- **Paper 2 (atlas) ↔ Papers 3/4 (canonical ↔ named instantiation).** P3's conservation family headings carry "[proofs owned by Paper 2]"; P4's delay-certificate statements carry "[canonical statement in the atlas]"; P2's rows carry "primary destination Paper 3/4" notes. Both directions attribute; neither side silently duplicates.
- **Paper 2 → Paper 5 (information layer).** P2's Theorem 6.6 (delayed-information obstruction) and Proposition 7.7 (information monotonicity) are marked "primary destination Paper 5"; P5 states the local instances and cross-references the owning entries.
- **Paper 3 ↔ Paper 4 (the seam).** The ledger-to-dynamics interface contract, stated in both papers (P3 §8, P4 §9), with the single-resource deficit identity as the exact shared object and CC-A018-004/CC-A019-004 as the declared cross-references — the strongest form of inter-paper citation in the programme: a jointly declared interface, not a borrowing.
- **Paper 1 §9.2 (admission discipline) → the four Wave E papers (executed).** P1 states the admission standard (preregistered scoring, held-out defect audits, frozen retention rules); the E papers execute it on two measured systems; P1 §9.1 instantiates the methodology with their verdicts (now stated accurately per system); P5 §9 declares the scored-forecast methodology as the rule the prospective programme inherits. The chain architecture → execution → inheritance is complete and bidirectional at the programme level.
- **The Wave E pairs.** Each intervention paper declares the companion prediction leg's object and results ("The governed surplus-production object of `wave_e_cod`: the ladder's own M2 class…"; "The prediction leg returned a negative certificate…"); E2↔E4 declare each other as the cross-system analogue, and the cod/Edwards retention contrast (none retained / reactive rules retained) is stated in both papers as a system-dependent finding — a genuine cross-paper scientific comparison, not decoration.

**The designed anti-decorative discipline:** no paper depends on a sibling for a locally load-bearing definition (the Minimal Working Realization principle, declared in every §1.5). Citations between the papers therefore exist exactly where content actually flows — and none where it does not. This is why the audit found no decorative citations to remove and declined to add any.

**The genuine gap (registered, not implemented):** the Wave E papers cite the programme's sources by internal identifier — "general theory §15", "R03", "R04 (Theorem 1 converse)", "R04.Cor2/R03.Cor5", "A014 (defect register)" — and the core papers likewise cite "the flagship manuscript" for manuscript-native rows. This is the honest form while the sibling papers and the monograph are unpublished repository files. **At publication, the citation resolution must be:** the intervention-selection requirement ("general theory §15") → Paper 1 §9.2 (the admission discipline) + Paper 5 §9 (the scored-forecast methodology and the falsification-design layer); the E-pair shared protocol sentences → explicit companion citations; the E papers' erosion conversion (R04.Cor2/R03.Cor5) → the programme's published carrier of the conversion theorems; the "flagship manuscript" anchors → the monograph preprint or the published papers, whichever is citable first. Implementing these resolutions now — citing unpublished, unaccepted files as if they were citable literature — would fabricate exactly the citation standing the architecture forbids.

**Not available (stated plainly, per the no-fabrication instruction):** there is no further nonsuperficial lending relation among these nine papers that the content supports. Papers 3/4/5 do not methodologically depend on each other beyond the declared seam; the two Wave E systems are never pooled by design; Paper 2 needs nothing from the applications (its theorems are stated at their own canonical level). Any additional cross-citation would be decorative.

## 6. Verification

All changes of this pass are editorial (terminology, pointers, counts, vocabulary, redundancy condensation): no theorem, proof, number, claim status, ledger row, CC-identifier set, scored verdict, retention decision, or first-edition file is changed. The full standing battery was re-run at the documented baseline after the edition pins were refreshed: `verify_batch5_editions` (extended with the consolidation-pass checks §8a–8n), `verify_review_packet` INTACT, `verify_validated_computations`, `verify_wave_e` 42/42, `verify_wave_e_spec_match` 36/36, `verify_concordance_rows` 409/354, `verify_wave_e_consolidation`, `verify_manuscript_sweep`, `verify_findings`, `verify_joint_disputes` — all PASS; `verify_consistency` at exactly its 13 documented defect-gone failures; the five paper self-checks PASS.

## 7. The venue-pass register (accumulated)

Everything this audit found and deliberately did not fix now, with its trigger:

1. Strip the header edition notes; convert companion file-path references to formal citations.
2. Resolve the Wave E papers' programme-source identifiers to the published sibling anchors (§5 above).
3. Shared companion-layer apparatus: cite the canonical carrier or vary (§4, class 2).
4. E-pair shared protocol sentences: cite the companion explicitly (§4, class 4).
5. Cross-paper house style: Northern/northern cod; E2's Ω notation; the Edwards z/H notation; en-dash normalization; E4's math delimiters; E1's three uncited DFO entries; the Cadigan 2016 rendering.
6. G13 orthography and the archival symbol renames (standing).
7. Paper 1's three-operator numbering harmonization; P2's "Section N"/"§N" style; P4's "Appendix A"/"App. A" cell abbreviation; P4's "certificate … for an interval" rewording; P3's ADH expansion; P3's H^win definition display; P5's MS-Native classification wording; E1's "Edwards J-17" compressed naming.
8. PROOF_MANIFEST Part VI re-pin to the v2 editions (behind the owner's acceptance gate, standing).

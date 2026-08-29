# External Review Packet — General Sustainability Programme (second edition)

**Prepared:** 2026-08-29 (batch-5 joint-audit response). **Relationship to the first edition:** this README_v2 supersedes `README.md` (2026-08-28) as the packet's entry point. The first edition remains committed and pinned unchanged — it is the frozen snapshot against which the batch-5 audits (`batch 5/`, four independent auditors, seven documents) were performed. This second edition (a) corrects the first edition's one inventory error (§1.3: `ms_part1.md`–`ms_part4.md` are the part files of a *separate* 14 August 2026 manuscript — the architectural-kernel version, subtitled "An Architectural Kernel and Composition Language for Ecological, Economic, and Social Systems" — not parts of the flagship "Robust Viability" manuscript; the two strands hold opposite positions on the flagship's §16.1 central conjecture, which the kernel strand retires at its Part VI §28.1), and (b) adds the batch-5 corrected editions of the nine paper drafts to the reviewer's inventory (§1.4). The repository (`https://github.com/MIKEAA2020/general-sustainability`) remains the single source of truth; this packet is the curated entry point into it, not a second copy.

**How to use this packet.** Clone the repository, read this file top to bottom, then read the manuscripts in the suggested order (§1). Every computational claim is checkable against the committed artifacts (§3) by running the verification battery (§6). The programme's claim-status discipline — every claim carries its evidentiary status, and no status is ever promoted — governs everything below. **For review purposes, read the second editions (`*_v2.md`, §1.4):** they are the audited drafts with the batch-5 accepted corrections applied; the first-edition files remain in place, byte-identical, as the audited baseline, so every correction is directly diffable. The joint evaluation of all four auditors' findings — including the rejected findings and the corrections made to the auditors' own suggestions — is `BATCH5_JOINT_AUDIT_EVALUATION.md` (repository root).

---

## 1. The paper drafts under review

### 1.1 The five core papers (the assured core) — first-edition paths

| # | Title (short) | First edition (audited) | Second edition (batch-5 corrections) | Ledger | Status |
|---|---|---|---|---|---|
| 1 | General Theory and Research Architecture of Sustainability | `papers/paper1_general_theory/manuscript.md` | `papers/paper1_general_theory/manuscript_v2.md` | 21 rows + 1 cross-ref | **Final draft** (v2: corrected edition) |
| 2 | The Formal Mathematical Foundations of Sustainability: A Typed Theorem Atlas | `papers/paper2_theorem_atlas/manuscript.md` | `papers/paper2_theorem_atlas/manuscript_v2.md` | 89 rows | **Final draft** (v2: corrected edition) |
| 3 | Conserved Material Ledgers and Componentwise Depletion Diagnostics | `papers/paper3_material_ledgers/manuscript.md` | `papers/paper3_material_ledgers/manuscript_v2.md` | 52 rows + 2 seam | **Final draft** (v2: corrected edition) |
| 4 | Delay-Driven Capital Liquidation and Nonlinear Institutional Dynamics | `papers/paper4_delay_dynamics/manuscript.md` | `papers/paper4_delay_dynamics/manuscript_v2.md` | 68 rows + 2 seam | **Final draft** (v2: corrected edition) |
| 5 | Sampled Governance, Empirical Identification, and Falsification Design | `papers/paper5_sampled_governance/manuscript.md` | `papers/paper5_sampled_governance/manuscript_v2.md` | 57 rows + 6 native | **Final draft** (v2: corrected edition) |

**What "final draft" means here:** content-complete at the scientific level — every planned theorem, application, ledger row, and camera-ready bibliography entry is in place; every paper's committed self-check (`papers/paper*/verify_retained_rows.py`) exits 0 on the first editions; the second editions carry the batch-5 corrections with in-text citation hooks now attached at the data- and method-bearing points. **What remains before submission:** the venue-format pass for each paper (journal template, length policy check, and — for Paper 2 — packaging of the full proof expansion as electronic supplementary material; §5).

### 1.2 The four Wave E papers (the scored empirical gate)

| # | Title (short) | First edition (audited) | Second edition | System | Status |
|---|---|---|---|---|---|
| E1 | Northern cod 2J3KL — scored forecast ladder | `wave_e_cod/manuscript/wave_E_cod_forecast_ladder.md` | `wave_E_cod_forecast_ladder_v2.md` | cod | **Final draft** (v2: corrected edition) |
| E2 | Northern cod 2J3KL — intervention analysis | `wave_e_cod/manuscript/wave_E_cod_intervention.md` | `wave_E_cod_intervention_v2.md` | cod | **Final draft** (v2: corrected edition) |
| E3 | Edwards Aquifer (San Antonio pool) — scored forecast ladder | `wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder.md` | `wave_E_edwards_forecast_ladder_v2.md` | Edwards | **Final draft** (v2: corrected edition) |
| E4 | Edwards Aquifer (San Antonio pool) — intervention analysis | `wave_e_edwards/manuscript/wave_E_edwards_intervention.md` | `wave_E_edwards_intervention_v2.md` | Edwards | **Final draft** (v2: corrected edition) |

There are exactly four Wave E manuscripts: two scored systems (Northern cod 2J3KL; Edwards Aquifer J-17), each with a forecast-ladder leg and an intervention leg. The first editions are pinned by SHA-256 in `PROOF_MANIFEST.md` Part VI (the pins are unchanged and remain the register of record for the audited texts); the second editions are pinned by `reaudit/verify_batch5_editions.py`. The two systems are never pooled and no result transfers between them (frozen specifications: `wave_e_cod/SPECIFICATION.md`, `wave_e_edwards/SPECIFICATION.md` — second editions `*_v2.md`, carrying the W03/W09 manuscript-echo corrections; machine-verified by `reaudit/verify_wave_e_spec_match.py`, 36/36 checks). The batch-5 corrections include two runner-level fixes (`wave_e_cod/src/run_intervention_v2.py`, convergence-corrected; `wave_e_edwards/src/run_intervention_v2.py`, comparator-corrected and verified inert) with regenerated artifacts committed alongside the audited ones (`results/intervention_results_v2.json`, `intervention_boundaries_v2.csv` in both directories).

### 1.3 Other manuscript files in the repository (not submission drafts)

| File | What it is | Status |
|---|---|---|
| `revised_sustainability_manuscript.md` | The monograph working preprint v1.0 (the architectural kernel, public and citable) | **Working preprint** — v1.1 (`revised_sustainability_manuscript_v1.1.md` + `.docx`, batch-5: the hybrid-trajectory formula repair, the completed §27 indicator rationale, one citation) supersedes it as the citable record |
| `general_theory_of_sustainability_manuscript.md` | The flagship working manuscript of 14 August 2026 — the "Robust Viability in Dependency-Closed Systems" strand | Superseded (archival; v-history: v0.1 → v0.2 → this); corrected edition: `general_theory_of_sustainability_manuscript_corrected.md` |
| `general_theory_of_sustainability_v0.1.md`, `general_theory_of_sustainability_v0.2_comprehensive.md` | Earlier flagship versions (same strand) | Superseded (archival); corrected editions: `*_corrected.md` |
| `ms_part1.md`–`ms_part4.md` | Part files of a **separate** 14 August 2026 manuscript — the architectural-kernel strand ("An Architectural Kernel and Composition Language…"; 33 sections in six Parts; successor to the flagship v-history; retires the flagship's §16.1 conjecture at its Part VI §28.1) | Superseded (archival); corrected editions: `ms_part{1..4}_corrected.md` |
| `formal_supplement_A001_A002_A006_A010.md` | Formal supplement restoring A001/A002/A006/A010 material at source status | Archival input (content routed to Papers 1–5) |
| `revised_articles/` (A001–A025) | The corrected source articles — the inputs the papers were built from | Provenance layer (not for submission) |
| `uploads/` | The original source manuscripts as uploaded | Provenance layer |

(The first edition of this table described `ms_part1.md`–`ms_part4.md` as "part files of the 14 August 2026 working manuscript", conflating the two same-dated strands; this is the correction recorded as finding G05 of the batch-5 joint evaluation. "Flagship" in repository documents refers to the Robust-Viability strand; the current monograph descends from the kernel strand.)

No paper-shaped file exists outside this table and §1.1–1.2: the publication architecture (`research_program/revised_optimal_publication_architecture_A001_A025.md`) routes every source proposition to Papers 1–5, the conditional docket (Papers 6–7, gated on their own theorem-completion conditions), the negative register, or the monograph — verified row by row by the 409-row concordance (§2).

**Suggested reading order for a first review:** Paper 1 (v2) → Paper 2 (v2) → Papers 3–5 (v2) → the four Wave E papers (v2) → `PROOF_MANIFEST.md` (the register of record for the audited first editions) → `BATCH5_JOINT_AUDIT_EVALUATION.md` (what changed between editions and why). Reviewers focusing on one paper can read it alone: every paper carries a Minimal Working Realization of the canonical objects it needs and cites no sibling paper for a locally load-bearing definition.

### 1.4 The batch-5 corrected editions — what changed and what did not

The four auditors' findings and their adjudication are documented finding-by-finding in `BATCH5_JOINT_AUDIT_EVALUATION.md`. Summary for the reviewer:

- **Changed:** presentational, count, citation, and terminology defects; two genuinely wrong constants (the cod intervention's flat-180-kt T=∞ kernel boundary 2335.4 → 2338.3, a convergence correction with the corrected runner committed; the Edwards BAU nominal-kernel horizon "T ≈ 14" → "T ≈ 13", the continuous crossover being 12.7); one results paragraph rewritten against the committed artifacts (the cod forecast §5.3 Brier paragraph, which had printed the Ω_2016 values inside the Ω_xte section with a conclusion false on Ω_xte); one proof supplied (Paper 2's Theorem 6.4, discharging its registered one-step obligation); one contradiction resolved (Paper 4's §6.1 lower-boundary passage, now branch-resolved with the source's dropped reconciling sentence restored and the SNPO classification marked provisional for the large branch); the monograph's hybrid-trajectory formula repaired at byte level.
- **Residual pass (2026-08-29, second session; evaluation §6):** four implementation-claim gaps closed (the flagship Appendix A's normative-authority slot, G04(a); the symbol-I overload declarations and the grievance-trigger disambiguation, GT-04; the registry-resolution supersession notes, GT-05/GT-06); two previously unadjudicated findings implemented (the ms_part4 §26 proof-obligations expansion acknowledgement, F7; the Appendix B provenance alphabet's definitional entry, F11); one edit-induced duplication removed from Paper 1 v2; the two SPECIFICATION second editions issued (W03/W09 echo corrections); the monograph v1.1 docx built (build script committed).
- **Not changed:** every scored verdict, retention decision, theorem status, ledger row count, CC-identifier set, and the audited first-edition files themselves (byte-identical; the pins in `PROOF_MANIFEST.md` and the first-edition packet remain valid).

---

## 2. The register of record

**`PROOF_MANIFEST.md`** (repository root) — every theorem with its honest status, every computation artifact with its SHA-256 and reproduction command, the Wave E support table (Part VI, pins all four Wave E first-edition manuscripts), the certification hierarchy for numerical claims (nominal → re-execution-verified → independently re-executed → certified), and the reproducibility/disclosure status. This is the document against which every claim in the papers is audited; the reaudit suites (§6) machine-verify its pins. The second editions are additionally pinned by `reaudit/verify_batch5_editions.py`; a manifest re-pin to the second editions belongs to the next manifest edition, after the owner accepts the corrected editions.

**The 409-row concordance** (`research_program/canonical_concordance_A001_A025.csv`) links every source proposition to canonical notation, assumptions, proof/evidence status, mapping type, destination paper, and monograph chapter; 354 rows are closed by dated full-source scientific passes across nineteen sources (the closure scripts are committed under `research_program/`; the closure report's title overcounts by one — recorded in the joint evaluation); the 27 open rows are exactly the three conditional-paper sources A021–A023 (Papers 6–7's gates), behind none of the nine manuscripts under review. The full accounting: 354 row-verified + 28 adjudicated rejected-or-negative-only (A008/A009/A015, the negative register) + 27 open = 409.

---

## 3. The validated computations

**`research_program/validated_computations/`** — the interval-certified layer, with committed code and artifacts:

| Artifact family | Entry points | What it certifies |
|---|---|---|
| A025 Hopf interval certificates | `a025_fold/a025_interval_hopf.py` (+ JSON outputs) | The interval-Newton enclosures of the Hopf crossings τ−∈[3.6661490142739, 3.6661490142743] yr and τ+∈[150.3584773101408, 150.3584773101421] yr cited in Paper 4 §4 and Appendix A |
| C4 orbit Krawczyk certificate | `a021_c4/c4_orbit_krawczyk.py`, `c4_orbit_krawczyk_certificate.json` | The periodic-orbit enclosure of the C4 system |
| C4 off-grid residual interval | `a021_c4/c4_offgrid_interval_v2.py`, `c4_offgrid_residual_interval.json` | Off-grid residual enclosure |
| C4 monodromy (dt = 0.25, 0.1) | `a021_c4/c4_monodromy*.py`, `.npz`, `_enclosure.json` | Monodromy-matrix enclosures at two mesh levels |
| B4 certificates (T2–T5) | `a021_c4/b4_t*_*.py`, `.json` | The continuum-transfer binding-product, slack-semigroup, prefactor, and assembly certificates |
| E5 admission | `e5_admission.py`, `E5_NUMBERS.json` | The E5 linear-template admission |
| Shared interval library | `interval_lib.py` | Outward-rounded float64 (nextafter), interval transcendentals at 50-digit working precision |
| Artifact manifests | `ARTIFACT_MANIFESTS.json` (built by `build_artifact_manifests.py`) | Hashes of every artifact above |
| Batch-5 corrected runners | `wave_e_cod/src/run_intervention_v2.py`, `wave_e_edwards/src/run_intervention_v2.py` (+ `results/*_v2.json`, `*_v2.csv`) | The cod side's convergence-corrected infinite-horizon kernels (one-entry diff against the committed results, machine-verified) and the Edwards side's comparator-corrected retention rule (outputs value-identical — the inertness proof) |

Reproduction: `python3 research_program/validated_computations/<script>.py` regenerates the JSON certificates deterministically; `python3 reaudit/verify_validated_computations.py` re-verifies every pinned artifact and certified claim against the manifest (currently: all pass). The five Part II certificates were additionally re-executed by a second agent on a different toolchain (Python 3.13 / numpy 2.3.5 / scipy 1.17.1 / mpmath 1.3.0): Hopf, E5, and the monodromy JSON+NPZ hash-identical; Krawczyk and off-grid re-certify the same discrete-level claims (`batch 4/VALIDATED_COMPUTATIONS_RERUN.md`).

---

## 4. Content deliberately not in the drafted papers

**`research_program/pending_separate_publications_register.md`** — the register of journal-appropriate content intentionally not carried by the nine papers: Class A (pending companion publications, each with its own trigger), Class B (venue-decision routing — the B-1 F08/F10 theorem families, resolved to monograph-carried by the §5 decision memo), Class C (monograph-delegated source content), Class D (documentation flags). This register is the counterpart of the non-loss rule: nothing legitimate is silently stranded, and nothing is force-fitted into a paper where it does not belong.

---

## 5. Supporting decision documents

- **`research_program/paper2_venue_and_split_recommendation.md`** — the Paper 2 venue/split decision memo: no split; the full atlas to Set-Valued and Variational Analysis first (JMAA alternate), main text ≈14–16k words + the ≈27.2k full-proof expansion as electronic supplementary material; the pre-authorized 2A/2B split is the documented fallback only. The decision owner is the programme owner; this memo resolves nothing unilaterally.
- **`research_program/revised_optimal_publication_architecture_A001_A025.md`** — the five-paper publication architecture (objectives, per-paper questions and sources, the conditional Papers 6–7, the release-wave protocol).
- **`revised_sustainability_manuscript_v1.1.md`** — the monograph working preprint, second edition (§1.3): the citable record of the architectural kernel that the nine papers decompose into refereable units.
- **`BATCH5_JOINT_AUDIT_EVALUATION.md`** — the batch-5 joint evaluation: every finding from the four auditors, adjudicated with verification evidence; the rejected findings argued from the committed artifacts; the implementation map to the second editions; §6 records the residual pass (the completeness audit of the evaluation itself, the closed implementation-claim gaps, the newly dispositioned findings, and the content-loss scan against the owner's older drafts — no legitimate content loss found).

---

## 6. Verification battery (all commands run from the repository root)

| Suite | Command | Expected result |
|---|---|---|
| Packet integrity (first edition) | `python3 external_review_packet/verify_review_packet.py` | All pinned first-edition hashes match |
| Batch-5 editions + residual pass | `python3 reaudit/verify_batch5_editions.py` | PASS (139 checks: second-edition hashes, content checks, and the residual-pass invariants) |
| Validated computations | `python3 reaudit/verify_validated_computations.py` | PASS |
| Wave E reproduction | `REPO=$PWD python3 reaudit/verify_wave_e.py` | PASS (42/42 pinned hashes — first editions) |
| Wave E spec match | `python3 reaudit/verify_wave_e_spec_match.py` | PASS (36/36) |
| Concordance machine layer | `python3 reaudit/verify_concordance_rows.py` | PASS (409 rows, 25/25 sources, 354 closed) |
| Wave E consolidation | `python3 reaudit/verify_wave_e_consolidation.py` | PASS (superset audit) |
| Manuscript sweep | `python3 reaudit/verify_manuscript_sweep.py` | PASS |
| Findings reproduction | `python3 reaudit/verify_findings.py` | PASS |
| Joint disputes | `python3 reaudit/verify_joint_disputes.py` | PASS |
| Consistency suite | `REPO=$PWD python3 reaudit/verify_consistency.py` | Exactly the 13 documented defect-gone failures (C1×2, C2, C3, C4×3, C5, C6×2, C8×3) — the repaired-corpus baseline; no new failures |
| Paper self-checks | `python3 papers/paper<1–5>_*/verify_retained_rows.py` | PASS ×5 (first editions; the second editions' ledgers are unchanged in row content) |

Notes: `verify_wave_e.py` and `verify_consistency.py` default to a `repo/` layout; the `REPO=$PWD` override points them at this repository. The 13 consistency failures are the documented baseline of the repaired corpus (each is a check that a *defect is gone* — the script asserts the presence of pre-repair defect text, so failure = the defect is absent). The manuscripts under review (both editions) contain none of the internal audit vocabulary (verified by word-boundary scan: F4, build_panel.py, NOT CONFIRMED, manifest, independent rerun — zero occurrences); the mathematical term "gate" (the multiplicative effort gate (1−E/Emax) of the C3 effort law, the gated/ungated model variants, `DYN-C3-GATED`) is retained in Papers 2–5 as the correct technical term.

---

## 7. Reviewer's checklist

1. **Scientific status honesty:** every claim in every manuscript carries its source-declared status (theorem / conditional theorem / conjecture / counterexample / numerical result at its certification level); spot-check any three ledger rows against `PROOF_MANIFEST.md` and the concordance.
2. **No cross-system transfer:** the cod and Edwards results, and the A001/A002 theorem corpus vs the named C3/C4 systems, are never pooled; the seams are stated in the papers (Paper 3 §interface, Paper 4 §9).
3. **Reproducibility:** run §6; the two `REPO=$PWD` overrides are the only environment-specific steps. For the cod forecast paper, note the v2 availability section's environment-sensitivity record for the optimizer-based rows.
4. **Diff discipline:** the second editions exist so that every batch-5 correction is reviewable as a diff against the audited first editions — if a correction's rationale is needed, it is in `BATCH5_JOINT_AUDIT_EVALUATION.md` §2–3.
5. **The negative results are first-class:** the cod forecast ladder's persistence-wins verdict, the cod intervention's no-policy-retained certificate, and the Edwards institutional-threshold negative certificate are the programme's scored findings — check that the manuscripts state them as such.
6. **Content completeness:** the register (§4) lists everything deliberately outside the papers; if a reviewer believes substantive content is missing from the nine, it should be checked against that register before being reported as a gap.

**Contact point for the programme owner's decision log:** `worklog.md` (repository root) — the session-by-session record; `RELEASE_NOTES.md` — the v1.0 release record.

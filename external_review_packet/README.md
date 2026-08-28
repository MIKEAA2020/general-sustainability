# External Review Packet — General Sustainability Programme

**Prepared:** 2026-08-28 (after the terminology-restoration editorial pass). **Packet status:** frozen snapshot for external review; the pinned SHA-256 hashes identify exactly the reviewed texts. The repository (`https://github.com/MIKEAA2020/general-sustainability`) is the single source of truth; this packet is the curated entry point into it, not a second copy. Any revision of a listed artifact requires re-pinning (`external_review_packet/verify_review_packet.py`).

**How to use this packet.** Clone the repository at the packet's commit, read this file top to bottom, then read the manuscripts in the suggested order (§1). Every computational claim in the manuscripts is checkable against the committed artifacts (§3) by running the verification battery (§6). The programme's claim-status discipline — every claim carries its evidentiary status, and no status is ever promoted — is described in §2 and governs everything below.

---

## 1. The paper drafts under review

### 1.1 The five core papers (the assured core)

| # | Title (short) | Exact path | Words | Ledger | Status |
|---|---|---|---|---|---|
| 1 | General Theory and Research Architecture of Sustainability | `papers/paper1_general_theory/manuscript.md` | ≈9.6k | 21 rows + 1 cross-ref | **Final draft** |
| 2 | The Formal Mathematical Foundations of Sustainability: A Typed Theorem Atlas | `papers/paper2_theorem_atlas/manuscript.md` | ≈15.4k (≈27.2k at full proof expansion) | 89 rows | **Final draft** |
| 3 | Conserved Material Ledgers and Componentwise Depletion Diagnostics | `papers/paper3_material_ledgers/manuscript.md` | ≈14.1k | 52 rows + 2 seam | **Final draft** |
| 4 | Delay-Driven Capital Liquidation and Nonlinear Institutional Dynamics | `papers/paper4_delay_dynamics/manuscript.md` | ≈17.2k | 68 rows + 2 seam | **Final draft** |
| 5 | Sampled Governance, Empirical Identification, and Falsification Design | `papers/paper5_sampled_governance/manuscript.md` | ≈13.6k | 57 rows + 6 native | **Final draft** |

**What "final draft" means here:** content-complete at the scientific level — every planned theorem, application, ledger row, and camera-ready bibliography entry is in place; every paper's committed self-check (`papers/paper*/verify_retained_rows.py`) exits 0; the reproducibility and data-availability sections are in standard journal language. **What remains before submission:** the venue-format pass for each paper (journal template, length policy check, and — for Paper 2 — packaging of the full proof expansion as electronic supplementary material; see §5). Paper 2's venue decision memo (§5) recommends Set-Valued and Variational Analysis with JMAA as alternate.

### 1.2 The four Wave E papers (the scored empirical gate)

| # | Title (short) | Exact path | Words | System | Status |
|---|---|---|---|---|---|
| E1 | Northern cod 2J3KL — scored forecast ladder | `wave_e_cod/manuscript/wave_E_cod_forecast_ladder.md` | ≈3.8k | cod | **Final draft** |
| E2 | Northern cod 2J3KL — intervention analysis | `wave_e_cod/manuscript/wave_E_cod_intervention.md` | ≈1.6k | cod | **Final draft** |
| E3 | Edwards Aquifer (San Antonio pool) — scored forecast ladder | `wave_e_edwards/manuscript/wave_E_edwards_forecast_ladder.md` | ≈3.6k | Edwards | **Final draft** |
| E4 | Edwards Aquifer (San Antonio pool) — intervention analysis | `wave_e_edwards/manuscript/wave_E_edwards_intervention.md` | ≈1.7k | Edwards | **Final draft** |

There are exactly four Wave E manuscripts: two scored systems (Northern cod 2J3KL; Edwards Aquifer J-17), each with a forecast-ladder leg and an intervention leg. Each manuscript is pinned by SHA-256 in `PROOF_MANIFEST.md` Part VI; the pins match this packet's pins below. The two systems are never pooled and no result transfers between them (frozen specifications: `wave_e_cod/SPECIFICATION.md`, `wave_e_edwards/SPECIFICATION.md`; machine-verified by `reaudit/verify_wave_e_spec_match.py`, 36/36 checks).

### 1.3 Other manuscript files in the repository (not submission drafts)

| File | What it is | Status |
|---|---|---|
| `revised_sustainability_manuscript.md` | The monograph working preprint v1.0 (the architectural kernel, public and citable) | **Working preprint** — will be updated or superseded by the definitive monograph after the papers pass external scrutiny |
| `general_theory_of_sustainability_manuscript.md` | The flagship working manuscript of 14 August 2026 | Superseded (archival; v-history: v0.1 → v0.2 → this) |
| `general_theory_of_sustainability_v0.1.md`, `general_theory_of_sustainability_v0.2_comprehensive.md` | Earlier flagship versions | Superseded (archival) |
| `ms_part1.md`–`ms_part4.md` | Part files of the 14 August 2026 working manuscript | Superseded (archival) |
| `formal_supplement_A001_A002_A006_A010.md` | Formal supplement restoring A001/A002/A006/A010 material at source status | Archival input (content routed to Papers 1–5) |
| `revised_articles/` (A001–A025) | The corrected source articles — the inputs the papers were built from | Provenance layer (not for submission) |
| `uploads/` | The original source manuscripts as uploaded | Provenance layer |

No paper-shaped file exists outside this table and §1.1–1.2: the publication architecture (`research_program/revised_optimal_publication_architecture_A001_A025.md`) routes every source proposition to Papers 1–5, the conditional docket (Papers 6–7, gated on their own theorem-completion conditions), the negative register, or the monograph — verified row by row by the 409-row concordance (§2).

**Suggested reading order for a first review:** Paper 1 (the architecture and its discipline) → Paper 2 (the theorem atlas) → Papers 3–5 (the applications, each self-contained) → the four Wave E papers (the scored empirical gate) → `PROOF_MANIFEST.md` (the register of record). Reviewers focusing on one paper can read it alone: every paper carries a Minimal Working Realization of the canonical objects it needs and cites no sibling paper for a locally load-bearing definition.

---

## 2. The register of record

**`PROOF_MANIFEST.md`** (repository root) — every theorem with its honest status, every computation artifact with its SHA-256 and reproduction command, the Wave E support table (Part VI, pins all four Wave E manuscripts), the certification hierarchy for numerical claims (nominal → re-execution-verified → independently re-executed → certified), and the reproducibility/disclosure status. This is the document against which every claim in the papers is audited; the reaudit suites (§6) machine-verify its pins.

**The 409-row concordance** (`research_program/canonical_concordance_A001_A025.csv`) links every source proposition to canonical notation, assumptions, proof/evidence status, mapping type, destination paper, and monograph chapter; 354 rows are closed by dated full-source scientific passes (the closure scripts are committed under `research_program/`); the 27 open rows are exactly the three conditional-paper sources A021–A023 (Papers 6–7's gates), behind none of the nine manuscripts under review.

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

Reproduction: `python3 research_program/validated_computations/<script>.py` regenerates the JSON certificates deterministically; `python3 reaudit/verify_validated_computations.py` re-verifies every pinned artifact and certified claim against the manifest (currently: all pass). The five Part II certificates were additionally re-executed by a second agent on a different toolchain (Python 3.13 / numpy 2.3.5 / scipy 1.17.1 / mpmath 1.3.0): Hopf, E5, and the monodromy JSON+NPZ hash-identical; Krawczyk and off-grid re-certify the same discrete-level claims (`batch 4/VALIDATED_COMPUTATIONS_RERUN.md`).

---

## 4. Content deliberately not in the drafted papers

**`research_program/pending_separate_publications_register.md`** — the register of journal-appropriate content intentionally not carried by the nine papers: Class A (pending companion publications, each with its own trigger), Class B (venue-decision routing — the B-1 F08/F10 theorem families, resolved to monograph-carried by the §5 decision memo), Class C (monograph-delegated source content), Class D (documentation flags). This register is the counterpart of the non-loss rule: nothing legitimate is silently stranded, and nothing is force-fitted into a paper where it does not belong.

---

## 5. Supporting decision documents

- **`research_program/paper2_venue_and_split_recommendation.md`** — the Paper 2 venue/split decision memo: no split; the full atlas to Set-Valued and Variational Analysis first (JMAA alternate), main text ≈14–16k words + the ≈27.2k full-proof expansion as electronic supplementary material; the pre-authorized 2A/2B split is the documented fallback only. The decision owner is the programme owner; this memo resolves nothing unilaterally.
- **`research_program/revised_optimal_publication_architecture_A001_A025.md`** — the five-paper publication architecture (objectives, per-paper questions and sources, the conditional Papers 6–7, the release-wave protocol).
- **`revised_sustainability_manuscript.md`** — the monograph working preprint v1.0 (§1.3): the citable record of the architectural kernel that the nine papers decompose into refereable units.

---

## 6. Verification battery (all commands run from the repository root)

| Suite | Command | Expected result |
|---|---|---|
| Packet integrity | `python3 external_review_packet/verify_review_packet.py` | All pinned hashes match (this packet) |
| Validated computations | `python3 reaudit/verify_validated_computations.py` | PASS |
| Wave E reproduction | `REPO=$PWD python3 reaudit/verify_wave_e.py` | PASS (42/42 pinned hashes) |
| Wave E spec match | `python3 reaudit/verify_wave_e_spec_match.py` | PASS (36/36) |
| Concordance machine layer | `python3 reaudit/verify_concordance_rows.py` | PASS (409 rows, 25/25 sources, 354 closed) |
| Wave E consolidation | `python3 reaudit/verify_wave_e_consolidation.py` | PASS (superset audit) |
| Manuscript sweep | `python3 reaudit/verify_manuscript_sweep.py` | PASS |
| Findings reproduction | `python3 reaudit/verify_findings.py` | PASS |
| Joint disputes | `python3 reaudit/verify_joint_disputes.py` | PASS |
| Consistency suite | `REPO=$PWD python3 reaudit/verify_consistency.py` | Exactly the 13 documented defect-gone failures (C1×2, C2, C3, C4×3, C5, C6×2, C8×3) — the repaired-corpus baseline; no new failures |
| Paper self-checks | `python3 papers/paper<1–5>_*/verify_retained_rows.py` | PASS ×5 |

Notes: `verify_wave_e.py` and `verify_consistency.py` default to a `repo/` layout; the `REPO=$PWD` override points them at this repository. The 13 consistency failures are the documented baseline of the repaired corpus (each is a check that a *defect is gone* — the script asserts the presence of pre-repair defect text, so failure = the defect is absent). The manuscripts under review contain none of the internal audit vocabulary (verified by word-boundary scan: F4, build_panel.py, NOT CONFIRMED, manifest, independent rerun — zero occurrences in all nine); the mathematical term "gate" (the multiplicative effort gate (1−E/Emax) of the C3 effort law, the gated/ungated model variants, `DYN-C3-GATED`) is retained in Papers 2–5 as the correct technical term.

---

## 7. Reviewer's checklist

1. **Scientific status honesty:** every claim in every manuscript carries its source-declared status (theorem / conditional theorem / conjecture / counterexample / numerical result at its certification level); spot-check any three ledger rows against `PROOF_MANIFEST.md` and the concordance.
2. **No cross-system transfer:** the cod and Edwards results, and the A001/A002 theorem corpus vs the named C3/C4 systems, are never pooled; the seams are stated in the papers (Paper 3 §interface, Paper 4 §9).
3. **Reproducibility:** run §6; the two `REPO=$PWD` overrides are the only environment-specific steps.
4. **The negative results are first-class:** the cod forecast ladder's persistence-wins verdict, the cod intervention's no-policy-retained certificate, and the Edwards class-grounded declination of a numerical win are the programme's scored findings — check that the manuscripts state them as such.
5. **Content completeness:** the register (§4) lists everything deliberately outside the papers; if a reviewer believes substantive content is missing from the nine, it should be checked against that register before being reported as a gap.

**Contact point for the programme owner's decision log:** `worklog.md` (repository root) — the session-by-session record; `RELEASE_NOTES.md` — the v1.0 release record.

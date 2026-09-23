# Viable-Selector Paper — v1 Addendum (disposition record)

**Version:** `paper2_viable_selector_v1` (new lineage — the successor's spine).
**Naming note:** the `paper3_*` prefix was rejected at push time — the repository suite already has a `paper3_material_ledgers` lineage (the original five-paper programme); the unification paper belongs to the obstruction-calculus programme and is numbered within it (`paper2_obstruction_calculus_*`, `paper2_companion_*`, `paper2_viable_selector_*`).
**Title:** *The Viable Selector: A Unifying Framework for Obstruction Certificates under Incomplete Observation*.
**Implements:** Track C items **C1–C2** of roadmap v3–v6, per the owner directive to build the successor spine (C3's five-layer architecture and D1's stochastic theory remain sequenced after this paper).

## 1. Content → source mapping

| Roadmap item | Where in v1 |
|---|---|
| C1 (four one-step mechanisms as specializations of the viable selector under information; timing as blind-window predecessor emptiness; fibre criterion connected but **not** a policy-viability obstruction) | §5 (specializations), Proposition 4 (timing/predecessor, with the load-bearing class declaration verified), Proposition 5 (label selection, with the certification-limit caveat kept explicit), §7 (the discipline: form unified, cause not) |
| C2 (unified meta-theorem: admissible ∧ implementable ∧ tube-safe ∧ recursively viable ⇒ impossibility of the class; strengthening lemmas) | §3 Theorem 2 (meta-theorem + monotone soundness + certificate semantics as dual witnesses), Corollary 1 (policy-class obstructions = the CE trap), §4 Propositions 3–5 (the ladder; timing-as-predecessor-emptiness; certification-as-label-selection) |
| Doc-source scaffolding | Theorem 1 (finite-horizon exactness of the recursive correspondence) + the measurable-selection qualification (Remark 1, citing Bertsekas–Shreve) — the source's own central object and its "important selector qualification", formalized |
| §12/§13 of the source (over-unification warning; strongest defensible claim) | §7 verbatim in spirit: dynamic exit not epistemic; fibre not policy-viability; CE trap not necessarily informational; strongest claim adopted in the source's own measured form |

## 2. Verification record (`paper2_viable_selector_v1_verify.py`, stdlib, exact rational/integer)

**7/7 checks pass** on the companion papers' worked systems:
- **V1** static intersection (two-floor): common admissible [0,1] nonempty, common safe empty — the common-action certificate *is* Γ^B = ∅.
- **V2** label selection (two-floor index + 2-D aggregate): crossing fibre Λ = ∅, safe fibre Λ = {1}; certainly-safe readings exactly I ≥ 7/5 (7 grid cells).
- **V3** ladder (two-patch): A_tube(·,2) ⊆ R_V^B ⊆ U^B everywhere, **strict at 5 states** (e.g. (1,2): tube empty vs safe {1}), tight at 4.
- **V4** recursive identity (two-patch audit): Γ_N correspondence recursion ≡ belief-kernel recursion on all six audited beliefs; singleton Γ_8 nonemptiness ≡ full-information kernel.
- **V5** timing-as-predecessor (hidden-regime, 48 cells): hold-class blind predecessor nonempty ⟺ z₀ ≥ 1+k (the viability boundary); unrestricted class ⟺ z₀ ≥ 2 for k ≥ 2 (declaration load-bearing).
- **V6** policy class (CE instance): corrected drift identically 0 on [1,2] vs CE drift ≥ 21/100 ⇒ unrestricted correspondence nonempty, class-restricted empty.

Fixes during verification: V1 initially conflated admissible with safe sets; V2's Λ returned {0,1} on crossing fibres instead of ∅ (the correspondence is empty when labels differ); one grid-count slip (7 cells, not 14). All corrected before build; final 7/7.

## 3. Build and probes
- Tectonic 0.15.0; `main.pdf` 131,797 B, **4 pp** (two-column letter; no figures/table beyond Table 1).
- pymupdf probes: 0 unresolved `??`; all theorem/proposition titles, Table 1, the discipline section, the outlook, declarations, and references verified present.

## 4. Files
- `paper2_viable_selector_v1.tex` / `.pdf`; `paper2_viable_selector_v1_verify.py`
- `paper2_viable_selector_v1_source.zip` (README + tex + pdf + verify script, 4 entries)
- `paper2_viable_selector_v1_source.zip` (README + tex + pdf + verify script, 4 entries)
- Roadmap: v7 records C1–C2 drafted; C3 and D1 next.

## 5. Status after this ship
Track C: **C1–C2 complete (this paper)**; C3 (five-layer successor absorbing D2/D3/D6) and **D1 (belief-state safety-value theory — the §8 outlook, seeded by the v47 instance and previewed in this paper's closing section)** are the next items per sequencing. Papers 1–2 submission-ready pending owner venue decisions; paper 3 is the spine document for what follows.

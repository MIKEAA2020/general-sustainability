# Paper 2 — v49 Addendum (selector-principle consolidation section)

**Version:** `paper2_obstruction_calculus_v49_Automatica_routes` (main only; supplementary unchanged at v46).
**Base:** v48 (pushed `aa2debc`). **Scope:** insertion of one consolidation section (§8, "The Selector Principle, Dual Certificates, and Monitoring Adequacy") that organizes the existing certificates of §3 around the recursively viable selector, states the exactness class of the strong-duality converse, and records the monitoring-adequacy reading with the corrected (non-strict) delay identity. **No new theorem is claimed; no existing certificate is modified.**

## 1. What changed

| # | Change | Detail |
|---|--------|--------|
| C1 | New §8 | Four paragraphs: the selector Γ_N (display, split alignment) = the recursion of Thm 1 with the one-step factors of the ladder Prop; dual witnesses by factor (seven, each a pointer to an existing §3/§4 object); exactness class (weak duality unconditional; strong duality exactly in the one-step/static/delayed classes; converse = Open Problem, open; causes not unified); monitoring adequacy (partition-form fibre criterion; four design rules as identities on the audited systems, with the boundary-viable non-strict timing identity T_obs ≤ σ*(B0) = z0 − 1). |
| C2 | Renumbering | Old §8 (case study) → §9; §9 (probabilistic) → §10; §10 (conclusion) → §11. Four cross-reference updates: §1 roadmap sentence ("Sections 7–10 … Section 11 concludes"), the timing-certificate checkability note ("instance of Section 9"), the belief-state worked-instance note ("audit system of Section 9"), and the conclusion's completion enumeration ("Four elements complete the picture"). |
| C3 | Layout repairs | (a) tab:patch (two-patch audit) wrapped in `\resizebox{\columnwidth}{!}{…}` — this table carried two overfull warnings (20.6 pt and 25.3 pt) already in the shipped v48 build; v49 is the first zero-overfull edition of the main text. (b) The new Γ_N display uses a `split` environment (the one-line form was 57 pt overwide in a column). |

## 2. Content provenance (every §8 statement is a pointer)

| §8 statement | Source (already shipped) |
|---|---|
| Selector Γ_N, recursion, ladder | §3.1 Theorem (finite-horizon soundness/completeness); ladder Proposition (§3.6); selector principle Proposition (§2.4) |
| Common-action witness + Farkas + m+1 sparse | §3.2–3.3 Theorem/Proposition (v46 LP instantiation) |
| Tube witness | uniform-margin Proposition (§3.5) |
| Timing witness, σ* threshold | delayed-information Theorem + threshold Remark (§3.7); closed form in §9 case study |
| Finite-time exit witness | exit Theorem + comparison Remark (§3.8) |
| Epistemic-emptiness witness | minimal-construction Proposition (§3.9) |
| Fibre witness + certainly-safe set | fibre Proposition + Corollary (§4) |
| Class-restriction witness (CE trap) | CE-trap Remark (§4) |
| Strong-duality scoping | one-step Theorem + static-reduction Theorem + delayed-class coverage Remark (§7); Open Problem (dynamic) |
| Partition-form adequacy, three two-point codices | monitoring companion (`monitoring_design_v3`, rules E1–E9) |
| Non-strict delay identity, boundary viable | monitoring v3 check E9; concordance companion (`paper2_selector_concordance_v1`, check C1: zero mismatches on the 48-cell grid; strict form fails exactly at (z0, T_obs) = (2, 1)) |
| Consolidated audited counts | concordance companion (checks C1–C8) |

## 3. Build record

19 pages; zero errors; **zero overfull warnings**; all internal references resolve; 21/21 PDF content probes pass (new section present; renumbering complete; non-strict identity present; boundary case stated; "Four elements" conclusion enumeration; inherited Declarations block unchanged).

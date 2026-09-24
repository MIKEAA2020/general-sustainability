# Worked Systems, Edition 6 — Addendum

**Editions:** supersedes `paper2_worked_systems_v5` (v1–v5 retained). All counts, tables, figures, and identities are unchanged; this edition is a definitional-and-exposition revision driven by the second external-audit round (adjudication: `paper2_worked_systems_round2_joint_audit_v1.md`).

**Delta (v5 → v6):**

- **The no-repeat protocol's register semantics are now part of the definition (§2):** "one previous-action register per information state, shared by all fibres, not one per branch" — the semantics implemented by the verification scripts, under which the alternation-forced pair's two branches collide at the register at step two. (Under a per-branch register the pair would be codex-viable; stating the audited semantics closes the external auditor's "name, definition, Table 1 cannot all be true" objection.)
- **"Boolean product" retired for the kernels:** the classes are a two-by-two product of aggregation level and protocol (abstract, §4, Figure 1); the kernels have incomparable middle cells, with the class join's kernel exceeding the middle-kernel union by exactly the alternation-forced pair (as printed since v4).
- **The decentralized protocol sentence corrected:** the audited protocol is memoryless and decentralized — no agency observes the belief, the other agency's observation, or anything like common knowledge (the "local memory with delay" phrasing is retired; the delayed variant lives in the lineage scripts).
- **Table 2's reading direction made explicit** ("agency 1's votes are the row labels, agency 2's the column labels") after an external auditor misread agency 2's column headers as agency 1's rows and proposed a "correction" (1211 → 1121) that would have introduced an error; the script-certified product stands.
- **ℓ1-normalized stated at every appearance** of the (1/2, 1/2) pair (abstract, Table 5 caption, §10, Figure 5), keeping the normalized margin 3/50 distinct from the cap-sum shortfall 3/25.
- **Intro range split** (shared system: Sections 3.–5. and 7.–8.; timing grid: Section 6.), the **keywords line** boxed against a mid-word column break, and the **verification-methods citation corrected** to the companion papers (Abaee, 2026b).

**Verification:** `paper2_worked_systems_v6_verification.py` 21/21 (chain 57/57) with five new text needles (register semantics, memoryless protocol, two-by-two product, caption direction, ℓ1-normalization). Build: 6 pages, zero overfull.

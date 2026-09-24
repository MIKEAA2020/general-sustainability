# Worked Systems, Edition 5 — Addendum

**Editions:** supersedes `paper2_worked_systems_v4` (v1–v4 retained). The audit frame, the master table, and all tabulated results are carried unchanged.

**Delta (v4 → v5):**

- **Figure 5 (static duality) redesigned** per owner directive: the legend now sits in the open wedge between the two drift rows (clear of both lines and of the min envelope), and the value annotation is two lines — "−1/10: max–min = min–max" over "Farkas (1/2, 1/2) constant" — both inside the whitespace, superimposing nothing.
- **Two wording sharpenings** from the external-audit round (full adjudication in `paper2_worked_computational_joint_audit_v1.md`): "nine **safe** states generate C(9,2) = 36 … (28 of the pairs full-information-viable; column F of Table 1)" — the safe/viable distinction made explicit; and the alternation-forced sentence now states the exact mechanism (the no-repeat protocol's single previous-action register must serve both branches; the second branch's required next action is forbidden once the first branch's choice occupies the register — collision at step two, the earliest possible step).
- New exact fact recorded this round (adjudication of the decentralized-causality critique): the maximal guaranteed basin of a single law pair is 6 of 36, attained by 12 law pairs — equal to the decentralized kernel; the 12-count is single-law causal. (Exact check shipped in the computational v2 verification.)

**Verification:** `paper2_worked_systems_v5_verification.py` 21/21 (chain 57/57), with the added "single previous-action register" needle. Build: 6 pages, zero overfull.

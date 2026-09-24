# Computational Viability Certification, Edition 2 — Addendum

**Editions:** supersedes `paper2_computational_certification_v1` (v1 retained; supplementary re-issued in step as v2 with matching equation numbers). All scientific content — the bridge theorem, the instance, the campaign, the rank separation, the erosion and oracle identities, the library — is unchanged; this edition's deltas are expositional and verification-side, driven by the external-audit round (full adjudication in `paper2_worked_computational_joint_audit_v1.md`).

**Delta (v1 → v2):**

- **Numbered section headings** in the house style; every cross-reference now prints a true number (the eleven empty "Section )" instances are gone — build-verified).
- **Sequential equation tags:** (10)→(9), (16)→(10), (15)→(11), (13)→(12), (14)→(13); (1)–(8) untouched, so the campaign scripts' displayed reference "LP (5)" remains valid; S1 v2 re-issued with the matching numbers.
- **Proof outline of the main theorem** added to the main text (outer moment approximation ⇒ the lower bound; piecewise-constant scenario realization charged the three error terms ⇒ the upper bound); the complete proof remains in Supplementary S1.
- **Pooling-weights note:** the certificate weights (3/8, 5/16, 5/16) are proved in-text unique on the equal-{2,3} family (3/8 = 1 − 2·5/16) — closing the external auditor's "weights" objection, which was refuted against the artifact (both v1 and v49 already carried these weights).
- **Oracle-recourse exactness disclosure** in the scope: exactness in the instance belongs to the complete revelation at τ, not to the (sound, incomplete) relaxation.
- **Library scope declared:** viacert is not a reimplementation of the bridge theorems; consolidation of the campaign programs as a `viacert.continuous` module is recorded as the library's next step.
- **Verification extended 13 → 15 checks:** new exact checks ship the adjudication results — (E-basin) the decentralized kernel of the audited system is single-law causal (max guaranteed basin 6 of 36 = |kernel|, attained by 12 law pairs); (E-weights) the pooling family sums to one, pools the kernel to zero, and reproduces Γ(τ) = τ − 7/50 with Γ(0.2) = 0.06.

**Verification:** `paper2_computational_certification_v2_verification.py` 15/15 — chain (record 51/51 re-run this round; campaign 9/9; viacert selftest 12/12), the two new checks, the mesh-law recomputation, and the needle set including the new passages. Build: 6 pages main + 3 pages supplementary, zero overfull.

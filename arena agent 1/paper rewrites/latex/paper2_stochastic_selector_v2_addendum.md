# paper2_stochastic_selector_v2 — addendum

**Lineage:** `paper2_stochastic_selector` (Track D1). This is the second
edition of the stochastic-selector paper, produced by the joint audit of
the first edition (two owner-supplied reviews, adjudicated jointly); the
full dispositions are in
`paper2_stochastic_selector_joint_audit_v1.md`. The first edition's
artifacts are retained unmodified.

**Changes (v1 → v2).** (1) Policy-class parameter made explicit
throughout the value theory (`V^Π_k`, `A(Π)`, blind-window segment form).
(2) Model boundary cases completed: state space `V ∪ {⊥}` with total
transition rows, absorbing `⊥` with observation `y_⊥` (observation laws
sum to one), masked witnesses (`α(⊥) = 0`). (3) Selector definition
repaired: attaining (argmax) set separated from the value-one level
`S^Π_k`; the first edition's nonemptiness sentence corrected.
(4) Deterministic degeneration restated as a change of Bellman operator
(robust operator; new remark). (5) `W_k` (k-step robust kernel in belief
space) defined; Proposition 3(ii) repaired. (6) Theorem 2(c) restated
(witness-family change exactly at z0 = 2 for k = 1, at z0 = 1 + k for
k ≤ T_obs — not at z0 = 2 for k = 2; parameter jumps at
z0 = 1 + min(k, T_obs); "kink" reserved for the belief-space PL value).
(7) Theorem 2(e) sharpened and verified: the classes coincide at k = 1
and differ exactly on the timing cells for k ≥ 2; unrestricted value 1 on
{z0 ≥ 2} for every k ≥ 1 (both audits had stated k ≥ 2). (8) Class-scope
remark: the timing obstruction is hold-class content; "adaptive" avoided
for blind windows. (9) Vacuous-indicator remark. (10) Broken references
repaired (exactly two rendered instances; the audits' counts were
slightly off; the defect real). (11) Section 6 lists all fifteen check
families with a complexity note; declarations updated (v2 script,
fifteen families, repository phrasing, AI disclosure covering both
editions).

**Verification.** `paper2_stochastic_selector_v2_verify.py` — fifteen
check families (S1–S15), 15/15 passing, exact rational arithmetic,
stdlib only, deterministic; extends the first edition's ten-family record
and absorbs both audits' computations (oscillation identity, unrestricted
table, jump loci, model completeness, selector split, dimension padding).

**Build.** Tectonic 0.15.0: zero overfull boxes (two overflowing displays
in the first draft repaired: the row-split display and the masked-backup
display, the latter by verbal masking boundary condition); 4 pages; 4 pp
post-build probes pass (no broken reference, new terminology present,
declarations intact).

**Defects found during this pass (before ship).** (i) The new check S8's
own first draft asserted "V_1 = 1/2 everywhere" for the unrestricted
class; computation refuted this (a single action saves both branches at
z0 ≥ 2) — the corrected check then sharpened Theorem 2(e) itself.
(ii) Two overfull displays in the first build (fixed as above; final
build zero). (iii) Dead placeholder code in the first draft of the v2
script (S6, S14) removed before ship.

**Status.** Shipped to `latex/` (tex + pdf + verify + this addendum)
via cp + cmp; source zip
`zips_archive/paper2_obstruction_calculus/paper2_stochastic_selector_v2_source.zip`
(4 entries); pushed with the joint audit record and roadmap v11.

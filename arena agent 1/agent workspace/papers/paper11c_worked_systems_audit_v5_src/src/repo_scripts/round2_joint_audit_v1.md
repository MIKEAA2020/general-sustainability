# Joint external-audit adjudication, round 2 — worked systems (v4/v5/v6)

**Round:** 2026-09-24, second external-audit file supplied by the owner (two auditor reports). **Audited edition:** both reports address v4-era text (auditor 1's report is byte-identical to its round-1 submission; auditor 2 re-audited with fresh eyes). **Method:** unchanged — verify-before-fix on the artifacts, fixes as new editions only; this round ships `paper2_worked_systems_v6` (from v5).

## A. Auditor 1 (report identical to round 1)

The eight findings were adjudicated in round 1 (`paper2_worked_computational_joint_audit_v1.md`); re-checked against the current editions, nothing new arises:

| # | Round-1 verdict | State in v5/v6 |
|---|---|---|
| 1 Benchmark "category error" | Refuted (public cap schedule; paper claims no epistemic conflict at Y = 6) | Unchanged; Table 5 states cap-sum shortfall 3/25 and normalized margin 3/50 separately |
| 2 Timing floor "contradiction" | Refuted (⌊z₀−1⌋ = z₀−1 at all 48 tenths; strict form fails exactly at (2.0, 1)) | Unchanged |
| 3 "Nine viable states" | Upheld | **Fixed in v5** ("nine safe states … 28 full-information-viable"); auditor 2 independently concurs |
| 4 Decentralized non-causality | Fairness demand upheld; count refuted-fine via the new exact result (max guaranteed basin 6 of 36 = the kernel, 12 laws) | Shipped as the E-basin check in the computational v2 verify |
| 5 Regime "vacuity" | Judgment (boundary-stating is content) | Unchanged |
| 6 No-repeat "backwards" | Partially upheld (clarity) | **Fixed in v5** (register sentence); **v6 adds the definitional statement** (shared register in §2) |
| 7 "Trivial arithmetic" | Judgment | Unchanged |
| 8 Citation monoculture | Partially upheld; scheduled (verified references only) | Owner-side/deferred |

Because auditor 1's report shows no engagement with the v5 fixes, its two upheld items are treated as already-actioned and its remaining claims stand adjudicated as in round 1.

## B. Auditor 2 (new, substantive; positive verifications recorded)

**Independently confirmed this round (recorded as strengthening evidence):** the shared system's definition and dynamics; the R(x) values R((1,2)) = {1}, R((2,1)) = {2}, R((2,2)) = {1,2}, R((3,1)) = {2}; the delay identity with the single strict-form failure at (2.0, 1); the CE labels (uncorrected s/5 + 1/100, min 21/100; corrected 0); the lattice arithmetic — meet of middles = institutional, class join with kernel remainder exactly {(1,2),(2,1)}, 28 − 12 = 16 decentralized losses; the design rules as identities; the strong-duality scoping; the Helly triple and the ℓ1-normalized two-floor pair.

**Findings adjudicated:**

| # | Finding | Verdict | Action |
|---|---|---|---|
| B1 | "Nine viable states" | Upheld (as in round 1) | Already fixed in v5; v6 carries it |
| B2 | Table 2 row "1211" is a misprint for "1121"; "until corrected, Table 2 does not certify the 16-law claim" | **Refuted against the artifact.** 1211/1212/2211/2212 are the *column headers* — agency 2's laws, whose encoding (l(z=0), l(z=1), l(z=2), l(z=3)) = (1,2,1,1) etc. has exactly the required forced votes (2 at z = 1, 1 at z = 2). The *rows* are agency 1's: 1121, 1122, 2121, 2122. The auditor read agency 2's columns as agency 1's rows. The 16-law product is script-certified from the dynamics (verify check M7). Replacing 1211 by 1121 would *introduce* an error (1121 votes 1 at z = 1 — wrong for agency 2). | v6 makes the reading direction explicit in the caption ("agency 1's votes are the row labels, agency 2's the column labels") |
| B3 | No-repeat vs alternation: "name, definition, and Table 1 cannot all be true" | **Partially upheld — as a definitional under-specification, not a misclassification.** The audited semantics (implemented in the chained scripts, which produce 24/26/25/28) threads a *single previous-action register per information state*, shared across fibres; under that semantics each branch alternates but the two branches' requirements collide at step two — the earliest possible step — so the pair is excluded. Under a per-branch register the pair *would* be codex-viable; the paper must (and now does) state which semantics is audited. | v6 §2 definition: "one previous-action register per information state, shared by all fibres, not one per branch" |
| B4 | "Boolean product" overstates the kernels (union 27 ≠ full 28) | Upheld | v6: all four occurrences reworded — the *classes* are a two-by-two product; the *kernels* have incomparable middle cells (the 27 + 1 reading was already printed) |
| B5 | Production: keywords hyphen break; §8 broken sentence; §12 stub; code path/archive ambiguity; intro range lumps §6 into the shared system | Mixed. §8 sentence: **refuted** (complete: "an adversary chooses at the end of step t−1 the regime realized at step t" — the auditor dropped the verb). Keywords break: **upheld (cosmetic)** → mbox fix. Intro range: **upheld** → v6 reads "Sections 3.–5. and 7.–8." for the shared system, timing grid named separately. §12 stub: declared forward scope, kept. Code path/DOI: owner-side standing item | v6 fixes keywords + intro range |
| B6 | H = 12 two-horizon verdict never justified; "local memory with delay" misleading; deadlock u = 0 should be tied to this dynamics | Partially upheld. The two-horizon verdict is attributed to the seed's Theorem 1 in §2 (attribution, not derivation — kept). "Local memory with delay": **upheld** — the audited protocol votes on the current own coordinate and is memoryless; the delayed variant lives in the lineage scripts, not this paper → v6 rewords ("memoryless and decentralized — no agency observes the belief, the other agency's observation, or anything like common knowledge"). Deadlock: already declared explicitly in §5 | v6 rewords the memory sentence |
| B7 | State "ℓ1-normalized" at first appearance; do not let "the" Farkas pair float between instances | Upheld | v6: ℓ1-normalized at all five appearances; the Helly triple and the two-floor instance are already distinct in the text; 3/25 vs 3/50 were separated in v5 |
| B8 | "What the paper still is not" (no calibrated map from the 9 cells to 2J3KL; not a library; not a completeness theorem) | Consistent with the paper's own scope; "bind = instantiate, not prove" accepted as the reading | No edit |

**Structural advice** ("do not keep D4/D7/D8/D11/D13 as separate preprints; this audit subsumes their non-recycled numbers"): owner-side lineage management, consistent with the standing consolidation policy; the seven per-system verification scripts remain chained in the master verify (57/57, re-run green this round).

## C. Round ledger

- Shipped: `paper2_worked_systems_v6` (verify 21/21, chain 57/57; zero overfull; 6 pp) — edits: §2 shared-register definition; four "Boolean product" rewordings; intro range split; §5 memoryless-decentralized protocol sentence; ℓ1-normalized (5×); Table 2 caption direction sentence; keywords mbox; methods citation corrected to the companion papers (2026b).
- Refuted with evidence: the Table 2 "misprint" (would have introduced an error); the §8 "broken sentence".
- Carried: all round-1 verdicts (no re-litigation succeeded).

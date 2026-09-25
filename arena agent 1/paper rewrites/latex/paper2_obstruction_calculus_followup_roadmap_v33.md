# Paper 2 — Obstruction Calculus: Follow-up Roadmap (v33)

**Subject:** *An Obstruction Calculus for Viability under Incomplete Observation*
(current: `paper2_obstruction_calculus_v49_Automatica_routes.tex` + supplementary v46).

**v33 changes:** **Round 14 — external-audit adjudication round** (audit attached
as `uploads/decision.txt`; note: both of its lists number from 2 — no item 1
exists in the file; nothing else was silently dropped). Verdicts:

| Finding | Verdict | Completion |
|---|---|---|
| Solid section (controls, self-correction, P5 re-adjudication, scaling structure, v5 bundle, strategic scoping) | **confirmed** — checked against the artifacts | no action |
| F2: P5 (a) vs (b) needs a charter-based memo | **ACCEPTED** | `paper2_p5_decision_memo_v1.md` shipped: charter quotes (applications note L4; residual ledger R9/R12; board wording) + the E1 v50 §3.10 review-timing evidence; **recommendation (a)** (designate E1 v50 as P5), (b) recorded as a future applied-viability build; owner confirms |
| F3: formalize the scaling lemma; scope it; z3 stays a cross-check | **ACCEPTED AND EXCEEDED** | `paper2_exact_belief_computation_v3.tex`: general-m pair-sum lemma + Cesàro proof + corollary h ≤ m − 5/2; all remaining proofs completed (7 proof environments); **NEW scope remark with sharpness witness** — the Hamming-ball construction r*(m) = ⌊(2m−5)/4⌋ (m=3..8 verified; m=5 witness: the 6-cell radius-1 ball survives from the floor's edge; m=7: the 29-cell radius-2 ball) proves the pairs-only census is exactly m = 4; m ≥ 5 classification explicitly open. Verify **19/19** (chains v2 → v1); 4 pp, overfull 0 |
| F4: parallel-edit race is a process bug; add the rule + pre-checks | **ACCEPTED** | rule recorded (single-writer sequential edits; exactly-once anchor assertions; verifier before build) in the v3 addendum; all round-14 edits executed under it |
| F5: recorded constructions unchanged; z3 outside the chains | **CONFIRMED — no change** | the m=5/m=7 witnesses are certified by exact arithmetic; no solver entered any chain |
| Action 5: board update; P1 venue decision visible | **DONE** | board below; P1 flagged as the critical-path non-technical blocker |
| Action 6 | **DONE** — no change | — |

**What the audit missed (strengthening):** (i) F3 asked for scoping "to the
cube or general" — the true answer is a third thing: the *instrument* is
general (h ≤ m − 5/2 with these drift constants), the *pairs-only
classification* is m = 4-sharp, and at m = 5 the structure jumps (ball of
radius 1, from every level) — a stronger and more useful result than either
option the audit offered; (ii) the audit's Q2-analog for completeness was
understated: edition 2 had **six** condensed/implicit proofs, not one — all
fixed in v3; (iii) the audit's own numbering lacks an item 1 in both lists
(flagged, not reconstructed).

## Flagship board (v17 architecture; status updated)

| # | Flagship | Latest | Status |
|---|----------|--------|--------|
| P1 | Obstruction calculus | v49 + supp v46 | shipped, frozen; **owner venue decision = next non-technical blocker** |
| P2 | Computational + library | comp v9 + S1 v6 + `viacert`; **exact belief computation v3 (19/19, proofs complete)** | current |
| P3 | Probabilistic sufficiency | v5 (28/28); v1–v4 frozen | current |
| P4 | Worked-systems supplement | ws v10 | current, scan-clean |
| P5 | Applied | **decision memo v1 shipped — owner to confirm (a) E1 v50 designation [recommended] or (b) obstruction-applied build** | memo stage |

Seeds byte-frozen: `paper2_stochastic_selector_v2*`, `paper2_belief_state_v2*`,
`hidden_parameter_learning_v1*`, ebc v1–v2 (chained seeds). Recorded
constructions (unchanged): cross-tool comparison study (z3 5.1.0 agreement
datum), conic/stochastic P2 edition citing P3's `prop:dr`, Epistemic-HJBI
conjectures, Lean (deferred by decision).

## Build-order status

1. P4 ws v10 — done.
2. P2 — comp v9 + S1 v6 + `viacert` + ebc v3 — done.
3. P3 v5 — done (round 13).
4. P5 — decision memo shipped; owner confirmation pending.
5. Supersession banners — map v3 current.

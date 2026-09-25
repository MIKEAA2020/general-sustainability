# Programme review — execution record (round 25)

**Date:** September 25, 2026. **Parent:** `programme_causal_coherence_and_crossstrengthening_review_v1.md` (owner-directed execution of its recommended sequence, items 1–5). **Shipped editions:** minimax v6 (31→34/34 with new needles; 5 pp), comp v14 (48/48; 11 pp), ws v14 (54/54, chained 57/57; 11 pp), E1 v55 (47/47; 36 pp) — all build gates green (exit 0, zero overfull, zero halts, no "??", `SOURCE_DATE_EPOCH`-pinned rebuilds byte-identical) and all verifier re-runs green. **New computational artifacts:** `certificate_exchange_v1.py` (+2 archived certificates), `paper2_coupling_dr_interpolation_check_v1.py` (6/6), `paper2_ebc_comp_beliefcell_joint_check_v1.py` (5/5, 295 probes).

## Item 1 — repairs (D1–D7)

- **D1 (minimax bibliography):** References section added — 2026a = ARV (Zenodo DOI), 2026b = P1 (submitted), 2026c = ws (submitted), 2026e = P3 (submitted); every author-year mention now resolves.
- **D2 (duplicated caps theorem):** split ownership executed — minimax `thm:benchmark` cites ws for the fibre criterion and radius bounds, owning "the two-stock derivation and the fibre-width formula"; ws §benchmark cites minimax for the derivation, owning "the per-aggregate audit and the radius reading". Symmetric, one clause each; constants untouched.
- **D3 (comp's wrong companions):** comp's library identities now cite "(Abaee, 2026b, 2026c)" (P1 + ws); the rank caveat cites ws; ws and minimax added to comp's bibliography.
- **D4 (stale code pointer):** minimax's code availability now names `minimax_dual_certificates_v6_verify.py`; "all eight check families" → "every check family".
- **D5 (E1 pointers and stubs):** replication block now names the archived `wave_e_cod/src/` paths (one command per line — the long `&&` chains were the round's only overfull source, cleared to zero); CRediT and Funding stubs completed.
- **D6 (author-year keying):** minimax re-keyed to the family table (2026a = ARV, 2026b = P1, 2026c = ws, 2026d = comp, 2026e = P3, 2026f = ebc, 2026g = minimax); E1's list is self-contained as verified (its 2026a/b/c = Edwards/periodic-review/ARV; P1 added as E1's 2026d). Verified during execution: E1's earlier "2026c" mention resolves (ARV) — no dangling citations existed.
- **D7 (minimax register/markup):** the proof-history passage ("the proposed argument … is the corrected one") deleted; "The corrected object" → "The envelope formulation"; four "corrected formulation/object" phrases replaced by content names (the tex now contains zero occurrences of "corrected"); the doubled section heading split; the AI declaration gained the family responsibility sentence.
- **D8:** carried (unchanged, queued).

## Item 2 — S2 certificate exchange (executed)

`certificate_exchange_v1.py`: schema-strict JSON reader, exact rational validation of two kinds (Farkas row witnesses; measure-dual atoms), independent of both papers' model builders. Archived certificates: `comp_three_branch_v1.json` (λ, η_j on F/f, pooling identity, β+e, interval-weight sum → margin −3/100 recomputed exactly) and `minimax_caps_v1.json` (μ\* = (1/2,1/2) on the floor atoms, pair_min consistent with the demand floor → margin −3/50 recomputed exactly): 18 checks, all valid; tamper probes (flipped margins) rejected with exit 1. The parser caught one real encoding error during construction (pairing against the demand instead of its half) — evidence the cross-check is substantive. comp v14's methods records the parser as shipped; minimax v6's code availability cites it; each paper's methods names the sibling's archived witness.

## Item 3 — S3 ebc ↔ comp belief cells (executed)

`paper2_ebc_comp_beliefcell_joint_check_v1.py`: comp's radius law on ebc's deadline instance — the radius-δ cell inherits the verdict exactly for δ ≤ s(z₀) = z₀ − (1 + T/2) (295 admissible probes over T = 0..4, all 16 mode cells, the audited z-grid); boundary cells zero-slack; δ = 0 recovers ebc's stored per-state bound (singleton clause); two-state cell labels = conjunctions of singleton verdicts. 5/5 exact. Construction note: the first probe draft failed by testing below the instance's audited domain (z ≥ 1) where the 60-step simulation's semantics differ — the domain restriction is recorded in the script. Citation routing: the sentence ships comp-side (v14, citing ebc = 2026f); ebc's reciprocal citation rides its next natural edition (recorded here; ebc v5 stays frozen this round).

## Item 4 — S5 residue ↔ DR interpolation (executed, theorem-grade outcome)

`paper2_coupling_dr_interpolation_check_v1.py` (6/6 exact): on the residue's two-window instance (G = d₁d₂, product coupling 0 vs comonotone +1 at identical one-step marginals), the DR interpolation family of P3 satisfies sup over 𝒟_ρ of E_q[G] = ρ exactly, at every probed ρ ∈ {1/4, 1/2, 3/4, 1}: the interpolation contains the coupling extremum at ρ = 1, preserves the one-step marginals at every ρ, and leaves the coupling-selection difficulty orthogonal to the mixture parameter. Shipped as one sentence in minimax v6's residue remark (citing P3 = 2026e); P3 v8 stays frozen (its reciprocal citation rides its next edition, same policy as S3).

## Item 5 — S4/S6 single-sentence bridges (executed)

- S4: comp v14's erosion section cites ws's master monotonicity as the discrete counterpart of the refinement axis (positivity non-monotone on both sides); ws v14's conclusion cites comp's meshes/stored-scenarios/belief-cells as the continuous counterpart. One sentence each, no shared prose.
- S6: E1 v55's discussion adds one sentence citing P1's delayed-information theorem as the formal recognition-time mechanism behind its documented one-year lead. ARV stays untouched (its band certificates remain S2's natural future case study, noted in the record only).

## Discipline

All four editions: explicit staging, collision-free names, collision cmp byte-identical, fresh-clone cmp, verifier re-runs from the clone, identity "Amin Abaee <amin_abaee@ut.ac.ir>"; family keying table recorded in the map's round-25 section; no superseded edition overwritten; uploads and `.cache/dl` never staged.

# Joint assessment, wave 4 — the three P3 audits (`paper3_material_ledgers_v2.md`)

Status: **COMPLETE** (verification + implementation + synthesis). Target file identified as `paper3_material_ledgers_v2.md`
(the only P3 candidate carrying Theorem 13 with the frozen-biomass face, the G3P caveat paragraph, and
the Θ_F/ADH link — all three audit-only markers). The three audits are: audit 1 (complete, sections A–K),
audit 2 (**truncated** mid-"3. Gap closures"), audit 3 (**truncated** after its first item, mid-sentence).
Every claim was checked against the v2 text line-by-line, including the arithmetic of every alleged
proof defect. Items were verified **jointly**: several audit claims contradict each other or the paper,
and those are disposed with the arithmetic shown. Implementation targets a new
`paper3_material_ledgers_v3.md`; v2 and all four predecessors remain untouched.

## Verification results by audit

### Audit 1 (complete)

| Item | Verification | Class | Action |
|---|---|---|---|
| A1 harvest routing vs Theorem 7 (α>0 conservation bug) | Confirmed: (2) has no harvest term in U̇; §2.3 routes αh to U; nowhere declared that (2) ≡ α = 0. | **GENUINE** | Routing declaration at §2.2 + Theorem 7 clause. |
| A2 §9 heuristic uses working flux 4.65, not closed-block drain 0.187 | Confirmed: "tens of thousands of years" at G_0/A^{act*}=10³ requires flux ≈4.65 (G_0≈4×10⁵); the sentence claims a bound in the extraction flux c but quotes the recharge-flux scale. | **GENUINE** | Name both fluxes and both scales in §9. |
| A3 symbol collisions (N,S,M,K,T,C,I,R) | Confirmed, and worse than the audit lists: incidence is S_T (§2.1), N (Thms 3–4), ℐ (Thm 8) — three letters for one object; S also = regeneration in §5.4's decline-pressure line (contradicts §2.2's R); M = mass + generic matrix in Thm 5; R = regeneration + reserves (§7.6); σ = donor fraction + noise (§7); z/x state letter (§2.1 vs §2.3/§5.1). | **GENUINE** | Notation table + targeted renames (below). |
| A4 state letter z vs x in §2.1 | Confirmed (prose z, equation (1) x). | **GENUINE** | z → x in §2.1, §5.1. |
| A5 "row-stochastic" in Thm 8 | Confirmed; with destinations as rows, splits summing to one across destinations are **column**-stochastic. The paper's own sentence ("sums to one across destinations") is right; the label is not. | **GENUINE (micro)** | "column-stochastic in the destination-indexed convention"; §10.2 tail reworded. |
| A6 abstract "answers neither" | Confirmed; §6.5.4 supplies the content. | **GENUINE (micro)** | Abstract clause rewritten. |
| A7 "same public data products" (§6.5.2) | Confirmed (three products). | **GENUINE (micro)** | "same" deleted. |
| A8 resources horizon as point (>300,000,000 ⇒ >1,125 not ≈) | Confirmed. | **GENUINE (micro)** | "≈ 1,125" → "> 1,125". |
| A9 μ,ν,ρ never defined | Confirmed (two uses: §5.4, §9). | **GENUINE (micro)** | Definition clause at first use. |
| B1 Thm 1 Lipschitz line "should be μ+δ not |μ−δ|" | **Audit arithmetic is wrong.** Exact defect expansion: μ[X_κ A/(κ+A) − X_0] − δ(X_κ−X_0) − c(X_κ²−X_0²) − qE(X_κ−X_0) = −μX_κ κ/(κ+A) + (μ−δ)e − c(X_κ+X_0)e − qEe. The exact e-coefficient is μ−δ; its sharp bound is |μ−δ| ≤ μ+δ. The paper's displayed line is correct and sharper than the audit's. The audit's secondary point (K_log needs μ>δ only for positivity; X_max assumed) is valid. | **DISPOSED + GENUINE (micro)** | Keep the algebra; split L into L₁, L₂ and add the X_max sufficiency note (audit 2's 1.4 refinement). |
| B2 Thm 11 face A=0 | Confirmed: the proof writes Ȧ = d_U + e_GA ≥ 0, dropping −g − e_AG which vanish only by donor limitation. | **GENUINE (micro)** | Write the two vanishing terms. |
| B3 Thm 12 mining dropped in the addition | Confirmed: the proof adds Ȧ_act + Ȧ_geo = −B + γ_U U, silently assuming C^A = 0 while the statement covers mining. | **GENUINE** | One-line mining case added. |
| B4 Thm 10 "C¹ extension through the origin" | Confirmed: residue of A_g0 = 0; with A_0, A_g0 > 0 the factors are C^∞. | **GENUINE (micro)** | Phrase deleted. |
| B5 existence | Confirmed absent. | **GENUINE (micro)** | One sentence after (2). |
| C1 T never sits in N | Confirmed (T enters Ȧ_act, U̇ only). | **GENUINE (micro)** | Named in §2.2 ("uptake is A^act→U throughput with N catalytic"). |
| C2 e_GA is linear donor-limited exchange | Confirmed; three recharge laws across the paper (primitive, banned target-relaxation, working derived) never tabulated. | **GENUINE** | Naming clause + three-row remark (folded into §2.2/§9 wording, table deferred to supplement sweep — see Section H). |
| C3 basal-mortality remark for the frozen-biomass face | Not present. | **GENUINE (micro)** | One clause in Thm 13. |
| C4 two stock families non-transfer | Paper says it in Thm 2's proof but unnumbered. | **GENUINE (micro)** | Numbered wording added to Thm 2's scope. |
| D1 G3P magnitudes in the main table | Confirmed; caveat exists but numbers remain; the horizon column is not recoverable from the displayed columns (414/49.7 ≈ 8.3 ≠ 2.7). | **GENUINE** | Implied window-minimum column added (arithmetic, flagged) + strengthened fence; full move-to-supplement rejected (the table is the worked instance of the index construction; the audit's alternative — self-auditing columns — is implemented). |
| D2 phosphate country lives imply untabulated productions | Confirmed (implied: China ≈121,429; US ≈22,222; Jordan ≈13,226; Morocco 40,000; Australia ≈2,778 kt/yr). | **GENUINE** | Implied-production column added + MCS-2026 re-pin registered. |
| D3 USGS 2026 vintage | Verified externally: MCS 2026 is real (January 2026 release; pubs.usgs.gov/periodicals/mcs2026). | **DISPOSED** | Vintage pinned in data availability. |
| D4 Σ_reserves boxing | v2 already fences it as the §10.1 worked instance; the "Non-example" label is missing. | **GENUINE (micro)** | Label added. |
| D5 fisheries median 1.8 yr | v2 already states cohort conditions; quartile table not feasible without the RAM pull. | **STALE + micro** | Quartile summary registered; pull-date note added. |
| E1 layers are different kinds of predicate | Confirmed absent. | **GENUINE (micro)** | One sentence in §3.1. |
| E2 abstract vs §10.1 ("by itself") | Confirmed. | **GENUINE (micro)** | Abstract softened. |
| E3 envelope: flux-admissible vs reachable set | Qualifications exist; forward-invariance condition absent. | **GENUINE (micro)** | One sentence + corollary retitle note. |
| E4 Thm 6 vs Thm 14 (M need not hit 0) | Confirmed: the §4.7 follow-up sentence invites the finite-hitting misreading. | **GENUINE (micro)** | Sentence aligned with integrability. |
| F §9 interface: quote T* gap; positive contract line | Confirmed: "O(1)" unexplained; no positive contract line. | **GENUINE** | T* ≈ 4.47 quoted; orthant + harvest sign pattern added to the shared object. |
| G first-passage: right-skew; Stratonovich; non-claim 6 undefined | All three confirmed ("productivity-illusion" occurs nowhere else). | **GENUINE** | Three micro edits. |
| H gap closures 1–10 | H1 notation table, H4 coincidence lemma, H6 worked envelope implemented; H2 three-law table → supplement registration; H7 covered by D1; rest covered above. | **MIXED** | As listed. |
| I1–I6 profound upgrades | I4 (noncompensation as a theorem on B(x,t)) implemented — one proposition with the existing Σ witness; I5 (Hopf non-transfer) one sentence; I6 (MFA reconciliation bridge) one clause; I3 (viability unification) one linking sentence; I1 (types-as-types page), I2 (phosphate as Thm-15 instance) deferred to the venue pass. | **MIXED** | As listed. |

### Audit 2 (truncated at "3. Gap closures")

| Item | Verification | Class | Action |
|---|---|---|---|
| 1.1 Thm 13 ray: A^geo ≥ 0 should be > 0 (A_g0 = 0 case) | Confirmed: at A^geo = 0, σ = 0, so e_GA = 0 and Ȧ_act = −ω_A A^eq < 0 at the would-be ray point. | **GENUINE** | Corrected in the Thm 13 rewrite. |
| 1.2 Thm 12 "since" clause misidentifies the failing coordinate | Confirmed: Ṅ = 0 at the working point by construction; rest fails via R = 0 on the abiotic pair. | **GENUINE** | Rewritten clause. |
| 1.3 opposite donor flow at the working point (−0.348 vs +4.652) | Confirmed by arithmetic: ω_A(50 − 397.87) = −0.34787. | **GENUINE** | Displayed in §9 reason 3. |
| 1.4 Thm 1 two L's as one | Valid refinement (audit 1's B1 algebra rejected; the L-split is kept). | **GENUINE (micro)** | L₁, L₂ split + X_max sufficiency. |
| 1.5 sink obstruction needs θ_K > 0 | Confirmed: with θ_K = 0, w(H) ≡ 0 and the loading argument fails. | **GENUINE (micro)** | Clause added. |
| 1.6 [A_eq,intrinsic]_+ vestigial | Confirmed: registered target 50 > 0. | **GENUINE (micro)** | Bracket moved to a remark. |
| 2.1 typing thesis vs overloaded symbols; (1) writes S_T, Thm 3 writes N | Confirmed; the worst collision (three incidence letters) resolved. | **GENUINE** | Unified to S_T; notation table; σ→ς in §7. |
| 2.2 four-block not mass-closed | v2 already has the closure sentence; the missing half is the harvest-routing declaration (A1). | **PARTIAL-STALE** | A1 sentence carries it. |
| 2.3 signed R vs primitive discipline | Confirmed. | **GENUINE (micro)** | R decomposed into two primitives. |
| 2.4 four-block ≠ six-compartment specialization | Confirmed (T is A^act→U catalytic; scaffold's m is slow X→U). | **GENUINE (micro)** | Timescale-lumping sentence. |
| 2.5 three conservation proofs, no common lemma | Confirmed; Proposition 1 IS the common lemma. | **GENUINE (micro)** | Instance remark after Thm 9. |
| 2.6 Δ_phys untyped | Confirmed; the reconstructed draft's M̂ formulation is adopted. | **GENUINE (micro)** | M̂ clause (from reconstructed_v2). |
| 2.7 nested routing never displayed | Confirmed. | **GENUINE (micro)** | One sentence in §2.2's closure. |
| 2.8 frozen-biomass face vs depletion narrative | Covered by C3 (basal-mortality remark); the optional m₀N primitive deferred. | **GENUINE (micro)** | C3 clause. |
| 2.9 (Z,E) equations never displayed; projection claimed | Confirmed. P4 companion carries the system (eq. (1) + §2.4 working core). | **GENUINE** | Projection claim re-based on the companion citation. |
| 2.10 applied tables violate the routing discipline | Confirmed per row (414/49.7 ≈ 8.3 ≠ 2.7; production columns missing; no pull date). | **GENUINE** | D1/D2/D3/D5 fixes. |
| 2.11 κ/K_A, h, σ collisions | Covered by the notation table. | **GENUINE** | Table. |
| 3. (truncated: primitive form of (2); unify empty viability) | Only fragment available; the primitive-form item is implemented via the R-decomposition (2.3); the viability unification via the §6.3/§2.4 linking sentence (I3-lite). | **GENUINE** | As listed. |

### Audit 3 (truncated after item 1)

| Item | Verification | Class | Action |
|---|---|---|---|
| 1. Thm 13 false as stated — missing carrying-capacity rest | **Confirmed by direct computation**: with E ≡ 0, (N = K, U = κ_A K s/γ_U, A^act = A^eq σ) satisfies Ṅ = R = 0, U̇ = 0, Ȧ_act = −(R+T) + T = −R = 0, Ȧ_geo = 0 — a rest the v2 theorem's exclusivity clause denies. The v2 rewrite regressed relative to the reconstructed draft, whose Theorem 6 states exactly the two families. | **GENUINE (major)** | Thm 13 rewritten as the two-family statement with the reconstructed draft's proof (adapted), the ray corrected (audit 2.1), the frozen face kept with the C3 remark. |
| (remaining items unavailable — truncation) | — | — | Recorded; the truncated audit 2 covers the same ground on its completed items. |

## Implementation plan (→ `paper3_material_ledgers_v3.md`)

~45 edits in eight groups: (A) abstract/§1; (B) §2.1–2.2 (state letter, harvest routing, existence,
R-primitives, [·]_+ remark, closure/nesting); (C) §2.3–2.6 (timescale lumping, θ_K, Thm 1 split-L,
Thm 2 non-transfer, notation table); (D) §3 (layer kinds; Thms 3–5 S_T unification, generic-matrix
letter, forward-invariance + reconciliation clauses, worked envelope); (E) §4 (Thm 7 routing clause,
Thm 8 column-stochastic + S_T, Thm 9 instance remark, Thm 10 smoothness, Thm 11 face line, Thm 12
mining + working-point rewrite, Thm 13 two-family rewrite, Thm 14 language + mining clause); (F)
§5 (service letter x; Δ_phys M̂ typing; μνρ definition; S(N)→R); (G) §6 (H4 coincidence remark;
G3P window-min column + fence; phosphate production column + vintage note; A7; Non-example 1 label;
fisheries quartile registration); (H) §7–§11 + data availability (σ→ς; right-skew; Stratonovich;
non-claim 6; §7.6 R→G; §9 μνρ citation, companion citation, T* quote, opposite-sign display, contract
line, two-scale heuristic, Hopf non-transfer; §10.1 proposition; §10.2 rules; conclusion; data notes).

Checks after implementation: numdiff v2→v3 (expected deltas: table columns −548, −292, −237, −88.5,
−33, 121,429 / 22,222 / 13,226 / 40,000 / 2,778 / 239,482 / 240,000 / 250,000, T* 4.47, −0.348,
2×10⁶, 8.6×10⁴, 120,000), delimiter balance, and a full diff review.

## Sweep dispositions (post-implementation)

- **Deferred (venue pass / supplement):** I1 types-as-types page; I2 phosphate-as-Thm-15-instance;
  H2 three-law recharge table (registered for the supplement); the optional m₀N basal-mortality
  primitive (audit 2.8's optional half); G3P full quarantine (superseded by the self-auditing-column
  fix); RAM quartile recomputation (registered revision requirement).
- **Rejected with reasons:** B1's algebra correction (audit arithmetic wrong — shown above); full
  G3P removal from the main text (no-condensation directive; the table is the worked instance).


---

## Implementation record (all applied to the new `paper3_material_ledgers_v3.md`)

55+ edits in six batches, each replacement verified against its expected occurrence count:

| Group | Content |
|---|---|
| Abstract/§1 | A6 clause ("gross-loss pressure scale, not a net-depletion diagnostic and not a hitting time"); E2 "by itself"; "vanishing-extraction rest set (extinction, carrying capacity, and the frozen-biomass face)" in abstract, contribution 3, and conclusion; "What is not claimed" front-matter paragraph (from the reconstructed draft). |
| §2 | State letter x (A4); harvest routing α = 0 declaration + companion (Z,E) citation + R primitive decomposition (A1/2.3/2.9); global existence (B5); [·]_+ one-way-valve remark (1.6); closure/nesting/donor-internal sentence (2.2/2.7); T-not-in-N naming (C1); **three-law recharge table** (C2/H2); timescale-lumping sentence (2.4); θ_K > 0 clause (1.5); Theorem 1 split into L₁, L₂ with the X_max sufficiency note (1.4 — keeping the paper's correct |μ−δ| algebra against audit 1 B1's incorrect one); Theorem 2 non-transfer sentence (C4); **notation table** (A3/H1/2.1/2.11) with §-references and the σ/ς, M/M̂, R/G, G-reserves entries. |
| §3 | Layer-kind sentence (E1); Theorems 3–5 incidence unified to S_T (three letters → one); generic-matrix letter 𝖠 (A3); forward-invariance clause (E3); MFA data-reconciliation bridge (I6); worked envelope on (2) (H6). |
| §4 | Theorem 7 routing clause (A1); Theorem 8 column-stochastic + S_T (A5); Theorem 9 instances-of-Prop-1 remark (2.5); Theorem 10 smoothness (B4); Theorem 11 face-A donor-limitation display (B2); Theorem 12 mining case closed + working-point clause rewritten (1.2/B3); **Theorem 13 rewritten as the two-family vanishing-extraction rest set** with the reconstructed draft's proof, the ray corrected to A^geo > 0 (2.1), the C3 basal-mortality remark, and audit 3's carrying-capacity family restored; Theorem 14 language aligned with non-finite hitting (E4) + mining-restored clause (from the reconstructed draft). |
| §5 | Service letter x (A4); Δ_phys typed via M̂ (2.6, reconstructed formulation); μ,ν,ρ defined (A9); decline-pressure S(N) → R(N, A^act) (A3 collision fixed). |
| §6 | Coincidence remark (H4); G3P implied window-minimum column + strengthened fence (D1/2.10); phosphate implied-production column + MCS-2026 re-pin + Australia JORC note (D2/D3/2.10); A7; Non-example 1 label (D4); fisheries quartile registration + pull-date note (D5). |
| §7 | Noise σ → ς throughout (2.1 collision); right-skew sentence (G); Stratonovich sentence (G); non-claim 6 defined (G); §7.6 reserves R → G (A3). |
| §9 | μ,ν,ρ citation (A9); (Z,E) projection re-based on the companion citation (2.9); T* ≈ 4.47 quoted (F); opposite-sign donor display −0.348 vs +4.652 (1.3); positive contract line (F); two-scale heuristic G₀/c vs G₀/B* (A2); Hopf non-transfer sentence (I5). |
| §10–11 + data | No-weighted-certification Proposition with the Σ witness (I4); rule 2 coefficient in S_T; rule (iv) column-check wording (reconstructed); "unit-sum split routing" (A5 tail); data-availability vintage pins (D3/D5). |

**Checks:** numdiff v2→v3 — 17 new significant numbers, every one deliberate (4.652×2, 0.187, 0.348, 4.47, 8.6, 33.0, 88.5, and the production-column values 13,226 / 22,222 / 40,000 / 121,429 / 239,482 / 240,000 / 250,000 / 120,000 / 2,778); nothing dropped. Delimiter balance even (1,888). Full diff reviewed line-by-line; two escape artifacts (notation-table § signs and one em-dash) found and fixed. Abstract, figures, and the remaining untouched content unchanged.

## Remaining-points sweep (task 2)

- **Implemented in the main pass above:** I4, I5, I6, I3-lite (via the existing K_maint/viability links), H4, H6, C2/H2 table, and every correctness item of all three audits that survived joint verification.
- **Recommended for the venue pass (worth doing, not safe as a text sweep):** I1 (types-as-types sort system — a page that makes §10.2 rules (i)–(v) instances of ill-typed terms); I2 (phosphate reserves/resources as two typed compartments with a kernel jump — turns "the ratio is not a forecast" into a lemma under Conditional Theorem 15, deepening the Tilton citation); the optional m₀N basal-mortality primitive (audit 2.8's optional half; the Theorem 13 remark already declares its effect).
- **Registered revision requirements (data, not text):** RAM 43-stock quartile summary and pull-date audit; MCS-2026 re-pin of every phosphate row (Australia row quarantined pending it); G3P basin-mask re-derivation before any numerical reuse.
- **Rejected with reasons:** audit 1 B1's Lipschitz correction (the audit's algebra is wrong — the exact e-coefficient is μ−δ, so the paper's |μ−δ| bound is correct and sharper; only the L-split refinement was adopted); full removal of the G3P table from the main text (the self-auditing columns achieve the audit's goal without violating the no-condensation directive).

## Synthesis (task 3)

`paper3_material_ledgers_v3.md` **is the best overall synthesis of all four P3 predecessors** and is declared the canonical P3 file. Lineage: base = material_ledgers_v2.md (the most complete arrangement, 14.2k words) + all verified audit fixes above + the unique substantive content of the reconstructed drafts (the two-family vanishing-extraction rest theorem and its proof — which restores the carrying-capacity rest the v2 rewrite had lost and which truncated audit 3 independently re-derived; the M̂ demand-coverage typing of Δ_phys; the "What is not claimed" front-matter; the rule (iv) column-check wording; the mining-restored integrable-extraction clause). The four predecessor files remain untouched in the workspace; the recovered reconstructed drafts' provenance is preserved. This resolves the standing P3 canonical-file decision.


---

## Wave 4b — the complete audit 3 (user re-uploaded the file; audit 3 now runs to the end)

The re-upload replaced the truncated 393-line file with the full 608-line version (audit 3 from line 386 to the end: critical flaws 1–4, internal inconsistencies, data/credibility, gap closures 1–11, profound upgrades A–G, "already strong" list, revision order). Every item was re-checked against v3; each item's status:

**Already fixed in v3 (by the main wave):** critical 1 (Theorem 13 two-family rest — v3's Theorem 13 restores the carrying-capacity family, the one-line existence check is the proof's N=K branch verification, the uniqueness sentence and §4.6 scope are corrected); critical 3 (incidence unified to S_T; no ℐ, no stray N-as-matrix — one residual found and fixed in v4, below); critical 4 (productivity-illusion now defined inline in non-claim 6); abstract "answers neither" (abstract already uses the pressure-scale phrasing); z vs x (x is canonical, z a declared §2.3 alias in the notation table); Theorem 12 proof mining term and the working-point phrasing (both rewritten); §9 opposite-sign donor display (−0.348 vs +4.652); harvest routing α=0; basal-mortality remark in Theorem 13; G3P order-of-magnitude hedge + quarantine; RAM cohort rule (F > 0, SSB > 0.2 max, pull date, quartile requirement); Σ_reserves kept as labeled Non-example 1 with its disowning paragraph (decision: kept — the audit's "kill it" option conflicts with the no-condensation directive, and the in-text fence is the audit's own "conceptually right" treatment); μ,ν,ρ defined in §5.4.

**Fixed in v4 (this wave — 21 checked edits, all arithmetic re-verified):**
- Critical 2: contribution 5 pointer (Section 6.6) → (Section 6.5). The one remaining incidence collision: §3.4's `c_m^⊤ N = 0` → `c_m^⊤ S_T = 0` (a stray letter the main wave's greps had missed because it was not in the S(N(t)) pattern).
- Notation: y and θ defined at eq. (1) and added to the notation table.
- §2.4 closed-ledger corollary: the "exceeds any finite ceiling" claim now carries the finite-mass qualification (which constraint fails first depends on M, K_max, remaining stock; ceiling ≥ total mass unreachable → the violated constraint is the resource floor, by Theorem 14).
- §3.4: barrier–conservation compatibility stated as a linear feasibility programme (the intersection may be empty although each object is well-defined).
- Theorem 5: polytope/LP envelope named as the tight version, box as the auditing relaxation (Feinberg lineage).
- §3.6: named Proposition (Depletion is compartmental) — invariant 1^⊤x, hitting times are compartment/barrier objects, never total mass.
- Theorem 14: added the does-not-decide clause (L¹ bound does not select extinction vs. recovery to K among Theorem 13's rests).
- §4: closed-ledger portrait paragraph (conservation/positivity/no-rest/rest-set/budget chain as the source object for the §9 interface).
- §9: Theorem pointer (Theorem 1) → (Theorems 1–2, pointwise, non-uniform); μ=ν=ρ clause in words; the three registered numbers displayed in reason 1 (50 / 397.87 / 5050; factor of eight; two orders); working-point precision clause with the qE*N* = 0.001×2.090×89.526 ≈ 0.187 reverse check (consistent — recomputed); the five reasons re-labeled as the short-time (1–3) / long-time (5) / fake-metric (4) trichotomy; **Theorem (Non-reduction of the open working completion)** with clauses (i)–(v); frozen-donor limit re-framed as a corollary of clause (i).
- §6.5: the classification matrix (quantity × question × G3P/phosphate/fisheries) added as the section's anti-drift instrument (upgrade A), number-free by design.
- §6.5.2: G3P trend-window consistency check (−49.7 cm yr⁻¹ over ≈21.4 yr places the fitted 2002 value near +6.5 m above reference → the fitted segment convention is part of the quarantine; arithmetic recomputed).
- Non-claim 3: positive IG characterization (T_A would be IG iff the active-pool residual were Brownian with constant drift, which (2) is not; the tabled numbers are IG means of Definition 6's surrogate and nothing else).
- §10.1: Γ_reg gap sentence (a weighted sum on B(x,t) cannot see (1−α_reg)s̄ — gap closure 7) and the strong/weak sustainability bridge (componentwise adequacy = strong sustainability as conjunctive predicate; positive weighted sum = weak sustainability as ranking device; upgrade E).
- Theorem 8: seven-compartment incidence declared as the pattern of Theorem 9's S(α,ρ) plus the inert column (gap closure 9's display option).

**Registered, not implemented (as planned):** yield-routing 2×2 witness (gap closure 8); face diagram of the orthant (venue pass figure); §7 full inversion (its content — surrogate means, IG characterization, corollary, non-claims — is already present in that order in v4); §6.5.2 supplement move (kept with fences per the no-condensation directive); basal-mortality primitive (remark already in Theorem 13); MCS re-pin, RAM quartiles, G3P re-derivation (revision requirements, unchanged).

**Checks on v4:** 21 edits applied with per-edit occurrence asserts; delimiter parity even (1,976); zero escape artifacts; number-token diff v3→v4 — only deliberate additions (5050, 2002, 6.5, precision-clause repeats of 2.090/89.526/4.652/0.187/0.001/397.87/50) and exactly one removal (6.6, the pointer); full diff reviewed line-by-line; v4 = 17,777 words.

Verdict on the file replacement: the re-uploaded 608-line file now IS the workspace copy at /home/user/uploads/grok audit paper 3 v2.txt (same path, no separate backup needed — the truncated version no longer exists in the workspace). `paper3_material_ledgers_v4.md` is the new canonical P3 draft; v1/v2/v3 and the two reconstructed drafts remain untouched.


---

## Wave 5 — flow/seam pass (user-reported: the synthesis reads stitched, e.g. the abstract's first two sentences)

New file `paper3_material_ledgers_v5.md` (v4 untouched). 21 checked edits, connective-only — no content numbers changed (token diff v4→v5 fully explained by the G3P anchor's digit, the portrait's theorem numbers, Theorem 8's naming, and the removal of Section 4's self-reference; zero escape artifacts; delimiters 1,976 even; 17,891 words).

Fixed seams: abstract rewritten as one connected argument (To separate them… / The accounting rests on three… / The layer is then specialized… / With the ledger in place… / Three public-data applications are then… / Complementing the classifications… / Finally…); §1.2 numbered list made contiguous (What-is-not-claimed moved after item 7 with a lead-in); §2.1 conservation fragment fused to its sentence; §2.2 three-law table given a lead-in and the post-table sentence anchored (In the closed block no derived target appears); the §2.2 mega-paragraph split into constitutive declarations vs. closure discipline; §2.4's dangling The-proposition phrase replaced by This mass balance; viability-kernel clause punctuation; both QED run-ons broken into their own paragraphs (Theorem 8, §10.1 — zero QED-glued sentences remain); the §3.6 Proposition repositioned as the closing named statement with a lead-in; the §4 closed-ledger portrait moved from mid-§4.7 to the true end of Section 4 and reworded (Theorems 7–14 assemble…); §6.5.1/6.5.3/6.5.4 each anchored to the classification matrix (The G3P/phosphate/fisheries column of the classification matrix is…); the §6.5.2 G3P nested parenthetical and the fisheries fragment-list parenthetical restructured into full sentences (all arithmetic content preserved); the §9 semiconjugacy dummy y → ξ (y is now uniquely the eq. (1) boundary state); the frozen-donor corollary pointer disambiguated (structural clause (i)).


---

## Wave 6 — deep content-integrity scan (user: any accidental loss / condensation? anything to restore?) + GitHub hand-off

**Method:** sentence-level normalized diff of all five P3 predecessors (v1, reconstructed, reconstructed_v2, v2) against v5, plus removed-line review of every edit transition (v2→v3: 89 lines; v3→v4: 15; v4→v5: 20).

**Result — no accidental loss; one genuine restoration found and made.**
- v2→v3 (89 replaced lines): all classified as deliberate replacements with preserved or strengthened content — notation unifications (z→x, ℐ→S_T, σ→ς, R→G, CN→CS_T), audit corrections (row→column stochastic, Thm 12 mining term, Thm 13 two-family rest set, registered-regime smoothness replacing the C¹-extension phrasing, cohort rule replacing "zero entries included"), table columns added (window minimum, implied production), §9 displays strengthened (−0.348, T*≈4.47, two-scale fluxes), §10.1/§10.2 rewordings. Nothing dropped.
- v3→v4 (15) and v4→v5 (20): the wave-4b and flow-pass edits; every removed line was a replaced original of a verified edit; number-token diffs were clean in both passes.
- v1-specific: "zero entries included" was corrected away per audit 3 (value verification = registered RAM quartile recomputation); v1's Theorem 13 exclusivity sentence was the regressed/wrong form, correctly replaced. Nothing to restore from v1.
- Reconstructed drafts: the five turn-33 absorptions re-verified present in v5; the detailed phosphorus identification ladder (per-parameter observations, prior ranges, falsification protocols) re-verified present in paper3_supplementary.md S2.1 (the main text's pointer arrangement — not a loss).
- **Restored in new paper3_material_ledgers_v6.md:** the reconstructed draft's universal constructive theorem — Theorem (Universal failure of weighted certification): for every w ≥ 0, w ≠ 0, on a ledger with m ≥ 2 components there exist a demand vector and an admissible state–operation pair with w^⊤b ≥ 0 while some b_m < 0; two-compartment witness proof in full (both cases: a zero weight entry, or all entries positive via the x_j scaling with ε); plus the no-dynamics remark and the compensating-pair domain condition, integrated without duplicating the existing strong/weak-sustainability bridge. v5's conditional Proposition remains as the domain-level form. Checks: delimiters even (2,056), zero escapes, number delta v5→v6 fully explained (indices, ε, m≥2, section refs), 18,307 words. v6 is canonical P3.
- Supplementary S4 statement inventory needs one line for the new theorem — registered as a follow-up (not edited in place to respect the versioning rule).

**GitHub hand-off (this turn):** token authenticated; repo and folders identified by listing; all paper rewrites (all versions + supplementaries + figures) committed to the exact "arena agent 1/paper rewrites" folder, all other workspace documents (audits, joint assessments, scan findings, writing plan, reading log, guides) to "arena agent 1/other documents". No other paths touched. Routine saved as /home/user/push-to-github.sh (reads the token from /home/user/.github-token; git config is not persisted across snapshots, so future turns re-run the script).

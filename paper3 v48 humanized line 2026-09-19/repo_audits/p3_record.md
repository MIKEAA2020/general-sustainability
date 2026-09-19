# P3 wave-4 record — paper3_material_ledgers_v28.md (Task 73-c)

Build: `apply_batch7_wave4_p3.py` (fail-loud; rebuild from v27 is byte-identical — verified by
the orchestrator twice). The build agent was interrupted after producing the script and v28; the
orchestrator verified the artifact and wrote this record. 209 changed lines, all dispositions
below verified against the v28 file by grep/read.

## Per-item disposition

| Item | Status | Evidence (v28) |
|---|---|---|
| R11 [both] "horizontal exhaustion estimate" → horizon | IMPLEMENTED | "exhaustion-horizon estimate" ×3 (§1.1, §11, reserve sentence); "horizontal exhaustion" survives only inside the version log's quotation |
| R12 [both] B = b·M undefined | IMPLEMENTED | §1.1 defining clause: "$B = b\cdot M$ — the aggregate regeneration flow, with $b$ the per-unit-mass regeneration rate and $M$ the natural-block mass; letters local to the introduction … from Section 2.2 on $B$ names the gross turnover $R+T$"; §11 token harmonised |
| R13 [claude] deep-time contradiction | IMPLEMENTED | §1.1 scoping sentence: deep-time clause scoped to "geological donors and mineral stocks"; the tabulated regenerative compartments "renew on human timescales — a crop within a season, an aquifer within years to decades, a fish stock within years" |
| R14 [claude] Mt/kt mix | IMPLEMENTED | §6.5.3: "approximately $74{,}000{,}000$ kt ($74{,}000$ Mt) of world reserves and $240{,}000$ kt/yr of production"; arithmetic unchanged (74,000 Mt = 74,000,000 kt) |
| R15 [claude] "five right-hand sides" | IMPLEMENTED | §9 hand-off lists the closed block's six right-hand sides; $A^{\mathrm{geo}}$ restored |
| R16 [grok] μ, ν, ρ early use; ρ collision | IMPLEMENTED | Defining clauses at §2.2 first use; retirement fraction re-lettered $\rho_P$ (15 sites); §9 gloss harmonised; Thm 15's hybrid state/flux re-lettered $\chi, \eta$; notation table moved to head of §2 and extended (17 previously omitted symbols) |
| R17 [both] data-vintage decisions | IMPLEMENTED (owner default: KEEP-IN-PLACE) | Indo-Gangetic daggered row stays first with the caveat adjacent; fisheries headline cohort stays in place with S5's non-reproducibility record cross-referenced at the headline site and the v4.66 broad-cohort reading stated as the primary public-release comparison |
| Theorem inflation [both] | IMPLEMENTED | Thm 2→Remark 2, Thm 3→Lemma 3, Thm 4→Proposition 4, Thm 6→Proposition 6, Lemma 16→Remark 16, Thm 17→Proposition 17, Thm 18→Proposition 18, Thm 20→Proposition 20; 1–20 counter unchanged; every cross-reference updated (grep-verified counts: Lemma 3 ×9, Prop 4 ×6, Remark 2 ×4, Prop 17/18 ×3, Remark 16 ×3, Prop 20 ×2, Prop 6 ×2) |
| R₀ split [both] | IMPLEMENTED | Theorem 13's rest set split into $\mathcal{R}_{\mathrm{ext}}$, $\mathcal{R}_K$, $\mathcal{R}_{\mathrm{frozen}}$; Theorem 12(iii) misuse corrected |
| Incidence matrices [both] | IMPLEMENTED | Four-row block incidence (§2.2) and seven-compartment incidence (Theorem 8) displayed with column-sum checks (7-compartment sums all zero; harvest/mining = −1 exports) |
| Theorem 14 E ≥ 0 [both] | IMPLEMENTED | Hypothesis stated; constant-flux labelled "a comparison flux only, not a donor-limited primitive" |
| §9 field-difference reconciliation [grok A11] | IMPLEMENTED | Both vector fields written at the same $(N, A^{\mathrm{act}}, U)$: difference $\kappa_A K - \gamma_U U$ ≈ 0.535 stock-units/yr at the working point ($\gamma_U U = T^* \approx 4.465$; $\kappa_A K = 0.05 \times 100 = 5.000$) and 5.000 at $U=0$ — replaces the three inconsistent readings (4.47 / O(κ_A K) = O(5) / 4.652 vs −0.348). Arithmetic self-verified by the orchestrator |
| Θ_F contradiction [grok] | IMPLEMENTED | Classification matrix's fisheries cell now "gross-loss analogue only — not a member (§6.5.4)", matching §6.5.4 |
| USGS single-vintage re-pin [both] | IMPLEMENTED (pin + registered action) | MCS 2026 declared the single pinned source of record; pin anchors displayed; per-row re-pin registered as the open data action (requires the per-country MCS 2026 reserve table) |
| §11 weak/strong re-argument [both] | IMPLEMENTED | Conclusion no longer re-argues the regimes; closes on the inventory |
| Three uncited companions [both] | IMPLEMENTED (cite-don't-drop) | In-text citations + reference entries: Author, D. (delay-dynamics), Author, E. (review screen), Author, F. (assessment separation) — fresh letters, repo pattern |
| Length [both] | PARTIAL (bounded, registered) | §1.1 strip (elevator restatement, no-drift triple) + §11 tightening; the remainder of the 21k→12k reduction registered with its reason (restructure-level cuts would remove content the auditors called the publishable core) |
| Housekeeping: supplementary pointer | IMPLEMENTED | Now cites `paper3_supplementary_v7.md` |

## Non-destructiveness

All pre-existing table rows byte-identical except the classification matrix's Θ_F cell (the
endorsed contradiction fix) and the notation table's moved/extended cross-reference cells; the
two incidence displays are new content. No frozen verdict, score, or table value changed.

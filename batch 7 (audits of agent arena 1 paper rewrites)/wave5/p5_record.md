# Wave-5 P5 record — paper5_sampled_governance_v22.md (from v21)

**Task ID:** 75-d. **Directive:** owner gate opened — re-evaluate the registered
follow-ups; re-open what is now worth doing.

## The re-opened items (each was declined only on wave-scope grounds, not merit)

| Item | Endorsement | v21 decline reason | Re-verification at v21 | Disposition |
|---|---|---|---|---|
| Two architecture names: "sampled governance" (§1 L55) vs "sample-and-hold governance" (abstract L9, keywords L18, title) | grok §6 ("pick one term after first definition") + claude ("unify") | "harmonising them is a title-level change outside this wave's mandate" | Verified open: two names for one architecture, title carries both, no equivalence declared anywhere | **IMPLEMENTED as the controlled fence** (not a rename): §1's naming sentence now declares the equivalence — "It is the same architecture the abstract, the keywords, and the title's second clause name *sample-and-hold governance*: one object under two names — *sampled governance* names the institutional loop, *sample-and-hold* its control-theoretic update law — and the two names are used interchangeably throughout this article." The title keeps both (no retitle endorsed); the audits' reader-confusion concern is answered by the declaration. |
| Abstract "thirty-plus" (L13) vs "more than thirty" (L43, L59, L158) | claude Title/Abstract note | "the joint item covers only the 42 count; both thirty-phrasings mean the same" | Verified open: 1 "thirty-plus" vs 3 "more than thirty" | **IMPLEMENTED** (one word-level harmonisation): abstract now reads "a structured search across more than thirty systems returns zero eligible cases" — the paper's dominant form; count claim unchanged |
| Figure 1 caption "four update pairs" (L272) | claude §3.4 note ("four update pairs → four update × channel combinations") | "not elevated to the wave-4 docket" | Verified open: the caption's own next sentences name the extractive/protective channels and Euler/exact updates | **IMPLEMENTED** (claude's exact wording, with the four named): "review-interval ranges for the four update × channel combinations (forward-Euler and exact updates on the extractive and protective channels), with crossing markers" |

## Build and verification

- `apply_batch7_wave5_p5.py` (fail-loud: three asserted-once sub1 anchors + the
  version-log splice). Ran clean twice: **MD5 64aa113a5edc34fb87cebc2c493e1331**
  both runs (542 lines). v21 untouched.
- Mechanical checks: "thirty-plus" body-zero; "more than thirty" ×4; the fence
  and caption strings present once; "four update pairs" zero; both architecture
  names' counts non-decreasing; title byte-identical; every v21 table line
  survives byte-identically with the line count unchanged (no table touched);
  frozen spectral needles (1.00035, 6.501, 47.536, 79.143, 2.306, 0.9967,
  0.9838, 42-annually-assessed, q = 0.1) and the clock-resolved needles
  (Rose (2026), 2026-09-01) unchanged.

## Still behind the gate (reasons re-verified, still valid)

- **Lemma 2.2's application to seal predation + Prop 2.1 demotion** (claude E7)
  — claim-changing, not presentation.
- **θ's strong-resonance check** — a computation; θ recorded as not-printed
  (the margins paragraph is the no-new-computation answer).
- **The nonlinear "exact update" definition** (claude §3.4) — defining it would
  assert content the manuscript does not record; left to the archive.
- **"Three objects"/"two operators" counts** — bound by the §2.3 reconciliation
  paragraph (verified present and binding).

## Non-destructiveness

No spectral record, crossing, verdict, table row, or recorded value changes;
title byte-identical; the three edits are presentation-layer.

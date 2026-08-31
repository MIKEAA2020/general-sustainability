# GitHub Provenance Investigation — Where the Corrected P3 Versions Do and Do Not Exist

**Date:** 2026-08-30 · **Question:** did the Grok-audit corrections to Paper 3 (the material-ledgers theorems) already exist in any GitHub file (uploads/, revised_articles/, joint-audit files, other corrected files)? Plus: any other corrections or lost content worth restoring?

**Method:** full tree fetch of `MIKEAA2020/general-sustainability` main (2,790 entries, not truncated); md5 comparison of every manuscript base in the local clone against raw.githubusercontent.com; content-level checks of every corrected/audit file against the 14 GENUINE + 2 NEW Grok items and the batch-5 finding list.

---

## 1. Preliminary fact — the scan base was already current

All nine manuscript bases in the local clone are **byte-identical to GitHub main** (md5):

paper1 v3 · paper2 v2 · paper3 v2 · paper4 v2 · paper5 v2 · wave_e cod ladder v2 · cod intervention v2 · Edwards ladder v2 · Edwards intervention v2 — all IDENTICAL.

So every arena-agen1 file was written from the **Batch-5 corrected editions** (the user's own joint-audit campaign of 2026-08-29, documented in `BATCH5_JOINT_AUDIT_EVALUATION.md`). The batch-5 corrections were inherited by my drafts; the deep numeric scans of the previous turns were against the corrected bases.

## 2. Question 1 — were the Grok-flagged P3 theorem fixes already on GitHub? **No.**

The Grok-audit items decompose into two provenance classes (Turn-27 trace, reconfirmed now):

**(a) Inherited flaws — present in the GitHub official edition itself.** The rest-set overclaim (missing frozen-biomass face), the Thm-12 m=1 gap, the ρ/t collisions, ADH≡Θ_F under two names, the mass-M/matrix-M collision, the dangling (S, χ) parenthetical, rule (iv) without a checkable criterion, the un-flagged restricted golden rule, the "zero entries included" ambiguity, and the four-basin magnitude flags are all in `papers/paper3_material_ledgers/manuscript_v2.md` on GitHub main. The batch-5 campaign did **not** fix them — its 10 accepted P3 findings are count/declaration/citation-level:

| Batch-5 P3 findings | Nature |
|---|---|
| P3-01 A_g0 missing from baseline | declaration fix (A_g0 > 0, separation of scale) |
| P3-02 K/N overloading in §2.4 | local-notation declaration |
| F11 — 16/18 uncited references | in-text hooks |
| F15 — "extraction and mining rates" wording | parenthetical fix |
| F19 — G3P magnitudes | one-sentence window-relative note |
| F24 — six-compartment incidence matrix | explicitly checked and **correct** |
| P3-C1 stale "two scored-forecast papers" count | corrected to four Wave E manuscripts |
| P3-C2 "54 codes" vs 52 retained | restated |
| P3-C3 Aubin (1991) unanchored | anchored at viability-kernel first use |

The batch-5 arena-agent-2 deep-dive recomputed the official P3's proofs and concluded "no mathematical or status error" — but it did **not** isolate the rest-set face or the m=1 gap (both are subtle; both were later confirmed genuine by the Grok audits and my verification). The agent-2 deep-dive IS a useful positive record: incidence matrix, conservation Thm 3.7, four-stock balance, mass identity Thm 3.6, no-rest Thm 3.11, inverse-Gaussian and GBM laws, exp(−M) entries, and the 52-row count were all re-verified computationally.

**(b) Introduced by my reconstruction — no counterpart exists anywhere.** The Thm-9 envelope sign error, the Thm-12 w⊤(s−d) slip, the Thm-7 mining-orthant gap, and the undefined demand-coverage matrix in the reconstruction's §6.3 are by construction absent from GitHub. The authorities for the correct statements are the official's own clean objects (its noncompensation statement; its defined demand-coverage matrix), which the v2 corrections followed.

**Other GitHub lineages checked and ruled out as "error-free versions":**
- `revised_articles/A013_component_accounting_corrected.tex`, `A019_closed_ledger_corrected.tex`, `A020_two_channels_corrected.tex` — earlier-scope source articles; they do not carry the full P3 theorem set (no envelope, no noncompensation theorem, no golden-rule, no ADH, no four-basin table).
- `uploads/paper3_final.md` ("Who Holds Adaptive Capacity" — the B6 distributive paper), `uploads/paper3_rev2.md` (Smooth-Krein barrier formulation), `uploads/paper3_empirical.txt` (periodic review / sampled governance) — the uploads numbering is a **different** paper numbering; none is the material-ledgers paper.
- `qwen writer/gpt audit of qwen paper 3.txt` — the qwen-writer P3 lineage has its own larger defects (overclaiming, tautological bridge theorem, a false Theorem 2, inconsistent ontology); it is the least clean lineage, not the most.
- Root-level `JOINT_AUDIT_ASSESSMENT.md` (batch-2 records R01–R09 — the general-theory family, not P3), `TRANSFER_AUDIT_RESPONSE.md` (session-work theorem cards), `parallel_audits_evaluation.md`, `joint_architectural_audit_evaluation.md` — other objects, no P3 theorem repairs.

**Conclusion for Question 1:** the corrected, error-free versions of the Grok-flagged P3 theorems exist **only** in the arena-agen1 v2 files — `paper3_material_ledgers_v2.md` and `paper3_material_ledgers_reconstructed_v2.md` (plus this campaign's non-reduction-boundary restoration). GitHub main carries the batch-5 corrections but not the Grok theorem fixes.

## 3. Question 2 — corrections/lost content found while scanning the GitHub tree

**Verified carried (my arena files were written from the corrected editions):** E4 flat-0 T=4 certified-horizon exception (≈687.9 ft, grid-skips-T=4) ✓; E4 T=5 year-set classification ✓; E2 exact operands 172.47 − 114.85 = 57.62 ✓; E2 corrected fixpoint 2338.3 (flat-180 T=∞) ✓; E1 cross-environment reproducibility record (M1b ±17 kt, 13/19 files, verdict robustness) ✓; E1 DFO-block reference ordering (capelin 2024/050 inside the block) ✓; E1 freeze-discipline caveat ✓; E3 abstract's 0.13-ft claim excluding M2_Rar ✓; P4 tether-threshold α≈1.3×10⁻³ withdrawn (my P4 does not reintroduce it) ✓; P4 branch-resolved lower-boundary statement (multiplier 1.0514→0.998983) ✓; P4 loop-gain maximizer ω≈0.0589 ✓; P4 τ₊ pairing 132–150 / 76–80 across both effort laws ✓; P4 memory-gain rename g→γ_m ✓; P3 A_g0 declaration ✓; P3 G3P window-relative note ✓; P5 Bangkok/La Mancha stabilising-side wording ✓; P1–P5 "two scored-forecast papers" count not reintroduced ✓; E2's cpm-label issue moot (my E2 names its cascade locally, defined at first use); E1-C1 changelog vocabulary absent ✓; E2-C2 "printed at the exact operand values" clause absent ✓.

**One restoration applied:** E1 abstract now carries the W09 parenthetical — "115–196 kt … under the coarse catch regime (115–206 kt across both catch treatments)".

**Noted for the venue pass (not papers):** `FINAL_EDITIONS_CONSOLIDATION_SCAN.md` on GitHub carries the batch-5 dependency map and the cross-paper overlap audit (12-gram overlap 0.01–1.55% per pair; five overlap classes; no substantive self-plagiarism) — the reference document for the remaining per-manuscript checklists and final venue passes.

## 4. Files changed this turn

- `paperE1_cod_forecast_ladder.md` — W09 parenthetical restored.
- `/home/user/arena agen1/audits/github_provenance_findings.md` — this document.

# Paper 2 — v48 Addendum (A3 editorial sweep — disposition record)

**Version:** `paper2_obstruction_calculus_v48_Automatica_routes` (main only; supplementary unchanged at v46).
**Base:** v47 (pushed `93d0b85`). **Scope:** the A3 editorial programme of roadmap v3/v4 (source: `uploads/qwen p2.txt`), executed as a point-by-point adjudication. **Result: three accepted edits, nine items already satisfied, four rejected with reasons, one partial. With v48, Track A is complete.**

## 1. Accepted edits (3, surgical)

| # | qwen item | Edit |
|---|-----------|------|
| E1 | 3.1 "necessity side" is misleading | §1: "What that literature does not supply is the necessity side: a calculus of obstruction certificates." → "…the converse direction: a calculus of obstruction certificates, each a sufficient condition for nonviability whose negation is a necessary condition for observation-based viability." The flagged phrase now has **zero** occurrences in the source (the abstract's "sound sufficient conditions … (equivalently, necessary conditions for viability)" was already precise and is untouched). |
| E2 | 3.7 sustainability framing too rhetorical | §1 erosion passage compressed per the reviewer's own suggested form: "…because use draws on the base rather than on its yield: the measured quantity can be held up while the base declines, and partial observation may not detect the erosion until a floor is breached." The closing signal sentence is retained. |
| E3 | 3.3 notation section "too defensive" | §2.4 lead of the local-letters paragraph: "Some letters carry site-local meanings." → "A few letters carry local meanings, as declared here:". Symbol renames (d→δ, μ for multipliers, etc.) **rejected** — see §3. |

## 2. Already satisfied (9) — verified against v47/v48, no edit

| qwen item | Verification |
|-----------|--------------|
| 4.2 State the unifying idea early | §1.2 tail states it verbatim: "observation-based viability is the existence of one response --- admissible, safe, and recursively viable --- for every compatible state, and each certificate proves that a specific response correspondence is empty"; formalized as the selector principle (Prop. 1, §2.4). |
| 4.3 Clean hierarchy (5 levels) | The obstruction ladder (Prop., §3.6; Figure) is exactly this hierarchy with cross-references; Table 1 maps certificates to responses. Restructuring the sections would disturb the guarded ladder apparatus for no content change. |
| 4.4 Computational section (6 bullets) | Present, distributed: finite belief recursion = Thm 1 (§3.1) + the §8/§9 audits; polyhedral safe-control LP + Farkas = Theorem 4 (§3.3, v46); timing computation = §3.3/Remark (guaranteed survival time); certainly-safe set = Cor. (§4) computed in §8 (index bins; y ≥ 4). |
| 4.5 Three figures | Exceeded: seven figures; the three demanded are exactly fig:fibre (fibre crossing the safe boundary), fig:common_action (incompatible safe controls), fig:timing (q(t) vs T_obs); plus ladder, obstruction tree, coverage audit, CE trap. |
| 4.6 Estimation-tube precision | §2.3 thesis: "the epistemic kernel is the greatest recursively viable collection of information states in the sense of the estimation-space reduction cited in Section 5"; §5(b): estimation-space controls are common controls, and the common-action obstruction is the certificate that no jointly admissible selection exists. |
| 3.2 Over-qualification | All flagged phrases absent from the source ("no theorem of this paper…", "not re-derived here", "we do not claim the underlying elementary facts": 0 hits); the robust/non-robust contrast is declared once (§2.3 paragraph) plus single-clause glosses. |
| 3.4 Demote elementary results | Fibre criterion = Proposition; CE trap = Remark; epistemic-emptiness minimal construction = Proposition ("minimal construction"); exit certificate presented as base, "closed-form conditional", not a novelty claim. |
| 3.5 "Theorem 2 is artificial" | The demanded structure is in place: common-action theorem + minimal admissibility-only construction (Proposition) + hidden-mode Example 1. |
| 3.8 Appendix A | Zero appendix content in the main text; the bounded constructions live in Supplementary S3 ("Bounded constructions and scope remarks"). |

Also audited: "complete proof" phrasings (qwen 4.7) — the four main-text occurrences are accurate post-v46 (§3 proofs and the v46 §7 proofs are in Supplementary S1; Gap-9 wording fixed in v45). The H1.2 long-alternative cleanup was **rejected**: the hypothesis-registry form is load-bearing (both readings — adverse-selection and convexified — are cited by proofs), and the hypothesis-tag consistency is a recorded guardrail; the safe application of the Scope-clarification pattern was already made (v45, Helly).

## 3. Rejected with reasons (4)

| qwen item | Reason |
|-----------|--------|
| 4.1 Rename "robust epistemic kernel" | Established across v32–v47 and referenced from the companion lineage (ECOMOD); a global rename would touch every section and the supplementary for zero mathematical content, against the recorded guardrails (ladder cross-referencing; tag consistency). The definition is stated plainly (Def., §2.3) and §2.4 pins the structural symbols uniquely. |
| 3.3 Symbol renames (global) | Same guardrail: equation/hypothesis tags and cross-lineage stability; the collision paragraph enumerates the genuine collisions, which is the proportionate remedy. |
| 4.8 Reduce the number of named mechanisms | The five-plus-one mechanism structure is the paper's spine (abstract, §1.2, Table 1, ladder, conclusion); consolidating it would be a major restructuring, not an editorial pass. |
| 3.6 H4.2 reformulation via a HJI value function | Substantively already done: the guaranteed survival time σ\*(B₀) (Remark, §3.3) **is** the worst-case exit-time object, the certificate reads T_obs > σ\*(B₀), its checkable special cases are recorded, v46's Theorem 4 closes the polytope-declared case, and the v45 Helly Scope remark records the relaxed-reading scope. A differential-game restatement would duplicate σ\* under a new name. |

## 4. Batch-7 QC: wave6 v5→v10 dropped-segment register review

Register: `batch 7 (audits of agent arena 1 paper rewrites)/wave6/scan/paper2_obstruction_calculus.md` (124 transition-dropped segments across v5→v10; classifications: modified-with-replacement, no-close-replacement, weak-pairing). **Verdict: no load-bearing loss; no restoration required.** Verified retained in the current source: the fibre-invariance identity K = O⁻¹(O(K)) (§4 and Table 1 row); the "separate safety classes, not states" design consequence (§6.4, v10 replacement form); the abstract's "sound sufficient conditions … do not exhaust the complement"; the conclusion's five-mechanism summary; the abstract's kernel/tangency opener; the notation lead. The remaining no-close items are abstract/list condensations whose content moved to §1.2, and definitional restructurings superseded by the hypothesis registry.

## 5. Build and probes
- Tectonic 0.15.0; `main.pdf` 510,453 B, **19 pp** (v47: 19 pp; +164 bytes source). No numerical claims changed — the v46/v47 verification records remain the verification layer (12/12 + 12/12).
- pymupdf probes: E1/E2/E3 present; "necessity side" and "site-local" absent; v46/v47 content intact (Theorem 4, two-patch audit, worked belief-state instance); Tables 1–4 render; **0 unresolved `??`**.

## 6. Status after v48
**Track A is complete** (A1 ✓ v45; A4 ✓ v45+v47; A5+A6 ✓ v46; A3 ✓ v48). The Automatica manuscript is submission-ready pending the owner's venue decision. Next per roadmap sequencing: Track B (companion paper, B1–B5, including the LP-solver verification step), then C1–C2, D1.

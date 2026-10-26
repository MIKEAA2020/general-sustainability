# Paper06 prose revision plan — v75

**Status:** Implemented in Paper06 v75. The v74 release and all earlier releases remain unchanged.

**Purpose:** Correct the prose workflow before any further revision. The v74 plan's instruction to “use Grok as the structural base” and Gemini only “selectively” was the wrong hierarchy and directly invited register drift. This v75 plan supersedes that stylistic instruction; the source-checked claim audit in [`EDITORIAL_ASSESSMENT_AND_REVISION_PLAN_v74.md`](EDITORIAL_ASSESSMENT_AND_REVISION_PLAN_v74.md) remains a guardrail.

## 1. Source and prose hierarchy

1. **Manuscript truth:** Paper06 v74’s source, definitions, proofs, and stated scope control every factual and mathematical claim.
2. **Prose base:** For §§1.1–1.2, start from Gemini’s supplied humanized drafts themselves—not from a blank page and not from Grok’s wording. Keep Gemini’s readable sentence flow, reader-facing questions, transitions, and plain-language explanations wherever they remain accurate.
3. **Grok’s contribution:** Use Grok as a targeted precision and clarity check, not as the voice or structural template. Retain its strongest features where useful: compact definitions, the explicit “different plan may serve each weight” distinction, source-near literature framing, and the bounded description of a negative certificate relative to the declared menu.
4. **Source-check every generated claim:** Where Gemini or Grok exceeds the manuscript, make the smallest correction needed and record why. Do not silently replace Gemini’s readable passage with a fresh, generic academic rewrite.

## 2. Scope implemented in v75

The first pass covers **§§1.1–1.2**, the passages targeted by the earlier plan and supplied with Gemini drafts. This does not decide whether the Gemini abstract or other supplied passages should be revised later. The v75 rewrite keeps the manuscript’s overall order, citations, theorem sequence, and Table 1; it does not transplant the full-paper rewrite’s new architecture as a package.

### §1.1 — Compensability as an acceptance question

- Retain Gemini’s direct opening question about whether strength in one area can make up for failure in another, and its accessible contrast between compensatory and noncompensatory approaches.
- Preserve the manuscript’s literature framing and citations, but avoid claiming that “almost this entire body” has a “blind spot.” State the narrower, source-supported contrast: much of the cited work classifies aggregation at a fixed profile, while this paper studies transitions.
- Keep the distinction between weight elicitation, static Pareto-front limitations, and this paper’s acceptance-rule question. Use direct transitions rather than dense academic shorthand.
- Remove or qualify unsupported rhetoric such as “widely held intuition,” “completely fairly,” and “a disaster waiting to happen.” Do not imply that the model documents actual policy practice.

### §1.2 — Two acceptance semantics

- Keep Gemini’s accessible progression from the transition problem to the two quantifier orders. Introduce the formal objects in plain language before relying on notation.
- Define the shared conditions correctly: both `E_w(z)` and `E_typ(z)` require physical safety, destination attainment, and every declared disturbance. The weighted or typed floor test is applied over the full tube and the successor set.
- State the rules with their domains and predicates:
  - **Common-plan:** `∃a ∈ A ∀w ∈ W_+ : a ∈ E_w(z)`.
  - **Weight-adaptive:** `∀w ∈ W_+ ∃a_w ∈ A : a_w ∈ E_w(z)`.
  Here `W_+` is the full nonnegative cone with zero excluded, including axis weights; the plan may differ with `w`. Under the shared conditions and exact-tube semantics, `E_typ(z) = ⋂_{w ∈ W_+} E_w(z)`, so common-plan acceptance is equivalent to `∃a ∈ E_typ(z)`.
- Retain the here-and-now/wait-and-see comparison only as an analogy for quantifier order, not as a claim about observed auditors or policymakers. Keep Table 1; do not duplicate it with an ASCII diagram.
- Tie the concrete example to the **action-indexed witness model** and the exact four-plan menu. At `(x,s₁,s₂)=(1/2,6/5,6/5)`, `s₁+s₂=12/5 ≥ 2`: every weight in `W_+` licenses at least one of FAST or SLOW, yet no plan in the declared menu is typed-admissible. This is a result for that datum, disturbance class, and menu—not a general claim about all composite indices or real-world plans.
- Avoid “completely false,” “100% clean bill,” “illusion of safety,” “real-world options will cause a crisis,” and claims that the failure is “generic” unless the relevant theorem and its assumptions are stated alongside the claim.

## 3. Source checks and fidelity method

**Implementation-critical source anchors:** v74 source bundle `paper06_assessment_separation_v74_src/parts/01_setting.tex` (definitions of `E_typ`, `E_w`, `Tube`, `Succ`, and the full cone) and `parts/03_witness.tex` (Theorem 2, action-indexed menu, and canonical witness). The inherited v74 claim audit remains the broader scope check.

For this pass, the Gemini opening question, accessible transitions from fixed profiles to transitions, and clear explanation that the plan may differ by weight were carried into the manuscript. The claims about a literature-wide blind spot, an observed policy menu, and a “clean bill of health” were not carried over because they exceed the manuscript’s scope. Grok’s precision was used to check definitions and qualifications, not to replace Gemini’s prose.

## 4. Implementation and validation

Applied to a **new derivative from v74**. Main and modular §1.1–1.2 source blocks are synchronized. The full build, source comparison, PDF audit, and visual inspection are recorded in [`IMPLEMENTATION_RECORD_v75.md`](IMPLEMENTATION_RECORD_v75.md). The v74 release and earlier releases remain unchanged. The new derivative was pushed to the archive branch at the user’s request.

**Acceptance criterion:** The prose must be both source-accurate and recognizably based on Gemini’s humanized text. “Technically correct but returned to the assistant’s default academic register” is a failed revision, not an acceptable trade-off.

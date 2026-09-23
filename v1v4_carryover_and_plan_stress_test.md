# v1–v4 Carry-over Evaluation & Stress-Test of the Hybrid Synthesis Plan

This document answers two questions, in order:

1. **Q1** — What in the earlier versions v1–v4 is worth carrying into the final synthesis (as-is or adapted)?
2. **Q2** — A deep check of the hybrid plan's weakest points, including corrections to the plan as written in `rewrite_comparison_audit.md`.

Every claim below was verified against the files themselves in this session, not from memory.

---

# Part A — What v1–v4 contribute to the final synthesis

## A.1 The decisive finding

**The three AI drafts are rewrites of `p1.txt` only, and `p1.txt` does not contain the content that v4/v5 added. Therefore a hybrid assembled purely from the three drafts would *regress* relative to v4/v5.** The final synthesis must be a four-way merge: the drafts supply prose polish; v4/v5 supply the merited related work, the generalized rescue threshold, and the error-bound remark.

Specifically, the drafts faithfully preserve `p1.txt`'s **narrower** rescue-threshold statement ("for STAGED and x < 1, κ\* = 1 − x"), while v4/v5 prove the **generalized** closed form

> κ\*(z) = (1 − x)₊ · 1[x < 1, s₁ < 2, s₂ < 2] = (1 − x) · 1[z ∉ V_typ],

with a proof covering every z ∈ X₀. Adopting the drafts' §5.5 verbatim would silently drop the stronger proposition. (See Part B, Weak point 2.)

## A.2 Version-by-version evaluation

### v1 (`humanized_paper.md`) — plain-language reading

| Element | Verdict | Action |
|---|---|---|
| TL;DR ("boil down… 'fine!'") | Drop | Colloquial front-matter; conflicts with the formal-journal constraint |
| Meta banner ("A faithful, humanized version… nothing added or removed") | Drop | Self-commentary the user rejected |
| §2.4 "The characters in this story" (notation walkthrough) | Adapt | Already superseded by v5's 21-row glossary table; no new content |
| Bold-the-key-term-on-first-use technique | Keep (implicit) | Cheap readability device already present in v4/v5 |
| §1.2 minimax framing in plain words | Adapt | Superseded by the Improved-rewrite bullets and v4's §1.2 |

**Net:** nothing new to carry. v1 is fully superseded by v2–v5.

### v2 (`humanized_paper_v2.md`) — improved humanization

| Element | Verdict | Action |
|---|---|---|
| Two-reservoir (two-tank) analogy | Already handled | Lives in `cover_letter.md` per standing instruction; must stay out of the paper |
| **"Plain English → The math → Why it's true" three-part format per result** | **Adapt — real candidate** | A stronger gloss convention than v5's bare "In words." Candidate for the single standardized gloss device in the final version (see Part B, Weak point 6) |
| **Fully worked numeric example** at (x, s₁, s₂) = (½, 6/5, 6/5) | **Adapt — verified correct** | FAST/SLOW dip to −4/5; ρ₁ = 2/3, ρ₂ = 3/2; rescue contrast at (1, 6/5, 6/5). Arithmetic re-checked this session: **correct.** Usable as an illustration box or a Supplementary item (S-numbered), not as main-text clutter |
| Roadmap section | Drop | Superseded by v5's reader's guide |
| "What this is / What's new in v2" meta | Drop | Rejected change-log framing |

**Net:** two genuine carry-overs — the three-part gloss format and the (verified) worked example.

### v3 (`humanized_paper_v3.md`) — v2 + editorial related-work insertions + meta

v3 is superseded: its only unique content is the related-work insertion block, which migrated to v4/v5 in clean, non-meta form. Its one remaining value is **private editorial rationale, not text**: the v3 block records *which claim each citation supports*, e.g.

- Aubin & Catté (2002) → the fixed-point/algebraic character of viability kernels and capture basins; the Saint-Pierre iteration is exactly that fixed-point iteration → backs the §5.2 "Established" paragraph.
- Cardaliaguet (1996); Cardaliaguet–Quincampoix–Saint-Pierre (1999) → the discriminating-kernel (reach/avoid game) reading of the assessor–planner gap → backs the §4.10/4.11 pure-vs-mixed-strategies remark.
- O'Neill et al. (2018); Fanning et al. (2022) → separately-checked floors in the doughnut literature, no country inside the safe space → backs §5.4 policy implication "Third."
- Lade et al. (2020) → interacting planetary-boundary processes → backs the §5.3 coupled-shock scope caveat.
- Fabian et al. (2010) → error-bound modulus → backs the §5.5 remark.

**Action:** keep this "citation → claim it supports" mapping as an internal checklist for the final assembly (so no related-work sentence is decorative); do **not** carry the v3 meta framing ("Editorial additions — not in the original") — the user rejected it, and v4 already removed it.

### v4 (`humanized_paper_v4.md`) — clean formal journal version

This is the highest-value source for the final synthesis, precisely because it holds everything the three AI drafts lack:

| Element | Verdict | Action |
|---|---|---|
| **§5.5 generalized κ\* closed form + proof** | **Carry as-is** | Strictly stronger than `p1.txt` and all three drafts |
| **§5.5 error-bound modulus remark (Fabian et al. 2010)** | **Carry as-is** | The honest formal-bridge note; not in the drafts |
| **§5.2 related-work insertions** (Aubin & Catté 2002; Cardaliaguet 1996 + CQSP 1999 in the §4.10/4.11 remark; O'Neill 2018 + Fanning 2022 in §5.4; Lade 2020 in §5.3) | **Carry as-is** | Verified cited in-body in v4; none appear in the drafts |
| §5.2 "Established / Proved here / Novelty qualification" format | **Carry as-is** | Present in `p1.txt` too; the anti-decorative, non-strawman related-work treatment |
| Abstract (humanized, reflects κ\*, blend results, merited related work) | **Carry as-is** | The drafts have no abstract; `p1.txt`'s is pre-humanization |
| Title/author block, keywords, MSC, References, Declarations (data availability; competing interest; AI disclosure) | **Carry as-is** | None exists in the drafts |

**Net:** v4/v5 are the content backbone; the drafts are the polish layer. The plan must treat them that way.

---

# Part B — Deep check: the hybrid plan's weakest points

Ranked by severity. "The plan" = §4–§5 of `rewrite_comparison_audit.md`.

### Weak point 1 — **The plan's source pool is incomplete (critical).**
The hybrid table in the audit draws every section from one of the three drafts. But the merited related work, the generalized κ\*, and the error-bound remark exist **only** in v4/v5 — verified absent from all seven draft passes and absent from `p1.txt`. As written, the plan produces a final version that is *worse* than v4/v5 on exactly the content the user most wanted integrated.
**Fix:** restate the assembly as a four-way merge. Related work, κ\*, error-bound remark, abstract, references, declarations → **v4/v5**. Body prose → drafts (polish only). Formal content re-check → `p1.txt`.

### Weak point 2 — **One cell of my own table is wrong: §5.5 (critical, self-corrected).**
The audit table assigns §5.5 to "DeepSeek verbatim." DeepSeek (and every draft) preserves `p1.txt`'s narrower κ\* statement. v4/v5's generalized closed form is strictly stronger and should be the §5.5 source. This is a concrete defect in the plan, corrected here.
**Fix:** §5.5 = v4/v5 (generalized κ\* + proof + error-bound remark + five data-requirement items). The drafts contribute nothing to §5.5.

### Weak point 3 — **Output format is unspecified (high).**
The drafts are LaTeX body fragments; v1–v5 are Markdown. The audit says "normalize typography to LaTeX," but the actual deliverables the user has been reviewing are `.md`. These imply different end states: a submission-ready `.tex` (requires reconstructing `\documentclass`, bibliography via BibTeX, figure environments) versus a Markdown manuscript (consistent with v1–v5, previewable in-app).
**Fix:** decide now. Recommendation: **Markdown** (consistent with all prior deliverables and the in-app preview; the body formal content is already math-typeset in v5). A LaTeX export can be a later mechanical step. If the user wants a `.tex`, that is a separate, larger task and should be stated explicitly.

### Weak point 4 — **Register seams from mixing three voices (high).**
Gemini's compressed/interpretive prose (§1, contributions, Takeaways), DeepSeek's verbatim proofs (§4), and v4/v5's formal journal register (§5) differ in rhythm, person, tense, and epistemic precision ("does not by itself prove" vs "does not replace the general proofs"). Assembling per-section best-of-breed without a normalization pass will read as patchwork.
**Fix:** designate **v4/v5's formal journal register** as the single voice; treat every borrowed passage as *material to be rewritten into that register*, not final text. One full-consistency pass (tense, person, dash conventions, "the paper/we" policy) after assembly.

### Weak point 5 — **The fidelity audit is presence-based, not equivalence-based (medium-high).**
The audit verified that formulas, citations, and numbering *exist* in each pass, and I deep-read the Gemini passes' Theorem 5 proof. It did not do a line-by-line proof-equivalence check for Theorem 7, Theorem 8, Proposition 9, Remark 6, or the §3/§4 definitions across all seven passes. Risk is low (all spot-checks passed) but nonzero.
**Fix:** before assembly, one full proof-level diff of the chosen backbone against `p1.txt` — every definition, statement, and proof, not just the display formulas.

### Weak point 6 — **The gloss convention is undecided (medium).**
Three incompatible candidates exist: v5's "In words" after *every* result (12 glosses); Gemini's two "Takeaway." boxes (after Theorem 5 and Theorem 8/Prop 9); the original/v2's single unnumbered "Remark." (after Theorem 5). The plan adopts Gemini's device but never says *how many* glosses or *which* results get them — and v2 offers a fourth option (the three-part "Plain English → The math → Why it's true").
**Fix:** pick **one** convention. Recommendation: **one gloss after each of the five headline results** (Remark 1, Prop 3(ii), Theorem 5, Theorem 8, Prop 9), drafted in v2's three-part style but labeled consistently (e.g., "In words."), replacing both Gemini's "Takeaway." and the original's "Remark." so nothing is duplicated.

### Weak point 7 — **Front matter source unstated (medium).**
The audit says "re-attach abstract/title/bibliography from `p1.txt`." `p1.txt`'s abstract is pre-humanization and its bibliography lacks the six added landmarks. v4/v5's abstract and references are the correct sources.
**Fix:** abstract, title block, keywords, MSC → v5; references → v4/v5's full list (supersedes `p1.txt`'s); declarations → v5. The drafts supply none of this.

### Weak point 8 — **Duplication risk: four overlapping "explain it in words" devices (medium).**
v2's worked example, v5's "In words" glosses, Gemini's "Takeaway." boxes, and the original's "Remark." all restate the same results. Keeping more than one bloats the paper and reads as repetition.
**Fix:** consolidate to exactly one gloss device (Weak point 6) plus at most one worked example (the verified v2 example, as a Supplementary item), and one glossary (v5's table). No other restatement devices.

### Weak point 9 — **The blocking decisions are still open (process).**
The audit ends with two open questions (gloss label; backbone file). The deep check adds two more that must be decided by fiat rather than asked: output format (Weak point 3) and the related-work source pool (Weak point 1). None of the four should block assembly any longer — the recommendations above resolve them.

### Weak point 10 — **The drafts' shared structural gaps are under-priced (low-medium).**
All three drafts are body-only fragments (no abstract/title/declarations/references). "Re-attach" is real editing, not copy-paste: the humanized abstract must be re-harmonized with the hybridized body (e.g., if a draft's phrasing for the blend result is adopted, the abstract must match). Budget for a front-matter harmonization pass.

---

# Amended synthesis recipe (supersedes §4–§5 of the audit)

1. **Content spine** = v5 (already complete: abstract, glossary, reader's guide, "In words" glosses, generalized κ\*, error-bound remark, full related work, references, declarations).
2. **Prose upgrades from the drafts (polish only):**
   - §1.1–1.3 intro and minimax bullets → Improved rewrite (v2, second pass), converted to Markdown and to v4/v5 register.
   - Contributions → Gemini's enumerated `\item` list, with DeepSeek's exact wording for items (iv) and (vii).
   - Theorem 5(7) four-violation list → Improved rewrite (keeps the exhaustive list with emphasis).
   - Figure-caption boundary-convention wording → Improved rewrite.
   - Disturbance-convention box and boundary-behavior paragraph → Gemini (adapted to v4/v5 register).
3. **Do not source from the drafts:** §5.2 related work, §5.5 (κ\* + error-bound remark), §4.9 machine-verification caveat (keep v4/v5's "does not by itself prove" wording), abstract, references, declarations.
4. **Gloss convention:** one "In words" gloss after each of the five headline results (Remark 1, Prop 3(ii), Theorem 5, Theorem 8, Prop 9), in v2's three-part style; delete Gemini's "Takeaway." labels and the original's "Remark." summary to avoid duplication.
5. **Pre-assembly verification:** one proof-level diff of the chosen backbone against `p1.txt` (definitions + every proof), extending the presence-based audit already done.
6. **Post-assembly passes:** register normalization (single voice = v4/v5); typography (Markdown, Unicode math as in v5); front-matter harmonization (abstract ↔ body).
7. **Format:** Markdown (consistent with v1–v5). LaTeX export only if explicitly requested.

**Open items now reduced to zero hard blockers.** The two questions from the audit (§5) are answered by fiat above; if the user prefers a different gloss label ("Remark." vs "In words." vs "Takeaway.") or a different backbone, those are one-line swaps, not structural changes.

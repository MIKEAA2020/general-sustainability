# Joint Synthesis v3 — ADDENDUM: remaining audit points found in unexamined places
## (v2 remains the base; this completes it. v2 + v3 = the full joint synthesis.)

**What this pass did:** re-read my audit file verbatim (nothing missing there — v2's register F.1 already covers all Tier 1–4 rows and the "already good" list); ran a **second, deeper sub-audit** on the paper (phrase battery + structural/LaTeX checks I never ran); and examined **two paper-2 files on GitHub I had never opened** (`build_paper2_v15.py`, `COVER_LETTER_paper2_obstruction_calculus_SVVA.md`) plus the full repo listing. This surfaced **6 new audit points** and **3 recovered items** from my 8-direction answer that v2 had dropped or softened.

---

# G. New audit points (with evidence)

## G.1 Hardcoded theorem numbering — renumbering hazard (LaTeX/consistency)
**Evidence:** all numbered results are hardcoded: `\textbf{Theorem 1}`…`\textbf{Theorem 5}`, `\textbf{Corollary 6}`, `\textbf{Remark 1}`, `\textbf{Example 1}`, `\textbf{Definition 1,2}` — with **no `amsthm`, no `\newtheorem`, no `\label`/`\ref`**. Every in-prose reference ("Theorem 3's safety case", "Theorem 4 refines Theorem 3", etc.) is a hardcoded string.
**Why it matters:** the synthesis **itself** mandates demoting Theorem 2 → example and Theorem 5 → proposition (D.1.3). Under hardcoded numbering that means hand-renumbering Theorems 3→2, 4→3, 5→4, Corollary 6→5 and hunting every hardcoded string; a missed one silently breaks. 
**Fix:** introduce `\newtheorem`/`\label`/`\ref` (or at minimum `\ref`) so renumbering is automatic. This also converts Qwen's "low-priority LaTeX polish" into a **blocking prerequisite** of the D.1.3 demotions. → fold into **D.1 (Layer 1), new item D.1.10**, and into the v16 execution step.

## G.2 §4.2 "Output-feedback form" is a 3-sentence stub
**Evidence:** L969–976 contains a subsection whose entire body is: "Theorem 3 covers the output-feedback form directly…" — one paragraph, no new content, duplicating §6.3.
**Fix:** delete §4.2; fold its single sentence into §4.1 or §6.3. → **D.1 (Layer 1), new item D.1.11** (structural).

## G.3 "a fortiori" hyphenation inconsistency
**Evidence:** "a-fortiori caveat" ×3 (L300, L397, L465) vs "transfer a fortiori" (L402). Two spellings in one document.
**Fix:** standardize (use "a fortiori" unhyphenated, or hyphenate consistently). → **D.1.7** (prose surgery, minor).

## G.4 Build-script evidence: meta-commentary is *persistent*, not one-off
**Evidence:** `build_paper2_v15.py` (GitHub) states its own job: "strip change-log residue, internal dialogue, meta-commentary, chat-history register, and naive over-hedging." It specifically rewrites a "**DEFINED-NOT-THEOREM object**" phrase — yet v15 **still contains** "This is a definition, not a theorem" ×2 and "no theorem of this paper is stated for it" ×2. The strip has been run at least once (v14→v15) and the residue regenerated/remained.
**Implication:** D.1.4's cut list must be executed **at the source text** (a full pass on v15), not via another build-script strip, and the resulting file must be grepped to zero on those phrases. Also confirms the header comment "(cleaned revision)" (T1.9) is diary language that survives builds. → strengthens **D.1.4 + D.1.9**; add a **zero-grep acceptance check** to the execution plan.

## G.5 Cover letter overclaims — cross-document contradiction (NEW category)
**Evidence:** `COVER_LETTER_paper2_obstruction_calculus_SVVA.md` states, as its central claim:
> "the *necessity* side, i.e., certifying that no observation-based policy is viable, has lacked a comparable instrument. **This paper supplies it**"
> "for a given observation structure it says **whether** viability is possible, **why not** when it is impossible"
> "To my knowledge, the **necessity side** of viability under incomplete observation has not previously been given a constructive, certificate-based instrument."

This directly contradicts the paper's own abstract ("sound sufficient conditions for nonviability and **do not exhaust** the complement of the epistemic kernel") and verification-table row 1. The paper hedges correctly; the cover letter does not.
**Fix:** the claim-reframe (D.1.1) must be applied **to the cover letter in the same revision** — otherwise a referee sees the overclaim at first contact. → new **D.1.12** (cross-document sync) + execution-plan note.

## G.6 No paper-2 supplementary exists; code-availability contradicts paper 1 (cross-corpus)
**Evidence:** repo listing shows `paper1_supplementary*.md`, `paper3_supplementary*.md`, `paper4_supplementary*.md`, `paper5_supplementary*.md` — **no `paper2_supplementary*`**. Meanwhile:
- the cover letter claims "the manuscript is self-contained with a **supplementary/scope appendix**" (there is none, unless it means Appendix A);
- the paper's Code availability says "available from the author **on request**" — while paper 1 archives to Zenodo (22545740).
**Fix:** align with the corpus convention: either archive paper-2 verification code (or a short supplementary) to Zenodo and cite the record, or change the sentence to "No code was used or produced; all constructions are symbolic" and drop the cover letter's supplementary claim. → strengthens **D.1.9 (T4.3)**; add explicit **D.1.13**.

---

# H. Recovered items from my 8-direction answer (softened or dropped in v2)

## H.1 The decomposition/taxonomy-closure theorem (my #1's core statement)
v2 reduced #1 to "finite-horizon completeness + game-value middle ground." The *specific* statement I originally proposed was stronger and should survive in the horizon layer:
> "B ∉ ERViab iff (under the paper's regularity) the **belief-space Nagumo condition** fails at B; and every failure is witnessed by one of the four dynamic mechanisms."
i.e., the infinite-horizon belief-space tangency characterization that makes **Theorems 3 and 4 corollaries of one condition** — a structure theorem, not a list. → add to **D.4** as a named horizon direction ("taxonomy closure / belief-space Nagumo unification").

## H.2 Optimal-coarsening design result (my #4's specific claim)
v2's D.3.19 has the cost-minimization formulation + minimal-refinement rule, but dropped:
> "under convex observation costs, the optimal observation **coarsens exactly along the safe-control partition** (Theorem 3's classes)."
→ add to **D.3.19** as the one structural design theorem.

## H.3 Two-regulator example (my #6's concrete instance)
v2's institutional line is generic. Recover the concrete opener:
> "two regulators with **disjoint observations** cannot jointly enforce a floor that either could enforce with the other's observation."
→ add to **D.4** institutional-multi-agent line as the first clean theorem to attempt.

---

# I. Updated register (supersedes F.1–F.3 where noted; F.4 added)

## I.1 Readability-audit items — CONFIRMED complete
Re-reading the audit file verbatim confirms v2's F.1 already covers **all** Tier 1 (9 items), Tier 2 (3), Tier 3 (7), Tier 4 (6), the "already good" list, and the suggested order of work. **No Tier 1–4 item was missing.** The new items G.1–G.3 are *beyond* the original audit (found by the deeper pass) and are added to Layer 1 as D.1.10–D.1.11 + a D.1.7 sub-point.

## I.2 Sub-audit numbers — COMPLETED (all counts, both passes)
First pass (already in v2 F.3): abstract **309 words**; em-dashes **157**; `IRViab` **4** occurrences (3 definitions); `EViab` **4**; "middle ground" **4**; "not proved here" **2**; "genuine" **3**; "exactly" **7**; "precisely" **1**; `\linenumbers` on; "companion" in-text **1**.
Second pass (this turn): "no theorem of this paper is stated" **2**; "definition, not a theorem" **2**; "contrast class" **4**; "a-fortiori" **3** + "a fortiori" **1** (hyphenation inconsistency, G.3); "not reproduced"/"cited, not reproduced" **1**; "not a theorem" **2**; "institutionally admissible" **3**; "mutatis mutandis" **1** (legitimate, keep); "merely" **2** (natural usage, keep); theorem environments **0** (hardcoded, G.1); §4.2 stub **1** (G.2).

## I.3 Verification table — CONFIRMED complete
All 22 rows of Part A are carried into v2 (Part A verbatim + conclusions folded into D.1–D.4 and Part C). **No row was dropped.** G.5–G.6 are *new* verification findings (cross-document), recorded as rows 23–24 below:
| 23 | "Cover letter supplies the necessity side" (cover letter) | **✗ contradicts paper's own abstract** | Paper: "do not exhaust the complement." Reframe cover letter in lockstep (D.1.12). |
| 24 | "self-contained with a supplementary/scope appendix" (cover letter) | **✗ no paper2_supplementary exists in repo** | Corpus has p1/p3/p4/p5 supplementaries; p2 has none (D.1.13). |

## I.4 My 8 directions — COMPLETED (register F.2 amended)
v2's F.2 already placed #1→D.2+D.4, #2→D.3.16, #3→D.4+decision, #4→D.3.19, #5→D.4, #6→D.4, #7→D.4, #8→D.4, plus the top-3 and the "least interesting gaps" verdict. The **three softenings** are now recovered: H.1 (decomposition theorem), H.2 (optimal coarsening), H.3 (two-regulator example). F.2 is thereby complete.

---

# J. Updated execution plan (amends Part E)

| Revision | Contents (v2 list **+ additions in bold**) |
|---|---|
| **v16** (claim + style) | Claim reframe **including cover-letter sync (D.1.12)**; Tier-1 cut list **with zero-grep acceptance check (G.4)**; hedging consolidation; symbol renames; prose surgery (+**a-fortiori standardization G.3**); abstract ≤265; §1.1 compress; Tier-4 housekeeping (drop "companion"; **code availability → Zenodo-or-"no code" (D.1.13)**; `\linenumbers`); **introduce `amsthm`+`\label`/`\ref` BEFORE the demotions (G.1/D.1.10)**; **delete §4.2 stub (D.1.11)**. |
| **v17** (spine) | Semantic conventions; `Pre_Δ` + `Succ`+⊥; finite-horizon completeness + obstruction tree; A–E taxonomy; `σ*` timing + comparison function; uniform-margin lemma. |
| **v18** (computational) | Farkas worked example; common-action gap g(B) + margins; algorithm box; integrated example; figures; partial-order monotonicity; cost-min design problem **+ optimal-coarsening claim (H.2)**; distance-to-viability. |
| **Outlook / companion** | σ-algebra + approximate certification; Π_CE/Witsenhausen; SOS; HJI; institutional multi-agent (**+ two-regulator example H.3**); **taxonomy-closure / belief-space Nagumo unification (H.1)**. |

**New pre-submission gate items (amend Qwen's 7):**
(7) Cover letter and abstract carry the *same* reframed claim (no "necessity side" anywhere, including the letter).
(8) `grep -c "no theorem of this paper\|definition, not a theorem\|not re-derived here\|cited, not reproduced"` returns **0** on the .tex.
(9) All numbered results reference via `\ref` (renumbering-proof) before the Thm 2/5 demotions.
(10) Code-availability statement matches the corpus convention (Zenodo record or explicit "no code"); cover letter's "supplementary" claim removed or a supplementary created.

---

# K. Net answer

Yes — there were remaining points, in places I hadn't looked:

1. **Within the paper, via a deeper grep** (not in my first audit): hardcoded theorem numbering (renumbering hazard), the §4.2 stub, and the a-fortiori hyphenation split.
2. **In the build script** (`build_paper2_v15.py`): proof that meta-commentary is *persistent* (a v14→v15 strip still left "definition, not a theorem" ×2), so the fix must be a zero-grep source pass, not another strip.
3. **In the cover letter** (`COVER_LETTER_paper2_SVVA.md`): it overclaims the "necessity side" in contradiction with the paper's own abstract, and claims a supplementary that does not exist.
4. **In the repo listing:** no `paper2_supplementary*` while papers 1/3/4/5 all have one, and paper 2's "code on request" contradicts paper 1's Zenodo archive.
5. **In my own 8-direction answer:** three specifics v2 had softened — the decomposition/Nagumo-unification theorem (H.1), the optimal-coarsening design result (H.2), and the two-regulator example (H.3).

All are now folded into the joint synthesis as G.1–G.6, H.1–H.3, register I.1–I.4, verification rows 23–24, and the amended execution plan J. **v2 (base) + v3 (this addendum) = the complete joint synthesis.**

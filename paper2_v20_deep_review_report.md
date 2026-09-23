# Deep review report — paper 2 v20 (five questions, answered with data)

## 1. Supplementary — NOT merited (excluded)
Test: a supplementary must hold something the main text cannot: omitted proofs, code, or data. Paper 2 has **complete proofs in the main text** (7 proof blocks), **no code** ("No code was used or produced" — consistent with the Zenodo code-availability convention), and is **self-contained at 25 pages**. Papers 1/3/4/5 have supplementaries because they carry verification code or auxiliary computations; paper 2 has neither to carry. A supplementary here would be padding. **Decision: none.**
_(If you later want corpus symmetry, the only defensible supplementary content would be a spelled-out backward-recursion algorithm + a second worked example; it is not merited now.)_

## 2. Deep scan — remnants / redundancy / flow (results + fixes)
**Remnants:** zero. The full old-meta battery is clean — "necessity side", "definition, not a theorem", "no theorem of this paper", "not re-derived here", "cited, not reproduced", "not itself an exhibit", "not proved here", "contrast class only", "site-local", "(Cited)", "cleaned revision" all = 0. No `\graphicspath` leftover (removed v19). No hardcoded theorem numbers. No double spaces in rendered output ("the the" / "and and" / ",," / " ," = 0), no comma-splice sentence starts (", The / This / There" = 0).

**Redundancy found & judged:**
- "epistemic kernel" ×16 — legitimate (the object of study). No change.
- "contrast class" ×4 → reviewed: one substantive statement (§2.3) + two symbol-glossary cross-refs (§2.1, §2.4) + one pointer; the pointer "defined below" was loose → **tightened** to "the non-robust contrast class."
- "certainly-safe set" ×6, "selector principle" ×2, "middle ground" ×1 — all legitimate. No change.
- First-person: "we" ×1 ("We use ERViab throughout"), "our" ×1 ("To our knowledge") — appropriately impersonal.

**Flow fixes made:**
- "which is why" ×2 (my v18 additions) → "hence" / "completeness is therefore claimed…" (**fixed**).
- §3.5 ended with the obstruction-tree paragraph and no instance; now closes with a **one-step instance** (§1) so the recursion theorem is concrete.
- §4.2 (CE trap) had no visual while the other mechanisms do; now has a figure, and the §4.2→§5 handoff is a clean figure-then-rule transition.

**Noted, not mass-edited:** em-dash density is **145** (down from 157 in v15, but up from 130 after v16.2 because my v17–v19 additions used them). Remaining ones are largely genuine appositive/parenthetical asides; an aggressive further cut risks flattening the prose. Flagged as an optional dedicated pass if you want it.

## 3. Additional genuine insights / pedagogical content
**New theorems: NO.** The mathematically merited content is complete after v16–v19. The remaining candidate theorems — belief-space Nagumo unification, SOS/Putinar certificates, probabilistic/approximate certification, HJI-viscosity characterization, optimal coarsening, distance-to-viability — each fails the sharp test *for this paper* (they re-derive the cited estimation-tube reduction, add notation without a result, or belong to a companion). Documented in the earlier verdicts.

**Pedagogical: ONE merited addition (implemented).** Theorem 4 (finite-horizon backward recursion) was the paper's only algorithmic result stated *without an instance*. Added a compact **one-step obstruction tree** re-using Example 1 (hidden mode): two states, two hidden branches, `Post(B₀,+1,−1) ∉ W₀` for both actions, tree = root + two adversary edges terminating in `z<0`. It ties Theorem 4 back to Theorem 2 in the finite-horizon language. (Verified correct by hand.)

## 4. Additional tables / figures / visual aids
- **Certificate summary table (Table 1, §6.1) — added.** Rows: the six mechanisms + finite-horizon recursion; columns: certificate / emptied response correspondence / **design consequence (§6.4)**. The design-consequence column is genuinely new synthesis — it makes explicit, in one place, the "consequences … are drawn" promise the abstract makes, using the ladder notation to unify the table with Proposition 3.
- **Certainty-equivalence figure (Fig 4) — added.** The one mechanism still without a visual: flat `u=g(S)` vs. drifting `u=g(Ŝ)`, crossing `S*`. Completes the figure set (each mechanism is now geometric).
- **Not added:** a nested-boxes "ladder" figure — the summary table + Proposition 3's displayed inclusion chain already carry the inclusion structure; a fourth abstract diagram would be decorative.

## 5. Meta-commentary / self-referential / apology scan
Full battery run on v19 (and re-verified on v20). **Clean:** "note that", "observe that", "we emphasize", "it is worth", "the reader", "we remind", "we now", "let us", "in this section", "for completeness", "recall that", "as shown", "unfortunately", "admittedly", "we do not claim", "to the best of our", "we are not aware", "beyond the scope", "we leave", "future work", "loosely speaking", "roughly", "somewhat", "arguably", "for the first time", "novel", "key contribution", "importantly", "crucially" — **all 0**. The only two meta-adjacent phrases were the "which is why" ×2 (fixed). One "informally" remains and is legitimate (it describes Martinez-Alier et al., not the paper). Self-reference is modest: "this paper" ×5 + "This paper" ×3 + "the paper" ×3 across 25 pages.

## Net (v20)
25 pages; 0 unresolved refs; 4 figures; 1 table; abstract 264 words; only the pre-existing 57.86pt overfull box (inherited from v15, unchanged). Pushed: v20 tex/pdf, Fig 4, build script.

Chain: v15 → v16 → v16.1 → v16.2 → v17 → v18 → v19 → v20, all preserved.

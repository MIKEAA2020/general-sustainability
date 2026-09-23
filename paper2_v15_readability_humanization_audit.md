# Readability & Humanization Audit — `paper2_obstruction_calculus_v15.tex`

**Scope:** "An Obstruction Calculus for Viability under Incomplete Observation" (86,796 bytes, 1,445 lines).
**Verdict:** The mathematical content is strong and the humanizing glosses (management/ecological readings, §6.4 governance consequences) are genuinely good. The main problems are **(1) pervasive meta-commentary** — authorial stage directions that read like drafting notes — and **(2) prose density** — 157 em-dashes, nested parentheticals, and triple-stated definitions. These are exactly the patterns the project's standing style rules ("no meta-commentary / no change-log artifacts", "humanized prose") target.

---

## Tier 1 — Meta-commentary & change-log artifacts (must fix)

These are sentences about *the paper itself* rather than about the mathematics. They read as drafting notes and should be removed or folded into ordinary scholarly scoping.

| # | Location | Text | Problem / fix |
|---|----------|------|----------------|
| 1 | **§2.1 (L309), §2.4 (L465), §6.4 (L1219)** | `IRViab` defined **three times, near-verbatim**: "…defined as the viability kernel of the system whose command correspondence is restricted to the institutionally admissible set… This is a definition, not a theorem… / a definition with no theorem claimed for it…" | Define **once** in §2.1; elsewhere write "the institutionally restricted kernel `IRViab_J(V)` of §2.1". Delete all "this is a definition, not a theorem" clauses. |
| 2 | **§2.1 (L300), §2.3 (L397, L403), §2.4 (L465)** | `EViab` introduced 4× as "defined as a **contrast class only**… **no theorem of this paper is stated for it**." | State the non-robust contrast class **once**; thereafter "the non-robust contrast class `EViab` (defined in §2.3)". The phrase "no theorem of this paper is stated for it" is pure stage direction. |
| 3 | **§5 heading (L1024)** | "5. The Sufficiency Landscape **(Cited)**" | Remove "(Cited)" from the heading — it's a revision artifact. |
| 4 | **§5 opening (L1029)** | "Their proofs repeat established literature and are **cited, not reproduced**." | Rewrite as content: "The following results are standard; proofs appear in the cited sources." (no "not reproduced"). |
| 5 | **§1.2 (L219)** | "Theorem 5 is the converse-side characterization of the certification limit itself, **not itself an exhibit of failure**." | Delete the clause. |
| 6 | **§2.3 (L413)** | "the epistemic kernel is the greatest recursively viable collection… **not re-derived here**" | Delete "not re-derived here". |
| 7 | **Appendix A (L1288)** | "They are stated in full with their scope remarks; **none of them is stated as a theorem of the main text**." | Delete; the appendix heading already says "constructions and scope remarks". |
| 8 | **Thm 1 (L506) + proof (L562)** | The "locally Lipschitz case is an extension **not proved here**" caveat appears **twice**. | State once (hypothesis), delete from the proof. |
| 9 | **Header (L2)** | "% …Revision v15 (**cleaned revision** with line numbers for review)…" + `\linenumbers` (L18) | Doesn't print (comment), but "cleaned revision" is diary language. For final submission, drop `\linenumbers` (or keep only if the target journal requires numbered review copy). |

---

## Tier 2 — Over-hedging / defensive scoping (should fix)

The incompleteness disclaimer is legitimate but is currently stated ~5 times, and two "we do not claim…" formulations read as self-defense rather than scoping.

| # | Location | Text | Fix |
|---|----------|------|-----|
| 1 | Abstract (L44); §5 (L1040, L1067); §6.5 (L1235); §7 (L1260) | "sound… and **do not exhaust** the complement…"; "the **middle ground**… is open" (×4 total) | Keep **once** in the abstract and **once** in §6.5 (Limitations). Delete the repeats in §5 and §7. |
| 2 | §1.3 (L216) | "…we do not claim the underlying elementary facts (quantifier commutation; Dini comparison) **as new**." | Replace with a positive statement of what *is* new ("new here are the certificates of Theorems 3–5…"). |
| 3 | §5 (L1040, L1067) | "a problem that satisfies neither is the open middle ground" ≈ "These results **delimit the middle ground**" | Duplicated; keep one. |

---

## Tier 3 — Readability / humanization (density)

1. **157 em-dashes in 86 KB** — prose is constantly interrupted. Convert most `---` asides into separate sentences or commas; keep em-dashes only for genuine appositive asides (~1–2 per paragraph max).
2. **§2.3 a-fortiori paragraph (L398–410)** — one run-on sentence with two nested em-dash interruptions and the phrase "the existential contrast class:" mid-sentence. Rewrite as 3–4 short sentences:
   > "The theorems are stated for the robust kernel `ERViab`. They do not transfer a fortiori to the non-robust contrast class `EViab`, in which some disturbance realization keeps every compatible trajectory in `V`. Since the robust kernel is contained in the non-robust one, a policy may exist there that no robust policy survives."
3. **§2.4 "Some letters carry site-local meanings" (L470–490)** — a dense paragraph of symbol bookkeeping. Recommend a compact table (Symbol | Meaning | Where) instead of prose.
4. **Definition 1 (L380–395)** — the quantifier-order parenthetical is important but buried in one huge parenthetical. Break it out into its own sentence or a remark.
5. **§2.2 "Two levels of the tangency condition" (L330–350)** — the local/global distinction is never crisply labeled; the reader must infer which is which. Add explicit labels: "**(i) local reading** … **(ii) kernel reading**".
6. **Word-choice tics:** "genuine" ×3, "exactly" ×7, "precisely" ×1 — trim a few for a less repetitive surface.
7. **Redundant framing in §1.1:** "Floors in sustainability assessment are typically constraints… Such a base can erode while measured output is maintained…" — the two-paragraph "base vs yield" gloss is good content but drifts from the section's job (stating the problem); consider compressing into one tight paragraph.

---

## Tier 4 — Conventions & consistency

| # | Item | Finding | Recommendation |
|---|------|---------|----------------|
| 1 | **Abstract length** | **309 words** (paper 1's standard was ≤265). | Trim to ~220–250; the second paragraph packs all six mechanisms into one 200-word sentence-chain. Split into 3–4 sentences. |
| 2 | **L766** | "the **companion** assessment-separation analysis (Abaee, 2026)" | Drop "companion": "the assessment-separation analysis of Abaee (2026)". The reference list already carries the full DOI — good. |
| 3 | **Code availability (L1438)** | "available from the author on request" — inconsistent with paper 1's Zenodo archive. | If code exists, archive it (Zenodo) and cite the record; otherwise write "No code was used or produced." |
| 4 | **Data availability (L1436)** | "No data were used; all constructions are symbolic." | ✓ Correct and consistent with the data-availability discussion. Keep. |
| 5 | **AI declaration (L1442)** | "GLM (Z.ai), Qwen (Alibaba Cloud) and DeepSeek AI assisted with drafting and iterative review." | ✓ Brief and at manuscript end — matches the standing rule. Keep. |
| 6 | **Citations** | All author–year + venue + DOI; no shorthand letters. | ✓ Passes. |

---

## What is already good (do not regress)

- **No** "In words" / "Takeaway" / "Reader's guide" artifacts anywhere. ✓
- **§1.2 Contributions** list is clear, ordered, and each mechanism is one bullet. ✓
- **Humanizing glosses** — "In management terms…", "In ecological terms…", "the two-action skeleton of every 'the stock is either recovering or collapsing' situation" — are excellent and should be preserved. ✓
- **§6.4 Consequences** (Timing / Coarseness / Aggregation / Bias / Institutions) is concrete, decision-oriented, and well written. ✓
- **§6.5 Limitations** honestly scopes the certificates (sufficient-not-necessary, set-membership semantics, finite-dimensional). ✓
- **§2.4 notation "no other letter serves either role"** (𝒥 vs ℐ) is helpful disambiguation — keep, but see Tier 3.3 for the bookkeeping paragraph.

---

## Suggested order of work

1. Tier 1 (delete/repoint meta-commentary) — mechanical, highest impact.
2. Tier 2 (consolidate hedging to 2 statements).
3. Abstract trim to ≤265 words.
4. Tier 3 prose surgery (em-dashes, the two worst paragraphs, notation table).
5. Tier 4 housekeeping (companion wording, code-availability, `\linenumbers`).

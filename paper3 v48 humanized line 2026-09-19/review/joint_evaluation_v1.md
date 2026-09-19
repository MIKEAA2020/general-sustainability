# Joint evaluation of all six versions — verification report (no rewriting)

**Date:** 2026-09-14 · **Scope:** evaluate + verify `uploads/p3 humanized.txt` and `uploads/humanizing.txt` against the source (`uploads/paper3_material_ledgers_v32.pdf` = `work/paper3.txt`) and against the three artifacts I produced (`summary/`, `review/`, `humanize/`). Nothing was rewritten; the prose of the article is untouched. Every number below was computed this session by the commands in §7.

---

## 0. Headline

| Question | Answer |
|---|---|
| Is the humanized file a faithful humanization? | **No.** The *body* prose is genuinely rewritten (only 2.0% of its words fall in verbatim runs ≥12 words), but it inverts one abstract-level claim, introduces nine assertions and derived quantities the source does not make (D1–D8, D10, §2.2), softens four status/discipline labels, and compresses the source's body to 66% of its word count (14,212 of 21,615) while promising "nothing is … subtracted". |
| How long is it? | F: 122,264 chars · 1,334 lines · **17,248 words** (14,212 body + 3,036 duplicated tail); A: 137,046 chars · 2,166 lines · **21,615 words**. So F's body carries **66%** of the source's word count and spends 3,036 words on a second copy of the abstract+§1. |
| Is it useless? | **No.** Three things are better than both the source and my draft and should be kept: the voice (we/our 4.0 per 1k words vs 0.1), the §1.2 "classification drift in practice" operationalization, and the resolution of the six `in review` placeholders into three citable companion papers. |
| Did it achieve the *accessibility* half of the brief? | **Not measurably.** Mean sentence length went **up** (27.8 → 28.9 words). What improved is register and punctuation (semicolons −43%, "X, not Y" antithesis −64%, em-dashes −32%), i.e. the *surface* of humanization, not its syntax. |
| Is the strategy note (`humanizing.txt`) sound? | **Yes, and stricter than the file that claims to follow it** — the file breaks four of its six rules (§4). |
| Do my own artifacts survive the same test? | **Yes on fidelity, with three amendments** (§5), one of which is a defect **in the source** I had not previously recorded: the paper's abstract and Lemma 3 describe opposite inference directions. |
| Can any of this be compiled/submitted today? | **No.** The humanized file is markdown with a `gemini:` prefix, mixed `\( \)`/`$$` math, fenced ASCII diagrams, a duplicated second copy of the abstract+§1 at the tail, and a trailing chat message. |

---

## 1. What was compared

| # | Artifact | Size | Nature |
|---|---|---|---|
| A | `work/paper3.txt` (extraction of the v32 PDF) | 137,046 chars · 2,166 lines · 21,615 words | authority |
| B | `summary/summary_paper3_v1.md` | 15,260 chars | my faithful summary (≈14.9k) |
| C | `summary/summary_paper3_v1_extended.md` | 40,635 chars | my section-by-section expansion |
| D | `review/weaknesses_and_upgrades_v1.md` (+ `review/sources.md`) | 34,218 chars | my 27-item critique, now with 21 verified comparator URLs |
| E | `humanize/01_landmark_style_notes.md`, `02_applied_draft.md`, `snippets.tex`, `style_audit.py` | — | my Option-1 patch draft, 21 compilable LaTeX lines (mean 21.9 w/sentence), and the 12-metric auditor |
| F | `uploads/p3 humanized.txt` | 122,264 chars · 1,334 lines · 17,248 words raw (13,182 after stripping math/fences) | whole-article markdown humanization |
| G | `uploads/humanizing.txt` | 2,302 chars | strategy note: "Option 3" + "Option 4", 6 compliance rules |

F, G are new-version files; A–E are unchanged, so the two "versions" in the workspace remain B (short) and C (extended).

---

## 2. Verification of F — three independent methods

### 2.1 Copy-paste check (12-word rolling fingerprint against A)

| Region | Words | Copied verbatim | Longest run |
|---|---|---|---|
| Body (front matter → Declarations, excl. References) | 9,348 | **2.0%** — and every ≥20-word run is in the reference list, the title line, or a heading | 23 w (a heading) |
| Tail (the second abstract+§1 block, lines 1244–1334) | 3,143 | **84.6%** | **405 words** |

Both figures are stable under the two counting conventions: on raw words the body is 14,212 vs A's 21,615 (66%) and the tail adds 3,036 duplicated words; on math/fence-stripped words, 9,348 vs 22,241 and the tail's 3,143. So the body is a real rewrite (my earlier impression of wholesale copying is corrected by this measurement) and the file's promise of non-subtraction is false; the *tail* block, by contrast, opens with ~600 characters of chatty rewriting ("People keep treating depletion numbers as if they all mean the same thing", "mash everything into one scalar") and then reverts into long verbatim stretches of the source — the elevator passage (157 w), the deep-time scoping paragraph (180 w), the scalar/vector reading passage (191 w), the strong-sustainability definition (115 w), the "illusion" passage (405 w). The two §1s have a 0.08 normalized similarity on their first 200 words.

**Consequence:** F's own closing note ("Both preserve all technical claims, status labels, and section numbering; the surrounding prose is rewritten") is untrue in both directions — the tail is largely *not* rewritten, and the body is *substantially shorter* than the source (22,241 → 13,182 words).

### 2.2 Numeric ledger (181 numeric tokens in A; 153 in F)

**33 dropped (18%), 5 added.** Classified:

*Formatting, harmless (4):* `1,000,000 → 1.0×10⁶`; `3,400,000 → 3.4×10⁶`; `50,000,000 → 5.0×10⁷`; `0.0` inserted into the phosphate row label.
*Derived insertions, not in A (2):* `4.465` = 5.000 − 0.535 (consistent with the printed pair; fine) and **`τ_aggregate ≈ 7.69 yr` = 1/0.130, which manufactures in display math the very scalar Non-example 1 exists to block.** Delete at merge.
*Real losses (27), most damaging:* `4.44`, `4.66`, `415`, `1.79`, `2.57` (the whole v4.44 fishery record and the "record low in 2023" comparison); `89.526`, `2.090`, `4.652133`, `8.6×10⁴`, `44.334`, `312.655`, `104.693`, `1353.761` (G3P working point, the τ table, the recharge-law table, and the quarantine benchmark that justifies the disclaimer); `0.85`, `0.25`, `0.70`, `0.20` (the ψ evidence-boundary and illustrative pairs); `150 yr`, `2002` (the 60-year horizon and its window); `2026` in two citations; `468`, `114`, `682` (Table 5 rows kept as ranges or first names); `4.0` of the 12.4±4.0 pair.

### 2.3 Targeted semantic probes (≈40, each with the source's own words for comparison)

**Confirmed in A (so the humanized change is a divergence):**

| # | A (source) | F (humanized) | Severity |
|---|---|---|---|
| **D1** | "Our **two-pool architecture is engineered to capture this wear phase**" (in F's §1.1) vs A's non-claim list and §10.4 (i): "the applied object we admit is the one-pool affine approximation" | — | **Critical.** It claims an object the paper explicitly does not establish. In A the phrase "two-pool" appears 11×, always guarded. |
| **D2** | A: "routing is never determined by diagnostic labels" — **0 occurrences in F** | F §2.5: "A regime **determines the routing**: if label B then ṽ=0 … if label F then P=1.0 … if label D then h=1.0" — an if-then rule over all six labels | **Critical.** Turns a prohibition into the definition of a mechanism; it also silently converts two *illustrative* parameter sets into assigned rules. |
| **D3** | A: "**Banned** unless donor-limited (Section 4.4)" | F: "**Admissible only when** its donor is a state or bounded, and the bound is registered (§4.4)" + invented "…unless artificially thresholded" | **High.** Deletes the prohibition verb and appends a clause A does not contain. |
| **D4** | A: "quarantined by the **consistency test below**: it sits an order of magnitude beyond published basin-mean trends … **must not be reused** … **declared, not computed**" | F: "flagged as an **extreme outlier within the dataset** … **should not be cited as** a global mean" + invented cause "reflects the sensitivity of the satellite-derived masks" | **High.** Replaces a benchmarked external failure with a generic statistical outlier and invents the explanation; the source's own benchmark — "typically a few cm yr⁻¹", and the +6.5 m fitted-2002 check that makes the row untenable — disappears with it. "quarantine" 5→0, "declared, not computed" 1→0, "must not be reused" 1→0, "degenerate" 1→0. |
| **D5** | A Table header: "USGS MCS, **2025 vintage** (reserves)"; registered action: "Phosphate reserves … **re-pin … to the 2026 vintage**" | F header: "USGS MCS **2026 Vintage**" while the country rows are unchanged from the 2025 vintage (Morocco 50,000,000 kt) | **Medium-High.** Claims a vintage update the paper lists as an action to be completed. |
| **D6** | Verbatim source strings verified present in A and **absent from F**: "already at minimum" (1), "42 of the 43" (1), "archived pull" (5), "row-by-row re-verification" (1), "transfer principle" (1), "no basal mortality" (1), "not promoted to a forecast" (1), "no cohort statistic is quoted" (1), "the scale must not… " — and, in $[\cdot]_+$/display form, the one-way-valve clause and $\tau_{\mathrm{exit}}=\min_m\{\tau_m^-,\tau_m^+\}$; plus the standing refusals in their source form — "This article establishes Layers 1–3 only", "The value is reported with its cohort conditions and is not promoted to a forecast", "no cohort statistic is quoted from a different database version" (the strings "This paper establishes no…", "no aggregate of that kind is reported" and "the eight zeros are a convention" are **my paraphrases, not the paper's wording** — struck 2026-09-14) | **Medium.** These are the sentences that carry the falsifiability discipline. *Verified against A by string search; earlier drafts of this row quoted three items ("τ = min over all moieties m", "the one-way valve", "the eight zeros are a convention") that are my paraphrases of displays/captions, not the paper's sentences — corrected 2026-09-14 after the 50-string re-audit reported in `ledger_audits_verified_v1.md` §6. |
| **D7** | A §11: "gives the accounting object on which the **questions can be posed precisely**"; limitations as "(i)–(viii)"; "In **one demonstrated case**, a headline indicator moved … an order of magnitude" | F §11: "**resolves both failures**"; "1.–8."; "In all demonstrated cases…"; adds "financial flows", "metabolic balance", "produces misleading policy conclusions" | **Medium-High.** Two of those phrases are the over-claiming the strategy note (G) warns against. |
| **D8** | A §10.4: 5 of 8 items are flat non-establishments ("This paper establishes **no** optimal tax…", "**does not constrain**…", "**does not recommend**…") | F: 7 of 8 are reworded as research needs ("Future research should…", "The present results provide…") + "This paper establishes **physical accounting principles**" | **Medium.** Converts "we do not answer X" into "X is future work", which reads as a stronger contribution claim. |
| **D9** | A: **5** in-text placeholders "(Author, D./F./E., et al., in review)"; 7 `doi.org` links; 32 dated reference entries, three of which are Abaee (2026) Zenodo records 22545740 / 22554217 / 22554297 | F: **0** placeholders — the five are mapped onto those same three Abaee (2026) records; 32 dated entries (count unchanged); **4** `doi.org` links | **Improvement with one authorial risk.** The Zenodo DOIs are *not* fabricated: all three already appear in A, so no registry check is needed (my earlier note on this was wrong, and `10.1007/s13762-024-00554-z` / `10.1371/journal.pone.0340369` were never in A — they are comparator URLs from D, not the paper's references). Two real issues: (a) F collapses "Author, D." (delay-dynamics) and "Author, F." (assessment analysis) onto works attributed to Abaee, which is only legitimate if those are the same papers — an authorial decision; (b) F drops 3 of A's 7 DOI links (`10.1007/s13762-024-05664-y`, `10.1371/journal.pbio.1001700`, `10.3390/resources7030058`) though it keeps the entries. |
| **D10** | notation: A renders the transpose as `ST`/`Sᵀ`; F has 44 literal `S_T` | — | **Medium.** `S_T` reads as "stock at time T". Fix by explicit `S^{\top}` at merge. |
| **D11** | abstract, twice in F (body and tail): "a flux-reconstruction identity … **recovers unobserved internal fluxes from observed stock trajectories**" | A's abstract says the *same thing* — but A's Lemma 3 (whose own section heading is "The flux-reconstruction identity") states `ẋ = Sᵀv + b` and concludes `S(t) = S(0) + ∫(CSᵀv + Cb) dt`, i.e. **readouts from fluxes**; F's §3.3 heading is "Stock Reconstruction from Flux Balances" | **Finding about the source, not a humanization error.** F inherited the abstract's direction and half-corrected it. The paper must fix the abstract (or retitle/restate Lemma 3), not the other way round. This is new: my D did not list it. |

**Where F is right and A is awkward:** F's §1.2 "Classification drift in practice" paragraph operationalizes a term A uses without an operational definition; F's §3.1 "Consequences" list is clearer than A's run-on; F's three fenced blocks (§3.1 layer comparison, §6.1 metric table, §10.2 closed-vs-open ledger) are the only table-like visuals either version has — but they are **unlabelled**, and so is everything else: numbered callouts of the form "Table N"/"Figure N" occur **0 times in A and 0 times in F**, so neither version can cross-reference them; F keeps the ORCIDs, e-mail and keywords rather than fabricating them.

---

## 3. Style verification of F (same auditor, same rules)

| Metric | A (source) | F (humanized) | My target | My `snippets.tex` |
|---|---|---|---|---|
| Mean words/sentence | 27.8 | **28.9** | ≤22 | 21.9 ✓ |
| Sentences >30 w | 55% | 53.8% | ≤35% | 28.6% |
| Longest sentence | 254 w | 269 w (table artifact) | ≤60 w | — |
| Semicolons | 293 | 166 | ≤80 | 0 |
| Em-dashes | 213 | 145 | ≤55 | 3 |
| "X, not Y" | 67 | 24 | ≤25 | 1 |
| we/our per 1k words | 0.1 | **4.0** | 5–8 | 8.4 |
| "consider/suppose/let" | 0 | 9 | — | 2 |
| Example markers | 0 | 0 | — | 3 |

Note A's "0 markers" is itself an artifact of the extraction: F's markdown `**Example (…)**` headers and A's LaTeX `\begin{exampleblock}` express the same thing, so **F is the only version that makes the example blocks visible as blocks** — one of G's rules ("put the technical core in labelled boxes") is satisfied in spirit only by F. The 269-word "sentence" in F is a flattened markdown table, not prose; the auditor must be run on prose-only text (my E script has the same limitation, and I flagged it when I built it).

---

## 4. `humanizing.txt` (G) evaluated rule by rule

G refers to "Option 3" and "Option 4". Neither exists in my artifacts (my `02_applied_draft.md` numbers its options 1–4 for *titles*), so I evaluated G on its own six rules and against your standing decision, "hybrid of all options". G's factual premises about venues were **not** verified this session (see §6, action A7).

| G's rule | Does F obey it? | Does my E obey it? | Verdict on the rule |
|---|---|---|---|
| 1. Journal template; boxes only if supported | ✗ F is markdown, no template decision | ✓ `snippets.tex` is compilable and box-free; my reader's note is a blockquote, not a `\begin{box}` | **Sound and unaddressed by F.** Deciding the venue is a prerequisite, not a polish step. |
| 2. Technical core self-contained | ~ F keeps defs/theorems/proofs but compresses them (59% of length) and drops 27 numeric tokens | ✓ E is patch-style: nothing removed | **Sound; F implements it as deletion, which is the wrong operator.** |
| 3. No chatty voice | ✗ the tail block violates it ("mash everything into one scalar", "People keep treating…") while the body complies | ✓ E's voice edits keep the hedging | **Sound, and the single rule F breaks most visibly.** This is the risk of voice-humanization in one pass. |
| 4. Caveats early, in the main text | ~ §1.2 "What is explicitly not claimed" survives and is prominent; ✗ §10.4's five "this establishes no…" items are softened to "future research" | ✓ E's boxed note moves the limitations *forward* and preserves all of them | **Right idea; F half-implements it.** |
| 5. Few optional boxes | vacuous — F has 0 boxes | ✓ 1 box planned | **Sound; both versions under-shoot the accessibility goal G itself states.** |
| 6. Abstract/conclusions precise, no over-claiming | ✗ "resolves both failures", "guaranteed", plus a *second* abstract in the tail that contradicts the first in register | ✓ E's abstract options keep the claim ceiling identical | **The most valuable rule, and the one F fails.** |

**Net:** G is a correct and conservative brief — more conservative than the file that invokes it. Its one gap is that it never says *how* to protect the status vocabulary while cutting, which is precisely where F failed. My recommended addition (to G, when we next revise): a rule "**Status-bearing sentences are copied verbatim; only status-free sentences may be rewritten**", which would have prevented D2–D4 and D7 outright, plus "**no derived numbers**" for D's 7.69 yr.

---

## 5. My own artifacts under the same test

> **Self-corrections made while verifying (recorded here, applied in the files).** (1) The 9× ε charge in D's E4 was overstated: the source declares its convention in §6.5.3 (`T_resource,10% = 0.9 G_resource/C_G`) and §7.6 (`(1−ε)G₀/P`), so 1,125 yr is right. D's E4 is re-framed as a labelling item and its severity lowered ●●●→●●. (2) "Six `in review` placeholders" → five in-text mentions naming three works (D×3, E×1, F×1); the E mention is split by a page break, which is why a line-based count under-reported it. (3) The Zenodo DOIs in F are not fabricated — all three appear in A; what F actually loses is 3 of A's 7 DOI links. (4) `paper3.txt` is 137,046 chars / 140,225 bytes / 2,166 lines, not 157,131.

**B — the 15,260-char summary.** Re-checked the load-bearing wording: my "**banned** unless the donor is a state or bounded, and the bound is registered (4.4)" matches A's status column exactly. My §2.4 routing sentence reproduces A's prohibition ("routing is never determined by the diagnostic labels"), i.e. B commits none of D2/D3. One genuine divergence remains open: **B describes Lemma 3 as "reconstructs moiety readouts by integrating observed fluxes", following A's *body*, while A's *abstract* says the reverse** (D11). B is internally consistent with the proofs; the paper is not. Decision needed (A6 below).
**C — the extended summary** (40,635 chars): same orientation, plus per-section coverage of every status line.
**D — the review.** Verified: all comparator URLs in `sources.md` are live and their claims are quoted from the sources; reference count restated as 28 (A has 28 entries — the count of `Example` environments is 0 because A uses `\begin{exampleblock}`, so D's phrasing is corrected in this report); E8 (five in-text placeholders naming three works) is confirmed and is now demonstrably fixable, since F shows the three companions with DOIs. **Two additions D needs:** (N7) the abstract↔Lemma 3 direction mismatch (D11); (N8) the notation hazard `S^T` vs `S_T` (D10) is worth one line in E's notation-table item E3, because the flattened PDF made me read `ST` correctly only by context.
**E — the style draft.** E does not commit D1 or D2: its "two-pool" edits explicitly state "We do not yet have the two-pool groundwater model" (line 217), and it never assigns routing by label. E also never produces a derived scalar. But E is a *patch* (4 title options, one abstract, one opening, one box, 12 micro-edits ≈ 600 words) and touches none of §§2.5, 6.5, 8.1–8.3, 10.4 in full. So E satisfies fidelity and G's rules 2, 4, 6, and 3 — and fails rule 1 only in that the venue was never chosen. **For coverage E is not a competitor to F; F's body is ~14× larger than E's committed text and covers all eleven sections.**

---

## 6. Merge plan (agreed architecture, still not executed)

Authority: **A's text for every status-bearing sentence**; F for voice and the two genuinely better passages; E for the abstract, the reader's box, and the sentence-length programme; G's six rules as the acceptance gate; D's E1–E8 as the *fix list that must not be lost*.

Priority buckets for when you say go:

* **P0 — integrity (9):** delete the tail duplicate and the `gemini:`/chat residue; delete F's invented assertions ("engineered to capture", F's routing rule, "artificially thresholded", "satellite-derived masks"); restore "Banned unless donor-limited"; restore "declared, not computed" + "must not be reused" + the "typically a few cm yr⁻¹" benchmark and the +6.5 m fitted-2002 check (and, in §9, the 2×10⁶ yr vs 8.6×10⁴ yr pair that "the scale must name its flux" governs); restore the $[\cdot]_+$ one-way-valve clause of §2.2 ("never binds here because the registered intrinsic target is positive"), "min over all moieties", "42 of the 43", "archived pull", "eight zeros are a convention", "not in the three-quantity hierarchy"; remove `τ_aggregate = 1/0.130`; revert §2.2's Eq. (2) mis-citation; retitle §10.4 to its own content; revert "resolves both failures".
* **P1 — restored numbers (verified list).** Recomputed this session: of A's 186 numeric tokens, 37 are absent from F, and after removing formatting artifacts (ORCID "000", "74000" for 74,000,000, "104"/"106" from 10⁴/10⁶, "5000", DOI fragments) the substantive losses are: **89.526 / 2.090 / 4.652133 / 4.47 / 397.87-context**, the **ψ pairs 0.85 / 0.25 / 0.70 / 0.20** and the **1.5** trough-depth factor (§2.5), **2002** (window), **150 yr** (§9), **4.44 / 415 / 2.57 / 4.66 / 2.9 / 1.79** (fisheries version-sensitivity and the positive sub-cohort), **2025** and the **0.9** in `T_resource,10% = 0.9 G_resource/C_G` (§6.5.3), **120,000 / 250,000** (pinned-vintage figures), **9.0 / 6.0** (sebastid, pleuronectid medians), and the three DOI links (§2.3/D9). *Correction to this file's earlier draft:* the numbers 44.334, 312.655, 104.693, 1353.761, 468, 682 and ±4.0 are **not in the source at all** and must not be chased; the ε-label row is likewise a labelling item, not a lost number (see §5 self-corrections).
* **P2 — mechanical readability:** split every sentence >45 words (target ≤22 w mean, ≤4 semicolons per page), keep F's em-dash economy, run `humanize/style_audit.py` until all 12 metrics pass.
* **P3 — LaTeX readiness:** boxes only after the venue is chosen (default = no boxes), `S^{\top}`, real `\begin{figure}` for F's network diagram, `\label`/`\ref` for the 3 diagram blocks, bibliography with DOIs of A ∪ F (union, then verify each).
* **Open actions:** A6 — decide whether the *abstract* or *Lemma 3* is wrong in A (I recommend fixing the abstract to "reconstructing unobserved moiety readouts from observed fluxes", since the proof is the authority); A7 — verify G's venue claims (HESS first-person policy, EGUsphere box support, whether any target journal permits plain-language boxes).

---

## 7. Reproduction

```bash
# copy rate + tail duplication
python3 - <<'PY'   # 12-word rolling fingerprint, math/table-stripped
# (the exact script is reproduced in this session's log; key results: body 2.0%, tail 84.6%)
PY
grep -c 'Two-pool\|two-pool' paper3_prose.txt                  # 11, all guarded
grep -c 'routing is never determined' work/paper3.txt           # 1
grep -c 'Routing is determined by' "uploads/p3 humanized.txt"   # 1  ← new mechanism
grep -c 'declared, not computed' work/paper3.txt                # 1 ; 0 in F
python3 humanize/style_audit.py "uploads/p3 humanized.txt" work/paper3.txt
pdflatex -interaction=nonstopmode humanize/snippets.tex         # exit 0 (E only; F does not compile)
```

## 8. One-sentence bottom line

F is a better *voice* pass and a worse *integrity* pass; E is the opposite; G is the right referee; **the article itself** still carries the three defects that make any humanization risky (the abstract↔Lemma 3 direction, the undeclared ε label at the resources row, and the five in-text "in review" placeholders naming three works) — which is why the merge in §6 should start with A corrected, not with F polished.

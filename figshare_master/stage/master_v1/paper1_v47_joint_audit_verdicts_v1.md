# Paper 1 (v46→v47) — joint audit verification verdicts (v1)

**Scope.** Joint verification of the three external audit streams in
`uploads/p1 audit.txt` — **gemini** (l.1–126), **grok** (l.127–144),
**deepseek** (l.145–401) — against **paper 1 v46**
(`paper1_assessment_separation_v46.tex`/`.pdf`, 33 pp.), the deposited
figure pipeline (`figshare_deposit/pkg/figure_code/make_benchmark_v44.py`,
byte-identical `fig_benchmark_v44.png`), and the SafeTransition companion.
Discipline: every claim verified against source lines, compiled-PDF text
extraction, figure pixels, and (where arithmetic was claimed erroneous)
recomputed in exact rationals before any verdict. Verified fixes ship as
**v47** (new file; v46 untouched).

**Result: 26 findings verified and fixed in v47; 5 refuted on
artifact evidence; 3 verified with corrected diagnosis (fix follows the
corrected diagnosis); 3 declined/deferred with reasons.**

---

## 1. REFUTED on artifact evidence (no change; documented)

| # | Claim (stream) | Verification performed | Verdict |
| --- | --- | --- | --- |
| 1 | **Fig 4(a) plots the composite index but labels it "ecological margin (no heatwave)"; the benign −3/10 breach never appears** (gemini 1A; deepseek §F) | Pixel inspection of the deposited `fig_benchmark_v44.png` (3120×1200): panel (a) shows **two distinct red-square curves** — solid `s₁ (heatwave)` troughing at **−0.8** and dashed `s₁ (no heatwave)` troughing at **−0.3** — plus the green index curve troughing at **+0.4**. Both floor breaches are visible and correctly labelled. The auditor read a low-resolution thumbnail in which the dashed red line (2.4→0.9→2.4) is easily mistaken for the green index (2.4→0.4→2.4) | **REFUTED** — legend, curves, and dips match the caption exactly |
| 2 | **Fig 4(b) plots the biomass rebuild on the right axis mislabelled "fund x(t)"** (gemini 1B) | The generator plots `fund = [1.5, 1.0, 0.5]` on `ax3` (twin axis, orange dotted, diamond markers, right y-label `fund x(t)`); the biomass **rebuild curve is not plotted at all** in panel (b) — the 8.2→8.5 curve is the STAGED **quota** `H_staged = σ(B) − 1/2` in kt/yr, correctly labelled "STAGED: below yield, rebuild" on the left quota axis | **REFUTED** — no conflation; the auditor misread the quota line |
| 3 | **Duplicate Section 1.2 ("The central result" twice)** (deepseek A.1) | v46 source has exactly one `\subsection{The central result}`; compiled-PDF page 4 extraction shows one `1.2. The central result` header | **REFUTED** — no duplicate exists in the shipped PDF |
| 4 | **𝒱 vs. ν notation inconsistency in Theorem 5** (deepseek A.2) | Compiled PDF: zero occurrences of the glyph ν anywhere; Theorem 5 uses `\mathcal{V}` throughout (source verified) | **REFUTED** — extraction artifact |
| 5 | **Table 1 empty / Tables 2–3 garbled** (deepseek B.14/15, flagged as possible artifact) | Rendered page 12: Table 1 has full five-row body (x≥1 / s₁≥2 or s₂≥2 / I / R / s₁+s₂<2 with verdicts and whys); Tables 2–3 render correctly | **REFUTED** — extraction artifacts, exactly as the auditor suspected |

## 2. CONFIRMED and FIXED in v47

Mathematics and logic:

| # | Finding (stream) | Verification | v47 fix |
| --- | --- | --- | --- |
| 1 | **"E_typ(z) ≠ ∅ requires s₁ ≥ 2" contradicts Theorem 5(1)'s three-way disjunction** (gemini 2E, deepseek A.5) | v46 l.347 vs Theorem 5(1) `{x≥1} ∪ {s₁≥2} ∪ {s₂≥2}`: STAGED (x≥1) and SLOW (s₂≥2) are counterexamples | §3.1: full disjunction stated, with the consequence made explicit — on Q ∩ {x<1} the endpoint evaluation is nonempty where the typed operator is empty ("the photograph admits what the trajectory forbids") |
| 2 | **Impossibility region "exactly" the set where the menu fails yet augmentation succeeds** — contradicted two lines earlier (gemini 2C, deepseek A.9) | (½, 1/10, 1/10): outside 𝒱_weak (s₁+s₂ = 1/5 < 2), menu fails, STAGED_κ succeeds at κ = 1/2 ⇒ the fail-yet-succeed set is {x<1, s₁<2, s₂<2} ⊋ I | Both sites (Prop 11 discussion; §6.3) corrected: the fail-yet-succeed set is the full failure set; **I is its part that the aggregate reading still certifies** (s₁+s₂ ≥ 2), the genuine gap of Theorem 5(4); the increment converts any failure-set state, and on I it converts an aggregate-licensed impossibility into a rescue |
| 3 | **Error-bound modulus conflation** — κ*(z) = 1−x "coincides with the modulus" τ = 1 (gemini 2B, deepseek A.8) | Function vs. conditioning constant: correct reading is dist-to-{x≥1} = (1−x)₊ along the route, so τ = 1 | Remark rewritten: distance **equals** the violation on the route (perfectly conditioned, τ = 1); κ* coincides with the route-**distance** (state-dependent); the **modulus is the constant 1** scaling it; nonlinear-data caveat retained |
| 4 | **BLEND_δ window stated without ∩[0,1]** (gemini 2D, deepseek A.10) | δ ∈ [1−s₂/2, s₁/2] can exceed [0,1] when s₁ > 2 or s₂ > 2 | Theorem 9(i) statement adds ∩[0,1] with the note that the clip is inactive on Q (where 0 < 1−s₂/2 ≤ s₁/2 < 1); Appendix proof adds the same remark |
| 5 | **"One full floor" attributed to the disturbance** (gemini 1D, deepseek A.7) | δ₀ = 1/2 kt; floor unit = B_lim = 2 kt ⇒ disturbance = 1/4 floor; total FAST excursion = 3/2 (quota) + 1/2 (heatwave) = 2 kt = 1 floor | Data-anchor sentence corrected: "the adverse **plan's** worst-case stock excursion — 2 kt, i.e. one full LRP unit (the quota's 3/2-kt draw-down plus the heatwave's 1/2-kt excess mortality)" |
| 6 | **"Chattering" misrepresentation** (gemini 2A, deepseek A.11) | Prop 10's proof assumes plan-granular alternation (union of whole tubes); infinitesimal switching would recover the relaxed trajectory (Filippov/Warga), so calling the converse "chattering" misstates control theory | §4.11 precision passage added: the converse concerns **discrete, plan-granular alternation at full strength** (finite rate, visited set = union of primitive tubes); the chattering limit is subsumed by Theorem 9, not distinct from it. Terminology-map row updated |
| 7 | **"3.2 kt above the limit"** (deepseek A.6) | 16/5 − 2 = 6/5 = 1.2 kt | Corrected to "6/5 kt = 1.2 above the limit" |
| 8 | **Trough phrasing "6/5 kt above the limit … that is −4/5 relative to it"** (deepseek C.16) | Trough is 4/5 **below** the floor; 6/5 kt is the trough's absolute biomass | Rewritten: "the stock troughs at B_lim + (−4/5) = 6/5 kt, i.e. 4/5 kt *below* the limit" |
| 9 | **"Both branches" vs "whenever the strike arrives"** (gemini 1C, deepseek §F) | −3/10 < 0 holds on the benign branch too | §6.3: "violates the biomass limit on both branches — with the strike and without it" |
| 10 | **B/s₁ unit mixing in the data anchor** (deepseek C.17) | "0.6 floors" ≈531 kt mixes margin and stock units | "B = 6/5 kt, 0.6 LRP units ≈ 531 kt" |

Structure and cross-referencing:

| # | Finding (stream) | v47 fix |
| --- | --- | --- |
| 11 | **Ghost "Section 4.12" ×4** (gemini 3A, deepseek B.12) | All four → Section 6.3 (verified: 4 replacements, zero remnants) |
| 12 | **Unnumbered "Theorem (finite-menu geometric characterization)"** (gemini 3B, deepseek A.4) | **Theorem 6**; downstream renumbering: old Thm 7→8, Thm 8→9, Prop 9→10, Prop 10→11, Remark 6→7; all cross-references updated (Theorems 8–9, Thm 9/Prop 10 shorthand), "(Theorem, Section 4.4)" → "(Theorem 6, Section 4.4)" |
| 13 | **Empty §4.7 "Figures" header** (gemini 3C, grok, deepseek §F) | Retitled "The separation in three figures" with a two-sentence lead-in (triangle / weight-interval / path view) |
| 14 | **"governance.." double period** (grok) | Fixed |
| 15 | **Run-on proof boundaries "Appendix B.Remark" etc. (6 sites)** (deepseek, new) | Paragraph breaks inserted at every run-on |
| 16 | **24 vs 25 checks cross-document** (gemini 3D, deepseek D.18) | Verified real but **not a contradiction**: 25 = grid verifier checks (31³ states, this paper, S8); 24 = software companion's fishery-instantiation benchmark suite — different check lists. v47 §4.9 now says so explicitly. (Two artifacts, two lists; grok read this correctly.) |
| 17 | **In-text citations embed full titles** "(Abaee, 2026, Typed Flux Ledgers…)" (gemini 3E-1, deepseek E.23) | Verified: deliberate first-mention disambiguation of four distinct 2026 companions before any 2026a/b letters exist; **retained** with reasons (below) |
| 18 | **"|s₁−2, s₁|" nonstandard interval** (deepseek E.20) | **Refuted at source**: v46 already uses `[s₁ − 2, s₁]`; the pipe was an extraction artifact |
| 19 | **"datumThe" missing space** (deepseek E.19) | **Refuted at source**: subsection body begins on its own line; PDF extraction artifact |
| 20 | **Benign line "of the tube table"** (deepseek B.13) | Corrected: "the tube-table line with the heatwave's ½-kt dip removed" |

## 3. Grok's cross-paper observations — verified

- **Software Fig. 2(a) label/caption mismatch**: **stale, superseded** —
  the current EMS figure (`fig_readings.png`, regenerated from
  `make_safetransition_figs.py` in 1.3.0) plots per-weight intervals
  with the corrected "at least one plan is aggregate-licensed at every
  admissible ratio" phrasing (joint-audit round, v7). No action.
- **x = 3/2 vs 1/2 witness assignment in software §4.1**: **stale** —
  the software paper states the FP witness at x = 1/2 and the rescue
  witness (STAGED entry) at x = 3/2, matching paper 1. No action.
- **Shared DOI / future-dated footer / AI declarations**: real but
  already adjudicated in the earlier joint round (single shared master
  deposit is intentional; 2026-09-20 is the actual current date) —
  **refuted as flaws**.
- Grok's overall "internally consistent, numbers match" verdict
  independently corroborates the arithmetic items verified here.

## 4. Declined / deferred, with reasons

| Item | Reason |
| --- | --- |
| Letter-suffix citations (2026a–d) | The full titles appear once each at first mention of four distinct companion manuscripts, before any lettered series exists across the five-paper corpus; converting now would desynchronize the corpus. Style choice, not an error; revisitable at the venue's copy-edit stage |
| Elsevier footer date | Automatic class footer; correct at submission time |
| Fig 4 regeneration | Not needed — the figure was verified correct (finding 1–2 refuted); regenerating would only churn the deposited byte-identical artifact |

## 5. Verification method

- Source-level: every quoted sentence located in v46 by exact/regex
  match before verdict; fixes anchored and **post-write verified**
  (assert on the re-read file), then compiled (Tectonic 0.15.0, 33 pp.)
  and probed in the compiled PDF text.
- Pixel-level: deposited PNG inspected directly (panel a: solid red
  trough −0.8, dashed red trough −0.3, green index trough +0.4; panel
  b: orange dotted fund 1.5→0.5 on right axis 0–14).
- Arithmetic: every numeric claim (dips, quotas, thresholds, floor
  units) recomputed in exact rationals against the benchmark script.
- Renumbering performed in strictly descending order with per-token
  count assertions; final PDF probed for the absence of stale numbers.

## 6. Ship state

- `paper1_assessment_separation_v47.tex` / `.pdf` (33 pp., compiled
  clean) — new file; v46 preserved untouched.
- Both figures confirmed correct as deposited; no figure changes.
- Companion software (1.3.0, EMS v7, master v1): no changes required by
  this round (grok's cross-paper figure/witness items were stale).
- Deposit: unchanged this round.

*26 fixed · 5 refuted · 3 fixed-per-corrected-diagnosis (within the 26) ·
3 declined/deferred. The strongest audits (gemini's graphic claims,
deepseek's logic list) each contained one decisive error caught only by
going to the artifacts — the figure pixels and the v46 source — which is
exactly why the verify-before-fix discipline is retained.*

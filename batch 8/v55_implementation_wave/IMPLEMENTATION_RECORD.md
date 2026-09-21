# Task 110 (item 2) — The §1.3 Contributions Item (xii) for §5.9: Adjudication and Implementation (v55)

**Owner directive executed:** *"an optional §1.3 contributions item for §5.9 if genuinely merited"* — the merit call delegated to this round, together with the standing push rule (PAT supplied).

**Deliverable:** `latex/paper1_assessment_separation_v55.tex` (+pdf) — Paper 1 (*Ecological Indicators*), v54 → **v55**: 2,801 → 2,816 lines (+15), 47 pp (unchanged). Standing rules honored: new version only (never overwrite); **purely additive** — no content removed or condensed (`SUPERSEDED` is empty; the inverse-reconstruction gate proves the diff is exactly the one enumerated edit); fail-loud build; every claim in the new item is already stated in v54's own §5.9, Table 5, §5.7 or §4.10 — no new claims, no new numbers.

---

## 1. The adjudication: MERITED

| # | Ground | Detail |
|---|---|---|
| (a) | **Parity precedent** | §1.3's item (xi) already covers the §5.8 labelled extension (added in v53, Task 107). §5.9 is the same format — a labelled extension with machine-verified theorems (M1–M4 + CT, 77 checks). Omitting it leaves the contributions list asymmetric between the paper's two labelled extensions. |
| (b) | **Main-text load** | §5.9's results are load-bearing in the main text: Table 5's middle cell and row (iii) carry its computed verdicts (§5.4); §5.7 carries the κ\* trichotomy with a prescription change (reserve accumulation → floor rebuilding); §4.10 carries the class-conditional blend caveat. A list that enumerates (xi) but not the extension that filled a main-text table understates the paper. |
| (c) | **The v54 record's own note** | The v54 implementation record (§4) recorded the additive item as "a one-line option" left out only because it was "not in the approved list" — a scope reason, never a merits reason. |
| (d) | **The owner's delegation** | "if genuinely merited" — the call was made this round on the merits, and it is affirmative. |

**Counters weighed and overruled:** *length* (the item adds one sentence of the same order as (iv) and (xi) themselves — the contributions paragraph runs (i)–(xii) as one paragraph, and its growth by ~6% is the honest cost of enumerating the paper's actual results); *scope* (the item claims nothing beyond what §5.9/Table 5/§5.7/§4.10 already state — checked claim-by-claim below); *a "core-results-only" reading of §1.3* (rejected: (xi) already includes a labelled extension, so the list's established scope includes them).

## 2. The edit (one anchored, position-recorded insertion)

The new item, appended after (xi) in the contributions paragraph (citing §5.9 by its label, mirroring (xi)'s citation style for §5.8):

> (xii) A labelled common-shock extension of the witness datum (Section 5.9): the middle-regime disturbance verdict of Table 5 computed exactly (the acceptance gap survives the common shock, reduced by the exact 1/2-cut, licensing thresholds unshifted on the surviving region), the class-conditional rescue trichotomy (κ\* = 0, (1 − x)₊, or ∞, with the first unrescuable-by-reserve failure states on this datum), the class-conditional caveat on the blend collapse (Theorem 9's window, not blend-closed on the fragile band), and two exact reading-conditional theorems for the coupled regime (the additive gap relocating rather than vanishing; the replace reading collapsing the typed/weak distinction itself) — machine-verified as a fourth check list.

**Claim-by-claim source check** (every phrase traces to v54's own text): "the acceptance gap survives the common shock, reduced by the exact \(1/2\)-cut, licensing thresholds unshifted on the surviving region" — §5.9 Theorem M1 (v54 lines 1807–1819); the trichotomy notation and "the first unrescuable-by-reserve failure states on this datum" — §5.7's M2 paragraph (v54 lines 1412–1416); "class-conditional caveat on the blend collapse" — §4.10's heading phrase; "not blend-closed on the fragile band" — §4.10/§5.9 (Theorem M3); "two exact reading-conditional theorems … relocating … collapsing the typed/weak distinction itself" — §5.9's opening (v54 lines 1744–1745) and Theorems M4 + CT; "machine-verified as a fourth check list" — §5.9's verification paragraph (77 checks; the family's non-pooling policy).

## 3. Build and verification battery (all green)

Build: `make_v55_p1.py` (this folder) — 1 anchored edit; **inverse-reconstruction gate**: reverting the one edit reproduces v54 byte-identically (the diff is exactly the item); **math-span multiset preservation**: v54's 1,245 spans all intact, 4 new spans added (\(1/2\), \(\kappa^* = 0\), \((1 - x)_+\), \(\infty\)), **zero alterations** (the purely-additive proof at the span level); **frontmatter gate**: title/abstract/highlights byte-untouched (the Task-108 σ-abstract DECLINED ruling stands); destination-exists (idempotence).

1. **Marker gates:** "(xii)" ×1; `\ref{common-shock-variant}` ×1 (the new label reference — §5.9 was previously referenced only by hardcoded strings; the item adds the proper cross-reference); "fourth check list" ×2; "unrescuable-by-reserve" ×3; "rescue trichotomy" ×3; "not blend-closed on the fragile band" ×1; "blend-closed" ×5; "fragile band" ×3; "reading-conditional" ×7; "class-conditional" ×8; "reduced by the exact \(1/2\)-cut" ×3; hardcoded "Section 5.9" ×8 and "Section 5.8" ×1 unchanged — every count the audited v54 value + the item's contribution.
2. **Compile:** tectonic clean — **47 pp** (unchanged), exit 0, **114 warnings — exactly v54's 114** (zero new; the paragraph reflowed within the existing budget); the only overfulls remain the two pre-existing 2.43091pt header-rule boxes (v53/v54-identical); zero unresolved references in the final PDF (`??` count 0; the new `\ref` resolves).
3. **Flat compile clean** (tex + figs_p1 alone in a fresh directory — exit 0, same page count and file size).
4. **PDF text layer:** the item renders complete and correct — "(xii) A labelled common-shock extension of the witness datum (Section 5.9): …" with "(Section 5.9):" resolved from the label and "Table 5" from `\ref{tab:disturbance}`; 9 rendered "Section 5.9" references (8 hardcoded + the new one; one pre-existing occurrence is line-split in text extraction — the rendering is correct); all marker counts match the tex gates.
5. **Never-overwrite audit:** `git status` shows only new files (v55.tex, v55.pdf, the two new wave folders); v54.tex/v54.pdf and every other existing file untouched.

## 4. Standing items not in this round's scope (recorded)

- The **off-diagonal wave's transcription items** (this round's first deliverable, `batch 8/off_diagonal_wave/OFF_DIAGONAL_WAVE.md` §8) remain **owner-gated** — the (xii) item covers §5.9's existing content only, per the directive's scope.
- Abstract/highlights untouched (the Task-108 ruling stands).
- The Zenodo deposit refresh remains owner-side.
- No other family manuscript modified (the item is P1-internal).

## 5. Reproduction

```
python3 "batch 8/off_diagonal_wave/off_diagonal_verify.py"     # 50/50, exit 0
python3 "batch 8/v55_implementation_wave/make_v55_p1.py"      # v54 -> v55 (1 edit, gated)
cd "arena agent 1/paper rewrites/latex" && tectonic paper1_assessment_separation_v55.tex
```

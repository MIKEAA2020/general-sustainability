# Task 109 — The Owner-Approved v54 Wave (Middle-Regime Transcription + F-Riders)

**Owner directive executed:** *"approved: the owner-gated v54 wave (fill Table 5's middle cell + row-(iii) refinement + κ\* trichotomy + blend-fragility caveat + optional spectrum subsection + F1/F2/F4/F5 riders)"* — with a freshly supplied PAT for the standing push rule.

**Deliverable:** `latex/paper1_assessment_separation_v54.tex` (+pdf) — Paper 1 (*Ecological Indicators*), v53 → **v54**: 2,425 → 2,801 lines (+376), 42 → 47 pp. Standing rules honored: new version only (never overwrite); no legitimate content removed or condensed; fail-loud build with the inverse-reconstruction gate proving the diff is exactly the enumerated edits; every constant transcribed from the verified wave record (`batch 8/middle_regime_wave/`, 77/77 checks, re-run green this round) or hand re-derived during this round's transcription review — nothing invented.

---

## 1. The wave (16 anchored, position-recorded edits; all items owner-approved)

### The middle-regime transcription items (MIDDLE_REGIME_WAVE.md §8)

| # | Item | Where | Content |
|---|---|---|---|
| 1 | **Table 5 middle-cell fill** | §5.4, `tab:disturbance` row (ii) + caption + pointer sentence | The computed verdict (Theorem M1): the gap **survives** the common shock, reduced by the exact 1/2-cut (every action-indexed gap state with min(s) < 1/2 weak-rejects), licensing thresholds unshifted on the surviving region, the canonical datum a member |
| 2 | **κ\* rescue trichotomy** | §5.7, new labelled paragraph after the Proposition-11 discussion | Theorem M2: κ\*=0 on V_typ^cs; (1−x)₊ on failure states with both floors ≥ 3/8; **∞** on {min(s) < 3/8} — the first unrescuable-by-reserve failure states on this datum (witness (1/2, 1/4, 3)); the canonical datum's shortfall unchanged at 1/2; the reserve-accumulation → floor-rebuilding prescription change |
| 3 | **Blend-fragility caveat** | §4.10, new paragraph after Theorem 9's Remark | Theorem M3: Theorem 9's window is class-conditional — common-class window {s_i ≥ δ, sum ≥ 3/2+2δ} (δ=1/2: {s_i ≥ 1/2, sum ≥ 5/2}); the common-shock gap is **not blend-closed** on the fragile band sum ∈ [2, 5/2), witness (1/2, 1, 1) with no admissible blend; the coupled gap, by contrast, is blend-closed |
| 4 | **Row-(iii) refinement** | §5.4: the coupled-delimitation bullet + the row-(iii) cell | Theorems M4 + CT: additive — universal rejection exact on I at full magnitude, depth-dependent with the exact boundary δ = 5/4 (witnesses (1/2, 19/10, 19/10) surviving at δ = 1/2; (1/2, 79/40, 79/40) at δ = 5/4 − 1/40), the gap **relocating** (the coupled(2) gap {x<1, 2 ≤ s_i < 7/2, sum ≥ 11/2}, witness (1/2, 3, 3)); replace — the licensing structure degenerates to one weight-independent requirement and the **typed/weak distinction itself collapses** (V_weak = V_typ = {s₁ ≥ 2, s₂ ≥ 2} ∪ {x ≥ 1, min(s) ≥ 15/8}), a strictly more demanding reading ((1/2, 3, 1) action-indexed typed-accept yet coupled-total full reject) |
| 5 | **The labelled-extension subsection** | **New §5.9** "The common-shock variant of the witness (a labelled extension)" (`\label{common-shock-variant}`), after §5.8, mirroring its format | The variant's model (the §6.3 decomposition, the five class definitions, the STAGED kink device); the regime-(i) handshake (Theorem 5 reproduced exactly on 676 grid states; ρ₁ = 2/3, ρ₂ = 3/2); **Theorems M1–M4 + CT** with machine-anchored proof sketches (A(p), the tent/kink cover argument, the boundary algebra, the collapse mechanism); the single-event sub-case; the δ-family (δ ∈ {0, 1/4, 1/2, 1, 5/4, 3/2, 2}; δ = 0 benign); the four-part relevance chain (the shared-heatwave rebuilding-certification decision; the 1/2-cut and κ\*-to-∞ report flips; the new exact witness data; the two action flips); verification (77 checks, **a fourth check list**, the family's non-pooling policy) and honest limits |

### The flaw-review riders (V53_FINAL_FLAW_REVIEW.md §3)

| Rider | Fix |
|---|---|
| **F1** (typographic, 5×) | Spaces inserted after "See Appendix A." at the five proof-pointer sites (lines 465/473/487/499/536) |
| **F2** (precision gloss) | Proposition 10's parenthetical gloss of I corrected: s₁ + s₂ **≥** 2 (I is defined with ≥; the strict gloss excluded the sum = 2 face) |
| **F4** (harmonization) | The 2015-stock gloss at §6.3 harmonized to the 33.8% / ≈ 299 kt framing (was ≈ 295 kt; the second site already carried the target framing) |
| **F5** (transparency clause) | One clause after Proposition 10's stipulated-visited-set sentence: the stipulated set is the pointwise worst case over alternation schedules, scoping the impossibility to the worst-case alternation |

**F3** is not a separate rider — it *is* the row-(iii) refinement (item 4), as the flaw review's §5 dispositions provided.

## 2. Build and verification battery (all green)

Build: `make_v54_p1.py` (this folder) — 16 anchored, position-recorded edits; **inverse-reconstruction gate**: reverting all 16 edits reproduces v53 byte-identically (the diff is exactly the wave); **math-span multiset preservation**: v53's 1,061 spans intact, 186 added, with exactly the two rider-enumerated span alterations (F2's gloss, F4's 295→299) accounted; **frontmatter gate**: title/abstract/highlights byte-untouched (the σ-abstract decline of Task 108 stands); destination-exists check; idempotent.

1. **Machine anchor re-verified:** `middle_regime_verify.py` re-run before transcription — 77/77, exit 0, byte-reproducible.
2. **Hand re-derivation during transcription** (the flaw-review standard): every transcribed closed form re-derived by hand this round — V_typ^cs/V_weak^cs/FP_cs (FAST's max(2p, p+1/2), SLOW's mirror, STAGED's g(p) = max(p,1−p)/2 − 1/8 all re-derived from the per-coordinate dip algebra); the tent-cover reduction to p ∈ {0, 1/2, 1}; the licensing-invariance endpoint 1/(1+ρ₁) (= s₂/(2−s₁+s₂) at δ = 1/2, checked at the canonical datum: 3/5); the κ\* trichotomy's structural 3/8 boundary; the blend-window algebra (both trough formulas; the (1/2, 1, 1) window [2/3, 1/3] empty); the coupled boundary δ = 5/4 (every I-state has sum < 4; (1/2, 79/40, 79/40) at δ = 49/40 exactly on the boundary); the relocation gap and (1/2, 3, 3); CT's A(p) ≥ 2 degeneration and the three serving witnesses ((1/2, 3, 1) serves [1/2, 1]); the single-event sub-case's three sets.
3. **Compile:** tectonic clean — **47 pp**, zero errors, zero undefined references; 114 warnings vs v53's 108, all the same cosmetic under/overfull class (the +6 are the widened Table 5 cells' narrow-column line breaks; the only overfulls are the two pre-existing 2.43pt header-rule boxes, byte-identical to v53's); **flat compile clean** (tex + figs_p1 alone in a fresh directory — the Task-101 scenario stays fixed).
4. **PDF text layer:** all 25+ new-content markers present (the three initially-unmatched phrases located: display-math boundary, the caption's typographic apostrophe, and the row-(iii) cell's pdftotext column-interleaving — the PDF renders correctly); zero stale markers ("not analysed", "honestly open", "Appendix A.The", "≈ 295 kt" all gone; "295" survives only in von Neumann's page range); 33.8% ×2 and ≈ 299 ×2; "Section 5.9" ×8 (M3 caveat ×2, §5.4 bullet/pointer/caption/middle cell/row-(iii) cell, §5.7 — exactly as built); "Section 5.8" ×3 in the PDF (1 hardcoded in §5.9 + the 2 rendered `\ref{substitutability-spectrum}` cross-references of v53).
5. **Never-overwrite audit:** the warning-comparison recompile touched the shipped v53.pdf; caught by `git status` and **restored byte-exact from git** (md5 adcc2268…) — the Task-107 protocol applied. The tree now shows only new files (v54.tex, v54.pdf, this folder).
6. **Diff review:** the full 437-line v53→v54 diff read hunk-by-hunk — exactly the 16 edits, nothing else.

## 3. The superseded placeholders (recorded verbatim; the supreme rule)

The owner's approval of the Table 5 fill and the row-(iii) refinement provides for replacing the open-cell placeholders by their computed verdicts. The four superseded v53 strings are recorded verbatim in `make_v54_p1.py`'s `SUPERSEDED` dict (the pointer sentence, the caption, the middle cell, the row-(iii) cell) and remain in git history and in v53 itself. The pointer sentence's discipline ("a verdict computed, not asserted") is preserved inside its replacement.

## 4. Standing items not in this round's approved scope (recorded)

- **Contributions list (§1.3):** no (xii) item added for §5.9 — not in the approved list; §5.9 is discoverable via §5.4's four pointers, §4.10's caveat, §5.7's trichotomy paragraph, and the Table 5 caption. A future additive item is a one-line option.
- **Abstract/highlights:** untouched (the Task-108 σ-abstract DECLINED ruling stands; this round added nothing abstract-side).
- **§4.8's check-list sentence** ("the two counts index different check lists"): left as is — historically accurate; §5.9 declares itself the fourth list.
- **Other family manuscripts:** no version bumps — the v54 wave is P1-only by the approval; no other manuscript references Table 5's open cell (verified in Task 106's consistency check: the middle-regime cell has no family pre-computation and no family cross-reference).

## 5. Honest residuals

- The off-diagonal geometric residual (σ-wave §7) stands as documented.
- The Zenodo deposit refresh remains owner-side.
- The middle-regime wave's own honest limits are inherited verbatim by §5.9 (stated there): witness-datum decomposition only; the two regime-(iii) readings bracket the coupled truth (both stated, neither chosen); grid verification fail-loud but finite with closed-form proofs cross-checked at every grid point; the κ\* ∞ verdict structural.

## 6. Reproduction

```
cd "batch 8/middle_regime_wave" && python3 middle_regime_verify.py   # 77/77, exit 0
python3 "batch 8/v54_implementation_wave/make_v54_p1.py"             # v53 -> v54 (16 edits, gated)
cd "arena agent 1/paper rewrites/latex" && tectonic paper1_assessment_separation_v54.tex
```

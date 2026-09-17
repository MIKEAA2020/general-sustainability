# Joint Evaluation — Gemini & Grok Humanized Rewrites of E3 (2026-09-17)

Sources: `uploads/gemini,grok humanized e3.txt`. Verified against frozen
`e3/paperE3_edwards_forecast_ladder_v16.tex`, `wave_e_edwards` archives
(annual_panel.csv, e3/e4 audit layers, intervention bound files), and the
claims ledger. House format: drift audit first, then style, then adjudication.

## 1. Drift audit

Token scan vs frozen vocab (v16 ∪ ledger): Gemini 52 distinct candidates /
Grok 3. Rulings on the load-bearing ones:

| Item | Gemini | Grok | Ruling |
|---|---|---|---|
| Pre-permit map parameters | γ̂ = −0.0310, δ̂ = −0.217 | not quoted | **GEMINI DRIFT (material)** — archived fits: γ ≈ −0.0284, δ ≈ −0.254 (intervention_boundaries / e4_audit_layer.json). Gemini's are wrong values, not rounding. The β̂ ≈ 0.0175 it prints alongside is archived (v16) |
| Counterfactual outcome numbers | "20% reduction (76.4×10³ ac-ft) → +5.2 ft, 646.8 ft (2023)" | not quoted | **PENDING-CLASS** — no archived artifact prints 76.4 / 5.2 / 646.8; v16's counterfactual carries different prints. Reject unless provenance is produced |
| Recovery-window row 43.62 / 55.32 / 33.72 | printed | printed | CLEAN — all archived in v16 (fixed-window table; 55.32 matches the M2 projection error, 33.7 the rain oracle) |
| 1956/1957 recharge pair 43.7 / 1,142.6 | printed | "R_1957 = 1143" | PARTIAL — 43.7 and 1143 are archived prints; Gemini's "1,142.6" adds unarchived precision. Accept as 1,143 only |
| Recharge/pumpage spans (44–2,486; 300–540) | printed | printed | CLEAN — archived in v16 |
| [610, 710] clip; 645.8 ft 1990 head | printed | printed | CLEAN — archived |
| Stage thresholds (660 ft Stage I) | printed | printed | CLEAN — matches v16's drought-stage convention |
| 3,207 German wells ML benchmark | — | printed | CLEAN — archived in v16 (it is a frozen cross-domain pointer, not new) |
| Comal Springs service series (§5.5) | developed | referenced | CLEAN topic (v16 threshold line archived); Gemini's added hydrograph detail to be checked at typesetting |

Verdicts: as with E1 — Grok high-fidelity (3 candidates, all archived),
Gemini more accessible but with two material drifts (map parameters,
counterfactual outcomes) that would corrupt the paper if adopted wholesale.

## 2. Style evaluation (four axes)

- **Humanized.** Gemini's structure is the strongest in the bundle: Definition
  3.1 (one-pool map), Remark 3.1 (class reduction), Definition 4.2 (frozen
  retention rule), §4.1 "Protocol Record and Pre-Declared Deviations" — that
  last one is exactly the E3 frozen-design story told in three lines, and it
  matches v16's own discipline ("avoid 'pre-registered'; record deviations in
  one place"). Adopt that structure verbatim-in-spirit.
- **Seamless flow.** Gemini's "Timing Bottleneck: Forecasting vs Nowcasting"
  heading (§6.1) names the paper's actual thesis better than v16's own
  section header; adopt the phrase. Grok's La Niña sentence ("September–
  November 1956 is La Niña (−0.92) and does not announce R_1957 = 1143") is
  the best single sentence on the climate modules in either file; adopt with
  its archived numerals.
- **Enhancing.** Gemini's counterfactual framing (pumping scenarios through
  the pre-permit map) is the right way to tell §5.6 — but renumber with
  archived outcomes only. Grok's "physical threshold high enough that Comal
  Springs does not cease" restatement of the cessation line is clearer than
  v16's; adopt.
- **Weaknesses exposed in OUR E3.** Both: (a) the point-rule/unified-rule
  M1 split is explained in two places and hedged in both — v18 states it
  once, plainly, with the ledger's CL-RULE row phrase; (b) the h>1
  climate-score convention (one-step forecast held constant) appears as a
  parenthetical — both rewrites promoted it to a convention line, as does
  v18.

## 3. Adjudication and implementation plan

- **Adopted base:** none (drift on both, per firewall). New artifact:
  `e3/paperE3_edwards_forecast_ladder_v18_humanized_gemini_weighted.md`
  (this turn) — Gemini-weighted prose (its §4.1 protocol-record structure,
  §6.1 bottleneck framing), Grok-fidelity sentences where cleaner (La Niña
  line), archived numbers only, rejected: γ̂/δ̂ pair, 76.4/5.2/646.8,
  "1,142.6", ASCII figures.
- **W1 (this turn):** v18 humanized as above.
- **W2 (owner-gated):** Re-derive and REGISTER the counterfactual-outcome
  table from `intervention_boundaries_v2.csv`/harness before any version
  prints scenario outcomes (Gemini's unarchived ones are presumed a fresher
  but unregistered pass — the numbers may be real but have no archive
  provenance). Restating the pre-permit map parameter set (γ/δ) belongs to
  the same registration. Comal-series fit details likewise.
- **W3 (packaging):** figure-axis captions, availability blocks, PDF build.

## 4. Note on rule-version language
v18 keeps v16's frozen verdict framing unchanged: point-rule M1 retention
(provisional, coin-flip, h=1) vs unified-rule withholding — one sentence,
ledger phrase CL-RULE-EDW-M1-DIFF, no re-hedging elsewhere.

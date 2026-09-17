# Joint Evaluation — Gemini & Grok Humanized Rewrites of E1 (2026-09-17)

Sources: `uploads/gemini,grok humanized e1.txt` (Gemini rewrite ~112 KB incl.
full re-tex of Abstract→References; Grok rewrite ~68 KB). Verified against
frozen `e1/paperE1_cod_forecast_ladder_v50.tex`, the claims ledger, and the
archived F1 v26 instrument values. House format per V11 precedent: drift audit
FIRST, then style, then adjudication. Supersedes (with carry-over) the
superseded Grok+Claude audit pair — its evaluation
(E1_HUMANIZED_JOINT_EVALUATION_20260917.md) remains the record for W2
scientific items.

## 1. Drift audit (before any adoption)

Automated numeric-token scan vs frozen vocab (v50 ∪ ledger):
Gemini 44 distinct non-whitelisted tokens / Grok 4. Adjudication of the
load-bearing ones:

| Item | Gemini | Grok | Ruling |
|---|---|---|---|
| Simulation operating numbers (D1/D5) | "96.5–98.5% recovers true autonomous", "97.0–98.5% rejects under null" | not asserted | **GEMINI DRIFT** — frozen F1 v26: D1 0.955/0.960, D5 spec 0.995/0.950. Both ranges are wrong; sentences rejected |
| Cadigan reference | "CJFAS 73(2), 286–308" | n/a | **GEMINI DRIFT** — frozen string: 73, 296–308. Page-number error |
| References added | "Kell et al. 2021, A validation framework…, Fish. Fish. 22(5), 1100–1114" — a real paper but NOT in the frozen list | — | **GEMINI DRIFT (firewall)** — references are frozen strings; new citations never enter via a prose pass |
| Derived arithmetic presented as data | "+37.4 kt", "+693.3 kt", "70.9% / 94.9%" splits (158.4 kt printed) | none | **PENDING-CLASS** — 158.0/337.4 are archived (v50 stale-start controls) but the derived percentages and 158.4 are not printed anywhere. Rule: archive the computation first (ledger) or drop the figures |
| Schijns-vs-STATLANT 1956 (236,210 vs 263,210 t) | — | present, verbatim-correct | **GROK CLEAN** (frozen v50 line) |
| Kell et al. 2016 citation | correct | **"ICES J. Mar. Sci. 73(8), 2094–2103"** | **GROK DRIFT (single)** — frozen string: Fisheries Research 183, 119–127 |
| Kokkalis 2024 citation | present | — | CLEAN (frozen in v50) |
| Tables/equations | full re-tex with frozen numerals; M4 decomposition re-expressed at more precision | compact restatements | Gemini table layer largely faithful AFTER filtering the flagged rows |

Verdicts: neither rewrite is adoptable wholesale. Grok = high fidelity with
one reference-string error, heavier register — same profile as its framework
rewrite (V11). Gemini = the more accessible architecture but repeats its
verified drift pattern: wrong sim ranges, one wrong page range, added
references, derived percentages presented as results.

## 2. Style evaluation (four axes)

- **Humanized.** Gemini: topic sentences, numbered moves ("(1) … (2) … (3)"),
  plain transitions, Definitions/Remarks boxes that make the ladder legible —
  the target register for the owner's directive. Grok: faithful but
  telegraphic, abstract compressed to the point of omission.
- **Seamless flow.** Gemini adds genuine connective tissue at section joints
  (its §4 openings are the best in the file). Grok's flow relies on the frozen
  text's own transitions.
- **Enhancing.** Gemini's M4-decomposition TABLE (delay cost vs model cost at
  both horizons, both specs) is exactly the audit-level restatement that E1
  needed — adopt the STRUCTURE, with arithmetic re-derived from archived rows
  only (86/12 h=1 Spec A; 693.3 split vs 158.0/337.4 controls h=5 Spec B).
  Gemini's class-reduction and protocol-record framing (Definition/Remark
  boxes) — adopt. Gemini's ASCII figure mocks — reject (journal register,
  per V11 precedent). Grok's hazard-warning sentences about the flat valley
  — adopt as sentences.
- **Weaknesses each exposes in OUR paper.** Both independently expose the same
  two: the abstract still reads the obstruction late (fixed in v52/v53), and
  the freeze chronology is scattered (pass-dates absent from the manuscript
  body). Both go to W3/packaging.

## 3. Adjudication and implementation plan

- **Adopted base:** none. Both contain confirmed drift; the owner directive
  demands Gemini-weighted prose with error-free delivery → the merged artifact
  is a NEW v53 humanized version (this turn), styled on Gemini's mechanics,
  fact-bound by the firewall, harvesting Grok's fidelity sentences with their
  one citation error corrected from the frozen list.
- **W1 (this turn):** v53 = Gemini-weighted humanized E1 (abstract, intro,
  design, results narrative, M4 table, status notes, conclusions); frozen
  numbers only; rejected items excluded (sim ranges, Cadigan 286, Fish-Fish
  addition, derived percentages, ASCII mocks).
- **W2 (owner-gated scientific, carried from the superseded Grok+Claude
  pair):** Prop 4.1 restatement (Claude A1 — flip-bifurcation regime; the
  single strongest scientific finding in either audit bundle), Lemma 3.2
  demotion, flat-valley/box-prior sensitivity section, regularised M1
  profile, drift/damped-trend baseline, LOO influence — all require harness
  runs + ledger registration.
- **W3 (packaging):** highlights ≤85 chars, availability blocks, Rose (2026)
  bibliographic lock, figure captions, PDF rebuild.
- **Ledger:** derived-arithmetic candidates (158.4-kt class) are either
  computed into a registered phase file (then citable) or stay out of the
  paper. No action taken this turn.

## 4. Carry-over ledger from the superseded Grok+Claude pair (user direction)

Open and carried: Claude A1 (Prop 4.1), Claude A2 (Lemma 3.2), Claude A5
(flat valley/box priors), Claude E7/E8 (drift baseline, LOO influence),
Claude A10 (Schijns-vs-STATLANT wording of the annual pass).
Already implemented in v52 and confirmed redundant for v53: Brier/direction
conventions-at-first-use, M4 label fix, abstract honesty items — absorbed
here and closed in the superseded doc.

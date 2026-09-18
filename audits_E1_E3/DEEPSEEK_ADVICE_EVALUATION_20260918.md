# Evaluation of "deepseek advice.txt" against E1 — verdicts, amendments, implementation (2026-09-18)

**Subject.** DeepSeek's framing critique of the E1 v57 rejection-response patch and its proposed replacement abstract + §1. Carrier of consequence: `e1/paperE1_cod_forecast_ladder_v58_humanized` (stamp `hu58-c1375ed`).

## 1. Evaluation of the diagnosis — adopted

DeepSeek's register diagnosis is sound and is adopted in full:

- Formal articles state findings; "this is neither X nor Y" is a negative definition that reads as rebuttal. True of my v57 abstract clause ("forecast-skill audit, not a re-estimation or replication") — removed.
- A dedicated "**Scope clarifications**" header in §1 signals contested scope — removed; the same content now lives as ordinary §1 framing in positive form.
- Conditional hindcast should be stated as a design fact that favours structure (conservative negative result), not as a concession — adopted verbatim from the advice ("Both features favour the structural models...").
- Monitoring-data coverage should be stated as coverage, not as rebuttal ("already enter ... reserved") — adopted with DeepSeek's own formulation.
- The objection-to-monitoring-data has a kernel of truth; the scope statement suffices for a modelling journal, RV-survey scoring remains the answer if a fisheries venue is attempted — noted as correct; `wave_e_cod/data/rv_fall_abundance_schijns_table3.csv` stands ready (34 rows, 1983–2016).

## 2. Verification of the proposed replacement text — three defects found and fixed

| DeepSeek's draft | Verdict | Amendment applied in v58 |
|---|---|---|
| "Two **independently** estimated series describe the same stock" | Independence is unarchived | "Two **published** estimated series ...". |
| "Operating characteristics ... measured in the companion framework paper" (as abstract close) | Misdirects: §3.7 of this carrier measures them in-paper | Closing changed → "measured in this paper (Section 3.7) under protocols archived with the companion framework paper", and the quantitative simulation results (97–99% specificity/power; <15% stock-flow/depensation) restored instead of a bare pointer. |
| Sustainability caveat dropped entirely | Frozen corpus (v50–v56) always carried it (v55 conclusions: "no conclusion follows about stock sustainability; no model shown best available") | Restored in DeepSeek's own positive style: "The result bears on forecast skill, not on stock status; no tested model is shown to be the best available." |

Also restored from v56's abstract that DeepSeek's compression dropped: the closing burden-of-proof sentence ("...cannot be assumed from structural elaboration alone..."); the roadmap sentence amended to name Appendix A.

Numerals in DeepSeek's draft audited against frozen archives: **all correct** — 98 / 115–196 / 265 / 289–488 / 84 / 120 / 694–819 / 670 / **688** (confirmed archived: v50 Table fixed-window mean=688; v50 abstract's own phrasing), 97–99%, 15%.

## 3. What was NOT adopted

- **Wholesale replacement of §1.** DeepSeek's §1 would silently de-cite roughly ten bibliography entries (Hyndman & Koehler 2006, Kell 2016/2021, Carvalho 2021, Kokkalis 2024, Walters & Maguire 1996, Shelton & Healey 1999, Rose & Rowe 2015, Rose 2026, Schijns 2021, Murphy 2025) and drop the two-shortcomings motivation ("Target Disconnect" / "Binary Certification") that is the paper's raison d'être. Instead: DeepSeek's object/target/coverage paragraph was **inserted** after §1 paragraph 1, the v57 scope-paragraph deleted, and a roadmap sentence added — every citation and paragraph of §1 survives.
- DeepSeek's keywords list (drops "model identifiability") — v56 keyword set retained.

## 4. Completion steps

- `e1/paperE1_cod_forecast_ladder_v58_humanized.md/.tex/.pdf` built (24 pp), numeral battery: **zero lost / zero new** vs v57; banned-token scan clean; citation inventory unchanged; abstract complete with links.
- Abstract now 402 words (v57: ~700), carrying every frozen quantitative claim of the long version except none.
- Cover-letter register already plain-positive (no rebuttal framing) — nothing to backport. If you want a resubmission cover letter that *does* carry the category-explanation (per DeepSeek's principle that the category error belongs in the letter, not the paper), say the venue.

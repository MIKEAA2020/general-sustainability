# PHASE B CHANGELOG — v14 → v15 (2026-09-13)

Text-only implementation pass per the owner's Phase B mandate (profound resolutions / root-cause analysis; honesty; novelty).
Source: `paperF1_retention_framework_v14.md` (untouched). Result: `paperF1_retention_framework_v15.md` (64,561 chars, 450 lines; 50 diff lines).
Applied by `framework/apply_phaseB_v14_to_v15.py` — 25 asserted replacement rules, one pass, idempotent (byte-identical re-run).
Decision record: `PHASE_B_ROOT_CAUSE_DECISION_MEMO.md`; owner answers collected interactively 2026-09-13:
**AD6 adopt fully · AD2 option (a) · AD4 option (b).**
Style gate: `journal_style_automated_scan.py` on v15 → 0 blockers, PASS.

## AD6 — the reframe (adopted fully): the deliverable is the standard

Root cause (memo §1): the paper's structure already *is* a reporting standard (rule → information-set audit → operating-characteristic study), but the framing presented it as a rule case study; its strongest results (empty retained set, power ≈ null in D3/D4, IC dominance) then read as failures of the instrument instead of evidence for the standard. One coordinated pass rewrote the framing surfaces; every verdict, table, and number is untouched.

| # | Surface | Change |
|---|---|---|
| 1 | Title | → *"When a model is not retained, what must be reported? A retention rule, an information-set audit, and operating characteristics — a minimum reporting standard worked on three scored objects in two domains"* |
| 2 | Abstract Problem | + "The field lacks a minimum standard for making such claims interpretable; this article proposes one and demonstrates it." |
| 3 | Abstract Approach | "states a retention rule…" → "proposes a minimum reporting standard for non-retention claims, with three components: …" |
| 4 | Abstract Approach | "The rule is applied unchanged" → "The standard is worked unchanged" |
| 5 | Abstract Implications | "leaves the reader unable to distinguish" → "…the two, which is why the standard makes them mandatory"; IC dominance reframed as "instrument choice within the standard, not against it" |
| 6 | Keywords | + "reporting standard" |
| 7 | §1 contribution paragraph | "It is that same rule…" → "It is a minimum reporting standard… The rule is the worked example; the standard is the deliverable." |
| 8 | §1 section map | "Section 7 states what pair jointly licenses and not" → "what the standard extracts from the pair, and what it does not license" |
| 9 | §7 heading | → "## 7. What the standard extracts from the two applications" |
| 10 | §7 Licensed opening | "Rule applicable…" → "The standard is applicable…" |
| 11 | §7 Implication | "Any non-retention report should carry the standard's three components: …"; IC sentence scoped "within the standard, not on the standard" |
| 12 | §8 first sentence | "Retention rule stated as algorithm…" → "The minimum reporting standard for non-retention claims is stated and demonstrated: …" |
| 13 | §8 last paragraph | + "The negative findings are themselves evidence for the standard: a pre-registered, calibrated rule retains nothing where the data are uninformative, and only the operating-characteristic study reveals the difference." |

## AD2 — mechanism misattribution (option a)

Root cause (memo §2): "false retention" conflated decision error (D5: the gate errs) with mechanism error (D6/D7: retention is correct by the rule's own licensing, but the predictive gain is not caused by the module's mechanism). The frozen pre-registered labels are kept; the concept is renamed in prose and the table gains a column stating what each row measures.

| # | Change |
|---|---|
| 14 | Table 2b: new column "Row measures" — D1–D4 "decision reliability", D5 "decision reliability (specificity)", D6/D7 "mechanism attribution"; frozen "false retention" Note labels untouched |
| 15 | Abstract D6/D7 sentence: "false retention 0.680/0.760 …" → "mechanism misattribution 0.680/0.760 … → mechanism misattribution 0.975/0.925 …" |
| 16 | §4.5 comparison-table header: "false retention misspecification D6-D7" → "mechanism misattribution, misspecified (D6-D7)" |
| 17 | Licensing sentence: + gloss "mechanism misattribution — retention on a real predictive gain that the module's mechanism did not cause" and the column's purpose |

Kept untouched (decision-error contexts, correct usage): "false retention 0.044 per module-replicate pair" (abstract + §4.3), "1.5–3.0% false retention under in-class null", the summary block's "False retention:" rates, and the frozen Table 2b labels.

## AD4 — prospective band, future-only (option b)

| # | Change |
|---|---|
| 18 | §4.5 registration sentence: + "for future applications of the standard; it never re-opens the verdicts reported here, which remain decided by the frozen 5% band." |

## Audit trail

- v14 untouched; the edit script reproduces v15 from v14 byte-for-byte (verified idempotent).
- Register updated: §5 Phase B marked DONE; §9 carries the owner decisions.
- v13 → v14 → v15 lineage: each version produced by its own asserted script, never overwritten.

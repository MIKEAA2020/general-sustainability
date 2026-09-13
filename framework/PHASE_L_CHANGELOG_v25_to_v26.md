# Phase L changelog — v25_restructured → v26_restructured (2026-09-13)

Owner-approved scope (OWNER_REVIEW_20260913_RELAXATION_AND_PHASING.md): O18, O22,
O24, O25, O27, O29 (+ NEW-19 band-invariance extension), O33, O37, O38, O39, and
the NEW-18 supplement move (Diebold–Mariano mechanics of Section 5 → S1.4).
One pass, 16 count-asserted rules in `apply_phaseL_v25_to_v26.py`.

| Rule | Open item | Edit |
|---|---|---|
| L1 | O38 | Abstract: "applied, unchanged" gains the parenthetical "(the one recorded rule-version difference is stated in Section 4)" |
| L2a | O37 | §1: "portable and domain-free" → "portable in their statement and demonstrated here on two domains" |
| L2b | O18 | §1: the normative core and a fillable checklist are stated separately as the two-page Supplement S2 |
| L3 | O29 | §2.2: the tie band is a practical-equivalence margin — pre-registered here at 5%; simulation-calibrated (Section 8) or decision-based bases admissible, basis stated |
| L4 | O24 | §2.2 after Definition 2.2: certificate claim-strength levels N0–N3, expiry (revised vintage / re-scored origin / amended rule), combining (lowest level of parts); the reported verdicts carry N2 |
| L5 | O27, O29 | §6.4: two-axis reading guide (predictive result × structural interpretation: identification-limited / gate-withheld / structurally redundant) + epistemic-consequence sentence (descriptive rather than evidential where the rule lacks power) |
| L6 | O27 | §4: the M2m decline is a ladder-membership verdict, not a predictive finding; its predictive margins remain reported (Table 5) |
| L7 | O25 | §4: Edwards decision-context paragraph (forecasting claims, not the permitting framework; persistence remains the decision baseline) |
| L8 | O25 | §5: cod decision-context paragraph (hindcast verdicts about forecast utility, not stock status or the assessments) |
| L9 | O29, NEW-19 | §6.5: the reported verdicts are band-invariant (cod: ranking alone decides; Edwards: class grounds at any band), so the calibration governs future verdicts only; decision-basis option stated |
| L10a | O29 | §8: a decision-based margin is an admissible alternative basis; the adopted basis is stated with the verdict |
| L10b | O22 | §8: third-domain prospective registration — audit, origin-matched baselines, rule + band + basis, OC study before any evidential claim (N3), pinned-seed archival, certificate level per verdict |
| L11 | O33 | §9: adoption tiers — core / evidential / strong non-retention (N3); the evidential tier is this article's own practice |
| L12 | O39 | §6.1: three quantities kept distinct — model-class identification (power), predictive selection, mechanism attribution |
| L13 | NEW-18 | §5: DM mechanics compressed to the descriptive label + non-calibration caveat + pointer to S1; verdicts "do not rest on DM statistics" retained |
| L14 | — | Data availability: Supplements S1 and S2 described |

**Supplement v26** (`paperF1_retention_framework_v26_supplement.md`, v21 supplement
left frozen): S1.1–S1.3 carried over, **S1.4** carries the moved Diebold–Mariano
mechanics verbatim, **S2** is the new standalone two-page specification and
fillable checklist (Page 1 normative: obligations, output vocabulary, N0–N3,
the worked rule, reporting a verdict; Page 2 fillable form).

**Verification.**

- Idempotent: v26 byte-identical across re-runs.
- Numeric accounting v25→v26 (main text): 444 → 431 tokens; **0 added**; the 13
  removed tokens (0.99, 0.001, 0.007, 0.042, 1.0, 1.85, 1.88, 4.7, 20.2, 28,
  92.5, 144.7, 177.4) are exactly the moved DM-mechanics tokens, all present in
  S1.4 — no other number added, removed, or altered.
- Scanners on v26: journal_formalization 0 flagged; journal_style PASS;
  redundancy 0.
- Coverage (main + v26 supplement vs v0 and v13 baselines, the established
  pair convention): all numeric claims covered, all domain terms OK. The
  main-only scan's "10.8645" flag is the pre-existing lineage disposition
  (superseded appendix oracle value; lives in S1.3 — the pair scan covers it).
- Frozen elements untouched: no reported verdict, frozen label, ladder rung,
  output vocabulary, pinned-seed number, or the executed band calibration was
  changed. Contradictions: 43 adjudicated, 0 outstanding (NEW-18/NEW-19 are
  owner decisions and review records, not contradictions).

Open after Phase L: O19 (owner approval of the proposed prospective
class-grounds criterion), O20/O30/O32 (Phase M), O26/O28 (Phase N), O23
(Phase O); O4/O5/O16-remainder/O35/O36 as before.

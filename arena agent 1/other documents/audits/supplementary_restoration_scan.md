# Supplementary Restoration Scan (Turn 51)

**Question.** Do the latest supplementary files differ from their older versions in any way beyond intended edits — accidental content loss, or anything worth restoring as-is or after correction?

**Files compared.** `paper1_supplementary.md` (v1 only), `paper3_supplementary.md` (v1 only), `paper4_supplementary.md` (v1) vs `paper4_supplementary_v2.md` (v2), `paper5_supplementary.md` (v1) vs `paper5_supplementary_v2.md` (v2).

## Verdicts

1. **P1 (`paper1_supplementary.md`): single version; nothing to compare against.** It is the only version ever written; its content is fully referenced by P1 v6/v7's supplementary pointer (extensions, statuses, conjectures, verification artifact details). No older alternative exists on disk or in the repo history. **Nothing to restore.**

2. **P3 (`paper3_supplementary.md`): single version; nothing to compare against.** Same situation; S1–S4 fully referenced by P3 v6/v7. **Nothing to restore.**

3. **P4: v2 = v1 verbatim (22,107 chars) + S9/S10 appended (5,722 chars).** Verified programmatically: the entire v1 file is a byte-exact prefix of v2. S1–S8 are untouched; the turn-50 consolidation added only the delayed-recruitment registration records (S9) and the expanded-proof details (S10). **Zero loss.**

4. **P5: exactly 5 diff hunks, all intended.** The v1→v2 diff contains exactly five hunks at the five locations of the turn-50 alignment fixes: (a) the subtitle line ("42-Stock Spectral Null" → "Selected 42-Stock Spectral Screen"); (b) the S1 inventory entry for §3.4 (reconstruction record added); (c) the S1 entry for §3.5 (screen/null wording); (d) the S1 entry for §2.7/§3.8 (lemma proof location); (e) S2.2 (informal proof replaced by deferral to the main-text proof) and (f) S8 (legacy-vs-reconstruction distinction). Sentence-level check: every sentence of v1 that is not verbatim in v2 belongs to one of these replaced blocks — **zero accidental loss.**

## Is anything worth restoring?

- The P5 S2.2 informal proof sentences were removed in favour of a deferral to the now-complete main-text proof (P5 v6+). **Not worth restoring:** the content survives in stronger form in the main text, and the v2 S2.2 retains the conditional-status remarks and the multiplicative-mortality summary.
- The P5 S8 "computational record is incomplete" passage was replaced by the legacy/reconstruction distinction. **Not worth restoring:** the replaced text stated the legacy record as the only record, which P5 v6's §3.4 superseded; the v2 register states both records at their true statuses.
- P1/P3 have no older versions anywhere (repo history included — their supps were created once and pushed verbatim since).
- No supplementary file contains numbers that changed between paper versions; the cross-checks of the turn-50 alignment pass (S4/S5/S6 values vs P5 v6, S7 witness vs P1 v6 §4.5/§4.9, split-assignment values vs P3 v6) remain valid against the new latest versions (no body numbers changed in v7/v8/v9).

**Bottom line: no accidental content loss in any supplementary file; nothing to restore.**

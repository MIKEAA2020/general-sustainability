# Phase B — Root-Cause Decision Memo (2026-09-13)

**Mandate (owner directive):** profound resolutions and root-cause analysis over shallow quick-fixes; honesty and novelty.
**Scope:** the three owner-gated items (AD6, AD2, AD4) plus the root causes behind the defect classes the two audits surfaced.
**Discipline:** every decision here is recorded *before* any edit; implementation is then a single coordinated pass producing **v15** (v13/v14 untouched).

---

## 1. AD6 — the reframe: what the paper is actually *for*

**Claude's point (§0):** the deliverable should be "a minimum reporting standard for non-retention claims," with the retention rule as the worked example — not "here is a retention rule applied to three objects."

**Root cause of the tension.** The paper's structure (§2 rule → §3 information-set audit → §4 operating characteristics) *already is* a reporting standard; the framing just hasn't caught up with its own strongest result. The paper's sharpest findings are negative: the rule retains nothing on two real objects, has power ≈ null in three of four structural classes (D3/D4), and is dominated by a simple information criterion. Presented as "a rule that works," the paper is a paper about a failed instrument. Presented honestly — as the *demonstration that non-retention claims are uninterpretable without exactly this machinery* — every one of those negative results becomes load-bearing evidence: **if even a pre-registered, calibrated, power-reported rule cannot certify retention here, what does that say about uncalibrated ad-hoc retention claims in the literature?** The IC-dominance result converts from an embarrassment into the standard's first comparison point.

**Why this is a root-cause resolution, not a re-brand.** The reframe does not discard the rule — it repositions the three existing sections as the three components of a reporting standard (a decision rule stated as an algorithm; an information-set audit separating available from supplied from revised; a mandatory operating-characteristic simulation). That is what the paper already requires of itself. The reframe also resolves qwen 3.3 ("why should a forecaster adopt this rule?") without contorting the rule's design.

**Cost (honesty about scope).** Title, abstract, §1, §7, §8 change in one pass; §2–§6 keep their content, with §7's "what the applications show" re-read as "what the standard extracts from each application." Verdicts, tables, and numbers are untouched. This is the only Phase B item that changes the stated contribution, which is why it is owner-gated.

**Recommendation: adopt fully.** Novelty is higher ("machine-checkable negative certificate with mandatory power reporting"), and it is the honest reading of what the evidence shows.

---

## 2. AD2 — D6/D7: the label that hides the mechanism the DGPs actually test

**The defect.** "False retention" conflates two different failures: (a) decision error — the gate retains when it should not; (b) mechanism error — the gate retains for a real predictive gain that is *caused by something other than the module's mechanism*. The D6/D7 DGPs test (b): under drifting productivity and under observation error, modules genuinely predict, so retention is *correct* by the rule's own licensing ("retention licenses a prediction claim, never a mechanism claim" — already added in v14). Calling D6/D7 "false retention" invites readers to believe the rule failed, when the row's real content is: **predictive success is not mechanistic evidence, and here is the measured gap between the two.**

**Root cause.** The DGP table (Table 2b) mixes decision-error rows (D5) and mechanism-error rows (D6/D7) under one label with no column stating which error each row measures. The pre-registered label was inherited, not designed.

**Resolution options:**
- (a) **Keep the pre-registered label in the frozen table** (pre-registration integrity — the label is part of the frozen sheet), add the prose rename "mechanism misattribution" and one table column "what the row measures: decision reliability vs mechanism attribution." Nothing in the frozen row labels changes.
- (b) Leave everything as v14.
- (c) Rename everywhere including the frozen table (breaks pre-registration — the D6/D7 rows were archived under "false retention"; a post-hoc rename of frozen vocabulary is exactly the class of edit this project prohibits).

**Recommendation: (a).** It adds clarity with zero pre-registration damage and turns a naming accident into an explicit measurement axis.

---

## 3. AD4 — the band: calibrate the operating characteristics, not the threshold

**The defect.** The 5% tie band was set ex ante but never simulation-supported. AD3 shows the load-bearing gate decision (M2m vs M1: 4.33% against the 5% band) sits 0.67pp from the edge — inside the environment sensitivity measured on cod (±17 kt on 445.5 kt = 3.8%). The band is doing gatekeeping at a precision its calibration does not support. claude 4.2: "pre-register the operating characteristics, not the threshold."

**Root cause.** The band was a reasonable editorial choice promoted to a decision threshold without the same operating-characteristic discipline the paper demands of modules. The paper's own §4 is the cure.

**Resolution.** A simulation-calibrated band targeting power ≥0.80 / specificity ≥0.90 at the object's own T and SNR, **pre-registered for future applications only** — retro-fitting would re-open closed verdicts and violate the freeze. v14 already carries the registration sentence in §4.5 (registration only; the 5% band and every verdict are untouched). Phase B decision is about the wording and scope of that sentence:
- (a) confirm v14's sentence as-is;
- (b) reword to state explicitly that the calibrated band applies to *future* applications and never re-opens this paper's verdicts;
- (c) remove the sentence.

**Recommendation: (b)** — the one-sentence addition costs nothing and pre-empts the misreading that current verdicts could change.

---

## 4. Root causes behind the defect classes (for the record — Phase C material)

1. **K-bound error (91.1/81.1 → 50.8/40.8).** Framework v13 compressed E1 v20's precise definition ("maximum over predictor states of the training transitions, excluding the terminal state") into a paraphrase that counted the terminal state. Lesson: definitions travel from companions **verbatim**, never paraphrased. (Fixed in v14.)
2. **Simulation provenance (N1).** The published §4.3 rates do not reproduce from the archived CSVs; the computation lineage is a transcript + generators, and the archived serialization belongs to a different run. Root cause: results were archived without a manifest pairing each CSV to its producing script version, seed, and environment hash. The profound fix (Phase C): re-run the generators and archive script+seed+env-hash+outputs as one unit — never output files alone.
3. **"5 of 32" vs "four of the twenty-eight" (N4).** Two universes (the full 32-row DM table including the four alternative-comparator rows; the 28-row primary-comparison subset) reported with different denominators in F1 and E1. Root cause: no single canonical DM-universe definition shared between companion papers. Fix: one sentence in each paper stating the universe (v14 done; E1 optional).
4. **Exhaustiveness (N6).** "All surviving points implemented" is only ever as-of-verified; precedent: E1's round-2 evaluation was later found non-exhaustive. The register now carries the caveat explicitly.

---

## 5. Honest uncertainties this memo carries forward (not hidden, not resolved)

- The candidate mechanism for the domain contrast (§6 of v14 — assessment-smoothing autocorrelation favouring persistence on the reconstructed target) is a **hypothesis registered with a decisive test** (rescoring D1 under a smoother), not a result.
- The M2m h=5 margin excludes zero by block bootstrap while the h=1 margin does not and MAEs tie — the tension is reported honestly in v14; no verdict is asserted beyond what the intervals support.
- The Edwards cross-environment tolerance figure (AD3) is **required and still missing** — the "gates are load-bearing" claim stands only as long as the rerun supports it. If sensitivity ≥0.67pp, the claim is downgraded in one coordinated edit. This is the single point that could overturn a headline claim, and it is left standing only with that condition attached.

---

## 6. Decision requests

Owner decisions on AD6 / AD2 / AD4 are requested via the interactive prompt; the register (§5 Phase B) is updated with the outcomes, and v15 is then produced as one pass per the chosen options.

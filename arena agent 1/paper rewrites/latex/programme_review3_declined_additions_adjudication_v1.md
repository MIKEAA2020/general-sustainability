# Programme review III — adjudication of the external reassessment of the declined additions

**Date:** September 26, 2026. **Record verified against:** the pushed tree at `fa5490a` (round 26 + figure-pin commit). **Method:** every factual premise in the external text checked against the shipped editions and locked files before any verdict; quotes traced to their sources; each decline re-derived independently of its original wording. No paper edited; the audit touches the programme record only.

---

## 1. What is being adjudicated

The external text evaluates three additions declined in review II §3.3 (hysteresis model in ARV, general max-plus duality theorem in ws, ecological viability-kernel section in ARV), the "insight density is already high" claim, and closes with a bottom-line test: the rejections would be wrong only if they also forbade mentioning the ideas as limitations, future work, or clearly cited extensions.

The external text is a faithful gloss of review II §3.3 — it quotes the recorded rationales almost verbatim. That makes this adjudication dual: it must verify the external text's reasoning **and** re-verify the recorded rationales it glosses. One of them does not survive.

## 2. Premise verification against the shipped record

| # | Premise | Status | Evidence |
|---|---------|--------|----------|
| P1 | ARV's locked files certify "comparisons, not the estimation a formal model requires" | **True, and understated** | ARV v6 contains zero statistical machinery (no bootstrap, confidence interval, likelihood, or posterior; grep count 0). All 236 verifier checks are exact rational recomputation. Claims are explicitly scoped: "their scope is the realized record" (l. 824). But the record certifies more than A-beats-B: exact temporal structure (1993 breach at 101.05 kt, 1995 minimum 9.68 kt, 22 consecutive below-floor readings to 2014, the 2015 re-crossing on both vintages) and exact threshold relations (276 / 884.6 kt). What it does not certify — and the external text correctly requires for a hysteresis model — is estimated switching thresholds with uncertainty, a transition rule, path-dependence effects, and validation. None of that machinery exists in the record. |
| P2 | P1 "already has an attributed Theorem 1" on the max-plus ground | **False** | P1 v53 contains **zero** max-plus content (grep count 0). Its eight theorems are: finite-horizon soundness and completeness, the common-action obstruction, the delayed-information obstruction, the LP instantiation of the timing certificate, the finite-time exit certificate, and three further theorems — none in max-plus algebra. The mis-premise originates in review II §3.3's own wording ("would re-prove P1's attributed Theorem 1 ground"); the external text hedged it with "if" but then reasoned from it as established. |
| P3 | P1 already owns the family's viability anchoring | **True** (wording: viability-*theory* anchoring, not "viability-application literature") | P1 v53: 67 "viability" hits, 10 "viability kernel" hits; the review II scan counts Aubin 14×, Saint-Pierre/Quincampoix 10×, Doyen 7× in P1. ARV cites no viability literature beyond the data sources and companions (now plus the one Hutchings–Myers sentence). |
| P4 | The insight-density inventory (ws factoring and stationary-policy propositions; comp redesign rates and belief cells; minimax tower and coupling orthogonality; ebc Hamming-regime separation) | **True** | All eight items verified present in the shipped editions: ws v15 factoring (1) and stationary (5); comp v15 redesign (4) and belief cells (2); minimax v7 tower (8) and coupling (16); ebc v6 Hamming (24). |
| P5 | The rejections are sound *unless* they forbid future-work mention | **Channels open and in use** | minimax v7 maintains a formal conjecture channel (9 mentions; `conj:envelope`; "recorded as conjectures", l. 65); ARV v6 has a Delimitations section (l. 739); ebc v6 has Delimitations (§ 0.10). The declines were cycle-scoped content decisions, not topical bans. One asymmetry the external text could not know: for the max-plus item, its own escape branch ("show a genuinely new case, condition, or proof delta") was tested against the record and does not fire — no shipped ws claim is blocked for lack of a general duality theorem (`prop:regime` certifies the instance exactly, inside the 54/54 chain), and ws has no conjecture apparatus at all (grep count 0), so an "extension" would need new section-grade machinery to be honest. |

## 3. The one mis-premise, corrected

Review II §3.3 recorded the max-plus decline with the rationale "would re-prove P1's attributed Theorem 1 ground." Verification shows P1 has no max-plus ground of any kind. Under the programme's rule (mis-premised items reported, not implemented), the rationale is retracted and the decline is re-derived from grounds that survive verification:

1. **No shipped claim needs it.** Every ws claim certifies at instance level; the regime-graph max-plus recursion is certified exactly (check P21, inside ws v15's 54/54). A general duality theorem would change no claim, method, or result.
2. **Scope.** ws is the certified-instances paper; a general theorem is theory-grade content whose natural owner would have to be P1 (the theory paper) — which has no max-plus content and does not need any.
3. **Attribution done the honest way.** The general algebra is now *cited*, not re-proved: ws v15 anchors the recursion at Baccelli et al. (1992) — the "clearly cited extension" form the external text itself recommends, already shipped.
4. **Cost side.** A new general theorem brings a new proof burden and a new owner question under the one-owner rule, with zero claim-level payoff.

This is the second review-era defect withdrawn after verification against the shipped text (the first: review I's minimax §2-reorder claim, withdrawn in round 26). The pattern and the remedy are the same: compute before asserting.

## 4. Adjudication per item

**4.1 Hysteresis model (ARV) — rejection correct.** The external text's provenance argument is right and, if anything, conservative: the record certifies deterministic recomputation of a realized record, and a two-threshold hysteresis model is an estimation-and-validation device the record cannot support. Its carve-out ("could survive as speculation, future work, or a clearly labeled conjecture") is available but not merited: ARV's Delimitations section already scopes the paper to the realized record, the paper contains zero hysteresis language by design, and the interpretive residue the model would address — the asymmetry between certified decline and the way up — is already anchored by the Hutchings–Myers (1994) sentence shipped in v6 at certified scope. A hysteresis conjecture would add interpretation the paper's discipline deliberately avoids, and a conjecture no claim needs is decorative by the programme's own bar.

**4.2 General max-plus duality theorem (ws) — rejection correct, recorded rationale wrong.** See §3. The external text's verdict sentence ("right to reject unless you can show a genuinely new case, condition, or proof delta that P1 does not cover") is directionally right but mis-locates the owner: P1 covers nothing here because P1 has no max-plus content. The corrected test — does a general theorem change any shipped claim, method, or result, and does a owner for it exist? — answers no on both counts. The external text's own framework, fed the corrected premise, reaches the same verdict.

**4.3 Ecological viability-kernel section (ARV) — rejection correct, and the permitted alternative is already shipped.** P1 owns the family's viability-theory anchoring; a full section in ARV would duplicate it under a different label (the one-owner rule exists precisely for this). The external text's carve-out — "a brief citation or related-work sentence is fine; a whole section is not" — is exactly what round 26 executed: one sentence (Hutchings and Myers, 1994) anchoring the certified collapse-recovery asymmetry, nothing more. There is nothing further to reopen.

**4.4 "Insight density is already high" — accurate.** All eight cited new-theory items verified in the shipped editions (P4 above). The derived prescription — what remains merited is anchoring and framing, not more theorems — is what round 26 shipped: five standard-result or field anchors (Chvátal, Helly, Milanese et al., Baccelli et al., Hutchings–Myers), three navigational tables, two asserted figures, two acronym expansions.

**4.5 The bottom-line condition — not violated, and now checkable.** The declines forbid nothing outside the cycle's content bar: minimax's conjecture apparatus is live, ARV's and ebc's Delimitations sections are live, and the ws max-plus extension exists in its honest form as a citation. The external text's condition for the call being wrong is therefore not met.

## 5. Where the external text is imprecise

1. Its item-2 premise (P1's attributed Theorem 1 on max-plus ground) is false — inherited from review II's wording, which this audit corrects.
2. Its item-1 summary ("only certify comparisons") understates the record: the locked files certify exact temporal structure and exact threshold relations, not merely pairwise comparisons. The conclusion stands because what a hysteresis model needs — estimation, transition rules, validation — is absent either way.
3. Its item-3 phrase "viability-application literature" should read viability-theory anchoring; the salami-slicing concern it raises is real and is codified in the programme as the one-owner rule.
4. Its frame "the AI is rejecting" treats the declines as one agent's taste; they are rule-derived (data-provenance discipline, one-owner rule, merit bar, proof bar) and were re-derived here from the record, not defended from authority.

## 6. Record corrections executed

- Review II gains a post-hoc verification appendix correcting §3.3's max-plus rationale (append-only; the shipped papers are untouched — no decline ever entered any paper, so there is nothing to retract from them).
- This document is the audit record for the correction. No edition bumps, no verifier changes, no build gates triggered: the papers' content is unaffected by every finding above.

## 7. Answer to "Is the AI right?"

On its own terms, and after premise verification: **yes on all three verdicts, with one material correction it could not have caught** — its second verdict reasons from a false premise (P1's non-existent max-plus theorem), and the rejection stands on grounds that survive verification, not on the recorded one. Its insight-density reading is accurate against the shipped editions, its bottom-line test is the right test, and the shipped record already satisfies it: nothing is forbidden from the future-work channels, and one of the three ideas (the max-plus extension) already exists in precisely the form the external text recommends — a citation. No addition is reopened; no paper changes.

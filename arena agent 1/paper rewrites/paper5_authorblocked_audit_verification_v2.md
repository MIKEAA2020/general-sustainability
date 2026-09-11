# Joint verification of the three author-blocked audits (DeepSeek + Qwen + methods-framing) — v2

This revision incorporates the third audit (R, methods-framing-oriented; pasted
2026-09-11). v1's §§1–2 (DeepSeek/Qwen per-item verdicts, defects D1–D10) stand
unchanged and are carried by reference
(`paper5_authorblocked_audit_verification_v1.md`); what follows is: the third
audit's verification (§7), REVISED three-way joint adjudications superseding
v1 §3 (J3-), a REVISED decision sheet superseding v1 §4, new defects D11–D17,
and a v1→v2 changelog. Target is unchanged (v29 + repo evidence).

## 7. Third audit (R) — item verdicts

Meta-note: R reasons from the root-cause report, not v29 (the practical note
proposes building v29, which is already built and pushed). Same staleness class
as v1's shared blind spots. R's repo numbers and code facts are exact throughout.

### 7.1 A3 full vector in Table 3 — CONFIRMED (strongest A3 advice of the three)

- The 11-value list (r, K, q, η, Emax, Δref, δ0, τm, Zref, δ, k) is code-exact
  AND correctly filed: Δref present (DeepSeek omitted it), δ0/τm in the main
  list (DeepSeek misfiled them to supplement). R fixes DeepSeek's filing errors.
- The interiority one-liner (Φ(0) = δ ⇒ s* = 0, slope exactly 0.5) is
  mathematically exact — verified analytically (strict monotonicity ⇒ unique
  s* = 0) and numerically (Φ(0) = δ bitwise, slope 0.5, floor non-binding).
  Adopted. Completion: it covers the Φ-side precondition only; pair it with the
  Π-side half-line (E* = 2.09 ∈ (0, 30)).
- Derived-quantities policy (supplement-or-print, cheap) is sound; staleness
  note: gains are already printed in v29 §2.1 (A1) — only the fixed point is
  still unlisted. "Scan construction stays archived" is likewise overtaken
  (already in Table 3). Neither affects the advice.
- "Trust the record → check the record" is adopted as the A3 rationale: it is
  the disclosure-side restatement of v1's dangling-pointer finding (Table 3's
  "computational record (this appendix)" resolves nowhere). Frame-independent.

### 7.2 A5 lead with the decomposition — PARTIAL (most actionable A5; one defect)

- Numbers exact (g = 5, η = 0.914 block ✓). The §3.3 restructure (windows
  paragraph + decomposition paragraph + supplement pointer; rwin/tau0 tables to
  the supplement) is concrete, repo-grounded (transcription work, no new
  science), and the most actionable A5 proposal across all three audits. Adopted.
- "Conflate plant and operator" is manuscript-native (§4.1: "plant--operator
  confound"), and the restructure would give §4.1's confound-claim its evidence
  base — currently asserted alongside, the decomposition would SHOW mechanism
  separation. Genuine value-add. Precision required (strengthening): the tau0
  decomposition separates mechanisms WITHIN one operator (cohort/biological vs
  institutional-delay), while §4.1's confound is about comparing ACROSS
  operators+plants. R blurs this ("precisely why the operator discipline
  matters" is true at slogan level); keep the two levels crisp or the methods
  paper commits a category slip in the act of preaching separation.
- Defect: "claim-vs-claim standoff between two unreproduced objects" is doubly
  off — the reconstruction is nominal WITH materials (code + five CSVs in repo;
  "will be deposited"), not unreproduced, and the manuscript already refuses the
  standoff ("consistency check, not validation"; "uninformative rather than a
  non-reproduction"). The elevation is real but smaller than pitched:
  quarantined-consistency-check → method-demonstrating decomposition. Tier note:
  the move is rhetorical; decomposition numbers stay provisional (archive-derived).
- Internal collision with R-A10 (§3.3 claimed by both; resolved in J3-A10).

### 7.3 A6 rebuild-or-reframe-as-illustrative — PARTIAL (best remedy reasoning; three completions)

- The graded fork with an explicit default ((b) reframe unless scripts exist) is
  the most decision-ready A6 advice of the three. "Illustrative application" is
  well calibrated: keeps the screen in Results as a worked example — weaker than
  the current restricted result, less destructive than Qwen's preliminary-demote.
- "Periodicity is not evidence" in quotes is a paraphrase, not verbatim (actual
  v29 L1235: "any claim that periodicity itself diagnoses an institutional
  feedback is unsupported by this cohort"). Meaning preserved; drop the quotes.
- "Report the null at provisional status" would be a STATUS CHANGE: Box-1
  currently reads "BH-adjusted selected-cohort consistency check," and
  "provisional" is the archive tier's word. Adopt carefully: "illustrative" +
  the explicit non-archival sentence; reserve "provisional" for archive-derived
  values to avoid tier confusion.
- "State the five gaps explicitly in the main text": the list is accurate
  (cohort definition, eligibility table, detrending rule, AR(1) calibration, MC
  code — §2.4's "stated rule" is itself unstated, AR(1) calibration unstated).
  Placement completion: back-matter disclosure exists (Data availability lists
  four of five); the adoption is FIRST-USE restatement (§2.4 + §3.5 status line).
- Russell-shift is text-grounded (§4.2, McManus et al. 2016) but restructures
  §4.2 (screen-first → precedent-first): dependency flagged, not made.
- Rebuild grades unseparated: exact-recovery (needs scripts/notes) vs
  re-derivation (needs criterion + public v4.66 + new code). "Only worth it if
  scripts exist" is too strong for re-derivation; completed in §4R.
- Shared blind spot repeated: no title/abstract consequences (screen in title,
  null in abstract — reframe requires retitle + rewrite). All three audits now
  share this miss; v1's completion stands.

### 7.4 A10 methods-forward restructure — PARTIAL (most concrete; internally inconsistent)

- Only audit to map real section numbers; "§4.1 is the methodological finding"
  is text-verbatim (§4.1: "The operator-spectra results of Section 3.4 are the
  paper's core methodological finding").
- INTERNAL CONTRADICTION: R-A5 keeps §3.3 as archive-windows + decomposition
  while R-A10 makes §3.3 operator spectra; the archived regions are homeless
  under A10's map. Resolution (J3-A10): no renumbering — spectra already lead at
  §3.4; adopt compression/demotion logic only.
- Retitle advocated ("appropriate") but not drafted, and retitling is itself
  undecided — the restructure is conditional on a decision it doesn't make.
  Stated as conditional in §4R (no title drafted here either: author voice).
- Appendix B unaddressed (gap vs Qwen) — v1's keep-verdict carries.
- "§4.2–4.4 compress" is compatible with A6(b) (cod already a "descriptive
  partition," §4.3); mild tension: invoking "falsification discipline" while
  compressing §4.4 (the five-condition standard). Note, don't block.

### 7.5 A11 sentence + placement — PARTIAL (best sentence; wrong "add"/"appendix" premises)

- The drafted sentence ("not archived; illustrative application; no
  confirmatory weight") is the best of the three audits: precise, status-setting,
  weight-setting. Adopted.
- "Add the F31 clause" → exists (§4.7(iv)). "Not just the appendix" → false
  premise (§4.7 is main-text Discussion). Salvage, adopted: FIRST-USE restatement
  (§2.4/§3.5) as an addition to (iv).
- Dependency unflagged: "no confirmatory weight" conflicts with §4.2's "value
  lies in what it refutes" — adopting the sentence requires the §4.2 revision
  R-A6 implies (Russell takes the load). The audit is internally consistent
  across A6(b)+A11; the dependency must be made explicit at build time.
- "If the screen is dropped, moot" ✓.

### 7.6 A8/A9 concur — CONFIRMED. Aligns with v1's completion (keep/leave with reasons).

### 7.7 Synthesis — CONFIRMED. Audit-trail inventory accurate (four code sites,
re-execution, bracket bug, decomposition); "disclosure policy, not new method"
converges with DeepSeek's meta-comment and v1's frame. Adopted as the v2 frame.

### 7.8 Practical note — MOOT (overtaken). v29 is built and pushed WITH every
listed fix (A1, A4, A7, I3, F27b, A2-number, a(E) guard, Supp v7 — all asserted
in the build). The independence claim ("none depend on A3/A5/A6/A10/AR(1)")
verifies TRUE and remains the sequencing rule: today's decisions target v30.

## 3R. Revised joint adjudications (three-way; supersede v1 §3)

- **J3-A3 (full Qwen+R vs split DeepSeek).** 2–1 for full main-text disclosure.
  R's list fixes DeepSeek's filing; R's interiority line + "check the record"
  rationale adopted. Decision: print R's 11 values + fixed point in Table 3
  (gains already printed); solver/scan archived; Φ+Π interiority one-liner in
  §2.1/§3.4; dangling pointer fixed. DeepSeek's split survives only as tidiness
  (numerical settings with their objects), not as a disclosure cut.
- **J3-A5 (keep DeepSeek+R vs demote Qwen).** 2–1 keep. Adopt R's §3.3
  restructure (concrete superset of DeepSeek's cite) + supplement rwin/tau0
  tables; Qwen's band-concern logged open (A6-gated). Corrections carried:
  provisional-vs-nominal (not "two unreproduced"); within-vs-cross-operator
  crispness; §4.1-confound evidence link (new value-add of the restructure).
- **J3-A6 (paragraph vs ultimatum vs illustrative).** Three statuses on offer:
  current restricted-result / R illustrative-application / Qwen
  preliminary-demote. RECOMMEND R's middle as the reframe option (keeps Results
  membership as worked example; Russell takes the inferential load; §4.2
  revised) vs graded rebuild (exact vs re-derived; Qwen's deposit spec for
  contents). Title/abstract/§4.2 consequences attached (all three missed).
  "On request" stays rejected.
- **J3-A10 (generic vs carve vs restructure).** Adopt R's compression/
  demonstration logic WITHOUT renumbering (resolves R's §3.3 collision; spectra
  already §3.4 — "lead with spectra" is achieved by compressing §§3.5–3.8, not by
  renumbering). App B keep (R silent; v1 reasons stand). Split rejected (v1
  stands; R implicitly concurs — one paper). Retitle: open decision with
  direction noted; restructure conditional on it (no churn under current frame).
- **J3-A11 (fork vs clause vs sentence).** Adopt R's sentence at first use
  (§2.4 + §3.5 status line) + keep §4.7(iv) + Qwen/5.3 sensitivity gated on A6;
  DeepSeek's fork collapses to R's (clause now, checks iff A6). §4.2 dependency
  flagged. Qwen's drafted clause stays rejected (v1 D9).
- **J3-A8/A9.** Settled keep/leave, 3-way agreement.

## 4R. Revised author decision sheet (supersedes v1 §4)

- **A3.** Print R's 11-value vector + fixed point (89.55188, δ, 2.08962) in
  Table 3; add Φ(0) = δ ⇒ s* = 0 / slope-0.5 line + E*-interiority half-line;
  archive code/seeds/solver config; fix the dangling "computational record"
  pointer. Grounds: near-unit-margin auditability + check-the-record.
- **A5.** Restructure §3.3 (windows para + decomposition para + supplement
  pointer); new supplement tables (rwin/tau0 windows + institutional-only slices
  + crossings 12→8); corrected two-level reading (within-operator mechanism
  separation evidencing §4.1's cross-operator confound-claim). Log Qwen's
  band-concern open (post-A6 re-prespecification needs a screen re-run).
- **A6.** Fork: (i) graded rebuild — exact (scripts/notes) or re-derived
  (criterion + public v4.66 + new code), contents per Qwen's deposit spec,
  Zenodo/repo; or (ii) R-reframe (RECOMMENDED if no scripts): "illustrative
  application" status, explicit five-gap non-archival sentence at first use
  (R's A11 sentence), Russell takes the §4.2 load, WITH retitle + abstract
  rewrite + Box-1 restatement. §3.8 + theory untouched either way.
- **A10.** No renumber; compress §§3.5–3.8 as demonstrations under the spectra
  lead; keep Appendix B; no split; notation table optional; retitle decided
  explicitly (restructure conditional on it).
- **A11.** Insert R's sentence at §2.4 + §3.5 first use; keep §4.7(iv); §4.2
  revision as dependency; 5.3 sensitivity list (ARMA/trend-stationary/
  block-bootstrap/regime-surrogate/detrending) gated on A6 rebuild.
- **A8/A9.** Keep/leave (§1.4 reasons). Settled.

## 5R. Defects (D1–D10 carried from v1; D11–D17 new)

- D11 R-A3 staleness: gains + scan-construction already in v29 (harmless; advice
  placement-agnostic). Π-side interiority missing from the one-liner → paired.
- D12 R-A5: "two unreproduced objects" → provisional-vs-nominal (S8 tiers);
  "claim-vs-claim standoff" → text already refuses it (consistency check).
- D13 R-A5/A10: §3.3 double-claimed (archive vs spectra) → resolved: no
  renumber; §3.3 restructured per A5, §3.4 stays spectra.
- D14 R-A6: "periodicity is not evidence" → paraphrase (L1235 actual). "Null at
  provisional status" → status change; use "illustrative" (tier hygiene).
  Rebuild ungraded → exact vs re-derived. Title/abstract consequences missing →
  attached. "State in main text" → first-use placement (back matter has it).
- D15 R-A11: "add F31" → exists (§4.7(iv)); "not just the appendix" → §4.7 is
  main text; salvage first-use placement + adopt the sentence; §4.2 dependency
  flagged.
- D16 R-practical-note: moot (v29 built/pushed with all fixes); independence
  claim verified TRUE → v30 sequencing rule.
- D17 R-A10: retitle advocated-undrafted + undecided → stated conditional; App B
  gap → v1 keep-verdict carries; §4.4-compress vs falsification-invocation
  tension noted.
- Shared-blind-spot ledger (now 3-audit): pre-existing disclosure ×8 (all
  missed); pre-existing F31 (all missed/misplaced); title consequence (all
  missed); A6-gating of A5-rebanding/A11-checks (all missed); dangling pointer
  (Qwen sensed, R's rationale restates, landed here); v29-existence (R missed).
  All three audits reasoned from the report, not the text — joint verification
  against v29 remains the value-add.

## 8. v1→v2 changelog

- Added: §7 (R verification), J3- joints (revised), §4R sheet (revised), D11–D17.
- Changed recommendations: A3 → R's list + interiority line (was: split-leaning
  full disclosure); A5 → R's §3.3 restructure + supplement tables (was: cite);
  A6 reframe → R's "illustrative application" recommended over Qwen's demote
  (was: fork without recommendation); A10 → no-renumber compression + retitle
  conditional (was: per-option only); A11 → R's sentence at first use (was:
  keep-iv + direction-fixed augmentation — the augmentation is superseded by
  R's sentence, which says it better).
- Unchanged: v1 §§1–2 verdicts, D1–D10, A8/A9, "on request" rejection,
  Qwen-clause rejection, split rejection, App-B keep.
- No manuscript edits (evaluation only). Next build v30 on author decisions.

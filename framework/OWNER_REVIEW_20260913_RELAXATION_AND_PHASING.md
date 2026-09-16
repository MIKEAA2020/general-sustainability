# Owner review 2026-09-13 — remaining audit points, supplement restructuring, and the frozen-elements relaxation test

Owner questions answered in order. Evidence: v25_restructured (head), the V12 joint
evaluation (`JOINT_EVALUATION_IMPACT_AUDITS_V12.md`), the merged plan (venue V12),
the Phase K archive (`phase_c/results/o6_cod_band_calibration_20260913.json`), and
the two audit texts (`uploads/framework impact.txt`).

---

## 1. Q1 — remaining points from either audit worth implementing

All audit claims are accounted for: every claim in both impact audits maps to a
CLOSED item, a recorded DUPLICATE, or an open item O18–O39 — nothing was dropped
without a record. The worth-implementing list, merit-ranked:

| Rank | ID | Item | Why it is worth implementing | Phase |
|---|---|---|---|---|
| 1 | O18 | Standalone two-page specification + checklist | Both audits' #1 practical item; turns the paper's "the standard is the deliverable" claim into an actual deliverable | L |
| 2 | O20 | IC instruments on the existing archive (IC at h=5; multi-horizon penalised criterion; IC-ranking + rule-gates hybrid) | Both audits' #1 technical item; the archive already carries per-replicate h=1 AND h=5 RMSEs — zero new simulation | M |
| 3 | O24 | Negative-certificate scoping (N0–N3 claim-strength taxonomy, expiry/invalidation, combining rules) | Formalises exactly what a non-retention claim can support; root-cause fix for over-interpretation of M3/M4 and gate evidence | L |
| 4 | O29 | Epistemic-consequence sentence + decision-based margin + **reported-verdict band-invariance statement** (extension, §4 below) | Honesty completion tied to the executed calibration | L |
| 5 | O32 | Formal identification decomposition P(retain) = P(rank 1) × P(baseline|rank 1) × P(gates|…) | Root-cause explanation of the frontier finding ("power is identification-limited at every width") | M |
| 6 | O30 | Exact counts + binomial (Wilson) intervals for every published rate | Cheap, removes the "point estimates without uncertainty" objection (GPT 2.2) | M |
| 7 | O27 | Two-axis reading guide + M2m clarifying sentence | Resolves the audits' central conceptual tension (prediction license vs structural decline) inside the frozen vocabulary | L |
| 8 | O26 | Minimal reproduction package (one script, archived data → rule → gates; 20 D1/D5 replicates, <1 hour) | Addresses "no software exists" directly | N |
| 9 | O28 | Reference gate implementation + YAML negative-certificate schema | Pairs with O24; the machine-readable form of the standard | N |
| 10 | O23 | Forecast-comparison / multiple-testing literature paragraph + comparison table | Qwen 3.6 is right: the MCS gets one sentence; the retention rule IS a sequential multiple-testing procedure and should be positioned as one | O |
| 11 | O22 / O25 / O33 / O37 / O38 / O39 | Third-domain prospective registration; decision-context paragraphs; tiered adoption guidance; "domain-free" moderation; abstract rule-version parenthetical; three-quantity terminology | Small, honesty-serving, no frozen-element contact — one text pass | L |
| 12 | NEW-18 moves | DM mechanics → Supplement S1 (§4/§5) | GPT 8: DM rows consume space without strengthening; verdicts already "do not rest on DM statistics" | L (newly approved, §2) |

**Not worth implementing (with reasons):** O21/O31 (new DGPs — heavy compute,
owner-gated, adds evidence the frontier already bounds); O34 (third-party
application — event-triggered, post-release); O35 (title tweak — the abstract
already says "proposes"; the question-form title is the O11 problem-first lead;
a change buys nothing); O19 retrospective part (forbidden by reported-verdicts
immutability — the prospective part is proposed in §4.3); O4/O5/O16-full (as
registered; O16's merited subset is now unblocked, §2).

---

## 2. Q2 — restructuring to supplementary, approved when merited (NEW-18)

Recorded as **NEW-18** (owner decision, 2026-09-13). Unblocks the
supplement-movement remainder of NEW-17 and O16.

**Merited moves (execute in Phase L):**

1. **DM mechanics → S1.** The §4 and §5 "uncertainty layer" paragraphs carry the
   DM p_perc formula, the 15-of-17 CI bookkeeping, and the three example rows
   (§5). GPT 8 is right that they consume space without strengthening: the
   verdicts already state they do not rest on DM statistics. Move the mechanics
   to S1 (new S1.4); the main text keeps the descriptive label, the
   "verdicts do not rest on DM statistics" sentence, and the one decision-relevant
   statement per domain — §4: the load-bearing gate decision (M2m vs M1, 4.33%
   against the 5% band) sits within numerical tolerance of the environment
   sensitivity measured on cod (3.8% of 445.5 kt); §5: the one-line label.
2. **No further §6.5 move is merited** — the uncertainty-robust variants are
   already summarised in the main text with full detail in S1.

**Not merited (kept in the main text):**

- The §6.5 IC co-primary block — placed deliberately in Phase F2 (O8, owner
  approved); it carries the decision-relevant edge case (M2m divergence) and the
  full instrument disclosure, which is an honesty asset.
- The §3 reporting template (Table 2b) — a load-bearing pillar; O18's standalone
  specification will reference it, not replace it.
- The §7 cross-application table and the §8 calibration frontier — core and
  root-cause disclosures respectively.
- **O16's full target (10.7k → 8–10k words) is NOT merited**: reaching it would
  cut decision-relevant evidence for density's sake. The merited subset above is
  executed; the remainder stays recorded as not-merited rather than silently
  dropped.

**Still owner-gated:** O36 (abstract compression). The approval above covers
main-text → supplement moves, not the abstract. Concrete proposal if the owner
wants it: compress the abstract to a findings-first form at ~60% of current
length, keeping every finding number (the moved method detail already exists in
§2/§3). One owner word unblocks it.

---

## 3. Q3 — do any pre-registrations or spec rules merit relaxing?

Test applied: **honesty** (is the frozen element currently making the paper say
something false or unfounded?) and **root cause** (does freezing it leave the
audit's underlying defect unaddressed?). Reviewed element by element, including
everything the audits ask that would change a reported verdict, a frozen label,
or the executed band calibration.

### 3.1 The 5% band for reported verdicts — NO relaxation, with an honesty completion

The audits' strongest claim here is Qwen 2e: "the reported verdicts rest on a
band whose adequacy has not been verified for the objects being scored."
Verified against the paper, **the premise is factually overstated** — the paper
discloses at three places that the band is not load-bearing for the reported
verdicts:

- §1: "Verdicts are unchanged under both versions" (band vs pre-registered no-band).
- §4 (Edwards): "Within the unified rule the band changes no outcome … Without
  the band it would pass H1 but still be declined on class grounds, so the empty
  set holds either way." (M2m's 4.33% margin vs M1; class grounds withhold at
  any band.)
- §5 (cod): "No structural module approaches the tie band on either specification
  at either horizon. The verdict is decided by ranking alone; the gates never
  engage on cod."

So the band is load-bearing only for the **simulation operating
characteristics** — and there the calibration the audits demand was executed
(Phase K, cod): no band attains power ≥ 0.80 ∧ specificity ≥ 0.90; the frontier
runs 0.4437/0.760 at 0% → 0.3731/0.9725 at 5% → 0.3119/1.000 at 15%; §8 reports
it, so GPT 5's "silent retention" charge is contradicted by the paper itself.
Edwards remains the prospective DRAFT (one owner decision pending, §3.8).

**Honesty completion (added to O29):** state the reported-verdict
band-invariance explicitly, tied to the frontier — the calibration governs the
*interpretation* of future verdicts, while the reported verdicts are
band-invariant by the archived margins. Also adopt GPT 5's substantive point
without renaming the frozen component: the band is a practical-equivalence
margin that may be set on either basis — simulation-calibrated (the executed
cod frontier) or decision-based (declared operational irrelevance) — with the
basis stated; the decision-based margin is recorded as the admissible
alternative. The term "tie band" is not renamed (frozen component name in the
algorithm box and archives); the umbrella sentence carries "practical-equivalence
margin".

### 3.2 Output vocabulary — NO relaxation (NEW-11 stands)

Renaming the pre-registered outputs retroactively would fork the archives, the
companion tables, and the reported verdicts' names — a label change with zero
epistemic content. The root cause of the audit's concern (readers conflating the
predictive result with the structural interpretation) is addressed inside the
frozen vocabulary by the two-axis reading guide (O27) and the three-quantity
terminology sentence (O39).

### 3.3 Ladder and comparators (M3/M4 removal) — NO relaxation (NEW-12 stands)

"Never truth" is already disclosed (Qwen 2b verified the disclosure). The root
cause of the over-interpretation risk is scoped by O24's claim-strength
taxonomy, not by deleting rungs. O4 (M3/M4-as-truth cells) remains owner-excluded.

### 3.4 Class-grounds rule — NO retroactive relaxation; prospective criterion proposed (O19)

The reported "declined on class grounds" verdict (M2m) was decided under the
pre-registered declared-judgement rule and is immutable. Honesty is intact: the
decline is declared with reasons (collapses to AR(1) under constant fluxes).
The reproducibility weakness Qwen 3.2 identifies is real for future
applications — the root-cause fix is a **prospective criterion registered now**:

1. the declared judgement with stated reasons stays (frozen for reported verdicts);
2. a quantitative screen is registered prospectively: a module is
   class-grounds-declinable when its predictions are affine-equivalent to a
   simpler ladder member under the declared conditions (the M2m→AR(1) collapse),
   with the equivalence convention stated in advance;
3. dual reporting (retention outcome with and without the decline), exactly as
   the Edwards DRAFT sheet already specifies for its E2m cell;
4. applies only to future applications — never re-opens a reported verdict.

This mirrors the AD4 machinery (prospective band calibration) and is the same
discipline applied to the class-grounds gate. Owner approval moves it from O19
into Phase L text.

### 3.5 "Power" terminology — NO relaxation (NEW-16 stands)

"Power" is explicitly defined in §6.1 (true-class retention rate against the
adequacy thresholds); there is no misrepresentation to fix, and a rename would
churn frozen language across the paper and archives. O39's three-quantity
sentence (model-class identification / predictive selection / mechanism
attribution) disambiguates instead.

### 3.6 Everything else the audits touch — no relaxation

- DGP labels, "Row measures", mechanism-misattribution framing — settled in
  Phase B (AD2a); no new audit ask touches them.
- Pinned-seed numbers — no audit ask; precedence rule stands.
- Reported verdicts — no audit point re-decides one directly; the two that
  would (band replacement, class-grounds threshold) are redirected to the
  prospective channels above, which is the honest disposition: the verdicts
  stand on their archived margins, not on the frozen elements the audits attack.
- Executed band calibration — no surviving flaw claim: GPT 5's "silent
  retention" is contradicted by §8's frontier disclosure; the Phase K validation
  pass reproduced all 10 published cells at 5%.

### 3.7 Verdict on Q3

**No pre-registration or spec rule merits relaxing.** In every case the honesty
criterion is satisfied by disclosure already in the paper (verified claim by
claim), and the root-cause criterion is satisfied by the prospective channels —
the executed cod calibration, the Edwards DRAFT, the O27 reading guide, the O24
claim-strength taxonomy, and now the two completions above. Relaxing a frozen
element would change reported verdicts or archived labels *without* adding
honesty — the opposite of what the criteria demand. Recorded as **NEW-19**.

### 3.8 One pending owner decision (not a relaxation)

The Edwards calibration DRAFT (`specifications/SPECIFICATION_prospective_band_edwards_DRAFT.md`)
is blocked only by the owner's choice of class-grounds convention for the E2m
(M2m) cell: **with-decline** (mirror of the frozen protocol; proposed) or
**without-decline** (E2m treated as an in-class truth; power reported both ways
either way). This is an approval, not a relaxation of any frozen rule. On the
owner's word, the Edwards calibration runs with the Phase C machinery.

---

## 4. Records and next step

- **NEW-18** (owner, 2026-09-13): supplement restructuring approved when
  merited → NEW-17/O16 merited subset unblocked (DM mechanics → S1); full 8–10k
  compression not merited; O36 remains owner-gated.
- **NEW-19** (this review): relaxation test executed element-by-element; no
  frozen element relaxed; O29 extended with the reported-verdict
  band-invariance statement and the practical-equivalence-margin umbrella;
  O19 gained a concrete prospective criterion (owner approval pending).
- Contradiction count unchanged at 43 adjudicated, 0 outstanding; NEW-18/NEW-19
  are owner decisions and review records, not new contradictions.

**Phase L is ready to execute on the owner's go**, now with the merited
supplement moves folded in: O18, O22, O24, O25, O27, O29 (+ band-invariance),
O33, O37, O38, O39, plus the S1 DM-mechanics move — one pass, idempotent apply
script, scanner battery, changelog, push. Phase M (O20/O30/O32), Phase N
(O26/O28), and Phase O (O23) follow unchanged.

---

## 5. Sweep addendum, 2026-09-13 (full-read sweep of both impact audits)

After Phase L, every claim in both audits was read end-to-end (not grep-sampled)
and cross-checked against V12 and the merged plan. Coverage: all audit items map
onto O18–O39, CV4, or explicitly declined V12 points; the two transcripts propose
nothing beyond the 22 registered items. Three records:

**NEW-20 — N-level semantic gap.** The audits define the certificate levels
semantically (N0 descriptive / N1 inconclusive — low or uncertain sensitivity /
N2 informative — demonstrated sensitivity / N3 operationally informative) and
enumerate expiry triggers; Phase L's §2.2/S2 implement them cumulatively by
evidence package. Both readings are consistent with the four-tier numbering, but
the audit's *language* (descriptive/inconclusive/informative) and the expiry
enumeration are recorded here as an optional refinement to be folded if the
certificate is ever formalised (NEW-21 dependent). No freeze implicated.

**NEW-21 — redistributive structure confirmation.** The audits' recommended
methods-paper structure redistributes existing content among main text, S1, and
S2 — it is exactly the long-section redistribution Phase J declined (§3.5), and
would renumber sections and reopen validated anchors. Phase J's adjudication:
changes confined to existing sections; new material appended as new supplement
sections only. S1.4 and S2 were built under that rule, and it stands. The
audits' content asks (specification, checklist, tiers) were all delivered within
the constraint; only the renumbering itself is declined.

**NEW-22 — extended instrument-comparison grid.** The audit's wider IC-family
comparison (4+ candidate instruments, class-ranks-first probabilities,
conditional gate-pass rates, regret, false-attribution rate) generalises the
three-instrument Phase M grid now executed (O20). Recorded as a potential
follow-up after the Phase M results are in front of the owner; no new
simulation — the grid is archive-only until the owner expands scope.

---

## 6. Review close, 2026-09-16 (NEW-20 and NEW-22 — this file is complete)

The two items left open in §5 are settled as **bequeathals**, not further text:
the framework's review corpus is now complete; both are optional future
refinements with a documented home, and neither is a defect in this version.

**NEW-20 — certificate-level semantics (descriptive / inconclusive / informative /
operationally-informative) and the trigger list.** S3's verdict record already
carries `certificate_level` and `expiry` as fields, so the semantic reading is
usable in S3 form today. Folding those exact words into §2.2's cumulative
definitions is a *prose refinement* — it would strengthen the paper but does not
change any level assignment and would re-open validated §2.2 anchors.
**Bequeathed to the first submission/revision pass of the certificate
formalisation (NEW-21 dependent).** Closed as filed-with-home.

**NEW-22 — extended instrument-comparison grid.** S1.5.1 already executes the
three-instrument grid on the existing archive and reaches a stable verdict (no
dominance; the comparator gate is the price of specificity). A wider candidate
set would need either a new registered campaign or new DGPs — both outside the
newest-only / archive-only scope of this whole effort, and both bequeathed to a
future campaign. **Closed as bequeathed to the next registered simulation
campaign.**

With NEW-18/19 executed (Phase L), NEW-20/22 filed, and O19/E2m decided in-sheet
(2026-09-16), this review has **no remaining actionable item**. Any further
question belongs to the submission/revision cycle, not this document.

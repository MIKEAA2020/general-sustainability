# Which v3? — v3-A vs v3-B vs v3-C

**Date:** 10 Sep 2026 · **Rev 5** (surviving upgrades landed in E3/E4) · rev 4 gate 4 FAILS → no v3 · rev 3 resolved gate 2 · rev 2 closed the gates raised in `deepseek e3 and e4.txt` · **Status:** decision memo, exploratory. Companion to `GENERALIZATION_PROTOCOL.md`.
**Question asked:** the external review ("generalizing2") presents three candidate v3s and asks which to pursue.

---

## Verdict — the gates were run, and **gate 4 fails. Write no v3.**

**Rev 4 supersedes the rev 1–3 recommendation.** The structural argument for v3-C was right and still stands:
Barton Springs is a real third pool, the R04 case is clean, and gate 2 resolved in the v3's favour. But the
**feasibility gate was always the binding constraint**, and it has now been run against actual data rather than
assumed. It fails on four independent grounds. Under the rule this memo pre-committed to in rev 2 —
*"if the gate fails, do not write a v3"* — the outcome is:

> **Do not promote v3.** The record's original core conclusion stands, now for a *demonstrated* reason rather
> than a default one. Barton Springs stays naive and is left available for a properly powered future test.

| # | gate | outcome |
|---|---|---|
| 1 | **R04 case** — no judgment transferred, only a scalar relation, every parameter pool-local (§1.1) | **clears** |
| 2 | **Declared-family equivalence** (§5 item 2) | **clears** — B unconditionally; C under the E4-comparable subfamily restriction |
| 3 | **Decision rules** for H1/H2 failure, sign failure, knife-edge (§5 item 5) | **clears** — machine-encoded |
| 4 | **Springflow map-form pre-check** (§6.3) | **FAILS — four grounds** |
| 5 | **Multiplicity enumerated** — 120 cells, α = 0.00083 (§5 item 8) | clears |

**Gate 4, as run** (`src/gate4_springflow_precheck.py` → `results/gate4_springflow_precheck.json`):

- **G1 — the "long record" premise was false.** Rev 1 introduced the springflow specification *specifically* to
  escape Lovelady's short record. Daily discharge at USGS **08155500 begins 1978-03-01** — that is the entire
  period of record per the site catalog (`dv|00060|00003|1978-03-01`), giving **49 usable annual observations**
  under the ≥240-day rule. Against J-17's 90 and J-27's 81, the mitigation **does not mitigate**. This was my
  error, carried through three revisions, and it was load-bearing.
- **G4 — H1 is degenerate, not merely uncertain.** Fitting the E4 map's autoregressive core to annual
  springflow gives **â = 0.178, 95% CI [−0.109, 0.465] — containing zero** (n = 48 transitions). H1 (`0 < a < 1`)
  is *nominally* satisfied by the point estimate, and a careless reading would tick the box. But `a ≈ 0` means
  annual springflow is close to **white**, so `H*₀ = (α + βF)/(1 − a)` collapses to roughly the unconditional
  mean and contraction is effectively instantaneous. The margin would then measure *threshold-vs-mean*, not
  *threshold-vs-attractor* — **the dynamical content the lemma is about is simply absent**. Compare the head
  specifications, where `a` is far from zero (J-17 0.644, Uvalde 0.844). This is the deepest of the four: it
  says the port is not merely underpowered but **structurally inapposite**.
- **G2 — H2 cannot be verified at all.** `γ < 0` is a fitted-sign assumption on a *pumpage* regressor, and no
  machine-retrievable annual BSEACD pumpage series exists — District aggregate production appears only in
  annual-report and HCP PDF tables. Without `P_t`, γ cannot be signed. Per the rev-2 rule, **unverified H2 = scope
  exclusion**.
- **G3 — the decisive episode is outside the record.** The **1950s drought-of-record** is the basis for the
  6.5 cfs DFC and the 5.2 cfs MAG, and it lies **entirely before the gauge**. The v3 could not test the regime
  its own thresholds were derived from.

**Why this is a real result and not just a dead end.** The gate did its job: it was pre-registered in rev 2,
before any Barton Springs data was touched, and it killed the v3 *on the pool's structure* rather than on a
disappointing sign test. Had these checks come after the margin computation, the same facts would have been
available as reasons to discount an unwelcome result. Note also that G4 could only have been found by looking —
no amount of document work would have revealed that springflow is near-white.

**What survives.** v3-A stays declined; the M1-loss mechanism (§6.2) stands as an E3 note; gate 2's finding —
that **E4-negative is family-free even against a strict superset with hysteresis** (§5 item 2) — is a genuine
strengthening of E4's negative leg and is independent of the v3 question. The remainder of this memo is the
rev 1–3 argument, retained because its structural analysis is what made the failure diagnosable.

---

## 1. The third pool the review said did not exist

The **Barton Springs segment** of the Edwards Aquifer (`BSEACD`, Austin) is a distinct segment, separately
regulated by a *different district* than the `EAA`. It has the structural features the three v3s need:

| Feature | Barton Springs segment | Why it matters here |
|---|---|---|
| Index well | **Lovelady monitor well** (USGS site `301237097464801`, `YD-58-50-301`, Travis Co.); first measurement 29 Jul 1949; continuous since 1991 | head-valued index, same construction as J-17/J-27 |
| **Physical/ecological threshold** | **Barton Springs flow** — GMA-10 extreme-drought DFC = **6.5 cfs**; all-conditions DFC = **49.7 cfs** (84-mo avg); 1950s drought-of-record daily low = 10 cfs | **the Comal analog** — this is exactly the ESA-referenced cessation-style limit E4's constructive leg requires |
| ESA-listed species | **Barton Springs salamander** (`Eurycea sosorum`), endangered 1997; **Austin blind salamander** | same legal mechanism as the Comal species constraint |
| Declared policy family | **BSEACD HCP (2018)**: cap pumping ≤ **5.2 cfs** under drought-of-record to hold ≥ **6.5 cfs** springflow | a *bounded, declared curtailment rule* — the `P ∈ [0, K_PHYS]` object E4 studies |
| Institutional thresholds | BSEACD Stage I–IV drought stages, triggered on Lovelady head (e.g. Stage IV at 457.1 ft-msl) **and** springflow | the institutional-half analog, for v3-B |
| Data | Barton Springs flow: USGS `08155500` daily values — **verified live, HTTP 200**; Lovelady: USGS/NGWMN monitor site | retrievable |

### 1.1 The R04 case, stated properly (rev 2)

The previous revision wrote "separately regulated by a different district, so under R04 it is a distinct pool."
That is a **jurisdictional** argument, and R04 does not ask a jurisdictional question — it asks whether a
**judgment is transferred across a failing typed-field map**. Separateness establishes only that Barton Springs
is not a sub-unit of an already-analyzed pool; it does not license the test. The actual R04 argument is:

> **No judgment is transferred.** v3-C does not carry E4's *verdict* from J-17 to Barton Springs. It carries a
> **scalar relation** — `m = K − H*₀`, whose sign implies emptiness by the lemma — and then **re-derives both
> sides of that relation from Barton Springs' own data**. `H*₀` is fitted on the new pool; `K` is read off the
> new pool's own declared threshold. Nothing crosses the map except the *form* of the relation, which is a
> theorem, not a finding.

This is also the **failure condition**, and it is the reason the argument belongs here rather than buried in the
pre-registration sketch: if the v3 ever needs a J-17-estimated quantity to score Barton Springs — a borrowed
coefficient, a borrowed floor, a borrowed domain — it *has* transferred a judgment and **R04 voids it**,
regardless of how good the hydrology looks. The pre-registration must state that **every parameter is
pool-local**.

**Consequence for the review's "ruled out" list.** The review wrote:

> *Ruled out: "The E4 constructive claim generalizes."* Uvalde has no physical-threshold analog.

That is correct **for Uvalde** — and the record's §4.5 stands unchanged. It is **not** true globally. The correct
statement is narrower: *E4's constructive leg is undefined on Uvalde, and its generalization must be tested on a
pool that has a physical threshold.* Such a pool exists. The review generalized a Uvalde-specific fact into a
global impossibility, and that overreach is what produced the "no valid v3" verdict.

---

## 2. The decisive criterion the review missed: power, not existence

The review separates v3-A/B/C by *what each generalizes*. The sharper separation is by **whether the
pre-registered statistic has power** — and on this axis the three options are not close.

The record already established (D1–D3) that a **point-RMSE comparison on this problem is underpowered**: on J-27,
M2 vs persistence gave DM `z = −1.256`, a bootstrap CI **covering zero**, and 38/66 origin wins. Pre-registering a
v3 whose test statistic is a point-RMSE comparison would be re-adopting the exact defect the record's §3.0
condemns. That damages **v3-A** (whose content *is* a retention/RMSE rule) and any v3-B/C stated in RMSE terms.

The **margin** is not a statistical statistic. `m(P,K,F) = K − H*₀` is a computed sign, and the lemma
**0 violations / 15 cases** says emptiness follows *deterministically* from `m > 0`. A v3 stated in margins
therefore has effectively **deterministic power on the sign** — the empirical content is only whether the sign
prediction is right, which fresh pools test cleanly.

**This is the reason v3-C is chosen.** Not because the positive claim is more flattering, but because it is the
only one whose confirmatory test is not a coin flip.

---

## 3. v3-B is not a separate option — it is the other half of v3-C

The review treats B (institutional threshold ⇒ empty kernel) and C (physical threshold with positive gap ⇒
constructive result holds) as two rival v3s. They are the **same quantity**:

```
m = K − H*_0     (margin;  m > 0  ⟺  kernel empty for every non-negative rule)
gap = H*_0 − K   (record §4.1 convention  =  −m)
```

- **K above the zero-pumping drought equilibrium** (`m > 0`) → *institutional* threshold, nothing protects it → **B**
- **K below it** (`m < 0`) → *physical* threshold, reactive rules can hold it → **C**

So "the institutional negative" and "the constructive positive" are the two signs of one relation. **No v3 should
pre-register one sign alone.** State the relation; B's half is then a corollary and arrives free.

**Rev 2 correction — B is testable, not near-definitional.** The previous revision argued that a protective
regulatory threshold is "almost by construction" set above the natural drought equilibrium, so `m > 0` is close
to definitional and B generalizes little. That overstated the case, and the word "almost" was carrying the
weight. Regulators sometimes set institutional thresholds *below* the drought equilibrium — precisely when they
choose a level the system can actually hold. So `m > 0` for institutional thresholds is an **empirical
regularity, not a definition**, and it is falsifiable the moment a pool shows an institutional threshold with
`m < 0`.

The pair should therefore be pre-registered **as one relation with a prediction on each side**, with B scored
rather than assumed:

| threshold type | prediction | falsified by |
|---|---|---|
| institutional (B) | `m > 0` ⇒ kernel empty for every non-negative rule | an institutional `K` with `m < 0`; or `m > 0` with a non-empty kernel |
| physical/ecological (C) | `m < 0` ⇒ some declared-family rule holds `K` | `m < 0` with an empty kernel under the declared family |

C still carries the harder content — `m < 0` for a threshold that does real ecological work is a substantive
claim about where the natural equilibrium sits relative to the line — but B is now a genuine test.

---

## 4. Why v3-A is declined

v3-A is the most interesting *idea* of the three, and the review is right that it is not a generalization of E3
but a **replacement** of E3's verdict. Three independent reasons to decline it as a v3:

1. **It revises a frozen paper, not a scope.** E3's published claim is that persistence and AR(1) are hard to
   beat. v3-A would say that claim is a *function of head AC(1)* and holds only in a sub-range. Whatever the
   merits, that is a **correction to E3**, and the standing discipline is that second-well work may not alter
   E3/E4's conclusions. A v3 generalizes; it does not silently retire the paper it came from.
2. **It is unidentified.** "Retention switches at head AC(1) = X" needs pools *spanning* AC(1) to locate a switch
   point. Two pools (0.644, 0.844) plus one more give at best a sign test at a single chosen X.
3. **Its statistic is the underpowered one** (§2).

**A real mechanism does exist, and it survives the decline** — see §6.2. It was found while *testing* v3-A
rather than dismissing it, and it is stronger than the "note to add to §3.2" that rev 1 filed it as.

Note the discipline trap v3-A sets: you would have to *check* whether a candidate pool's AC(1) lies in the
untested range in order to know whether it is usable — **and the check itself spends the pool.** Only a
*directional* pre-registration ("AC(1) > X ⇒ M2 retained") avoids the trap.

---

## 5. What v3-C must pre-register

Nine requirements. Items **2, 5, 6 and 8** are new in rev 2, and they are the ones that decide whether the
resulting v3 is actually confirmatory or merely looks it.

1. **The relation, both signs:** threshold `K` is holdable by the declared family ⟺ `m = K − H*₀ < 0`, with
   `H*₀ = (α + βF)/(1 − a)`; require **H1** `0 < a < 1` and **H2** `γ < 0` to hold on the new pool, and *report*
   them rather than assuming them.
2. **Declared-family equivalence — RESOLVED (rev 3).** Worked from documents only; no third-pool statistic
   computed. Full detail in `src/gate2_family_equivalence.py` → `results/gate2_family_equivalence.json`.

   **The two families share their functional shape.** Both are *multiplicative, piecewise-constant reductions
   off an authorized baseline, with jumps at declared trigger levels, and both admit ρ = 0* (full cessation —
   BSEACD's post-2004 **Conditional** permits are explicitly curtailable to 100%). Even the cut ladders line up:

   | | E4 `cpm` | BSEACD mandatory stages |
   |---|---|---|
   | cuts | 20 / 30 / 35 / 40 % | **20 / 30 / 40 / 50 %** |
   | triggers | H = 660 / 650 / 640 / 630 ft | Q = **38 / 20 / 14 / 10 cfs**; H_L = **478.4 / 462.7 / 457.1 / 453.4** ft-msl |

   **But BSEACD's family is a strict *superset*, on two counts:**

   - **D1 — two trigger variables.** Stage is set by Barton Springs flow *Q* **and** Lovelady head *H_L*. E4's
     family is a function of a single state variable and simply cannot express these rules.
   - **D2 — hysteresis.** A stage is *entered* if **either** indicator crosses, but *exited* only when **both**
     recover. The rule is therefore **path-dependent**, not a memoryless function of the current state.
   - (D3, definitional: cuts are off *authorized permit volume*, not realized pumpage, so `P_bar` must be
     defined as the authorized baseline or the percentages are not comparable.)

   **The superset finding splits the two halves — and this is the useful result:**

   - **B clears unconditionally.** The margin lemma bounds `H_{t+1} ≤ a·H_t + α + βF` for *any non-negative
     pumping sequence* (H2), then contracts (H1). It never refers to a rule's functional form, so it subsumes
     two-variable **and** path-dependent/hysteretic rules. **E4-negative\* survives even against a strict
     superset** — the family-free property is doing real work here, not just decoration.
   - **C clears only under a restriction.** Construction *is* family-relative, so an unrestricted search could
     succeed using a rule E4 never admitted — which by §1.1's own standard is not a generalization of E4.
     **Required restriction:** define the v3 declared family as the **E4-comparable subfamily** — single state
     variable, memoryless, piecewise-constant multiplicative cuts at BSEACD's *declared* trigger levels
     (20/30/40/50% at Q = 38/20/14/10 cfs, or at H_L = 478.4/462.7/457.1/453.4 ft-msl), plus the flat-ρ members.
     This is a **subset** of what BSEACD actually operates, so a positive result is **conservative** and
     comparable to E4. If the restriction is ever relaxed, the result must be reported as a **BSEACD policy
     finding, not a generalization of E4**.

3. **State it in the object's own threshold variable.** Barton Springs' threshold is in **cfs**, and its record is
   long. The margin lemma is unit-agnostic — it is a property of a linear stock-flow map, not of feet — so the
   v3 can be stated in springflow units directly, **introducing no head↔flow mapping assumption.** Prefer this over
   re-expressing the threshold in Lovelady feet.
4. **Falsification, written first:** the prediction fails if a pool with `m < 0` yields an empty kernel, or a pool
   with `m > 0` yields a non-empty one under the declared family.
5. **Decision rules for every outcome, not just the clean one.** The previous revision said to *report* H1/H2
   rather than assume them, but never said what a failure *means* — leaving no decision rule for half the
   outcome space. Pre-registered, and machine-encoded in `src/v3_gate_checks.py` →
   `results/v3_gate_checks.json`:

   | outcome | ruling |
   |---|---|
   | **H1 fails** (`a ≥ 1`) | **scope exclusion** — `H*₀` undefined, pool is not a valid test object. Report; do not score. |
   | **H2 fails** (`γ ≥ 0`) | **scope exclusion** — the lemma is void. Report; do not score. |
   | H1, H2 hold; sign prediction **wrong** | **falsification** |
   | H1, H2 hold; sign prediction **right** | **corroboration** (one instance) |
   | margin within the knife-edge band (record §4 rule 1) | **indeterminate** — reported, scored as neither |

   Scope exclusion is not a free pass: a v3 whose pools are *all* scope-excluded has no test and must be
   **withdrawn**, not reported as unfalsified.
6. **Restate the margin lemma with its proof** (`GENERALIZATION_PROTOCOL.md` §1), H1 and H2 as explicit
   hypotheses. A v3 may not cite "0 violations / 15 cases" in place of the theorem: the machine check is
   evidence that the implementation matches the lemma, not a substitute for stating it.
7. **Porting parameters frozen up front:** domain/clip bounds, **and the kernel domain `(H_LO, H_HI)`** — the rev-3
   bug shows this one is destructive when wrong (record §5.0).
8. **Multiplicity — enumerated, not gestured at.** "Multiplicity stated" is not a control unless the count is
   fixed in advance. Enumerated in `src/v3_gate_checks.py`. Gate 2 *raised* this count, because it replaced the
   guessed threshold set with BSEACD's **declared** trigger levels: **5 thresholds** (GMA-10 DFCs 6.5 and
   49.7 cfs; Stage III 20 cfs; Stage IV 14 cfs; ERP 10 cfs) × **3 floors** (drought-of-record, q05, q10) ×
   **4 driver definitions** × **2 specifications** = **120 primary cells** (240 across two horizons). The margin
   sign is a *readout* of each cell, not an extra multiplier. Correction: **Holm–Bonferroni within
   specification-family**, family size **60**, per-test α = **0.00083** at family α = 0.05.

9. **Uvalde appears only as a motivating case**, never as a test.

---

## 6. The feasibility gate — **RUN, and it failed** (rev 4; the analysis below is rev 2's, retained)

Endorsing v3-C is not clearing it. Three caveats, all to be resolved **before** any v3 is written.

1. **Lovelady's usable annual coverage is probably short.** Continuous data only from **1991**; the annual rule
   (≥240-day year) will drop most earlier years — roughly 35 usable years against J-17's 90 and J-27's 81.

2. **Machine retrieval of Lovelady was not validated.** Existence is confirmed (BSEACD and NGWMN monitor pages;
   USGS gauge live). Programmatic pulls from the USGS groundwater endpoints were **flaky** — `503`, `301` and
   `400` across four attempts, and zero manual rows returned for 1949–1960. Treat retrieval as unproven.

3. **The springflow mitigation carries its own untested presupposition — this resolves an internal tension in
   rev 1.** Rev 1 argued that the margin has *effectively deterministic power* (§2), then conceded that ~35
   years is short enough to "interact badly with the underpowering problem." Both cannot stand unqualified. The
   resolution: the lemma's *implication* is deterministic, but **locating `H*₀` is itself a statistical problem**
   — `(a, α, β, γ)` must be estimated — so the determinism buys nothing if the estimate is too noisy to sign the
   margin. That is a real limitation on the head specification.

   The springflow specification avoids it (long record), but only by presupposing that **springflow dynamics are
   also well-described by a linear stock-flow map with a computable fixpoint**. That presupposition is untested
   and must not be smuggled in. **Pre-register a diagnostic:** fit the same map form to springflow and check H1
   and H2 *before* testing any sign prediction. If the diagnostic fails, the springflow port is invalid too, and
   the long record does not rescue it.

**If the gate fails, do not write a v3.** Rev 1 named "fall back to v3-B on Barton Springs." That fallback is
withdrawn: it is too weak to justify the versioning cost, because (i) B's evidential value is lower than rev 1
implied it would need to be, and (ii) the same family-equivalence and map-form questions remain unresolved on
that pool. A weak v3 is worse than none — it spends the pool *and* buys little. The correct action on gate
failure is to **defer**, leaving Barton Springs naive for a properly powered future test.

## 6.1 The E3 half of the program — stated, not left silent

v3-C generalizes E4. Declining v3-A leaves E3 without a generalization path, and silence would imply indefinite
deferral. Stated explicitly, the position adopted is **both** of the honest options, in different registers:

- **E3 does not generalize in verdict form.** This is the Uvalde record's actual finding, and it should be
  written into E3 as a **scope limit**, not left as an exploratory footnote: the ladder's retention verdict is
  established for its pool and is not claimed beyond it.
- **E3 generalizes in mechanism form** — recharge whiteness as the mechanism, head AC(1) as the moderator, and
  M1's convergence on persistence as the proximate cause of the retention flip (§6.2). This is v3-A's *content*
  without v3-A's confirmatory test. It is a **theoretical extension**, testable only where a pool is genuinely
  naive, and it is not part of v3-C's pre-registered claim set.

## 6.2 The M1-loss mechanism — elevated from erratum to secondary prediction

Rev 1 filed this as a proposed note to record §3.2. That undersells it. The retention flip's proximate cause is
not that M2 improved; it is that **M1 stopped working**:

| pool | head AC(1) | persistence h1 | M1 (AR1) h1 | M1's edge |
|---|---|---|---|---|
| J-17 (full window) | 0.6437 | 13.2301 | 12.8391 | **+0.391** (M1 wins) |
| J-17 (matched 1941–) | 0.6437 | 13.7623 | 13.1265 | **+0.636** (M1 wins) |
| Uvalde (native window) | 0.8442 | 8.0933 | 8.2250 | **−0.132** (M1 loses) |

As head AC(1) → 1, an estimated AR(1) converges on persistence and its RMSE edge decays into estimation noise.
Verified in `src/v3_gate_checks.py` (`erratum_M1_edge`, `erratum_monotone_in_ac1 = true`); it holds under both
J-17 windows, so it is not a window artifact.

Why this is more than an erratum:

- it **predicts** the direction of the retention flip *without fitting the flip*;
- it is **monotone** in AC(1), hence testable on a third pool;
- it is **mechanistic rather than statistical**, so it does not inherit the D1–D3 underpowering problem.

It therefore partially rehabilitates the two-pool comparison even though the point-rule flip itself is noise.
**Disposition:** carry it as a **secondary, clearly-labelled prediction** on v3-C's pool (never as the primary
claim, and outside the multiplicity family of §5 item 8 — it is a direction, not a cell), and as a standalone
mechanism note in E3.

**This also corrects the record.** Record §3.2/D6 glosses the flip as "persistence is a stronger baseline on
Uvalde, which makes the flip more surprising, not less." That reads the sign backwards: high head AC(1) does not
make the flip surprising, it **predicts M1's failure** and hence the rule's escalation to M2. This does *not*
overturn C4 — which falsifies mean reversion as the source of M2's *gain* (−0.18) — because that concerns a
different event (M1's *loss*).

## 7. Discipline note — what I did and did not look at

While establishing that the pool exists, I verified **only existence**: that endpoints resolve, that the well and
gauge are real, and what the declared thresholds are. **No statistic was computed on Barton Springs or Lovelady
data** — no AC(1), no means, no fit, not even a coverage count of the head series. Checking any of those now would
burn the pool exactly as Uvalde was burned. The whole value of v3-C is that its pool is still naive.

One correction to the review for the record: it cites recharge AC(1) as **0.182 vs 0.168**. My `0.182` is the
*J-17 full-window* value; the matched-window (1941–2023) figure my §2 table uses, and the like-for-like comparison
against Uvalde's native window, is **0.172 vs 0.168**. Both are correct; the review compared across windows. The
conclusion is unaffected.

**The general form of the trap that burned Uvalde.** The same discipline applies to v3-A's moderator check: **no
candidate pool's head AC(1) may be inspected to determine whether it lies in the "untested range."** Any such
check spends the pool — and this is exactly how Uvalde was spent, one defensible-looking look at a time. Only a
*directional* pre-registration ("AC(1) > X ⇒ M2 retained"), fixed before any inspection, avoids it. §4 states
this as an argument against v3-A; it is restated here because it is the **general rule**, not a v3-A quirk.

**"Pre-check" is not a firewall; it is a stage.** Adopted verbatim into the standing discipline:

> Any check that constrains a hypothesis's outcome is part of the hypothesis's test.

This is a fair retrospective criticism of how gate 4 was framed. Fitting the map yields `(a, α, β, γ)`, and those
determine `H*₀`, hence the *sign* of `m` — so the "pre-check" was never information-neutral with respect to the
sign test it was gating. The framing should have been **Stage 0 of one pre-registered analysis**, not a separate
feasibility gate.

**In this instance the defect was harmless, and it is worth being precise about why.** Gate 4 failed at the
*porting* level — record length, a near-zero `a`, an unobtainable `γ` — which under either framing is a Stage 0
failure: "the springflow specification is dead," not "the hypothesis is falsified." No sign test was computed, no
margin was formed, and no threshold comparison was made, so no confirmatory claim was ever at stake. Had gate 4
*passed*, the leak would have mattered a great deal, and the two-stage structure would have been mandatory.

**Standing rule going forward:** any future third-pool work is pre-registered as a single two-stage analysis
(Stage 0 porting → Stage 1 hypothesis), with the full fit reported rather than hidden — the discipline lives in
the pre-registration, not in the analyst's ignorance. Recorded for whoever picks up the Lovelady head route,
which remains **unrun**: no Lovelady AC(1) or coverage statistic has been computed.

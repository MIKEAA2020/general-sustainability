# E1 — Joint evaluation of three ecological audits (round 3)

**Source:** `uploads/e1 audit 2.txt` (1,648 lines; gpt L1, grok L494, qwen L772)
**Manuscript under review:** effectively v26 (`E1_v26.tex`) — no auditor cites a version number
**Evaluator:** agent, 10 Sep 2026

---

## 0. What kind of round this is

**This file is not round 2.** It replaced the earlier upload of the same name (2,312 lines →
1,648 lines, different content hash). The pushed copy of the previous round survives at
`batch 7/source_audits/e1 audit 2.txt` in the repository, so nothing was lost, but the
two must not be confused.

The difference matters for triage. Rounds 1–2 were **defect audits**: they found errors,
and the correct response was to fix or reject each item. Round 3 is a **contribution
audit**: all three auditors accept that the forecast result is sound and argue that the
*ecological content is thin*. Almost nothing here is a defect. The question is therefore
not "is this right?" but "does this change what the paper claims, and is it in scope?"

That distinction drives the whole evaluation. A contribution proposal that requires new
data or a new model class is not a correction — it is a different paper. Several of these
are excellent ideas that still must be declined.

---

## 1. Verdict summary

| # | Item | Auditor(s) | Verdict | Tier |
|---|---|---|---|---|
| **E1** | Lower equilibrium is **harvest-induced**, not biological depensation | gpt §1, grok §1 | **ACCEPT — correctness-adjacent** | **1** |
| **E2** | Capelin multiplier cannot produce negative production | gpt §4 | **ACCEPT** | 2 |
| **E3** | M1b cannot test a predator pit (𝔰 bounded below the collapsed range) | grok §3, qwen 2.5 | **ACCEPT — scope disclosure** | 2 |
| **E4** | Persistence winning is itself an ecological result (demographic memory) | qwen 2.1, grok §5 | **ACCEPT — framing** | 2 |
| **E5** | Prey non-retention is a lag/transmission result, not "capelin is irrelevant" | grok §4, qwen 2.4 | **ACCEPT — framing** | 2 |
| **E6** | Brier degeneracy on Spec A; propose ecological threshold metrics | qwen 3.10 | **ACCEPT diagnosis / DECLINE redesign** | 3 |
| **E7** | Report MSY = rK/4, B_MSY = K/2 next to every fitted (r,K) | grok C | **ACCEPT** | 2 |
| **E8** | (r,K) ridge: pre-collapse cannot identify r, post-collapse cannot identify K | grok §1 | **ACCEPT with correction** | 2 |
| **E9** | Regime-split RMSE (pre-1991 / 1991–95 / 96–2012 / 2013–24) | grok F, qwen 3.4 | **DEFER — attractive, out of frozen spec** | — |
| **E10** | Apparent-production figure P_t vs S_t with fitted curves | grok A, qwen 3.3 | **DEFER** | — |
| **E11** | Age-structured / cohort benchmark; ΔSSB decomposition | qwen 3.2/3.3, gpt §3, grok G | **DECLINE — data not available** | — |
| **E12** | Lagged capelin scan; recruitment depensation; seal-predation module | grok E, qwen 3.6–3.8, gpt §4 | **DECLINE — new model class** | — |
| **E13** | Refit M1b with 𝔰 above max training S | grok D(1) | **DECLINE — take D(2) instead** | — |
| **E14** | Time-varying / random-walk productivity module | qwen 3.5 | **DECLINE — frozen spec** | — |
| **E15** | Management strategy evaluation | qwen 3.13 | **DECLINE — different paper** | — |
| **E16** | Drop Prop 4.1, "canonical", aquifer from introduction | grok §6 | **PARTIAL — already done in v24** | — |

**Tier 1: 1 item. Tier 2: 6 items. Deferred: 2. Declined: 6. Partial: 1.**

---

## 2. Verified findings

Everything below was checked against source, not accepted on assertion.

### E1 — the harvest-induced threshold (the one item that touches correctness)

gpt's algebra is exact. For the Schaefer map, positive equilibria satisfy `rS(1−S/K)=C`, so

  S±(C) = (K/2)·[1 ± √(1 − 4C/(rK))]

Using E1's own printed fit (r = 1.935, K = 1032.7):

| C (kt) | S₋ (kt) | S₊ (kt) |
|---|---|---|
| 240 | **144.15** | **888.55** |
| 120 | 66.27 | 966.43 |
| 5 | **2.59** | 1030.11 |
| 3.19 | 1.65 | 1031.05 |
| → 0 | → 0 | → K |

This reproduces E1's printed repeller 144 kt and attractor 889 kt to the decimal, which
confirms the parameterisation is being read correctly.

**The consequence is the finding.** The 1995 SSB of 9.7 kt is below S₋(240) = 144 kt but
**above** S₋(5) = 2.59 kt. So the "no recovery from below the repeller" obstruction is a
property of *sustained 240-kt removals*, not of the stock's biology. Once catch falls to
moratorium levels the threshold drops by two orders of magnitude and the observed path is
no longer below it.

I checked whether v26 already says this: `grep` for harvest-induced / not-biological
framing next to depensation returns **nothing**. Proposition 4.1 correctly states
`C_t ≡ C` as a hypothesis, and §4 already scopes it away from M2/M3/M4 and from the
stochastic map — so the proposition is not *wrong*. But the paper never tells the reader
that the threshold is a function of catch, and a fisheries audience will read "lower
repelling equilibrium" as depensation. Both gpt and grok independently flag this.

**This is Tier 1 not because a statement is false, but because the most likely
misreading is a biological claim the paper does not intend and cannot support.**

### E8 — the ridge, with a correction

grok claims 1983–1990 cannot identify (r,K) because ΔS ≈ 0 with large catch leaves one
equation in two unknowns. I refit the collapse window at fixed K, optimising r:

| K (kt) | best r | training RMSE (kt) | implied MSY = rK/4 |
|---|---|---|---|
| 1032.7 | 1.764 | **60.73** | 455 |
| 1200 | 0.980 | 63.73 | 294 |
| 1500 | 0.627 | 68.83 | 235 |
| 2000 | 0.460 | 71.86 | 230 |
| 3000 | 0.363 | 73.78 | 272 |
| 5000 | 0.310 | 74.87 | 388 |

**The direction is confirmed and the magnitude is overstated.** A 5.7-fold change in r
(1.76 → 0.31) moves training RMSE by only 23% (60.7 → 74.9 kt), and MSY ranges over
230–455 kt. That is weak identification and it is a real ecological point — the fitted
r ≈ 1.9 is not a life-history estimate for a late-maturing gadoid. But it is **not** the
flat ridge grok describes ("the published fit is the high-r end of a ridge" implies near-
indifference). The minimum is shallow, not flat.

grok's parallel claim about the *recovery* window — that K is unidentified there — is
already in v26 and quantified: MSE moves only 127.4 → 149.9 over K ∈ [60, 5000]. **That**
one is genuinely flat. So the paper already makes half of grok's point; the pre-collapse
half is new and should be stated with the measured numbers above, not as "a ridge".

### E2 — the capelin sign argument

Verified against v26 L962: surplus is scaled by `(I_known/I_ref)^b`. For positive index
values this factor is strictly positive regardless of the sign of b, so
`sign{q(I)·g(S)} = sign{g(S)}`. With 0 < S < K and r > 0 the modelled production stays
positive: the module can shrink production but can never make it negative. Food
limitation severe enough to cause a net loss is therefore **outside the module's
representable set**, which is a sharper and more defensible statement than "the prey
module was not retained".

### E6 — Brier degeneracy

qwen says the Spec A Brier score is degenerate because the LRP sits above every origin
state. Checked: LRP = 884.58 kt, and **0 of 26** origins (1990–2015) are at or above it.
Confirmed. v26 already explains the mechanism in prose; qwen's contribution is naming it
a *design* limitation rather than a curiosity. The proposed replacement metrics
(P(S_{t+h} < S_t), rebuilding risk, CRPS) are a scoring redesign and are declined under
the frozen spec — but the diagnosis is right and can be stated in one sentence.

### E11 — why the demographic work must be declined

All three auditors converge on age structure as the highest-value enhancement, and they
are probably right that it is the missing ecology. It is **not feasible on the data in
this repository.** Inventory of `wave_e_cod/data/`:

- `ncam_2016_table_a2.csv` → `year, abundance_millions, biomass_kt, ssb_kt, age2_millions, M_age5_14, F_age5_14`
- `xtencam_table17_ssb.csv` → `year, abundance_millions, age0_millions, biomass_kt, ssb_kt, ssb_lo, ssb_hi, ssb_over_blim`

There are **no numbers-at-age, no weight-at-age, no maturity-at-age**. qwen's cohort
projection `Ŝ_{t+1} = Σ_a N_{a,t}e^{−Z}w_{a+1}m_{a+1} + R̂w₀m₀` cannot be built. gpt's
ΔSSB decomposition into survival/growth/maturity/recruitment cannot be built. grok's
item G is explicitly conditional ("if Table A2 gives recruitment, weight-at-age, maturity")
and that condition **fails** — grok was right to hedge it.

Two caveats worth recording, because they are not nothing:

1. `age2_millions` is present for all 33 years and is a genuine pre-recruit series. gpt's
   minimal test `ΔS ~ α + βS + γJ` is therefore *feasible in principle*. I ran it as a
   feasibility check only: in-sample RMSE 86.2 → 82.7 with age-2 added (n = 32). **This
   is in-sample on 32 points and is not evidence of forecast skill.** Turning it into a
   scored module means adding a rung to a frozen ladder, which requires
   `SPECIFICATION_v3.md`. Declined here, flagged as the strongest available follow-up.
2. `M_age5_14` records the mortality pulse directly: 0.40 (1990) → 1.00 → 2.21 → **2.58
   (1993)** → 0.29 (1995). This is in E1's own input file. It corroborates grok's §2
   point that the collapse requires a mortality/productivity term larger than the catch
   decline — and it means the paper can reference the pulse without appealing to the
   scalar residual, which is exactly the confusion T-FIX removed in v22.

---

## 3. What I disagree with

**grok, §6, "drop Proposition 4.1 from the introduction."** Already done — v24 removed
the equilibrium paragraph (r, K, repeller, attractor) from §1 and left a pointer to
Prop 4.1. grok is reviewing pre-v24 text on this point. The remaining introduction
mentions of "canonical" and the companion aquifer paper are legitimate: the companion is
citable by DOI under standing policy, and "canonical" describes the post-mortem
literature, not the authors' own work.

**grok, "Proposition 4.1 is a corollary of one ridge fit. The ridge itself is the
finding."** Half right. The proposition is a statement about *any* map in the family with
two positive equilibria and constant catch; it is not a corollary of the particular fit.
What *is* fit-specific is the claim that the Specification A path satisfies its
hypothesis. The honest repair is E1 (say the threshold is catch-dependent), not demoting
the proposition.

**qwen, 3.9 "compare forecast skill on raw survey indices."** The paper's predictand is
assessment SSB by design, and the smoothing caveat is already stated. Swapping the
predictand is a different study, not a strengthening.

**gpt's framing that the paper should "change the question" from *does structure beat
persistence* to *which ecological assumptions make it fail*.** This is a good research
programme and the wrong instruction for this manuscript. The retention rule was fixed
before scoring; rewriting the question after seeing the answer is precisely the practice
the protocol disclosure exists to prevent. The ecological *interpretation* can deepen
(E1–E8). The question cannot move.

---

## 4. What actually changes in the manuscript

Tier 1 and Tier 2 are all prose. No number changes, no new run, no ladder change, no
frozen-spec relaxation.

1. **E1** — after Prop 4.1's scope paragraph, add the catch-dependence of S₋ with the
   computed table (240 → 144 kt; 5 → 2.6 kt) and state plainly that the threshold is
   generated by sustained removals, not by biological depensation, so it does not explain
   non-recovery under moratorium catches.
2. **E8** — next to the collapse-window fit, report that fixing K over [1032.7, 5000]
   moves training RMSE only 60.7 → 74.9 kt while r moves 1.76 → 0.31, and that r ≈ 1.9 is
   not a plausible life-history rate for this species. Pair with the existing recovery-
   window flat-valley result as the two complementary identification failures.
3. **E7** — print MSY = rK/4 and B_MSY = K/2 beside each fitted (r,K) in Table 10.
4. **E2** — one sentence: the multiplicative index cannot represent a net production loss.
5. **E3** — one sentence: 𝔰 ≤ min_train S confines the threshold to at or below the
   collapsed range, so M1b does not test a high threshold or predator pit. (grok's
   option D(2), not D(1).)
6. **E4/E5** — reframe two existing passages: persistence as demographic-plus-smoothing
   memory rather than a null baseline; prey non-retention as a statement about
   contemporaneous transmission, not about capelin's ecological importance.
7. **E6** — name the Brier degeneracy as a threshold-design limitation in one clause.

**Deferred with reasons recorded (E9, E10):** the regime-split RMSE table and the
apparent-production figure are the two best remaining ideas and both use objects already
computed. They are deferred rather than declined because they change *reported scores and
figures* under a frozen specification; they belong in a declared additional pass, not in
a presentation revision.

---

## 5. Process note

The previous round exposed a failure mode I have to guard against here: gpt's
"Final sentence equating M and the residual" was raised in round 2, never transcribed
into the round-2 evaluation, and survived as a live contradiction in v19–v21 until it was
caught during Tier 3 planning. Accordingly, every numbered section of all three audits in
this file has been assigned a verdict in the table above, including the ones I decline.
Nothing in the source is left untriaged.

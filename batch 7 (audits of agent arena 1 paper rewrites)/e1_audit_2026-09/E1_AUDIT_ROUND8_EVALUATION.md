# E1 — Evaluation of the reframing proposal (round 8)

**Source:** `uploads/e1_audit_round8_reframing.txt` (122 lines, single reviewer)
**Manuscript reviewed:** v35 (see §1)
**Evaluator:** agent, 10 Sep 2026

---

## 0. Character of this round

Not a defect audit. A **strategic reframing proposal**: turn a case-study negative result
into a methods-and-practice contribution — a reusable retention rule plus information-set
framework, validated by simulation, with Northern cod as the worked application.

The diagnosis is largely right, and one of its observations is genuinely sharp. But it must
be triaged against two standing constraints it does not know about, and one of its seven
sections is already obsolete.

---

## 1. Section 7 is already done — the reviewer read v35

Every item in "Fix remaining terminology and consistency issues" was implemented in v36,
verified by grep against v37:

| item 7 claim | status |
|---|---|
| "delay" in retention rule and ladder ordering | fixed v36 |
| stale §3.5 numbers (16.7–108.2, p=0.90) | fixed v36 |
| Table 9 described as annual pass | fixed v36 |
| M1b "at its lower bound" | fixed v36 |
| 264 vs 303 cited to Table 5 | fixed v36 |
| Prop 4.1 → §3.3 | fixed v36 |
| 1992 catch-drop endogeneity | fixed v36 |

**No action.** Worth recording: reviews sometimes arrive against material that has already moved on, as
at round 5.

---

## 2. The strongest observation, and it is free

> "Even with future catch supplied — an advantage no operational forecast has — the
> structural modules still lose to persistence."

This is the best line in the review. It **inverts the conditional-hindcast caveat from an
apology into a strengthening**: the modules were given information no real forecast would
have, and still lost. The material is already in the paper (Table 2b distinguishes
*available* from *supplied*), but the paper never draws the inference.

**Verdict: ACCEPT, and it costs nothing.** It requires no new computation, no spec change,
and no reframing — one sentence in the Discussion. It is the highest value-per-risk item
in the review and is independent of everything else.

---

## 3. The core proposal: a simulation study

**Verdict: ACCEPT the science, pre-register before running.**

The reviewer is right that this is the highest-value addition and right about why: it is
the only way to answer "is your negative result just low power?" from inside the paper.
The manuscript currently answers with scope language, which is honest but uninformative —
it does not tell a reader whether the rule *could* have detected a real improvement.

But a simulation generates new scored results, and the standing frozen-spec discipline
holds that these cannot ride inside a presentation revision. More importantly, running it
first and specifying it afterwards would repeat exactly the weakness the paper already
discloses about its own tie band and comparator declarations.

**Action taken:** `SPECIFICATION_v4.md` written and **locked, not executed**. It fixes six
DGPs anchored to archived fits (verified: `r = 1.935/K = 1032.7`, `r = 0.458/K = 500.0`,
`σ = 11.8/33.8`, `φ = 0.95` all match `fixed_window_scores.csv`), the noise levels, the
series lengths matched to the real specifications, 1,000 seeded replicates per cell, and —
critically — **the interpretation thresholds in advance**:

| true-module retention | declared conclusion |
|---|---|
| ≥ 0.80 | rule has adequate power; cod non-retention reflects the data |
| 0.30–0.80 | partial power; result consistent with both readings |
| < 0.30 | **substantially underpowered; the manuscript's negative result must say so in the abstract** |

The third row is the point of pre-registering. Fixing it now removes the option of
reporting whichever outcome is more flattering. The sheet also discloses in advance that
the DGPs are members of the ladder's own class, so an adequate-power result is an **upper
bound** and does not license the claim that the real result is fully explained.

Per the user's instruction, the sheet is written and execution is held.

---

## 4. Where I do not agree

**Retitling to a methods framing.** Held. The title lock stands, and the user's own
reasoning is the right test: the methods framing becomes defensible when the paper
acquires a second application — the Edwards companion, or a simulation that establishes
the rule's operating characteristics across conditions. Until Ω_sim runs, the paper is a
case study with a stated protocol, which is what the current title says. Retitling first
would be a promise the content does not yet keep.

**"Target a 30–40% reduction in main-text length"** (section 5). Directionally reasonable,
but the specific cuts proposed are not. The reviewer would move to supplement: the M1b
profile, the M4 decomposition, the catch-treatment reconciliation, the floor-binding
counts. **Every one of those was added or sharpened in direct response to an earlier
audit round** — the M4 decomposition answers round 4 F22 and round 5 G18; the
floor-binding counts answer deepseek 24; the catch reconciliation answers round 6 H26.
Relocating them wholesale would re-open items that took five rounds to close. The Tier 3
experience already recorded that a −20% target rested on cuts that turned out to be locked
content.

**Accept in principle, reject the specific list:** length reduction should come from
sentence-level compression, not from removing material that answers standing objections.

**"Do not simply add more caveats — the paper is already over-caveated."** Half right. The
paper *is* dense with qualification, and the reviewer is right that impact does not come
from defending every corner. But several of those caveats exist because an auditor
demonstrated the unqualified claim was wrong. The distinction that matters is between
**scope statements that carry information** (which stay) and **hedging that carries none**
(already removed under the register scans). I will not strip qualifications that were
added to fix a verified error.

---

## 5. Disposition

| Item | Ruling |
|---|---|
| §7 terminology and consistency | already done in v36 |
| Supplied-catch inversion (§3 of the review) | **implement now** — one sentence, no new computation |
| Simulation study (§2) | **pre-registered** as `SPECIFICATION_v4.md`; execution held |
| Retention rule as general algorithm (§3) | partially present; strengthen when Ω_sim runs |
| Information-set table promotion (§4) | table exists (2b); promotion is a reframing decision, held with the title |
| Streamlining (§5) | accept the aim, reject the proposed cuts |
| Reframe the negative result (§6) | contingent on Ω_sim |
| Retitling | **held** — the lock stands until a second application exists |

---

## 6. Note on the reframing as a whole

The proposal is a good one and I expect it to be right eventually. The sequencing matters:
a methods paper claims that a rule is reusable, and that claim needs the operating
characteristics to back it. The correct order is **run Ω_sim, then reframe** — not reframe
and hope the validation supports it. `SPECIFICATION_v4.md` is the first half of that
sequence.

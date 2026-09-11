# Evaluation of the two advisories, and a strengthened condition set

**Date:** 10 Sep 2026 · **Basis:** v48, E3 v16, archived Edwards and cod scores, the band
check (`E1_E3_BAND_CHECK.md`).

---

## 0. The two advisories contradict each other

| | recommendation |
|---|---|
| **Q1 advisory** | Merge E3 into E1, restructure, retitle. "Option 2 is the best route to a general methods framing." |
| **Q2 advisory** | Modify condition 2 to *verdicts in the methods artefact, detail in cited companions* — which, in its own words, "makes the E1 + E3 + framework trio satisfy the test **without merging**, which is the outcome the merits favor." |

Both start from the same premise — that the deposit objection is withdrawn — and reach
opposite conclusions. They cannot both be adopted. Adjudicating requires a fact neither
advisory had.

---

## 1. The fact that decides it: **condition 1 is not currently met**

Both advisories treat condition 1 ("rule applied unchanged to ≥2 systems in different
domains") as satisfied. Verified against the two manuscripts and their specification
sheets, it is not:

| rule element | E1 | E3 |
|---|---|---|
| beat persistence | yes | yes |
| beat next-simpler comparator | yes | yes |
| **5% tie band** | **yes** | **no** |
| **both horizons required** | **yes** | **no** |
| oracle module (cannot retain) | no | yes |
| "declined on class grounds" | no | yes |

E3's published rule reads: *"A causal module was retained only if it beat both persistence
and the next-simpler causal model under a protocol frozen before any score."* No band, no
both-horizons requirement.

The Q2 advisory anticipated exactly this — *"'applied unchanged' must mean the same gates,
the same horizons, the same tie band… If E3 modified anything, say so and reclassify."*
That caveat turns out to be the operative one. **The two systems have not yet been scored
under one rule.** Any claim of reusability, in a merged paper or a framework paper, is
premature until they are.

## 2. What the band check already settles

Applying E1's rule to E3's archived scores (arithmetic on the decision, no refitting):

- **Edwards retained set under the unified rule: empty.**
- **Cod retained set under the same rule: empty.**
- **No E3 verdict changes.** Six margins fall inside the band; the one substantive case,
  M2m, was already excluded on class grounds.

So the unification is achievable and costless in verdict terms. **Same rule, same outcome,
two unrelated domains** — that is the reusability datum, and obtaining it required a
re-statement of E3's verdict under the unified rule, not a merge.

## 3. Adjudication

**The Q2 advisory is right on structure; the Q1 advisory is right on standard.**

Q1's core argument is that scattered evidence invites the question *"why isn't the
comparison in one place?"* That is a real objection, but Q2's modification answers it
directly: put both **verdicts** in the methods artefact, with detail cited. A reader sees
cod and Edwards side by side without leaving the paper. This is ordinary methods-paper
practice and does not require destroying an archived record.

Q1's argument for merging also rests on a claim that does not survive the condition-1
finding: it says Option 2 "needs the method to be *demonstrated* twice, which it already
is." It is not — not under one rule. Both routes need the same unification work first.
Once that work is done, the merge's remaining advantage is proximity of presentation,
which Q2's modified condition 2 supplies at far lower cost.

Q1 is right, however, that the **standard** must be demanding: a thin synthesis citing two
papers is not a methods contribution. Q2's modification prevents that by requiring the
verdicts, tables and comparison to be in the methods artefact itself.

**Recommendation: do not merge. Adopt the Q2 structure with the Q1 standard.**

The merge also carries a cost neither advisory weighs fully: E1 is at v48 after nine audit
rounds and is submission-ready. Restructuring it into a two-domain methods paper restarts
that process on a substantially different object. The framework paper can be written
without putting v48's stability at risk.

## 4. On the proposed conditions

Accepting Q2's set with two changes.

**Condition 2 — accept the modification, with a floor.** Verdicts in the methods artefact,
detail in cited companions. Adding the Q1 standard as an explicit floor: the artefact must
carry both applications' scored tables and the cross-application comparison as primary
content, not a summary sentence.

**Condition 5 — accept.** Portability is the claim a methods title makes, and a rule
embedded in prose is not portable. Cheap to meet; v43 already added an algorithm box, so
this is close to satisfied for E1's rule and needs restating for the unified rule.

**Condition 4 — verified, met.** The Q2 advisory was right to demand verification rather
than assertion. Checked: v48's comparison table reports **decision rules applied to the
same task**, each returning retain/not-retain — the adopted rule (0.376 / 0.978), MASE < 1
(0.651 / 0.675), an information criterion `n·log MSE + 2k` (0.509 / 0.992), plus tie-band
and gate variants. These are alternatives *to the rule*, not alternative scores. Persistence
is not among them, so the circularity the advisory warned about does not arise.

**Rejecting the two additions Q2 rejects**, for its reasons: third-party application is
unbounded in time; a third domain is diminishing returns.

**Adding condition 0**, which the verification exposed and neither advisory states as a
gate.

## 5. Final condition set

> **(0) Unification.** The rule is stated once, and every application's verdict is derived
> under that single rule. Where a companion applied a variant, the verdict is restated
> under the unified rule and any change disclosed. *Currently unmet: E3 used no tie band
> and no both-horizons requirement. The restatement is computed and changes nothing.*
>
> **(1)** The rule is applied unchanged to ≥2 systems in different domains. *Met once (0)
> is discharged: marine stock and groundwater aquifer.*
>
> **(2)** Both applications' retention verdicts are reported in the artefact carrying the
> methods title — scored tables and the cross-application comparison as primary content —
> with full application detail in cited companions. *Unmet; the framework paper supplies it.*
>
> **(3)** Operating characteristics established across >1 series length **and** ≥1
> misspecified-truth DGP. *Unmet. The binding constraint.*
>
> **(4)** The rule is compared against ≥1 standard alternative **to the rule**. *Met and
> verified: AIC-style and MASE-only, v48.*
>
> **(5)** The rule is stated portably enough that an independent analyst could apply it to
> a new system without consulting the applications. *Near-met; algorithm box in v43.*

When all six hold, the title lock lifts by its own terms. **Conditions 0, 2, 3 remain.**

## 6. Sequence

1. **Discharge condition 0.** Restate E3's verdict under the unified rule, with the band
   check as evidence and the pre-registration disclosure already drafted. No refitting.
2. **Discharge condition 3.** Amend `SPECIFICATION_v4.md` — dated, before execution — to
   add a misspecified-truth DGP and `T = 71`. Note that the naive regime-switch candidate
   is degenerate (floor in four steps) and needs calibrating to stay in range.
3. **Write the framework paper** stating the five conditions in its design section, dated,
   before the additional simulation work, so the title lift is deterministic.
4. **Lift the lock** when all six conditions hold.

E1 v48 stays as it is throughout. Its title remains accurate for what it does.

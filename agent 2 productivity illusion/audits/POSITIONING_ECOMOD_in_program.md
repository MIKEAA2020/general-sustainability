# Positioning the ECOMOD manuscript within the broader program

**Question:** After the scope-A re-modelling, should `manuscript_ECOMOD_v32` be published *separately* from the
"dehedged" version (`manuscript_v18_dehedged.txt`), or do they merit merging?

**Answer: publish separately — do not merge ECOMOD into v18.** The portfolio (below) makes this clearer, and
also reveals that the *real* overlap risk after scope-A is not v18 but two of its sibling papers.

---

## 1. The portfolio (what the "9 papers" actually are)

The account is a *program*, not one paper, and it is structured at two layers:

| ID | Title | Layer |
|----|-------|-------|
| **v18** | Scarcity-Driven Capital Liquidation and Delay-Amplified Instability: A Vector-Valued Flow-Balance Framework | **Master / synthesis** — consolidates the theory |
| paper1 | The Limits of Compensatory Aggregation: Weak vs Strong Sustainability Assessment | Theory (aggregation theorem / **Proposition 1**) |
| paper2 | An Obstruction Calculus for Viability under Incomplete Observation | Theory (viability) |
| paper3 | Typed Flux Ledgers and Depletion Arithmetic: Conservation, Componentwise Diagnostics | Theory (**vector accounting**) |
| paper4 | Delay-Induced Regime Change in Harvested Stocks: Mobilising & Protective Channels | Theory (**delayed-feedback core**) |
| paper5 | Periodic Review as Sampled Governance + 42-stock screen + Northern Cod | Theory + empirical |
| E1–E4 | Cod / Edwards Aquifer forecast-ladder and intervention tests | Applied case studies |
| **ECOMOD v32** | Emergent Carrying Capacity, the Biocapacity Ratio, and the Productivity Illusion | **Focused applied/dynamical** (this work) |

Key observation: **the author already publishes this as focused papers, not one giant manuscript.** v18 is the
*synthesis* of the theory (it contains Prop 1, the vector ledgers, the delay core, and the sampled-governance /
empirical audit). paper1–5 are the focused theory papers; E1–E4 the applied ones. ECOMOD is exactly the same
kind of focused paper — an applied, dynamical, self-contained contribution.

**Consequence:** subsuming ECOMOD into v18 would (a) bloat an already-synthesis-sized paper and (b) bury a
clean, focused manuscript. It is not the intended structure of this program.

## 2. Where the overlap risk *actually* is after scope-A

The initial instigation was "ECOMOD vs v18." But scope-A re-models ECOMOD into exactly the two things v18's
*siblings* already own:

- **paper1** owns the aggregation theorem ("no positively-weighted scalar aggregate certifies componentwise
  safety") — i.e. **the productivity-illusion theorem, in general form.** Re-scoping ECOMOD's headline to
  "the illusion is generic" collides with paper1.
- **paper3** owns the multi-component ledger / depletion-horizon accounting — i.e. **the vector accounting.**
  Re-scoping ECOMOD to "multi-component + active pool" collides with paper3.

v18 itself is *further* from ECOMOD than these two are, because v18's unique load is the delay-amplified
instability + four-state + empirical audit — a bifurcation/pathology story, not the footprint-accounting story.

## 3. What ECOMOD must OWN vs must CITE

For separate publication to be defensible (and to avoid self-plagiarism / salami-slicing within the author's own
body of work), the split is:

**ECOMOD cites (does not re-claim):**
- **paper1** for the aggregation theorem (sustainability-assessment theory).
- **paper3** (and v18) for the vector/ledger accounting and depletion horizons.
- **paper4** for the delayed-institutional-feedback regime-change results.

**ECOMOD owns as its own contribution:**
- **Emergent carrying capacity** (K arising from interaction, not imposed) — *not* in paper1–5.
- **The biocapacity/natural-capital operating boundary `R_B = 1`** vs the **flow-yield ratio `R_A = 1`** as a
  leading-but-non-causal signal — *not* in the theory papers.
- **The flow-yield share σ** (flow separable from stock vs capital growth/liquidation) and its decisive role.
- **The `τ_g` (regeneration-delay) recovery cliff** and the falsifiable predictions in footprint language.
- The orchard / bank-account framing that links the general framework to the **footprint-biocapacity
  sustainability-accounting literature** (GFN, Borucke et al.), which is ECOMOD's natural audience.

This is a legitimate, non-duplicative slot: paper1 is static *assessment theory*; ECOMOD is a *dynamical model*
that shows the same masking phenomenon arising *mechanically* from a delayed coupled system, and *quantifies* it
(5-yr window, R_B boundary, recovery cliff) in footprint terms.

## 4. Venue-specific note (you chose "nonlinear dynamics / ecological modelling")

For that venue ECOMOD must carry genuine dynamical content, and there is one more collision to manage:

- **ECOMOD's delays are ecological:** regeneration `τ_g` and demographic `τ_p`.
- **paper4's delays are institutional:** mobilising-vs-protective governance response, and the review interval.

ECOMOD must **state this distinction explicitly** — it is modelling the *fast ecological + demographic*
feedback, whereas paper4 models the *institutional feedback channel*. That is a real, defensible separation and
must be made explicit to a dynamics audience who will otherwise see them as overlapping.

Also, before submission to a dynamics venue, ECOMOD's headline stability claim must be fixed. Its current
abstract asserts "a positive real eigenvalue for *every* delay," which I verified in turn-6 to be **false at
forest scale** (dies for V≥50; only the degenerate s=0 continuum survives). That is precisely what the scope-A
re-derivation on the debt-on, multi-component system is for — but it must be corrected, not asserted, and the
resulting stability classification must be shown not to duplicate paper4's.

## 5. Recommended cross-reference map

```
paper1  (aggregation theorem)      ──► cited by ECOMOD (illusion is generic)
paper3  (vector ledgers/depletion) ──► cited by ECOMOD (multi-component + active pool)
paper4  (institutional delays)     ──► cited by ECOMOD (distinct delay channel: ecological vs institutional)
v18     (master synthesis)         ──► cited by ECOMOD as the overarching framework
ECOMOD  (emergent capacity, R_B=1, σ, τ_g cliff)  = the focused footprint/biocapacity dynamical paper
```

## Bottom line

**Do not merge ECOMOD into v18.** Publish it separately, positioned as the focused applied/dynamical companion
that connects the program's general framework to the footprint-biocapacity and emergent-carrying-capacity
literature. The discipline that makes this safe: **cite paper1/paper3/paper4/v18 for the general theory; keep
EMCOMOD's novelty in emergent capacity, R_B=1, σ, and the τ_g recovery cliff; make the ecological-vs-institutional
delay distinction explicit; and fix the (currently false) "vicious cycle for every delay" claim before submission.**

*Decision note. Read-only; verified against the 9-paper program, v18, paper1, and paper3. No manuscript modified.*

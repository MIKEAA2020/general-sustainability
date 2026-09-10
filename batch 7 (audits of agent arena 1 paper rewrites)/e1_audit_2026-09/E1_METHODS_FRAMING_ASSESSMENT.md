# E1 — Is a methods reframing now justified? And what can be borrowed from E2–E4?

**Date:** 10 Sep 2026 · **Basis:** v40, Ω_sim results, and the archived Edwards
(`wave_e_edwards/`) and cod (`wave_e_cod/`) trees.

---

## Part 1 — Retitling to a methods framing

### 1.1 The test the user set

> "If the paper acquires a second application — the Edwards Aquifer case, or a simulation
> study that genuinely establishes the rule's operating characteristics across a range of
> conditions — then the methods framing becomes defensible."

Two routes were named. **The simulation has now run.** So the question is whether Ω_sim, as
executed, meets the "across a range of conditions" bar.

### 1.2 Honest answer: not yet, on the simulation alone

Ω_sim establishes operating characteristics under a **narrow** range:

| dimension | covered | not covered |
|---|---|---|
| series length | `T = 33` only | `T = 71` (Specification B) |
| noise | σ ∈ {11.8, 33.8} | σ = 0, intermediate values |
| truth | 4 correctly-specified members of the ladder's own class | **any misspecified truth** |
| generating modules | M1, M2, M1b | **M3, M4 never simulated** |
| rule variants | the empirical rule only | tie band and horizon pair never varied |

A methods paper claims a rule is **reusable**. That claim needs the rule characterised
where a user would actually apply it — different lengths, different noise, and above all
against truth outside the model class, since no real system is a member of one's ladder.
Ω_sim currently measures power against the easiest possible alternatives and says so.

**Retitling now would promise generality the validation does not yet deliver.** The title
lock should hold.

### 1.3 But the *other* route is closer than I assumed

The Edwards companion is not a loose analogue. Checked against
`wave_e_edwards/SPECIFICATION_v2.md` and its archived scores, it runs **the same ladder
architecture and the same retention rule** on a hydrological system:

| | Northern cod | Edwards Aquifer |
|---|---|---|
| predictand | SSB, kt | aquifer head, ft |
| baselines | naive_persist, naive_train_mean | naive_persist, naive_mean |
| ladder | M1, M1b, M2, M3, M4 | M1, M2, M2m, M3, M4 |
| rule | beat next-simpler **and** persistence | beat next-simpler **and** persistence |
| oracle | — | M2_oracle (diagnostic, cannot retain) |
| verdict | no module retained | no module retained |

And the two reach that verdict by **different routes**, which is what makes the pair
informative rather than repetitive:

| system | h=1 module | persistence | 5% band | outcome |
|---|---|---|---|---|
| cod | M1 120.5 | 98.0 | 93.1 | loses outright, by 23% |
| Edwards | M1 **12.84** | **13.23** | 12.57 | **beats persistence on the point rule, dies in the tie band** |

Verified: Edwards M1 is *below* persistence at h=1 (12.84 vs 13.23) yet is not retained,
because it fails to clear the 5% band and reverses at h=5 (21.25 vs 21.11). On cod nothing
comes close; on Edwards a module reaches the bar and the **tie band and two-horizon
requirement do the deciding**.

**That is a genuine methods result.** It demonstrates the rule's gates are load-bearing —
not decoration — on a system where the point ranking alone would have retained a module.
Ω_sim shows the same thing synthetically (the gates remove 69–94% of H2-passers); Edwards
shows it on real data from another domain.

### 1.4 Recommendation

**Hold the title. Pursue the cross-system framing as the route to it, not the simulation.**

The strongest available methods paper is not "cod plus a power study" — it is **one rule,
two unrelated systems, two different failure modes, plus a power study explaining when the
rule can and cannot see structure.** That is a framework claim with two applications, which
is exactly the test the user set.

Sequence:
1. Extend Ω_sim on the two axes that matter most for a reusability claim: a
   **misspecified-truth DGP** (bounds power from *below*) and `T = 71`.
2. Coordinate with the Edwards paper on a shared statement of the rule.
3. *Then* retitle, with two applications and a two-sided power bound behind it.

Retitling before step 1 would repeat the pattern this project has already corrected twice:
making a claim and assembling the support afterwards.

---

## Part 2 — What can be merged or borrowed from E2–E4

### 2.1 What the constraints actually forbid

`SPECIFICATION_v2.md` is precise, and the distinction matters:

> "no row of one enters any fit, score, or verdict of the other, and R04 forbids judgment
> transfer between them … Nothing in this tree is pooled with the Edwards J-17 object."

This forbids **pooling data** and **transferring verdicts**. It says nothing about reusing
a *decision rule*, a *reporting template*, or a *diagnostic*. A rule is not a row of data
and applying it twice is not a judgment transfer. So the following are all admissible.

### 2.2 Borrowable now, no new computation, no constraint touched

| # | Borrow | From | Value |
|---|---|---|---|
| **B1** | **The tie-band demonstration.** Edwards M1 beats persistence on points and is still not retained. | E3 | Shows the gates decide real cases. E1 currently has no example where the band bites. |
| **B2** | **The oracle-module device.** Edwards runs `M2_oracle` with realised future fluxes, explicitly unable to retain — an upper bound on what perfect information buys (7.55 against persistence 13.23). | E3 | E1 has the *ingredients* (M2–M4 already receive future catch) but never frames a bound. This would sharpen the supplied-catch inversion added in v38. |
| **B3** | **"Declined on class grounds."** Edwards M2m beats persistence at h=1 (12.28) yet is declined because it collapses to AR(1) under constant fluxes — "not extra structure". | E3 | A principled category E1 lacks: a module can win on score and still not count as added structure. Directly relevant to M1b, whose 𝔰 → 0 makes it the zero-threshold cubic branch. |
| **B4** | **Cross-system framing of the null.** Two systems, same rule, same verdict, different mechanism. | E3/E4 | The core of any methods framing. |

### 2.3 Not borrowable

- **Pooling any series.** Forbidden explicitly, and correctly.
- **Transferring the Edwards verdict** to cod or vice versa. R04 forbids it; the typed
  fields differ.
- **Merging E1 and E3 into one paper.** Both are complete, both are submitted-ready, and
  both have Zenodo DOIs. A merged paper would supersede two archived records. The
  cross-system contribution belongs in a *third* framework paper that cites both, which is
  option 4 in the round-8 review's own ranking.

### 2.4 What E2 and E4 offer

E2 and E4 are the intervention papers (viability kernels, governance families). They share
the frozen-spec discipline and the uncertainty-class vocabulary, but not the forecast
ladder. **Borrow the discipline, not the content.** The one transferable item is the
`UC-min / UC-q05 / UC-q10` uncertainty-class convention, which is a cleaner way to label
scenario strata than E1's current prose — but E1 has no scenario strata, so there is
nothing to relabel. **No action.**

---

## Part 3 — Recommended next steps, in order

1. **B1 and B3 now** — one paragraph each in E1, no new computation. B1 gives the rule a
   demonstrated bite; B3 gives a principled name to what M1b does. Both cite Abaee (2026a)
   as a companion, which standing policy already permits by DOI.
2. **B2 next** — frame the supplied-catch asymmetry as an information bound, using the
   Edwards oracle as the precedent.
3. **Extend Ω_sim** — misspecified truth and `T = 71`. This is the real gate on a methods
   claim, and it is the one thing that cannot be borrowed.
4. **Then reconsider the title**, with two applications and a two-sided power bound.

Steps 1–2 strengthen E1 as it stands. Step 3 is what would make the reframing honest.

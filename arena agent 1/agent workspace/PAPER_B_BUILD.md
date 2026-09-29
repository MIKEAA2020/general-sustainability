# Paper B — build document

**Working title.** *The decision clock: how review timing and response delay determine
resource stability*
**Venue.** preprints.org first; journal submission derived from it afterwards.
**Length is not a constraint.** No word budget. This retires the `cut the math density hard`
instruction, which was advice for a NatSustain limit that no longer applies.

Status 2026-09-29: **unblocked**. The plan's §4 item 1 ("settle the P5/E2 question") was
closed by the §2 computation, and item 5 ("reconcile E2 and ARV") was closed by §8.2. Both
were the long-pole items. What remains is drafting, one research item, and figures.

---

## 1. Source map

| source | file | words | supplies |
|---|---|---|---|
| P5 sampled governance | `diffs/p5_v47.tex` | 18,259 | review interval → closed-loop stability boundary |
| P4 governance delay | `diffs/p4_v41.tex` | 27,339 | response delay → stabilising window |
| E2 cod certification | `fam/e2/paperE2_cod_intervention_v29.tex` | 16,176 | `C*`, `T*`, the frozen protocol |
| ARV | `arv_v9` ≡ `applied_regime_viability_v9` | — | **no file in the workspace** |

**ARV is absent locally and this is not a blocker.** Its reconciliation with E2 is already
archived in `FAMILY_CONSOLIDATION_PLAN.md` §8.2, which is the only thing Paper B needs from
it. Should the full text be wanted, it is presumably on the remote under one of its two
names; it has not been fetched.

E2's graphical abstract already exists: `fam/e2/graphical_abstract_e2.png`,
`fam/e2/graphical_abstract_e2_data.json`, `make_graphical_abstract_e2.py`. It is the model
for the other two figures.

---

## 2. The headline and the result that carries it

> What decides whether management stabilises or destabilises a renewable resource is not
> biology alone but the decision clock.

**The two results conflict, and the conflict is the result.** This is stronger than the
agreement would have been, and it must be stated as a finding rather than smoothed over.

| | object | bound | direction |
|---|---|---|---|
| E2 | open-loop certification horizon | `T* = 6` (worst class) / `T* = 7` (informative) | longer is **certificate-failing** |
| P5 on cod | closed-loop stability boundary | unstable below **17.5–175 yr** | longer is **stabilising** |

On cod biology the two constraints are not merely non-coincident, they are **incompatible**:
no review interval is both stable and certifiable. The feasible window is empty by a factor
of at least 2.5.

### 2.1 Both caveats travel with the result

Both are load-bearing. Neither may be demoted to a footnote.

1. **The transport is not unique.** P5's institutional parameters carry implicit scale —
   `Zref`, `delta`, `Emax` are absolute, not scaled to biomass — so "run P5 on cod" admits
   several defensible calibrations and the crossing is pinned only within **17.5–175 yr**
   across six transports. The *conclusion* (no coincidence; constraints incompatible) holds
   in all six. The *number* does not.
2. **The 6.501 yr is ill-conditioned.** A **0.2%** change in the exploitation ratio moves
   the crossing by 55%:

   | `N*/K` | crossing |
   |---|---|
   | 0.89552 | 6.50 yr |
   | 0.89343 | 10.10 yr |
   | 0.88507 | 18.38 yr |
   | 0.87462 | 25.31 yr |

   P5's headline number is a property of one knife-edge calibration, not a robust timescale
   of the mechanism. **Do not lead with it without a sensitivity band.** The plan flags this
   as worth raising with P5 before the merge; that recommendation stands.

### 2.2 What must not be said

The conflated claim — that the two numbers are two faces of one quantity — would put the two
constraints intersecting in `[6.501, 7]` yr, a half-year window, empty under E2's worst
residual class. It is striking, and it is a cross-system inference between systems whose
growth rates differ by **11.8×** (`r = 0.2369 /yr` for cod against `0.02 /yr` for P5's
baseline). Any reviewer who checks the parameters finds the window is an artefact. It does
not go in.

Root cause, recorded so it is not repeated: **the headline was written before the check.**
The plan said *"If those are two faces of one quantity, Paper B has a headline no reviewer
can miss"* — a conclusion stated as an aspiration, attached to a comparison nobody had
performed, which then survived an entire drafting cycle unchallenged.

---

## 3. The E2 / ARV paragraph

One paragraph, both directions named. **There are no numbers to reconcile** — the two read
the same cod record and answer opposite questions.

| | ARV | E2 |
|---|---|---|
| direction | obstruction / necessity | construction / sufficiency |
| arithmetic | exact rational, no fitted model | floating point, Schaefer fitted 1983–2007 |
| certified object | harvest-free multiplier bracket `[rho, max{rho+r, rho/(1-r)}]` | `C* = 91.59 kt`, `C_vac = 215.2 kt`, `T* = 6/6/7` |
| finding | both collapse steps are harvest-free contractions (upper bounds 0.754, 0.372); the reference window's worst step does **not** certify — "a typology, not a blanket verdict" | the reference point is expansive (`F'(K*) = 1.1531`) and 91.59 kt is certifiably viable for 6–7 years |

The link worth using runs the other way: ARV's harvest-free collapse certificates are
*evidence for* E2's regime-dependence conclusion (171 kt on the post-moratorium window,
0 ± 8 kt on the modern series). A record whose collapse steps were harvest-free contractions
is not one stationary production regime — which is exactly why E2's bound is
regime-dependent. Paper B should say that.

---

## 4. The null result, promoted

Currently framed as a limitation. Well-framed null results are publishable at this level;
buried ones are not. **It belongs in the abstract.**

- P5's multiplicity-controlled screen of **42 stocks** finds no robust institutional cycles.
- The **32-system** cross-sector search finds no unconfounded oscillator.

Together with the headline: periodicity alone cannot diagnose governance feedback. That is
the positive content of the null, and it is what makes the mechanism argument (rather than a
cycle-hunting argument) the right one.

---

## 5. Figures

E2's Figure 10 is the model: one glance, no notation. No figure budget to respect.

1. **Review interval → stability**, from P5. Must carry the sensitivity band, not the single
   6.501 point.
2. **Governance delay → the stabilising window**, from P4.
3. **The certified horizon against catch**, from E2.

One of the three exists in substance already (E2's graphical abstract, with its data JSON
and generator script); two are to be drawn.

---

## 6. Outline

1. **Introduction** — the headline; the two halves of the mechanism; the cod instance.
2. **The decision clock: two mechanisms** — 2.1 review interval and sampled-control
   stability (P5); 2.2 response delay and the stabilising window (P4); 2.3 why these are one
   idea and not two.
3. **Evidence I: 42 stocks** — the multiplicity-controlled null, promoted.
4. **Evidence II: 32 cross-sector systems** — the unconfounded-oscillator null, promoted.
5. **The cod certification (E2)** — `C* = 91.59 kt`, `C_vac = 215.2 kt`, `T* = 6/6/7`,
   `F'(K*) = 1.1531`, frozen protocol.
6. **The conflict** — certification expires at 6–7 yr while the sampled loop is unstable
   below ~17.5 yr on the same stock; the window is empty; **both caveats carried here**.
7. **The harvest-free reading (ARV)** — one paragraph, §3 above.
8. **Figures** — the three of §5, with the sensitivity band on the first.
9. **Cadence table** — real institutional review cycles against the horizon each must sit
   inside (§7 below).
10. **Discussion and policy.**
11. **Conclusion.**

---

## 7. Open items before drafting can complete

| item | kind | state |
|---|---|---|
| Cadence table | **research** | needs an actual survey of institutional review cycles. E2's Discussion names two real ones — the IWC's six-year implementation reviews and aboriginal subsistence strike limits set in six-year blocks — plus NOAA's management-track assessments. Those three are a start, not a survey. |
| Figures 2 and 3 | **production** | to be drawn; generator script for E2's abstract is the pattern to copy. |
| 6.501 sensitivity | **decision** | the plan recommends raising the ill-conditioning with P5 before the merge. Unresolved. |
| ARV full text | optional | not needed for the paragraph; fetch only if more is wanted. |

---

## 8. Honesty constraints for this paper

- The conflict is a finding, but it is a **cross-system** one with a non-unique transport.
  State the conclusion, carry both caveats, and never print the half-year window of §2.3 as
  a result.
- Do not present the P5/E2 numerical proximity as meaningful. It is a selection from a
  four-entry crossing record, two of whose entries are explicitly forward-Euler artefacts,
  and whose protective-exact channel has no crossing at all.
- The null result is a result. Do not bury it in a limitations paragraph.

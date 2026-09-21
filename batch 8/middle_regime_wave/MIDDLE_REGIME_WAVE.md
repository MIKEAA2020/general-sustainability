# The Middle-Regime (Common-Shock) Computation on the Paper-1 Witness Datum — Research Wave Record

Task 108 / batch 8 / paper 1 (Ecological Indicators). Queue point 3.A-6 / 3.E-42: the
three-regime disturbance table's middle cell (v53 Table 5, Section 5.4) is *"not analysed
on this datum: the verdict requires its own exact computation --- a common-shock variant
of the witness --- not an assertion."* This wave executes that computation, together with
the regime-(i) handshake (the action-indexed class must reproduce Theorem 5 exactly) and
the regime-(iii) verification (the coupled class, both formalizations). Owner directive
(this round): the middle-regime computation is the next small exact wave.

Discipline (the σ-wave standard, Task 105): standard library only;
`fractions.Fraction` exclusively — no floats, no tolerances, no randomness;
deterministic; any failed gate exits nonzero. Every decision is an exact rational
comparison; every interval endpoint is solved in closed form. Deliverables:
`middle_regime_verify.py` (the fail-loud exact verifier) and
`middle_regime_run_log.txt` (the committed byte-reproducible passing log —
**77/77 checks pass**, exit 0).

Witness baseline: `paper1_assessment_separation_v53.tex` (Section 4.5 datum,
Section 6.3 fishery reading, Table 5 in Section 5.4). All section/table references
below use the v53 rendered numbering.

---

## 1. The program being executed

The batch-8 queue (Task 104's joint assessment, Task 105's plan) left the middle
cell of Table 5 as the one honestly-open verdict in the disturbance-class scoping:
row (i) is proven (the action-indexed witness exhibits the acceptance gap,
Theorem 5), row (iii) is asserted (the coupled collapse), and row (ii) — the
common biomass shock, "one shared shock strikes the same floor coordinate of every
plan" — demanded its own exact computation before any verdict is asserted. The
practitioner checklist's sixth audit point ("Disturbance structure … the
separation's scope rides on the class", Section 5.5) inherits whatever this
computation yields. This record supplies the missing verdict and, in the process,
sharpens row (iii) from an assertion into two exact, reading-conditional theorems.

## 2. The common-shock variant of the witness (the model, on the manuscript's own currency)

The Section 4.5 datum decomposed per the Section 6.3 arithmetic, exactly as the
σ-wave found it:

- Each principal plan's announced schedule is a mid-interval tent drawdown of
  depth **3/2** in its characteristic coordinate (FAST: the quota pulse on s1;
  SLOW: the gradual burden on s2); the other coordinate is constant.
- Each environmental event is a transient tent dip of depth **δ** in ONE floor
  coordinate, troughing at t = 1/2, recovered by t = 1 (successors unchanged).
- The Section 4.5 worst-case depth **2 = 3/2 + 1/2** is the Section 6.3 identity:
  quota pulse 3/2 + heatwave 1/2 (check 0.2).
- STAGED spends x (tube [x−1, x], so it needs x ≥ 1) while its floors grow
  linearly to s + e, e = (1/4, 1/4); an event of depth δ on a growing floor dips
  it to s + 1/8 − δ (the trough at t = 1/2 on the linear growth), i.e. by
  **max(0, δ − 1/8)** (check 0.3).

Disturbance classes (each a set of disturbances; a disturbance is a map
coordinate → event depth; the disturbance quantifier is innermost, per the
manuscript's own quantifier discipline, Section 2.2):

| class | reading | disturbances |
|---|---|---|
| `action_indexed` | regime (i), Section 4.5's convention | each plan suffers only its own characteristic coordinate's event (STAGED and NO-SWITCH: none) |
| `common` | regime (ii) — **the middle cell** | the two coordinate events are separate disturbances, each striking EVERY plan |
| `coupled` | regime (iii), additive reading | ONE disturbance carrying both coordinate events simultaneously, riding on the plans' own schedules |
| `coupled_total` | regime (iii), replace reading | every announced-schedule plan's worst case is the full-magnitude dip 2 in EACH floor (tent schedules suppressed) |
| `single` | row-(ii) literal sub-case | only the s1 event exists |

All verdicts are exact: per-weight serving sets are computed as intersections of
closed intervals with rational endpoints; coverage is an exact interval-union test;
every closed form below is verified on grids (5000-state grids for the common
class) plus a curated witness list, and every constant is a Fraction.

**The STAGED kink lemma** (used throughout; the wave's one methodological
device): STAGED's aggregate dip is `max(0, raw(p) − 1/8)` with raw affine in the
weight share p — a *kinked* function. The admissibility requirement
`A(p) ≥ max(0, raw(p) − 1/8)` decomposes **exactly** into the two affine
conditions `A(p) − raw(p) + 1/8 ≥ 0` and `A(p) ≥ 0` (check 1.10 probes the
decomposition against the closed form g(p) = max(p, 1−p)/2 − 1/8 on the whole
p-grid). FAST/SLOW dips are affine in p, so their endpoint interpolation is
exact. No floating point anywhere.

## 3. The regime-(i) handshake (Part 0 of the run log)

The action-indexed class reproduces the manuscript's Theorem 5 exactly, on
676 grid states + the witness list:

- V_typ = {x ≥ 1} ∪ {s1 ≥ 2} ∪ {s2 ≥ 2} (Theorem 5(1); check 0.7);
- V_weak = {x ≥ 1} ∪ {s1 + s2 ≥ 2} (Theorem 5(2); check 0.8);
- the licensing handshake at the canonical datum (1/2, 6/5, 6/5): FAST serves
  p ∈ [0, 3/5] (r ≥ ρ1 = 2/3), SLOW serves [2/5, 1] (r ≤ ρ2 = 3/2), the
  Section 6.3 numbers (checks 0.9–0.10);
- the strictness witness (1/2, 1/10, 1/10) fails even the weak test
  (Theorem 5(5); check 0.11).

The computation is anchored to the deposited datum before any new class is
evaluated — the bridge the σ-wave established (its Part 0) is re-established
here against v53.

## 4. The middle-cell verdict (regime ii) — the exact results

**Theorem M1 (the middle-cell verdict).** On the common-shock variant of the
Section 4.5 witness datum at event depth δ = 1/2:

- **V_typ(common) = {s1 ≥ 2, s2 ≥ δ} ∪ {s2 ≥ 2, s1 ≥ δ} ∪ {x ≥ 1, s_i ≥ 3/8}**
  (check 1.1; identical to the coupled class — per-coordinate tube minima are
  event-combination independent, check 3.1);
- **V_weak(common) = {x < 1: s_i ≥ 1/2, s1+s2 ≥ 2} ∪ {x ≥ 1: s_i ≥ 3/8}**
  (check 1.2);
- the acceptance gap **SURVIVES the common-shock regime**:
  **FP_cs = V_weak \ V_typ = {x < 1, 1/2 ≤ s_i < 2, s1 + s2 ≥ 2}** (checks
  1.4–1.5) — strictly smaller than the action-indexed gap region
  I = {x < 1, s_i < 2, s1+s2 ≥ 2} by **the exact 1/2-cut**, nonempty with
  interior, and the canonical datum (1/2, 6/5, 6/5) is a member: the
  compensatory/noncompensatory separation is **not** an artifact of the
  action-indexed convention.
- **the exact cut:** every action-indexed gap state with min(s) < 1/2 is
  weak-REJECTED under the common class — universal rejection on that sub-region
  (check 1.8; e.g. (1/2, 1/10, 19/10), which the action-indexed weak test
  accepts by sum = 2);
- **thresholds unshifted on the surviving region:** on all 432 grid gap states,
  FAST's common-class licensing endpoint EQUALS the action-indexed endpoint
  s2/(3/2+δ−s1+s2) = 1/(1+ρ1), SLOW's the mirror (checks 1.6–1.7; the general-δ
  version at δ ∈ {1/4, 1/2, 1} is check 4.e). The audit's "Reduced / Shifted"
  cell is now exact: **reduced by the 1/2-cut, not shifted** (check 6.2).

*Proof sketch (machine-anchored).* FAST's common-class requirement at weight
share p is A(p) ≥ max(2p, p + 1/2) (its own tent 3/2 in s1 plus the event 1/2
in s1, and the event 1/2 in s2 weighted by 1−p); SLOW's is the mirror; STAGED's
(x ≥ 1) is A(p) ≥ max(p, 1−p)/2 − 1/8 (the kink lemma). The pointwise minimum
of the three thresholds is STAGED's g(p) wherever x ≥ 1 and the FAST/SLOW tent
pair min(1/2 + min(p, 1−p)) elsewhere; covering [0,1] against an affine A
reduces to endpoint evaluations, giving exactly the stated closed forms. ∎

**Theorem M2 (the rescue trichotomy).** Under the common class the rescue
threshold becomes (check 1.11, grid-adjudicated; witnesses 1.12–1.13):

  κ*(z) = 0 on V_typ;  (1−x)+ on {s_i ≥ 3/8} \ V_typ;  **∞ on {min(s) < 3/8} \ V_typ.**

The qualitative change: **the resource route no longer rescues every failure
state.** Witness (1/2, 1/4, 3): no reserve increment whatsoever rescues it
(κ* = ∞) — the weak floor is below the 3/8 event-exposure of the growing
STAGED floors; while the canonical datum's shortfall stays 1/2 (its
action-indexed κ*). Under the action-indexed class κ* = (1−x)+ whenever the
gap is entered with both floors at least … — there the route is unconditionally
finite; the common shock introduces the first **unrescuable-by-reserve**
failure states on this datum.

**Theorem M3 (blend fragility).** Theorem 9's convexification handshake breaks
under the common class, by exactly one event depth:

- action-indexed: the blend window is nonempty exactly on {s1+s2 ≥ 3/2+δ}
  (Theorem 9 at every tested depth; checks 2.2, 4.f);
- **common (and coupled): nonempty exactly on {s_i ≥ δ, s1+s2 ≥ 3/2+2δ}**
  (δ = 1/2: {s_i ≥ 1/2, sum ≥ 5/2}; checks 2.1, 2.3, 2.5, 3.9, 4.f).

The common-class gap is therefore **not blend-closed** on the fragile band
sum ∈ [2, 5/2): the convexification-fragility witness (1/2, 1, 1) is a
common-shock gap state with NO admissible blend (check 2.4), and every grid gap
state with sum ≥ 5/2 has one (check 2.5). An agency tempted to invoke Theorem 9's
collapse at a shallow common-shock gap state cannot: the blended menu itself is
inadmissible there. (The coupled gap, by contrast, IS blend-closed — its window
threshold and weak boundary coincide, {s_i ≥ δ, sum ≥ 3/2+2δ}; check 3.9 —
the fragility is class-conditional, check 3.10.)

**The single-event sub-case (the row-(ii) literal reading):** V_typ = {s1 ≥ 2}
∪ {s2 ≥ 3/2, s1 ≥ 1/2} ∪ {x ≥ 1, s1 ≥ 3/8}; V_weak = {x < 1: s1 ≥ 1/2,
sum ≥ 2} ∪ {x ≥ 1: s1 ≥ 3/8}; gap = {x < 1, 1/2 ≤ s1 < 2, s2 < 3/2,
sum ≥ 2}, the canonical datum a member (checks 5.1–5.4).

**The δ-family (Part 4):** all closed forms above are verified at
δ ∈ {0, 1/4, 1/2, 1, 5/4, 3/2, 2} on 4-cross-section grids (checks 4.a–4.d);
δ = 0 degenerates to the benign datum on which all classes coincide (check 4.g)
— the middle-cell verdict is a genuine disturbance-structure effect, not a
modeling artifact.

## 5. The coupled regime made exact (regime iii, both readings)

v53's row (iii) asserts: "universal rejection: the per-weight licensing
structure degenerates and the compensatory/noncompensatory divergence collapses
into common rejection." The computation converts this into two exact,
reading-conditional statements.

**Theorem M4 (additive reading — depth-dependence, boundary, relocation).**
Under the `coupled` class (events riding on the plans' own schedules):

- V_typ(coupled, δ) = V_typ(common, δ) (check 3.1); V_weak(coupled, δ) =
  {x < 1: s_i ≥ δ, sum ≥ 3/2+2δ} ∪ {x ≥ 1: s_i ≥ max(0, δ−1/8)} (checks 3.2–3.3);
- at the datum's full magnitude (δ = 2): every enumerated I-state is
  weak-REJECTED — the Section 5.4 claim holds on the witness's gap region
  (check 3.5);
- **but the claim is depth-dependent with the exact boundary δ = 5/4**: at
  heatwave magnitude (δ = 1/2) deep-I states SURVIVE as coupled gap states —
  e.g. (1/2, 19/10, 19/10) (check 3.6) — no I-state survives at δ ≥ 5/4 while
  (1/2, 79/40, 79/40) survives at δ = 5/4 − 1/40 (check 3.7, fine
  3,752-state I-grid);
- and at full magnitude the separation **relocates rather than vanishes**: the
  coupled(2) gap {x < 1, 2 ≤ s_i < 7/2, sum ≥ 11/2} is nonempty — (1/2, 3, 3)
  is weak-accepted and typed-rejected (check 3.8). "Universal rejection" is
  exact on I, not global: the divergence re-emerges at larger floors.

**Theorem CT (replace reading — the collapse).** Under the `coupled_total`
class (each announced-schedule plan's worst case is the full-magnitude dip 2 in
EACH floor; tent schedules suppressed):

- FAST and SLOW degenerate to the SAME, weight-independent requirement
  A(p) ≥ 2 — identical serving intervals at every probe; they fail together at
  every weight (check 3.11: both serve nowhere at the canonical datum; both
  serve [0,1] at (1/2, 5/2, 5/2); both serve exactly [1/2, 1] at (1/2, 3, 1));
- **V_typ = V_weak = {s1 ≥ 2, s2 ≥ 2} ∪ {x ≥ 1, s_i ≥ 15/8}** (check 3.12):
  the typed/weak separation **COLLAPSES entirely** — the gap is empty on every
  grid state and witness (check 3.13);
- the collapse mechanism: the weak test's advantage is weight-wise plan choice;
  when every plan faces the same plan- and weight-independent dip, choice buys
  nothing, and the per-weight cover condition degenerates to the same
  per-coordinate condition the typed test applies. The replace reading is also
  **strictly more demanding** than the action-indexed class: the witness
  (1/2, 3, 1) is action-indexed typed-ACCEPT (s1 ≥ 2) yet a coupled-total FULL
  REJECT on both tests, as is the canonical datum itself;
- STAGED's rescue route survives (its growth mechanics are not a "schedule" in
  the cost sense; the dip lands on the growing floor: threshold 15/8, exactly
  its coupled(2) branch) — and it is the only surviving distinction between the
  two tests' hypotheses (x ≥ 1), which both tests apply identically.

Row (iii)'s prose is thus correct in spirit under the additive reading on I at
full magnitude, correct in mechanism under the replace reading — but the exact
statement is two-theorem, reading-conditional, and depth-dependent, not the
unconditional "collapses into common rejection" of the current table cell.

## 6. The relevance test — all four components (the σ-wave standard)

(i) **A named ecological decision.** Whether a composite biomass index may
certify a stock-rebuilding transition (Northern-cod-style, the Section 6.3
benchmark) when the assessment's disturbance class is a shared environmental
shock — a marine heatwave striking the SAME biomass coordinate regardless of
which harvest-rebuild plan is running — rather than plan-specific risk. This is
Table 5 row (ii) applied at the canonical datum: the dashboard either may or may
not license the transition, and the checklist's sixth audit point demands the
class be specified.

(ii) **Changes what an actual indicator reports.** Yes, on two exact surfaces.
The 1/2-cut: any action-indexed gap state with min(s) < 1/2 flips its
compensatory verdict from ACCEPT to REJECT (e.g. (1/2, 1/10, 19/10)); an index
that certified "aggregate above 2, transition licensed" now reports rejection.
The rescue margin: on {min(s) < 3/8} the reported κ* changes from a finite
reserve requirement to ∞ — "rescuable with reserve κ*" becomes "not rescuable
by any reserve" (Theorem M2).

(iii) **A new exact witness datum.** The common-shock variant itself: FP_cs and
its 1/2-cut, the 3/8 rescue boundary, the licensing-invariance identity, the
5/4 coupled boundary with its 79/40 witness, the 11/2 relocation gap, and
Theorem CT's collapse — all exact rationals, machine-anchored, 77/77 checks,
byte-reproducible log.

(iv) **Alters at least one management action.** Yes. At an asymmetric gap state
(min(s) < 1/2) the action-indexed prescription — accumulate bridge reserve to
x = 1 (κ* = (1−x)+) — is replaced under a shared-shock assessment by a
floor-targeted action: rebuild the weaker floor above 1/2 first (above 3/8 for
the staged route), because no reserve increment alone certifies (κ* = ∞).
Reserve accumulation and floor rebuilding are different management actions with
different costs and timescales. Second action flip: on the fragile band
sum ∈ [2, 5/2), blended quota policies (Theorem 9's convexification) are NOT
admissible under a shared shock — an agency that would otherwise blend FAST and
SLOW shares at such a state must not (Theorem M3).

All four components pass. The middle cell's verdict is ecologically load-bearing,
not merely formal.

## 7. Honest limits and scope

- Everything is on the witness datum's decomposition (tent events, exact tubes,
  the specific STAGED mechanics, the Section 6.3 arithmetic); no claim about
  other data beyond the δ-family verified.
- The two regime-(iii) readings (additive/replace) bracket the coupled truth;
  Theorem CT is reading-conditional, and the record states both rather than
  choosing.
- Grid verification is fail-loud but finite; the closed forms carry proofs
  (affine interval arithmetic; the kink lemma), and the two were cross-checked
  against each other at every grid point — the standard the σ-wave set.
- κ* under the common class is adjudicated on a k-grid with step 1/40 plus
  closed-form confirmation on the survivors; the ∞ verdict on {min(s) < 3/8}
  is proved structurally (the event exposure of a growing floor is
  max(0, δ−1/8) ≥ 3/8 > any floor below 3/8 can carry), not merely sampled.
- No stochastic, partial-observation, or infinite-horizon claim is made; the
  disturbance quantifier remains innermost throughout (the manuscript's
  Section 2.2 discipline).

## 8. What a future manuscript round can transcribe (owner-gated; additive only)

For a future v54 (all additive; nothing removed or condensed; owner-gated per
the standing plan protocol):

1. **Fill Table 5's middle cell** with the computed verdict (Theorem M1):
   the gap survives, reduced by the exact 1/2-cut, thresholds unshifted on the
   surviving region; cite this record.
2. **§5.7 addition** (Theorem M2): the rescue trichotomy and the first
   unrescuable-by-reserve failure states on this datum.
3. **Theorem 9 discussion addition** (Theorem M3): the class-conditional blend
   fragility — the common-shock gap is not blend-closed on sum ∈ [2, 5/2).
4. **§5.4 row-(iii) refinement** (Theorems M4 + CT): depth-dependence with the
   exact 5/4 boundary, the relocation at full magnitude, and the replace-reading
   collapse stated precisely (V_weak = V_typ; the mechanism; the strictly-more-
   demanding witness (1/2, 3, 1)).
5. Optionally (the largest item): a labelled-extension subsection "the
   common-shock variant of the witness" transcribing Theorems M1–M4 + CT with
   the machine-verification pointer, mirroring §5.8's labelled-extension format.

## 9. Reproduction

```
cd "batch 8/middle_regime_wave"
python3 middle_regime_verify.py        # exit 0; 77/77; ALL CHECKS PASS
```

Byte-identical reruns (verified); the committed `middle_regime_run_log.txt` is
the captured passing run. Python 3, standard library only, `fractions.Fraction`
exclusively.

---

*Standing rules honored: new files only (the verifier and this record are the
wave's creations; the run log the committed evidence); no existing repository
file modified; no content removed or condensed; the witness manuscripts remain
read-only consistency references.*

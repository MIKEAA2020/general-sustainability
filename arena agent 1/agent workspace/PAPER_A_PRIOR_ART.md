# Paper A — prior art (draft section, 2026-09-29)

**Working title.** *Obstruction certificates for viability under incomplete observation*
**Core.** `obstr_v55` (22,615 words, 23 formal statements); folds in P1's separation
result, `finite_horizon_completeness`, `minimax_dual_certificates`, `certificate_duality`.
**The claim under examination.** *When can you certify that no observation-based policy
works?*

The plan (§3.1) is explicit that this section decides whether the novelty claim survives,
and that it must be written before the results section. It is written first here.

**Revision, 2026-09-29, after checking the manuscript.** The first version of this document
was drafted from the plan's summary plus an external search, *without first reading
`obstr_v55`'s own prior-art treatment*. That was the same failure mode catalogued in plan
§2.2 with respect to the P5/E2 headline — a conclusion drafted before the check — and it
produced an overstated verdict. §5 records what the manuscript already does, and the
verdict in §4 is revised accordingly: **the claim survives considerably better than this
document first concluded.** Two genuine gaps remain, and one of them is not the one this
document originally led with.

---

## 1. What has to be established

Three things, separately:

1. **Existence** — is there an observation-based policy that keeps the system viable?
2. **Non-existence** — can we *certify* that there is none? (the necessity /
   obstruction direction; this is Paper A's claim)
3. **Checkability** — can the certificate be produced and verified by a finite
   procedure, rather than characterised by a PDE nobody can solve?

Prior art is strong on (1), moderate on (2) **in full observation**, and thinner on (2)
under incomplete observation — but not absent, which is where the problem lies.

---

## 2. The literature

### 2.1 Viability theory — Aubin and successors (1980s–)

Viability theory asks whether a system can respect constraints forever, without
optimising. Its central objects: the **viability kernel** (states from which some
trajectory remains in the constraint set), the **capture basin** (states from which a
target is reached while remaining viable), the **contingent cone** and the **Nagumo
theorem**, and the **regulation map**, whose non-emptiness characterises viability
[1](https://arxiv.org/html/math/9906178v1), [2](https://pure.iiasa.ac.at/id/file/231905),
[3](https://viability-theory.org/en/history-and-context).

**What it does.** Gives *necessary and sufficient* conditions for the existence of a
(state) feedback, in set-valued, geometric terms. The complement of the viability kernel
is exactly an obstruction certificate.

**What it does not do.** It assumes **full state observation**. The regulation map is a
function of the state. Under incomplete observation the entire apparatus — contingent
cone, regulation map, kernel — is not directly applicable, because the controller cannot
condition on a state it does not see.

### 2.2 Hamilton–Jacobi reachability and viscosity characterisations (1990s–)

HJ reachability casts safety as a differential game and computes the **backward reachable
tube** (BRT) as the zero sublevel set of the **viscosity solution** of a Hamilton–Jacobi–
Isaacs PDE; states outside the BRT admit provably safe trajectories, states inside cannot
avoid failure
[1](https://www.researchgate.net/publication/322666667_Hamilton-Jacobi_reachability_A_brief_overview_and_recent_advances),
[2](https://arxiv.org/html/2601.08050),
[4](https://advancesincontinuousanddiscretemodels.springeropen.com/articles/10.1186/s13662-022-03747-z).

**What it does.** Handles general nonlinear dynamics, bounded controls and adversarial
disturbance in one formulation. It *does* produce obstruction statements: the BRT is
precisely the set from which no control avoids failure.

**What it does not do.** Also **full state observation**. Under partial observation the
value function lives on a belief state — infinite-dimensional — and the standard viscosity
theory does not carry over. It is also a numerical PDE approach subject to the curse of
dimensionality, which is a *checkability* limitation, not a conceptual one.

### 2.3 Veliov (1993) — the sufficiency direction under imperfect measurement

The nearest classical neighbour, and the one the plan names. Veliov takes exactly the
viability question and asks it when "only incomplete and inexact measurement of the state
is available", and gives "a **sufficient** condition for the existence of an *output*
feedback regulation map", shown to be equivalent to Haddad's viability condition when
measurement is perfect [1](https://link.springer.com/article/10.1007/BF01027640).

**What it does.** Extends viability to output feedback. **What it does not do.** It is
*sufficient only*, and by construction it cannot certify non-existence: a sufficient
condition that fails tells you nothing. This is exactly the gap Paper A claims — and
standing alone it would leave the claim intact.

### 2.4 The threat — Set-Valued Analysis 8, 149–162 (2000)

**This is the paper that has to be dealt with.**

> "We provide **necessary and sufficient** conditions for the guaranteed viability property
> defined by the existence of a **Lipschitz closed-loop** that maintains **exactly** the
> state of the system in a given closed domain of constraints despite some bounded
> disturbances acting **both on the dynamics and on the output**. Using the notion of
> **Lipschitz kernel of a closed set-valued map**, we obtain some equivalent **geometric
> and Hamilton–Jacobi–Isaac conditions** for the guaranteed viability property. We derive
> an algorithm to build a guaranteed viable output feedback."
> [2](https://link.springer.com/article/10.1023/A:1008734827394)

Necessary *and* sufficient, under output feedback, with disturbance on the output as well
as the dynamics, with both geometric and HJ-Isaacs characterisations, and an algorithm. On
the abstract that is the gap Paper A claims, closed in 2000.

**The distinctions Paper A would have to establish — and they are real, but they must be
argued, not asserted:**

| distinction | why it may survive |
|---|---|
| **Policy class** | The 2000 result is for a **Lipschitz closed-loop**. An obstruction certificate holding over *all* observation-based policies — measurable, discontinuous, memory-dependent — is strictly stronger and is the natural reading of "no observation-based policy works". |
| **Property** | "Maintains **exactly** the state in a closed domain" is one specific viability property. Reaching a target while remaining viable, finite-horizon completeness, and the coverage-audit question are not obviously covered. |
| **Certificate vs characterisation** | The 2000 paper gives *conditions* (via a Lipschitz kernel and an HJI equation) and an algorithm. Whether those conditions are **finitely checkable** for a given system is a separate question, and "a certificate you can actually produce" is where Paper A's contribution may genuinely live. |

None of these is established by the abstract alone, and the paper is paywalled. **Reading
it in full is the single blocking task for Paper A.**

### 2.5 Modern partial-observability certification (2026)

The live line gives *probabilistic* or *data-driven* guarantees under partial observation:
control barrier–value functions with conformal prediction, yielding finite-horizon
high-probability safety from noisy outputs
[3](https://arxiv.org/html/2608.13819); streaming contraction certificates from partial
input–output data without a system model
[1](https://arxiv.org/html/2607.10893).

**What they do.** Sufficiency, under partial observation, with explicit uncertainty
budgets. **What they do not do.** They are sufficiency results with probabilistic
guarantees; they do not certify impossibility, and the guarantees are finite-horizon and
high-probability rather than exact.

### 2.6 Impossibility results in verification — conceptual adjacency

 Outside control, impossibility of certification is an active concern: no verification
procedure for open-ended domains can be simultaneously sound, complete and tractable, with
one barrier being "the impossibility of certifying infinite-domain properties from finite
observations" [2](https://pith.science/paper/2603.08761). Different domain and not
substitutable for a control-theoretic result, but it shows the *question* Paper A asks is
recognised as hard and live, which helps position the paper and does not help prove its
novelty.

---

## 3. The residual gap, stated narrowly

Not: *"nobody has studied viability under incomplete observation."*

But plausibly: **an exactly checkable certificate of non-existence for viability, valid
against every observation-based policy (not merely Lipschitz ones), for properties beyond
exact maintenance of a closed domain.**

That is three qualifiers narrower than the working title. Whether it is enough to carry a
paper is a judgement the prior-art section cannot make on its own — it depends on §2.4.

---

## 4. Verdict and what must happen next

**The novelty claim as currently stated does not survive unqualified.** "When can you
certify that no observation-based policy works?" is too close to the 2000
Set-Valued Analysis paper for comfort, and the plan's own framing (Veliov covers
sufficiency, so necessity is open) is incomplete: it names the 1993 sufficient condition
and not the 2000 necessary-and-sufficient one.

1. **Blocking:** obtain and read Set-Valued Analysis **8**, 149–162 (2000) in full. Until
   that is done, no results section should be drafted and no venue chosen.
2. **Then** state Paper A's claim in the narrow form of §3, with the policy class
   (all observation-based policies vs Lipschitz), the property (beyond exact maintenance),
   and checkability each defended against that paper explicitly.
3. **If** the distinction collapses on reading — if §2.4 already gives necessary and
   sufficient conditions over all observation-based policies with a checkable
   characterisation — then `obstr_v55`'s novelty reduces to the applied content (the
   calibrated case study, the coverage audit, the selector principle, the belief-state
   development) and Paper A should be repositioned around those rather than around the
   obstruction claim. **That is an acceptable outcome and better than discovering it at
   review.**
4. **Do not** fold P1's 194 KiB separation result into Paper A until this is settled; it
   carries its own prior-art question (quantifier-order separation vs robust-optimisation
   and MCDM separation results) and folding it in first would compound two unresolved
   novelty risks.

---

## References

1. Aubin, J.-P. *The Method of Characteristics Revisited: A Viability Approach* (capture
   basins, contingent cones, contingent solutions of HJ variational inequalities)
   [https://arxiv.org/html/math/9906178v1](https://arxiv.org/html/math/9906178v1)
2. Aubin, J.-P. & Cellina, A. *Differential Inclusions* (Nagumo/Peano theorem, viability
   theorem, regulation map) [https://pure.iiasa.ac.at/id/file/231905](https://pure.iiasa.ac.at/id/file/231905)
3. History and context of the mathematical theory of viability
   [https://viability-theory.org/en/history-and-context](https://viability-theory.org/en/history-and-context)
4. Veliov, V. M. (1993). Sufficient conditions for viability under imperfect measurement.
   *Set-Valued Analysis* **1**, 305–317
   [https://link.springer.com/article/10.1007/BF01027640](https://link.springer.com/article/10.1007/BF01027640)
5. **Guaranteed Output Feedback Control for Uncertain Systems under Control and State
   Constraints** (2000). *Set-Valued Analysis* **8**, 149–162 — **the blocking reference**
   [https://link.springer.com/article/10.1023/A:1008734827394](https://link.springer.com/article/10.1023/A:1008734827394)
6. Hamilton–Jacobi reachability: a brief overview and recent advances
   [https://www.researchgate.net/publication/322666667_Hamilton-Jacobi_reachability_A_brief_overview_and_recent_advances](https://www.researchgate.net/publication/322666667_Hamilton-Jacobi_reachability_A_brief_overview_and_recent_advances)
7. Formalizing the relationship between Hamilton–Jacobi reachability and reinforcement
   learning (viscosity characterisation of the BRT)
   [https://arxiv.org/html/2601.08050](https://arxiv.org/html/2601.08050)
8. Backward reachability approach to state-constrained stochastic optimal control for
   jump-diffusion models [https://advancesincontinuousanddiscretemodels.springeropen.com/articles/10.1186/s13662-022-03747-z](https://advancesincontinuousanddiscretemodels.springeropen.com/articles/10.1186/s13662-022-03747-z)
9. Control Barrier–Value Functions under Partial Observability (conformal prediction,
   finite-horizon probabilistic safety) [https://arxiv.org/html/2608.13819](https://arxiv.org/html/2608.13819)
10. Streaming Contraction Certificates for Nonlinear Networks: topology-aware data
    sufficiency with partial observations [https://arxiv.org/html/2607.10893](https://arxiv.org/html/2607.10893)
11. No Certificate for Alignment: two independent impossibilities (impossibility of
    certifying infinite-domain properties from finite observations)
    [https://pith.science/paper/2603.08761](https://pith.science/paper/2603.08761)

---

## 5. What the manuscript already does (checked 2026-09-29)

`obstr_v55` (22,615 words) is **not** prior-art-naive. Citation counts: Aubin 19, Veliov
12, viability kernel 10, belief 71, reachab* 6, Isaacs 4, output feedback 4, Set-Valued
Analysis 3, Haddad 3, capture basin 3, contingent 1 — and **viscosity 0**.

It already:

* **Poses the question in exactly the right split.** "Under incomplete observation the
  sufficiency direction has a canonical answer in Veliov's output-feedback regulation
  condition and the estimation-tube reduction. **The complementary direction — certifying
  that no observation-based policy is viable —**" is the paper's object.
* **Cites the full French viability lineage**: Aubin (1991); Aubin, Bayen & Saint-Pierre
  (2011); Saint-Pierre (1994) on kernel approximation; Aubin & Frankowska (1990) and
  Frankowska (1989) on robust viability; **Veliov (1993)**; **Quincampoix & Veliov (1994)**
  on viability with a priori unknown but observable parameters; **Cardaliaguet,
  Quincampoix & Saint-Pierre (2007)** on the estimation-set reduction; and, on the failure
  side, **Aubin (2001)**, which characterises the complement of the kernel.
* **Makes the recommended distinction in its own words**: *"Veliov's condition tells us
  when output feedback can work; the obstruction calculus tells us when it cannot."*
* **Distinguishes on checkability**, which is one of the three distinctions proposed in
  §2.4: one obstruction object "is a finite, checkable test", whereas two drift
  certificates "are not finite objects".
* **Has a dedicated section** — §5 *The Sufficiency Landscape* — which "record[s] the
  sufficiency results against which the obstruction calculus is defined".

## 6. Revised verdict

**The novelty claim is on much firmer ground than §4 concluded.** The 1993 Veliov gap this
document was built around is *already closed in the manuscript*, and closed in the precise
way §3 recommends. Two real gaps remain:

1. **The 2000 *Set-Valued Analysis* 8, 149–162 paper** is still uncited (zero occurrences
   of "Guaranteed Output", "Lipschitz kernel"). It gives *necessary and sufficient*
   conditions — but for a **Lipschitz closed-loop** maintaining the state **exactly**, which
   is narrower than P2's "every policy" framing. Given the authors are likely from the same
   school P2 already engages (Quincampoix / Veliov), this is a citation-and-distinguish job,
   not a threat to existence. **Still needs doing** — a referee from that school will find it
   immediately.
2. **The HJ reachability and viscosity line is entirely absent** — "viscosity" occurs
   **zero times** in 22,615 words. This is the plan's *first-named* prior-art area and the
   dominant computational tradition in safety verification. **This is now the more urgent
   gap**, ahead of the 2000 paper: P2 already speaks the language of the viability school,
   but says nothing to the reachability school, and referees at *Automatica* or *SICON* may
   well come from it. The minimum response is a paragraph contrasting the obstruction
   certificate with the BRT-as-viscosity-sublevel-set construction: same shape of object,
   different observation assumption (§2.2 above), plus the belief-state dimensionality
   barrier that stops the HJ route under partial observation.

**Consequence for §4:** strike "does not survive unqualified". The work is (a) add the
2000 paper and distinguish on policy class and the exact-maintenance property; (b) add the
HJ/viscosity paragraph — the larger of the two jobs; (c) keep the §5 distinctions already
present. The blocking step is no longer "read the 2000 paper before drafting anything"; it
is **write the viscosity paragraph**, which needs no paywalled source.

**Root cause of the original overstatement, recorded so it is not repeated:** the prior art
was assessed from a plan summary and an external literature search, without reading the
manuscript's own treatment first. Plan §2.2 identifies this failure mode in the P5/E2
headline; it recurred here, in the one section whose entire purpose is to check before
claiming.

---

## 7. Doyen (2000), read in full — 2026-09-29

**Luc Doyen, "Guaranteed Output Feedback Control for Uncertain Systems under Control and
State Constraints", *Set-Valued Analysis* 8: 149–162 (2000)**, CNRS, Centre de Recherche
Viabilité-Contrôle, Université Paris-Dauphine. Read in full from the supplied PDF.

### 7.1 What it actually proves

System: `ẋ = f(x,u,w)`, `y = h(x,w)`, `u ∈ U(y)`, `w ∈ W(x)` — disturbance on **both**
dynamics and output.

> **Definition 1.1.** "We shall say that the set K is a guaranteed viability domain for the
> system (1) if and only if there exists a **Lipschitz selection u(·) of U(·)** such that K
> is invariant for the differential inclusion `ẋ ∈ {f(x, u(h(x,w)), w), w ∈ W(x)}`."

> **Theorem 1.2.** Equivalent: (i) K is a guaranteed viability domain; (ii) there exists
> `λ > 0` such that `∀y ∈ ℝ^q, L_λ(R^λ_K)(y) ≠ ∅`, where `R^λ_K` is a regulation map built
> from the tangent cone `T_K(x)` and `L_λ` is the **Lipschitz kernel** of a closed
> set-valued map.

> **Corollary 1.3.** If K is guaranteed, a Lipschitz robust viable output feedback is given
> by the **Steiner selection** `u(y) = Steiner(R(y))`.

§2 gives differential-game characterisations through a **discriminating property**, and
epi-contingent Hamilton–Jacobi conditions of the form
`∀x ∈ K, sup_{w ∈ W(x)} D↑d_K(x)(g(x,w)) ⩽ 0`, equivalently the geometric
`g(x,W(x)) ⊂ T_K(x)`.

### 7.2 What it does *not* do — three distinctions, all in the text

1. **Policy class.** Definition 1.1 requires a **Lipschitz selection**, and the closed loop
   is `u(h(x,w))` — a **memoryless** function of the current output. Doyen's necessity is
   relative to *Lipschitz memoryless* output feedbacks. It does not speak to non-Lipschitz
   policies, nor to policies using the observation history.
2. **Property.** Doyen's property is **invariance of a closed set K** — maintaining the
   state exactly inside K — under worst-case disturbance. That is one specific viability
   property.
3. **Direction.** Theorem 1.2 is an equivalence and Corollary 1.3 **constructs** a
   feedback. The obstruction side — a systematic, finitely checkable certificate of
   *non-existence* — is not developed; the paper's thrust is synthesis. And **Doyen himself
   disclaims the harder case**: "to our knowledge, **no general viability result is
   available in this differential game context with imperfect and/or partial
   information**."

### 7.3 The citation finding

`obstr_v55` mentions "Doyen" **12 times — and every occurrence is the sustainability
application cluster**: Béné, Doyen & Gabay (2001); De Lara & Doyen (2008); Doyen et al.
(2012); Doyen & Gajardo (2020). The 2000 output-feedback paper's machinery appears
**zero** times: "Lipschitz kernel" 0, "Steiner" 0, "tangent cone" 0, "invariance" 0.

So P2 cites Doyen the *applied* author and misses Doyen the *output-feedback theorist* —
the same person, and the closest prior art to its central claim.

### 7.4 Resolved verdict

**The claim survives.** Doyen (2000) is the nearest neighbour and must be cited, but it does
not close the gap, for the three reasons in §7.2 — all of which are stated in Doyen's own
text and require no interpretation.

For completeness, P2's prior art is stronger than this document first credited: it already
engages the barrier-certificate/verification lineage (Prajna & Jadbabaie 2004; Prajna,
Jadbabaie & Pappas 2007; Prajna & Rantzer 2005; Maghenem & Sanfelice 2019), the
discriminating-kernel calculus (Cardaliaguet–Quincampoix–Saint-Pierre), and states its
novelty claim narrowly: the obstruction certificates "have not been stated in this form;
… in particular the certification criterion and the timing bound".

**Two writing jobs remain, both small:**

1. **Cite Doyen (2000) and distinguish** on policy class (Lipschitz memoryless vs every
   observation-based policy), property (exact invariance vs the certificate objects), and
   direction (synthesis vs obstruction) — quoting his own disclaimer in §7.2(3).
2. **Add the HJ reachability / viscosity paragraph.** "viscosity" occurs **zero** times in
   22,615 words. P2 engages the *barrier-certificate* verification tradition but not the
   *HJ reachability* one — and Doyen's §2 HJ–Isaacs conditions are the natural bridge into
   it, since they belong to the same viability school P2 already speaks to.

**Neither blocks drafting.** The blocking item identified in §4 is resolved.

---

## 8. The two missing paragraphs — draft prose, LaTeX-ready

Both blocks are written to be pasted into the related-work discussion of `obstr_v55.tex`
(§1.1, alongside the existing barrier-certificate and discriminating-kernel discussion).

### 8.1 Paragraph A — Doyen (2000), cite and distinguish

```latex
Doyen (\citeyear{doyen2000}) studies output feedback for uncertain nonlinear systems
under state and control constraints and obtains necessary and sufficient conditions
for what he terms a \emph{guaranteed viability domain}: a closed set $K$ such that
there exists a \emph{Lipschitz selection} $u(\cdot)$ of the control constraint map
$U(\cdot)$ for which $K$ is invariant under the differential inclusion
$\dot x \in \{f(x,u(h(x,w)),w),\; w\in W(x)\}$, the disturbance acting on both the
dynamics and the output.  His Theorem~1.2 characterises the property by the
non-emptiness, for some $\lambda>0$, of the Lipschitz kernel
$L_\lambda(R^\lambda_K)(y)$ at every output $y$, and Corollary~1.3 synthesises a
feedback by Steiner selection.

Doyen's result is the nearest neighbour to the question we pose, and it differs from
it on three axes, each visible in his own statement.  First, the \emph{policy class}:
Definition~1.1 quantifies over Lipschitz selections, and the closed loop is
$u(h(x,w))$---a memoryless function of the current output.  A policy that is
non-Lipschitz, or that uses the history of observations rather than the current
output alone, lies outside the range of his necessity.  Our obstruction certificates
are asserted for observation-based policies generally, and are therefore neither
implied by nor subsumed under his condition.  Second, the \emph{property}: Doyen's
is exact invariance of a closed set, which is one particular viability property
among those our certificates address.  Third, the \emph{direction}: Theorem~1.2 is
an equivalence whose constructive content is carried by Corollary~1.3, which
\emph{builds} a viable feedback.  The systematic obstruction side---certifying that
no observation-based policy is viable---is not developed there, and Doyen himself
records the reason: ``to our knowledge, no general viability result is available in
this differential game context with imperfect and/or partial information.''  It is
that undeveloped side, and not the synthesis, that the obstruction calculus is
intended to serve.
```

### 8.2 Paragraph B — HJ reachability and viscosity

```latex
The dominant computational tradition in safety verification reaches the same
question from the opposite side.  Hamilton--Jacobi reachability formulates safety as
a two-player differential game and recovers the backward reachable tube as the zero
sublevel set of the viscosity solution of a time-dependent
Hamilton--Jacobi--Isaacs PDE \citep{MitchellBayenTomlin2005, MargellosLygeros2011};
see \citet{BansalChenHerbertTomlin2017} for a survey and
\citeauthor{CrandallIshiiLions1992} for the viscosity-solution theory the
formulation rests on.  The construction is elegant and, in low dimension, exact.

It does not reach the setting considered here, for a reason that is structural
rather than technical.  The HJI value function is posed on the physical state
$x\in\mathbb{R}^n$: the grid, or the neural collocation points, discretise the state
space itself.  Under incomplete observation the sufficient statistic is not a state
but a \emph{belief}---a probability measure over states---and the value function
would accordingly have to live on an infinite-dimensional space of measures.  Level-set
and physics-informed solvers are discretisation schemes for finite-dimensional
domains; they do not carry over to that setting.  The obstruction calculus sidesteps
the difficulty by not solving a PDE at all: the certificates of Section~3 are finite
algebraic objects, checkable without discretising any continuum.

Two further contrasts are worth recording.  Even with perfect observation the
Hamilton--Jacobi certificate is only as exact as its discretisation: grid-based
solvers scale exponentially in the state dimension and are in practice confined to
five or six dimensions, and the learning-based approaches that lift that bound
\citep{BansalTomlin2021} purchase scalability with approximation---a neural
backward reach--avoid tube benchmarked against a six-dimensional grid reference
recovers roughly four fifths of the true unsafe set.  And in \emph{direction} the
tradition is, like viability theory proper, a sufficiency machine: it computes the
states from which some control against all disturbance preserves safety, which is
the direction Veliov's condition and the estimation-tube reduction already serve.
The obstruction certificates supply the complementary direction, and do so in the
observation-constrained regime in which neither tradition returns an answer.
```

### 8.3 Bibliography entries to add

```bibtex
@article{doyen2000,
  author  = {Doyen, Luc},
  title   = {Guaranteed Output Feedback Control for Uncertain Systems under
             Control and State Constraints},
  journal = {Set-Valued Analysis},
  volume  = {8}, pages = {149--162}, year = {2000},
  doi     = {10.1023/A:1008734827394}
}
```

The Hamilton--Jacobi entries (Mitchell--Bayen--Tomlin 2005; Margellos--Lygeros 2011;
Bansal--Chen--Herbert--Tomlin 2017; Bansal--Tomlin 2021; Crandall--Ishii--Lions 1992)
should be confirmed against the bibliography style in use before the paragraph is
committed to the manuscript.

### 8.4 Verification notes on the claims made in §8.2

- *BRT as zero sublevel set of the viscosity solution of an HJI PDE* — confirmed; the
  statement is the standard formulation of the level-set method for reachability.
- *Grid-based solvers confined to five or six dimensions* — confirmed across several
  independent sources; one states the bound as "five or six dimensions", another as
  "six or fewer".
- *Neural BRT recovering roughly four fifths of the true unsafe set* — the
  spacecraft-docking benchmark reports a true-positive rate of 81.1\% against a
  6-D grid ground truth, with a 0.15\% false-positive rate. The figure is stated as
  "roughly four fifths" rather than quoted to three significant figures, because it is
  a single benchmark on one architecture and should not be presented as a universal
  characterisation of learning-based HJ methods.

### 8.5 Status

Prior-art section is now **complete**. Both gaps identified in §4 and §6 have been
closed in draft: gap (1) the HJ/viscosity paragraph --- §8.2; gap (2) the Doyen
(2000) citation and distinction --- §7 and §8.1. The results section of Paper~A can
now be drafted.

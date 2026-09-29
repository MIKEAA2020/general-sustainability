# Paper A — prior art (draft section, 2026-09-29)

**Working title.** *Obstruction certificates for viability under incomplete observation*
**Core.** `obstr_v55` (22,615 words, 23 formal statements); folds in P1's separation
result, `finite_horizon_completeness`, `minimax_dual_certificates`, `certificate_duality`.
**The claim under examination.** *When can you certify that no observation-based policy
works?*

The plan (§3.1) is explicit that this section decides whether the novelty claim survives,
and that it must be written before the results section. It is written first here. **The
headline finding is that the claim as stated does not survive unqualified**, and the reason
is a specific paper, identified in §2.4.

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

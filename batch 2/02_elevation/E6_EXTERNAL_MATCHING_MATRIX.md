# E6 — External Matching Matrix (Internal Best-Effort; Audit NOT Executed)

**Provenance:** reconstructed and expanded after the filesystem loss of the long-form original (session worklog Task 3; expansion recorded in TRANSFER_AUDIT_RESPONSE Finding 1).

**Mandatory status:** every entry below is **internal-best-effort** — the nearest-known-type identifications were made from the programme's internal knowledge of the six literatures, **not** from a systematic external audit. The external novelty audit (G5/F1) is **NOT DONE**; this matrix is its *agenda*, not its result. No novelty claim anywhere in the programme may rest on this file.

---

## The matrix

Columns: **NKT** = nearest known type in the external literature (internal best-effort identification); **Δ** = the delta between our result and the NKT (what would be new *if the identification is confirmed*); **Action** = the concrete verification action the external audit must perform.

### 1. Robust DP / reachability (Aubin–Bayen, Bokanowski–Zidani, Bertsekas, Mitchell level sets)

| Ours | NKT | Δ | Action |
|---|---|---|---|
| B3 Operator II backward recursion with exact tubes (packet) | Viability-kernel / capture-basin dynamic programming (Aubin's Viability Kernel algorithm; level-set HJ reachability) | Finite-architecture, fixed-review, *exact-tube* discretization discipline + typed disturbance/review semantics | Compare against Bokanowski–Zidani error bounds for reachability under state constraints; check whether the "exact tube at finite review depth" claim appears |
| C4.2 uniform-horizon theorem | Compactness arguments in finite-horizon reachability termination | The uniform-exit-horizon form as a *diagnostic soundness* statement (tied to certification, not just termination) | Search termination/uniform-horizon results in HJ reachability |
| C-a.Thm2 decidability at fixed data | Complexity results for finite-state/game reachability (model checking) | The judgment-language (8 families, TCS-1.0 §4) typing and the O(N·|grid|) bound *per sentence including negations* | Check against game-solving complexity literature; the typing is the candidate delta |

### 2. Viability theory (Aubin, Frankowska, Quincampoix; Saint-Pierre)

| Ours | NKT | Δ | Action |
|---|---|---|---|
| Packet B1 strong invariance + conditional tubular erosion | Nagumo/tangential conditions; invariance theorems (Aubin's *Viability Theory* ch. 5–6); proximal-normal invariance (Clarke–Ledyaev–Stern–Wolenski) | The **erosion bookkeeping** (`L_G r + Δ ≤ α`) wired into the certificate status discipline | Check whether erosion-as-status-discipline (not just a lemma) appears in viability monographs |
| E2.B1(a)/(b) certificate gfp = backward iteration | Viability kernel as the largest closed invariant... the kernel *is* a gfp; standard | The **(REG)-certificate-family** packaging (certificates as first-class objects with status) | Search "viability kernel" + "certificates"; the packaging is the candidate delta, the fixed-point mathematics is classical |
| E2.B2(a) measurable selection for safe-action maps | Kuratowski–Ryll-Nardzewski applications to viability/regulation (Quincampoix's measurable selection results) | Essentially none expected — **re-instantiation risk**: E2.B1 may be a re-derivation of known selection-for-viability results | **Highest-priority check**: Quincampoix (1992ff) on measurable viable controls; if identical in scope, E2.B1 must be re-labelled "known, re-proved" |

### 3. Hybrid safety (Lygeros–Tomlin–Sastry; Alur–Henzinger; event-bookkeeping)

| Ours | NKT | Δ | Action |
|---|---|---|---|
| B1 sampled-data erosion theorem | Inter-sample safety in sampled-data control (e.g., Nesic–Teel; sampled-data HJ) | The **three-hypothesis certificate form** (envelope inclusion + inter-sample confinement + successor certificates) closing R02.Cor6 | Compare sampled-data safety certificates; the bridge form is the candidate delta |
| A3 interleaved-segment compactness + clopen-fibre kernel | Hybrid trajectory spaces (segment topologies); quantized-observation safety | The **budgeted piecewise-history space** with interleaved-segment topology; clopen-fibre kernel closure | Search "piecewise history space" compactness; the budgeted class is the candidate delta |
| E4 generation transfer | Multi-mode/multi-shot invariance; hybrid jumps' invariance | The **depth co-Lipschitz jump margin as declared data** + the refutation showing it is not derivable | Check jump-invariance conditions in hybrid viability (Aubin–Haddad type); the non-derivability witness is the candidate delta |

### 4. ISS / small-gain (Sontag, Jiang–Teel–Wang, Dashkovskiy et al.)

| Ours | NKT | Δ | Action |
|---|---|---|---|
| R05.Thm1/2 contract-amplitude composition (linear case) | Linear ISS small-gain (matrix small-gain condition `ρ(Γ) < 1`) | The **contract-amplitude/erosion form** (deficit budgets `δ_ij`, margins `α_i`) rather than gain functions | **Priority-one audit row**: compare against vector Lyapunov/small-gain formulations; the deficit-budget form may coincide with known vector-Lyapunov conditions |
| A4 monotone-operator assume–guarantee (nonlinear) | Nonlinear ISS small-gain (max-form gain composition; Dashkovskiy–Rüffer) | The **lattice-theoretic contract form** (Tarski greatest sub-solution, monotone iteration, no gain-function algebra) + the shared-control sharpness witness | Compare against max-form small-gain: the shared-control nonconvexity witness (A4.Ex3) has no obvious ISS counterpart — candidate delta; the existence theorem itself is likely close to known fixed-point small-gain proofs |
| E7/C-e moiety barriers | Material-balance/stock-flow safety in process control | The **sandwich from flux data alone** + noncompensatory multi-moiety form | Search conservation-based barrier certificates (chemical process safety); the noncompensation tie to Farkas is the candidate delta |

### 5. Moment closure / aggregation (population dynamics, Kuehn's moment closure)

| Ours | NKT | Δ | Action |
|---|---|---|---|
| R06.Lem1/Thm3 + C3 closure classification | Exact moment closure literature (Kuehn; Visser–Bentley); projectability conditions | The **fibre-constancy iff** as an exact classification + the non-atomic theorem + the two-patch quadratic positive case | Search "exact moment closure conditions"; the two-patch closure `ṁ = m² + v, v̇ = 4mv` is elementary — likely known in two-moment closure literature; the classification form is the candidate delta |
| C-f RFDE-aggregate memory | Delay-equation model reduction (reduced-order DDE) | The **memory-horizon characterization** (`τ̃ < τ` iff projection collapses the relevant dependence) | Search DDE model reduction; the fibre-lifted criterion is the candidate delta |

### 6. Axiomatic frameworks (formal methods specification, assume–guarantee)

| Ours | NKT | Δ | Action |
|---|---|---|---|
| E1.A2 relative completeness (5 rules, U/M inventory) | Assume-guarantee rule soundness/completeness results (Jones; Misra–Chandy; ALASS) | The **sustainability-judgment calculus** over the TCS-1.0 inventory with status discipline | Compare compositional reasoning calculi; the judgment typing + status field is the candidate delta |
| A4 assume–guarantee via Tarski | Circular assume-guarantee fixed points (Fixpoint/ω-regular AG rules) | The **erosion-depth contract lattice** (contracts are *numbers*, not propositions) | Search quantitative/circular AG; numeric-contract AG is the candidate delta |
| TCS schema discipline (1.0/1.1) | Versioned specification languages (Z, Alloy schemas) | The 17-field record + mapping-type registry as *mathematics* infrastructure | Not a novelty claim — infrastructure |

---

## Priority ordering for the external audit

1. **R05 vs linear ISS/small-gain** (row 4.1) — the risk that the linear composition theorem is a re-statement of vector-Lyapunov small-gain is the single largest exposure for Paper 2.
2. **E2.B1 vs Quincampoix's selection-for-viability** (row 2.2) — re-instantiation risk, flagged above.
3. **A4 vs nonlinear ISS small-gain** (row 4.2) — the existence theorem may be close to known; the sharpness witness is the defensible delta.
4. **C3 vs moment-closure literature** (row 5.1) — the two-patch example is likely folklore; the classification theorem is the claim to check.
5. Rows 1.x, 3.x, 6.x — lower risk (typing/packaging deltas, honestly labeled).

**Output protocol:** each row must come back from the external audit as {confirmed-new | known-equivalent (cite) | known-and-weaker (cite + delta confirmed)}, and the PROOF_MANIFEST statuses updated accordingly. Until then: **all entries internal-best-effort; G5 NOT DONE.**

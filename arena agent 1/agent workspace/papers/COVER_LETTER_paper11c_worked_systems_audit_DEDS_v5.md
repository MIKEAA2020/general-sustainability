# Cover letter

**To:** The Editors, *Discrete Event Dynamic Systems: Theory and Applications*
**Manuscript:** *Worked systems for viability under incomplete observation: exact belief kernels across observation structures, protocols and decentralisation, a monitoring-design census, and certified margins*
**Author:** Amin Abaee (independent researcher; ORCID 0000-0002-0019-1842)

Dear Editors,

I submit the above manuscript for consideration as a regular paper. It studies viability (safety) under incomplete observation on a small finite system and asks a question that is usually settled tacitly: how much of the viability kernel depends on *which* function of the state is observed, on *which protocol* governs the re-use of an instrument and on *who* holds the record of the last decision. The paper gives exact answers on a worked system with two stocks and two instruments and organises them around theorems that the computations test rather than illustrate.

**Contributions.**
1. A fibrewise belief game whose kernel is the greatest fixed point of a single operator on beliefs, with a monotonicity theorem along three independent axes (observation refinement, protocol relaxation, horizon). On the worked system every axis is strict and the two middle information classes are incomparable (111, 143, 119 and 255 viable beliefs out of 511).
2. Closed forms: with two instruments the no-repeat protocol is strict alternation; the shared-ledger kernel depends on the observation only through the first step, while the private-register kernel is a phase-coherence condition. The two record-keeping conventions are incomparable, which identifies the earlier "ledger" kernels as a property of the register rather than of the protocol.
3. Decentralised unanimity factors statewise, and the allocation of a single floor vote moves the kernel between 12 and 4 pairs.
4. Monitoring design reduces to graph structure: a partition is dynamically adequate for the whole viable set iff it is one-step adequate iff it is independent in the incompatibility graph, which gives a Bell-number count (1 694 of 4 140 partitions) confirmed by a census that also reports kernel sizes, coarsest designs and the designs that are useless under the shared ledger.
5. Review timing as a max-plus hitting time, with the exact boundary cells where the natural strict identity fails, and a continuous companion fibre whose crossover, dual margin and robustness radius coincide.

**Why DEDS.** The objects are finite-state systems with partial observation, information structures, protocols and decentralised control; the methods are fixed-point computation on beliefs, max-plus recursion and exact arithmetic — the core subject matter of the journal. The paper also offers a reproducibility standard for such studies: one exact script regenerates every number, two independent implementations of the kernels agree on all 511 beliefs, 64 named checks are evaluated, and the monotonicity theorem is formalised in Lean 4.

**Reproducibility.** The exact core, the generators of all tables and figures, the verifier with its output and the Lean modules are part of the submission package and are publicly available (repository `MIKEAA2020/general-sustainability`). The supplement (13 pages) carries the complete tables.

The manuscript is not under consideration elsewhere; there are no competing interests and no funding to declare. Large language models assisted with drafting and iterative review; the author reviewed and edited all output and takes full responsibility.

Suggested reviewers: researchers in viability theory and set-invariance under partial observation, in games with imperfect information, and in decentralised control / team decision theory.

Yours sincerely,
Amin Abaee

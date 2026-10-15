**To the Editors, *SIAM Journal on Control and Optimization***

Dear Editors,

I submit the manuscript *Finite certificates of nonviability under incomplete observation: a continuous-to-finite bridge with exact witnesses* for consideration as a research article.

**Problem.** Proving that a safety specification *cannot* be met is harder under partial observation than under full observation: the certificate must exclude every measurable, information-adapted policy, and the adversary chooses mode, initial state and disturbance after the policy is announced. Discretising the control and finding the finite problem infeasible proves only the infeasibility of a held-control subclass. Viability-kernel algorithms, level-set methods and occupation-measure relaxations address the full-information problem; exact imperfect-information safety games exist for finite graphs; what has been missing is a justified bridge from a continuous system with a measurable policy class to a finite program whose certificates are sound for the continuous problem and complete under refinement.

**Contribution.** For linear systems with a hidden mode revealed through an exogenous schedule of history partitions, the manuscript constructs that bridge. An outer moment relaxation of the information-adapted controls and an inner adversarial selection of labels and scenarios yield a finite linear program whose value is a certified lower bound on the continuous-time safety value and whose certified inflation is an upper bound; every dual-feasible point is a finite obstruction certificate valid against every measurable policy; nonviability is eventually detected along any vanishing refinement sequence; and the value admits an exact atomic dual representation (Sion). Certificate size is governed by the information–time rank, not the input dimension: positive certificates need at most r + 1 labels, a scalar-input construction saturates this, and the obstruction depth is a matching lower bound. On a three-branch delayed-observation instance everything is carried exactly: every pair of compatible states is viable and a common blind control is safe, yet the triple is obstructed past the exact delay 7/50; the finite value obeys a closed mesh law certified by one mesh-independent primal–dual witness pair; and, read prescriptively, the certificate yields an exact delay hierarchy for sub-beliefs, prices candidate observers through an erosion identity, and brackets the installation time of an early partial observer within an interval of width below 3·10⁻³.

**Fit.** The results are theorems of continuous-time control under information constraints—weak-∗ compactness of policy spaces, minimax duality, support-function calculus, polyhedral Farkas/Helly arguments—with a computational realisation that is linear rather than semidefinite and whose optimality is certified by exact witnesses rather than solver output. The related-work section states precisely what is new relative to two-sided kernel approximation, moment relaxations, the scenario approach and exact LP verification.

**Reproducibility.** Every reported value is re-derived in exact rational arithmetic by a 63-check script distributed with the submission; figures are produced by a recompute-then-assert script; the Farkas core is mechanised in Lean 4 with its scope stated plainly. Complete proofs are in Appendices A–B and the Supplementary Material.

The work is not under consideration elsewhere. Large language models assisted with drafting and code review, as declared in the manuscript; I reviewed and re-ran everything and take full responsibility for the content.

Yours sincerely,

Amin Abaee
Independent Researcher — ORCID 0000-0002-0019-1842 — amin_abaee@ut.ac.ir

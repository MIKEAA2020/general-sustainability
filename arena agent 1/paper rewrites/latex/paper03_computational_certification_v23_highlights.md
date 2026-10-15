# Highlights — paper03 v23

* A finite linear program whose dual-feasible points are nonviability certificates valid against **every measurable, information-adapted policy**, with a certified two-sided bound on the continuous-time safety value and completeness along any vanishing refinement sequence (Theorem 3.2).
* The value has an **exact atomic dual representation**: nonviability ⇔ a finite list of labelled rows with weights has positive margin (Corollary 3.3).
* **Certificate size is an information–time quantity**: at most r + 1 labels where r is the information–time rank; a scalar-input construction saturates the bound and the obstruction depth is a matching lower bound (Section 4).
* On a three-branch delayed-observation instance every weaker test passes (full-information viability, blind-window safety, pairwise viability) and the certificates still detect the obstruction at the exact delay 7/50; the finite value obeys the closed law ρ(𝓗) = 3/50 − ¼ Σ|J|² on every aligned mesh, certified by one mesh-independent witness pair; HiGHS reproduces it to 4.2·10⁻¹⁷.
* **Read prescriptively**, the certificate yields an exact delay hierarchy for sub-beliefs ((15−√183)/6, (10−√58)/6), prices candidate observers through an erosion identity (33/200, 11/80, 11/50), and brackets the installation time of an early partial observer within [3/25, (6−√29)/5].
* All exact statements are re-derived in rational arithmetic (63 checks); the solver is a confirmation, never a proof object; the Farkas core is mechanised in Lean 4 with its scope stated.

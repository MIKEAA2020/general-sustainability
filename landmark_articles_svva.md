# Landmark Articles in *Set-Valued and Variational Analysis* — Reading Notes

*Journal background:* **Set-Valued and Variational Analysis** (Springer) is the continuation of **Set-Valued Analysis** (1993–2008). Its scope: variational analysis and its applications; set-valued analysis and generalized differential calculus; numerical/computational aspects; equilibrium problems; variational principles; optimal control; **viability theory**; variational inequalities and variational convergence; fixed points of set-valued maps; differential/integral/operator inclusions.

---

## The journal's most-cited papers (per citation aggregators)

| # | Paper | Authors | Citations (approx.) |
|---|---|---|---|
| 1 | Primal-Dual Splitting Algorithm for Solving Inclusions with Mixtures of Composite, Lipschitzian, and Parallel-Sum Type Monotone Operators | Combettes & Pesquet | ~280–356 |
| 2 | A Three-Operator Splitting Scheme and its Optimization Applications | Davis & Yin | ~155–205 |
| 3 | Error Bounds: Necessary and Sufficient Conditions | Fabian, Henrion, Kruger, Outrata | ~106–110 |
| 4 | On Directional Metric Regularity, Subregularity and Optimality Conditions for Nonsmooth Mathematical Programs | Gfrerer | ~90 |

*(Counts vary by aggregator; ranges shown.)*

---

## 1. Combettes & Pesquet (2012) — Primal-Dual Splitting

> Combettes, P. L., & Pesquet, J.-C. "Primal-dual splitting algorithm for solving inclusions with mixtures of composite, Lipschitzian, and parallel-sum monotone operators." *Set-Valued Var. Anal.* **20**, 307–330 (2012). Preprint: arXiv:1107.0081. *(Read in full via arXiv.)*

**What it does.** Proposes a primal-dual splitting algorithm for **monotone inclusions** that mix sums, linear compositions, and parallel sums of **set-valued** and **Lipschitzian** operators.

**The key idea (why it became a landmark).** The algorithm separates the two kinds of operators:
- **Lipschitzian (single-valued, smooth-ish) operators** are processed *individually* by **explicit (forward) steps** — cheap, no inversion needed.
- **Set-valued operators** are processed *individually* via their **resolvents** (implicit/backward steps).

Most of the steps run **in parallel** (simultaneously). The paper unifies and extends a wide family of structured monotone-inclusion methods, with special attention to convex minimization.

**Why it matters.** This is the foundation of the modern primal-dual algorithms (the "PDHG / Condat–Vũ" family) now standard in imaging, signal processing, and machine learning. It is the single most-cited paper the journal has published.

---

## 2. Davis & Yin (2017) — Three-Operator Splitting

> Davis, D., & Yin, W. "A three-operator splitting scheme and its optimization applications." *Set-Valued Var. Anal.* **25**, 829–858 (2017). Preprint: arXiv:1504.01032. *(Read in full via arXiv.)*

**What it does.** Introduces a **three-operator splitting scheme** for monotone inclusions with *three* operators, one of which is **cocoercive**.

**The key idea.** A simple update rule that does **not** reduce to any previously known splitting scheme, yet **recovers** the classical forward-backward, Douglas–Rachford, and forward–Douglas–Rachford splittings as special cases.

**Applications it unlocks.** 3-set split feasibility problems; 3-objective minimization; doubly/multiple regularization; and — notably — the **simplest extension of ADMM from 2 to 3 blocks of variables** (a long-standing open pain point). The paper also adds practical accelerations, including one achieving the optimal rate for strongly monotone inclusions.

**Why it matters.** It resolved a structural gap in operator splitting (going from 2 to 3 operators/blocks) and became a standard reference in optimization for learning and inverse problems.

---

## 3. Fabian, Henrion, Kruger & Outrata (2010) — Error Bounds

> Fabian, M. J., Henrion, R., Kruger, A. Y., & Outrata, J. V. "Error bounds: necessary and sufficient conditions." *Set-Valued Anal.* **18**, 121–149 (2010). DOI: 10.1007/s11228-010-0133-0.

**What it does.** Gives a **general classification scheme** for the **error bound property** — the statement that the distance from a point *x* to the solution set is controlled by some residual (e.g. how far the constraints are from being satisfied).

**The key idea.** It systematically organizes **necessary** and **sufficient** conditions for the error bound property, using derivative-like objects from **both** the primal and the dual space — subdifferentials and "slopes" (in the tradition of Ioffe's approximate subdifferentials and the strong slope of De Giorgi–Marino–Tosques). Keywords: error bounds, calmness, subdifferential, slope.

**Why it matters.** Error bounds / calmness are the quantitative backbone of convergence-rate analysis for optimization algorithms and of stability theory in variational analysis. This paper is the standard unified reference.

---

## 4. Gfrerer (2013) — Directional Metric Regularity

> Gfrerer, H. "On directional metric regularity, subregularity and optimality conditions for nonsmooth mathematical programs." *Set-Valued Var. Anal.* **21**, 151–176 (2013). DOI: 10.1007/s11228-012-0220-5.

**What it does.** Studies **directional** versions of **metric regularity** and **metric subregularity** for general set-valued mappings between infinite-dimensional spaces, using techniques of variational analysis and generalized differentiation (Mordukhovich-style calculus).

**The key idea.** Metric regularity (roughly: "a small violation of the condition can always be corrected by a proportionally small change, with the proportionality constant stable in a direction") is refined to hold only along specified **directions**. Necessary and sufficient conditions are derived that **extend even the known results for conventional (full) metric regularity**.

**Why it matters.** Directional regularity/subregularity and the associated "calmness" concepts are the modern language for constraint qualifications and sharp optimality conditions in nonsmooth optimization, including MPECs (mathematical programs with equilibrium constraints).

---

## 5. Aubin & Catté (2002) — Algebraic structure of viability kernels and capture basins

> Aubin, J.-P., & Catté, F. "Bilateral fixed-points and algebraic properties of viability kernels and capture basins of sets." *Set-Valued Analysis* **10**, 379–416 (2002). DOI: 10.1023/A:1020667819804. *(Abstract read in full; full text paywalled.)*

**What it does.** Shows that the central objects of **viability theory** — viability/invariance **kernels** and capture/absorption **basins**, under discrete multivalued systems, differential inclusions, and dynamical games — share **algebraic properties** that yield simple but powerful characterizations: each is a **largest or smallest fixed point**, or a **unique minimax ("bilateral") fixed point**, of a suitable map defined on **pairs of subsets**.

**The key idea.** The well-known algorithms of the field are algebraic in nature: the **Saint-Pierre viability-kernel algorithm** (discrete systems) and the **Cardaliaguet algorithm** (discriminating kernels in games) both implement these fixed-point characterizations. The paper also brings in the **Matheron theorem** and the **Galois transform** to clarify concepts and simplify proofs in control and differential games.

**Why it matters (and why it's the most relevant to your paper).** This is the journal's canonical statement of the *structural/algebraic* side of viability kernels and capture basins — exactly the machinery the sustainability paper builds on (its "exact-tube" operators are typed instances of viability-kernel/reachability constructions).

---

## How these connect to the sustainability paper (*p1.txt* / the humanized version)

1. **Viability lineage (Aubin & Catté, and the broader Aubin–Frankowska program).** The paper's §5.2 explicitly acknowledges this: its backward recursion is "a typed instance of established robust-predecessor, reach-avoid, capture-basin, and hybrid-reachability constructions (Aubin 1991; Aubin, Bayen & Saint-Pierre 2011; Saint-Pierre 1994; Lygeros, Tomlin & Sastry 1999)." The "exact-tube" requirement — safe **at every point of the path, not just the endpoint** — is precisely the viability idea (states from which *some* evolution stays in the safe set), as opposed to mere reachability of a terminal set.

2. **The tube vs. endpoint distinction** mirrors the viability-kernel vs. reachability-set distinction: the endpoint-only operator ("the photograph") is reachability-like; the typed-tube operator ("the trajectory") is viability-like.

3. **Metric regularity / error bounds / calmness (Gfrerer; Fabian et al.)** are the quantitative stability cousins of the paper's thresholds: the licensing thresholds ρ₁, ρ₂ and the rescue threshold κ\* = 1 − x are exactly the kind of boundary/feasibility statements that regularity theory quantifies (how robustly a feasibility property holds as parameters move). The paper doesn't invoke these tools, but they sit in the same journal and the same intellectual neighborhood.

4. **Operator splitting (Combettes–Pesquet; Davis–Yin)** is the journal's other major pole — algorithmic variational analysis for computation — relevant if one wanted to *compute* the accepted sets/viability kernels efficiently at scale, alongside the paper's machine-checked 31³ grid.

---

## Access notes

- **Open (read in full):** Combettes & Pesquet (arXiv:1107.0081); Davis & Yin (arXiv:1504.01032).
- **Paywalled (abstract read; full text available via subscription/purchase):** Fabian–Henrion–Kruger–Outrata (a full-text PDF is also posted at the WIAS Berlin site: https://www.wias-berlin.de/people/henrion/errorbound.pdf); Gfrerer; Aubin & Catté.
- **Adjacent classics not in this journal but cited throughout:** Aubin & Frankowska, *Set-Valued Analysis* (Birkhäuser, 1990 — the book that named the field); Saint-Pierre, "Approximation of the viability kernel," *Appl. Math. Optim.* 29 (1994); Aubin, "Viability kernels and capture basins of sets under differential inclusions," *SIAM J. Control* 40 (2001).

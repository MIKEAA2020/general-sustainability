# Prior-art pass — units 2–6

Started 2026-09-30. **Unit 6 complete** (the designated literature search).
**Units 2–5 pending.** This file is the working record.

---

## 0. Correction: the architecture's prior-art table is false

`SUBMISSION_ARCHITECTURE.md` states units 2–6 have **0 words** of prior art. Direct
measurement of the source heads refutes it. Every one of these units has a substantial
Related work section:

| unit | source head | architecture claim | **measured** |
|---|---|---|---|
| 2 | `paper02_probabilistic_sufficiency_v12.tex` | 0 | **1,493 w** |
| 3 | `paper03_computational_certification_v16.tex` | 0 | **1,680 w** |
| 4 | `paper04_minimax_dual_certificates_v16.tex` | 0 | **1,321 w** |
| 5 | `paper05_exact_belief_computation_v15.tex` | 0 | **1,111 w** (709 + 402) |
| 6 | `paper06_assessment_separation_v66.tex` | 0 | **1,881 w** (921 + 960) |

**Consequence for the architecture.** One of the two venue-independent grounds given for
keeping units 1–5 separate — *"folding cannot produce a prior-art section"* — rested on this
measurement error. The partition may still be correct, but that argument no longer supports
it. **The premise of the whole prior-art pass was mis-specified**: this is a verification job
on existing sections, not a drafting job from scratch.

---

## 1. Structural finding: unit 6's source head contains unit 9

`paper06_assessment_separation_v66.tex` (58,710 w) is a container holding **two disjoint
papers**, joined by a deliberate "Cross-part conclusion" section:

| | words | sentence-overlap with `paper10_v53` |
|---|---|---|
| Part I (chars 0–201,302) — the separation theorem | 25,443 w | **0.0%** |
| Part II (chars 201,302–end) | 33,267 w | **91.6%** |
| `paper10_depletion_ledgers_v53.tex` for reference | 31,015 w | — |

Part II shares 812 of paper10's 886 sentences — it *is* paper10, at a slightly earlier state.
Part I shares none.

The architecture treats these as **separate units 6 and 9**, so the split is intended — but the
source head has not been split. **Blocking question for the prior-art pass:** edits to unit 6
must land in Part I only, and the file must be split before any merge is re-run, or unit 9's
content will be silently carried into unit 6's merge.

---

## 2. Unit 6 — novelty test (literature search)

### 2.1 What the paper already does well

Part I's "Related work, and what is actually new here" already engages all three adjacent
literatures and **disclaims** what is not new:

- **Scalarization gap, multi-objective optimization** — Koski 1985; Stadler & Dauer 1992;
  Stadler 1995; Athan & Papalambros 1996; Chen/Hansen/Jaumard/Tuy 1999; Das & Dennis 1998;
  Messac & Mattson 2002; Huang/Li/Liu 2007; Miettinen 1999; Ehrgott 2005. It states plainly:
  *"The reader should therefore not read the convex-hull characterization as a new fact about
  scalarization. It is the scalarization gap, transported."*
- **Adjustable and randomized robust optimization** — Ben-Tal, Goryashko, Guslitzer &
  Nemirovski 2004 (*Math. Program.* 99(2), 351–376); Ben-Tal, El Ghaoui & Nemirovski 2009;
  Bertsimas & Goyal 2012. Randomization line: Krause/Singla/Golovin 2011; Vorobeychik & Li
  2014; Sinha/Fang/An/Kiekintveld 2018; Sessa/Bogunovic/Kamgarpour/Krause 2020; Kobayashi &
  Takazawa 2023.
- **Weak and strong sustainability** — Pearce & Atkinson 1995; Daly 1995; Beckerman 1994;
  Ayres 1996; Neumayer 2003; Dietz & Neumayer 2007.

It narrows its own claim to four items and names the vulnerable one:

> *"Theorem 9 shows that fractional blending closes the gap exactly, while alternating between
> plans over time does not. In robust optimization the ordering runs the other way... **This is
> the sharpest claim in the paper and the one most likely to be contested.**"*

That is where the search went.

### 2.2 Finding 1 — MATERIAL: Kuhn's theorem is absent, and it generates the obvious objection

**The objection a trained reader will raise unprompted.** Theorem 9 says: mixing *over plans*
works, alternating *over time* does not. In game theory these are **mixed** and **behavioural**
strategies, and **Kuhn's theorem (1953)** states that in extensive-form games with perfect
recall the two are realization-equivalent — for every mixed strategy there is an equivalent
behavioural strategy and vice versa. On its face, Theorem 9's second half contradicts one of
the most famous theorems in game theory.

**The contradiction is superficial, and the escape is the paper's own scope claim.** Kuhn's
equivalence is *realization equivalence*: equality of the induced **probability distribution
over paths**, evaluated under **expected payoff**. Unit 6's constraint is **path-wise** — it
must hold on *every* disturbance trajectory in the uncertainty set. Under a worst-case
criterion the two are not interchangeable, because convexification must occur **within** a
time step (a blend applied at each step yields the convex combination of margins at that step),
whereas alternation varies **across** steps and therefore yields only a vertex at any given
step. The binding constraint is per-step, so across-step variation never convexifies.

**But the paper never says any of this.** Verified by grep on the source head:

| term | count in `paper06_v66` |
|---|---|
| `Kuhn` | **0** |
| `perfect recall` | **0** |
| `behavior` / `behaviour` | **0** / 2 (unrelated sense) |
| `mixed strateg*` | 2 — decision-theoretic sense only, not game-theoretic |

The game-theoretic randomization literature is entirely absent. Only the robust-optimisation
randomization line is cited, and that line studies worst-case **objective value**, not
path-wise feasibility.

**Fix — cheap, and it strengthens the paper.** Add to the "Adjustable and randomized robust
optimization" subsection:

1. A paragraph distinguishing Kuhn's realization-equivalence (distributions over paths,
   expected payoff) from the paper's path-wise feasibility setting, stating that the two
   notions of randomization are *not* interchangeable under a worst-case criterion for the
   within-step/across-step reason above.
2. **Main, J.C.A. & Randour, M.** — *Different strokes in randomised strategies: Revisiting
   Kuhn's theorem under finite-memory assumptions.* arXiv:2201.10825; **Games and Economic
   Behavior** (2024), DOI 10.1016/j.geb.2024.05.004. Their result: *"Kuhn's theorem crumbles
   when restricting ourselves to finite memory"* — some finite-memory behavioural strategies
   cannot be emulated by finite-memory mixed strategies. **The paper's setting is finite-horizon
   with finite memory, so this actively supports Theorem 9** rather than threatening it.

### 2.3 Finding 2 — MATERIAL: the closest prior art in existence is not cited

**Verified (Crossref, DOI 10.1007/s10107-023-02049-w):**

> **Wei, N., Zhang, P. 2024.** *Adjustability in robust linear optimization.*
> **Mathematical Programming 208**(1–2), 581–628. Published online 27 January 2024;
> print November 2024. Springer. 61 references.

> *"Based on the discovery of an interesting connection between the reformulations of the
> static and fully adjustable problems, our analysis gives a **necessary and sufficient
> condition — in the form of a theorem-of-the-alternatives — for adjustability to be zero**
> when the uncertainty set is polyhedral."*

This is the quantifier-commutation question answered **exactly**, from the opposite side: Wei &
Zhang characterize when the gap is **zero**; unit 6 proves when it is **nonempty with open
interior**. Same object, opposite face.

**Why this matters more than a routine omission.** The paper writes that Bertsimas & Goyal
(2012) *"characterize when static and adjustable solutions agree."* Bertsimas & Goyal (2012) is
*On the power and limitations of affine policies in two-stage adaptive optimization* — a paper
about **affine policies**, not about the zero-adjustability condition. The paper that actually
does what unit 6 attributes to it is Wei & Zhang (2024). Left uncited, the paper's statement
*"we have not found this comparison, or this inversion, in the robust optimization ...
literatures surveyed above"* is **exposed**, because Wei & Zhang is precisely such a comparison.

**Fix.** Cite Wei & Zhang and state the distinction:

- they measure the gap in **objective value**; unit 6's gap is in **feasibility**;
- their necessary-and-sufficient condition is for **polyhedral** uncertainty sets;
- their result is a **theorem-of-the-alternatives** for the static-vs-adjustable objective gap,
  not a statement about the geometry (open interior) of a feasibility gap on a witness datum.

### 2.4 Finding 3 — tightening, not fixing

The ARO literature writes the quantifier pair explicitly as

  ∩_{ξ∈Ξ} Y_ξ  (static: one decision feasible for every realization = ∃y ∀ξ)
  versus
  Π_{ξ∈Ξ} Y_ξ  (policy space: a function of ξ = ∀ξ ∃y)

which is exactly unit 6's commutation. The paper's positioning is correct but implicit;
naming this notation would let a reader from robust optimisation locate the result instantly.

Also nearby: **finitely adaptable solutions** (Bertsimas et al.) — a small set of solutions
specified per stage, with the best selected on realization — is close to the paper's "finite
menu" and deserves one distinguishing sentence.

### 2.5 Verdict

**Novelty survives.** The claim is genuinely narrow and the path-wise-feasibility scope is a
real and defensible boundary — the literature surveyed studies objective value, not feasibility.

**No repositioning or dropping indicated.** Two citations had to land before the claim could be
made. Under a no-withdrawal publication target, publishing Theorem 9 without addressing Kuhn was
the one avoidable risk in this unit: the objection is immediate, obvious to any reader with
game-theory training, and fully answerable in one paragraph.

### 2.6 STATUS: BOTH FIXES APPLIED (2026-09-30) to `paper06_assessment_separation_v67.tex`

1. **Wei & Zhang (2024)** — added to the *Adjustable and randomized robust optimization*
   subsection, replacing the mis-attribution to Bertsimas & Goyal (2012), which is a paper
   about affine policies and does not give the zero-adjustability condition. The distinction is
   stated on three axes: objective value vs feasibility; polyhedral uncertainty sets vs the
   present setting; and characterising when the commutation *closes* vs exhibiting when it
   *fails* with nonempty interior.
2. **Kuhn** — 343-word paragraph added, stating the objection in the reader's own terms and
   answering it: Kuhn's realization-equivalence is an equality of *distributions over paths*
   under an *expected* criterion, whereas the certified constraint is *path-wise*; convexification
   must occur *within* a step, and alternation varies *across* steps. **Main & Randour (2024)**
   added as reinforcement from the other side — Kuhn's equivalence *fails outright under finite
   memory*, which is this paper's setting, so the classical theorem does not apply even before
   the worst-case criterion is imposed.

Three bibliography entries added in the paper's own flat hand-formatted style, anchored on the
alphabetically-following entries (Kuhn after Krause; Main after Lygeros; Wei after von Neumann).

**Verified after the edit:** all six checked citations resolve (Kuhn 1953, Main 2024, Wei 2024,
Krause 2011, Kobayashi 2023, Sion 1958); braces balanced in every inserted passage and in the
whole file (1824/1824); one `\begin{document}` / `\end{document}`. Unit 6 is now **27,325 w**
(24,799 before the fixes). Compilation still unverified — see §3.1.

**Citation record — all three verified against Crossref before insertion:**

| work | record | DOI |
|---|---|---|
| Kuhn, H.W. 1953 | *Contributions to the Theory of Games (AM-28), Vol. II*, 193–216, Princeton UP | 10.1515/9781400881970-012 |
| Main, J.C.A. & Randour, M. 2024 | *Information and Computation* **301**, 105229 | 10.1016/j.ic.2024.105229 |
| Wei, N. & Zhang, P. 2024 | *Mathematical Programming* **208**(1–2), 581–628 | 10.1007/s10107-023-02049-w |

> **Process note.** Main & Randour was first recorded here as *Games and Economic Behavior*
> with DOI `10.1016/j.geb.2024.05.004`. **That DOI was fabricated** — inferred from a PII
> prefix I misread — and the journal was wrong. Both were corrected by Crossref lookup before
> the entry was inserted. Under a no-withdrawal target an invented DOI would have been
> permanent, so no citation goes into a source file unverified.

---

## 3. Second structural finding: unit 5's source head also contains a second unit

`paper05_exact_belief_computation_v15.tex` (17,439 w) is a **`\part`-structured container**
holding two architecture units, exactly as `paper06_v66` does:

| | words | sentence-overlap with `paper11c_v2` |
|---|---|---|
| Part I — *Computation at scale* (chars 8,963–50,977) = **unit 5** | 6,297 w | **0.0%** |
| Part II — *Exact audits of worked systems* (50,977–end) = **unit 11** | 11,142 w | **67.4%** |

Part I and Part II share **0 sentences**. Part II is a slightly earlier state of `paper11c_v2`.
The architecture's figures (unit 5 = 6,435 w; unit 11 = 11,123 w) match Part I and Part II
respectively, so the split is intended — but again the source head has not been split.

**Consequence:** the earlier table in §0 conflated the two. Corrected: **unit 5 has 709 w of
prior art** (Part I), and **unit 11 has 402 w** (Part II — consistent with the architecture's
405 w figure for unit 11).

### 3.1 RESOLVED 2026-09-30 — containers split

`split_parts.py` performs the split **non-destructively**: containers are left byte-identical
and new numbered versions are written.

| new file | unit | words | note |
|---|---|---|---|
| `paper05_exact_belief_computation_v16.tex` | **5** | 5,654 | Part I; has its own title/abstract/maketitle |
| `paper06_assessment_separation_v67.tex` | **6** | 24,799 | Part I; own abstract, but **no** `\maketitle` — one is injected |

Two candidate splits were **discarded as redundant**: `paper11c…v3` and `paper10…v54` (the
container-derived Part IIs) overlap their pre-existing standalone files by only 67.4% and
91.6%, i.e. the containers hold *earlier* states. **`paper11c_v2` and `paper10_v53` remain
authoritative for units 11 and 9.** They were deleted to prevent ambiguity about which file is
the unit source.

**Asymmetries the splitter had to handle** (a blind split would have broken both):

- `paper05`: Part I has its own `\title`/`\maketitle`/`\begin{abstract}`. Keeping the umbrella
  block too emitted **two `\maketitle`** and printed the title block twice. Fixed by starting
  Part I at its `\part` and injecting the umbrella `\title`.
- `paper06`: Part I has its own abstract but **no `\maketitle`** — in the container the
  umbrella's `\maketitle` covers both parts. Fixed by starting at its `\part` and injecting
  `\title` + `\maketitle`.
- `paper10`'s Part II emits its abstract as `\section*{Abstract}`, not `\begin{abstract}`.

**Verification performed** (no LaTeX toolchain available in this session — `apt` needs root and
the tectonic binary could not be fetched, so compilation was not possible):

- 1 `\documentclass`, 1 `\begin{document}`, 1 `\end{document}`, 1 `\part` per file;
- all environments balanced (`enumerate`, `itemize`, `abstract`, `figure`, `table`, `center`,
  `document`);
- **no cross-part macro dependency** — every `\newcommand`/`\def`/`\newtheorem`/
  `\DeclareMathOperator` defined only in one part is checked against the other, and none is
  used across the boundary;
- no dangling `\ref` after stripping comments (a `\ref{priorart}` inside a `%%` comment is a
  false positive and is not a defect);
- word counts consistent with the measured part sizes.

**Residual risk:** the preambles are copied verbatim from sources known to compile, so package
availability is unchanged. The unverified step is compilation itself — **the four splits should
be compiled once a toolchain is available** before any of them is merged or posted.

#### Bibliography: the first split silently dropped the entire reference list

Both containers keep **one shared reference list at the very end of the document, inside Part
II's character range**, even though it serves both parts. The first split therefore produced
files with **no bibliography at all**.

This was nearly missed, and for an instructive reason: **these papers use no `\cite` commands**
— citations are literal inline text (`(Ben-Tal, Goryashko, Guslitzer and Nemirovski, 2004)`). A
missing list therefore produces **no `?` markers and no LaTeX warning**; it is invisible until
the end of the document. It is nonetheless fatal for publication.

**Two further source defects surfaced while extracting it:**

- **paper06's list is fragmented.** It runs A→V, is interrupted by a
  `\section{Supplementary material}`, then resumes with a **second `\label{references}`**
  block. A "stop at the next heading" rule truncates it (86 of 109 entries, with Sion 1958,
  Saint-Pierre 1994, Schaefer 1954, Solow 1974, Roy 1996 and Vincke 1992 all unresolved).
- **A shape-based filter is also too strict.** Testing entries on `Surname, X.` silently drops
  institutional authors with no comma (`DFO. (2016).`, `World Bank. (2011).`), lowercase
  nobiliary prefixes (`von Neumann, J. (1928).`), and LaTeX accents
  (`Sch\"ar, S., Pohl, E., and Geldermann, J. (2025).`).

**Resolution:** capture from the References heading to the Declarations section, then keep the
heading plus every paragraph matching `Surname, X.` **or** containing a parenthesised year —
bibliography entries essentially always carry a year, supplementary prose mostly does not.

| | container | first split | final split |
|---|---|---|---|
| paper05 → unit 5 bib entries | 22 | 0 | **22** |
| paper06 → unit 6 bib entries | 109 | 0 → 86 → 108 | **109** |
| unit 6 unresolved citations | — | 15 | **0 real** (2 regex false positives) |
| `\label{references}` | 2 (duplicate) | — | **1** |
| supplementary sections leaked | — | — | **0** |

**Known cosmetic issue:** both splits carry the umbrella title, which names both parts (e.g.
*"…computation at scale and the audits that bind the obstruction calculus to its worked
systems"*). Narrowing the titles is a content decision and was not taken.

---

## 4. Unit 5 — novelty test

### 4.1 What the paper claims, and how honestly

Part I's related work is notably disciplined. It states outright:

> *"**This paper proves no new theorem about antichains.** The census of Section … is a
> computation on one instance: 1,048,576 raw subset evaluations collapsing to 496 stored
> maximal sets. That figure is an output... **The classical results are the scaffold, not the
> contribution.**"*

It cites the *combinatorics* of antichains correctly: Sperner 1927; Kleitman 1966; Stanley 2013;
Engel 1997. And it cites the POMDP point-based line (Pineau, Gordon & Thrun 2003; Shani, Pineau
& Kaplow 2013) and Chatterjee, Doyen & Henzinger 2009 for the qualitative decidability
landscape. Its five claimed contributions are all instance-specific: a complete classification
of the 4-cube; the cost figures; the pairwise-Hamming restrictions *as they apply here*; the
complete classification of the 5-cube; and machine-checking.

**The five contributions survive.** See §4.2–4.3 for what must be added.

### 4.2 Finding 1 — MATERIAL: the antichain *algorithms* literature is entirely uncited

The paper cites antichain **counting** (Sperner, Kleitman, Stanley, Engel). It does not cite
antichain **algorithms** — a large, separate literature in formal verification in which
*storing maximal elements of a downward-closed set* is the standard compact representation, and
in which the **exponential compression is a proved theorem, not an empirical surprise**:

- **De Wulf, M., Doyen, L., Henzinger, T.A., Raskin, J.-F. 2006.** *Antichains: A New Algorithm
  for Checking Universality of Finite Automata.* CAV 2006, **LNCS 4144**, 17–30.
  DOI 10.1007/11817963_5. — They prove *"there exists an infinite family of NFAs A_k … for
  which the forward subset algorithm is exponential, and the (forward and backward) antichain
  algorithms are polynomial."*
- **Doyen, L., Raskin, J.-F.** Antichain algorithms for finite automata / Büchi automata;
  *"such compact representations do not come at the price of an increase in the time
  complexity... while this size can be exponentially smaller than the actual downward-closed
  set."*
- **De Wulf, M., Doyen, L., Maquet, N., Raskin, J.-F. 2008.** *Antichains: Alternative
  Algorithms for LTL Satisfiability and Model-Checking.* TACAS 2008, **LNCS 4963**, 63–77.
- **Filiot, E., Jin, N., Raskin, J.-F. 2009.** *An Antichain Algorithm for LTL Realizability.*
  CAV 2009, **LNCS 5643**, 263–277. — and the journal version, *Antichains and compositional
  algorithms for LTL synthesis*, **Formal Methods in System Design 39**, 261–296 (2011).
- **Games of imperfect information.** Doyen's antichain programme covers these explicitly, and
  Berwanger, Doyen & Chatterjee's **Alpaga** tool rests on the observation that *"the set of
  winning belief states is downward-closed... for downward-closed sets, we only store the
  maximal elements."*

That last item is **unit 5's instrument, stated verbatim**. Unit 5 stores the maximal elements
of a downward-closed survivable set over belief states; the 2²⁰ → 496 collapse is an instance
of a succinctness result proved in general form in 2006.

**Note the near-miss:** the paper already cites **Chatterjee, Doyen & Henzinger 2009**. Doyen
and Henzinger are co-authors on the founding antichain papers. The bridge is one step away and
was not taken.

**Fix (repositioning, not retraction).** The five claimed contributions are unaffected. Add a
subsection distinguishing this paper from the antichain-algorithms literature on three axes:
(i) those algorithms compute **fixed points** (reachability/universality/LTL realizability),
whereas this paper **classifies one finite instance exhaustively in exact arithmetic**;
(ii) those settings are **qualitative** (win/lose), whereas this is **quantitative** — a
maximal *probability* of remaining safe; (iii) the compression here is a **measured cost
figure**, not a claimed asymptotic advance.

### 4.3 Finding 2 — MATERIAL: Harper's theorem governs the m=5 result and is not cited

The paper's five-cube result is: *"the maximal sets are the 32 radius-one balls at every
level."* That is a **Hamming-ball extremal statement**, and it is exactly what hypercube
vertex isoperimetry governs.

**Harper's theorem (Harper, 1966):** among all vertex subsets of the hypercube Q_n of a given
size, Hamming balls — the initial segments of the **simplicial order** — minimise the vertex
boundary. Stability versions (Keevash & Long, arXiv:1807.09618) additionally give **uniqueness
of the extremal configurations**: sets attaining the minimum boundary *are* Hamming balls.

The related work gestures at this — *"Hamming adjacency, and the coding-theoretic machinery
built on it, is likewise classical"* — but cites **neither Harper nor any isoperimetric
result**. A reader in extremal combinatorics will immediately ask whether the radius-one-ball
result is an independent finding or a consequence of Harper applied to this instance.

**Fix.** Cite Harper (verify volume/pages via Crossref before insertion) and state the relation
explicitly: whether the paper's extremality result *follows from* Harper, *coincides with* it,
or is *independent* of it (e.g. because the survivability constraint is not a pure boundary
minimisation). Any of the three is a defensible position; leaving it unstated is not.

### 4.4 Finding 3 — abstract/body mismatch (Phase 0, surfaced here)

The abstract makes a **general** claim: *"the exact discipline survives the curse of
dimensionality... **It scales further than the relaxing instinct expects**"* — presenting the
compression as a discovery about scaling.

The body makes an **instance-specific** claim and disclaims the general one: *"This paper
proves no new theorem about antichains... a computation **on one instance**... The classical
results are the scaffold, not the contribution."*

These are not the same claim. Under the standing calibration rule (*target the broadest claim
the content supports*; under-ambition and overclaiming are both rejection modes) the abstract
is currently the **looser** of the two, and it is the part a reader sees first. With §4.2's
literature added, the abstract's framing becomes actively vulnerable: the obvious reply is
"antichain succinctness has been known since 2006."

**Fix.** Tighten the abstract to the claim the body actually defends — that the *cost* of
exhaustive exact classification at this size is measured and reported, and that the instance is
classified completely — rather than that exactness scales.

### 4.5 Verdict

**Unit 5 survives. It does not need to be dropped** — contrary to the attrition plan's
expectation that it was the likeliest casualty. Its five contributions are real, specific, and
correctly scoped in the body.

Required: **one new subsection** on antichain algorithms (§4.2), **one citation plus a stated
relation** on Harper (§4.3), and **a scope tightening** (§4.4). No change to the partition.

### 4.6 STATUS: ALL THREE APPLIED (2026-09-30) to `paper05_exact_belief_computation_v16.tex`

1. **New subsection "Antichain algorithms in formal verification"** — De Wulf, Doyen, Henzinger
   & Raskin (2006); Doyen & Raskin (2009); De Wulf, Doyen, Maquet & Raskin (2008); Filiot, Jin
   & Raskin (2009, 2011). States plainly that *"the compression itself should not be read as a
   new result"*, then distinguishes three axes: those algorithms compute **fixed points**
   whereas there is none here; those settings are **qualitative** (a winning region) whereas
   \(V_k(b)\) is a **quantitative** worst-case probability whose stored antichain is the
   identifying structure of its \(\alpha\)-vectors; and the compression figures are **measured
   costs of exhaustive exact classification at this size**, not a claimed asymptotic
   improvement.
2. **Harper (1966)** — cited, with the relation stated precisely. The paper's radius-one-ball
   result turns out to be **independent of isoperimetry**, and the source now says why: the
   balls arise *radially* — the constant matched action \(u=\mathbf{1}\) gives a cell at Hamming
   distance \(k\) the drift \(-\tfrac12 + \tfrac{m-2k}{5}\), which depends on the cell only
   through \(k\), so the set on which it is nonnegative is a Hamming ball *automatically*.
   Nothing is minimised, and no result of the paper depends on Harper's theorem. The coincidence
   with the isoperimetric extremal sets is structural rather than consequential.
3. **Scope tightening** — the split itself removed the umbrella abstract, and with it both
   overclaiming phrases (`scales further`, `relaxing instinct`: verified 0 occurrences in v16,
   1 each in the container). One residual survived in the Introduction — *"the answer is
   affirmative"* to a general question, qualified only two sentences later. Changed to *"**On
   the instance studied here** the answer is affirmative"*, aligning it with the related work's
   own discipline.

Six bibliography entries added in the paper's flat style, anchored alphabetically (De Wulf ×2
and Doyen & Raskin after Baccelli; Filiot ×2 after Farkas; Harper after Geretti).

**Verified after edit:** all eight checked citations resolve; braces balanced in every inserted
passage and file-wide (546/546); one `\begin{document}` / `\end{document}`. Unit 5 is now
**6,710 w** (6,068 before). Compilation still unverified — see §3.1.

**All six new citations Crossref-verified before insertion:**

| work | record | DOI |
|---|---|---|
| De Wulf, Doyen, Henzinger & Raskin 2006 | CAV 2006, LNCS 4144, 17–30 | 10.1007/11817963_5 |
| De Wulf, Doyen, Maquet & Raskin 2008 | TACAS 2008, LNCS 4963, 63–77 | 10.1007/978-3-540-78800-3_6 |
| Doyen & Raskin 2009 | *Logical Methods in Computer Science* 5(1) | 10.2168/lmcs-5(1:5)2009 |
| Filiot, Jin & Raskin 2009 | CAV 2009, LNCS 5643, 263–277 | (publisher record) |
| Filiot, Jin & Raskin 2011 | *Formal Methods in System Design* 39, 261–296 | (Springer record) |
| Harper 1966 | *J. Combinatorial Theory* 1, 385–393 | 10.1016/s0021-9800(66)80059-5 |

---

## 5. Units 2, 3, 4 — novelty test

**All three pass. No additions required.** Two of them had already anticipated the classical
objections I went looking for, and conceded them in the source.

### 5.1 Unit 4 — CLEAN

Concedes the central collision outright:

> *"**This paper's obstruction is the emptiness of that object, and it should be read that
> way.** ... That is a real collision with prior art and is **conceded here rather than argued
> around**."*

Engages Aubin 1991; Aubin & Catté 2002; Cardaliaguet, Quincampoix & Saint-Pierre 1994/2007
(discriminating kernel); Farkas 1902; Isaacs 1965; Cardaliaguet & Quincampoix 2008 (value
existence on the space of measures); **Sion 1958** — *"this paper makes no claim to have
originated the equality."*

**I went looking for Carathéodory as the uncredited source of the ≤ k+1 support bound. It is
already credited**, at `paper04…v16.tex` lines 223–225:

> *"the pairing argument itself is **Carathéodory's theorem in ℝ^k**. The tightness bound is
> **Helly's theorem in the plane** (Helly, 1923) applied to the row half-spaces."*

It carries explicit **Claimed** / **Not claimed** lists. The claimed residue is the *certificate
form* (finitely supported, tightly bounded, exactly checkable measure witness) and the
*negative boundary result* — both genuinely outside the kernel programme.

**One optional tightening, not a defect:** the Carathéodory/Helly attribution sits in the body
(§223–225), not in the "Minimax equality" subsection of the related work, which discusses only
Sion. A reader who stops at the related work sees Sion rebutted but not Carathéodory conceded.
Cross-referencing the body attribution into the related work would close the reflex objection
at the point where it forms.

### 5.2 Unit 3 — CLEAN

Saint-Pierre 1994 (viability kernel algorithm); Mitchell, Bayen & Tomlin 2005 (level-set HJ);
Maidens et al. 2013 (Lagrangian reachable sets). States plainly:

> *"**The two-sided structure is not new, and this paper does not claim it is.**"*

Engages moment–SOS (Lasserre 2001; Parrilo 2003) with **three concrete** differences: LP rather
than SDP; convergence along a refinement sequence rather than in relaxation degree; and the
certified object is an *obstruction*, not a recovered minimiser. Engages the scenario approach
(Calafiore & Campi 2005, 2006; Campi & Garatti 2008, 2011; Campi, Garatti & Prandini 2009) and
distinguishes the guarantee as **worst-case rather than probabilistic**.

**Helly 1923 is engaged and shown false in the relevant case** (`…v16.tex` line 966): the
Helly-type "at most m+1 states suffice" bound holds for convex common-action sets in ℝᵐ but
**not** for a common blind control function — the correct dimension being information–time
rank, not instantaneous input dimension. That is a real, non-obvious distinction and it is
explicitly drawn.

**No additions required.** This is the strongest-positioned unit in the family.

### 5.3 Unit 2 — CLEAN

Åström 1965; Smallwood & Sondik 1973; Bertsekas & Shreve 1978; Veliov 1993; **Luc Doyen 2000**;
Cardaliaguet, Quincampoix & Saint-Pierre 2007; Chatterjee, Doyen & Henzinger 2009;
Papadimitriou & Tsitsiklis 1987; Lovejoy 1991.

Positioned item by item against the two nearest neighbours:
- **vs Veliov (1993):** his condition is sufficient only; this one is necessary *and*
  sufficient, so failure is informative rather than inconclusive.
- **vs Doyen (2000):** different admissible policy class (history-dependent here vs Lipschitz
  *memoryless* there, strictly — the feedback recursion contains the blind recursion strictly),
  and a quantitative deficit rather than exact maintenance of a closed domain.
- **vs Chatterjee et al.:** quantitative vs qualitative, with the sharp observation that the
  support-only reduction valid for *almost-sure* objectives **does not extend** to the
  quantitative criterion — which is why the value, not just the support, must be carried.

**Two objections I was prepared to raise are already answered.** Distributionally robust POMDPs:
*Nakao, Jiang & Shen 2021* is cited and distinguished — *"the disturbance model here is
worst-case over a support rather than distributional, so the two are not comparable and
neither subsumes the other."* Safe RL shielding: *Alshiekh et al. 2018* is cited and
distinguished (unknown model / learning vs known model / exact sufficiency).

Two marks of care worth preserving: the source carries an explicit maintainer note that **Luc
Doyen (2000, viability) and Laurent Doyen (2009, qualitative POMDPs) are different authors and
must not be merged**; and the claim list discloses that *"one bound remains cited rather than
formalized: the Sperner bound."*

**No additions required.**

---

## 6. Summary

| unit | prior art (w) | verdict | action |
|---|---|---|---|
| 2 | 1,493 | **PASSES** | none |
| 3 | 1,680 | **PASSES** | none |
| 4 | 1,321 | **PASSES** | optional: surface Carathéodory/Helly in related work |
| 5 | 709 | **SURVIVES** | 1 new subsection (antichain algorithms); Harper citation + stated relation; tighten abstract |
| 6 | 921 | **SURVIVES** | Kuhn/finite-memory paragraph; Wei & Zhang 2024 citation; split source head |

**No unit needs to be repositioned, combined, or dropped.** The attrition budget was not
drawn on. Under the attrition plan's options, all five resolved at (i) or better.

**Two cross-cutting findings:**

1. **The measurement that motivated this pass was wrong** (§0), and with it one of the two
   grounds for keeping units 1–5 separate in the architecture.
2. **Two source heads are `\part`-structured containers** holding two architecture units each
   (§1, §3): `paper06_v66` = unit 6 + unit 9; `paper05_v15` = unit 5 + unit 11. Both must be
   split before any merge is re-run or any unit-level edit is applied.

## 4. Citation mechanics reminder

Each paper uses its own **flat hand-formatted** bibliography — no `\bibitem`. New entries must
be anchored on the **alphabetically-following entry that already exists**, in that paper's own
style. Unit 6's source head must be **split** (§1) before any edit, so that unit 6 edits land
in Part I only.

---

## 7. Extension of the pass to units 7–11 (2026-09-30)

The ratified prior-art pass covered units 2–6. Units 7–11 had never been tested. Their
prior-art sections were measured first:

| Unit | File | Related-work sections | Words |
|---|---|---|---|
| 7 | `paper08_governance_delay_v46` | 1 | 508 |
| 8 | `paper09_cod_certification_v32` | 3 (merged from three papers) | 606 / 638 / 586 |
| 9 | `paper10_depletion_ledgers_v53` | 1 | 509 |
| 10 | `paper11_forecasting_baselines_v64` | 2 (merged) | 526 / 424 |
| 11 | `paper11c_worked_systems_audit_v2` | 1 | 398 |

Per-paper prior art runs 398–638 words, against 709–1,680 for units 2–6. Read, they are
substantive rather than stubs: each names its founding literature and states what it adds.
Unit 9, for instance, cites Brunner and Rechberger (2016) and Sterner and Elser (2002) and says
plainly that "the contribution is therefore not a new way to close a balance but a typing
discipline that rules out a class of aggregations". Unit 11 cites Aubin (1991), the ARCH-COMP
benchmark literature, and Farkas, Helly and max-plus algebra, and states that "none of these is
contributed here".

### 7.1 First finding — unit 5 revisited: the constrained-POMDP literature was uncited

Re-reading unit 5 against its own central object surfaced a gap the first pass missed. Unit 5
computes \(V_k(b)\), "the maximal probability of remaining safe for \(k\) steps". That is
precisely the objective of the **constrained and chance-constrained POMDP** literature. Unit 5
cited the POMDP *algorithms* literature — Lovejoy (1991), Pineau, Gordon and Thrun (2003),
Shani, Pineau and Kaplow (2013), all on point-based value iteration — but **nothing** on
constrained or chance-constrained formulations. A grep confirmed `constrained` appeared zero
times in the file.

So the paper engaged the literature on *how to compute belief-space values approximately* and
not the literature on *the objective it computes*. The question it answers is asked and
answered approximately in that literature; the question is not new.

**Fixed.** New subsection "Constrained and chance-constrained POMDPs" (`\label{scale-cpomdp}`),
inserted before "Mechanized verification". It names Altman (1999) for constrained MDPs, then
Poupart et al. (2015), Undurti and How (2010) and Santana et al. (2016) for constrained POMDPs,
and Ono et al. (2015) for chance-constrained dynamic programming. It separates on three axes —
those formulations optimise over policies subject to a constraint whereas \(V_k(b)\) is the
value *function* studied as an object; their constraint is a feasibility threshold whereas the
result here is the probability's *shape* (the piecewise-linear \(\alpha\)-vector support and the
antichain structure); and every one of those methods is approximate whereas nothing here is.
It closes by stating that the question is not new and the paper does not claim it is.

All five citations were Crossref-verified before insertion, per the standing rule:

| Citation | Venue | DOI |
|---|---|---|
| Altman, E., 1999 | *Constrained Markov Decision Processes*, Chapman & Hall/CRC | 10.1201/9781315140223 (2021 CRC reprint) |
| Poupart, Malhotra, Pei, Kim, Goh and Bowling, 2015 | AAAI **29**(1) | 10.1609/aaai.v29i1.9655 |
| Santana, Thiébaux and Williams, 2016 | AAAI **30**(1) | 10.1609/aaai.v30i1.10423 |
| Undurti and How, 2010 | ICRA 2010, 3966–3973 | 10.1109/robot.2010.5509743 |
| Ono, Pavone, Kuwata and Balaram, 2015 | *Autonomous Robots* **39**, 555–571 | 10.1007/s10514-015-9467-7 |

Note on Altman: the canonical original is 1999 (Chapman & Hall); Crossref indexes the 2021 CRC
reprint, whose DOI is recorded. The entry cites 1999 and carries the reprint DOI.

**Unit 5 survives.** Its contributions — exact rational arithmetic, the support identity, the
antichain structure of the \(\alpha\)-vectors, and the exhaustive classification — are untouched
by this literature, which is uniformly approximate. No repositioning.

Verified after the edit: braces +0; document/abstract/enumerate/itemize balanced; no dangling
`\ref`; all five in-text citations resolve to bibliography entries; 7,580 → 8,101 words.

### 7.2 Status of the extension

Unit 5 revisited and fixed. Units 7–11 remain to be tested individually — §7.1 came out of
re-reading unit 5, not from the units 7–11 sweep, which has only reached the measurement stage
above. That sweep is the next manuscript task.

### 7.3 Unit 9 — weak/strong sustainability framed without citing its origin

Unit 9 (`paper10_depletion_ledgers_v53`) otherwise covers its ground well: a bibliography check
found Tilton (2), Redner, Daly, Neumayer, Munda (2), Ekins, Hubbert (2), Bartlett, Sterner and
Brunner (2) all cited — reserve-life criticism, first-passage processes, ecological economics,
noncompensatory aggregation, MFA and stoichiometry.

But its third objective is to "formalize weak and strong sustainability not as irreconcilable
ethical doctrines, but as two distinct operating regimes", and the **Weak Sustainability Regime**
bullet describes exactly the substitutability assumption that Solow and Hartwick formalized —
while citing only Daly (1990), Neumayer (2013) and Ekins (2003). `Solow` and `Hartwick` appeared
zero times. The weak-sustainability criterion (a non-declining consumption path sustained by
investing resource rents in reproducible capital) is the canonical origin of precisely the
regime the bullet defines.

**Fixed** by adding the origin at the claim site, and distinguishing rather than merely naming:

> "This substitution-based criterion is the one canonically associated with Solow's
> intergenerational-equity formulation and the rule that bears Hartwick's name ... The ledger does
> not dispute that criterion; it makes its precondition checkable, since whether material loops
> close at the rate of throughput is a property of the incidence structure that the aggregate
> criterion presupposes and does not itself test."

Crossref-verified: Solow, R.M. (1974), *Review of Economic Studies* **41**, 29–45,
doi:10.2307/2296370. Hartwick's 1977 *American Economic Review* original is **not** indexed by
Crossref; the entry cites the original and carries the DOI of the verified 2017 Routledge reprint
(*The Economics of Sustainability*, 63–65, doi:10.4324/9781315240084-4). That discrepancy is
recorded here rather than smoothed over.

**Unit 9 survives.** Its contributions — the typed ledger, the three certification layers, the
no-nonnegative-weighting theorem, the double-counting rules, the reclassification of the three
public indicators — are untouched by Solow–Hartwick, which the paper now uses as the frame it
makes checkable rather than as a competitor.

Verified after edit: braces +0; no dangling `\ref`; both citations resolve; 32,782 words.

### 7.4 Unit 11 — computes viability kernels without citing the literature that computes them

Unit 11's prior art was the thinnest at 398 words. It cited Aubin (1991) for viability theory's
founding move, the ARCH-COMP benchmark literature, and the classical instruments (Farkas, Helly,
max-plus). It also handled its own positioning honestly, disclaiming superiority over
interval arithmetic: "a statement about the verification pipeline and not a claim of
superiority over validated or interval-arithmetic approaches".

But several audits tabulate viability kernels — "kernel sizes 24, 26, 25, and 28 of 36 belief
pairs" — and the literature on *computing* viability kernels was entirely uncited.

**Fixed** with a new paragraph, "Computing viability kernels", naming Saint-Pierre's
backward-reaching-set algorithm with its convergence property (Saint-Pierre, 1994) and the
support-vector approximation of kernels and resilience values (Deffuant, Chapel and Martin,
2007). It separates on two axes: those methods address **fully observed** dynamics in continuous
or large discrete spaces, where exact computation is infeasible and the honest goal is a
guaranteed approximation, whereas the audits here are exact in rational arithmetic with no
approximation error to bound; and their objects are kernels over states, not the
observation-constrained kernels over **belief pairs** under declared observation structures and
policy-class restrictions tabulated here. It closes by naming what *does* transfer — the
question of which states admit a constraint-satisfying control, and the finding that the answer
is not monotone in the observation structure, which is a statement about the observation layer
those methods do not model.

Crossref-verified: Saint-Pierre, P. (1994), *Applied Mathematics & Optimization* **29**, 187–209,
doi:10.1007/bf01204182. Deffuant, G., Chapel, L. and Martin, S. (2007), *IEEE Transactions on
Automatic Control* **52**(5), 933–937, doi:10.1109/tac.2007.895881.

**Unit 11 survives.** It is an audit paper; its contribution is the exact tabulation, which is
precisely what the approximated methods cannot supply.

Verified after edit: braces +0; document/abstract balanced; no dangling `\ref`; both citations
resolve; 11,730 → 12,003 words.

### 7.5 Sweep status

| Unit | Tested | Outcome |
|---|---|---|
| 5 (revisited) | yes | gap found and fixed — constrained/chance-constrained POMDPs |
| 9 | yes | gap found and fixed — Solow–Hartwick origin of weak sustainability |
| 11 | yes | gap found and fixed — computational viability kernel literature |
| 7, 8, 10 | **not yet** | measured only (§7 table); central claims not yet tested |

Three units tested, three gaps found, three fixed, **no unit repositioned, combined or dropped**.
The attrition budget remains undrawn after two passes. Units 7, 8 and 10 are the remainder.

### 7.6 Unit 7 — delay as a stabilising mechanism, without the literature that stabilises by delay

Unit 7's prior art is strong and honestly framed. It names three literatures — delays in
population dynamics (Hutchinson 1948; Hale and Verduyn Lunel 1993; Diekmann et al. 1995; Kuang
1993; Hassard et al. 1981; Hayes 1950), informational and knowledge delay (Adamson and Hilker
2020; Li et al. 2016; Peterson et al. 2022), and management delay as a cost (Shertzer and Prager
2007; Brown et al. 2012; Karlsson and Gilek 2020; Hocherman et al. 2025) — and reconciles its own
finding with the third by localising the range over which their monotonicity should be expected
to hold. It also cites the sampled-data control canon (Åström and Wittenmark; Chen and Francis)
and the bifurcation texts (Kuznetsov; Guckenheimer), and is careful about Neimark–Sacker: the
paper calls it the "linear spectral signature" and repeatedly states that the *nonlinear*
conditions are not verified.

But its headline differentiator is that "for the mobilising rule, intermediate delay
*stabilises* the equilibrium, with two subcritical Hopf crossings bounding the stabilising
window" — and the literature on **delay as a stabilising mechanism** was entirely uncited:
Pyragas, Niculescu, Michiels, Sipahi, Insperger and Stépán all appeared zero times.

**Fixed** with a new paragraph, "Delay as a stabilising mechanism", placed between "delay as a
cost" and "Where this paper departs". It names Pyragas's delayed-feedback stabilisation of
unstable orbits (Pyragas, 1992), delayed positive feedback stabilising oscillatory systems
(Abdallah, Dorato, Benites-Read and Byrne, 1993), and the general eigenvalue-based treatment
(Niculescu, 2007). It then separates on **who chooses**: in that literature the delay is a
*control design parameter* — introduced, tuned, and proved stable at a chosen value — whereas
here the delay belongs to the institution, nobody introduces it as a stabiliser, and the finding
is that a bounded intermediate range happens to stabilise. It closes by tying this to why the
result is reported as a bracketed window with its perturbation band rather than as a
recommendation.

Crossref-verified: Pyragas, K. (1992), *Physics Letters A* **170**, 421–428,
doi:10.1016/0375-9601(92)90745-8. Abdallah, C.T., Dorato, P., Benites-Read, J. and Byrne, R.
(1993), *1993 American Control Conference*, 3106–3107, doi:10.23919/acc.1993.4793475.
Niculescu, S.-I. (2007), *Stability and Stabilization of Time-Delay Systems*, SIAM,
doi:10.1137/1.9780898718645.

**Unit 7 survives.** The operator contrast and the bounded stabilising window are untouched.
Verified after edit: braces +0; document/abstract balanced; no dangling `\ref`; all three
citations resolve; 47,863 words.

### 7.7 Unit 10 — a locked evaluation design, without the data-snooping literature

Unit 10 is the most candid of the set about scope. The cod section states that the
M-competitions aggregate over tens of thousands of series and 61 methods whereas this paper
scores five modules plus two baselines on one stock, and that "a cross-series result about the
average performance of method classes does not entail anything about a particular stock". The
Edwards section states that "the paper's contribution is therefore not a new forecasting model;
it is a locked evaluation design applied to a familiar model family, with the negative result as
the finding." Diebold and Mariano (1995), Hyndman and Koehler (2006) and Makridakis et al.
(2000, 2018, 2020) are all cited.

But the paper's methodological claim — "a negative result of this kind is informative only
against a protocol fixed before any score is computed" — is precisely the data-snooping problem,
and that literature was entirely uncited: White, Romano, Wolf, Hansen, "data snooping",
"multiple testing", "pre-registered", "pre-specified" and "cross-validation" all appeared zero
times in the bibliography.

**Fixed** with a new paragraph, "Guarding against selection after the fact", placed in the
methodology discussion. It names White's reality check, which constructs the distribution of the
best performance statistic across candidates under the null that none has skill (White, 2000),
and the stepwise testing literature's familywise-error control (Romano and Wolf, 2005). It then
distinguishes: those procedures take a *set of already-computed scores* and ask which survive
correction for having been selected, whereas here nothing is selected from the scores at all —
the rule is a predicate fixed before any score is read, applied without exception, with its
operating characteristics measured by simulation under known ground truth. That is why a
negative result can be reported as a finding rather than an absence of evidence. It also states
the cost, which is real: a rule fixed in advance cannot be tuned to the series.

Crossref-verified: White, H. (2000), *Econometrica* **68**(5), 1097–1126,
doi:10.1111/1468-0262.00152. Romano, J.P. and Wolf, M. (2005), *Econometrica* **73**(4),
1237–1282, doi:10.1111/j.1468-0262.2005.00615.x.

**Unit 10 survives.** The locked design and the negative result are untouched; the citations
supply the reason the design is necessary.
Verified after edit: braces +0; document/abstract balanced; no dangling `\ref`; both citations
resolve; 32,229 words.

### 7.8 The recurring shape of the gaps

Five units have now yielded exactly one genuine gap each, and all five have the same shape:

| Unit | Literature engaged | Literature that owns its central object, and was missing |
|---|---|---|
| 5 | POMDP *algorithms* (PBVI) | constrained / chance-constrained POMDPs |
| 9 | composite-indicator critique, MFA, stoichiometry | Solow–Hartwick, origin of weak sustainability |
| 11 | viability theory's founding text, ARCH-COMP | computing viability kernels |
| 7 | delay as a cost; sampled-data control | delay as a stabilising mechanism |
| 10 | forecast accuracy, M-competitions | data snooping / multiple testing |

In every case the paper cites the literature *adjacent to its method* and misses the literature
that owns *its objective*. This is a diagnosable habit of the series rather than five
coincidences, and it is the check to run first on any remaining unit.

### 7.9 Unit 8 — the production model is used throughout and never cited

Unit 8 (`paper09_cod_certification_v32`) has the strongest prior art of the set. Across its three
merged papers it names owners rather than neighbours: Regnier and De Lara (2015) for robust
viability kernels, with an explicit distinction (their kernel is computed numerically by a
descending set iteration on a discretised state space; here the increasing branch collapses to
algebra), Butterworth (2007) and Punt et al. (2016) for management strategy evaluation, and
Hutchings and Myers (1994), Myers and Cadigan (1995) and Myers, Hutchings and Barrowman (1997)
for the received attribution of the collapse — with a paragraph stating plainly that the paper
"does not adjudicate" the tension and that a reader taking the harvest-free result as evidence
about productivity "is going beyond what is certified". It also flags the VPA-versus-survey
divergence as load-bearing for its own choice of series.

But the governed object is a **surplus-production model of Schaefer form**, and the count is
decisive: `Schaefer` appears **ten times in the body** — "Schaefer fit 1983–2007", "the registered
Schaefer form", "Schaefer-form (Allee term off)", "Registered Schaefer & 989.0" — and **zero
times in the References**. Schaefer, Clark, Hilborn, Walters, Quinn, Deriso and Pella all absent.
The single most standard model in fisheries is used, compared against two alternatives (Allee,
Fox) across an entire section, and never once attributed.

**Fixed** with a new paragraph, "The production model", in the cod section's prior art. It names
Schaefer (1954) for the logistic surplus-production form and Fox (1970) for the exponential
surplus-yield form fitted as a co-equal alternative, states that neither is contributed and that
the comparison is decided on residual MSE rather than convention, and then separates on the use
to which the fitted form is put: the production-model literature estimates parameters and asks
what harvest maximises yield or profit, whereas here the fitted surplus enters a viability
problem and the quantity extracted is not an optimal effort but a *kernel*. It closes on why the
form comparison is not a sensitivity check — the two forms give different kernels, not merely
different optimal efforts.

Crossref-verified: Schaefer, M.B. (1954), *Bulletin of the Inter-American Tropical Tuna
Commission* **1**(2), 27–56; the 1954 original is not DOI-indexed, so the entry cites it and
carries the DOI of the verified 1991 reprint (*Bulletin of Mathematical Biology* **53**, 253–279,
doi:10.1007/bf02464432). Fox, W.W. (1970), *Transactions of the American Fisheries Society*
**99**(1), 80–88, doi:10.1577/1548-8659(1970)99<80:aesmfo>2.0.co;2.

**Unit 8 survives.** The closed-form collapse, the no-dominance verdict and the harvest-free
certificates are untouched; citing Schaefer attributes the model, not the result.

Verified after edit: braces +0; document/abstract balanced; no dangling `\ref`; both citations
resolve; 35,150 words.

### 7.10 Sweep complete

| Unit | Central object | Literature that owns it, and was missing | Fixed |
|---|---|---|---|
| 5 | belief-state safety value \(V_k(b)\) | constrained / chance-constrained POMDPs | yes |
| 7 | intermediate delay stabilises | delay as a stabilising mechanism | yes |
| 8 | Schaefer-form surplus production | Schaefer 1954; Fox 1970 | yes |
| 9 | weak vs strong sustainability | Solow 1974; Hartwick 1977 | yes |
| 10 | locked pre-specified retention rule | data snooping / multiple testing | yes |
| 11 | viability kernels over belief pairs | computing viability kernels | yes |

**Six units tested, one gap each, six fixed. No unit repositioned, combined or dropped. The
attrition budget was never drawn on.**

The recurring shape (§7.8) held to the end, with unit 8 the sharpest instance: the paper's
*method* literature was cited thoroughly while the *model* it governs — used on nearly every
page — went unattributed. The diagnostic that finds these is not "what is adjacent to this
paper?" but "who owns the object this paper computes, and is that name in the bibliography?"

### 7.11 One process failure worth recording

The unit 8 bibliography insertion initially **failed silently in part**: a helper was called with
one argument where two were required, raising `TypeError`. The body paragraph had already been
written, so for a period the paper cited Schaefer and Fox in text with **no bibliography entries
at all** — strictly worse than before the edit. Caught by the verification step, which reports
in-text and entry counts side by side, and repaired in the same turn.

The lesson is the standing one and now has a concrete instance behind it: **verify after every
write, and verify the thing that could break rather than the thing that is easy to check.** A
braces-balance check would have passed throughout.

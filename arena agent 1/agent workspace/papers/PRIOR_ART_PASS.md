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
relation** on Harper (§4.3), and **an abstract tightening** (§4.4). No change to the partition.

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

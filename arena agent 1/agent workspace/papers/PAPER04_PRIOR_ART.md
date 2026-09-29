# Paper 4 (minimax dual certificates) — prior art added, 2026-09-29

## What the paper does

For control-affine dynamics with a compact convex control set: the common safe-action set is
**empty precisely when** an adversarial probability measure on the active boundary–disturbance
bundle drives expected inward drift strictly negative against every control, with a
certificate supported on at most **k+1 points** (k the **control** dimension), tight.
Polyhedral case recovers the ℓ1-normalised Farkas pair; singleton case recovers the Isaacs
drift with the adversarial *distribution* load-bearing. A two-action instance exhibits a
**strict minimax gap**: without convexity the equivalence fails and **no measure certifies**.
Machine-verified in exact rational arithmetic, 8 check families.
Labels: `thm:dual`, `prop:sparse`, `prop:recover`, `prop:gap`, `thm:benchmark`, `lem:bridge`,
`thm:envelope-finite`, `prop:recourse-id`, `prop:tower`, `prop:strict`, `prop:refine`,
`thm:general`.

## The honest baseline: this IS the discriminating-kernel question

**The main concession.** The discriminating kernel (Aubin 1991; Aubin & Catté 2002;
Cardaliaguet, Quincampoix & Saint-Pierre 1994, 2007) is the largest closed subset of the
constraint set that is a discriminating domain — Victor's victory domain, characterised as the
largest/smallest/**unique minimax** (bilateral) fixed point of an adequate map, computed by a
descending-kernel algorithm.

**Paper 4's obstruction is the emptiness of that object.** `thm:dual` is, in that programme's
vocabulary, a certificate for the discriminating kernel being empty. This is a real collision
and the text concedes it rather than arguing around it.

## What survives (four items)

1. **The certificate is a measure, not a set.** That programme returns a *subset of state
   space* via a set iteration. `thm:dual` returns a finitely supported *probability measure*;
   membership in a kernel becomes existence of a checkable dual object.
2. **The support bound and its tightness.** `prop:sparse`: at most k+1 points, k the
   **control** dimension — the witness count scales with the *instrument* space, not the state
   space. Nothing in the fixed-point characterisation yields a finite witness.
3. **The convexity boundary is located exactly where the kernel programme puts it, from the
   other side.** **CQS 1994 Proposition 2.3: under convexity, the discriminating kernel IS
   convex.** Paper 4's `prop:gap` is the complementary negative. Together they show convexity
   is load-bearing in the strongest sense — it is simultaneously what makes kernels convex and
   what makes measure duality sound.
4. **One-sided and observation-constrained.** The kernel programme computes a victory domain
   in both directions; paper 4 certifies only the negative. That narrowing is what buys items
   1 and 2, and is stated as a narrowing, not an improvement.

## The five neighbour groups

1. **Discriminating-kernel programme** — Aubin (1991) *Viability Theory*, Birkhäuser;
   Aubin (2001) *SIAM J. Control Optim.* **40**(3), 853–881; **Aubin & Catté (2002)
   *Set-Valued Analysis* **10**, 379–416** (verified: doi 10.1023/A:1020667819804);
   **CQS (1994) *RAIRO/M2AN* **28**(4), 441–461** (the algorithm paper, source of Prop 2.3);
   CQS (2007) *Advances in Dynamic Game Theory*, Ann. ISDG 9, 3–35, Birkhäuser.
2. **Farkas / LP duality** — Farkas (1902), already cited. Classical alternative, finite and
   static; the generalisation is to measures over a boundary–disturbance bundle and to the
   emptiness of a set of *simultaneously* safe actions. The polyhedral recovery
   (`prop:recover`) is a consistency check, not the generalisation.
3. **Isaacs / HJI** — Isaacs (1965), already cited. Classical value as a function of state
   under full observation versus a one-directional refutation over an information set; the
   adversarial *distribution* is what carries the singleton case.
4. **Differential games under incomplete information on the space of measures** —
   **Cardaliaguet & Quincampoix (2008), *Int. Game Theory Rev.* **10**(1), 1–16**. The single
   closest neighbour: players know only a distribution on the initial state; value exists via
   HJI uniqueness **on the space of measures**. Difference: that is an analytic *existence*
   result in an infinite-dimensional setting; paper 4 gives a *finite certificate*, k+1 points,
   exactly checkable. Existence-and-uniqueness yields no finite witness. **This reference was
   NOT in the roadmap — found during this pass.**
5. **Minimax equality** — **Sion (1958), *Pacific J. Math.* **8**(1), 171–176**
   (doi 10.2140/PJM.1958.8.171). `thm:dual`'s equality in the convex case is arguably an
   instance of this classical circle, and the paper claims no origination of the equality.
   What Sion does not supply is the **sparse witness** and its tightness. Symmetrically,
   `prop:gap` is consistent with it: minimax equality is what fails when convexity is dropped.

## Two citation traps handled

- **Aubin and Catté** — accented, *not* "Catte". Verified against the Springer record; the
  `.tex` carries a warning comment not to strip the accent.
- **A dropped claim.** The roadmap inherited a note attributing to Aubin (2001) "the
  complement of the kernel — Poincaré's shadow". **This could not be verified** and is
  **not asserted**. Aubin (2001) is cited only for the verified fixed-point characterisation
  of kernels and capture basins. This is the right call — an unverified attribution is worse
  than a missing one.

## Checks

- All 12 `\ref` targets resolve; zero missing.
- All cited labels verified present: `thm:dual`, `prop:sparse`, `prop:recover`, `prop:gap`,
  `thm:envelope-finite`, `prop:tower`, `prop:strict`, `thm:general`, `thm:benchmark`,
  `priorart`.
- Braces balanced in the inserted block (58/58).
- All seven new bibliography entries verified against publisher records.

## Result

`paper04_minimax_dual_certificates_v14.tex`: 6,508 → 8,397 words (+29%).

## Note on the bar table

Paper 4 was the thinnest of the eleven at 6,508 words with 10 years and 10 author-initials —
the highest-risk of the 2/3/4 group. It is now 8,397 words with a conceded prior-art position
and a sharpened five-item claim. The residual risk is different in kind now: not "no prior
art" but "does the measure form plus the tight k+1 bound plus the located convexity boundary
constitute enough for a top journal". That is an editorial judgement, not a checkable one.

Next: 9, 10, 11.

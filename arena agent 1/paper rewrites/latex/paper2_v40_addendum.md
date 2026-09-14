# v40 — Pass C: probabilistic instance, timing checkability, post-recourse example

## Changes

1. **GAP 5 (worked POMDP instance) + correctness fix.** Proposition 9
   (degenerate limit) previously concluded "V_k(b) -> 0" for B notin W_k, which
   is not derivable from its hypotheses for an averaged initial belief (the
   two-floor conflict gives V_k = 1/2, not 0). The statement is corrected to
   the deterministic-kernel reading: the posterior support equals Post(B,a,y);
   V_k(b) = 1 iff B in W_k, and if B notin W_k then V_k(b) <= 1 - min_x b(x) < 1,
   with the proof rewritten to match. A worked instance (the two-floor conflict
   as a finite POMDP) is added at the end of Section 9, showing V_k(b_0) = 1/2
   attaining the chance-constrained bound of Proposition 8 exactly.

2. **GAP 6 (timing checkability).** Added a "Checkability of the timing
   certificate" paragraph in Section 3.3: for finite blind-window control
   classes the drift hypothesis is a finite check (branchwise integration or
   the Section 3.1 recursion), the hidden-regime instance being its closed form
   (sigma* = z0 - 1); for continuous control classes it remains a template and
   is folded into Open Problem 1.

3. **GAP 7 (post-observation recourse).** Added A.3 to the supplementary: a
   three-state system with root belief B_0 in W_1 but not in W_2, where the
   failure is located at the post-observation belief (state x_4 in V but
   outside the kernel), no certificate fires at the root, and only the
   recursion witnesses it. Section 6.5(ii) now points to it, making the named
   limitation concrete.

## QA

- Main: 16 pages, 4 images, 0 `??`, no overfull, abstract 262 words.
- Supplementary: 13 pages, 3 images, 0 `??`.
- Numbering unchanged and complete: Theorems 1-7, Propositions 1-9,
  Remarks 1-4; the corrected Proposition 9 statement renders with no stray
  "-> 0" clause.

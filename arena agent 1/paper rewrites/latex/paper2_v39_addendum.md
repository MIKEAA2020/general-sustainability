# v39 — Pass B: Helly scope counterexample + worked method comparison

## Changes

1. **GAP 4 (Helly hypothesis boundary).** Added a "Scope of the convexity
   hypotheses" paragraph in Section 3.4, after the worked two-floor
   certificate: a three-set example in a single control dimension
   (R₁={0,1}, R₂={0,2}, R₃={1,2}) with pairwise nonempty but empty total
   intersection, showing that without convexity no (m+1)=2-state witness
   exists. Convexity is now stated as excluding exactly this failure mode.

2. **GAP 3 (worked method comparison).** Added "A worked comparison: barrier,
   estimation-tube, and obstruction certificates on one system" to the
   supplementary (S2), using the paper's own two-floor system: what the
   barrier programme can/cannot say (no state to feed back -> "no barrier
   found", ambiguous), what the estimation-tube reduction returns (empty
   belief-state kernel, as a black box), and what the obstruction certificate
   delivers (the explicit Farkas multiplier λ=(1/2,1/2), margin 0.1, and the
   design remedy). A one-sentence pointer was added at the end of Section 6.3.

## QA

- Main: 15 pages, 4 images, 0 `??`, no overfull, abstract 262 words.
- Supplementary: 13 pages, 3 images, 0 `??`.

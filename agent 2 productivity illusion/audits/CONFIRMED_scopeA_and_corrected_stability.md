# Confirmed scope-A + corrected stability (fixes the false "vicious cycle for every delay")

**Purpose.** Confirm the scope-A direction and give the numerically-verified form of the corrected stability
claim, so the false "positive real eigenvalue for *every* delay" statement can be fixed on honest ground.
Every number below is reproduced from `model_sims/char_eq.py` (the registered S0 linearisation), not asserted.

---

## 1. The model being analysed (S0 deficit-regime linearisation)

States `A, P, D`; biocapacity `B = b₀A + b_G G(A)`; equilibrium family `P* = K(A*) = B(A*)/e` (one-parameter,
the neutral continuum). Deviations about `(A*, P*)`:

```
a1 = G'(A*)            (regeneration, delayed τ_g)
a3 = b₀/b_G = 1/V      (depletion, current)   <-  V = b_G/b₀  (CORRECT identity)
aE = -e/b_G            (depletion→P, current)
a4 = r K'(A*)          (carrying capacity, delayed τ_p)
a5 = -r                (logistic damping, current)
D(s; τ_g,τ_p) = (s − a1 e^{−s τ_g} − a3)(s + r) − aE·a4 e^{−s τ_p} = 0
```

## 2. The τ=0 closed form (the C0 transverse root)

Setting τ_g=τ_p=0 and using `aE·a4 = −r(1/V + G′(A*))`:

```
D(s) = (s − G′ − 1/V)(s + r) + r(1/V + G′) = s[ s + (r − G′ − 1/V) ]
  -> eigenvalues  s = 0  (neutral continuum, the one-parameter family)
                  s_TR = G′(A*) + 1/V − r   (the transverse / monotone root)
```

Note the manuscript's own condition `b/b_G + G′(A*) > r` **is** `1/V + G′ > r` — i.e. it **is** the sign
condition on `s_TR`. So the *inequality* is right; the defect is that it was asserted as **universal** rather
than as a **condition on V**.

## 3. Verified honesty sweep (genuine positive root, discriminated from the s=0 continuum)

`b_G = b₀·V` (option-b physical identity), representative A\* = MSY = A_max/2 (G′=0), τ_p=25.

| V (yr) | genuine positive real root | ≈ 1/V |
|:-----:|:--------------------------:|:-----:|
| 1.6 | **+0.625** | 0.625 |
| 5 | +0.1999 | 0.200 |
| 10 | +0.0986 | 0.100 |
| 20 | +0.0450 | 0.050 |
| 30 | +0.0256 | 0.033 |
| 40 | +0.0154 | 0.025 |
| 50 | +0.00896 | 0.020 |
| 60 | +0.00454 | 0.017 |
| 80 | **none** | 0.013 |
| 100 | **none** | 0.010 |

**V_crit (root vanishes) = 74.98 yr**, and it is **exactly delay-independent**:

| τ_g (yr) | V_crit (yr) |
|:-----:|:-----:|
| 0, 5, 10, 20, 40, 60, 80 | 74.98 (all identical) |

So the positive real eigenvalue is a **structural, monotone** instability (no delay-tuning, no Hopf), and it is
**present for V < ~75 yr** and **absent for V ≳ 75 yr**.

## 4. The corrected claim (what the abstract must actually say)

1. **Identity:** `V = b_G/b₀` and `γ = 1/b_G ≠ 1/V` (fix the units). The honest baseline implied by the
   manuscript's own parameters is `V = b_G/b₀ = 0.8/0.5 = 1.6 yr` — **not** the 20–100 yr the text claims.
2. **The structural vicious cycle is real and monotone.** At the honest baseline `V=1.6 yr` the S0 equilibrium
   carries a positive real eigenvalue `s ≈ 1/V = +0.625`, and it is **identical for every delay** τ_g ∈ [0,80]
   (and τ_p=25). So "structural, not delay-tuned" is correct.
3. **But it is a sufficient condition on turnover, not a universal.** The root is positive iff
   `1/V + G′(A*) > r`, i.e. iff `V < V_crit ≈ 75 yr` (`V_crit ≈ 1/(r − G′)` at the linear level; the exact
   value at MSY at r=0.02 is 74.98 yr). It must be stated *as a condition on V*, not "for every interior point /
   every parameter set."
4. **At forest scale it dies.** For V ≳ 75 yr — the manuscript's *claimed* forest regime (V≈20–100) upper end —
   **no positive real eigenvalue exists for any delay** (only the s=0 continuum). The universal reading of the
   claim is false there; the honest reading (`V=1.6`, fast turnover) it is true.

## 5. What scope-A does and does not fix

- **scope-A (two-land conversion / multi-component aggregate)** makes the *masking* **generic** (Proposition 1):
  the aggregate `B` can rise while a critical component falls, for essentially any parameters — this is the
  "productivity illusion is structural, not a 5-yr window" reframing. This part is **V-independent**.
- **The monotone debt-vicious-cycle** (`s_TR`, the +0.625) is a **separate, V-restricted** result — it is the
  *fast-turnover* signature. It is NOT fixed by scope-A; it is fixed by stating the sufficient condition on V
  and by using the honest baseline V=1.6.

## 6. The honest division of labour (this is the key takeaway)

- **fast turnover (small V, orchard/crop/pelagics; honest baseline V=1.6):** the structural *monotone*
  collapse holds — ECOMOD's signature result. Claim is TRUE once V is pinned to 1.6.
- **slow turnover (large V, forest; V ≳ 75):** the monotone root vanishes; collapse is instead
  *delay-amplified* (Hopf / bistable windows) — which is **paper4 / v18's** domain.

So ECOMOD should be positioned as the **fast-turnover** companion in which the debt-driven monotone vicious
cycle holds, and explicitly hand the slow-turnover, delay-amplified regime to paper4/v18. This makes the two
genuinely complementary rather than overlapping, and keeps ECOMOD's headline honest and defensible.

*Verified with `char_eq.py`; no manuscript modified. Read-only decision note.*

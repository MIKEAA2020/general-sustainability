# P4 exact-hold monodromy — verified derivation and paper insertion (2026-08-31)

Item: the separating computation that P4 Section 7 explicitly declared unresolved —
"Whether the crossing is a property of review cadence or of the explicit-Euler command
step is unresolved: the separating computation is the exact held-measurement update, and
until it is reported the result is stated for the declared Euler-reviewed operator only."
Standing rule: new math enters papers only after verification. Script:
`p4_exact_hold_monodromy.py` (this folder); model reconstruction from
paper4_delay_dynamics_v2.md Sections 2–3 only.

## 1. Validation gate — committed Euler numbers reproduced

Model reconstructed from the paper's own formulas (Candidate A):
- Equilibrium: E* = 2.089623 (paper ~2.08962), N* = 89.551883 (paper ~89.55188), Z* = δ = 0.069315.
- Jacobian: A_N = −0.017910, A_E = −0.089552, B_N = 0.001791, B_E = 0.008955, d = 0.2.
- Gains: mobilising C_E = −0.059518, C_Z = +1.785019 (paper −0.0595, +1.785);
  protective C_E = −0.850336, C_Z = −1.661702 (paper −0.850336, −1.661702).
- Euler monodromy M = R_Euler·exp(A_hold T_r), R_Euler[3,:] = (0, T_r·C_Z, 1 + T_r·C_E):
  * protective ρ(1) = 0.983796 (paper 0.9838); ρ = 1 crossing at 2.3064 yr, real −1 (paper ≈2.306). ✓
  * mobilising ρ(1) = 1.000545 (paper 1.00055); crossings at 47.535982 yr (complex pair
    0.1893 + 0.9819i, |λ| = 1) and 79.143836 yr (real −1.0004) (paper 47.536 / 79.143). ✓
All committed values reproduced → the reconstruction is the committed operator.

## 2. Exact held-measurement update — the new math

Same architecture, same flow-then-update timing convention, one change: the effort law
ė = C_E e + C_Z z is integrated exactly with the measurement held at the flowed
end-of-period value. Update factor: e_{k+1} = e^{C_E T_r} e_k + ((e^{C_E T_r}−1)/C_E) C_Z z⁻.
Consistency limit verified numerically for both schemes: (M(T_r) − I)/T_r → J_cont
(error 3.6e-6 / 4.1e-6 at T_r = 1e-5 for Euler/exact — first-order in T_r as stated).

Results (grid [0.2, 300] yr, 400001 points, crossings refined by bisection to ~1e-6):

| channel | quantity | Euler (committed) | exact held-measurement |
|---|---|---|---|
| protective | ρ(1) | 0.9838 | 0.98381 |
| protective | ρ = 1 crossings | 2.306 yr (real −1) | none; max ρ = 0.99674 (at T_r = 0.2) |
| mobilising | ρ(1) | 1.00055 | 1.00035 |
| mobilising | ρ = 1 crossings | 47.536 yr (complex pair), 79.143 yr (−1) | one: 6.5023 yr (complex pair) |
| mobilising | ρ at 47.536 / 79.143 | 1.000 / 1.000 | 0.7858 / 0.5970 |

Protective: the exact-hold map is stable at EVERY tested review interval (max ρ = 0.9967,
the approach to the continuous limit at short T_r; protective J_cont is Hurwitz, verified
all three eigenvalues negative). The 2.306-yr crossing vanishes → confirmed by direct
computation as a pure explicit-Euler command-step artefact (the Euler factor 1 + T_r C_E
with C_E = −0.850 is replaced by e^{C_E T_r} ∈ (0,1), a strict contraction).

Mobilising: annual-review instability SURVIVES the exact update (ρ = 1.00035, consistent
with 1 + maxRe(J_cont) = 1.00036 — the undelayed linearisation is unstable, Section 5.1).
The Euler crossings do NOT survive (exact ρ = 0.786 / 0.597 there) — command-step
artefacts. The exact map's single unit-circle crossing on [0.2, 300] yr is the
restabilising complex pair at T_r = 6.5023 yr: eigenvalues 0.984635 ± 0.174619i
(|λ| = 1), third eigenvalue 0.164696 inside the disc, non-resonant argument
(2π/θ ≈ 35.8, not 2π/3, 2π/4, 2π/5), transverse (ρ − 1 changes sign: 1.0000009 at
6.5 yr → 0.999994 at 6.51 yr). The restabilisation direction survives with the crossing
relocated from 47.5 yr to ≈6.5 yr — the qualitative governance finding ("lengthening
review restabilises") is cadence-driven, not a command-step artefact. Convention
robustness: holding the measurement at the start-of-period value instead gives identical
crossing locations at the reported precision (both channels).

## 3. Paper insertion — paper4_delay_dynamics_v3.md (= v2 + 14 surgical edits)

1. Abstract: hold-sampling sentence updated with the exact-hold numbers; stray "  --" removed.
2. Contribution #5 updated (exact ρ values; crossing at 6.50 yr; Euler crossings flagged as artefacts).
3. §6.4: the "belongs to the discretisation" finding now carries its separating computation.
4. §7: the unresolved sentence replaced by the resolution; contrast sentence updated.
5. New Proposition 7 (Exact held-measurement monodromy) inserted at the end of §7: update
   formula, consistency limit, protective (i) and mobilising (ii) outcomes, proof and
   verification-status note; equation tag (13).
6. Renumbering: existing Proposition 7 (Logistic identification, §9) → Proposition 8
   (sole occurrence; no cross-references affected). §9 equation tags (13)→(14), (14)→(15)
   with both textual references updated; the tag sequence is now 1–15, sequential, no
   duplicates (machine-checked).
7. §10 discussion: protective and mobilising review-interval sentences updated.
8. Limitations (iii): the sample-and-hold scope now names both schemes (Theorem 5, Proposition 7).

Integrity battery: 1908 $ delimiters even; 14905 → 15595 words (+690, all attributable);
28 changed diff lines reviewed against v2; both remaining "unresolved" occurrences are the
§8 homoclinic/fold items (legitimate, untouched). Neimark–Sacker discipline preserved:
nonlinear conditions not verified — the name is reserved exactly as in Theorem 5.

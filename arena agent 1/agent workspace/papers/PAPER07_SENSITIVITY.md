# Paper 7 — sensitivity of the 6.501-yr crossing, computed 2026-09-29

## The gap

Bar assessment: "headline 6.5-year figure moves 55% under a 0.2% change in the exploitation
ratio; needs a sensitivity band, not a point." The paper had sensitivity *language* but no
computed band — "exploitation ratio", "condition number" and "ill-conditioned" appear
nowhere in v48.

## Method

The paper's own Candidate A reconstruction was recovered from the remote —
`arena agent 1/other documents/rerun_campaigns/campaign_p5_crossing_scan.py` — rather than
reverse-engineered from the prose. Reproduced before perturbing anything:

```
mobilising exact  rho(1) = 1.00035   (paper 1.00035)
mobilising Euler  rho(1) = 1.00055   (paper 1.00055)
protective Euler  rho(1) = 0.9838    (paper 0.9838)
crossing          = 6.5013 yr        (paper 6.501)
drho/dT           = -6.834e-04       (paper -0.000683)
```

Exact model: `r, K, q = 0.02, 100.0, 0.001`; `eta, Emax, dref = 0.914, 30.0, 1.0`;
`d0, tm, Zref = 0.01, 5.0, 1.0`; `delta = ln2/10`. Monodromy = review matrix × `expm(A_hold·T)`.
Script: `/home/user/p7/sensitivity.py`.

## Results

### One-at-a-time (±1% / ±2%)

| parameter | −2% | −1% | +1% | +2% | worst finite 2% swing |
|---|---|---|---|---|---|
| K | none | 2.99 | 8.67 | 10.37 | 59.5% |
| q | none | 3.44 | 8.50 | 10.10 | 55.4% |
| Emax | none | 3.45 | 8.50 | 10.10 | 55.3% |
| eta | 5.27 | 5.92 | 7.02 | 7.49 | 18.9% |
| r | 7.35 | 6.94 | 6.04 | 5.55 | 14.6% |
| dref | 10.78 | 8.89 | 2.35 | none | 65.7% |
| tm | 6.60 | 6.55 | 6.45 | 6.39 | 1.6% |
| d0 | 6.50 | 6.50 | 6.51 | 6.51 | 0.1% |
| Zref | 6.51 | 6.50 | 6.50 | 6.50 | 0.1% |

The final column is the largest **finite** ±2% endpoint crossing shift as a
percentage of the unperturbed 6.5013-year crossing. An endpoint marked "none"
has no detected crossing on [0.2, 200] yr at the tested grid resolution; it is
not a finite displacement. For dref the −2% endpoint supplies the 65.7% shift,
while the +2% endpoint is "none". The K, q and Emax shifts exceed 50% at ±2%,
not all at ±1% (actual ±1% values: 54.08%, 47.12%, 47.02%).

### Joint boxes over the six influential parameters (2^6 = 64 corners)

| box | corners with a crossing | range | as % of baseline |
|---|---|---|---|
| ±0.5% | 60 / 64 | 0.87 – 10.67 yr | −87% to +64% |
| ±1% | 44 / 64 | 4.42 – 13.65 yr | −32% to +110% |

At ±1%, **20 of 64 corners lose the crossing entirely** (loop stable at every interval).

### Conditioning

`drho/dT = -6.834e-04` per yr at the crossing ⇒ an error of 1e−3 in rho displaces T by
**~1.5 yr**. Baseline `rho(1) - 1 = 3.5e-04`.

## The finding

**The crossing is not identifiable, and the qualitative verdict is fragile, not just the
number.** Four parameters perturbed by 2% in the stated directions remove the crossing
altogether: the loop is stable at every tested interval, so "annual review is unstable and
the loop restabilises above a threshold" is not numerically displaced but false. The sign
of `rho(1) − 1` is 3.5e−04 at baseline — that is the whole margin.

## What was written

`paper07_sampled_governance_v49.tex`:
- new **§3.5** with Table `tab:sens` (one-at-a-time), the joint boxes, the conditioning
  calculation, an explicit statement of what is and is not reported, and a "what survives"
  paragraph.
- abstract amended to point the 6.5 figure at §3.5 and name the band.

Deliberately **not** reported as a confidence interval: the parameter uncertainties are
conventions, not measurements with a sampling distribution. A CI would be an assumption
dressed as an inference.

## What survives (and carries the paper)

1. The **operator contrast** — Euler artefacts at 47.536 / 79.143 yr vs the exact update.
   Verified independently of the crossing location.
2. The **protective channel** — stable at every tested interval, max rho 0.9967,
   minimum tested-grid stability margin about 0.0033. The annual mobilising
   instability excess is about 0.00035; these are different interval sets, not
   evidence for a three-orders-of-magnitude ratio.
3. The **multiplicity-controlled screen** finding no robust institutional cycles — a null
   result, independent of the crossing value.

## Residual risk

A referee may reasonably ask whether a paper whose headline number admits a 1–11 yr range
has an empirical contribution at all at that point. The honest answer is that the
contribution there is the operator contrast and the null screen, and the crossing is
illustrative. §3.5 now says so. If the 6.5 figure is load-bearing for the paper's framing
elsewhere (it is cross-referenced by paper 8, which was told to cite rather than re-derive
it), paper 8's use of it must be re-examined too.

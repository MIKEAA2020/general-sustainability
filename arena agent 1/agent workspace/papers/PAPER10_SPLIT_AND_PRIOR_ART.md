# Paper 10 — split into two papers, prior art added, 2026-09-30

## Systemic discovery: three papers were multi-document concatenations

Scanning the whole set for the paper-9 failure mode found it twice more:

| file | `\documentclass` | `\begin{document}` | `\end{document}` |
|---|---|---|---|
| `paper09_cod_certification_v30.tex` | 2 | 2 | 2 |
| `paper10_depletion_ledgers_v51.tex` | 2 | 2 | 2 |
| `paper11_forecasting_baselines_v61.tex` | **3** | **3** | **3** |

Papers 1–8 are clean. In every case the `\part` merge marker (`E2`/`Arv`, `E4`, `E3`/`Ws`)
sits in the **gap between documents** — outside any document — which is why the merge never
worked. Paper 9 was fixed in the previous turn; paper 10 here. **Paper 11 (three documents)
is still outstanding.**

## Paper 10's defect

`v51` = two complete LaTeX documents, and it **did not compile at all**.

| | Part I (Typed Flux Ledgers) | Part II (Edwards Aquifer) |
|---|---|---|
| `\documentclass` | `[11pt]{article}` @ 1,686 | `[11pt]{article}` @ 236,809 |
| `\end{document}` | 235,852 | 299,278 |
| words | 34,258 | 8,530 |
| title | *Typed Flux Ledgers and Depletion Arithmetic* | *Governance operators and viability kernels of the Edwards Aquifer: a J-17 test* |

**Compile proof (tectonic, figures stubbed):**

| file | pages | PDF |
|---|---|---|
| `v51` (merged) | **NO PDF** | 0 B |
| `v52` (Part I) | **55** | 393,179 B |
| `v1` (Part II) | **17** | 131,022 B |

Both new files: **zero undefined references, zero LaTeX errors.**

## Why split, on content and merits

Zero overlap on every distinctive term:

| marker | Part I | Part II |
|---|---|---|
| `ledger` / `typed` / `compartment` | 135 / 35 / 79 | **0 / 0 / 0** |
| `stoichiometric` / `phosphate` | 15 / 19 | **0 / 0** |
| `flux` / `conservation` | 89 / 66 | 1 / 3 |
| `Edwards` / `J-17` / `pumping` | **0 / 0 / 0** | 22 / 14 / 70 |
| `trigger` / `governance operator` | 1 / 0 | 36 / 4 |

Part I never mentions Edwards; Part II never mentions ledgers. Part I is a general typed
stock–flow accounting framework (moieties, conservation, componentwise deficits, depletion
arithmetic across groundwater, phosphate and fisheries). Part II is a single-aquifer
empirical viability-kernel study. Two papers.

## Result

- `paper10_depletion_ledgers_v52.tex` — Part I, 34,903 words, 55 pp.
- `paper10b_edwards_aquifer_v1.tex` — Part II, 9,326 words, 17 pp.

`v51` preserved untouched.

## Prior art — Part I (`v52`)

New `\subsection*{1.4 Related work}`.

1. **Material / substance flow analysis — NEW.** Brunner & Rechberger (2016), *Handbook of
   Material Flow Analysis*, 2nd ed., CRC Press. The established discipline for closing
   stock–flow balances. **What is added is typing:** conserved moieties are tracked
   independently and never summed across types, so the paper's central negative result —
   that compensatory scalar aggregation masks critical physical deficits — is a *prohibition
   on a step MFA routinely performs*. Not a new way to close a balance; a typing discipline.
2. **Ecological stoichiometry — NEW.** Sterner & Elser (2002), Princeton University Press.
   The moiety bookkeeping and stoichiometric conservation of §4 are the same idea carried into
   depletion accounting; Redfield-type ratios are the canonical instance.
3. **Reserve-life / R:P / the "time to depletion" confusion — NEW.** Hubbert (1956),
   *Drilling and Production Practice*, API, 1–57; Bartlett (2000), *Math. Geol.* **32**(1),
   1–17. The paper's opening problem is that reserve-life ratios, trend-persistence metrics
   and gross-removal pressure scales are all reported in years and read as one quantity. The
   positioning: **the confusion is not a property of one badly-behaved indicator but a symptom
   of leaving the indicator untyped.**
4. **Viability theory** — Aubin (1991), cited in passing for the constraint-satisfaction
   framing.
5. **Two-cell aquifer modelling — NEW.** Augeraud-Véron & Pereau (2022). Their result — that
   a one-cell bathtub model allocates too much water to extraction at the expense of
   groundwater-dependent ecosystems, so conductivity and multi-cell structure must be
   represented — is the direct antecedent of the two-pool gap in §8.2.

## Prior art — Part II (`v1`)

New `\subsection{Related work}`.

1. **The regulatory object.** Verified against EAA and EARIP documents: **the J-17 index well
   is the official regulatory trigger for Critical Period Management**, and **the paper's
   660-ft level is the real Stage I trigger** (J-17 < 660 ft MSL → 20% withdrawal reduction,
   San Antonio Pool, rising to 40% at Stage IV; Uvalde Pool staged separately on J-27;
   permitted withdrawals capped at 572,000 ac-ft/yr). So the results read directly as a
   statement about the instrument in force rather than an arbitrary level.
2. **Viability applied to groundwater — NEW.** Pereau, Pryet & Rambonilaza (2019), *Ecol.
   Econ.* **161**, 109–120 (optimal control with environmental flows as externality vs viable
   control with them as constraint); Pereau, Mouysset & Doyen (2018), *Environ. Resour. Econ.*
   **71**(2), 319–336 (kernel identified analytically); Oubraham & Zaccour (2018) survey.
   **What is added is the robust element and the geometry of the trigger:** kernels computed
   against a persistent drought-floor recharge, and the negative finding that nothing is
   retained at 660 ft because the rules are invisible to the kernel of their own trigger — a
   question about the relation between a trigger level and the reachable set under it, which
   that literature does not ask.
3. **Safe yield → sustainability: a conspicuous omission, now engaged.** The term "safe yield"
   appears **zero times** in this manuscript, yet the safe-yield critique is the classical
   groundwater-sustainability literature most directly analogous to its central finding. Now
   cited: Sophocleous (1997), *Ground Water* **35**(4), 561 — safe yield is unsustainable
   because it ignores the natural discharge that recharge already supports; Alley, Reilly &
   Franke (1999), USGS Circular 1186; Sophocleous (2000), *J. Hydrology* **235**, 27–43;
   Alley & Leake (2004), *Ground Water* **42**(1), 12–16; Devlin & Sophocleous (2005),
   *Hydrogeol. J.* **13**, 549–554. The paper's finding — that a positive
   attractor-to-threshold margin defeats every non-negative pumping rule, so 660 ft is
   protected by wet years rather than by policy — is identified as **the robust-viability
   analogue of the safe-yield critique**.
4. **Viability theory** — Aubin (1991).

## Verification

- Both files: exactly 1 `\documentclass`, 1 `\begin{document}`, 1 `\end{document}` after
  stripping comments.
- All `\ref` targets resolve (Part I 1 ref; Part II 0 refs — neither half used cross-refs).
- Compiled: 55 pp and 17 pp, zero errors, zero undefined references.
- The single "not found" log line in each is the benign `pdftexcmds` info message about
  `\pdfdraftmode`, not a missing asset.
- Stub figures were created only under `/tmp/p10`; none written into `/home/user/papers`.

## Tool note

Tectonic had lost its exec bit again mid-session (`Permission denied`); re-`chmod +x` fixed it.
This has now happened twice.

## Next

**Paper 11 is three concatenated documents** (`paper11_forecasting_baselines_v61.tex`) —
Northern cod forecasting (20,048 w), Edwards Aquifer forecasting (8,819 w), and Exact Audits
of Worked Systems for the Obstruction Calculus (10,374 w, `\part{Ws}`). `ws` is a separate unit
in the authoritative eight-paper scope.

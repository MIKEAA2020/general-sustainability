# D-Tier — Empirical Agenda

## Readiness matrix

| Criterion | Groundwater (A005) | Phosphorus (A004) | Fisheries resource–sink (A001 §6) |
|---|---|---|---|
| Data availability | High (geological surveys) | Moderate (agricultural) | High (RAM legacy, ICES) |
| Observation model | Direct (well levels) | Indirect (soil tests) | Model-based assessments |
| Governance records | Available (permits, metering) | Moderate (subsidies, regulations) | Available (quotas, seasons) |
| Calibration feasibility | Blocked (constitutive curves need lithology data) | Blocked (jump balance undefined) | **Ready — on the LINEAR module only (E5: linear, closed-form kernel). The real-system tracks (G1a: the 2J3KL cod fishery; G1b: an Edwards J-17-type aquifer system) are NOT calibration-ready: each is gated on the R04 admission of the corresponding scored model (or Cor2 approximate admission — for the Edwards-type system, forecast-map only), neither constructed** |
| Code provenance | Moderate | Weak | **Complete (E5 script + JSON committed)** |
| Admission status | Conditionally admissible (5 blocking items) | Conditionally admissible (5 blocking items) | **ADMITTED WITH NUMBERS — linear module only** (E5 committed, SHA-256: 5670bcc8...; toy scope; real-system transfer gated on R04/Cor2 — see the two-track decision below) |

## Decision: fisheries resource–sink as the primary G1 case — **two-track reading (mandatory)**

**Track 1 (method, READY):** the linear A001 §§6–10 resource–sink module is admitted with interval-verified numerical constants (`research_program/validated_computations/E5_NUMBERS.json`): margins α_S=0.4, α_K=0.2, Lipschitz L=0.2, erosion menu with exhibited triple L=0.2/r=0.05/Δ≤0.18, confinement [2,8]×[0,2], and a displayed (REG) certificate family on the infinite horizon. **These numbers are the linear toy's — they support no claim about the real fishery.** This track delivers the admission method, the screening template, and the worked example.

**Track 2 (real systems, GATED):** the empirical case against a real system requires, before any certified claim:

- **G1a (fisheries):** scored in [`wave_e_cod/`](../../wave_e_cod/) (\(\Omega_{2016}\), \(\Omega_{\mathrm{xte}}\)). Persist wins; no M2–M4 retained. A001/A014 admission does **not** transfer E5 numbers onto NCAM SSB. Kernel certificate for the surplus ladder: **not constructed**.
- **G1b (groundwater):** scored in [`wave_e_edwards/`](../../wave_e_edwards/) (\(\Omega_{\mathrm{SA}}\), J-17 annual mean). Persist / thin M1; causal stock-flow rejected. A005 two-pool blockers remain open. Cor2 exists **only** as `wave_e_edwards/admission/R04_Cor2_edwards_H0.md` (forecast map, not a kernel). The “confound-gate rejection” of Edwards is **withdrawn** — no such manuscript is in this repository.

By R04.Thm1's converse, no judgment transfers without one of these; verbal analogy is excluded from transfer by the theorem itself. This is a **Wave-0 gating item** (see PUBLICATION_STRATEGY.md and TRANSFER_AUDIT_RESPONSE.md Finding 2).

### The three objects (mandatory disambiguation)

The earlier shorthand "2J3KL / J-17 scored models" collapsed three distinct objects and is **retired**:

| Object | Kind | In-repo path | R04 / Cor2 | Independent rerun |
|---|---|---|---|---|
| NAFO **2J3KL** | fisheries \(\Omega_{2016}\), \(\Omega_{\mathrm{xte}}\) | `wave_e_cod/` | A001/A014 class admitted; E5 does not transfer; surplus-ladder Cor2 not constructed | **NONE** |
| Edwards well **J-17** | groundwater \(\Omega_{\mathrm{SA}}\) | `wave_e_edwards/` | two-pool not constructed; H0 forecast-map Cor2 only | **NONE** |
| A021 C4 **J-series** | docket + DDE, not a basin | `research_program/validated_computations/a021_c4/` | not a Wave E forecast \(\Omega\) | **NONE** |

A021 J-series is external-review bookkeeping. It is not Edwards J-17 and not 2J3KL.

"All mathematics is in place" refers to Track 1's method chain (admission template + E2 selection + E7 barriers + B1 erosion + C-a decidability). It does **not** mean the real-system transfer exists.

## Three preregistered protocols

| Protocol | Tests | External obligations |
|---|---|---|
| H1: observation aggregation | Aggregate-only certification misclassifies component safety | Reference R01.Thm2/R03.Thm3 witnesses; external check vs. compositional-verification literature (E6 row) |
| H2: governance phase ordering | Extractive vs. protective controllers have opposite-signed phase relations; deployment delay shifts the relation | Reference the certified Floquet data (C4 monodromy); external check vs. closed-loop identification literature |
| H3: substitution certificate | Dual infeasibility certificates predict service shortfalls better than aggregate elasticities | Reference A002 thm:farkas; external check vs. constrained-optimization diagnostics |

## A004/A005 blocking-list completion plan

| Blocking item | Action | Owner |
|---|---|---|
| V-A005-04 (q_rel routing) | Declare the recharge partition from hydrogeology | author |
| V-A005-05 (leakage limiter) | Specify the limiter functional; verify positivity | author |
| V-A005-06 (storage + jump identities) | Close the DAE jump balance (E4 jump-margin template) | author |
| V-A005-07 (donor/recipient positivity) | Verify on the declared constitutive curves | author + data |
| V-A005-11 (compatible-state topology) | Hausdorff-continuity check (E2 machinery) | this programme |
| V-A004-03 (hybrid jump balance) | A3 transversality declaration on the event surfaces | author |
| V-A004-05 (χ definition) | Declare the functional dynamics | author |
| V-A004-06/08/09 | Upper bound, trade routing, topology | author + this programme |

## Sequencing

Track 1 (G1a-method) proceeds now — the admission method is committed with numbers on the linear module. **Track 2 (real systems: G1a fisheries / G1b Edwards-type groundwater) activates only after the R04/Cor2 transfer certificate is constructed for the corresponding scored model (for an Edwards-type system, Cor2 is forecast-map only)** — that construction is the next programme-side action on the empirical track. The groundwater track (G1b) activates when the author-side declarations are made. The programme-side items (topology checks) are routine applications of the E2 machinery.

## Critical rule

**No empirical claim is treated as certified without the independent rerun of the computational artifacts and the Wave E specification match.** See PROOF_MANIFEST.md “Reproducibility status” (disclosure consolidation).

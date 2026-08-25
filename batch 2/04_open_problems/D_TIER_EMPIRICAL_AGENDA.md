# D-Tier — Empirical Agenda

## Readiness matrix

| Criterion | Groundwater (A005) | Phosphorus (A004) | Fisheries resource–sink (A001 §6) |
|---|---|---|---|
| Data availability | High (geological surveys) | Moderate (agricultural) | High (RAM legacy, ICES) |
| Observation model | Direct (well levels) | Indirect (soil tests) | Model-based assessments |
| Governance records | Available (permits, metering) | Moderate (subsidies, regulations) | Available (quotas, seasons) |
| Calibration feasibility | Blocked (constitutive curves need lithology data) | Blocked (jump balance undefined) | **Ready (E5: linear, closed-form kernel)** |
| Code provenance | Moderate | Weak | **Complete (E5 script + JSON committed)** |
| Admission status | Conditionally admissible (5 blocking items) | Conditionally admissible (5 blocking items) | **ADMITTED WITH NUMBERS (E5 committed, SHA-256: 5670bcc8...)** |

## Decision: fisheries resource–sink as the primary G1 case

The E5 admission is not just designed but **committed with interval-verified numerical constants** (`research_program/validated_computations/E5_NUMBERS.json`): margins α_S=0.4, α_K=0.2, Lipschitz L=0.2, erosion menu with exhibited triple L=0.2/r=0.05/Δ≤0.18, confinement [2,8]×[0,2], and a displayed (REG) certificate family on the infinite horizon.

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

The fisheries track (G1a) proceeds now — all mathematics is in place. The groundwater track (G1b) activates when the author-side declarations are made. The programme-side items (topology checks) are routine applications of the E2 machinery.

## Critical rule

**No empirical claim is treated as certified without the independent rerun of the computational artifacts and the Wave E specification match.** See HONEST_DISCLOSURE.md.

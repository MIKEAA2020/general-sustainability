# WS-upgrades audit — routing adjudication addendum

**Date:** September 25, 2026. **Audit:** `uploads/ws upgrades.txt` (two reports: luna, ten items; gemini, three priorities), addressed to the worked-systems line. **Disposition of substance:** rounds 22–23, evaluated/verified/strengthened/completed jointly — shipped as `paper2_worked_systems_v13` (verifier 54/54, chained lineage 57/57; build gate green: exit 0, zero overfull, 11 pages, rebuild-identical under `SOURCE_DATE_EPOCH`; commit `ec67e78`), recorded in the map v11 round-23 row. This addendum records the **routing adjudication**: the audit was checked against both candidate papers before its defects were assigned.

## 1. Routing checked against both papers

The owner asked whether the audit "pertains to the computational-certificate paper more," noting it was originally intended for that paper. Adjudication method: every quoted defect was located by string and constant search in the two shipped texts (`paper2_computational_certification_v12.tex`, `paper2_worked_systems_v13.tex`) before acceptance.

| Audit quote | comp v12 | ws v13 | Location verdict |
|---|---|---|---|
| shared-/branch-local-register semantics ambiguity (luna 2) | 0 occurrences of "register" | protocol/memory axis, `prop:stationary` | ws |
| "replace the 4×4 census … current 15-partition table" (luna 4) | absent (library self-test mention only) | census section + incompatibility-graph bounds | ws |
| "inflated raw law counts" 256 (luna 5) | 0 occurrences of 256 | 256 raw / 64 behavioral laws, symmetry-classed | ws |
| 48-cell observation (luna 6) | cited companion identity in the library self-test | timing study, exact hitting-time theorem | ws |
| margin 3/50 (luna 8) | 3 occurrences — the instance's own continuous margin | margins proposition, radius form | **each paper's own instance** (see §3) |
| "five audited tables" thesis (luna 10) | — | the audited catalogue reframed as the small theory | ws |

The quoted defects are ws's sentences. comp's mentions of the census and the 48-cell identity are inherited library identities explicitly labelled "software self-tests pointing to the published audits" — companion-by-citation, as required. comp's three-branch delayed-observation instance (delay τ* = 7/50, mesh law ρ(h) = 3/50 − Th/4, hexagonal control set, T = 6/5) appears nowhere in ws (0 occurrences of 7/50, "hexagon", "three-branch", "delayed-observation"); ws's caps benchmark (Y* = 27/5, 47/25 at Y = 6) appears in comp only as the same kind of inherited library identity. The routing to ws was correct; the substantive fixes landed there in v13.

comp-side, the audit's prescriptive items were already discharged in v12 on comp's own objects: master finite-horizon theorem → the finite obstruction certificate and the continuous-to-finite bridge; minimax hypotheses and Farkas/separation → compact convex polytope stated as structural, the residual-bounded multiplier test (eq. 11), nonconvex actuator sets delimited in Scope; complexity and independent verification → polynomial size bound, margin-dependent mesh-resolution bound, and the methods-section independence disclaimer; robustness → the resolution bound as a function of the margin γ.

## 2. The three proposed comp-v13 edits, adjudicated

Each was tested against the merit bar (truly merited, non-decorative) before any edit; all three fail.

1. **Cross-reference "the shared instance's robustness radius" — rejected; the premise is false.** The two papers' margins of 3/50 belong to *different instances*. ws's radius proposition (`prop:margins` i) is proved on the caps benchmark: a static allocation instance with no dynamics, U = {u ≥ 0 : u₁ + u₂ ≥ 2}, crossover Y* = 27/5, margin (Y − 27/5)/10, equal to 3/50 at Y = 6, where the radius result (feasibility returns exactly at δ = 3/50, infeasible at δ = 3/200) is proved. comp's 3/50 is the continuous obstruction value of the three-branch delayed-observation program, derived from its own dual witnesses (Farkas contradiction −53/100 + 1/2 = −3/100; moment error 3/100; mesh law ρ(h) = 3/50 − Th/4 with T = 6/5). The shared value is a coincidence across distinct systems; the proposed sentence would have asserted an identity that does not exist. (Same failure mode the round-2 audit flagged as B7 — constants floating between instances; the separation discipline there applies here.)
2. **Helly (m+1) pointer for m-dimensional action domains — rejected as decorative.** comp states no general action-domain criterion; its fibre-criterion mentions are inherited companion machinery governed by citation, and the Helly content is discharged where it belongs, in ws v13 (incompatibility-graph criterion, Helly numbers 2 and 3). A pointer in comp would restate a companion's content beside a citation that already governs it.
3. **Tightening the independent-verification wording — no edit exists to make; already discharged in v12.** The methods section states exactly the required discipline: "independence here means a separate formula path from the subordinate scripts, not a separate implementation — an independent certificate-file parser that reads the archived witnesses without importing the model builder is a recorded next step." The abstract's "independent primal and dual witnesses" is the mathematically accurate duality usage. The audit's target phrasing does not survive in comp.

## 3. Outcome

- No comp v13: comp v12 stands as the current edition of the computational-certification line (verifier re-run green this round: 39/39).
- No paper editions changed by this addendum; the ws-upgrades audit's substantive adjudication is carried by the shipped v13, its verifier, and the map v11 round-23 row.
- Record value of the routing check: the audit's quoted defects were verified against both shipped texts before assignment, and a numerically seductive but false instance-identity (the two 3/50s) was caught and documented rather than shipped.

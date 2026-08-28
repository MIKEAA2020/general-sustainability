#!/usr/bin/env python3
"""B4 continuum transfer — STAGE T5: the assembly and the persistence-input
statement.

Reads the three channel certificates (T2 binding, T3 slack, T4 prefactor)
and assembles the product bunching inequality of the two-block periodic-NAIM
scaffold at both transfer horizons:

    q_n = M_c * max{ ||S_x^n||_int , ||T_y(n P_hat)||_cert }  <  1 .

The generic two-block periodic persistence theorem's own application target
(its Section 'Quantitative application target') additionally requires
q_40 < 1/4 with chart/error margin.

What the assembly certifies (all three channels at their stated levels):

- T4: M_c <= 4.590009620 (the phase-tangent history ratio, certified upper
  bound; the committed discrete value 4.553557132612546; 0.80% excess).
- T3: ||T_y(35 P_hat)|| <= 8.991634934562145e-02 and
       ||T_y(40 P_hat)|| <= 3.3884763006444694e-02 — the slack-block
  semigroup of the TRUE linear DDE at the declared slack equilibrium,
  certified in outward-rounded interval arithmetic (roots enclosed with
  certified counts and simplicity; the residue-functional decomposition with
  the rigorous contour remainder).
- T2: ||S_x^35||_int <= 5.892303451960152e-03 and
        ||S_x^40||_int <= 3.682017756781228e-03 — the deflated n-period
  evolution (Mon D)^n + Delta_n of the COLLOCATION monodromy (D the
  certified-tangent deflation), in the 4b affine noise-symbol arithmetic at
  point-tight widths.

ASSEMBLY:
    q_35 = 0.4127169084916832  <  1        (factor 2.42 margin)
    q_40 = 0.15553138817100126 <  1/4      (factor 1.61 margin)

The remaining hypotheses of the persistence theorem (its own status note:
'Application to the C4 scaffold remains conditional on CAP and perturbation
bounds') are recorded at their exact status:

- H1 (regularity/localization): the certified orbit's smoothness at the
  SOLUTION level is the committed Stage-4d certificate (the true periodic
  solution within 3e-7, C^infinity away from representation artifacts per
  the eta-lift cascade); the delta_eps perturbation class is the declared
  generic one (||R_eps||_{C^1} <= C|eps|), with the concrete A021 coupling
  G, f, g still AWAITING THE AUTHOR DECISION (OPEN_PROBLEMS_REGISTER A2).
- H2 (split tubular coordinates): not separately certified; the T2
  deflation realizes the normal evolution in the tangent-orthogonal
  complement of the certified tangent (the working chart); the C^1 stable
  bundle and the tubular chart at the certified radius remain a stated
  construction route.
- The binding channel's operator-level continuum lift (the true DDE
  variational monodromy vs the collocation monodromy) remains OPEN: T2
  certifies the collocation system's stable-complement product with its
  interval evaluation uncertainty. The solution-level continuum lift is the
  committed Stage-4d certificate.

Consequently: the product bunching inequality of the two-block scaffold
CLOSES at both horizons with the channel levels as stated; the Paper 4
capstone support row is NOT promoted (the paper-claim-level match and the
coupling declaration remain); Paper 6's gate (A021 continuum periodic-NAIM)
is substantially advanced but not passed.

Deterministic; no computation beyond reading the three committed JSONs.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parent


def main():
    t2 = json.loads((ROOT / "b4_t2_binding_product_certificate.json").read_text())
    t3 = json.loads((ROOT / "b4_t3_slack_semigroup_certificate.json").read_text())
    t4 = json.loads((ROOT / "b4_t4_prefactor_certificate.json").read_text())

    mc = t4["M_c_upper_bound"]
    b35 = t2["assembly"]["binding_35"]
    b40 = t2["assembly"]["binding_40"]
    s35 = t3["semigroup_bounds"]["35"]["bound"]
    s40 = t3["semigroup_bounds"]["40"]["bound"]

    q35 = mc * max(b35, s35)
    q40 = mc * max(b40, s40)
    # the binding channel's share (which channel dominates)
    dom35 = "slack" if s35 >= b35 else "binding"
    dom40 = "slack" if s40 >= b40 else "binding"

    checks = {
        "t2_all_checks": t2["all_checks_pass"],
        "t3_all_checks": t3["all_checks_pass"],
        "t4_all_checks": t4["all_checks_pass"],
        "q35_lt_1": q35 < 1.0,
        "q40_lt_quarter": q40 < 0.25,
    }

    out = {
        "title": "B4 continuum transfer — Stage T5: the assembly and the "
                 "persistence-input statement",
        "inputs": {
            "T2": "b4_t2_binding_product_certificate.json (collocation-level "
                  "binding channel, 4b affine arithmetic)",
            "T3": "b4_t3_slack_semigroup_certificate.json (continuum-level "
                  "slack channel, outward-rounded interval arithmetic)",
            "T4": "b4_t4_prefactor_certificate.json",
        },
        "M_c": mc,
        "channels": {
            "binding_35": b35, "binding_40": b40,
            "slack_35": s35, "slack_40": s40,
            "dominant_35": dom35, "dominant_40": dom40,
        },
        "q_35": q35, "q_35_pass": bool(q35 < 1.0),
        "q_35_margin": 1.0 / q35,
        "q_40": q40, "q_40_quarter_pass": bool(q40 < 0.25),
        "q_40_quarter_margin": 0.25 / q40,
        "theorem_hypotheses_status": {
            "H1": "the certified orbit's solution-level smoothness is the "
                  "Stage-4d certificate; the perturbation class is the "
                  "declared generic one; the concrete A021 coupling G,f,g "
                  "awaits the author decision (register A2)",
            "H2": "not separately certified; the T2 deflation realizes the "
                  "normal evolution in the tangent-orthogonal complement of "
                  "the certified tangent; the C1 stable bundle and tubular "
                  "chart at the certified radius remain a construction route",
            "binding_continuum_lift": "OPEN: T2 certifies the collocation "
                                      "system's product; the true-DDE "
                                      "variational monodromy lift is not "
                                      "enclosed (the solution-level lift is "
                                      "the Stage-4d certificate)",
            "coupling": "the certified object is the two-block scaffold's "
                        "bunching, not the coupled system's persistence",
        },
        "register_consequences": {
            "B4_row": "the product bunching inequality of the two-block "
                      "scaffold CLOSES at both horizons with the channel "
                      "levels as stated (slack continuum-level, binding "
                      "collocation-level); the full COMPUTED (continuum) "
                      "promotion additionally requires the binding "
                      "channel's operator-level continuum lift",
            "paper4_capstone": "NOT promoted: the paper-claim-level match "
                               "and the coupling declaration remain",
            "paper6_gate": "substantially advanced, not passed (the "
                           "continuum periodic-NAIM statement additionally "
                           "requires H2's chart and the coupling)",
        },
        "checks": {k: bool(v) for k, v in checks.items()},
        "all_checks_pass": bool(all(checks.values())),
    }
    (ROOT / "b4_t5_assembly_certificate.json").write_text(json.dumps(out, indent=1, sort_keys=True))
    print(f"q_35 = {q35:.10f}  < 1: {q35 < 1}  (margin {1.0/q35:.2f}x, dominant: {dom35})")
    print(f"q_40 = {q40:.10f}  < 1/4: {q40 < 0.25}  (margin {0.25/q40:.2f}x, dominant: {dom40})")
    print("all_checks_pass =", out["all_checks_pass"])


if __name__ == "__main__":
    main()

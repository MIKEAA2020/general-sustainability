"""Model simulators used by the numerical verification harness.

These are self-contained ports of the scripts that were independently verified
during the audit (sim.py / demo_unified.py / mask_rk4.py / audit_basin.py /
audit_s0.py). Keep them dependency-light (numpy only) so the CI numerical audit
can run anywhere. Two models are distinguished and labelled:

  * ORIGINAL  : gross-depletion, M-in-gha, B=b*M, 2-D, unique interior attractor.
  * CORRECTED : unified stock-flow (1'''), A-in-ha, B=bA+b_G*G(A), deficit depletion.
"""

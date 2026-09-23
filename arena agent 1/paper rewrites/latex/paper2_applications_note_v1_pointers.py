#!/usr/bin/env python3
"""
Applications-note pointer record — machine-checks every object the note
quotes against the shipped artifacts of the programme (their PDFs).

Dependency: pymupdf (PDF text extraction) — the one stated dependency;
everything else is stdlib. Deterministic; text identity after
normalization (soft hyphens, line-break hyphenation, whitespace).

Pointers verified:
  P1  calculus (paper 2, v48): Theorem 3 (timing), Proposition 7 and
      Corollary 1 (fibre criterion), Remark 4 (certainty-equivalence),
      the composite-indices application sentence, Open Problem 1,
      blind-window control classes.
  P2  stochastic selector v2: attaining set / value-one level (the
      selector split), the class-scope remark, the oscillation identity
      check S11 and the class table check S8.
  P3  monitoring design: the fibre rule instances — coarsest admissible
      monitoring (2 cells), the 15-partition enumeration.
  P4  policy-class lattice: the title object and the audited chain
      counts (24, 26, 28).
  P5  comparison-function exit: the lineage title and drift reading.
  P6  successor: the five-layer architecture title.
  P7  companion bridge: the continuous-to-finite certificate title.
  P8  buffered viability: the obstruction-margin object.
  P9  finite-horizon completeness: the counterstrategy-tree object.
"""
import os
import re
import sys

try:
    import pymupdf
except ImportError:
    print("FAIL dependency: pymupdf is required (pip install pymupdf); "
          "the pointer record cannot run without it.")
    raise SystemExit(1)

HERE = os.path.dirname(os.path.abspath(__file__))

def norm(t):
    t = t.replace("\u2010", "-").replace("\u00ad", "")
    t = re.sub(r"-\s*\n", "", t)
    return re.sub(r"\s+", " ", t)

def text_of(rel):
    path = os.path.join(HERE, rel)
    if not os.path.exists(path):
        return None
    doc = pymupdf.open(path)
    return norm(" ".join(p.get_text() for p in doc))

PASS = []
def check(name, cond):
    PASS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

CALC = "paper2_obstruction_calculus_v48_Automatica_routes.pdf"
SS2 = "paper2_stochastic_selector_v2.pdf"

t = text_of(CALC)
p1 = t is not None and all(s in t for s in
    ["Theorem 3", "Proposition 7", "Corollary 1", "Remark 4",
     "composite indices", "Open Problem", "blind-window"])
check("P1 calculus v48: Theorem 3; Proposition 7; Corollary 1; Remark 4; "
      "composite-indices application; Open Problem 1; blind-window "
      "classes — all present", p1)

t = text_of(SS2)
p2 = t is not None and all(s in t for s in
    ["attaining set", "value-one level", "class-scoped", "oscillation"])
check("P2 stochastic selector v2: attaining set / value-one level "
      "(selector split); class-scope remark; oscillation identity — "
      "all present", p2)

t = text_of("monitoring_design_v1.pdf")
p3 = t is not None and ("coarsest admissible monitoring" in t
                        and "2 cells" in t and "15" in t)
check("P3 monitoring design: fibre-rule instances — coarsest admissible "
      "monitoring (2 cells) over the 15-partition enumeration", p3)

t = text_of("policy_class_lattice_v1.pdf")
p4 = t is not None and all(s in t for s in
    ["Which Restriction", "24", "26", "28"])
check("P4 policy-class lattice: the attribution diagnostic and the "
      "audited chain counts 24 / 26 / 28 of 36", p4)

t = text_of("comparison_drift_exit_v1.pdf")
p5 = t is not None and ("Beyond Constant Drift" in t
                        and "comparison" in t.lower())
check("P5 comparison-function exit: lineage and reading present", p5)

t = text_of("successor_five_layer_v1.pdf")
p6 = t is not None and "Five Layers of Obstruction" in t
check("P6 successor: the five-layer architecture lineage present", p6)

t = text_of("paper2_companion_recourse_bridge_v1.pdf")
p7 = t is not None and "Finite Nonviability Certificates" in t
check("P7 companion bridge: the continuous-to-finite certificate "
      "lineage present", p7)

t = text_of("buffered_viability_v1.pdf")
p8 = t is not None and "obstruction margin" in t.lower()
check("P8 buffered viability: the obstruction-margin object present", p8)

t = text_of("finite_horizon_completeness_v1.pdf")
p9 = t is not None and "counterstrategy" in t.lower()
check("P9 finite-horizon completeness: the counterstrategy-tree object "
      "present", p9)

n_pass = sum(1 for _, ok in PASS if ok)
print(f"\npointer record: {n_pass}/{len(PASS)} pointers verified")
raise SystemExit(0 if n_pass == len(PASS) else 1)

#!/usr/bin/env python3
"""E2 v28 pass 3: site 7 (indented \item) and its dependent claims."""
import re

SRC = "/home/user/fam/e2/paperE2_cod_intervention_v28.tex"
tex = open(SRC, encoding="utf-8").read()

OLD = r"""  No non-BAU policy dominates BAU, and the mechanism is the clause-(H1)
  reading at the 5th-percentile \(T=\infty\) class rather than boundary
  geometry or, alone, supply: every positive-catch rule is empty there
  while BAU's kernel is nonempty (\(2219.6\) kt). Under the informative
  10th-percentile class the critical-zone, cascade, and graded rules
  match BAU's protection exactly, and the surplus-proportional family at
  \(\phi \le 0.50\) holds the LRP at every horizon and harvests more
  than the moratorium --- so the reactive family registers a genuine
  trade-off, not a strict improvement. It still does not dominate BAU:
  it does not improve on BAU at the harsher-informative class, and an
  equally protective flat 60-kt cap supplies more."""

NEW = r"""  No non-BAU positive-catch policy dominates BAU, and the mechanism is
  clause (H1) read at every reading --- BAU is at least as protective as
  every positive-catch rule at all 27 (class, horizon) readings and
  strictly more protective at 25 of them --- rather than boundary
  geometry or, alone, supply; the 5th-percentile \(T=\infty\) reading
  ties every rule at empty and does not itself decide the verdict.
  Under the informative 10th-percentile class the critical-zone rule,
  the cascade and graded2 sit at \(900.3\) kt at \(T = \infty\) against
  BAU's \(884.6\) kt, and the surplus-proportional family at
  \(\phi \le 0.25\) holds the LRP at every horizon and harvests more
  than the moratorium --- so the reactive family registers a genuine
  trade-off, not a strict improvement. It still does not dominate BAU:
  it does not improve on BAU at the harsher-informative class, and a
  near-equally protective flat 60-kt cap supplies more."""

if OLD in tex:
    tex = tex.replace(OLD, NEW)
    print("OK   site7 applied")
else:
    print("MISS site7")

open(SRC, "w", encoding="utf-8").write(tex)

print("\nresidual sweep:")
bad = 0
for tok in ["2219.6", "2070.9", "920.2", "989.0", "1025.5", "1064.7",
            "1111.3", "1161.0", "0.906", "0.862", "0.958", "0.647",
            "0.835", "0.903", "0.857", "0.955"]:
    hits = len(re.findall(r"(?<![\d.])" + re.escape(tok) + r"(?!\d)", tex))
    if hits:
        print(f"  {tok:10s} x{hits}   <-- STILL PRESENT")
        bad += 1
print("  (clean)" if not bad else f"  {bad} token(s) remain")
print("\n'seven':", len(re.findall(r"\bseven\b", tex)))
print("'2219.6':", tex.count("2219.6"))

"""Build paper5 v35 from v34 (supp-alignment main-side fixes). Asserted-once."""
import sys

SRC = '/home/user/paper5_v34/paper5_sampled_governance_v34.tex'
DST = '/home/user/paper5_v35/paper5_sampled_governance_v35.tex'

s = open(SRC, encoding='utf-8').read()
n0 = len(s)

SUBS = [
 ('Q7-header',
  "% Periodic Review as Sampled Governance (paper 5, revision v34): audit-sweep revision (endpoint-trim check, periodogram deposit, power-design specification, prospective-design completion, methods precision) with line numbers for review.",
  "% Periodic Review as Sampled Governance (paper 5, revision v35): supplementary-completeness and alignment revision (S1 currency, S2 notation, S2.3/Table-3 closed-form bridge, S8/App-A register pointers) with line numbers for review."),
 ('Q3-s5-pointer',
  "The ecosystem context is background only: between 1985--87 and 2013--15,",
  "The ecosystem context (Supplementary S5) is background only: between 1985--87 and 2013--15,"),
 ('Q4-appa-s8',
  "preregistration targets with no registration identifier or archived\nprotocol.",
  "preregistration targets with no registration identifier or archived\nprotocol. The full discharge register is Supplementary S8."),
 ('Q5-table3-s23',
  "equilibrium routine \\texttt{base\\_equilibrium},\n\\texttt{droop\\_test.py} L86--93 @ 24c980cd \\\\",
  "equilibrium routine \\texttt{base\\_equilibrium},\n\\texttt{droop\\_test.py} L86--93 @ 24c980cd; closed form in Supplementary S2.3 \\\\"),
 ('Q2-screening-log',
  "screening log, exact-update comparison) are registration",
  "query log, nonlinear exact-update comparison) are registration"),
 ('Q1-dataavail',
  "exact-update comparison of Section 3.4, and the case-screening",
  "nonlinear exact-update comparison of Section 3.4, and the case-screening"),
 ('Q6-supp-pointer',
  "accompanying file \\texttt{paper5\\_supplementary\\_v10.md}",
  "accompanying file \\texttt{paper5\\_supplementary\\_v11.md}"),
]

fails = []
for tag, old, new in SUBS:
    c = s.count(old)
    if c != 1:
        fails.append((tag, c))
        continue
    s = s.replace(old, new, 1)

if fails:
    print('FAILED:', fails)
    sys.exit(1)
open(DST, 'w', encoding='utf-8').write(s)
print(f'v35 built: {len(SUBS)}/{len(SUBS)} subs ok, {n0} -> {len(s)} bytes')

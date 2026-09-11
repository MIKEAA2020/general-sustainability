# Paper 5 venue-synthesis record (v38 / supp v14) — 2026-09-12

Source review: `uploads/qwen p5 rewrite.txt` (1639 lines; journal-fit
assessment + Nature Sustainability rewrite draft + 8 elevation points).
Rule applied: adopt the best suggestion(s) from EACH of the 11 venues
plus the cross-cutting and elevation sections, subject to (a) mutual
non-contradiction, (b) the standing manuscript constraints (formal
register, no editorial/self-praise, no draft-talk, no phantom
strawmen), and (c) no new unexecuted research presented as results.

## Adopted, by venue

- **3.1 Nature Sustainability**: governance-design reframing (new title;
  decision-clock term defined once); policy box (Box 2, four design
  principles); 6.5-yr crossing now explicitly illustrative (baseline
  clause, §3.4); assertive rewritten abstract with caveats kept in the
  body only.
- **3.2 PNAS**: one central result sharpened (abstract + §5 close);
  significance carried by the decision-clock closing sentence.
  (Full PNAS compression rejected: contradicts keeping one paper.)
- **3.3 One Earth**: plain-language accessibility (bridge paragraph,
  conceptual Figure 1); actionable recommendations (Box 2 + eight
  management implications, all section-grounded).
- **3.4 Fish and Fisheries**: HCR/TAC/MSE management-procedure bridge
  paragraph; management-regime Box 1 (annual TAC / multiannual plan /
  moratorium / data-limited); extractive-controller diagnostic framing
  with subsidy grounding; screen stays a diagnostic (already the
  manuscript's stance).
- **3.5 ICES JMS**: advice chain displayed explicitly (§2.1);
  protective-channel result promoted (abstract + implication 3);
  review intervals compared as management alternatives (Box 1 rows).
  (Full F-reparameterisation rejected as new research; adopted as the
  stated next step in limitation (ii).)
- **3.6 Marine Policy**: policy translations folded into the single
  bridge paragraph (one bridge, not two); real regimes in Box 1;
  recommendations in §4.8. (Appendix B untouched: out of scope.)
- **3.7 CJFAS**: η question already discharged in v37 (no change);
  near-unit-circle margin now explicitly framed as high sensitivity,
  not a robust universal verdict (§3.4); ledger overhead reduced via
  the Box 1 move (below).
- **3.8 Theory / 3.9 SIADS**: NS language already at "signature,
  nondegeneracy not verified" (confirmed, no change); honest
  generality scope sentence added (§4.8: logistic core illustrative;
  operator-dependence, finite-horizon scope, and Euler/exact
  non-equivalence are the structural results). (Empirics-removal and
  NS-verification rejected: contradict goal / new research.)
- **3.10 Control**: formal advice-chain display (§2.1); Euler/exact
  caution scoped to the studied class (§4.8). (Fisheries-removal
  rejected: contradicts goal.)
- **3.11 Ecol. Modelling / EMS**: framework-framing paragraph (§4.8:
  the three reusable-modelling questions); figure-generation script
  deposited (`fig_concept_v38.py`).

## Adopted from cross-cutting (§4) and elevation (§§7–8, draft)

- 4.1/4.2/§8: new title + rewritten abstract (~185 words, six-part
  skeleton); every abstract claim section-grounded (incl. exact
  "32-system" count from the deposited table).
- 4.3/elev-8: Box 1 (evidential-status table) moved out of the main
  text; replaced by a short paragraph pointing to Supplementary S1,
  which already holds the full inventory — zero information loss.
- 4.4: terminology already fixed by the manuscript's own note (body
  uses sample-and-hold throughout); "decision clock" added strictly
  as a defined gloss (title/abstract/§1/§4.8/§5), never alternating.
- 4.5/§7.1/elev-2: extractive-controller grounding paragraph
  (diagnostic perverse-pressure representation; capacity-enhancing
  subsidies, Sumaila et al. 2019, verified reference). Controller
  rename rejected (consistency risk); object name kept.
- 4.6/§7.6: q-sensitivity already fully reported (both scales, flipped
  verdicts, "uninformative" comparison); adopted compatibly as the
  named F-reparameterisation next step in §4.7(ii) — nine-count kept.
- 4.7/§7.5: archived records already provisional with the
  reconstruction primary (confirmed, no change).
- 4.8/§7.4: screen-as-diagnostic already the stance (confirmed).
- 4.9: dedicated "Implications for management design" (§4.8, eight
  items, each with section pointer).
- 4.10/elev-5: conceptual Figure 1 (matplotlib; Panel A architectures,
  Panel B schematic slice with computed markers only, labelled
  schematic in-figure and in caption); old Figure 1 → Figure 2
  (single cite updated).
- Elev-1: cross-sector clock paragraph (§1: Paris NDC Art. 4.9 +
  stocktake Art. 14, verified; governance/ecological/environmental
  clocks) with §4.8 echo; S1 row marks it illustrative, not a case
  claim.
- Elev-3 ("myth" rhetoric), elev-6 (full sticky lexicon): rejected per
  register constraints; substance kept ("circuit breakers" once as a
  gloss for asynchronous emergency triggers).
- Elev-4: cod circuit-breaker lesson folded into §4.8 implication 5
  and Box 2 principle 4 (grounded §§3.8/4.5).
- §7.2/§7.3/§7.7: baseline-conditionality clause (§3.4), sensitivity
  frame (§3.4), caveats consolidated via Box-1 move + §4.7 pointer.

## Rejected as contradicting the goal (recorded, not lost)

Split-the-paper (Option B); remove-empirics / remove-policy /
remove-fisheries (theory/control maximalist versions); universalise
the 6.5-yr result; verify NS nondegeneracy; execute the sensitivity
battery or F-reparameterisation (all new research); cover-letter
hype language.

## Reproducibility

`build_paper5_v38.py` / `build_paper5_supp_v14.py` regenerate both
files from v37/v13 with count-guarded edits. Figure: deposited
generator + PNG (`figs_p5/fig_concept_v38.png`). Push: single
race-checked commit (tex + supp + 2 builders + memo + fig script +
fig PNG).

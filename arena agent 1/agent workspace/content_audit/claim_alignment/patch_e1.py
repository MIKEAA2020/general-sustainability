#!/usr/bin/env python3
"""Non-destructive E1 composite draft from exact reviewed live head."""
from pathlib import Path
from difflib import unified_diff
import re
r=Path('/home/user');b=r/'content_audit/claim_alignment';src=r/'papers/paper11_forecasting_baselines_v64.tex';old=src.read_text();s=old
abstracts=re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',old,re.S)
assert len(abstracts)>=2
(b/'original_abstracts').mkdir(parents=True,exist_ok=True)
(b/'original_abstracts'/(src.stem+'.txt')).write_text('\n\n% ----- ABSTRACT BOUNDARY -----\n\n'.join(abstracts))
for i, a in enumerate(abstracts, 1):
 (b/'original_abstracts'/(src.stem+f'_abstract_{i}.txt')).write_text(a)
def change(a,z):
 global s
 assert s.count(a)==1,(s.count(a),a[:100]);s=s.replace(a,z,1)
# V61 concatenation tokens occur in a comment only; retain its provenance in words.
change('%% NOTE: v61 was THREE complete LaTeX documents concatenated (3x \\documentclass,\n%%   3x \\begin{document}, 3x \\end{document}); \\part{E3} and \\part{Ws} sat in the\n%%   GAPS between them, outside any document. Nothing past the first \\end{document}',
       '%% NOTE: v61 was THREE complete LaTeX documents concatenated (three document\n%%   starts and terminators); E3 and Ws sat in the gaps between them,\n%%   outside any document. Nothing past the first document terminator')
change('A model that persists a\nnear-white driver has no claim to beat persistence, whatever its mechanistic fidelity.',
       'For the tested process modules, persisting a weakly predictive driver did not\nimprove the scored forecast against persistence at the stated horizons.')
change('a negative result of this kind is informative only against a protocol\nfixed before any score is computed;',
       'a negative result is interpretable against a stated scoring core,\nwith later tie-band and comparator completions disclosed;')
change('On both systems, at the annual origin, last-value persistence is\nmore accurate than the process-based alternatives scored. On the cod series no module is retained\non either unpooled specification; on the aquifer the univariate AR(1) is retained, by a margin the\npaper shows to be a coin-flip.',
       'On the cod series, at both scored horizons, persistence has lower pooled\nrolling-origin RMSE than the tested structural modules on either unpooled\nspecification. On the aquifer, at the annual origin, the output-only\nunivariate AR(1) reads 12.84 versus 13.23 ft for persistence and is\nretained under its original one-horizon point rule, though the margin is\nwithin noise; a water-balance-identified affine model with climatological\nfluxes reads 12.28 ft but is declined by its protocol class clause.')
change('--- keep a module only if it lowers RMSE against both the next-simpler module and\npersistence --- was fixed before any score was computed, and the rule itself is then evaluated\nby simulation under known ground truth.',
       '--- compare RMSE against both the next-simpler module and\npersistence --- was coded before the first scoring pass. The 5\\% tie band\nand comparator declarations were recorded after the scores, as \\S2.3 discloses;\nthe applied rule is then evaluated by simulation under known ground truth.')
change('Here nothing is selected from the scores at all: the retention rule is a predicate fixed before\nany score is read, applied without exception, and its operating characteristics are measured by\nsimulation under known ground truth. That is why a negative result can be reported as a finding\nrather than as an absence of evidence --- the rule either retains a module or it does not, and\non both systems it does not.',
       'Here the model class and scoring core were fixed before scoring, but the\nretention predicate does select on RMSE, and the later tie-band and comparator\ncompletions are disclosed in \\S2.3. Simulation estimates operating\ncharacteristics conditional on the rule as applied; it is not a\nfamilywise-error correction or evidence that every clause was prespecified.\nOn cod the applied rule retains no structural module; the aquifer\noriginally retains an output-only AR(1) at one year while declining\nwater-balance stock-flow additions.')
change('fixed in advance cannot be tuned to the series, so a module that a more permissive protocol\nwould have retained is still reported here as not retained.',
       'with its scoring core set in advance and later completions disclosed cannot\nbe retroactively retuned without changing the interpretation of the verdict.')
change('the record and recompares the printed scores, reference points and\nwindow facts against the locked input files; it is archived alongside\nthis manuscript.',
       'the outcome-year, vintage and threshold checks against the locked\ninput files, but does not recompute the rolling-origin forecast scores\nor power simulations; those are archived with their separate campaign\nscripts and results. The v60 verifier also requires a compatible\n\\texttt{texcheck.py} helper defining \\texttt{no\\_variant}; archive that helper\nwith it before describing a reproducible exit-status check.')
# Surgical corrections to inherited abstract sentences; archive above stays verbatim.
change('Index-well head forecasting is a recurring operational need, while deliberately simple process-based water-balance models are rarely tested against naive benchmarks under a locked retention rule.',
       'Index-well head forecasting is a recurring operational need; this record tests a deliberately simple water-balance model against naive benchmarks under a disclosed retention rule.')
change('A causal module was retained only if it beat both persistence and the next-simpler causal model under a protocol frozen before any score.',
       'The scoring core compared RMSE with persistence and the next-simpler model before the first pass; comparator and tie-band clauses were completed after scores and are disclosed here.')
change('The decision-relevant uncertainty of the period accumulated in the\nobservation and reference-point layer, not in forecast structure.',
       'In the observed 2016--2023 update window, changes to observations\nand reference points affect decision interpretation; this window does\nnot independently establish that forecast structure was irrelevant.')
change('Pella and\nRomano, J.P. and Wolf, M., 2005. Stepwise multiple testing as formalized data snooping.\n\\emph{Econometrica}, 73(4), 1237--1282. doi:10.1111/j.1468-0262.2005.00615.x.\n\nTomlinson, 1969)',
       'Pella and\nTomlinson, 1969)')
change('White, H., 2000. A reality check for data snooping.',
       'Romano, J.P. and Wolf, M., 2005. Stepwise multiple testing as formalized data snooping.\n\\emph{Econometrica}, 73(4), 1237--1282. doi:10.1111/j.1468-0262.2005.00615.x.\n\nWhite, H., 2000. A reality check for data snooping.')
change('The restatement changes no outcome: the retained set is empty\non both systems under either form of the rule.',
       'Under the stricter E1 two-horizon 5\\% rule, no tested structural\nmodule is retained on either series. This is a restatement of the Edwards\nscores under a different rule, not a claim that its original one-year\npoint rule rejects the output-only AR(1), which it retains.')
change('The retained set is\nempty on both systems, while the series are not pooled and no verdict is\ntransferred between them.',
       'Under the E1 stricter restatement the tested structural retained set\nis empty on both systems; the aquifer original one-year point rule does\nretain its output-only AR(1). The series are not pooled and no verdict is\ntransferred between them.')
# All original abstracts are archived verbatim; only targeted false sentences changed.
assert len(re.findall(r'\\begin\{abstract\}.*?\\end\{abstract\}',s,re.S))==len(abstracts)
out=b/'drafts'/src.name;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(s)
(b/'diffs'/(src.stem+'.diff')).write_text(''.join(unified_diff(old.splitlines(True),s.splitlines(True),fromfile=str(src),tofile=str(out))))
print(out)

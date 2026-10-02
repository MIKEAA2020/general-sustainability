#!/usr/bin/env python3
"""Make versioned reader-facing journal cleanups; old files are never overwritten."""
from pathlib import Path
import re,shutil,difflib,hashlib
R=Path('/home/user');P=R/'papers';S=R/'paper 2 family';A=R/'content_audit/journal_submission';A.mkdir(exist_ok=True)
units=[('paper01_obstruction_calculus',64,65,'01_obstruction'),('paper02_probabilistic_sufficiency',13,14,'02_probabilistic_sufficiency'),('paper03_computational_certification',17,18,'03_computational_certification'),('paper04_minimax_dual_certificates',17,18,'04_minimax_dual_certificates'),('paper05_exact_belief_computation',17,18,'05_exact_belief_computation'),('paper06_assessment_separation',68,69,None),('paper07_sampled_governance',51,52,None),('paper09_cod_certification',33,34,'09_cod_with_arv'),('paper09b_arv_certification',3,4,'09_cod_with_arv'),('paper11_forecasting_baselines',65,66,'11_forecasting_baselines'),('paper11c_worked_systems_audit',3,4,'11c_worked_systems')]
def once(t,a,b):
 assert t.count(a)==1,(a[:95],t.count(a));return t.replace(a,b,1)
def strip_comments(t):
 lines=t.splitlines(True);removed=sum(x.lstrip().startswith('%') for x in lines)
 t=''.join(x for x in lines if not x.lstrip().startswith('%'))
 # leading blank lines do not belong in journal-facing TeX source
 return t.lstrip('\n'),removed
def submit(old,new,t):
 assert old.exists(),old
 orig=old.read_text();new.write_text(t)
 dest=A/'diffs';dest.mkdir(exist_ok=True);name=old.parent.name.replace(' ','_')+'__'+new.stem+'.diff'
 (dest/name).write_text(''.join(difflib.unified_diff(orig.splitlines(True),t.splitlines(True),fromfile=str(old.relative_to(R)),tofile=str(new.relative_to(R)))))
 print(new.relative_to(R),len(t.splitlines()))
for base,ov,nv,subdir in units:
 for d in (P, *([S/subdir] if subdir else [])):
  old=d/f'{base}_v{ov}.tex';new=d/f'{base}_v{nv}.tex';t=old.read_text()
  if base=='paper01_obstruction_calculus':
   a='\\paragraph{Fidelity to the text.} The formalization\'s source of record is version 53 of\nthis manuscript; the present version descends from version 57. Comparing the two, no\nlabelled result present in the earlier version has been dropped, and every result named\nabove is present in both. The formalization therefore applies to the results as they\nstand here.'
   b='\\paragraph{Scope of formal support.} The named Lean declarations establish the\ndiscrete results under their stated hypotheses. Continuous-time exit and Dini-derivative\narguments, and any stationary-policy sufficiency statement not encoded as a policy tree,\nremain supported by their displayed mathematical proofs rather than by these declarations.'
   t=once(t,a,b)
  elif base=='paper03_computational_certification':
   needle=r'paper03\_computational\_certification\_v17\_supplementary.tex';t=once(t,needle,r'paper03\_computational\_certification\_v18\_supplementary.tex')
  elif base=='paper05_exact_belief_computation':
   t=once(t,'and selected headline strings in the original source. A passing\nstring check does not recompute the five-cube alpha masks or prove the\nclassification.', 'and checks selected headline strings. A passing string check does not recompute\nthe five-cube alpha masks or prove the classification.')
  elif base=='paper06_assessment_separation':
   t=once(t,r'paper06\_assessment\_separation\_v68\_supplementary.md',r'paper06\_assessment\_separation\_v69\_supplementary.md')
  elif base=='paper09_cod_certification':
   t=once(t,'set --- the second by \\(5.4\\) kt, not by the wide margin an earlier version\nof this paper reported (Section 3.4) --- \\(\\phi = 0.75\\) is empty, and the\nband \\(0.531 < \\phi < 0.727\\) is the regime in which the rule is viable but\nonly from above the reference point. No member of the originally declared\nfamily fell in that band, which is why the erroneous criterion went unnoticed;\nthe family has been extended by \\(\\phi = 0.60\\) so that Table 1 exhibits it.', 'set, with a \\(5.4\\)-kt margin for the second (Section 3.4). The \\(\\phi = 0.75\\)\nmember has an empty kernel. In the intervening band \\(0.531 < \\phi < 0.727\\),\na rule is viable only from above the reference point; \\(\\phi=0.60\\) in\nTable 1 exhibits this nonempty proper kernel.')
   t=once(t,'\(920.2\) kt at \(T=1\)). Between the two thresholds the rule is\nviable but only from above the reference point: at the added member\n\(\phi = 0.60\) the informative kernel is \([1074.8, 10^4]\) kt, not\nthe safe set, and it is this regime that an earlier version of this paper\nmissed by quoting \(0.727\) as the threshold for holding the safe set.\nThe three tabulated verdicts were unaffected, which is why the error\nsurvived every numeric check.', '\(920.2\) kt at \(T=1\)). Between the two thresholds the rule is\nviable but only from above the reference point: at \(\phi = 0.60\),\nthe informative kernel is \([1074.8, 10^4]\) kt, not the safe set.\nThe threshold for holding the entire safe set is \(0.531\); \(0.727\)\ninstead marks the nonemptiness boundary.')
  elif base=='paper11_forecasting_baselines':
   t=once(t,'reproduced in full from its companion paper without condensation. The\ncommon RMSE scoring comparison', 'presented with its own protocol and evidence. The\ncommon RMSE scoring comparison')
   t=once(t,'\\noindent\\textbf{Source study:} Does a surplus-production ladder improve forecasts of Northern cod? A scored test on NAFO 2J3KL. September 24, 2026.','\\noindent\\textbf{Northern cod:} The first study compares a scored surplus-production ladder with persistence on NAFO 2J3KL.')
   t=once(t,'\\noindent\\textbf{Source study:} Does a one-pool water-balance model improve forecasts of Edwards Aquifer head? A scored test at J-17. September 6, 2026.','\\noindent\\textbf{Edwards Aquifer:} The second study scores a one-pool water-balance ladder against J-17 forecasting benchmarks.')
   t=once(t,r'paper11\_forecasting\_baselines\_v65\_SI.md',r'paper11\_forecasting\_baselines\_v66\_SI.md')
  elif base=='paper11c_worked_systems_audit':
   a='Earlier worked-systems source text uses the same two-coordinate construction but repeats the cod-origin attribution; that lineage alone does not establish an independent derivation from cod. '
   t=once(t,a,'')
  t,rem=strip_comments(t)
  submit(old,new,t)
# Preserve attachments as new names; only update reader-facing main-file pointers.
for root in [P,S/'01_obstruction']:
 old=root/'paper01_obstruction_calculus_v64_supplementary.tex';t,rem=strip_comments(old.read_text());submit(old,root/'paper01_obstruction_calculus_v65_supplementary.tex',t)
for root in [P,S/'03_computational_certification']:
 old=root/'paper03_computational_certification_v17_supplementary.tex';t,rem=strip_comments(old.read_text());submit(old,root/'paper03_computational_certification_v18_supplementary.tex',t)
old=P/'paper06_assessment_separation_v68_supplementary.md';t=old.read_text().replace('v68','v69');submit(old,P/'paper06_assessment_separation_v69_supplementary.md',t)
for root in [P,S/'11_forecasting_baselines']:
 old=root/'paper11_forecasting_baselines_v65_SI.md';new=root/'paper11_forecasting_baselines_v66_SI.md';new.write_bytes(old.read_bytes());assert hashlib.sha256(new.read_bytes()).hexdigest()=='fb3f8bd2e1eb5590c20371a6107fe7a40670eb67c8f92ae73682e26c31a4f122'

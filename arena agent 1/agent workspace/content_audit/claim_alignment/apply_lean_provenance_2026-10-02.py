#!/usr/bin/env python3
"""Apply only supported, source-specific Lean-provenance corrections to aligned drafts.
Run AFTER source-family patch generators and paper09 host extraction; regenerate
live-head diffs and compile the final candidate TeX after this step.
"""
from pathlib import Path
from difflib import unified_diff
import re
R=Path('/home/user');B=R/'content_audit/claim_alignment';D=B/'drafts'
run=r'\url{https://github.com/MIKEAA2020/general-sustainability/actions/runs/36946730855}'
provenance=(r'\noindent\textbf{Current Lean provenance.} The committed project pin '
 r'\texttt{v4.34.1} was rebuilt in GitHub Actions (default Lake target: '
 r'\(60/60\) jobs, exit~0; '+run+r'). The exact project source and two footprint-check '
 r'\texttt{.lean} files are archived with SHA-256 manifests. A comment-aware scan of all '
 r'\(62\) source files finds no \texttt{sorry}, \texttt{admit}, explicit '
 r'\texttt{axiom} or \texttt{constant} declaration. Twenty-one named footprints contain '
 r'no \texttt{sorryAx}; the aggregate-import environment exposes three '
 r'source-level \texttt{native\\_decide} uses in the P3 support/value examples, yielding '
 r'nine distinct generated axiom names under this pin. These are executable '
 r'computational certificates that extend kernel-only trust to the Lean compiler/runtime; '
 r'they are not admitted gaps and must not be described as zero axioms or as '
 r'kernel-only proofs. Three preserved historical modules outside the aggregate import '
 r'closure are not certified by the default build. The v4.14.0 comparison of the '
 r'\emph{current} source fails in the prelude and does not reproduce the old source run.')
def once(s,old,new,fn):
 n=s.count(old)
 assert n==1,(fn,'expected one match, got',n,old[:85])
 return s.replace(old,new,1)
pending=[]
def change(fn,transform):
 p=D/fn;before=p.read_text();after=transform(before)
 assert after!=before,fn
 live=R/'papers'/fn
 diff=(''.join(unified_diff(live.read_text().splitlines(True),after.splitlines(True),fromfile=str(live),tofile=str(p))) if live.exists() else None)
 pending.append((p,before,after,diff))
 print('PLANNED',fn,len(before),'->',len(after))
def replace_provenance(s,fn):
 marker=r'\noindent\textbf{Verification provenance.}'
 assert s.count(marker)==1,fn
 start=s.index(marker);end=s.index('\n\n',start)
 # Historical theorem-count explanations precede the provenance paragraph.
 return s[:start]+provenance+s[end:]
def paper01(s):
 s=replace_provenance(s,'paper01')
 return once(s,r'\texttt{sorryAx} appears nowhere.',r'\texttt{sorryAx} is absent from the checked P1 declarations and the audited aggregate-import footprints; project-wide generated native-evaluation axioms are disclosed in the provenance paragraph below.','paper01')
change('paper01_obstruction_calculus_v63.tex',paper01)
def psuff(s):
 s=once(s,'(Lean~4; no axioms, no admitted gaps, ordered-field interface\nonly)', '(Lean~4; no \texttt{sorryAx} in the audited import environment,\nwith generated \texttt{native\\_decide} trust dependencies scoped below)', 'psuff opening')
 s=once(s,'are formalized in Lean~4 with no axioms and no\n  admitted gaps.', 'are formalized in Lean~4 with no \texttt{sorryAx} in the audited\n  aggregate-import environment. Three \texttt{native\\_decide} uses in the P3\n  support/value examples generate nine axiom names in this pinned source,\n  relying on compiled finite computation rather than kernel-only reduction.', 'psuff summary')
 anchor='\n\\noindent Not claimed: the belief-state reduction'
 assert s.count(anchor)==1
 s=s.replace(anchor,'\n'+provenance+'\n'+anchor,1)
 return s
change('paper02_probabilistic_sufficiency_v12.tex',psuff)
def comp(s):
 s=once(s,'(Lean~4, 60 modules under \\texttt{Formalizations/}, no axioms and no admitted gaps)',
   '(Lean~4, 60 preserved modules under \\texttt{Formalizations/}; the default target builds 60/60 jobs and the checked soundness declaration has no admitted gap)', 'comp')
 p=re.compile(r'\\emph\{The project is pinned to Lean~4 in \\texttt\{lean-toolchain\}.*?The build has not\nbeen re-run since the toolchain pin moved\.\}',re.S)
 assert len(p.findall(s))==1
 s=p.sub(lambda _:provenance,s,count=1)
 return s
change('paper03_computational_certification_v16.tex',comp)
def minimax(s):
 s=once(s,'No current-toolchain build is claimed. The module imports only the','The declared-pin default-target build now passes in GitHub Actions. The module imports only the','minimax')
 s=replace_provenance(s,'minimax')
 s=once(s,'Declarations using classical reasoning depend only on \\texttt{Classical.choice}, \\texttt{propext} and \\texttt{Quot.sound}, the standard axioms of Lean\'s classical logic.',
  'The named Minimax declarations checked here use only those standard classical axioms or none; the wider project also has the P3 native-evaluation dependencies disclosed below.', 'minimax axioms')
 return s
change('paper04_minimax_dual_certificates_v16.tex',minimax)
def ebc(s):
 s=once(s,'The full project builds cleanly under Lean~4 (\\(60\\) of \\(60\\) build jobs).','The pinned default Lake target builds cleanly under Lean~4 v4.34.1 (\\(60\\) of \\(60\\) jobs).','ebc build')
 s=replace_provenance(s,'ebc')
 s=once(s,'Declarations using classical reasoning depend only on \\texttt{Classical.choice}, \\texttt{propext} and \\texttt{Quot.sound}, the standard axioms of Lean\'s classical logic.',
  'The EBC declarations checked in this source family use only those standard classical axioms or none; this does not erase the separate P3 native-evaluation dependencies disclosed below.', 'ebc axioms')
 return s
change('paper05_exact_belief_computation_v16.tex',ebc)
def arv(s):
 old=('declarations using classical reasoning depend only on \\texttt{Classical.choice},\n'
      '\\texttt{propext} and \\texttt{Quot.sound}.')
 s=once(s,old,'the checked bracket declarations use only standard classical axioms or none.\nThe broader project also contains the separately disclosed P3 native-evaluation dependencies.','arv')
 return s
change('paper09b_arv_certification_v2.tex',arv)
# WS and E1 have true *source-scan* claims, but clarify their limited evidentiary scope.
for fn,anchor in [
 ('paper11c_worked_systems_audit_v2.tex','declaration anywhere.\n\n\\noindent\\textbf{Scope'),
 ('paper11_forecasting_baselines_v64.tex','declaration anywhere. The scope is narrow')]:
 def patch(s,fn=fn,anchor=anchor):
  return once(s,anchor,('declaration anywhere. This scans explicit source syntax, not generated\n'
    'axiom footprints; the pinned build succeeds and the project\'s P3 support/value\n'
    'examples retain three \\texttt{native\\_decide} uses (nine generated axiom names).\n\n\\noindent\\textbf{Scope'
    if 'worked_systems' in fn else
    'declaration anywhere. This source scan does not erase three P3\n'
    '\\texttt{native\\_decide} computational proof steps (nine generated\n'
    'axiom names under the pinned build). The scope is narrow'),fn)
 change(fn,patch)
assert len(pending)==8
for p,before,after,diff in pending:
 p.write_text(after)
 if diff is not None:(B/'diffs'/(p.stem+'.diff')).write_text(diff)
 print('UPDATED',p.name)
prehost=(B/'original_sections/paper09b_arv_v2_prehost.tex').read_text()
final_arv=(D/'paper09b_arv_certification_v2.tex').read_text()
(B/'diffs/paper09b_arv_certification_v2_host_2026-10-02.diff').write_text(''.join(unified_diff(prehost.splitlines(True),final_arv.splitlines(True),fromfile='original_sections/paper09b_arv_v2_prehost.tex',tofile='drafts/paper09b_arv_certification_v2.tex')))
print('Source-specific Lean prose corrections staged; rebuild TeX/PDF and review all diffs before claiming final source.')

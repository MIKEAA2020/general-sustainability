#!/usr/bin/env python3
"""Report-only source-year family preservation screen (not a correctness gate)."""
import json,sys
from pathlib import Path
sys.path.insert(0,'/home/user/content_audit')
from scan_content import HEAD, comparison
ROOT=Path('/home/user/content_audit/family_depth')
D=ROOT/'source'
series={
 'obstr':('paper01','paper2_obstruction_calculus_v','_Automatica_routes.tex',[53,54,55,56]),
 'comp':('paper03','paper2_computational_certification_v','.tex',[16,17,18,19,20]),
 'ws':('paper11c','paper2_worked_systems_v','.tex',[15,16,17]),
 'minimax':('paper04','minimax_dual_certificates_v','.tex',[8,9,10,11,12]),
 'ebc':('paper05','paper2_exact_belief_computation_v','.tex',[8,9,10,11,12,13]),
 'psuff':('paper02','paper2_probabilistic_sufficiency_v','.tex',[10,11,12,13,14]),
 'arv':('paper09b','applied_regime_viability_v','.tex',[7,8,9]),
 'e1':('paper11','paperE1_cod_forecast_ladder_v','.tex',[56,57,58,59,60]),
}
results=[]
for fam,(key,pre,suf,vers) in series.items():
 for v in vers:
  src=D/f'{pre}{v}{suf}'
  r=comparison(src,HEAD[key],key,'source-year-'+fam)
  r.update(family=fam,version=v)
  results.append(r)
  print(f'{fam:8} {v:2d} coverage={r["coverage"]:.2%} runs={len(r["missing_runs"]):2d} labels={len(r["missing_labels"]):2d} figures={len(r["missing_figs"]):2d}')
for v in [49,50,51]:
 src=D/f'paper2_obstruction_calculus_v{v}_Automatica_routes_supplementary.tex'
 r=comparison(src,Path('/home/user/papers/paper01_obstruction_calculus_v63_supplementary.tex'),'paper01s','source-year-obstr-supp')
 r.update(family='obstr_supp',version=v);results.append(r)
 print(f'obstr_supp {v} coverage={r["coverage"]:.2%} runs={len(r["missing_runs"])}')
for v,n in [(4,'paper2_computational_certification_v4_supplementary.tex'),(5,'paper2_computational_certification_v5_supplementary.tex'),(6,'paper2_computational_certification_supplementary_v6.tex')]:
 src=D/n;r=comparison(src,HEAD['paper03'],'paper03s','source-year-comp-supp-vs-main')
 r.update(family='comp_supp_vs_main',version=v);results.append(r)
 print(f'comp_supp {v} vs main coverage={r["coverage"]:.2%} runs={len(r["missing_runs"])}')
(ROOT/'comparisons.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')

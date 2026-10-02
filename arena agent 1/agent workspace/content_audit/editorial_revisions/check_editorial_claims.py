#!/usr/bin/env python3
"""Scoped textual/attachment crosswalk; not an independent proof of all manuscript claims."""
from pathlib import Path
import hashlib,json,re
R=Path('/home/user');P=R/'papers';S=R/'paper 2 family';results=[]
def check(name,ok,detail=''):
 results.append({'check':name,'passed':bool(ok),'detail':detail});print('PASS' if ok else 'FAIL',name,detail)
for d in (P,S/'01_obstruction'):
 t=(d/'paper01_obstruction_calculus_v64.tex').read_text();supp=(d/'paper01_obstruction_calculus_v64_supplementary.tex').read_text()
 check(str(d.relative_to(R))+' 01 construction',all(q in t for q in [r'r(S)=S',r'S(0)e^{-t}',r't=\log S(0)',r'\{0, S\}']))
 check(str(d.relative_to(R))+' 01 supplement control',all(q in supp for q in [r'[0,2]',r'u=m',r'm+(S(0)-m)e^{-t}', 'unsuccessful search for a barrier is inconclusive']))
for d in (P,S/'09_cod_with_arv'):
 t=(d/'paper09_cod_certification_v33.tex').read_text()
 check(str(d.relative_to(R))+' 09 new xte conclusion',all(q in t for q in [r'7.4898',r'7.49 & 276.0 & 276.0',r'345.00']) and 'Author, C., et al., in preparation' not in t)
for d in (P,S/'11_forecasting_baselines'):
 t=(d/'paper11_forecasting_baselines_v65.tex').read_text();sp=d/'paper11_forecasting_baselines_v65_SI.md'
 check(str(d.relative_to(R))+' cod SI provenance',sp.is_file() and hashlib.sha256(sp.read_bytes()).hexdigest()=='fb3f8bd2e1eb5590c20371a6107fe7a40670eb67c8f92ae73682e26c31a4f122' and all(re.search(r'^## SI-'+str(i)+r'\b',sp.read_text(),re.M) for i in range(1,6)) and all('SI-'+str(i) in t for i in range(1,6)))
 check(str(d.relative_to(R))+' protocol',all(q in t for q in ['distinct retention protocols','one-horizon point rule','non-nested comparator declarations']))
for d in (P,S/'11c_worked_systems'):
 t=(d/'paper11c_worked_systems_audit_v3.tex').read_text();check(str(d.relative_to(R))+' toy provenance','constructed worked example' in t and 'systems are drawn from the applied model' not in t)
for d in (P,S/'05_exact_belief_computation'):
 t=(d/'paper05_exact_belief_computation_v17.tex').read_text();files=d/'artifacts/ebc_fivecube'
 check(str(d.relative_to(R))+' five-cube artifacts',all((files/q).is_file() for q in ['alpha_check.py','witnesses.py','alpha_run_2026-10-02.log','witnesses_run_2026-10-02.log']) and 'Alongside it, the results of\nThe formal layer' not in t)
for d in (P,S/'03_computational_certification'):
 t=(d/'paper03_computational_certification_v17.tex').read_text();check(str(d.relative_to(R))+' supplement pointer','paper03\\_computational\\_certification\\_v17\\_supplementary.tex' in t and (d/'paper03_computational_certification_v17_supplementary.tex').exists())
for d,n in [(P,'paper07_sampled_governance_v51.tex'),(P,'paper08_governance_delay_v47.tex')]:
 t=(d/n).read_text();check(n+' distinct sections',t.count('3.4.1 Sensitivity')==1 and t.count('3.5 The selected 42-stock')==1 and '3.5 Sensitivity' not in t)
a=(P/'paper08_governance_delay_v47_supplementary_delay.md').read_text();check('08 delay vs sampled interval','not the sampled review interval $T_r$' in a and 'Headline status (updated' in a)
check('08 main cross-candidate pointer','The cross-candidate interval-enclosure table is in the main text' in (P/'paper08_governance_delay_v47.tex').read_text())
for log in ['COMPILE_RESULTS.json','STAGED_COMPILE_RESULTS.json']:
 data=json.loads((R/'content_audit/editorial_revisions'/log).read_text());check(log+' all TeX main and supp compilation',all(x['status']=='compiled' and not x['undefined_references'] for x in data),f'{len(data)} units; all supplied figures real')
(R/'content_audit/editorial_revisions'/'CLAIM_CHECK_RESULTS.json').write_text(json.dumps(results,indent=2))
assert all(x['passed'] for x in results)

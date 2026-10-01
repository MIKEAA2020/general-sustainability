#!/usr/bin/env python3
"""Read-only retrieval of manuscript seeds documented in the paper headers.
Records Git blob SHA and byte length for reproducibility. Never overwrites existing files.
"""
import json, urllib.request, urllib.parse, pathlib, hashlib
BASE='https://api.github.com/repos/MIKEAA2020/general-sustainability'
PAT=open('/home/user/uploads/github_pat.txt').read().strip()
H={'Authorization':'Bearer '+PAT,'Accept':'application/vnd.github+json','User-Agent':'content-audit'}
url=BASE+'/git/trees/e2-v3-source-year?recursive=1'
tree=json.load(urllib.request.urlopen(urllib.request.Request(url,headers=H)))
assert not tree['truncated']
items={x['path']:x for x in tree['tree']}
SEEDS={
 '01':'arena agent 1/agent workspace/diffs/obstr_v57.tex',
 '02':'arena agent 1/paper rewrites/latex/paper2_probabilistic_sufficiency_v14.tex',
 '03':'arena agent 1/paper rewrites/latex/paper2_computational_certification_v20.tex',
 '04':'arena agent 1/agent workspace/fam/minimax_v11.tex',
 '05':'arena agent 1/paper rewrites/latex/paper2_exact_belief_computation_v13.tex',
 '06':'arena agent 1/paper rewrites/latex/paper1_assessment_separation_v63.tex',
 '07':'arena agent 1/agent workspace/diffs/p5_v47.tex',
 '08':'arena agent 1/agent workspace/diffs/p4_v41.tex',
 '09':'arena agent 1/agent workspace/fam/e2/paperE2_cod_intervention_v29.tex',
 '09b':'arena agent 1/paper rewrites/latex/applied_regime_viability_v9.tex',
 '10':'paper3/latest-2026-09-19/manuscript/paper3_material_ledgers_v50.tex',
 '10b':'arena agent 1/paper rewrites/latex/paperE4_edwards_intervention_v16.tex',
 '11':'arena agent 1/paper rewrites/latex/paperE1_cod_forecast_ladder_v60.tex',
 '11b':'arena agent 1/paper rewrites/latex/paperE3_edwards_forecast_ladder_v17.tex',
 '11c':'arena agent 1/agent workspace/fam/ws_v17.tex',
 '01s':'arena agent 1/paper rewrites/latex/paper2_obstruction_calculus_v51_Automatica_routes_supplementary.tex',
 '06s':'arena agent 1/paper rewrites/paper1_supplementary_v12.md',
 '08sd':'arena agent 1/paper rewrites/paper4_supplementary_v8.md',
 '08sg19':'arena agent 1/paper rewrites/paper5_supplementary_v19_NatSustain.md',
 '08sg20':'arena agent 1/paper rewrites/paper5_supplementary_v20_blinded_NatSustain.md',
 '10sm':'paper3/latest-2026-09-19/manuscript/paper3_supplementary_v18.md',
 '10st':'paper3/latest-2026-09-19/manuscript/paper3_supplementary_v18.tex',
}
D=pathlib.Path('/home/user/content_audit/seeds');D.mkdir(parents=True,exist_ok=True)
manifest={}
for k,p in SEEDS.items():
    if p not in items:
        print('NOT IN TREE',k,p);continue
    dest=D/(k+'_'+p.rsplit('/',1)[-1]); blob=items[p]
    if dest.exists():b=dest.read_bytes()
    else:
        raw='https://raw.githubusercontent.com/MIKEAA2020/general-sustainability/e2-v3-source-year/'+urllib.parse.quote(p)
        b=urllib.request.urlopen(urllib.request.Request(raw,headers={'User-Agent':'content-audit'}),timeout=120).read()
        if b'404: Not Found' == b:raise ValueError(p)
        dest.write_bytes(b)
    assert len(b)==blob['size'],(k,p,len(b),blob['size'])
    manifest[k]={'repo_path':p,'blob_sha':blob['sha'],'size':len(b),'sha256':hashlib.sha256(b).hexdigest(),'local':str(dest)}
    print(k,len(b),dest.name,flush=True)
(D.parent/'seed_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('fetched/verified',len(manifest),'tree truncated',tree['truncated'])

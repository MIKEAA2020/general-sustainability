from pathlib import Path
import json,shutil,hashlib,ast,csv
P=Path('/home/user/ecomod_followup_feasibility_R03');D=Path('/home/user/.cache/cci_next_R03');B=Path('/home/user/ecomod_followup_F09')
files=['acquisition_sources.json','harmonization_code_identity.json','plot2map_code_identity.json','agbref_preprint_identity.json','native_reacquisition.json','native_metadata_identity.json','agbref_archive_directory.json','agbref_archive_head.json','agbref_range_probe.json','local_reference_rows.json']
for name in files:shutil.copyfile(D/name,P/'metadata'/name.replace('.json','_R03.json'))
# Public catalogue metadata, not source measurements/full reports/code.
for name in ['agbref_record.json','agbref_versions_latest.json','irati_record.json','zenodo_code_record.json','agbref_files.json']:
 shutil.copyfile(D/name,P/'metadata'/name.replace('.json','_R03.json'))
reg=json.loads((B/'metadata/native_probe_provenance.json').read_text());rows=[r for r in reg['native_payloads']if r['ISO3']=='BRA'];(P/'metadata/native_payload_registry_R03.json').write_text(json.dumps(rows,indent=2)+'\n')
plan={'revision':'R03','geometry_changed':False,'window':{'rows':[105890,106145],'columns':[146433,146688]},'maximum_response_bytes':25000000,'initial_descriptive_inspection_preceded_this_record':True,'no_prospective_registration_claim':True,'analyses':['integer SD validity and zero patterns','positive-AGB SD descriptive quantiles','stored zero-state cross-tabulation'],'not_permitted_inference':['true absence','zero true error','cross-year error covariance from map/SD correlation','forest-stock change','calibrated interval coverage','national estimates'],'raw_native_arrays_redistributed':False}
(P/'protocol/NATIVE_SD_SCOPE_R03.json').write_text(json.dumps(plan,indent=2)+'\n')
# Source code facts with exact line addresses, not redistributed full code.
s=(D/'script.py').read_text();tree=ast.parse(s);facts=[]
for node in ast.walk(tree):
 if isinstance(node,ast.Assign):
  names=[ast.unparse(t)for t in node.targets]
  if any(x in names for x in ['std_diff','no_std','annual_incr']):facts.append({'symbol':';'.join(names),'line_start':node.lineno,'line_end':node.end_lineno,'expression':ast.unparse(node.value)})
 if isinstance(node,ast.Call)and isinstance(node.func,ast.Attribute)and node.func.attr=='SetNoDataValue':facts.append({'symbol':'SetNoDataValue','line_start':node.lineno,'line_end':node.end_lineno,'expression':ast.unparse(node)})
code={'provider_change_script_url':next(r['url']for r in json.loads((D/'acquisition_sources.json').read_text())if r['key']=='script'),'bytes':len(s.encode()),'sha256':hashlib.sha256(s.encode()).hexdigest(),'matches_F08_F09_source_identity':True,'facts':facts,'provider_script_executed':False,'production_aggregation_kernel_located':False,'production_normalization_verified':False,'released_files_inferred_to_have_flag_NODATA_zero':False,'scope':'Reverified distributed change script; article-linked code folder and selected Plot2Map validation-tool files, not all possible repositories'}
(P/'metadata/implementation_audit_R03.json').write_text(json.dumps(code,indent=2)+'\n')
# Preserve a compact, properly attributed local derived subset (4 released aggregate rows).
local=json.loads((D/'local_reference_rows.json').read_text());out=[]
for member,info in local['members'].items():
 for row in info['inside']:
  out.append({'source_member':member,'source_record':'20793072',**row,'eligible_primary_2015_2023':'no','reason':'No labelled2023 endpoint; N=1; minimum/local-representativity/strict flags=0; original census identity/date absent'})
fields=list(dict.fromkeys(k for r in out for k in r))
with (P/'data/local_reference_candidate_R03.csv').open('w',newline='')as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(out)
(P/'metadata/prior_package_manifest_hashes_R03.json').write_text(json.dumps({name:hashlib.sha256(Path('/home/user',name,manifest).read_bytes()).hexdigest()for name,manifest in [('ecomod_followup_F08','artifact_manifest.json'),('ecomod_followup_F09','artifact_manifest_F09.json')]},indent=2)+'\n')
print('Code facts',facts,'local derived rows',len(out))

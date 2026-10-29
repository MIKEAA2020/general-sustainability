"""R03 evidence consistency/preservation and artifact manifest; no validation claim."""
from pathlib import Path
import argparse,hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
MANIFEST='artifact_manifest_R03.json';EXCLUDED={'.cache','__pycache__'}
def require(v,m):
    if not v:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def files():return sorted(p for p in ROOT.rglob('*')if p.is_file()and not any(x in EXCLUDED for x in p.relative_to(ROOT).parts)and p.name!=MANIFEST)
def verify():
    m=json.loads((ROOT/MANIFEST).read_text());require({str(p.relative_to(ROOT))for p in files()}=={r['path']for r in m['files']},'Manifest coverage')
    for r in m['files']:require((ROOT/r['path']).stat().st_size==r['bytes']and sha(ROOT/r['path'])==r['sha256'],'Artifact changed')
    return len(m['files'])
def record():
    expected=json.loads((ROOT/'metadata/prior_package_manifest_hashes_R03.json').read_text());protected={}
    for folder,name in [('ecomod_followup_F08','artifact_manifest.json'),('ecomod_followup_F09','artifact_manifest_F09.json')]:
        base=ROOT.parent/folder;require(sha(base/name)==expected[folder],'Protected manifest changed');m=json.loads((base/name).read_text())
        for r in m['files']:require(sha(base/r['path'])==r['sha256'],'Protected package changed')
        protected[folder]=len(m['files'])+1
    tests={}
    for name in ['tests_R03_all.txt','tests_R03_optimized.txt']:
        p=ROOT/'metadata'/name;t=p.read_text();n=int(re.search(r'Ran (\d+) tests',t).group(1));require(n==36 and t.rstrip().endswith('OK'),'Test failure');tests[name]={'passed':n,'sha256':sha(p)}
    a=json.loads((ROOT/'metadata/reference_archive_inspection_R03.json').read_text());b=json.loads((ROOT/'metadata/reference_archive_reproduction_R03.json').read_text());guard=json.loads((ROOT/'protocol/REFERENCE_ARCHIVE_GUARD_R03.json').read_text())
    require(a['selected']==b['selected'],'Archive reproduction differs');require(a['unique_source_bytes_represented']<=guard['maximum_cumulative_source_bytes'],'Archive guard exceeded')
    require(not a['whole_archive_md5_verified']and not a['whole_archive_downloaded'],'False whole-file claim')
    require(all(r['crc_verified_complete_member']for r in a['selected']),'Member CRC missing')
    code=json.loads((ROOT/'metadata/code_reverification_R03.json').read_text());require(len(code['verified'])==21 and not code['provider_code_executed'],'Code verification scope')
    native=json.loads((ROOT/'metadata/native_sd_audit_R03.json').read_text());require(native['original_payloads_full_SHA256_matched']and not native['new_error_covariance_estimated']and not native['country_admissions_changed'],'Native scope')
    result={'revision':'R03','date':'2026-10-29','protected_package_files_verified':protected,'tests':tests,'code_files_full_SHA256_reverified_not_executed':21,'reference_complete_members_CRC_verified':4,'reference_unique_source_bytes':a['unique_source_bytes_represented'],'reference_source_cap_bytes':guard['maximum_cumulative_source_bytes'],'whole_ZIP_MD5_verified':False,'archive_cache_reproduction_selected_results_exact':True,'archive_reproduction_new_body_bytes':b['network_bytes_this_run'],'native_original_payloads_full_SHA256_matched':True,'new_eligible_paired_reference':False,'production_aggregation_lineage_resolved':False,'calibrated_change_uncertainty_added':False,'national_admissions_changed':False,'technical_checks_are_ecological_validation':False,'provider_questions_sent':False}
    (ROOT/'metadata/verification_R03.json').write_text(json.dumps(result,indent=2)+'\n')
    m={'revision':'R03','self_excluded':True,'excluded_directories':sorted(EXCLUDED),'files':[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)}for p in files()]};(ROOT/MANIFEST).write_text(json.dumps(m,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--write',action='store_true');a=p.parse_args()
    if a.write:record()
    print(json.dumps({'verified_manifest_files':verify(),'technical_QA_not_ecological_validation':True}))

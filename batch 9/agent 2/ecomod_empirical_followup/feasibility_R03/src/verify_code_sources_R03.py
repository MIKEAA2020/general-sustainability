"""Verify pinned code bytes without executing third-party code; cache only."""
from pathlib import Path
import argparse, hashlib, json
import requests
ROOT=Path(__file__).resolve().parents[1]
CAP=2_000_000

def verify(cache):
    groups=[('harmonization_code','harmonization_code_identity_R03.json'),('plot2map','plot2map_code_identity_R03.json')]
    rows=[]
    for folder,name in groups:
        for row in json.loads((ROOT/'metadata'/name).read_text()):
            rows.append((row,cache/folder/row['path'].replace('/','__')))
    script=json.loads((ROOT/'metadata/implementation_audit_R03.json').read_text())
    rows.append(({'url':script['provider_change_script_url'],'bytes':script['bytes'],'sha256':script['sha256'],'path':'create_change_maps.py'},cache/'script.py'))
    if sum(r['bytes']for r,p in rows)>CAP:raise ValueError('Code source cap')
    verified=[]
    for row,path in rows:
        path.parent.mkdir(parents=True,exist_ok=True)
        if not path.exists():
            with requests.get(row['url'],stream=True,timeout=(20,90))as response:
                response.raise_for_status();out=bytearray()
                for b in response.iter_content(65536):
                    out.extend(b)
                    if len(out)>row['bytes']:raise ValueError('Code size cap')
            path.write_bytes(out)
        data=path.read_bytes()
        if len(data)!=row['bytes']or hashlib.sha256(data).hexdigest()!=row['sha256']:raise ValueError('Code SHA256 mismatch')
        if 'git_blob'in row:
            blob=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
            if blob!=row['git_blob']:raise ValueError('Git blob mismatch')
        verified.append({'path':row['path'],'sha256':row['sha256'],'bytes':len(data),'git_blob_verified':'git_blob'in row})
    return {'verified':verified,'bytes_represented':sum(r['bytes']for r in verified),'provider_code_executed':False,'production_v7_aggregation_lineage_verified':False}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--cache',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();result=verify(a.cache);a.output.write_text(json.dumps(result,indent=2)+'\n');print('Verified',len(result['verified']),'source files; none executed')

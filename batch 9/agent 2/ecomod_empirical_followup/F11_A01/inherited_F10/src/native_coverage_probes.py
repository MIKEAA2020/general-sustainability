"""Bounded native coverage probes, not a national sample or biomass analysis.
Reads native values solely to distinguish fill, zero, invalid and valid support.
No stock, mean density, difference, sign, trend or error-rate estimate is made.
"""
from pathlib import Path
import json,re,hashlib,argparse,concurrent.futures
import numpy as np
import requests
from shapely import contains_xy
from physical_support import ROOT,load_boundary,write_csv

def parse_ascii(text,shape):
    if '---------------------------------------------' not in text:raise ValueError('Missing DAP ASCII separator')
    data=text.split('---------------------------------------------',1)[1];values={};current=None
    for line in data.splitlines():
        line=line.strip()
        m=re.match(r'(agb(?:_sd)?)(?:\.\1)?\[',line)
        if m:current=m.group(1);values[current]=[];continue
        if current and line.startswith('['):
            tail=re.sub(r'^(?:\[\d+\])+\s*,?\s*','',line)
            a=np.fromstring(tail,sep=',',dtype=np.int32)
            values[current].extend(a.tolist())
    expected=int(np.prod(shape));out={}
    for key in ['agb','agb_sd']:
        if len(values.get(key,[]))!=expected:raise ValueError(f'DAP shape mismatch for {key}: {len(values.get(key,[]))} vs {expected}')
        out[key]=np.asarray(values[key],dtype=np.int32).reshape(shape)
    return out

def retrieve(url,dest,cap):
    if dest.exists():return dest.read_bytes()
    r=requests.get(url,stream=True,timeout=(20,120));r.raise_for_status();out=bytearray()
    for b in r.iter_content(262144):
        out.extend(b)
        if len(out)>cap:raise ValueError('Response exceeds collection limit')
    dest.write_bytes(out);return bytes(out)

def run(cache):
    cache.mkdir(parents=True,exist_ok=True);planpath=ROOT/'configs/native_probe_plan_F04.json';planbytes=planpath.read_bytes();plan=json.loads(planbytes);reg=json.loads((ROOT/'metadata/physical_source_registry.json').read_text());h=lambda b:hashlib.sha256(b).hexdigest()
    freeze={'plan_sha256':h(planbytes),'specification_sha256':h((ROOT/'protocol/PHYSICAL_SUPPORT_F04.md').read_bytes()),'selection_basis':'geometry only; no reselection','prior_to_native_payload_requests':True,'interpretation':'Plan timing does not establish prospective registration or independent validation'}
    frozen=ROOT/'metadata/native_probe_freeze.json'
    if frozen.exists():assert json.loads(frozen.read_text())==freeze
    else:frozen.write_text(json.dumps(freeze,indent=2)+'\n')
    jobs=[]
    for p in plan['plans']:
        a,b=p['rows'];c,d=p['columns'];query=f'agb.agb[0][{a}:1:{b}][{c}:1:{d}],agb_sd.agb_sd[0][{a}:1:{b}][{c}:1:{d}]'
        for year in plan['years']:
            url=reg['native_biomass'][str(year)]['url']+'.ascii?'+query;jobs.append((p,year,url))
    payloads={};records=[]
    prior=ROOT/'metadata/native_probe_provenance.json'
    expected={x['url']:x['sha256']for x in json.loads(prior.read_text())['native_payloads']} if prior.exists() else {}
    def job(j):
        p,year,url=j;dest=cache/f"{p['ISO3']}_{year}.ascii";b=retrieve(url,dest,plan['maximum_response_bytes']);assert len(b)<=plan['maximum_response_bytes']
        if expected:assert url in expected and h(b)==expected[url],'Native source changed: reviewed amendment/new revision required'
        a=parse_ascii(b.decode(),p['shape']);return p,year,a,dict(ISO3=p['ISO3'],year=year,url=url,bytes=len(b),sha256=h(b),plan_sha256=freeze['plan_sha256'],cache_filename=dest.name)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2)as executor:
        for p,year,arrays,r in executor.map(job,jobs):
            payloads[p['ISO3'],year]=arrays;records.append(r);print('Retrieved native coverage probe:',p['ISO3'],year,r['bytes'],'bytes',flush=True)
    results=[];joint=[]
    for p in plan['plans']:
        code=p['ISO3'];g,_=load_boundary(code);y0,y1=p['rows'];x0,x1=p['columns'];step=360/405000
        lat=80-(np.arange(y0,y1+1)+.5)*step;lon=-180+(np.arange(x0,x1+1)+.5)*step;xx,yy=np.meshgrid(lon,lat);inside=contains_xy(g,xx,yy);valids={}
        for year in plan['years']:
            arrays=payloads[code,year];a=arrays['agb'];sd=arrays['agb_sd'];v=(a>=0)&(a<=10000);u=(sd>=0)&(sd<=10000);valids[year]=v&u
            results.append(dict(ISO3=code,year=year,probe_cells=int(a.size),polygon_centre_cells=int(inside.sum()),agb_fill_cells=int((a==-32768).sum()),agb_zero_cells=int((a==0).sum()),agb_valid_cells=int(v.sum()),agb_other_invalid_cells=int(((~v)&(a!=-32768)).sum()),sd_valid_cells=int(u.sum()),joint_agb_sd_valid_cells=int((v&u).sum()),polygon_joint_valid_cells=int((inside&v&u).sum()),role='bounded_access_probe_not_national_or_forest_coverage'))
        good=valids[2015]&valids[2023];n=int(inside.sum())
        joint.append(dict(ISO3=code,probe_cells=int(inside.size),both_endpoints_joint_valid_cells=int(good.sum()),polygon_centre_cells=n,polygon_both_endpoints_joint_valid_cells=int((inside&good).sum()),polygon_both_endpoints_valid_fraction=None if n==0 else float((inside&good).sum()/n),national_coverage_established=False,forest_sample_eligible=False))
    write_csv(ROOT/'data/support/native_probe_coverage.csv',results);write_csv(ROOT/'data/support/native_probe_common_coverage.csv',joint)
    out={'native_payloads':records,'interpretation':'Raw values read for coverage only; no national biomass values, stocks, changes or signs computed','global_native_file_downloaded':False,'plan_sha256':freeze['plan_sha256']}
    (ROOT/'metadata/native_probe_provenance.json').write_text(json.dumps(out,indent=2)+'\n')
    return results,joint
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cache',type=Path,required=True);args=p.parse_args();run(args.cache)

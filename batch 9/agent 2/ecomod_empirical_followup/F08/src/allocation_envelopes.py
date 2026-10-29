"""Conditional map-domain biomass allocation sets, not confidence intervals.
Raw source arrays remain external; only aggregate envelopes and overlap counts
are distributed. Every source is matched to inherited payload/range hashes.
"""
from pathlib import Path
import argparse,json,csv,hashlib,math
import numpy as np
import requests,tifffile
from scipy.sparse import csr_matrix
from bounded_tiff import RangeReader
from brazil_support import read_window,tiff_grid,overlap_weights,savecsv
from native_coverage_probes import parse_ascii
ROOT=Path(__file__).resolve().parents[1]

def require(c,m):
    if not c:raise ValueError(m)
def digest(b):return hashlib.sha256(b).hexdigest()
def axis_membership(target,source):
    a=np.asarray(target,float);b=np.asarray(source,float);require(np.all(np.diff(a)>0)and np.all(np.diff(b)>0),'Nonascending edges');rows=[];cols=[]
    for i,(lo,hi)in enumerate(zip(a[:-1],a[1:])):
        first=max(0,np.searchsorted(b,lo,side='right')-1);last=min(len(b)-1,np.searchsorted(b,hi,side='left'))
        for j in range(first,last):
            if min(hi,b[j+1])>max(lo,b[j]):rows.append(i);cols.append(j)
    return csr_matrix((np.ones(len(rows),dtype=np.int32),(rows,cols)),shape=(len(a)-1,len(b)-1))
def certificates(wx,wy,binary):
    x=wx.astype(np.int32);y=wy.astype(np.int32);counts=np.asarray((x@(y@np.asarray(binary,dtype=np.int32)).T).T);total=np.asarray(y.sum(axis=1)).ravel()[:,None]*np.asarray(x.sum(axis=1)).ravel()[None,:]
    require(np.all(total>0)and np.all((counts>=0)&(counts<=total)),'Invalid topology counts');return counts,total

def envelope(mass,counts,total):
    q=np.asarray(mass,float);c=np.asarray(counts);n=np.asarray(total);require(q.shape==c.shape==n.shape,'Envelope shape mismatch');require(np.all(np.isfinite(q))and np.all(q>=0),'Nonfinite/negative mass');require(np.issubdtype(c.dtype,np.integer)and np.issubdtype(n.dtype,np.integer),'Topology counts must be integers');require(np.all(n>0)and np.all((c>=0)&(c<=n)),'Invalid intersection counts')
    pure=c==n;present=c>0;return dict(lower_Mg=float(q[pure].sum()),upper_Mg=float(q[present].sum()),pure_cells=int(pure.sum()),present_cells=int(present.sum()),mixed_cells=int((present&~pure).sum()),absent_cells=int((~present).sum()))
def difference_interval(first,last):
    require(first['lower_Mg']<=first['upper_Mg']and last['lower_Mg']<=last['upper_Mg'],'Reversed endpoint interval');lo=last['lower_Mg']-first['upper_Mg'];hi=last['upper_Mg']-first['lower_Mg'];return dict(lower_change_Mg=lo,upper_change_Mg=hi,contains_zero=bool(lo<=0<=hi))

def native(entry,cache,offline):
    path=cache/entry['cache_filename'];expected=entry['bytes'];require(expected<=25_000_000,'Native cap exceeded')
    if path.exists():b=path.read_bytes()
    else:
        require(not offline,'Missing native offline cache');r=requests.get(entry['url'],stream=True,timeout=(20,120));buf=bytearray()
        try:
            require(r.status_code==200,'Native request failed')
            for block in r.iter_content(65536):buf.extend(block);require(len(buf)<=expected,'Native response length/cap exceeded')
        finally:r.close()
        b=bytes(buf);require(len(b)==expected and digest(b)==entry['sha256'],'Native payload identity drift');cache.mkdir(parents=True,exist_ok=True);path.write_bytes(b)
    require(len(b)==expected and digest(b)==entry['sha256'],'Native cached identity drift');d=parse_ascii(b.decode(),[256,256]);require(all(np.all((v>=0)&(v<=10000))for v in d.values()),'Missing/invalid native support requires explicit amendment');return d

def run(cache,offline=False):
    freeze=json.loads((ROOT/'metadata/allocation/freeze_F07.json').read_text());require(digest((ROOT/'protocol/ALLOCATION_ENVELOPE_F07.md').read_bytes())==freeze['protocol_sha256'],'Frozen protocol drift');require(digest((ROOT/'configs/allocation_F07.json').read_bytes())==freeze['configuration_sha256'],'Frozen configuration drift');cfg=json.loads((ROOT/'configs/allocation_F07.json').read_text())
    inputs=json.loads((ROOT/'metadata/allocation/input_hashes_F07.json').read_text())
    for p,h in inputs.items():require(digest((ROOT/p).read_bytes())==h,'Inherited input drift: '+p)
    old=json.loads((ROOT/'metadata/brazil/range_provenance.json').read_text());native_entries=[r for r in json.loads((ROOT/'metadata/native_probe_provenance.json').read_text())['native_payloads']if r['ISO3']=='BRA'];t=old['CCI_affine'];r0,r1=cfg['rows'];c0,c1=cfg['columns'];xe=t[0]+np.arange(c0,c1+2)*t[1];ye=t[3]+np.arange(r0,r1+2)*t[5];saved=np.load(ROOT/'data/brazil/BRA_F05_support_fractions.npz');area=saved['cell_area_ha'];rows=[];aux=[];arrays={};provenance=[];by_group={g:{}for g in cfg['groups']}
    for year in cfg['years']:
        entry=next(e for e in native_entries if e['year']==year);d=native(entry,cache/'native',offline);mass=area*d['agb'];aux.append(dict(year=year,full_window_cell_mass_auxiliary_Mg=float(mass.sum()),cells=int(mass.size),observed_zero_density_cells=int((d['agb']==0).sum()),interpretation='full_pixel_auxiliary_not_forest_stock_or_national_estimate'))
        src=next(e for e in old['endpoints']if e['year']==year);rr=RangeReader(src['url'],src['whole_object_size'],src['etag'],cache/'ranges'/str(year),cap=cfg['cover_range_cap_per_endpoint'])
        if offline:
            def denied(*a,**k):raise ValueError('Missing range cache in offline mode')
            rr.session.get=denied
        with tifffile.TiffFile(rr)as tf:
            require(len(tf.pages)==1,'Unexpected TIFF pages');g=tiff_grid(tf.pages[0]);require(g==src['source_grid'],'Source grid drift');a,tiles=read_window(rr,tf.pages[0],src['fine_window']);require(digest(a.tobytes())==src['decoded_subset_sha256'],'Decoded source subset drift');require(not np.isin(a,[0,27]).any(),'Unclassified support requires amendment')
        iy0,iy1,ix0,ix1=src['fine_window'];fx=g['x0']+np.arange(ix0,ix1+1)*g['dx'];fy=g['y0']-np.arange(iy0,iy1+1)*g['dy'];require(fx[0]<=xe[0]and fx[-1]>=xe[-1]and fy[0]>=ye[0]and fy[-1]<=ye[-1],'Partial source coverage')
        wx=axis_membership(xe,fx);wy=axis_membership(ye[::-1],fy[::-1]);weightsx=overlap_weights(xe,fx);weightsy=overlap_weights(ye[::-1],fy[::-1],latitude=True)
        maxerr=0.
        for group,codes in cfg['groups'].items():
            binary=np.isin(a[::-1],codes);counts,total=certificates(wx,wy,binary);counts=counts[::-1];total=total[::-1];fraction=np.asarray((weightsx@(weightsy@binary.astype(float)).T).T)[::-1];key='forest_formations'if group=='forest_formations'else 'forest_plus_savanna';err=float(np.abs(fraction-saved[f'{key}_{year}']).max());require(err<1e-12,'Fraction alignment drift');maxerr=max(maxerr,err)
            out=envelope(mass,counts,total);rows.append(dict(year=year,group=group,**out,interpretation='conditional_on_exact_point_maps_nonnegative_unconstrained_allocation_not_CI'));by_group[group][year]=out;arrays[f'{group}_intersections_{year}']=counts.astype(np.uint16);arrays[f'total_intersections_{year}']=total.astype(np.uint16)
        actual=rr.receipts();expected={(r['start'],r['end']):r['sha256']for r in src['ranges']}
        require(all(expected.get((r['start'],r['end']))==r['sha256']for r in actual),'Accessed source range not verified against F05');provenance.append(dict(year=year,native_payload_sha256=entry['sha256'],native_bytes=entry['bytes'],decoded_cover_sha256=digest(a.tobytes()),distinct_cover_bytes=rr.transferred,source_ranges_match_F05=True,tiles_match_F05=tiles==src['tiles_decoded'],fraction_alignment_max_error=maxerr));rr.close();print('Computed conditional allocation endpoints',year,flush=True)
    changes=[dict(group=g,**difference_interval(v[2015],v[2023]),interpretation='allocation_difference_interval_not_measurement_error_or_validated_ecological_change')for g,v in by_group.items()]
    savecsv(ROOT/'data/allocation/endpoint_envelopes_F07.csv',rows);savecsv(ROOT/'data/allocation/difference_envelopes_F07.csv',changes);savecsv(ROOT/'data/allocation/full_cell_auxiliary_F07.csv',aux);np.savez_compressed(ROOT/'data/allocation/overlap_certificates_F07.npz',**arrays)
    (ROOT/'metadata/allocation/computation_F07.json').write_text(json.dumps({'sources':provenance,'all_65536_cells_used_at_each_endpoint':True,'integer_topology_not_fraction_threshold':True,'no_density_fraction_stock_estimator':True,'measurement_uncertainty_calibrated':False,'primary_stock_target_replaced':False,'national_inference':False,'assumptions':cfg['allocation_assumptions']},indent=2)+'\n');print(json.dumps({'endpoints':rows,'differences':changes,'auxiliary':aux},indent=2));return rows,changes

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cache',type=Path,required=True);p.add_argument('--offline',action='store_true');a=p.parse_args();run(a.cache,a.offline)

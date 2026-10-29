"""Bounded external land-cover support on the unchanged F04 Brazil CCI window.
No national forest change, biomass stock or transition accuracy is estimated.
"""
from pathlib import Path
import sys,json,re,math,csv,hashlib,argparse
import numpy as np
from scipy.sparse import csr_matrix
import tifffile
from bounded_tiff import RangeReader
from estimands import wgs84_rectangle_area_ha
ROOT=Path(__file__).resolve().parents[1]

def require(condition,message='Support verification failed'):
    if not condition:raise ValueError(message)

def primitive(lat):
    f=1/298.257223563;e2=f*(2-f);e=math.sqrt(e2);s=np.sin(np.deg2rad(lat))
    return s/(2*(1-e2*s*s))+np.arctanh(e*s)/(2*e)

def overlap_weights(target_edges,source_edges,latitude=False):
    """Ascending edges. Exact normalized longitude or WGS84 latitude integrals.
    Missing spatial support is NOT renormalized to one.
    """
    a=np.asarray(target_edges,float);b=np.asarray(source_edges,float)
    if not(np.all(np.diff(a)>0)and np.all(np.diff(b)>0)):raise ValueError('Ascending edges required')
    fn=primitive if latitude else lambda x:x;rows=[];cols=[];values=[]
    for i,(lo,hi)in enumerate(zip(a[:-1],a[1:])):
        start=max(0,np.searchsorted(b,lo,side='right')-1);stop=min(len(b)-1,np.searchsorted(b,hi,side='left'))
        den=fn(hi)-fn(lo)
        for j in range(start,stop):
            l=max(lo,b[j]);h=min(hi,b[j+1])
            if h>l:rows.append(i);cols.append(j);values.append(float((fn(h)-fn(l))/den))
    return csr_matrix((values,(rows,cols)),shape=(len(a)-1,len(b)-1))

def tiff_grid(p):
    scale=p.tags['ModelPixelScaleTag'].value;tie=p.tags['ModelTiepointTag'].value;keys=p.tags['GeoKeyDirectoryTag'].value;entries={keys[i]:keys[i:i+4]for i in range(4,len(keys),4)}
    if entries.get(2048,[0,0,0,0])[3]!=4326 or entries.get(1025,[0,0,0,0])[3]!=1:raise ValueError('Require WGS84 geographic pixel-area raster')
    if p.dtype!=np.dtype('uint8')or not p.is_tiled or p.samplesperpixel!=1:raise ValueError('Unexpected raster representation')
    if 'ModelTransformationTag' in p.tags or scale[0]<=0 or scale[1]<=0:raise ValueError('Require north-up unrotated grid')
    return dict(x0=float(tie[3]-tie[0]*scale[0]),y0=float(tie[4]+tie[1]*scale[1]),dx=float(scale[0]),dy=float(scale[1]),height=p.imagelength,width=p.imagewidth,tilewidth=p.tilewidth,tileheight=p.tilelength)

def read_window(rr,p,window):
    y0,y1,x0,x1=window;out=np.empty((y1-y0,x1-x0),dtype=p.dtype);th=p.tilelength;tw=p.tilewidth;nt=math.ceil(p.imagewidth/tw);tiles=[]
    for gy in range(y0//th,(y1-1)//th+1):
        for gx in range(x0//tw,(x1-1)//tw+1):
            index=gy*nt+gx;off=int(p.dataoffsets[index]);count=int(p.databytecounts[index]);rr.seek(off);b=rr.read(count);decoded,_,_=p.decode(b,index)
            if decoded is None:raise ValueError('Missing tile cannot be silently treated as zero')
            tile=decoded[0,:,:,0];ay=max(y0,gy*th);by=min(y1,(gy+1)*th);ax=max(x0,gx*tw);bx=min(x1,(gx+1)*tw)
            out[ay-y0:by-y0,ax-x0:bx-x0]=tile[ay-gy*th:by-gy*th,ax-gx*tw:bx-gx*tw];tiles.append(index)
    return out,tiles

def savecsv(path,rows):
    with path.open('w',newline='')as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def run(cache):
    cfg=json.loads((ROOT/'configs/brazil_support_F05.json').read_text());freeze=json.loads((ROOT/'metadata/brazil/support_freeze_F05.json').read_text());h=lambda b:hashlib.sha256(b).hexdigest()
    for key,path in [('protocol_sha256','protocol/BRAZIL_SUPPORT_F05.md'),('configuration_sha256','configs/brazil_support_F05.json'),('legend_sha256','metadata/brazil/legend_collection11.csv')]:require(freeze[key]==h((ROOT/path).read_bytes()),'Frozen support rule changed')
    old=json.loads((ROOT/'configs/native_probe_plan_F04.json').read_text());bra=next(x for x in old['plans']if x['ISO3']=='BRA');require(cfg['rows']==bra['rows']and cfg['columns']==bra['columns'])
    endpoints=json.loads((ROOT/'metadata/forest_observation_candidates_F04.json').read_text())['MapBiomas_Brazil']['endpoints'];legend={int(x['class_id']):x['class_name_en']for x in csv.DictReader((ROOT/'metadata/brazil/legend_collection11.csv').open())};legend.update({0:'Unclassified/absent code',27:'Legacy unobserved code'})
    # Read the actual declared native affine transform; do not assume exact nominal spacing.
    transforms=[]
    for year in cfg['years']:
        das=(ROOT/f'metadata/geography/CCI_native_{year}.das').read_text();s=re.search(r'String GeoTransform "([^"]+)"',das).group(1);transforms.append([float(x)for x in s.split()])
    require(transforms[0]==transforms[1]);t=transforms[0];require(t[2]==t[4]==0 and t[1]>0 and t[5]<0)
    y0,y1=cfg['rows'];x0,x1=cfg['columns'];xe=t[0]+np.arange(x0,x1+2)*t[1];ye=t[3]+np.arange(y0,y1+2)*t[5];west,east=xe[0],xe[-1];south,north=ye[-1],ye[0]
    rowarea=np.array([wgs84_rectangle_area_ha(xe[0],xe[1],ye[j+1],ye[j])for j in range(len(ye)-1)]);areas=np.broadcast_to(rowarea[:,None],(256,256)).copy();footprint=areas.sum();outputs={};summaries=[];classes=[];receipts=[];grids=[];checks=[]
    for entry in endpoints:
        year=entry['year'];headers=entry['headers'];url=entry['url']+'?generation='+headers['x-goog-generation'];rr=RangeReader(url,int(headers['x-goog-stored-content-length']),headers['ETag'],cache/str(year),cap=cfg['maximum_bytes_per_endpoint'])
        with tifffile.TiffFile(rr)as tf:
            p=tf.pages[0];g=tiff_grid(p);grids.append(g);iy0=math.floor((g['y0']-north)/g['dy']);iy1=math.ceil((g['y0']-south)/g['dy']);ix0=math.floor((west-g['x0'])/g['dx']);ix1=math.ceil((east-g['x0'])/g['dx']);window=[iy0,iy1,ix0,ix1]
            require(0<=iy0<iy1<=g['height']and 0<=ix0<ix1<=g['width']);a,tiles=read_window(rr,p,window);unexpected=set(map(int,np.unique(a)))-set(legend)
            if unexpected:raise ValueError('Unexpected cover codes: '+str(unexpected))
            fe_x=g['x0']+np.arange(ix0,ix1+1)*g['dx'];fe_y=g['y0']-np.arange(iy0,iy1+1)*g['dy'];wx=overlap_weights(xe,fe_x);wy=overlap_weights(ye[::-1],fe_y[::-1],latitude=True)
            error=max(float(np.abs(np.asarray(wx.sum(axis=1)).ravel()-1).max()),float(np.abs(np.asarray(wy.sum(axis=1)).ravel()-1).max()));require(error<1e-9)
            # Fine pixels south-to-north for separable latitude integration.
            array=a[::-1];group=dict(cfg['classification_groups']);assigned={c for codes in group.values()for c in codes};group['other_mapped']=sorted(set(legend)-assigned);part=[]
            # Exact fine-pixel area within the target rectangle, including clipped boundary pixels.
            fy_s=np.maximum(fe_y[1:],south);fy_n=np.minimum(fe_y[:-1],north);fx_w=np.maximum(fe_x[:-1],west);fx_e=np.minimum(fe_x[1:],east);fine_lat=np.maximum(0,primitive(fy_n)-primitive(fy_s));fine_lon=np.maximum(0,np.deg2rad(fx_e-fx_w));f=1/298.257223563;aa=6378137.;e2=f*(2-f);fine_area=aa*aa*(1-e2)/1e4*fine_lat[:,None]*fine_lon[None,:]
            max_area_error=0
            for name,codes in group.items():
                binary=np.isin(array,codes).astype(float);fraction=np.asarray((wx@(wy@binary).T).T)[::-1];require(fraction.min()>=-1e-12 and fraction.max()<=1+1e-9);fraction=np.clip(fraction,0,1);part.append(fraction);outputs[f'{name}_{year}']=fraction
                area=float((fraction*areas).sum());direct=float(fine_area[np.isin(a,codes)].sum());err=abs(area-direct);max_area_error=max(max_area_error,err);require(err/max(1,footprint)<1e-9)
                summaries.append(dict(year=year,group=name,area_ha=area,footprint_fraction=area/footprint,interpretation='local_mapped_cover_not_validated_forest_land_use_or_change'))
            total=np.sum(part,axis=0);require(np.max(np.abs(total-1))<1e-9)
            for code,label in sorted(legend.items()):classes.append(dict(year=year,class_id=code,class_name=label,window_pixel_count=int((a==code).sum()),clipped_footprint_area_ha=float(fine_area[a==code].sum())))
            outputs[f'forest_plus_savanna_{year}']=outputs[f'forest_formations_{year}']+outputs[f'savanna_{year}'];outputs[f'forest_plus_plantation_{year}']=outputs[f'forest_formations_{year}']+outputs[f'plantation_{year}'];checks.append(dict(year=year,weight_partition_max_error=error,group_partition_max_error=float(np.max(np.abs(total-1))),maximum_area_closure_error_ha=max_area_error))
        r=dict(year=year,url=url,etag=rr.etag,whole_object_size=rr.size,whole_object_downloaded=False,source_grid=g,fine_window=window,source_subset_shape=list(a.shape),decoded_subset_sha256=h(a.tobytes()),native_CCI_rows=cfg['rows'],native_CCI_columns=cfg['columns'],distinct_source_bytes=rr.transferred,tiles_decoded=tiles,ranges=rr.receipts());receipts.append(r);print('Aligned bounded land cover',year,'fine shape',a.shape,'range bytes',rr.transferred,flush=True);rr.close()
    require(grids[0]==grids[1])
    outputs.update(cell_area_ha=areas,longitude_centres=(xe[:-1]+xe[1:])/2,latitude_centres=(ye[:-1]+ye[1:])/2)
    # Numeric support descriptors, not a persistent-forest-only inference sample.
    f0=outputs['forest_formations_2015'];f1=outputs['forest_formations_2023'];u0=outputs['unobserved_2015'];u1=outputs['unobserved_2023'];tol=1e-9
    joint=dict(footprint_area_ha=float(footprint),native_cells=65536,complete_mapped_both_cells=int(((u0<tol)&(u1<tol)).sum()),forest_presence_union_cells=int(((f0>tol)|(f1>tol)).sum()),forest_presence_both_cells=int(((f0>tol)&(f1>tol)).sum()),mapped_pure_forest_both_cells=int(((f0>1-tol)&(f1>1-tol)).sum()),mixed_formation_cells_2015=int(((f0>tol)&(f0<1-tol)).sum()),mixed_formation_cells_2023=int(((f1>tol)&(f1<1-tol)).sum()),threshold_role='Numerical zero/one tolerance only, not ecological or detection threshold',persistent_only_selection_used=False,national_forest_sample_finalized=False,biomass_stock_or_change_estimated=False,local_mapped_cover_endpoints_inspected=True)
    np.savez_compressed(ROOT/'data/brazil/BRA_F05_support_fractions.npz',**outputs);savecsv(ROOT/'data/brazil/endpoint_support_areas.csv',summaries);savecsv(ROOT/'data/brazil/source_class_areas.csv',classes)
    (ROOT/'metadata/brazil/alignment_checks.json').write_text(json.dumps(checks,indent=2)+'\n');(ROOT/'metadata/brazil/range_provenance.json').write_text(json.dumps(dict(endpoints=receipts,freeze=freeze,CCI_affine=transforms[0]),indent=2)+'\n');(ROOT/'data/brazil/common_support_summary.json').write_text(json.dumps(joint,indent=2)+'\n');return summaries,joint

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cache',type=Path,required=True);run(p.parse_args().cache)

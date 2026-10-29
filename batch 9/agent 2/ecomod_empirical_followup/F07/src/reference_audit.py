"""Bounded artifact/schema/reference-coverage audit; no map/reference accuracy test."""
from pathlib import Path,PurePosixPath
import argparse,csv,io,json,hashlib,zipfile,re,math,collections
import requests
import shapefile
ROOT=Path(__file__).resolve().parents[1]
CAP=25_000_000

def require(condition,message):
    if not condition:raise ValueError(message)
def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb')as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()
def number(value):
    if value is None:return None
    t=str(value).strip().replace(',','.')
    try:v=float(t)
    except ValueError:return None
    return v if math.isfinite(v)else None

def code(value):
    v=number(value)
    return int(v)if v is not None and v.is_integer()else None

def safe_members(z):
    infos=z.infolist();require(bool(infos),'Empty archive')
    require(all(not PurePosixPath(i.filename).is_absolute()and '..'not in PurePosixPath(i.filename).parts and not i.flag_bits&1 for i in infos),'Unsafe/encrypted archive member')
    require(all(i.file_size<=250_000_000 for i in infos)and sum(i.file_size for i in infos)<=500_000_000,'Decompression cap exceeded')
    require(len({i.filename for i in infos})==len(infos),'Duplicate member name')
    return infos

def acquire(meta,path,offline=False):
    if path.exists():require(sha(path)==meta['sha256'],'Archive cache hash drift');return
    require(not offline,'Missing archive in offline mode');require(meta['bytes']<=CAP,'Archive exceeds download cap')
    r=requests.get(meta['url'],headers={'If-Match':meta['etag'],'Accept-Encoding':'identity'},stream=True,timeout=(20,60))
    try:
        require(r.status_code==200,'Archive request failed');require(r.headers.get('ETag')==meta['etag'],'Archive ETag drift');b=bytearray()
        for block in r.iter_content(65536):
            b.extend(block);require(len(b)<=min(CAP,meta['bytes']),'Archive response cap exceeded')
        require(len(b)==meta['bytes']and hashlib.sha256(b).hexdigest()==meta['sha256'],'Archive length/hash drift');path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(b)
    finally:r.close()

def bounds():
    d=json.loads((ROOT/'metadata/brazil/range_provenance.json').read_text());t=d['CCI_affine'];r0,r1=d['endpoints'][0]['native_CCI_rows'];c0,c1=d['endpoints'][0]['native_CCI_columns']
    return [t[0]+c0*t[1],t[0]+(c1+1)*t[1],t[3]+(r1+1)*t[5],t[3]+r0*t[5]]
def inside(x,y,b):return b[0]<=x<b[1]and b[2]<=y<b[3]

class Profile:
    def __init__(self,fields):
        self.fields=fields;self.years=sorted(int(m.group(1))for x in fields if(m:=re.fullmatch(r'CLASS_(\d{4})',x)));self.n=0;self.ids=set();self.labels={y:collections.Counter()for y in [2015,2023]};self.local_nonblank=collections.Counter();self.codes={y:collections.Counter()for y in [2015,2023]};self.flags={x:collections.Counter()for x in ['AMOSTRAS','AMOSTRA_AM']if x in fields};self.weights={x:[]for x in ['PROB_AMOS_','PROB_AMOS','PESO_AMOS']if x in fields};self.coord=0;self.local=0;self.b=bounds()
    def add(self,row,xy):
        self.n+=1;require(self.n<=100_000,'Unexpected reference population size');ident=code(row['TARGETID']);require(ident is not None and ident not in self.ids,'Missing/duplicate point ID');self.ids.add(ident)
        if xy and all(v is not None for v in xy):
            x,y=xy;require(-180<=x<=180 and -90<=y<=90,'Invalid geographic coordinate');self.coord+=1;self.local+=int(inside(x,y,self.b))
        for y in self.codes:
            field=f'CLASS_{y}'
            if field in self.fields:
                token='' if row[field] is None else str(row[field]).strip();self.labels[y][token]+=1
                value=code(row[field])
                if value is not None:self.codes[y][value]+=1
                if xy and all(v is not None for v in xy)and inside(*xy,self.b)and token:self.local_nonblank[y]+=1
        for field in self.flags:self.flags[field][str(row[field])]+=1
        for field in self.weights:self.weights[field].append(number(row[field]))
        return ident
    def summary(self):
        return {'records':self.n,'unique_TARGETID':len(self.ids),'fields':self.fields,'class_years':self.years,'numeric_endpoint_code_counts_not_area_or_accuracy':{str(y):{str(k):v for k,v in sorted(c.items(),key=lambda x:str(x[0]))}for y,c in self.codes.items()},'raw_endpoint_label_counts_not_area_or_accuracy':{str(y):dict(sorted(v.items()))for y,v in self.labels.items()},'endpoint_nonblank_records':{str(y):sum(n for label,n in v.items()if label)for y,v in self.labels.items()},'local_endpoint_nonblank_records':{str(y):self.local_nonblank[y]for y in self.labels},'endpoint_fields_present':{str(y):f'CLASS_{y}'in self.fields for y in self.codes},'endpoint_nonblank_numeric_code_records':{str(y):sum(v for k,v in c.items()if k is not None)for y,c in self.codes.items()},'explicit_role_field_values':{k:dict(sorted(v.items()))for k,v in self.flags.items()},'weight_field_profiles':{k:{'nonfinite_or_unparseable':sum(x is None for x in v),'nonpositive':sum(x is not None and x<=0 for x in v),'exactly_one':sum(x==1 for x in v),'min':min(x for x in v if x is not None),'max':max(x for x in v if x is not None)}for k,v in self.weights.items()},'complete_coordinate_records':self.coord,'points_in_unchanged_local_footprint':self.local,'coordinate_rule':'CSV LON/LAT as labelled; vector uses POINT geometry in source WGS84 PRJ, not mislabeled attributes'}

def run(cache,offline=False):
    frozen=json.loads((ROOT/'metadata/reference/audit_freeze_F06.json').read_text());require(sha(ROOT/'protocol/REFERENCE_AUDIT_F06.md')==frozen['protocol_sha256'],'Frozen reference protocol drift')
    registry=json.loads((ROOT/'metadata/reference/archive_registry_F06.json').read_text());source_checks={}
    for key,m in registry.items():
        head=frozen['heads'][key];h=requests.structures.CaseInsensitiveDict(head['headers']);require(m['url']==head['url']and m['etag']==h['ETag']and m['bytes']==int(h['Content-Length']),'Frozen archive identity drift');path=cache/(key+'.zip');acquire(m,path,offline)
        with zipfile.ZipFile(path)as z:
            records=[]
            for info in safe_members(z):
                h=hashlib.sha256()
                with z.open(info)as f:
                    for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
                records.append({'member':info.filename,'bytes':info.file_size,'sha256':h.hexdigest()})
            source_checks[key]={'archive_sha256':sha(path),'members':records}
    saved={}
    with zipfile.ZipFile(cache/'csv_zip.zip')as z:
        files=[x.filename for x in safe_members(z)if x.filename.lower().endswith('.csv')];require(len(files)==1,'Unexpected CSV archive schema')
        with z.open(files[0])as raw:
            reader=csv.DictReader(io.TextIOWrapper(raw,encoding='utf-8-sig'));cp=Profile(reader.fieldnames)
            for row in reader:
                x=number(row['LON']);y=number(row['LAT']);ident=cp.add(row,(x,y));saved[ident]=(x,y,code(row['CLASS_2015']),code(row.get('COUNT_2015')),code(row.get('BORDA_2015')))
    compared=collections.Counter();max_direct=0.;max_swapped=0.;max_csv_geometry=0.
    with zipfile.ZipFile(cache/'vector_zip.zip')as z:
        names=z.namelist();base=next(n[:-4]for n in names if n.endswith('.shp'));prj=z.read(base+'.prj').decode('ascii');require('GCS_WGS_1984'in prj,'Unexpected vector CRS')
        with z.open(base+'.dbf')as dbf:
            reader=shapefile.Reader(shp=io.BytesIO(z.read(base+'.shp')),shx=io.BytesIO(z.read(base+'.shx')),dbf=dbf,encoding='utf-8');vp=Profile([f[0]for f in reader.fields[1:]])
            for record in reader.iterShapeRecords():
                require(record.shape.shapeType==1 and len(record.shape.points)==1,'Reference geometry is not POINT');row=record.record.as_dict();x,y=record.shape.points[0];ident=vp.add(row,(x,y));a=number(row['LON']);b=number(row['LAT'])
                if a is not None and b is not None:
                    direct=max(abs(a-x),abs(b-y));swapped=max(abs(a-y),abs(b-x));max_direct=max(max_direct,direct);max_swapped=max(max_swapped,swapped);compared['attribute_LON_LAT_match_geometry_within_1e-8_deg']+=int(direct<=1e-8);compared['attribute_LAT_LON_match_geometry_within_1e-8_deg']+=int(swapped<=1e-8)
                if ident in saved:
                    compared['common_ids']+=1;cx,cy,c,co,bo=saved[ident];distance=max(abs(cx-x),abs(cy-y));max_csv_geometry=max(max_csv_geometry,distance);compared['csv_coordinates_match_vector_geometry_within_1e-8_deg']+=int(distance<=1e-8)
                    compared['same_2015_COUNT']+=int(co is not None and co==code(row['COUNT_2015']));compared['same_2015_BORDA']+=int(bo is not None and bo==code(row['BORDA_2015']))
            reader.close()
    result={'revision':'F06','scope':'Reference artifact/schema/coverage audit, not validation of mapped classes or change','frozen_local_bounds_west_east_south_north':bounds(),'csv_zip':cp.summary(),'vector_zip':vp.summary(),'cross_artifact_comparison_not_map_accuracy':dict(compared),'2015_reference_class_comparison':'Not performed: CSV textual labels and vector numeric codes require a verified source-specific crosswalk','coordinate_checks':{'max_direct_vector_attribute_geometry_error_deg':max_direct,'max_swapped_vector_attribute_geometry_error_deg':max_swapped,'max_csv_coordinate_geometry_error_deg':max_csv_geometry},'source_PRJ':prj,'source_page_collection_label':9,'Collection11_identity_and_reference_independence_certified':False,'local_map_reference_confusion_computed':False,'transition_accuracy_or_uncertainty_calibrated':False,'national_physical_admission_changed':False}
    out=ROOT/'data/reference';out.mkdir(exist_ok=True);(out/'reference_audit_F06.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n');(ROOT/'metadata/reference/verified_source_members_F06.json').write_text(json.dumps(source_checks,indent=2)+'\n');print(json.dumps({k:{x:result[k][x]for x in ['records','class_years','points_in_unchanged_local_footprint','explicit_role_field_values']}for k in ['csv_zip','vector_zip']},indent=2,ensure_ascii=False));print('Cross-artifact checks:',dict(compared));return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cache',type=Path,required=True);p.add_argument('--offline',action='store_true');a=p.parse_args();run(a.cache,a.offline)

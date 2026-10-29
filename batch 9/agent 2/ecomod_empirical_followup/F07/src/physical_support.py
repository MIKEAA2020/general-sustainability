"""Territorial/grid support preflight, not forest masks or national stock estimates.
Decode pinned full-resolution TopoJSON (not the simplified download), repair
invalid polygon topology explicitly, and intersect with the documented native
product domain. The 1-degree index is for planning, never a biomass estimator.
"""
from pathlib import Path
import json,gzip,math,csv,hashlib
import numpy as np
from shapely import make_valid,segmentize,clip_by_rect
from shapely.prepared import prep
from shapely.geometry import shape,box,Polygon,MultiPolygon,GeometryCollection
from shapely.geometry.polygon import orient
from shapely.ops import unary_union
from pyproj import Geod
from estimands import wgs84_rectangle_area_ha
ROOT=Path(__file__).resolve().parents[1];GEOD=Geod(ellps='WGS84')

def decode_topology(t):
    transform=t.get('transform');arcs=[]
    for arc in t['arcs']:
        if transform:
            points=np.cumsum(np.asarray(arc,dtype=float),axis=0)*transform['scale']+transform['translate']
        else:points=np.asarray(arc,dtype=float)
        arcs.append(points)
    def ring(ids):
        chunks=[]
        for j,i in enumerate(ids):
            a=arcs[i] if i>=0 else arcs[~i][::-1]
            chunks.append(a if j==0 else a[1:])
        out=np.concatenate(chunks)
        if not np.array_equal(out[0],out[-1]):out=np.vstack([out,out[0]])
        return out
    def geom(o):
        ty=o['type']
        if ty=='GeometryCollection':return GeometryCollection([geom(x)for x in o['geometries']])
        if ty=='Polygon':return Polygon(ring(o['arcs'][0]),[ring(r)for r in o['arcs'][1:]])
        if ty=='MultiPolygon':return MultiPolygon([Polygon(ring(p[0]),[ring(r)for r in p[1:]])for p in o['arcs']])
        raise ValueError('Unsupported boundary geometry '+ty)
    gs=[geom(o)for o in t['objects'].values()]
    # Do not union invalid geometry before its repair.
    return gs[0] if len(gs)==1 else unary_union([make_valid(g)for g in gs])

def polygon_parts(g):
    if isinstance(g,Polygon):return [g]
    if hasattr(g,'geoms'):return [p for x in g.geoms for p in polygon_parts(x)]
    return []

def area_ha(g):
    # Segmentization follows lon/lat linework and approximates clipped parallels;
    # it does not increase ecological resolution or boundary accuracy.
    return sum(abs(GEOD.geometry_area_perimeter(orient(segmentize(p,.02),sign=1))[0])for p in polygon_parts(g))/1e4

def load_boundary(code):
    b=gzip.decompress((ROOT/f'data/geography/{code}_ADM0.topojson.gz').read_bytes())
    r=json.loads((ROOT/'metadata/physical_source_registry.json').read_text())['boundaries'][code]
    assert hashlib.sha256(b).hexdigest()==r['sha256']
    g=decode_topology(json.loads(b));valid=g.is_valid
    if not valid:g=unary_union(polygon_parts(make_valid(g,method='structure',keep_collapsed=False)))
    if g.is_empty:raise ValueError('Empty country polygon')
    return g,valid

def write_csv(path,rows):
    with path.open('w',newline='')as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def run():
    cfg=json.loads((ROOT/'configs/study_design.json').read_text());registry=json.loads((ROOT/'metadata/physical_source_registry.json').read_text());domain=box(-180,-60,180,80);rows=[];cells=[];plans=[]
    for code in cfg['pilot_candidates_iso3']:
        g,valid=load_boundary(code);supported=g.intersection(domain);a=area_ha(g);s=area_ha(supported);outside=area_ha(g.difference(domain));assert abs(a-s-outside)/a<2e-5
        meta=registry['boundaries'][code]
        # Largest polygon representative point: fixed geometry-only choice,
        # not selected using forest cover, biomass values or outcome signs.
        p=max(polygon_parts(supported),key=lambda x:x.area).representative_point();lon,lat=p.x,p.y
        step=360/405000;ix=int((lon+180)/step);iy=int((80-lat)/step);n=256
        x0=max(0,min(ix-n//2,405000-n));y0=max(0,min(iy-n//2,157500-n))
        plans.append(dict(ISO3=code,selection='largest_polygon_representative_point',longitude=lon,latitude=lat,rows=[y0,y0+n-1],columns=[x0,x0+n-1],shape=[n,n],outcome_based_selection=False,forest_targeted=False))
        rows.append(dict(ISO3=code,boundary_id=meta['boundaryID'],boundary_year=meta['boundaryYearRepresented'],west=g.bounds[0],south=g.bounds[1],east=g.bounds[2],north=g.bounds[3],polygon_area_ha=a,native_domain_polygon_area_ha=s,outside_native_domain_polygon_area_ha=outside,outside_native_domain_pct=100*outside/a,source_geometry_valid=valid,topology_repaired=not valid,territory_compatibility='unverified',forest_support='not_frozen',national_valid_pixel_coverage='not_estimated',physical_sample_status='hold_not_admitted',reason_codes='territory_confirmation;endpoint_forest_support;full_coverage;change_validation'))
        w,south,e,north=supported.bounds;prepared=prep(supported)
        for y in range(math.floor(south),math.ceil(north)):
            for x in range(math.floor(w),math.ceil(e)):
                cell=box(x,y,x+1,y+1)
                if not prepared.intersects(cell):continue
                full=wgs84_rectangle_area_ha(x,x+1,y,y+1)
                if prepared.contains(cell):ac=full
                else:
                    clip=clip_by_rect(supported,x,y,x+1,y+1)
                    if not clip.is_valid:clip=make_valid(clip)
                    if clip.is_empty or clip.area==0:continue
                    ac=area_ha(clip)
                if ac>0:cells.append(dict(ISO3=code,west=x,south=y,east=x+1,north=y+1,polygon_intersection_ha=ac,cell_area_ha=full,polygon_fraction=min(1,ac/full),role='geographic_planning_not_forest_or_biomass_mask'))
        print(code,'polygon area ha',round(a),'outside native domain %',round(100*outside/a,5),flush=True)
    write_csv(ROOT/'data/support/country_domain_support.csv',rows);write_csv(ROOT/'data/support/geographic_planning_grid.csv',cells)
    # Freeze this plan before retrieving any pixel payloads. Never reselect a
    # point on the basis of valid coverage or observed biomass.
    out=ROOT/'configs/native_probe_plan_F04.json';content=json.dumps(dict(grid_shape=[157500,405000],domain=[-180,-60,180,80],years=[2015,2023],maximum_response_bytes=25000000,role='bounded native access/coverage probes, not a national probability sample',plans=plans),indent=2)+'\n'
    if out.exists():assert out.read_text()==content,'Refuse to alter frozen probe plan'
    else:out.write_text(content)
    return rows,cells
if __name__=='__main__':run()

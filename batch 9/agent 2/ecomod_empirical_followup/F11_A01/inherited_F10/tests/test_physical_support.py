import unittest,sys,json,gzip,hashlib,csv
from pathlib import Path
import numpy as np
from shapely.geometry import box
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from physical_support import decode_topology,area_ha,ROOT
from native_coverage_probes import parse_ascii
from estimands import wgs84_rectangle_area_ha

class GeometryTests(unittest.TestCase):
    def test_transformed_topology(self):
        t={'type':'Topology','transform':{'scale':[.5,.25],'translate':[-1,2]},'arcs':[[[0,0],[2,0],[0,4],[-2,0],[0,-4]]],'objects':{'test':{'type':'Polygon','arcs':[[0]]}}}
        g=decode_topology(t);self.assertEqual(g.bounds,(-1,2,0,3));self.assertAlmostEqual(g.area,1)
    def test_reversed_arcs(self):
        t={'arcs':[[[0,0],[1,0]],[[1,0],[1,1]],[[0,1],[1,1]],[[0,0],[0,1]]],'objects':{'p':{'type':'Polygon','arcs':[[0,1,-3,-4]]}}}
        self.assertAlmostEqual(decode_topology(t).area,1)
    def test_hole_preserved(self):
        t={'arcs':[[[0,0],[2,0],[2,2],[0,2],[0,0]],[[.5,.5],[1.5,.5],[1.5,1.5],[.5,1.5],[.5,.5]]],'objects':{'p':{'type':'Polygon','arcs':[[0],[1]]}}}
        g=decode_topology(t);self.assertAlmostEqual(g.area,3);self.assertEqual(len(g.interiors),1)
    def test_ellipsoid_area_consistent_with_rectangle(self):
        for south in [-45,0,60,79]:
            expected=wgs84_rectangle_area_ha(10,11,south,south+1)
            self.assertLess(abs(area_ha(box(10,south,11,south+1))-expected)/expected,1e-7)
    def test_native_domain_clipping(self):
        g=box(0,79,1,81);d=box(-180,-60,180,80);self.assertGreater(area_ha(g.difference(d)),0)
        self.assertLess(abs(area_ha(g)-area_ha(g.intersection(d))-area_ha(g.difference(d)))/area_ha(g),1e-7)

class PayloadTests(unittest.TestCase):
    def fixture(self,dotted=False):
        a='agb.agb'if dotted else'agb';b='agb_sd.agb_sd'if dotted else'agb_sd'
        return 'Dataset {}\n---------------------------------------------\n'+a+'[1][2][2]\n[0][0], -32768, 0\n[0][1], 12, 10001\n\n'+b+'[1][2][2]\n[0][0], -32768, 0\n[0][1], 2, 1\n'
    def test_parse_fill_zero_valid_invalid(self):
        x=parse_ascii(self.fixture(),[2,2]);a=x['agb'];self.assertEqual(int((a==-32768).sum()),1);self.assertEqual(int((a==0).sum()),1);self.assertEqual(int(((a>=0)&(a<=10000)).sum()),2)
    def test_dotted_dap_names(self):self.assertEqual(parse_ascii(self.fixture(True),[2,2])['agb'][1,0],12)
    def test_shape_mismatch_fails_closed(self):
        with self.assertRaises(ValueError):parse_ascii(self.fixture(),[3,3])
    def test_missing_array_fails_closed(self):
        with self.assertRaises(ValueError):parse_ascii('Dataset {}\n---------------------------------------------\nagb[1][1][1]\n[0][0], 0\n',[1,1])

class FrozenSupportTests(unittest.TestCase):
    def test_boundary_hashes(self):
        r=json.loads((ROOT/'metadata/physical_source_registry.json').read_text())
        for c,v in r['boundaries'].items():
            b=gzip.decompress((ROOT/f'data/geography/{c}_ADM0.topojson.gz').read_bytes());self.assertEqual(len(b),v['bytes']);self.assertEqual(hashlib.sha256(b).hexdigest(),v['sha256']);self.assertEqual(len(v['commit']),40)
    def test_plan_bounds_and_no_reselection(self):
        p=json.loads((ROOT/'configs/native_probe_plan_F04.json').read_text());self.assertEqual(p['years'],[2015,2023]);self.assertEqual(len(p['plans']),8)
        for x in p['plans']:
            self.assertEqual(x['shape'],[256,256]);self.assertFalse(x['outcome_based_selection']);self.assertFalse(x['forest_targeted']);self.assertGreaterEqual(x['rows'][0],0);self.assertLess(x['rows'][1],157500);self.assertLess(x['columns'][1],405000)
    def test_domain_report_not_eligibility(self):
        rows=list(csv.DictReader((ROOT/'data/support/country_domain_support.csv').open()));self.assertEqual(len(rows),8)
        for x in rows:self.assertEqual(x['physical_sample_status'],'hold_not_admitted');self.assertEqual(x['national_valid_pixel_coverage'],'not_estimated')
        canada=next(x for x in rows if x['ISO3']=='CAN');self.assertGreater(float(canada['outside_native_domain_pct']),0)
    def test_geographic_partition_closure(self):
        rows=list(csv.DictReader((ROOT/'data/support/country_domain_support.csv').open()));cells=list(csv.DictReader((ROOT/'data/support/geographic_planning_grid.csv').open()))
        for r in rows:
            a=float(r['native_domain_polygon_area_ha']);total=sum(float(x['polygon_intersection_ha'])for x in cells if x['ISO3']==r['ISO3']);self.assertLess(abs(total-a)/a,2e-5)
    def test_catalogue_endpoint_gap(self):
        f=json.loads((ROOT/'metadata/geography/CDS_land_cover_form.json').read_text());years=next(x['details']['values']for x in f if x['name']=='year');self.assertIn('2015',years);self.assertNotIn('2023',years)

if __name__=='__main__':unittest.main()

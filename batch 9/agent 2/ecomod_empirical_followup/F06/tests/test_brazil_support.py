import sys,unittest,tempfile,json,io
from pathlib import Path
from unittest.mock import Mock
import numpy as np
import tifffile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from bounded_tiff import RangeReader
from brazil_support import overlap_weights,read_window,ROOT

class OverlapTests(unittest.TestCase):
    def test_identity(self):np.testing.assert_allclose(overlap_weights([0,1,2],[0,1,2]).toarray(),np.eye(2))
    def test_noninteger_alignment(self):
        x=overlap_weights([0,.9,1.8],[-.1,.2,.5,.8,1.1,1.4,1.7,2]).toarray();np.testing.assert_allclose(x.sum(axis=1),1,atol=1e-12);self.assertGreater(np.count_nonzero(x[0]),2)
    def test_missing_support_not_renormalized(self):
        x=overlap_weights([0,1],[.5,1]).toarray();self.assertAlmostEqual(x.sum(),.5)
    def test_latitude_weights_conserve(self):
        w=overlap_weights([60,60.1,60.2],[59.99,60.03,60.07,60.11,60.15,60.19,60.23],latitude=True).toarray();np.testing.assert_allclose(w.sum(axis=1),1,atol=1e-12)
    def test_nonascending_rejected(self):
        with self.assertRaises(ValueError):overlap_weights([1,0],[0,1])
    def test_class_partition_conserved(self):
        wx=overlap_weights([0,.5,1],[-.1,.2,.6,1.1]);wy=overlap_weights([10,10.5,11],[9.9,10.2,10.6,11.1],latitude=True);a=np.array([[1,0,0],[0,1,0],[0,0,1]],float);f=np.asarray((wx@(wy@a).T).T);g=np.asarray((wx@(wy@(1-a)).T).T);np.testing.assert_allclose(f+g,1,atol=1e-12)

class TiffTests(unittest.TestCase):
    def test_bounded_tile_decode_equals_slice(self):
        a=np.arange(32*32,dtype=np.uint16).reshape(32,32);b=io.BytesIO();tifffile.imwrite(b,a,tile=(16,16),compression='lzw');b.seek(0)
        with tifffile.TiffFile(b)as tf:r,tiles=read_window(b,tf.pages[0],[3,29,7,25]);np.testing.assert_array_equal(r,a[3:29,7:25]);self.assertEqual(len(tiles),4)

class ReaderTests(unittest.TestCase):
    def reader(self,p,cap=100):return RangeReader('https://example.test/pinned',10,'"fixed"',p,cap=cap,block_size=4)
    def response(self,status=206,content_range='bytes 0-3/10',etag='"fixed"'):
        r=Mock();r.status_code=status;r.headers={'Content-Range':content_range,'ETag':etag};r.iter_content.return_value=[b'abcd'];return r
    def test_range_ignored_rejected_before_body(self):
        with tempfile.TemporaryDirectory()as p:
            rr=self.reader(p);r=self.response(status=200);rr.session.get=Mock(return_value=r)
            with self.assertRaises(ValueError):rr.read(2)
            r.iter_content.assert_not_called();rr.close()
    def test_wrong_etag_rejected(self):
        with tempfile.TemporaryDirectory()as p:
            rr=self.reader(p);r=self.response(etag='"changed"');rr.session.get=Mock(return_value=r)
            with self.assertRaises(ValueError):rr.read(2)
            r.iter_content.assert_not_called();rr.close()
    def test_cap_checked_before_request(self):
        with tempfile.TemporaryDirectory()as p:
            rr=self.reader(p,cap=3);rr.session.get=Mock()
            with self.assertRaises(ValueError):rr.read(2)
            rr.session.get.assert_not_called();rr.close()
    def test_cached_block_corruption_fails(self):
        with tempfile.TemporaryDirectory()as p:
            rr=self.reader(p);rr.session.get=Mock(return_value=self.response());self.assertEqual(rr.read(2),b'ab');rr.close();Path(p,'000000000000_000000000003.bin').write_bytes(b'bad!');rr=self.reader(p)
            with self.assertRaises(ValueError):rr.read(2)
            rr.close()
    def test_wrong_content_range_rejected_before_body(self):
        with tempfile.TemporaryDirectory()as p:
            rr=self.reader(p);r=self.response(content_range='bytes 1-4/10');rr.session.get=Mock(return_value=r)
            with self.assertRaises(ValueError):rr.read(2)
            r.iter_content.assert_not_called();rr.close()
    def test_truncated_body_rejected(self):
        with tempfile.TemporaryDirectory()as p:
            rr=self.reader(p);r=self.response();r.iter_content.return_value=[b'abc'];rr.session.get=Mock(return_value=r)
            with self.assertRaises(ValueError):rr.read(2)
            rr.close()
    def test_oversized_body_rejected(self):
        with tempfile.TemporaryDirectory()as p:
            rr=self.reader(p);r=self.response();r.iter_content.return_value=[b'abcde'];rr.session.get=Mock(return_value=r)
            with self.assertRaises(ValueError):rr.read(2)
            rr.close()
    def test_missing_cache_hash_rejected_without_request(self):
        with tempfile.TemporaryDirectory()as p:
            Path(p,'000000000000_000000000003.bin').write_bytes(b'abcd');rr=self.reader(p);rr.session.get=Mock()
            with self.assertRaises(ValueError):rr.read(2)
            rr.session.get.assert_not_called();rr.close()
    def test_cache_identity_rejected_without_request(self):
        with tempfile.TemporaryDirectory()as p:
            rr=self.reader(p);rr.session.get=Mock(return_value=self.response());rr.read(2);rr.close();m=Path(p,'000000000000_000000000003.json');v=json.loads(m.read_text());v['url']='https://example.test/changed';m.write_text(json.dumps(v));rr=self.reader(p);rr.session.get=Mock()
            with self.assertRaises(ValueError):rr.read(2)
            rr.session.get.assert_not_called();rr.close()
    def test_cache_access_counts_against_cap(self):
        with tempfile.TemporaryDirectory()as p:
            rr=self.reader(p);rr.session.get=Mock(return_value=self.response());rr.read(2);rr.close();rr=self.reader(p,cap=3);rr.session.get=Mock()
            with self.assertRaises(ValueError):rr.read(2)
            rr.session.get.assert_not_called();rr.close()
    def test_unbounded_read_rejected(self):
        with tempfile.TemporaryDirectory()as p:
            rr=self.reader(p,cap=5)
            with self.assertRaises(ValueError):rr.read()
            rr.close()

class FrozenBrazilTests(unittest.TestCase):
    def test_current_legend_and_group_separation(self):
        c=json.loads((ROOT/'configs/brazil_support_F05.json').read_text());g=c['classification_groups'];self.assertEqual(g['forest_formations'],[3,5,6,49]);self.assertEqual(g['savanna'],[4,7]);self.assertEqual(g['plantation'],[9]);self.assertEqual(sum(map(len,g.values())),len(set(v for xs in g.values()for v in xs)))
    def test_fraction_partition_and_area(self):
        d=np.load(ROOT/'data/brazil/BRA_F05_support_fractions.npz');area=d['cell_area_ha'];self.assertEqual(area.shape,(256,256))
        for year in [2015,2023]:
            total=sum(d[f'{g}_{year}']for g in ['forest_formations','savanna','plantation','open_water','unobserved','other_mapped']);np.testing.assert_allclose(total,1,atol=1e-9)
    def test_no_national_admission_or_biomass_inference(self):
        c=json.loads((ROOT/'data/brazil/common_support_summary.json').read_text());self.assertFalse(c['national_forest_sample_finalized']);self.assertFalse(c['biomass_stock_or_change_estimated']);self.assertFalse(c['persistent_only_selection_used']);self.assertTrue(c['local_mapped_cover_endpoints_inspected'])

if __name__=='__main__':unittest.main()

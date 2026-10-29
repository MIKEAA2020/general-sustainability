import unittest,sys,json,csv,tempfile,zipfile,io
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from reference_audit import number,code,inside,Profile,safe_members,acquire,ROOT
from plot_account_coverage import availability_counts

class AuditTests(unittest.TestCase):
    def test_decimal_comma(self):self.assertAlmostEqual(number('6,139945317647E-06'),6.139945317647e-6)
    def test_missing_and_nonfinite_not_zero(self):
        for x in ['',None,'NA','NaN','inf']:self.assertIsNone(number(x))
        self.assertEqual(number('0'),0)
    def test_text_class_not_forced_to_code(self):self.assertIsNone(code('FORMAÇÃO FLORESTAL'));self.assertEqual(code('3.0'),3)
    def test_half_open_membership(self):self.assertTrue(inside(0,0,[0,1,0,1]));self.assertFalse(inside(1,.5,[0,1,0,1]))
    def test_empty_endpoint_not_zero_or_negative_class(self):
        p=Profile(['TARGETID','LON','LAT','CLASS_2015','CLASS_2023']);p.add({'TARGETID':1,'CLASS_2015':'FORMAÇÃO FLORESTAL','CLASS_2023':''},(-49.7,-14.2));s=p.summary();self.assertEqual(s['endpoint_nonblank_records'],{'2015':1,'2023':0});self.assertEqual(s['endpoint_nonblank_numeric_code_records']['2015'],0)
    def test_absent_year_distinguished_from_blank_field(self):
        p=Profile(['TARGETID','CLASS_2015']);p.add({'TARGETID':1,'CLASS_2015':3},(-49.7,-14.2));self.assertFalse(p.summary()['endpoint_fields_present']['2023'])
    def test_duplicate_ids_fail_closed(self):
        p=Profile(['TARGETID']);p.add({'TARGETID':1},(0,0))
        with self.assertRaises(ValueError):p.add({'TARGETID':1},(0,0))
    def test_archive_traversal_rejected(self):
        b=io.BytesIO()
        with zipfile.ZipFile(b,'w')as z:z.writestr('../bad.csv','x')
        with zipfile.ZipFile(b)as z:
            with self.assertRaises(ValueError):safe_members(z)
    def test_archive_decompression_size_guard(self):
        info=zipfile.ZipInfo('a.dbf');info.file_size=250_000_001
        class Z:
            def infolist(self):return [info]
        with self.assertRaises(ValueError):safe_members(Z())
    def test_offline_cache_missing_fails_without_request(self):
        with tempfile.TemporaryDirectory()as d,patch('requests.get')as req:
            with self.assertRaises(ValueError):acquire({'sha256':'x'},Path(d)/'none.zip',offline=True)
            req.assert_not_called()
    def test_cached_archive_drift_fails_without_request(self):
        with tempfile.TemporaryDirectory()as d,patch('requests.get')as req:
            p=Path(d)/'bad.zip';p.write_bytes(b'bad')
            with self.assertRaises(ValueError):acquire({'sha256':'x'},p,offline=True)
            req.assert_not_called()
    def test_current_artifacts_not_eligible_local_validation(self):
        d=json.loads((ROOT/'data/reference/reference_audit_F06.json').read_text());self.assertEqual(d['csv_zip']['records'],85152);self.assertEqual(d['csv_zip']['endpoint_nonblank_records']['2023'],4053);self.assertFalse(d['vector_zip']['endpoint_fields_present']['2023']);self.assertEqual(d['csv_zip']['local_endpoint_nonblank_records']['2023'],0);self.assertFalse(d['local_map_reference_confusion_computed'])
    def test_geometry_not_reversed_attribute_used(self):
        d=json.loads((ROOT/'data/reference/reference_audit_F06.json').read_text());c=d['cross_artifact_comparison_not_map_accuracy'];self.assertEqual(c['attribute_LAT_LON_match_geometry_within_1e-8_deg'],85152);self.assertEqual(c['attribute_LON_LAT_match_geometry_within_1e-8_deg'],0)
    def test_count_kernel_keeps_183_53(self):
        with (ROOT/'data/derived/account_availability.csv').open()as f:c=availability_counts(list(csv.DictReader(f)))
        self.assertEqual(sum(v for (r,k),v in c.items()if k=='pass'),183);self.assertEqual(sum(v for (r,k),v in c.items()if k=='fail'),53)
    def test_invalid_account_flag_rejected(self):
        with self.assertRaises(ValueError):availability_counts([{'account_available':'unknown','UN_region':'Europe'}])
    def test_corrected_figure_region_boxes_disjoint(self):
        d=json.loads((ROOT/'results/account_coverage_F06_checks.json').read_text());self.assertTrue(d['region_label_boxes_disjoint']);self.assertEqual(d['totals'],{'available':183,'unavailable':53})

if __name__=='__main__':unittest.main()

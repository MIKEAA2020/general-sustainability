"""Offline safety, arithmetic and evidence-gate tests; not ecological validation."""
from pathlib import Path
import csv, hashlib, json, sys, tempfile, unittest
from unittest.mock import patch
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from native_uncertainty_R03 import parse_ascii, summarize, acquire
from reference_ranges_R03 import ReferenceRanges


def load(name): return json.loads((ROOT/name).read_text())
def sample(): return 'Dataset metadata\n---------------------------------------------\nagb[1][2][2]\n[0][0], 0, 1\n[0][1], 3, -32768\nagb_sd[1][2][2]\n[0][0], 0, 0\n[0][1], 2, -32768\n'

class NativeTests(unittest.TestCase):
    def test_parse_exact_shape_and_values(self):
        a=parse_ascii(sample(),(2,2));self.assertEqual(a['agb'].tolist(),[[0,1],[3,-32768]])
    def test_missing_separator(self):
        with self.assertRaises(ValueError):parse_ascii('x',(2,2))
    def test_duplicate_separator(self):
        with self.assertRaises(ValueError):parse_ascii(sample()+'---------------------------------------------',(2,2))
    def test_wrong_shape(self):
        with self.assertRaises(ValueError):parse_ascii(sample(),(3,2))
    def test_missing_array(self):
        with self.assertRaises(ValueError):parse_ascii(sample().split('agb_sd')[0],(2,2))
    def test_duplicate_array(self):
        with self.assertRaises(ValueError):parse_ascii(sample()+'agb[1][2][2]\n',(2,2))
    def test_out_of_order_row(self):
        with self.assertRaises(ValueError):parse_ascii(sample().replace('[0][0]','[0][1]',1),(2,2))
    def test_short_row(self):
        with self.assertRaises(ValueError):parse_ascii(sample().replace('0, 1','0',1),(2,2))
    def test_noninteger_rejected(self):
        with self.assertRaises(ValueError):parse_ascii(sample().replace('0, 1','0, 1.5',1),(2,2))
    def test_int16_overflow_rejected(self):
        with self.assertRaises(ValueError):parse_ascii(sample().replace('0, 1','0, 32768',1),(2,2))
    def test_summary_retains_zero_not_fill(self):
        s=summarize(parse_ascii(sample(),(2,2)),2015)
        self.assertEqual((s['cells'],s['joint_valid'],s['zero_agb'],s['positive_agb_zero_sd']),(4,3,1,1))
        self.assertEqual((s['agb_fill'],s['sd_fill']),(1,1))
    def test_invalid_sd_not_counted_as_zero_precision(self):
        s=summarize({'agb':np.array([1,2,0]),'agb_sd':np.array([-1,10001,0])},2015)
        self.assertEqual(s['joint_valid'],1);self.assertEqual(s['positive_agb_zero_sd'],0)
        self.assertIsNone(s['positive_agb_sd_median_Mg_ha'])
    def test_hash_mismatch_stops_before_decode(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'bad').write_bytes(b'bad')
            with self.assertRaises(ValueError):acquire({'cache_filename':'bad','bytes':3,'sha256':'0'*64},p)

class Response:
    def __init__(self,status=206,content_range='bytes 0-3/8',body=b'abcd'):
        self.status_code=status;self.headers={'Content-Range':content_range};self.body=body;self.body_read=False
    def __enter__(self):return self
    def __exit__(self,*args):return False
    def iter_content(self,*args):self.body_read=True;yield self.body

class RangeTests(unittest.TestCase):
    def setUp(self):self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
    def reader(self,cap=8):return ReferenceRanges('https://example.org/immutable.zip',8,'date',self.temp.name,cap=cap,block=4)
    def test_exact_range_then_cache(self):
        r=self.reader();response=Response()
        with patch('reference_ranges_R03.requests.get',return_value=response)as get:
            self.assertEqual(r.read(4),b'abcd');r.seek(0);self.assertEqual(r.read(4),b'abcd');self.assertEqual(get.call_count,1)
        self.assertEqual((r.transferred,r.network_bytes),(4,4))
    def test_ignored_range_not_read(self):
        response=Response(status=200)
        with patch('reference_ranges_R03.requests.get',return_value=response):
            with self.assertRaises(ValueError):self.reader().read(4)
        self.assertFalse(response.body_read)
    def test_wrong_total_not_read(self):
        response=Response(content_range='bytes 0-3/9')
        with patch('reference_ranges_R03.requests.get',return_value=response):
            with self.assertRaises(ValueError):self.reader().read(4)
        self.assertFalse(response.body_read)
    def test_overflow_rejected(self):
        with patch('reference_ranges_R03.requests.get',return_value=Response(body=b'abcde')):
            with self.assertRaises(ValueError):self.reader().read(4)
    def test_truncation_rejected(self):
        with patch('reference_ranges_R03.requests.get',return_value=Response(body=b'a')):
            with self.assertRaises(ValueError):self.reader().read(4)
    def test_cap_before_network(self):
        with patch('reference_ranges_R03.requests.get')as get:
            with self.assertRaises(ValueError):self.reader(cap=3).read(3)
            get.assert_not_called()
    def test_full_read_over_cap_rejected(self):
        with self.assertRaises(ValueError):self.reader(cap=4).read()
    def test_negative_seek_rejected(self):
        with self.assertRaises(ValueError):self.reader().seek(-1)
    def test_orphan_cache_rejected(self):
        (Path(self.temp.name)/'0_3.bin').write_bytes(b'abcd')
        with self.assertRaises(ValueError):self.reader().read(4)
    def test_corrupted_cache_rejected(self):
        with patch('reference_ranges_R03.requests.get',return_value=Response()):self.reader().read(4)
        (Path(self.temp.name)/'0_3.bin').write_bytes(b'xxxx')
        with self.assertRaises(ValueError):self.reader().read(4)
    def test_prefetch_then_read_counts_once(self):
        response=Response(content_range='bytes 0-7/8',body=b'abcdefgh');r=self.reader()
        with patch('reference_ranges_R03.requests.get',return_value=response)as get:
            r.prefetch(0,1);self.assertEqual(r.read(8),b'abcdefgh');self.assertEqual(get.call_count,1)
        self.assertEqual((r.transferred,r.network_bytes),(8,8))
    def test_prefetch_cap_before_network(self):
        with patch('reference_ranges_R03.requests.get')as get:
            with self.assertRaises(ValueError):self.reader(cap=7).prefetch(0,1)
            get.assert_not_called()

class EvidenceTests(unittest.TestCase):
    def test_code_reverification_complete_not_execution(self):
        a=load('metadata/code_reverification_R03.json')
        self.assertEqual(len(a['verified']),21);self.assertLessEqual(a['bytes_represented'],2000000)
        self.assertFalse(a['provider_code_executed']);self.assertFalse(a['production_v7_aggregation_lineage_verified'])
    def test_archive_reproduction_exact(self):
        a=load('metadata/reference_archive_inspection_R03.json');b=load('metadata/reference_archive_reproduction_R03.json')
        self.assertEqual(a['selected'],b['selected']);self.assertEqual(b['network_bytes_this_run'],0)
    def test_native_source_identity_matches_protected_registry(self):
        original=ROOT.parent/'ecomod_followup_F09/metadata/native_probe_provenance.json'
        if not original.exists():self.skipTest('Protected F09 not present')
        rows=[r for r in json.loads(original.read_text())['native_payloads']if r['ISO3']=='BRA']
        self.assertEqual(rows,load('metadata/native_payload_registry_R03.json'))
    def test_native_metadata_not_equated_to_geotiff(self):
        a=load('metadata/native_variable_facts_R03.json')
        self.assertEqual(a['coarse_released_diff_qf_fill'],-32768)
        self.assertFalse(a['released_NetCDF_semantics_equated_to_script_GeoTIFF'])
    def test_archive_partial_not_full_identity(self):
        a=load('metadata/reference_archive_inspection_R03.json');g=load('protocol/REFERENCE_ARCHIVE_GUARD_R03.json')
        self.assertFalse(a['whole_archive_md5_verified']);self.assertFalse(a['whole_archive_downloaded'])
        self.assertEqual(a['unique_source_bytes_represented'],22551986)
        self.assertLessEqual(a['unique_source_bytes_represented'],g['maximum_cumulative_source_bytes'])
        self.assertEqual(len(a['selected']),4)
        self.assertTrue(all(r['crc_verified_complete_member'] and r['rows']==200152 for r in a['selected']))
    def test_archive_no_2023_label_not_invented(self):
        a=load('metadata/reference_archive_inspection_R03.json')
        self.assertFalse(any('2023' in n for n in a['archive_members']))
        self.assertEqual(a['selected'][-1]['epoch_field_values'],{})
    def test_local_reference_not_admitted(self):
        with (ROOT/'data/local_reference_candidate_R03.csv').open()as f:rows=list(csv.DictReader(f))
        self.assertEqual(len(rows),4)
        for r in rows:
            self.assertEqual(r['eligible_primary_2015_2023'],'no');self.assertEqual(r['N'],'1')
            for k in ['QUALITY_MIN_PLOTS','QUALITY_LOCALLY_REP','QUALITY_STRICT_FILTER']:self.assertEqual(r[k],'0')
        self.assertEqual(rows[-1]['Year'],'')
        self.assertEqual(len({r['ID'] for r in rows[:3]}),3)
    def test_sd_summary_reconciles(self):
        a=load('metadata/native_sd_audit_R03.json')
        for r,pz in zip(a['rows'],[1032,946]):
            self.assertEqual(r['joint_valid'],65536);self.assertEqual(r['positive_agb_zero_sd'],pz)
            self.assertEqual(r['zero_sd'],r['zero_agb']+pz)
        states=a['zero_estimate_endpoint_states'];self.assertEqual(sum(r['cells']for r in states),65536)
        self.assertEqual(states[0]['cells'],44021)
    def test_no_registered_after_fact_claim(self):
        a=load('protocol/NATIVE_SD_SCOPE_R03.json')
        self.assertTrue(a['initial_descriptive_inspection_preceded_this_record']);self.assertTrue(a['no_prospective_registration_claim'])
    def test_no_false_production_verification(self):
        a=load('metadata/implementation_audit_R03.json')
        for k in ['provider_script_executed','production_aggregation_kernel_located','production_normalization_verified','released_files_inferred_to_have_flag_NODATA_zero']:self.assertFalse(a[k])
    def test_no_covariance_or_admission(self):
        a=load('metadata/native_sd_audit_R03.json')
        for k in ['new_error_covariance_estimated','confidence_intervals','zero_origin_verified','country_admissions_changed']:self.assertFalse(a[k])

if __name__=='__main__':unittest.main()

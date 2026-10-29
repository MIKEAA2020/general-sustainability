import unittest,sys,json,hashlib,unicodedata,csv
from pathlib import Path
from types import SimpleNamespace
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from xlsx_reference_audit import token,rowhash,safe_zip,ROOT

def load(name):return json.loads((ROOT/name).read_text())
def member(name='xl/worksheets/sheet1.xml',size=10,flag=0):return SimpleNamespace(filename=name,file_size=size,flag_bits=flag)
def archive(*items):return SimpleNamespace(infolist=lambda:list(items))

class F08Tests(unittest.TestCase):
    def setUp(self):self.cfg=load('configs/xlsx_retry_F08.json')
    def test_missing_is_blank_not_zero_or_literal_None(self):
        self.assertEqual(token(None),'');self.assertEqual(token('  '),'');self.assertEqual(token(0),'0');self.assertNotEqual(token('None'),'')
    def test_integral_serialization_only(self):
        self.assertEqual(token('3.0'),'3');self.assertEqual(token('3,00'),'3');self.assertEqual(token('3.25'),'3.25');self.assertEqual(token('Floresta'),'Floresta')
    def test_unicode_normalization_retains_class_meaning(self):self.assertEqual(token(unicodedata.normalize('NFD',' NÃO OBSERVADO ')),'NÃO OBSERVADO')
    def test_payload_hash_compares_named_fields_not_dictionary_order(self):
        self.assertEqual(rowhash({'a':3,'b':None},['a','b']),rowhash({'b':'','a':'3.0'},['a','b']));self.assertNotEqual(rowhash({'a':3,'b':0},['a','b']),rowhash({'a':3,'b':None},['a','b']))
    def test_safe_archive_passes(self):self.assertEqual(len(safe_zip(archive(member()),self.cfg)),1)
    def test_unsafe_paths_rejected(self):
        for name in ['../a.xml','/a.xml','xl/../a.xml']:
            with self.assertRaises(ValueError):safe_zip(archive(member(name)),self.cfg)
    def test_duplicate_members_rejected(self):
        with self.assertRaises(ValueError):safe_zip(archive(member(),member()),self.cfg)
    def test_encrypted_members_rejected(self):
        with self.assertRaises(ValueError):safe_zip(archive(member(flag=1)),self.cfg)
    def test_member_cap_rejected(self):
        with self.assertRaises(ValueError):safe_zip(archive(member(size=400000001)),self.cfg)
    def test_total_cap_rejected(self):
        with self.assertRaises(ValueError):safe_zip(archive(member('a',300000000),member('b',200000001)),self.cfg)
    def test_scope_specific_frozen_caps(self):
        f=load('metadata/reference/xlsx_retry_freeze_F08.json')
        for p,k in [('protocol/XLSX_RETRY_F08.md','protocol_sha256'),('configs/xlsx_retry_F08.json','configuration_sha256')]:self.assertEqual(hashlib.sha256((ROOT/p).read_bytes()).hexdigest(),f[k])
        self.assertEqual(self.cfg['workbook_download_cap'],40000000);self.assertEqual(self.cfg['maximum_data_rows'],100000);self.assertEqual(self.cfg['maximum_columns'],500)
        self.assertEqual((ROOT/'configs/brazil_support_F05.json').read_bytes(),(ROOT.parent/'ecomod_followup_F07/configs/brazil_support_F05.json').read_bytes()) if (ROOT.parent/'ecomod_followup_F07').exists() else None
    def test_complete_source_identity(self):
        d=load('metadata/reference/xlsx_full_source_F08.json');self.assertEqual(d['bytes'],33714740);self.assertEqual(d['sha256'],'f4bec9d2eb624aff25efb0620476cebbb0e07eaefb699d03b40ef3efcf69ac62');self.assertEqual(load('data/reference/xlsx_audit_F08.json')['workbook_sha256'],d['sha256'])
    def test_full_population_and_formula_scope(self):
        d=load('data/reference/xlsx_audit_F08.json');self.assertTrue(d['all_data_rows_streamed']);self.assertEqual(d['xlsx_profile']['records'],85152);self.assertEqual(d['xlsx_profile']['unique_TARGETID'],85152);self.assertEqual(len(d['xlsx_profile']['fields']),135);self.assertEqual(d['formula_cells_not_executed'],0)
    def test_all_common_annual_payloads_agree(self):
        d=load('data/reference/xlsx_audit_F08.json');self.assertEqual(len(d['common_annual_fields_compared']),117);self.assertEqual(d['exact_CSV_comparison']['same_all_common_annual_payloads'],85152);self.assertEqual(d['IDs_not_in_CSV'],0);self.assertEqual(d['CSV_ids_not_in_workbook'],0)
    def test_coordinates_roles_and_endpoint_tokens_agree(self):
        d=load('data/reference/xlsx_audit_F08.json');c=d['exact_CSV_comparison']
        for k in ['direct_coordinates_match_within_1e-8_deg','same_training_role_tokens','same_2015_label_tokens','same_2023_label_tokens']:self.assertEqual(c[k],85152)
        self.assertEqual(c['transposed_coordinates_match_within_1e-8_deg'],0);self.assertEqual(d['xlsx_profile']['explicit_role_field_values']['AMOSTRAS'][''],75153)
    def test_no_new_validation_or_admission(self):
        d=load('data/reference/xlsx_audit_F08.json');self.assertEqual(d['xlsx_profile']['endpoint_nonblank_records']['2023'],4053);self.assertEqual(d['xlsx_profile']['local_endpoint_nonblank_records']['2023'],0)
        for k in ['local_paired_reference_validation_established','map_reference_class_confusion_computed','national_admission_changed']:self.assertFalse(d[k])
        rows=list(csv.DictReader((ROOT/'data/support/physical_admission_F08.csv').open()));self.assertEqual(len(rows),8);self.assertTrue(all(x['admission']=='hold_not_admitted'for x in rows))
    def test_linked_orcid_in_both_sources(self):
        for n in ['main','SI']:self.assertIn(r'\href{https://orcid.org/0000-0002-0019-1842}{0000-0002-0019-1842}',(ROOT/f'followup_F08_{n}.tex').read_text())
    def test_seven_novelty_keywords_visible_and_in_metadata(self):
        words=load('configs/study_design.json')['keywords'];self.assertEqual(len(words),7);self.assertIn('Partial identification',words);self.assertIn('Subpixel biomass allocation',words)
        for n in ['main','SI']:self.assertIn('pdfkeywords={'+ '; '.join(words)+'}',(ROOT/f'followup_F08_{n}.tex').read_text())
        self.assertIn(r'\textbf{Keywords:} '+'; '.join(words)+'.',(ROOT/'followup_F08_main.tex').read_text())
    def test_exact_author_approved_declaration(self):self.assertIn(r'\href{http://Arena.ai}{Arena.ai} Agent Mode was used to assist with computational methods and literature review.',(ROOT/'followup_F08_main.tex').read_text())
    def test_access_status_does_not_conflate_head_with_reading(self):
        a=load('metadata/reference/access_checks_F08.json');self.assertEqual([x['status']for x in a],[200,404,404,200]);self.assertTrue(all(not x['body_read']for x in a));self.assertEqual(int(a[0]['bytes_header']),67553500)
        text=(ROOT/'INPUT_LINKS_F08.md').read_text()
        for x in a:self.assertIn(x['url'],text)
        self.assertIn(load('metadata/reference/xlsx_full_source_F08.json')['url'],text)

if __name__=='__main__':unittest.main()

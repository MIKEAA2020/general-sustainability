"""Strict bounded ZIP metadata inspection; not a whole-workbook reference audit."""
from pathlib import Path
import argparse,json,zipfile,hashlib,xml.etree.ElementTree as ET
from bounded_tiff import RangeReader
ROOT=Path(__file__).resolve().parents[1]
NS={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def run(cache,offline=False):
    f=json.loads((ROOT/'metadata/allocation/freeze_F07.json').read_text())
    for name,key in [('protocol/ALLOCATION_ENVELOPE_F07.md','protocol_sha256'),('configs/allocation_F07.json','configuration_sha256')]:
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=f[key]:raise ValueError('Frozen XLSX inspection scope drift')
    cfg=json.loads((ROOT/'configs/allocation_F07.json').read_text());h={k.lower():v for k,v in f['xlsx_HEAD']['headers'].items()};rr=RangeReader(f['xlsx_HEAD']['url'],int(h['content-length']),h['etag'],cache,cap=cfg['xlsx_range_cap']);out={'revision':'F07','url':rr.url,'etag':rr.etag,'whole_object_bytes':rr.size,'whole_file_exceeds_25MB_cap':rr.size>25_000_000,'whole_file_downloaded':False,'full_workbook_audited':False,'local_paired_reference_completeness_established':False}
    if offline:
        def denied(*a,**k):raise ValueError('Missing XLSX range cache in offline mode')
        rr.session.get=denied
    try:
        with zipfile.ZipFile(rr)as z:
            infos=z.infolist();out['members']=[dict(name=i.filename,bytes=i.file_size,compressed_bytes=i.compress_size)for i in infos];out['worksheet_exceeds_250MB_member_cap']=any(i.filename.startswith('xl/worksheets/')and i.file_size>250_000_000 for i in infos);meta={}
            for name in ['xl/workbook.xml','xl/sharedStrings.xml']:
                info=z.getinfo(name)
                if info.file_size>250_000_000 or info.compress_size>cfg['xlsx_range_cap']:raise ValueError('Metadata member exceeds bounded scope')
                b=z.read(name);meta[name]={'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
                if name.endswith('workbook.xml'):
                    tree=ET.fromstring(b);out['sheet_names']=[e.attrib.get('name')for e in tree.findall('s:sheets/s:sheet',NS)]
                else:
                    tree=ET.fromstring(b);strings=[''.join(si.itertext())for si in tree.findall('s:si',NS)];out['shared_string_tokens_include']={v:v in strings for v in ['CLASS_2015','CLASS_2023','CLASS_2024','AMOSTRAS','AMOSTRA_AM']}
            out['fully_read_metadata_members']=meta;out['scope_note']='ZIP directory, workbook and shared-string metadata only. Worksheet declared size exceeds the full-member guard and was not opened/decoded. Shared-string tokens do not certify populated columns, rows, or reference completeness.'
    finally:
        out['distinct_source_bytes']=rr.transferred;out['ranges']=rr.receipts();rr.close()
    (ROOT/'metadata/reference/xlsx_metadata_F07.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='ranges'},indent=2));return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--cache',type=Path,required=True);p.add_argument('--offline',action='store_true');a=p.parse_args();run(a.cache,a.offline)

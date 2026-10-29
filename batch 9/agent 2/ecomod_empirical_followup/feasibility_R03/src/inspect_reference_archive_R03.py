from pathlib import Path
import sys,json,zipfile,hashlib,csv,io,re,requests
from reference_ranges_R03 import ReferenceRanges
ROOT=Path(__file__).resolve().parents[1]
def check_identity(original,head,guard):
 resp=requests.get(original['links']['self'],timeout=60);resp.raise_for_status();now=resp.json();f=now['files'][0];old=original['files'][0]
 if (f['key'],f['size'],f['checksum'])!=(old['key'],old['size'],old['checksum']):raise ValueError('Source record changed')
 h=requests.head(guard['source_url'],allow_redirects=True,timeout=60);h.raise_for_status()
 if h.headers.get('Last-Modified')!=head['headers']['last-modified'] or int(h.headers.get('Content-Length',0))!=guard['source_advertised_bytes']:raise ValueError('Archive HEAD identity changed')

def run(cache, output=None):
 guard=json.loads((ROOT/'protocol/REFERENCE_ARCHIVE_GUARD_R03.json').read_text());head=json.loads((ROOT/'metadata/agbref_archive_head_R03.json').read_text());original=json.loads((ROOT/'metadata/agbref_versions_latest_R03.json').read_text());reader=ReferenceRanges(guard['source_url'],guard['source_advertised_bytes'],head['headers']['last-modified'],cache/'reference_zip_ranges',cap=guard['maximum_cumulative_source_bytes']);selected=guard['selected_members_after_directory_before_member_payload'];results=[];decoded=0
 check_identity(original,head,guard)
 with zipfile.ZipFile(reader)as z:
  allinfo=z.infolist();names=[i.filename for i in allinfo]
  if len(allinfo)>guard['maximum_archive_members'] or len(names)!=len(set(names)):raise ValueError('Unsafe archive member count/duplicates')
  for name in names:
   if name.startswith('/')or '..'in Path(name).parts:raise ValueError('Unsafe archive path')
  for name in selected:
   info=z.getinfo(name);decoded+=info.file_size
   if info.flag_bits&1 or info.file_size>guard['maximum_member_decoded_bytes'] or decoded>guard['maximum_total_selected_decoded_bytes']:raise ValueError('Member decode cap/encryption')
   i=names.index(name);next_offset=allinfo[i+1].header_offset if i+1<len(allinfo)else z.start_dir
   reader.prefetch(info.header_offset//reader.block,(next_offset-1)//reader.block)
   b=z.read(name) # Complete-member CRC32 is checked by zipfile at EOF.
   if len(b)!=info.file_size:raise ValueError('Decoded size mismatch')
   dest=cache/Path(name).name;dest.write_bytes(b);text=b.decode('utf-8-sig');sample=text[:8000];sep=';'if sample.splitlines()[0].count(';')>sample.splitlines()[0].count(',')else',';rows=csv.DictReader(io.StringIO(text),delimiter=sep);fields=rows.fieldnames
   r={'member':name,'bytes':len(b),'compressed_bytes':info.compress_size,'sha256':hashlib.sha256(b).hexdigest(),'crc32':f'{info.CRC:08x}','crc_verified_complete_member':True,'fields':fields,'rows':0,'epoch_field_values':{},'fixed_footprint_centroid_count':0,'nearby_centroid_count_0p25deg_padding':0,'source_codes':{}}
   bounds=(-180+146433*360/405000,-180+146689*360/405000,80-106146*360/405000,80-105890*360/405000);print('HEADER',name,fields,flush=True)
   for row in rows:
    r['rows']+=1
    if r['rows']>guard['maximum_csv_rows_per_member']:raise ValueError('CSV row cap')
    for k in fields:
     if k.lower()in ['epoch','year','map_year','mapyear','avg_year']:
      values=r['epoch_field_values'].setdefault(k,{})
      token=row[k];values[token]=values.get(token,0)+1
    code=row.get('CODE','');r['source_codes'][code]=r['source_codes'].get(code,0)+1
    try:x=float(row['POINT_X']);y=float(row['POINT_Y'])
    except (KeyError,ValueError):continue
    w,e,s,n=bounds
    if w<=x<=e and s<=y<=n:r['fixed_footprint_centroid_count']+=1
    if w-.25<=x<=e+.25 and s-.25<=y<=n+.25:r['nearby_centroid_count_0p25deg_padding']+=1
   print('INSPECTED',name,r['rows'],'rows','local',r['fixed_footprint_centroid_count'],'nearby',r['nearby_centroid_count_0p25deg_padding'],flush=True);results.append(r)
 # Recheck the published record's advertised identity and HEAD last modification.
 check_identity(original,head,guard)
 out={'source_version_record':original['id'],'whole_archive_size':guard['source_advertised_bytes'],'whole_archive_downloaded':False,'whole_archive_md5_verified':False,'partial_identity_scope':'Version URL, advertised checksum before/after, HEAD date/size, exact ranges, range SHA256 and complete selected-member CRC32','unique_source_bytes_represented':reader.transferred,'network_bytes_this_run':reader.network_bytes,'archive_members':names,'selected':results,'source_record_and_HEAD_rechecked_after':True,'new_reference_admitted':False}
 (output or ROOT/'metadata/reference_archive_inspection_R03.json').write_text(json.dumps(out,indent=2)+'\n');print('TOTAL SOURCE BYTES',reader.transferred,flush=True)
 return out
if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('cache',type=Path)
 parser.add_argument('--output',type=Path)
 args=parser.parse_args();run(args.cache,args.output)

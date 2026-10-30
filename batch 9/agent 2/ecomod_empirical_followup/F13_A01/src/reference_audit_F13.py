#!/usr/bin/env python3
"""Audit the currently linked Brazilian vector archive without expanding its 209 MB DBF."""
import json,struct,zipfile
from pathlib import Path
from analyze_sources_F13 import ROOT,source,require

def run(out):
 name='BRA_current_public_vector_2026_10.zip'
 with zipfile.ZipFile(source(name))as z:
  with z.open('mapbiomas_85k_points_validation.dbf')as f:
   b=f.read(32);n=struct.unpack('<I',b[4:8])[0];h=struct.unpack('<H',b[8:10])[0]
   header=b+f.read(h-32);fields=[header[i:i+11].split(b'\0')[0].decode()for i in range(32,h-1,32)]
 require(n==85152 and len(fields)==126,'Current public vector schema changed')
 d=dict(source_name=name,record_count=n,field_count=len(fields),field_names=fields,
  annual_fields_2023=[x for x in fields if'2023'in x],annual_fields_2024=[x for x in fields if'2024'in x],
  new_reference_collection_3_established=False,no_full_DBF_extraction_required=True,
  current_link_year_does_not_establish_reference_epoch_coverage=True)
 out.write_text(json.dumps(d,indent=2)+'\n');return d
if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,default=ROOT/'metadata/BRA_current_vector_schema_F13.json');a=p.parse_args();print(json.dumps(run(a.output),indent=2))

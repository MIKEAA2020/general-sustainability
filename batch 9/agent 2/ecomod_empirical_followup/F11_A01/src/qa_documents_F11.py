#!/usr/bin/env python3
"""Compiled-document QA; no claim of ecological validation."""
import json
import hashlib
from pathlib import Path
import re
import unicodedata
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]

def run():
    records=[]
    for kind in ('main','SI'):
        path=ROOT/f'followup_F11_A01_{kind}.pdf'
        doc=fitz.open(path);text='\n'.join(page.get_text()for page in doc)
        normalized=unicodedata.normalize('NFKC',text)
        if '??'in normalized:raise ValueError('Unresolved PDF reference marker')
        if 'identifiability'not in normalized:raise ValueError('Active F11 title missing')
        log=(ROOT/f'.cache/tex/followup_F11_A01_{kind}.log').read_text(errors='replace')
        warnings=[line for line in log.splitlines()if re.search(r'Overfull|Underfull|Warning|undefined',line)]
        if warnings:raise ValueError('Document build warnings: '+repr(warnings))
        outside=[]
        for i,page in enumerate(doc):
            for b in page.get_text('blocks'):
                if b[0]<-1 or b[1]<-1 or b[2]>page.rect.width+1 or b[3]>page.rect.height+1:
                    outside.append(dict(page=i+1,bbox=list(b[:4])))
        if outside:raise ValueError('PDF text outside page bounds')
        if kind=='main':
            for needle in ('70.23','1.4555','1.9495','49.05','55.93'):
                if needle not in normalized:raise ValueError('Numerical result missing: '+needle)
            if 'Arena.ai'not in normalized:raise ValueError('AI declaration missing')
        else:
            compact=re.sub(r'\s+','',normalized)
            for needle in ('native_probe_coverage_F11.csv','joint_quadrant_certificates_F11.csv'):
                if needle not in compact:raise ValueError('Supplemental traceability missing: '+needle)
        records.append(dict(file=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),pages=len(doc),text_characters=len(text),
                            warning_lines=warnings,unresolved_reference_markers=False,
                            text_outside_page_bounds=outside))
    payload=dict(documents=records,scope='Compilation, reference markers, key result presence and page bounds; visual review separate')
    (ROOT/'metadata/document_QA_F11.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))

if __name__=='__main__':run()

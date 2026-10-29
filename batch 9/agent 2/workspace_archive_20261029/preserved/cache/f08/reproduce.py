from pathlib import Path
import hashlib,json,sys,contextlib
from unittest.mock import patch
P=Path('/home/user/ecomod_followup_F08');paths=['data/reference/xlsx_audit_F08.json','metadata/reference/xlsx_member_hashes_F08.json'];h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();before={x:h(P/x)for x in paths};sys.path.insert(0,str(P/'src'));import xlsx_reference_audit
with Path('/home/user/.cache/f08/reproduction.log').open('w')as log,contextlib.redirect_stdout(log),patch('requests.get',side_effect=RuntimeError('HTTP disabled')),patch('requests.Session.get',side_effect=RuntimeError('HTTP disabled')):xlsx_reference_audit.run(Path('/home/user/.cache/f08'),offline=True)
assert all(h(P/x)==v for x,v in before.items());(P/'metadata/reference/xlsx_reproduction_F08.json').write_text(json.dumps({'network_disabled':True,'complete_workbook_reparsed':True,'audit_and_member_hashes_byte_identical':True,'files':before},indent=2)+'\n');print('F08 whole-workbook offline reproduction byte-identical',flush=True)

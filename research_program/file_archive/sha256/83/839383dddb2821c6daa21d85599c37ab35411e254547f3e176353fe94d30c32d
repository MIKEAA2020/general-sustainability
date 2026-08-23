#!/usr/bin/env python3
from pathlib import Path
import csv
root=Path(__file__).parent
rows=list(csv.DictReader((root/'action_register.csv').open(encoding='utf-8')))
order=['manuscript_policy','integration_decision','cross_article_decision','bridge','cross_article_bridge','verification','implementation']
out=['# Research Program Action Register','','This is the human-readable view of `action_register.csv`. The CSV is the operational source for filtering and status updates.','','## Status vocabulary','','- `open`: ready for work','- `blocked`: waits on listed dependencies','- `active`: standing decision or work in progress','- `completed`: discharged with evidence','- `superseded`: replaced by another action','']
for typ in order+sorted(set(r['action_type'] for r in rows)-set(order)):
 selected=[r for r in rows if r['action_type']==typ]
 if not selected:continue
 out+=['## '+typ.replace('_',' ').title(),'']
 for r in selected:
  out.append(f"### {r['action_id']} — {r['title']}")
  out.append(f"- **Source:** {r['source']}")
  out.append(f"- **Status:** {r['status']}")
  out.append(f"- **Priority:** {r['priority']}")
  out.append(f"- **Target:** {r['target']}")
  if r['dependencies']:out.append(f"- **Dependencies:** {r['dependencies']}")
  if r['notes']:out.append(f"- **Notes:** {r['notes']}")
  if r['completion_evidence']:out.append(f"- **Evidence:** {r['completion_evidence']}")
  out.append('')
(root/'action_register.md').write_text('\n'.join(out),encoding='utf-8')
print(f"Rendered {len(rows)} actions")

import re
txt = open('data/revisions/IMPLEMENTED_revision_ECOMOD_v21.md').read()

# split body vs references
ref_idx = txt.find('## References')
body = txt[:ref_idx]
refs_txt = txt[ref_idx:]

# grab each reference's first-authorship token
ref_entries = re.findall(r'^- (.+?)\n', refs_txt, re.M)

# citation forms: "Name (year)", "Name & Other (year)", "Name et al. (year)", "Name, Other & Third (year)"
# We'll map surname -> year for candidate checks
def surnames(entry):
    # entry like "Blomqvist, L., Brook, B. W., ... & Shellenberger, M. (2013)."
    before = entry.split('(')[0]
    # take surnames: tokens ending in comma are given; surnames are before comma.
    names = re.split(r',\s*', before.strip())
    su = [n.strip() for n in names if re.match(r'^[A-Z][A-Za-z\-]+', n.strip())]
    return su

issues = []
for e in ref_entries:
    if 'Companion manuscripts' in e or 'Reproducibility' in e or 'Data availability' in e:
        continue
    m = re.search(r'\((\d{4})\)', e)
    yr = m.group(1) if m else None
    su = surnames(e)
    if not su:
        continue
    last = su[0]  # primary surname
    # search body for surname
    if last not in body:
        issues.append((last, yr))
    else:
        # if surname found, confirm a year-citation somewhere
        print(f"OK  {last} ({yr}) found in body")

print("\n--- References with surname NOT found in body ---")
for last, yr in issues:
    print(f"ORPHAN? {last} ({yr})")
if not issues:
    print("(none)")

import io

P = '/home/user/p5/phase0_scan.py'
s = io.open(P, encoding='utf-8').read()

# ---------------------------------------------------------------- 1. PLACE_TAIL
ANCHOR = "# a reference entry must carry a year"
assert ANCHOR in s

PLACE = r'''# a bare publisher/city tail left behind by the splitter, e.g.
# "Birkhaeuser, Boston." / "Prentice-Hall, Upper Saddle River, NJ." /
# "Fisheries and Oceans Canada, Ottawa." Two to five capitalised words,
# comma-separated, carrying no year of its own.
#
# Promoted to FATAL 2026-10-01 after triage in report-only mode: 20 hits across
# 59 files, 100% precision, every one a genuine detached tail. It currently has
# ZERO live-head hits, so it does not change the exit status today -- it is a
# guard against future merges, which is the point.
PLACE_TAIL = re.compile(
    r'^[A-ZÄÖÅ][\w\'\-]*'
    r'(?:\s+(?:and|of|for|the|de|van|der)\s+[a-zA-Z\'\-]*'
    r'|\s+[A-Z][\w\'\-]*){0,4}'
    r'(?:,\s*[A-ZÄÖÅ][\w\'\-]*(?:\s+[A-Z][\w\'\-]*){0,3}){1,3}\.?$')

# institutional / corporate authors. Needed because these are legitimate
# year-less citations (a data portal has no publication year), and without
# them the "no year, no author" signal reports them as detached tails.
CORPORATE = re.compile(
    r'^(?:U\.?\s?S\.?|U\.?\s?K\.?|UNFCCC|UNEP|UN\s|FAO|ICES|DFO|NOAA|USGS|NASA|'
    r'EPA|OECD|Eurostat|Statistics\s+Canada|World\s+Bank|'
    r'Texas\s+Water\s+Development\s+Board|Edwards\s+Aquifer\s+Authority|'
    r'National\s+Research\s+Council|Fisheries\s+and\s+Oceans\s+Canada|'
    r'Geological\s+Survey'
    r'|[A-Z][A-Za-z\'\-]*\s+(?:University|Institute|Department|Ministry|Agency|'
    r'Bureau|Survey|Council|Commission|Authority|Board|Centre|Center|Service|'
    r'Laboratory|Observatory|Administration)s?\b)')

'''

s = s.replace(ANCHOR, PLACE + ANCHOR, 1)

# ------------------------------------------------------- 2. K rule: add place-tail
OLD_K = """    ents = ref_entries(c)
    for ln, e in ents:
        if not YEAR.search(e):"""
NEW_K = """    ents = ref_entries(c)
    for ln, e in ents:
        # a bare publisher/city fragment is a detached tail on its own
        # evidence -- it does not need the "no year" test below, and it does
        # not need to open with a known journal name either.
        if PLACE_TAIL.match(e) and not YEAR.search(e) and not CORPORATE.match(e):
            out.append(('K.place-tail', e[:52],
                        'detached publisher/city tail: no year, and it is the '
                        'place half of an entry whose head is elsewhere', ln))
            continue
        if not YEAR.search(e):"""
assert OLD_K in s, 'K loop not found'
s = s.replace(OLD_K, NEW_K, 1)

# ---------------------------------------------------------------- 3. FATAL set
OLD_F = "FATAL = frozenset(['H.duplicate-declarations', 'I.duplicate-supplement',"
NEW_F = "FATAL = frozenset(['H.duplicate-declarations', 'I.duplicate-supplement',\n                   'K.place-tail',"
assert OLD_F in s
s = s.replace(OLD_F, NEW_F, 1)

io.open(P, 'w', encoding='utf-8').write(s)
print('K.place-tail promoted to FATAL; CORPORATE author guard added')

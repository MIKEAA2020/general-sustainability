"""Phase 0 soundness sweep — systematic, not enumerative.

The defect list is open, so this does not hard-code a list of known defects and stop. It
looks for *classes* of defect, mechanically, across every source paper:

  A. Stale provenance      -- version pins / counts contradicted by the artifact tree
  B. Convention contamination -- numbers produced on a superseded basis
  C. Unverifiable claims   -- build/compile claims that cannot be re-run here
  D. Abstract selection    -- headline numbers in the abstract that differ from the body
  E. Unsourced numbers      -- tabulated quantities with no stated provenance nearby
  F. Mis-cited prior art   -- nearest neighbour named in the audit but absent from the text
  G. Bare point estimates  -- headline figures quoted without their uncertainty band

  H. Duplicated declarations  -- more than one Declarations block per file
  I. Duplicated supplement    -- more than one supplementary-material passage per file
  J. Cross-unit file refs     -- paperNN_* file belonging to a different unit than this one
  K. Split bibliography       -- a reference entry with its head or tail detached
  L. Duplicate bibliography   -- two entries sharing a normalised key

H-L are the STRUCTURAL GATE. They were added after the paper08 reference list was
repaired by hand and then reappeared, unchanged, on a clean re-merge: the merges
(mergelib.py and the per-pair merge_*.py scripts) are scripted, and their
split_entries() shreds reference lists. Repairing the merged .tex is therefore
temporary. These classes detect the damage the scripts CAUSE, and merge_gate()
below is intended to be called by the merge scripts so that a re-merge FAILS
rather than silently regenerating the defect.

Each finding is reported with file, line and the matching text so it can be checked.
"""
import io, os, re, sys, json

PAPERS = '/home/user/papers/'

# ------------------------------------------------------------------ signatures
# (A) stale provenance: the artifact tree says these are wrong
STALE = [
    (r'v4\.14\.0', 'Lean toolchain pin; repo pin is v4.34.1'),
    (r'\b54\s+modules\b', 'Lean module count; repo has 60 under Formalizations/'),
    (r'\b60\s+build\s+jobs\b', 'build claim from the v4.14.0 run; not reproducible here'),
]

# CONTEXT CHECK — a string match is a CANDIDATE, not a finding.
#
# Seven of the first ten "findings" were false positives: every one of papers 1, 3, 4 and 5
# states the stale Lean pin *and then discloses it* ("The build has not been re-run since
# the toolchain pin moved, so the build-job figures below date from the v4.14.0 run and
# should be re-confirmed before submission"). Editing those would have DELETED an honest
# caveat. So: if the excusing context is present near the match, the hit is reclassified as
# a disclosed caveat -- which is a POSITIVE signal, not a defect.
#
# This is the mirror of enumeration-undercounting: pattern-matching invents defects, and
# acting on invented defects degrades the paper.
CONTEXT_WINDOW = 700   # characters either side of the match
CONTEXT_EXCUSE = {
    r'v4\.14\.0': [
        r'currently\s*\\texttt\{v4\.34\.1\}',      # states the current pin too
        r'build has not\s*\\?\s*(?:been\s*)?re-?run',  # and discloses it
    ],
    r'\b54\s+modules\b': [r'(?:currently|now)\s*\\texttt\{?60'],
    r'\b60\s+build\s+jobs\b': [r'build has not\s*\\?\s*(?:been\s*)?re-?run'],
}

# Self-disclosure is a GOOD sign. Detect it so the sweep can report it positively.
DISCLOSED_MARKERS = [
    (r'build has not\s*\\?\s*(?:been\s*)?re-?run', 'toolchain caveat disclosed'),
    (r'should be re-?confirmed before submission', 'pre-submission recheck flagged by the paper'),
    (r'not verifiable (?:here|now)|UNVERIFIABLE', 'verification limit stated'),
]

# (B) superseded hybrid basis (E2): v2 numbers, wrong under the source-year ruling
HYBRID_BAD = {
    '-460.03': 'UC_min v2 (hybrid) -> -328.97',
    '-318.76': 'UC_q05 v2 (hybrid) -> -287.36',
    '-114.85': 'UC_q10 v2 (hybrid) -> -80.87',
    '134.96': 'residual SD v2 (hybrid) -> 114.91',
}

# (F) nearest neighbours the audits say must be cited
MUST_CITE = {
    'paper01': [('Doyen', 'Doyen 2000 output-feedback (Set-Valued Analysis 8:149-162)'),
                ('viscosity', 'HJ-reachability / viscosity lineage')],
    'paper06': [('robust optimi', 'robust-optimisation separation results')],
}

# (G) headline figures that the audits say are ill-conditioned and must carry a band
ILLCOND = [
    (r'\b6\.5(?:0|01)?\s*(?:yr|years?)\b', '6.5-yr crossing: must carry the 0.87-10.67 band'),
]


def strip_comments(s):
    return "\n".join(re.sub(r'(?<!\\)%.*$', '', l) for l in s.split('\n'))


def find_line(c, needle):
    for i, l in enumerate(c.split('\n')):
        if needle in l:
            return i + 1
    return None


# ============================================================================
#  H-L: structural gate
#
#  These detect damage that the merge scripts PRODUCE, not damage inherited from
#  a source. Established empirically 2026-10-01: paper08 v45 (36 reference
#  entries, 0 orphans) and paper07 v50 (37 entries, 0 orphans) are clean, yet
#  merge_08_07.py's split_entries() turns them into 30/14 and 59/12 and the
#  re-merged v46 reproduces every artifact that had been repaired by hand.
# ============================================================================

# A "passage" is a block that OPENS with the supplement phrase. In-text mentions
# ("deposited with the supplementary material, S9") mid-sentence are not
# passages and must not fire.
SUPP_HEAD = re.compile(r'\\(?:sub)*section\*?\{Supplementary material\}', re.I)
SUPP_OPEN = re.compile(r'^\s*(?:\\textbf\{\s*Supplementary material\s*\}|Supplementary material\b)',
                       re.I)

DECL_HEAD = re.compile(r'\\(?:sub)*section\*?\{Declarations\}')

# a bare publisher/city tail left behind by the splitter, e.g.
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

# a reference entry must carry a year; a fragment left behind by the splitter
# ("Academic Press, Boston." / "Ambio 49, 1067--1075.") never does
YEAR = re.compile(r'\b(?:1[89]\d{2}|20\d{2})\b')

# a GLUED entry: the tail of one reference runs straight into the next author
# head with no period in between, so the script's splitter cannot see the seam.
# The token immediately before the surname is a DOI, a page range, a volume:page
# or a bare year -- i.e. something that ends a reference. "and Richardson, A.J.,
# 2012" and "Smith, J., Jones, A., 2020" deliberately do NOT match.
TAIL_TOK = r'(?:\bdoi:\S+|\d+\s*-{1,2}\s*\d+|\b\d+\s*:\s*\d+|\b(?:19|20)\d{2}\b)'
NAME_YR = r'[A-ZÄÖÅ][\w\'{}\\\"~\^\- ]{1,30}?,\s*(?:19|20)\d{2}'
GLUED = re.compile(TAIL_TOK + r'\s+' + NAME_YR)

# tokens that begin a detached tail rather than an author head
TAIL_LEAD = re.compile(
    r'^(?:Ambio|Nature|Science|Theoretical Ecology|ICES Journal|Fish(?:eries)?|'
    r'Marine Policy|Management Science|Astrophysics|Automatica|Biogeosciences|'
    r'Cambridge University|Academic Press|Springer|SIAM|Prentice|Wiley|'
    r'Journal of Public|Nonlinear Oscillations|Lawrence Erlbaum)')

# underscores are escaped in LaTeX ("paper4\_supplementary\_v8.md"), so the
# separator may be a literal _ or \_
CROSS_UNIT = re.compile(r'\bpaper0?(\d+)(?:\\?_[A-Za-z0-9]*)*\.(?:md|tex|pdf)')


def ref_block(c):
    """-> (text of the References section, line offset) or (None, None)."""
    m = re.search(r'\\(?:sub)*section\*?\{References\}', c)
    if not m:
        return None, None
    tail = c[m.start():]
    # The reference list ends at the FIRST thing that is not a reference.
    # Stopping only at Declarations is wrong: paper08 has a Supplementary
    # material section (and a horizontal rule) between the two, and swallowing
    # its prose turns it into a fake "entry" with no year.
    end = len(tail)
    for pat in (r'\\(?:sub)*section\*?\{(?:Declarations|Data [Aa]vailability|'
                r'Declaration of competing)',
                r'\\(?:sub)*section\*?\{Supplementary material\}',
                r'\\begin\{center\}'):
        d = re.search(pat, tail)
        if d and d.start() < end:
            end = d.start()
    return tail[:end], c[:m.start()].count('\n')


def ref_entries(c):
    """Blank-line-delimited reference entries -> [(line_number, text), ...]."""
    blk, off = ref_block(c)
    if blk is None:
        return []
    out, cur, at = [], [], None
    for i, l in enumerate(blk.split('\n')):
        if l.strip():
            if at is None:
                at = i
            cur.append(l.strip())
        else:
            if cur and not cur[0].startswith('\\'):
                out.append((off + at + 1, re.sub(r'\s+', ' ', ' '.join(cur)).strip()))
            cur, at = [], None
    if cur and not cur[0].startswith('\\'):
        out.append((off + at + 1, re.sub(r'\s+', ' ', ' '.join(cur)).strip()))
    return out


def norm_key(e):
    return re.sub(r'[^a-z0-9]', '', e.lower())[:110]


def _norm_text(t):
    """Lowercased, LaTeX-stripped, alphanumeric words -- for title similarity."""
    t = re.sub(r'\\[A-Za-z]+', ' ', t)
    t = t.replace('{', ' ').replace('}', ' ')
    t = t.lower()
    t = re.sub(r'[^a-z0-9 ]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip()


_DOI = re.compile(r'\b(10\.\d{4,9}/[^\s,;"\}]+)', re.I)
# "2016/026", "Rep.~2016/026", "Report 2011/037", "No. 3328", "Circular 1186"
_REPORT = re.compile(
    r'\b(\d{4}/\d{2,4})\b'
    r'|\b(?:rep(?:ort)?\.?|no\.?|circular|advis(?:ory)?)\s*~?\s*'
    r'(\d{1,4}(?:/\d{2,4})?)\b', re.I)


def fingerprints(e):
    """-> set of identity fingerprints for a reference entry.

    A DOI or a report number identifies a work outright. A year alone does
    not, but year + title does.
    """
    fps = set()
    d = _DOI.search(e)
    if d:
        fps.add('doi:' + d.group(1).rstrip('.').lower())
    r = _REPORT.search(e)
    if r:
        v = r.group(1) or r.group(2)
        if v:
            fps.add('rep:' + v.lower())
    y = YEAR.search(e)
    if y:
        fps.add('yr:' + y.group(0))
    return fps


def same_work(a, b):
    r"""Do two entries cite the SAME work?

    This replaces byte-identity, which is the wrong test: two entries citing
    one report routinely differ in citation style and nothing else, so a
    byte comparison reports "they differ" and leaves a human to notice that
    the report number is identical. Identity of work is decided by:

      - a shared DOI, or
      - a shared report number            (decisive either way)
      - else the same year AND >=60% title-token overlap

    The DFO 2016 pair that motivated this was:

        DFO, 2016. Stock Assessment of Northern cod (NAFO Divs. 2J3KL) in
        2016. DFO Can. Sci. Advis. Sec. Sci. Advis. Rep.~2016/026.
        DFO (2016). Stock assessment of Northern cod (NAFO 2J3KL).
        \emph{Can. Sci. Advis. Sec. Sci. Advis. Rep.} 2016/026.

    Not byte-identical. Same report, 2016/026. One work.
    """
    fa, fb = fingerprints(a), fingerprints(b)
    for p in ('doi:', 'rep:'):
        sa = set(x for x in fa if x.startswith(p))
        sb = set(x for x in fb if x.startswith(p))
        if sa and sb:
            # both carry this kind of identifier: agreement is decisive, and
            # so is disagreement
            return bool(sa & sb)
    ya = set(x for x in fa if x.startswith('yr:'))
    yb = set(x for x in fb if x.startswith('yr:'))
    if not (ya and yb and (ya & yb)):
        return False
    ta, tb = set(_norm_text(a).split()), set(_norm_text(b).split())
    if not ta or not tb:
        return False
    return len(ta & tb) / float(len(ta | tb)) >= 0.60


def surname_year(e):
    """First author surname + year, for near-duplicate detection."""
    m = re.match(r'^(.*?)(?:,\s|\.\s)', e + ' ')
    head = m.group(1) if m else e.split(',')[0]
    for a, b in (('\\AA', 'A'), ('\\"o', 'o'), ('\\\'a', 'a'), ('\\\'e', 'e'),
                 ('\\v{s}', 's'), ('\\~a', 'a'), ('\\^e', 'e')):
        head = head.replace(a, b)
    head = re.sub(r'\\[A-Za-z]+', '', head).replace('{', '').replace('}', '')
    head = re.sub(r'[^A-Za-z\- ]', '', head).strip().lower()
    y = re.search(r'\b(?:1[89]\d{2}|20\d{2})\b', e)
    return (head, y.group(0) if y else None)


def scan_structural(path, c, stem):
    """Classes H-L. Returns [(kind, hit, why, line), ...]."""
    out = []

    # H -- more than one Declarations block
    hits = [(c[:m.start()].count('\n') + 1, m.group(0))
            for m in DECL_HEAD.finditer(c)]
    if len(hits) > 1:
        out.append(('H.duplicate-declarations', '%d blocks' % len(hits),
                    'Declarations blocks at lines %s -- collapse to one'
                    % ', '.join(str(h[0]) for h in hits), hits[1][0]))

    # I -- two supplementary-material passages that describe the SAME supplement.
    #
    # A merged paper legitimately carries TWO passages when they point at two
    # different supplementary files (paper08 v46: ..._supplementary_delay.md and
    # ..._supplementary_governance.md -- both files state that both are required,
    # because the main text cites sections from each). Counting passages and
    # failing on >1 therefore flagged a correct merge as broken. A passage is a
    # DUPLICATE only if it describes the same supplement as another one, which is
    # decided by the file it names, or by near-identical wording when it names
    # none.
    supp = []
    for m in SUPP_HEAD.finditer(c):
        tail = c[m.end():]
        nxt = re.search(r'\\(?:sub)*section\*?\{', tail)
        supp.append((c[:m.start()].count('\n') + 1, 'heading',
                     tail[:nxt.start()] if nxt else tail))
    for blk in re.split(r'\n\s*\n', c):
        if SUPP_OPEN.match(blk):
            ln = c[:c.find(blk)].count('\n') + 1 if blk in c else None
            supp.append((ln, 'paragraph opener', blk))

    def _supp_file(text):
        m = re.search(r'\\texttt\{([^}]*supplementary[^}]*)\}', text, re.I)
        return m.group(1).strip() if m else None

    def _tokens(text):
        t = re.sub(r'\\[a-zA-Z]+\*?(?:\{[^}]*\})?', ' ', text)
        t = re.sub(r'[^a-z0-9 ]', ' ', t.lower())
        stop = set('the a an of and or in for with to is are be this that '
                   'these those it its as at on by from we our which material '
                   'supplementary file provided accompanying'.split())
        return set(w for w in t.split() if len(w) > 3 and w not in stop)

    # 1. two passages naming the same file are duplicates
    named = {}
    for ln, kind, text in supp:
        f = _supp_file(text)
        if f:
            named.setdefault(f, []).append((ln, kind))
    dupes = [v for v in named.values() if len(v) > 1]

    # 2. passages naming no file: duplicates only if near-identical wording
    unnamed = [(ln, kind, text) for ln, kind, text in supp if not _supp_file(text)]
    tok = [_tokens(t) for _, _, t in unnamed]
    for i in range(len(unnamed)):
        for j in range(i + 1, len(unnamed)):
            if not tok[i] or not tok[j]:
                continue
            jac = len(tok[i] & tok[j]) / float(len(tok[i] | tok[j]))
            if jac >= 0.6:
                dupes.append([unnamed[i][:2], unnamed[j][:2]])

    # 3. a named passage and an unnamed one that is the same text
    for f, group in named.items():
        for ln, kind, text in unnamed:
            for gln, gkind in group:
                gt = next((t for l, k, t in supp if l == gln and k == gkind), '')
                a, b = _tokens(text), _tokens(gt)
                if a and b and len(a & b) / float(len(a | b)) >= 0.6:
                    dupes.append([(ln, kind), (gln, gkind)])

    if dupes:
        flat = []
        for d in dupes:
            for ln, kind in d:
                if ln is not None and (ln, kind) not in flat:
                    flat.append((ln, kind))
        out.append(('I.duplicate-supplement', '%d passages' % len(flat),
                    'supplementary-material passages at lines %s (%s) -- these '
                    'describe the same supplement; keep one'
                    % (', '.join(str(l) for l, _ in flat),
                       ', '.join(k for _, k in flat)),
                    flat[1][0] if len(flat) > 1 else flat[0][0]))

    # J -- cross-unit file references (comment-stripped, so provenance notes in
    #      % headers are not counted; this is what a READER would see)
    own = re.match(r'paper0?(\d+)', stem)
    own = int(own.group(1)) if own else None
    if own is not None:
        for m in CROSS_UNIT.finditer(c):
            other = int(m.group(1))
            if other != own:
                out.append(('J.cross-unit-ref', m.group(0),
                            'unit %d file referenced inside unit %d -- almost '
                            'certainly merge contamination' % (other, own),
                            c[:m.start()].count('\n') + 1))

    # K -- split bibliography entries
    ents = ref_entries(c)
    for ln, e in ents:
        # a bare publisher/city fragment is a detached tail on its own
        # evidence -- it does not need the "no year" test below, and it does
        # not need to open with a known journal name either.
        # NOTE: CORPORATE is deliberately NOT consulted here. Triage showed
        # PLACE_TAIL alone is 20/20 precise, while adding the corporate guard
        # suppressed five genuine tails -- "Cambridge University Press,
        # Cambridge.", "Eurostat, Luxembourg.", "OECD Publishing, Paris.",
        # "Princeton University Press, Princeton, NJ." and "Fisheries and
        # Oceans Canada, Ottawa." -- because publisher names end in the same
        # words institutional authors do. The guard belongs only on the
        # no-year/no-author signal, where the USGS false positive arose.
        if PLACE_TAIL.match(e) and not YEAR.search(e):
            out.append(('K.place-tail', e[:52],
                        'detached publisher/city tail: no year, and it is the '
                        'place half of an entry whose head is elsewhere', ln))
            continue
        if not YEAR.search(e):
            # Institutional data citations legitimately carry no year
            # ("Statistics Canada. Tables 38-10-0167-01 ...", "World Bank.
            # Poverty and Inequality Platform. ..."), so a missing year alone is
            # not enough: the fragment must also LOOK like the tail of a
            # reference -- a journal/publisher opener or a bare DOI.
            if TAIL_LEAD.match(e) or 'doi:' in e.lower():
                out.append(('K.split-refs', e[:52],
                            'detached tail: no year, and it is the '
                            'journal/publisher half of an entry whose head is '
                            'elsewhere', ln))
        elif GLUED.search(e):
            g = GLUED.search(e)
            out.append(('K.split-refs', (e[:26] + ' ... ' + g.group(0))[:52],
                        'glued: end of one reference runs into the next author '
                        'head with no separating period', ln))
        elif TAIL_LEAD.match(e):
            out.append(('K.split-refs', e[:52],
                        'entry opens with a journal/publisher token, not an author',
                        ln))

    # L -- duplicate bibliography keys
    seen = {}
    for ln, e in ents:
        k = norm_key(e)
        if k in seen:
            out.append(('L.dup-ref', e[:52],
                        'identical to the entry at L%d' % seen[k], ln))
        else:
            seen[k] = ln
    bykey = {}
    for ln, e in ents:
        k = surname_year(e)
        if k[1] is None:
            continue
        if k in bykey:
            prev_ln, prev_txt = bykey[k]
            # Same author and year is NOT enough to call two entries a
            # duplicate: an author legitimately publishes two things in a
            # year, and flagging those was most of this rule's output. It now
            # fires only when the two entries are the same WORK by the
            # semantic test (shared DOI, shared report number, or same year
            # plus title overlap). That makes the finding actionable --
            # "merge these", not "go and check whether these conflict".
            if same_work(prev_txt, e):
                out.append(('L.dup-ref-key', '%s %s' % k,
                            'same author+year as L%d and the SAME WORK '
                            '(shared DOI, report number, or year+title) -- '
                            'merge to one entry' % prev_ln, ln))
            # keep the FIRST entry as the comparison point
            continue
        bykey[k] = (ln, e)
    return out


def merge_gate(path):
    """Structural gate for merge scripts. Returns [] if the file is sound.

    Call this at the end of every merge_*.py and abort the write if it returns
    anything -- otherwise the next re-merge silently regenerates the damage.
    """
    return gate_text(io.open(path, encoding='utf-8', errors='replace').read(),
                     os.path.basename(path))


# L.dup-ref-key is deliberately NOT fatal. Verified 2026-10-01: paper11 carries
# four DIFFERENT Abaee 2026 works (one-pool water balance, periodic review as
# sampled governance, robust viability of 2J3KL, obstruction calculus) and
# paper08 carries two different DFO 2024 documents (a news release and a CSAS
# stock assessment). Those are legitimate same-author-same-year bibliographies
# that need a/b/c/d letters -- real, but not merge damage, and not grounds to
# refuse to emit the file.
FATAL = frozenset(['H.duplicate-declarations', 'I.duplicate-supplement',
                   'K.place-tail',
                   'J.cross-unit-ref', 'K.split-refs', 'L.dup-ref'])


def gate_text(text, stem):
    """Same gate, applied to a document string before it is written.

    Merge scripts assemble the whole document in memory, so they can gate it
    before touching the filesystem. Only FATAL classes are returned.
    """
    c = strip_comments(text)
    return [f for f in scan_structural(stem, c, stem) if f[0] in FATAL]


# --------------------------------------------------------------------------
# live-head classification
#
# Merging always writes a NEW version, so an old version is never re-merged
# and nobody will ever repair it. Counting it as a gate failure is how a gate
# trains people to ignore it: the same handful of dead files fail on every run,
# forever. Superseded files are reported as INFORMATIONAL and never counted.
VERSIONED = re.compile(r'^(paper\d+[a-z]*_[a-z_]+)_v(\d+)\.tex$')


def live_heads(files):
    """-> set of the newest version of each paper family.

    Files that do not match the versioned pattern (supplementary .tex, and
    any other unversioned artifact) are treated as live, since nothing
    supersedes them.
    """
    best = {}
    for f in files:
        m = VERSIONED.match(f)
        if not m:
            continue
        fam, ver = m.group(1), int(m.group(2))
        if fam not in best or ver > best[fam][0]:
            best[fam] = (ver, f)
    return set(v[1] for v in best.values())


def classify(files):
    """-> [(filename, 'live' | 'superseded'), ...]"""
    live = live_heads(files)
    out = []
    for f in files:
        m = VERSIONED.match(f)
        out.append((f, 'superseded' if (m and f not in live) else 'live'))
    return out


def report_gate(hits, what):
    """Print gate failures and raise SystemExit(1). Called by the merge scripts."""
    if not hits:
        return
    print("\n" + "=" * 72)
    print("MERGE GATE FAILED — %d structural defect(s) in %s" % (len(hits), what))
    print("=" * 72)
    print("The merged artifact was produced broken. Repairing the .tex is")
    print("temporary: the next re-merge regenerates every one of these.")
    print("Fix merge_08_07.py / mergelib.py (or the source), then re-run.\n")
    for kind, hit, why, ln in hits:
        print("  [%-26s] %-22s %-7s %s"
              % (kind, str(hit)[:22], 'L%s' % ln if ln else '-', why))
    raise SystemExit(1)


def scan(path):
    raw = io.open(path, encoding='utf-8', errors='replace').read()
    c = strip_comments(raw)
    stem = os.path.basename(path)
    key = re.match(r'(paper\d+\w*)', stem)
    key = key.group(1) if key else stem
    out = []

    # positive check: the paper discloses its own verification limits
    for pat, why in DISCLOSED_MARKERS:
        if re.search(pat, c, re.I):
            out.append(('OK.disclosed', 'present', why, None))

    for pat, why in STALE:
        for m in re.finditer(pat, c, re.I):
            lo = max(0, m.start() - CONTEXT_WINDOW)
            hi = min(len(c), m.end() + CONTEXT_WINDOW)
            ctx = c[lo:hi]
            excuses = CONTEXT_EXCUSE.get(pat, [])
            if excuses and all(re.search(e, ctx, re.I) for e in excuses):
                # disclosed on purpose -> not a defect
                out.append(('OK.disclosed-not-defect', m.group(0),
                            '%s — but the paper states the current value and the caveat '
                            'beside it' % why, c[:m.start()].count('\n') + 1))
                continue
            out.append(('A.stale', m.group(0), why, c[:m.start()].count('\n') + 1))

    for num, why in HYBRID_BAD.items():
        if num in c:
            out.append(('B.hybrid', num, why, find_line(c, num)))

    for pat, why in ILLCOND:
        n = len(re.findall(pat, c, re.I))
        if n:
            # does the band appear anywhere in the paper?
            banded = bool(re.search(r'0\.87|10\.67', c))
            out.append(('G.illcond' if not banded else 'G.illcond(band present)',
                        '%d bare' % n, why, find_line(c, re.search(pat, c, re.I).group(0))))

    for kw, why in MUST_CITE.get(key, []):
        if not re.search(kw, c, re.I):
            out.append(('F.priorart', 'ABSENT: %s' % kw, why, None))

    # (F') sharper: Doyen is cited 12x but only as the APPLIED author. The 2000
    # output-feedback paper is the nearest neighbour and must appear by venue/year.
    if key == 'paper01':
        has_2000 = bool(re.search(
            r'Doyen[^\n]{0,80}(?:2000)|Set-Valued Analysis\s*\**8', c, re.I))
        if not has_2000:
            out.append(('F.priorart', 'Doyen 2000 absent',
                        'cites Doyen the applied author, not the output-feedback theorist',
                        None))

    # (D) abstract selection: numbers in the abstract vs the body
    for env in ('abstract',):
        m = re.search(r'\\begin\{%s\}(.*?)\\end\{%s\}' % (env, env), c, re.S)
        if not m:
            continue
        ab = m.group(1)
        body = c[:m.start()] + c[m.end():]
        for num in sorted(set(re.findall(r'(?<![\w.])-?\d+\.\d{2,}', ab)), key=len, reverse=True)[:12]:
            if num not in body:
                out.append(('D.abstract-only', num,
                            'in abstract but nowhere in body', find_line(c, num)))

    # (H-L) structural gate
    out.extend(scan_structural(path, c, stem))

    return out


GATE = ('H', 'I', 'J', 'K', 'L')


def main():
    args = [a for a in sys.argv[1:]]
    gate_only = '--gate' in args
    quiet = '--quiet' in args
    files = sorted(f for f in os.listdir(PAPERS) if f.endswith('.tex'))

    if gate_only:
        # merge output gate: H-L only.
        #
        # Two things this used to get wrong, both of which made the number
        # untrustworthy:
        #   1. it counted FINDINGS but printed them as "failure(s)", so a run
        #      reporting "32" and a count of "12 failing files" looked like a
        #      contradiction when they were different units. Both are printed.
        #   2. it failed on superseded versions, which nobody will ever fix.
        #      Only LIVE HEADS count toward the exit status now.
        rows = []
        for f, status in classify(files):
            hits = merge_gate(PAPERS + f)
            if hits:
                rows.append((f, status, hits))

        for f, status, hits in rows:
            tag = ('STRUCTURAL GATE FAILED' if status == 'live'
                   else 'informational (superseded, not counted)')
            print("  %-46s %s — %d finding(s)" % (f, tag, len(hits)))
            for kind, hit, why, ln in hits:
                print("      [%-26s] %-14s %-6s %s"
                      % (kind, str(hit)[:14], 'L%s' % ln if ln else '-', why))

        live_rows = [r for r in rows if r[1] == 'live']
        dead_rows = [r for r in rows if r[1] == 'superseded']
        live_files = len(live_rows)
        live_findings = sum(len(r[2]) for r in live_rows)
        dead_files = len(dead_rows)
        dead_findings = sum(len(r[2]) for r in dead_rows)

        print()
        print("LIVE HEADS failing  : %d file(s), %d finding(s)   <-- exit status"
              % (live_files, live_findings))
        print("superseded, ignored : %d file(s), %d finding(s)"
              % (dead_files, dead_findings))
        print("scanned             : %d file(s)" % len(files))
        sys.exit(1 if live_findings else 0)

    print("Phase 0 sweep — %d .tex files (all sources AND merged outputs)\n" % len(files))
    total, gate = 0, 0
    for f in files:
        res = scan(PAPERS + f)
        if not res:
            print("  %-46s clean" % f)
            continue
        print("  %-46s %d finding(s)" % (f, len(res)))
        for kind, hit, why, ln in res:
            loc = 'L%s' % ln if ln else '-'
            print("      [%-26s] %-14s %-6s %s" % (kind, str(hit)[:14], loc, why))
            if kind[:1] in GATE:
                gate += 1
        total += len(res)
    print("\nTOTAL: %d findings" % total)
    if gate:
        # A structural finding means the artifact was produced broken. Repairing
        # the .tex is temporary -- the next re-merge regenerates it. Fail loudly.
        print("STRUCTURAL FAILURES (H-L): %d — fix the merge script, not the output"
              % gate)
        sys.exit(1)


if __name__ == '__main__':
    main()

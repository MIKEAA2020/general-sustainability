#!/usr/bin/env python3
"""
Automated journal-style scan — implements previous prompt:
- Companion papers ARE citable (with DOI), superseded manuscript versions never published -> no reference
- No change-log / diary / project report / implementation summary
- No reference to earlier mistakes unless strong pedagogical/methodological value, and even then no reference to unpublished versions
- Can debunk literature with citation, no phantom/strawman or unpublished work
- No editorial, self-praise, self-commentary, informal chat terms
- Formal academic conventions
- Strip metaphor apology / "map is not territory" over-hedging, keep legitimate scope
- Scan navigation/diary/hedging and methodological self-description
- Scan scientific/pedagogical/expository content for lost/condensed content

Checks all types of meta-commentary, including methodological ones.
"""
import re, pathlib, sys

FILE = sys.argv[1] if len(sys.argv) > 1 else "framework/paperF1_retention_framework_v10.md"
text = pathlib.Path(FILE).read_text()

checks = {
    "BLOCKER_version_ref": {
        "desc": "No reference to unpublished/superseded versions",
        "pat": r"\b(SPECIFICATION_v\d+\.md|paperE1_cod_forecast_ladder_v\d+|paperE3_edwards_forecast_ladder_v\d+|v\d+ reported|earlier versions of this article|previous draft|as printed in the source|Framework artefact v\d+|deep scan of entire workspace)\b",
        "type": "BLOCKER"
    },
    "BLOCKER_self_correction": {
        "desc": "No self-correction narrative (silently state correct result)",
        "pat": r"\b(withdrawn|that was an error.*corrected here|we previously stated|this has been fixed|previously wrong|was wrong|was correct.*previously|neither is reconciled here)\b",
        "type": "BLOCKER"
    },
    "BLOCKER_phantom": {
        "desc": "No phantom/strawman contrasts against unpublished work",
        "pat": r"\b(naive positions nobody holds|unpublished work|previous versions of the manuscript|in review|in preparation|under separate review|forthcoming)\b",
        "type": "BLOCKER"
    },
    "BLOCKER_diary": {
        "desc": "No project-diary register",
        "pat": r"\b(in this pass|post-freeze layer|freeze-discipline record|pre-score protocol file|the machine layer|this round|we then implemented|deep scan|framework artefact|condition \d+ discharged|condition \d+ satisfied|Tier [ABC]|Appropriate path|Preserves|no overwrite|byte-identical|30/30|29/29|checksum|seeded deterministic|import check|verification gate|manuscript_style_scan|tier3_guard|clip-binding|load-bearing conclusion|independent rerun|different toolchain|determinism two consecutive|present_file tool|v\d+ preserved)\b",
        "type": "BLOCKER"
    },
    "BLOCKER_project_diary_methodological": {
        "desc": "No methodological self-description / project diary (including methodological meta-commentary)",
        "pat": r"\b(Sheet status: PRE-REGISTRATION|NO SIMULATION RUN|Issued 10 Sep|Nothing executed|If any element changes|dated amendment|exploratory|does not amend, relax, supersede|Every v2 verdict|No number in Tables|Distinct from SPECIFICATION|adds no module|re-uses existing|varies only data|cost \d+ s/pass|200 fixed now|95% interval on proportion|Must be reported in abstract per Amendment|interpretation fixed before execution|Method lesson|Most consequential finding|Appropriate next action|plan needs explicit stopping condition|presenting whichever more flattering)\b",
        "type": "BLOCKER"
    },
    "BLOCKER_editorial": {
        "desc": "No editorial/self-praise/self-assessment",
        "pat": r"\b(this is a strength|the paper is honest|the paper is rigorous|the paper is careful|we are careful to|this paper guards against|novel|unprecedented|state-of-the-art)\b",
        "type": "BLOCKER"
    },
    "BLOCKER_metaphor_apology": {
        "desc": "No metaphor apologies / naive over-hedging (map is not territory)",
        "pat": r"\b(the metaphor is not an empirical claim|this needs one sentence, not a parable|the narrative that usually carries the point|should not be taken literally|is only an analogy|Note: The map is not the actual territory|map is not the territory|Readers inherently understand that an orchard is not)\b",
        "type": "BLOCKER"
    },
    "REVIEW_coinage": {
        "desc": "Project-internal coinage — define once or use plain term",
        "pat": r"\b(machine layer|observation fibre|class-level incompatibility|safe-set map|specification-matching discipline)\b",
        "type": "REVIEW"
    },
    "REVIEW_intensifier": {
        "desc": "Editorial intensifiers",
        "pat": r"\b(Importantly|Notably|Crucially|It is worth noting)\b",
        "type": "REVIEW"
    },
}

blockers = 0
reviews = 0
for name, cfg in checks.items():
    hits = list(re.finditer(cfg["pat"], text, flags=re.IGNORECASE))
    if hits:
        if cfg["type"] == "BLOCKER":
            blockers += len(hits)
            print(f"\n[BLOCKER] {name}: {cfg['desc']} — {len(hits)} hits")
            for m in hits[:5]:
                ctx = text[max(0,m.start()-50):m.start()+80].replace("\n"," ")
                print(f"  ...{ctx}...")
        else:
            reviews += len(hits)
            print(f"\n[REVIEW] {name}: {cfg['desc']} — {len(hits)} hits")

print(f"\n=== Summary ===\nBlockers: {blockers}\nReviews: {reviews}")
if blockers == 0:
    print("PASS — journal conventions met")
    sys.exit(0)
else:
    print("FAIL — blockers must be removed")
    sys.exit(1)

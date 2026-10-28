#!/usr/bin/env bash
# Refresh the v77 SHA-256 manifest; run from any directory.
set -euo pipefail
PACKAGE="$(cd "$(dirname "$0")" && pwd)"
MANIFEST="$PACKAGE/SHA256SUMS_v77.txt"
TMP="$MANIFEST.tmp"
cd "$PACKAGE"
{
  find QA_v77 paper06_assessment_separation_v77_src -type f -print0
  printf '%s\0' \
    README_v77.md \
    CHANGELOG_v76_to_v77.md \
    EDITORIAL_REVISION_PLAN_v77.md \
    IMPLEMENTATION_RECORD_v77.md \
    assemble_v77.py \
    build_v77.sh \
    checksum_v77.sh \
    paper06_assessment_separation_v77.tex \
    paper06_assessment_separation_v77.pdf \
    paper06_assessment_separation_v77.log \
    paper06_assessment_separation_v77_supplementary.tex \
    paper06_assessment_separation_v77_supplementary.pdf \
    paper06_assessment_separation_v77_supplementary.log
} | sort -zu | xargs -0 sha256sum > "$TMP"
mv "$TMP" "$MANIFEST"
printf 'Wrote %s\n' "$MANIFEST"

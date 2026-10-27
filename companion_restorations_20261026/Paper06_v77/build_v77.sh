#!/usr/bin/env bash
# Reproducible local build for Paper06 v77. Run from any directory.
set -euo pipefail

PACKAGE="$(cd "$(dirname "$0")" && pwd)"
TEX_ENGINE="${TEX_ENGINE:-tectonic}"
QA="$PACKAGE/QA_v77"
mkdir -p "$QA"

# Start from clean TeX state; the SI imports the freshly built main .aux file.
rm -f \
  "$PACKAGE/paper06_assessment_separation_v77.aux" \
  "$PACKAGE/paper06_assessment_separation_v77.out" \
  "$PACKAGE/paper06_assessment_separation_v77.spl" \
  "$PACKAGE/paper06_assessment_separation_v77.xdv" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.aux" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.out" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.spl" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.xdv"

python3 "$PACKAGE/assemble_v77.py"
"$TEX_ENGINE" --version | tee "$QA/tectonic.version.txt"

# Compile the main article first: the SI imports its labels through xr.
(
  cd "$PACKAGE"
  "$TEX_ENGINE" --keep-logs --keep-intermediates paper06_assessment_separation_v77.tex
) 2>&1 | tee "$QA/build_main.stdout.log"
(
  cd "$PACKAGE"
  "$TEX_ENGINE" --keep-logs --keep-intermediates paper06_assessment_separation_v77_supplementary.tex
) 2>&1 | tee "$QA/build_si.stdout.log"

cp "$PACKAGE/paper06_assessment_separation_v77.log" "$QA/main.tex.log"
cp "$PACKAGE/paper06_assessment_separation_v77_supplementary.log" "$QA/supplementary.tex.log"

# Keep the source, PDFs, and QA logs; discard only TeX's reproducible scratch files.
rm -f \
  "$PACKAGE/paper06_assessment_separation_v77.aux" \
  "$PACKAGE/paper06_assessment_separation_v77.out" \
  "$PACKAGE/paper06_assessment_separation_v77.spl" \
  "$PACKAGE/paper06_assessment_separation_v77.xdv" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.aux" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.out" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.spl" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.xdv"

printf 'Built v77 main and supplementary PDFs in %s\n' "$PACKAGE"

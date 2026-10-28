#!/usr/bin/env bash
# Reproducible local build for Paper06 v77. Run from any directory.
set -euo pipefail

PACKAGE="$(cd "$(dirname "$0")" && pwd)"
if [[ -n "${TEX_ENGINE:-}" ]]; then
  TEX_ENGINE="$TEX_ENGINE"
elif command -v tectonic >/dev/null 2>&1; then
  TEX_ENGINE="$(command -v tectonic)"
else
  TEX_ENGINE="$(command -v pdflatex)"
fi
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
: > "$QA/build_main.stdout.log"
: > "$QA/build_si.stdout.log"

python3 "$PACKAGE/assemble_v77.py"
"$TEX_ENGINE" --version | tee "$QA/tex_engine.version.txt"

if [[ "$TEX_ENGINE" == *tectonic* ]]; then
  # Tectonic resolves references internally; compile the main article before SI.
  (
    cd "$PACKAGE"
    "$TEX_ENGINE" --keep-logs --keep-intermediates paper06_assessment_separation_v77.tex
  ) 2>&1 | tee -a "$QA/build_main.stdout.log"
  (
    cd "$PACKAGE"
    "$TEX_ENGINE" --keep-logs --keep-intermediates paper06_assessment_separation_v77_supplementary.tex
  ) 2>&1 | tee -a "$QA/build_si.stdout.log"
else
  # pdfLaTeX needs repeated passes for references, citations, and imported main labels.
  for pass in 1 2 3; do
    printf 'Main pdfLaTeX pass %s/3\n' "$pass" | tee -a "$QA/build_main.stdout.log"
    (
      cd "$PACKAGE"
      "$TEX_ENGINE" -interaction=nonstopmode -halt-on-error -file-line-error paper06_assessment_separation_v77.tex
    ) 2>&1 | tee -a "$QA/build_main.stdout.log"
  done
  for pass in 1 2 3; do
    printf 'SI pdfLaTeX pass %s/3\n' "$pass" | tee -a "$QA/build_si.stdout.log"
    (
      cd "$PACKAGE"
      "$TEX_ENGINE" -interaction=nonstopmode -halt-on-error -file-line-error paper06_assessment_separation_v77_supplementary.tex
    ) 2>&1 | tee -a "$QA/build_si.stdout.log"
  done
fi

cp "$PACKAGE/paper06_assessment_separation_v77.log" "$QA/main.tex.log"
cp "$PACKAGE/paper06_assessment_separation_v77_supplementary.log" "$QA/supplementary.tex.log"

# Keep the source, PDFs, and QA logs; discard only reproducible TeX scratch files.
rm -f \
  "$PACKAGE/paper06_assessment_separation_v77.aux" \
  "$PACKAGE/paper06_assessment_separation_v77.out" \
  "$PACKAGE/paper06_assessment_separation_v77.spl" \
  "$PACKAGE/paper06_assessment_separation_v77.xdv" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.aux" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.out" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.spl" \
  "$PACKAGE/paper06_assessment_separation_v77_supplementary.xdv"

printf 'Built main and Supplementary Information PDFs in %s\n' "$PACKAGE"

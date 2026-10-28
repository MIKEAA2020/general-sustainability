#!/usr/bin/env bash
# Assemble and build the separate local ECOMOD Continued 11 draft.
set -euo pipefail

PACKAGE="$(cd "$(dirname "$0")" && pwd)"
ENGINE="${TEX_ENGINE:-pdflatex}"
QA="$PACKAGE/output_submission_cleanup_20261028"
MAIN="ecomod_continued_11_revision_draft_20261028"
SI="ecomod_continued_11_revision_draft_20261028_SI"
mkdir -p "$QA"

cd "$PACKAGE"
python3 assemble.py
python3 check_c11_sources.py
"$ENGINE" --version > "$QA/tex_engine.version.txt" 2>&1

rm -f "$MAIN.aux" "$MAIN.out" "$MAIN.spl" "$MAIN.toc" \
      "$SI.aux" "$SI.out" "$SI.spl" "$SI.toc"

for pass in 1 2 3; do
  "$ENGINE" -interaction=nonstopmode -halt-on-error -file-line-error "$MAIN.tex" \
    > "$QA/main_pass${pass}.stdout.log" 2>&1
  cp "$MAIN.log" "$QA/main_pass${pass}.log"
done

for pass in 1 2 3; do
  "$ENGINE" -interaction=nonstopmode -halt-on-error -file-line-error "$SI.tex" \
    > "$QA/si_pass${pass}.stdout.log" 2>&1
  cp "$SI.log" "$QA/si_pass${pass}.log"
done

cp "$MAIN.log" "$QA/main_final.log"
cp "$SI.log" "$QA/si_final.log"
python3 check_c11_sources.py > "$QA/source_checker_final.log" 2>&1

# Retain the assembled sources and PDFs, and discard only reproducible TeX scratch files.
rm -f "$MAIN.aux" "$MAIN.out" "$MAIN.spl" "$MAIN.toc" "$MAIN.log" \
      "$SI.aux" "$SI.out" "$SI.spl" "$SI.toc" "$SI.log"
printf 'Built %s.pdf and %s.pdf with %s\n' "$MAIN" "$SI" "$ENGINE"

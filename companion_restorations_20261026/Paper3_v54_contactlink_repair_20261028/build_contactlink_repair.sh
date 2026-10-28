#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
ENGINE="${TEX_ENGINE:-pdflatex}"
TEX="paper3_material_ledgers_v54_contactlink_repair_20261028"
mkdir -p "$DIR/QA"
cd "$DIR"
rm -f "$TEX.aux" "$TEX.out" "$TEX.toc"
"$ENGINE" --version > QA/tex_engine.version.txt 2>&1
for pass in 1 2 3; do
  "$ENGINE" -interaction=nonstopmode -halt-on-error -file-line-error "$TEX.tex" \
    > "QA/pass${pass}.stdout.log" 2>&1
  cp "$TEX.log" "QA/pass${pass}.log"
done
cp "$TEX.log" QA/final.log
rm -f "$TEX.aux" "$TEX.out" "$TEX.toc"
printf 'Built %s.pdf with %s\n' "$TEX" "$ENGINE"

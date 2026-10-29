#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .cache/tex
python code/prepare_revision_C18_A01.py
for kind in main SI; do
  for pass in 1 2 3; do
    pdflatex -interaction=nonstopmode -halt-on-error -output-directory=.cache/tex "ecomod_C18_A01_${kind}.tex" > "evidence/tex_${kind}_pass${pass}_C18_A01.txt" 2>&1
  done
  cp ".cache/tex/ecomod_C18_A01_${kind}.pdf" .
  cp ".cache/tex/ecomod_C18_A01_${kind}.log" "evidence/tex_${kind}_final_C18_A01.log"
done

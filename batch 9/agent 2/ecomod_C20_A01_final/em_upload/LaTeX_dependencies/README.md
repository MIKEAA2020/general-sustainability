# LaTeX build dependencies (optional upload)

These are the figure PDFs and `\input` table fragments that the manuscript and SI sources reference by
relative path (`figures/`, `tables/`, `inherited_C17/...`). Editorial Manager does not compile LaTeX, so you
do **not** need to upload this folder: the submitted PDFs are complete. It is included so that the `.tex`
sources in this folder can be compiled by anyone who wants to check typesetting, e.g.:

    cp Manuscript_ECOMOD_C20_A01.tex Supplementary_Information_ECOMOD_C20_A01.tex LaTeX_dependencies/
    cd LaTeX_dependencies && pdflatex -interaction=nonstopmode Manuscript_ECOMOD_C20_A01.tex   # x3

Bibliographies are embedded; no BibTeX step is required.

# Build the ECOMOD v34 manuscript with the correct engine (LuaLaTeX).
#   make          -> build PDF (latexmk -lualatex)
#   make view     -> build then open the PDF
#   make clean    -> remove build artifacts
#
# NOTE: this document uses fontspec + unicode-math, so it MUST be LuaLaTeX.
# pdfLaTeX (pdflatex / latex) will fail. Do not use them.

MAIN   := manuscript_ECOMOD_v34
ENGINE := lualatex

.PHONY: all view clean

all:
	latexmk -$(ENGINE) $(MAIN).tex

view: all
	$(if $(wildcard $(MAIN).pdf),open $(MAIN).pdf,xdg-open $(MAIN).pdf)

clean:
	latexmk -C $(MAIN).tex
	rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).synctex.gz $(MAIN).fdb_latexmk $(MAIN).fls

LATEX = latexmk -pdf -g -outdir=docs
RM = rm -rfv

%.pdf: %.tex ./%/*/*.tex references.bib
	$(LATEX) $<

all: PythonEssentials.pdf DataScienceEssentials.pdf Volume1.pdf Volume2.pdf Volume3.pdf Volume4.pdf GettingStarted.pdf

GettingStarted.pdf: GettingStarted.tex Appendices/Setup/SetupStudent.tex
	$(LATEX) $<

clean:
	bash .clean.sh

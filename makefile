all: exam/MNUM_resol_exam.pdf tests/1/MNUM_resol_teste1.pdf tests/2/MNUM_resol_teste2.pdf

%.pdf: %.tex
	cd $(<D) && latexmk -interaction=nonstopmode -pdf $(<F)

clean:
	cd exam    && latexmk -C
	cd tests/1 && latexmk -C
	cd tests/2 && latexmk -C

cleanall:
	git clean -dfX

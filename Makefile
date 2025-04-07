all: blue.htm wj.htm defense.htm
	@:

%.htm: %.bml %/*.bml common/*.bml
	bml2html $<

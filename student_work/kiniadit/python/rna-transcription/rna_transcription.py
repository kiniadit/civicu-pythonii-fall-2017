import re
def to_rna(dna_strand):
	if re.findall('[^ATGCatgc]+',dna_strand):
		return ''

from utils import *

# data = '>Rosalind_99\nAGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'

data = dna_to_rna(parse_fasta(data, first=True))
data_rev = reverse_complement(data)
strs = set()
for strand in data, data_rev:
	for start in range(len(strand) - 3):
		if strand[start:start + 3] == 'AUG':
			candidate = 'M'
			for codon in [strand[n:n + 3] for n in range(start + 3, len(strand), 3)]:
				if codon not in codon_table:
					break
				if codon_table[codon] == 'Stop' and len(candidate):
					strs.add(candidate)
					break
				else:
					candidate += codon_table[codon]
save('\n'.join(strs))

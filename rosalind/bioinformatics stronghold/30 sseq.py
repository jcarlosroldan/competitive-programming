from utils import *

# data = ">Rosalind_14\nACGTACGTGACG\n>Rosalind_18\nGTA"
dna, motif = list(parse_fasta(data).values())

inds = []
last_ind = 0
for b in motif:
	last_ind += 1 + dna[last_ind + 1:].index(b)
	inds.append(last_ind)

save(' '.join(str(i + 1) for i in inds))
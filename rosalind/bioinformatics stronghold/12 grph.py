from utils import *

# data = '>Rosalind_0498\nAAATAAA\n>Rosalind_2391\nAAATTTT\n>Rosalind_2323\nTTTTCCC\n>Rosalind_0442\nAAATCCC\n>Rosalind_5013\nGGGTGGG'

overlap = 3
data = list(parse_fasta(data).items())
edges = []
for n1, (label1, dna1) in enumerate(data, 1):
	for label2, dna2 in data[n1:]:
		if dna1[-overlap:] == dna2[:overlap]:
			edges.append((label1, label2))
		if dna2[-overlap:] == dna1[:overlap]:
			edges.append((label2, label1))
save('\n'.join('%s %s' % (label1, label2) for label1, label2 in edges))
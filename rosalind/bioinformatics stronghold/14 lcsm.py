from utils import *

# data = '>Rosalind_1\nGATTACA\n>Rosalind_2\nTAGACCA\n>Rosalind_3\nATACCA'

dnas = list(parse_fasta(data).values())

def lcs(base=''):
	res = None
	if all(base in dna for dna in dnas):
		for symbol in 'ACGT':
			sub = lcs(base + symbol)
			if sub and (res is None or len(sub) > len(res)):
				res = sub
		if res is not None:
			return res
		return base

print(lcs())
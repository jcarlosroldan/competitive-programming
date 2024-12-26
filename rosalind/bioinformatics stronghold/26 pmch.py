from utils import *
from math import factorial

# data = '>Rosalind_23\nAGCUAGUCAU'

dna = parse_fasta(data, first=True)
G, U, C, A = (dna.count(base) for base in 'GUCA')

if G == C and A == U:
	save(factorial(G) * factorial(A))
else:
	save(0)
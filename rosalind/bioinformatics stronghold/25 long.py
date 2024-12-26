from utils import *
from math import ceil

# data = '>Rosalind_56\nATTAGACCTG\n>Rosalind_57\nCCTGCCGGAA\n>Rosalind_58\nAGACCTGCCG\n>Rosalind_59\nGCCGGAATAC'

def joins(str1, str2):
	''' Dataset ensures that minimum overlap is more than half their length. '''
	res = set()
	max_overlap = min(len(str1), len(str2))
	for overlap in range(ceil(max_overlap / 2), max_overlap + 1):
		if str1[-overlap:] == str2[:overlap]:
			res.add(str1[:-overlap] + str2)
		if str2[-overlap:] == str1[:overlap]:
			res.add(str2[:-overlap] + str1)
	return res

class GenomeAssembler(DynProg):
	""" Simple child class to give an example of use. Solves N-Queens problems
	using dynamic programming. """
	def __init__(self, reads):
		self.initial_state = [reads[0], reads[1:]]

	def alternatives(self, state):
		for s1, str1 in enumerate(state[1]):
			for join in joins(state[0], str1):
				yield [join, [str2 for s2, str2 in enumerate(state[1]) if s2 != s1]]

	def is_final(self, state):
		return len(state[1]) == 0

	def penalty(self, state):
		return len(state[0]) + sum(len(r) for r in state[1])

ga = GenomeAssembler(list(parse_fasta(data).values()))
res = ga.solve(DynProg.ONE_OPTIMAL_SOLUTION)
save(res[0])
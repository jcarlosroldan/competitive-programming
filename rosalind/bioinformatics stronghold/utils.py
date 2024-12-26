from collections import OrderedDict
from os.path import basename, exists
from sys import argv

num, problem_id = basename(argv[0])[:-3].split(' ')
file = 'input/rosalind_%s.txt' % problem_id
if exists(file):
	with open(file, 'r', encoding='utf-8') as fp:
		data = fp.read().strip()
else:
	print('No data file found. You can set your own data.')

def save(res, print_output=True):
	res = str(res)
	if print_output:
		print('=== begin %s ===\n%s\n=== end %s ===' % (problem_id, res, problem_id))
	with open('output/%s %s.txt' % (num, problem_id), 'w', encoding='utf-8') as fp:
		fp.write(res)

# --- useful functions --------------------------------------------------------

codon_table = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V', 'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V', 'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', 'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', 'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', 'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', 'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', 'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}
monoisotopic_mass_table = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}
monoisotopic_mass_water = 18.01056

def parse_fasta(data_string, first=False):
	dnas = OrderedDict()
	current_dna = None
	for line in data_string.split('\n'):
		if line.startswith('>'):
			current_dna = line[1:].strip()
			dnas[current_dna] = ''
		else:
			dnas[current_dna] += line.strip()
	if first:
		dnas = next(iter(dnas.values()))
	return dnas

def dna_to_rna(dna):
	return dna.replace('T', 'U')

def rna_to_dna(rna):
	return rna.replace('U', 'T')

def rna_to_protein(rna):
	return ''.join(codon_table[rna[n:n + 3]] for n in range(0, len(rna), 3)).strip('Stop')

def reverse_complement(dna, is_rna=True):
	if is_rna:
		return dna.translate(str.maketrans('GUCA', 'CAGU'))[::-1]
	else:
		return dna.translate(str.maketrans('GTCA', 'CAGT'))[::-1]

def print_matrix(matrix, rows=None, cols=None, elem_width=None, separator=' '):
	for row in matrix[:rows]:
		for col in row[:cols]:
			print(str(col)[:elem_width], end=separator)
		print()

class DynProg:
	""" Abstract class to solve problems using dynamic programming. To use it,
	make a child class implementing alternatives, is_final and penalty. Then,
	make one of such objects providing the initial state in the constructor, and
	call to solve(), providing one search type. """
	ONE_SOLUTION = 0
	ONE_OPTIMAL_SOLUTION = 1
	ALL_SOLUTIONS = 2
	ALL_OPTIMAL_SOLUTIONS = 3

	def __init__(self, initial_state):
		self.initial_state = initial_state

	def alternatives(self, state):
		raise NotImplementedError("This should return all the alternatives for a given state, without modifying the given state.")

	def is_final(self, state):
		raise NotImplementedError("This should return whether a state is a final state or not.")

	def penalty(self, state):
		raise NotImplementedError("This should return an upper bound for the penalty of the problem. Ideally, optimal solutions should have no penalty.")

	def solve(self, search_type=ONE_SOLUTION):
		assert search_type in range(4), "Invalid search type."
		final_states = []
		explored = []
		remaining = [(self.penalty(self.initial_state), self.initial_state)]
		while len(remaining):
			_, state = remaining.pop(0)
			explored.append(state)
			for alternative in self.alternatives(state):
				if alternative in explored: continue
				penalty = self.penalty(alternative)
				if self.is_final(alternative):
					if search_type == self.ONE_SOLUTION or penalty == 0 and search_type == self.ONE_OPTIMAL_SOLUTION:
						return alternative
					else:
						final_states.append((penalty, alternative))
				else:
					index = sum(1 for p, _ in remaining if p < penalty)
					remaining.insert(index, (penalty, alternative))
		if search_type == self.ALL_SOLUTIONS:
			return [state for _, state in final_states]
		else:
			min_penalty = min([penalty for penalty, _ in final_states])
			optimals = [state for penalty, state in final_states if penalty == min_penalty]
			if search_type == self.ALL_OPTIMAL_SOLUTIONS:
				return optimals
			else:
				return optimals[0]
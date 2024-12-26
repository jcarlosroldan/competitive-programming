from utils import *

# data = '>Rosalind_0209\nGCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA\nAGTACGGGCATCAACCCAGTT\n>Rosalind_2200\nTTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC\nGGTACGAGTGTTCCTTTGGGT'
data = list(parse_fasta(data).values())

_rings = {'A': 2, 'G': 2, 'C': 1, 'T': 1}
def transition_transversion_ratio(s1, s2):
	transitions = 0
	transversions = 0
	for b1, b2 in zip(s1, s2):
		if b1 != b2:
			if _rings[b1] == _rings[b2]:
				transitions += 1
			else:
				transversions += 1
	return transitions / transversions

save(transition_transversion_ratio(*data))
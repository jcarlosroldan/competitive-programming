from utils import *

# data = '>Rosalind_1\nATCCAGCT\n>Rosalind_2\nGGGCAACT\n>Rosalind_3\nATGGATCT\n>Rosalind_4\nAAGCAACC\n>Rosalind_5\nTTGGAACT\n>Rosalind_6\nATGCCATT\n>Rosalind_7\nATGGCACT'

data = parse_fasta(data)
dna_len = len(next(iter(data.values())))
profile = [{symbol: 0 for symbol in 'ACGT'} for _ in range(dna_len)]
for dna in data.values():
	for s, symbol in enumerate(dna):
		profile[s][symbol] += 1
res = ''.join([
	max(profile[s], key=lambda k: profile[s][k])
	for s in range(dna_len)
])
for symbol in 'ACGT':
	res += '\n%s: %s' % (
		symbol,
		' '.join(str(profile[n][symbol]) for n in range(dna_len))
	)
save(res)
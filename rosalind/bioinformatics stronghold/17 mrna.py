from utils import *

# data = 'MA'

codon_vals = list(codon_table.values())
rev_table = {k: codon_vals.count(k) for k in set(codon_vals)}
res = rev_table['Stop']
for prot in data:
	res *= rev_table[prot]
save(res % 1000000)
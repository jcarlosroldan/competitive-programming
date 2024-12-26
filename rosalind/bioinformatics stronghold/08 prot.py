from utils import *

# data = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

encoded = ''.join(codon_table[data[n:n + 3]] for n in range(0, len(data), 3))
save(encoded[:-4])  # remove the Stop
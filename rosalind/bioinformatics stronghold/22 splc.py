from utils import *
from re import split

# data = '>Rosalind_10\nATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG\n>Rosalind_12\nATCGGTCGAA\n>Rosalind_15\nATCGGTCGAGCGTGT'

data = parse_fasta(data)
rna, *introns = data.values()
exons = ''.join(split('|'.join(introns), rna))
save(rna_to_protein(dna_to_rna(exons)))
from utils import *

# data = '>Rosalind_24\nTCAATGCATGCGGGTCTATATGCAT'

data = parse_fasta(data, first=True)
res = ''
for pos in range(len(data)):
	for ln in range(4, min(12, len(data) - pos) + 1):
		part = data[pos:pos + ln]
		if part == reverse_complement(part, False):
			res += '%s %s\n' % (pos + 1, ln)
save(res.strip())
from utils import *
from requests import get
from re import match

# data = 'A2Z669\nB5ZC00\nP07204_TRBM_HUMAN\nP20840_SAG1_YEAST'

motif = r'N[^P][ST][^P]'  # N-glycosylation motif
url = 'http://www.uniprot.org/uniprot/%s.fasta'
res = ''

pids = data.split('\n')
for pid in pids:
	seq = list(parse_fasta(get(url % pid).text).values())[0]
	locations = [n + 1 for n in range(len(seq)) if match(motif, seq[n:n + 4])]
	if len(locations):
		res += '%s\n%s\n' % (pid, ' '.join(map(str, locations)))
save(res.strip())
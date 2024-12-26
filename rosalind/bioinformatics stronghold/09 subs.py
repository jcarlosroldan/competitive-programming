from utils import *

# data = 'GATATATGCATATACTT\nATAT'

st1, st2 = data.split('\n')
occurrences = (n + 1 for n in range(len(st1)) if st1[n:].startswith(st2))
save(' '.join(map(str, occurrences)))
from utils import *

# data = 'GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT'

st1, st2 = data.split('\n')
save(sum(c1 != c2 for c1, c2 in zip(st1, st2)))
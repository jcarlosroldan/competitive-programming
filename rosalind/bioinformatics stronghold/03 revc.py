from utils import *

# data = 'AAAACCCGGT'

save(data.translate(str.maketrans('GTCA', 'CAGT'))[::-1])
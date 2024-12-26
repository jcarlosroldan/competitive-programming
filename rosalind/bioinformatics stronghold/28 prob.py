from utils import *
from math import log10

# data = 'ACGATACAA\n0.129 0.287 0.423 0.476 0.641 0.742 0.783'
s, A = data.split('\n')
A = list(map(float, A.split(' ')))
s_gc = s.count('G') + s.count('C')

B = [
	s_gc * log10(gc / 2) + (len(s) - s_gc) * log10((1 - gc) / 2)
	for gc in A
]
save(' '.join('%.3f' % b for b in B))
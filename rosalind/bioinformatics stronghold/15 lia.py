from utils import *
from math import factorial

# data = '2 1'

# P(Aa Bb) = P(Aa) * P(Bb) = 1/2 * 1/2 = 1/4

def comb(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))

k, N = map(int, data.split(' '))
pop = 2**k
prob = 1
for n in range(N):
	res = comb(pop, n) * (1 / 4)**n * (3 / 4)**(pop - n)
	prob -= res

save(prob)
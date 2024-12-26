from random import shuffle
from math import sqrt, log10
from Euler import prime_sieve, is_prime

triangle = lambda n: n*(n+1)/2
square = lambda n: n**2
pentagonal = lambda n: n*(3*n-1)/2
hexagonal = lambda n: n*(2*n-1)
heptagonal = lambda n: n*(5*n-3)/2
octagonal = lambda n: n*(3*n-2)

def find_4digit(generator):
	res = []
	digits = 0
	i = 1
	while True:
		n = generator(i)
		i += 1
		digits = int(log10(n)) + 1
		if digits == 4:
			res.append(n)
		elif digits > 4:
			break
	return res

def backtrack():
	seqs = [find_4digit(funct) for funct in [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]]
	shuffle(seqs)
	def solve(state):
		if len(state) == 6:
			if state[-1]%100 == state[0]//100:
				return state
		elif len(state) == 0:
			res = None
			for candidate in seqs[len(state)]:
				res = solve(state + [candidate])
				if res != None:
					break
			return res
		else:
			res = None
			for candidate in seqs[len(state)]:
				if state[-1]%100 == candidate//100:
					res = solve(state + [candidate])
					if res != None:
						break
			return res
	return solve([])

s = None
while s == None:
	s = backtrack()
print(s)
print(sum(s))
from random import shuffle
from math import sqrt, log10
from Euler import prime_sieve, is_prime
from collections import defaultdict

i = 1
cubes = defaultdict(list)
while True:
	n = i**3
	i += 1
	k = str(sorted(str(n)))
	cubes[k].append(n)
	if len(cubes[k]) == 5:
		print(min(cubes[k]))
		break

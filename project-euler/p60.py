from math import sqrt, log10
from Euler import prime_sieve, is_prime

N = 10000
primes = prime_sieve(N)

def good(a, b):
	a = primes[a]
	b = primes[b]
	la = 10 ** (int(log10(a)) + 1)
	lb = 10 ** (int(log10(b)) + 1)
	return is_prime(a*lb + b) and is_prime(b*la + a)

def solve():
	for d1 in range(len(primes)):
		for d2 in range(d1+1, len(primes)):
			if good(d1, d2):
				for d3 in range(d2+1, len(primes)):
					if good(d1, d3) and good(d2, d3):
							for d4 in range(d3+1, len(primes)):
								if good(d1, d4) and good(d2, d4) and good(d3, d4):
									for d5 in range(d4+1, len(primes)):
										if good(d1, d5) and good(d2, d5) and good(d3, d5) and good(d4, d5):
											print(list(primes[n] for n in [d1,d2,d3,d4,d5]))
											print(sum(primes[n] for n in [d1,d2,d3,d4,d5]))
											exit()
	print("Increase N")

if __name__ == '__main__':
	solve()
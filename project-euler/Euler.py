from math import sqrt, ceil
from itertools import zip_longest, compress, chain, product, combinations
from functools import reduce

def prime_list(n: int) -> list:
	''' Returns the list of primes number from 2 to n. '''
	sieve = [True] * int(n / 2)
	for i in range(3, ceil(sqrt(n)), 2):
		if sieve[int(i / 2)]:
			sieve[int(i * i / 2)::i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
	return [2] + [2 * i + 1 for i in range(1, int(n / 2)) if sieve[i]]

def is_prime(n: int) -> bool:
	''' Checks if a number is prime. '''
	res = True
	if n == 2 or n == 3:
		res = True
	elif n < 2 or n % 2 == 0:
		res = False
	elif n < 9:
		res = True
	elif n % 3 == 0:
		res = False
	r = int(sqrt(n))
	f = 5
	while f <= r:
		if n % f == 0 or n % (f + 2) == 0:
			res = False
		else:
			f += 6
	return res

def fibonacci(n: int) -> int:
	''' Returns the n-th Fibonacci number. '''
	def _fib(n):
		if n == 0:
			return (0, 1)
		else:
			a, b = _fib(n // 2)
			c = a * (2 * b - a)
			d = b * b + a * a
			if n % 2 == 0:
				return (c, d)
			else:
				return (d, c + d)
	return _fib(n)[0]

def lcm(a: int, b: int) -> int:
	''' Least common multiple of two numbers. '''
	return a * b / gcd(a, b)

def gcd(a: int, b: int) -> int:
	''' Greatest common divisor of two numbers. '''
	if a < 0:
		a = -a
	if b < 0:
		b = -b
	if a == 0:
		return b
	while (b):
		a, b = b, a % b
	return a

def factor(n: int) -> list:
	''' Returns the factors of n and its exponents. '''
	f, factors, prime_gaps = 1, [], [2, 4, 2, 4, 6, 2, 6, 4]
	if n < 1:
		return []
	while True:
		for gap in ([1, 1, 2, 2, 4] if f < 11 else prime_gaps):
			f += gap
			if f * f > n:  # If f > sqrt(n)
				if n == 1:
					return factors
				else:
					return factors + [(n, 1)]
			if not n % f:
				e = 1
				n //= f
				while not n % f:
					n //= f
					e += 1
				factors.append((f, e))

def palindrome_list(k: int) -> list:
	''' Returns a list of every palindromic number with k digits. '''
	if k == 1:
		return [1, 2, 3, 4, 5, 6, 7, 8, 9]
	return [
		sum([
			n * (10**i)
			for i, n in enumerate(
				([x] + list(ys) + [z] + list(ys)[::-1] + [x])
				if k % 2 else ([x] + list(ys) + list(ys)[::-1] + [x])
			)
		])
		for x in range(1, 10)
		for ys in product(range(10), repeat=k // 2 - 1)
		for z in (range(10) if k % 2 else (None,))
	]

def phi(n: int) -> int:
	''' Returns the Euler's phi function of n. '''
	res = n
	factors = [f[0] for f in factor(n)]
	multiplier = 1
	for fs in range(1, len(factors) + 1):
		multiplier *= -1
		for primes in combinations(factors, fs):
			val = reduce(lambda x, y: x * y, primes)
			if val <= n and n % val == 0:
				res += (n // val) * multiplier
	return res
from Euler import prime_sieve

MAX_TEST = 5000
PRIMES = prime_sieve(MAX_TEST)

_mem_ways_to_sum = {}
def ways_to_sum(number, max_prime):
	if number <= 0: return 0
	k = (number, max_prime)
	if k in _mem_ways_to_sum: return _mem_ways_to_sum[k]
	res = 0
	primes = [p for p in PRIMES if p <= max_prime]
	for p in reversed(primes):
		remain = number - p
		res += ways_to_sum(remain, p)
		if remain in primes and remain <= p: res += 1
	_mem_ways_to_sum[k] = res
	return res

for n in range(1, MAX_TEST + 1):
	if ways_to_sum(n, n) > 5000:
		print(n)
		exit()
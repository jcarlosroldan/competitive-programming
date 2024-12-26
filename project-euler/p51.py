from Euler import is_prime, prime_sieve

def first_of_family(family_size):
	digits = 1
	while True:
		digits+=1
		for repeating_digits in range(1,digits):
			r = _families(digits,repeating_digits,family_size)
			if r>0:
				return r

def _families(digits,repeating_digits,family_size):
	numbers = [n for n in '0123456789']
	upper_bound = 10**digits
	lower_bound = upper_bound/10
	sieve = [n for n in prime_sieve(upper_bound) if n<upper_bound and n>lower_bound]
	max_not_primes = 10-family_size
	for prime in sieve:
		s = str(prime)
		for n in numbers:
			if s.count(n)==repeating_digits:
				# get family for this number
				not_prime = 0
				for nn in numbers:
					candidate = int(s.replace(n,nn))
					if not is_prime(candidate) or candidate<lower_bound:
						not_prime +=1
						if not_prime > max_not_primes:
							break
				else:
					return prime
	return -1

print(first_of_family(8))
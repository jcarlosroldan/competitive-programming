from Euler import phi

N = 10000000

max_v = 0
max_n = None
for n in range(2, N + 1):
	p = phi(n)
	v = n / p
	if set(str(n)) == set(str(p)) and v > max_v:
		max_v = v
		max_n = n
print(max_n)
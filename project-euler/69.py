from Euler import phi

N = 1000000

max_v = 0
max_n = None
for n in range(2, N + 1):
	v = n / phi(n)
	if v > max_v:
		max_v = v
		max_n = n
print(max_n)
from time import sleep
from math import sqrt

def fraction(n):
	res = [int(sqrt(n))]
	final_state = (1, res[0])
	state = final_state
	while True:
		a = (n - state[1]**2) // state[0]
		res.append(int((sqrt(n) + state[1]) / a))
		b = res[-1] * a - state[1]
		state = (a, b)
		if state == final_state:
			break
	return res

# N = 13
N = 10000
print(sum((len(fraction(n)) - 1) % 2 for n in range(N + 1) if sqrt(n) % 1 != 0))
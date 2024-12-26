"""
_mem_mod_collatz = {}
def mod_collatz(n):
	res = ""
	while n != 1:
		if n in _mem_mod_collatz:
			res += _mem_mod_collatz[n]
			break
		if n % 3 == 0:
			n /= 3
			res += "D"
		elif n % 3 == 1:
			n = (4* n + 2) / 3
			res += "U"
		else:
			n = (2 * n - 1) / 3
			res += "d"
	_mem_mod_collatz[n] = res
	return res

for n in range(10**15):
	if mod_collatz(n).startswith("UDDDUdddDDUDDddDdDddDDUDDdUUDd"):
		print(n)
		break

"""
def untangle_sentence(sentence):
	res = 1
	for op in reversed(sentence):
		if op == "D":
			res *= 3
		elif op == "U":
			res = (3 * res - 2) / 4
		elif op == "d":
			res = (res * 3 + 1) / 2
	return res

print(untangle_sentence("UDDDUdddDDUDDddDdDddDDUDDdUUDd"))
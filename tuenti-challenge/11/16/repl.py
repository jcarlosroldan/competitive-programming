from math import gcd as _gcd
from pwn import remote
from numpy import zeros
from simpler import mem_cache

@mem_cache
def gcd(x, y):
	return _gcd(x, y)

_remote = None
def say(message=None):
	global _remote
	if _remote is None: _remote = remote('codechallenge-daemons.0x14.net', '7162')
	if message is not None: _remote.sendline(message.encode())
	res = _remote.recvline().decode().strip()
	return res

N, Q = map(int, say().split())
_board = zeros((N, N), dtype=int)
def ask_gcd(x, y):
	if _board[x - 1, y - 1] == 0:
		res = int(say(f'? {x} {y}'))
		_board[x - 1, y - 1] = _board[y - 1, x - 1] = res
	return _board[x - 1, y - 1]

@mem_cache
def is_prime(n):
	return all(n % i for i in range(2, int(n ** 0.5) + 1))

def solve():
	domains = {n: list(range(1, N + 1)) for n in range(1, N + 1)}
	for n in range(1, N + 1):
		for m in range(n + 1, N + 1):
			val = _board[n - 1, m - 1]
			if val > 1:
				domains[n] = [x for x in domains[n] if x % val == 0]
				domains[m] = [x for x in domains[m] if x % val == 0]
	while True:
		changed = False
		new_singles = {}
		for n in range(1, N + 1):
			for m in range(n + 1, N + 1):
				val = _board[n - 1, m - 1]
				if val > 0:
					if len(domains[n]) == 1 and len(domains[m]) > 1:
						before = len(domains[m])
						domains[m] = [x for x in domains[m] if gcd(x, domains[n][0]) == val]
						changed = changed or len(domains[m]) != before
					if len(domains[m]) == 1 and len(domains[n]) > 1:
						before = len(domains[n])
						domains[n] = [x for x in domains[n] if gcd(x, domains[m][0]) == val]
						changed = changed or len(domains[n]) != before
		if not changed: break
	return domains

print('Populating dependencies')
[ask_gcd(n, n + 1) for n in range(1, N)]
[ask_gcd(n, n + 2) for n in range(1, N - 1)]
[ask_gcd(1, n) for n in range(2, N + 1)]

print('Searching highest GCDs')
search = {2, 3, 5, 7, 11, 13, 17, 19, 66, 14}
numbers = []
for r, row in enumerate(_board, 1):
	for c, val in enumerate(row, 1):
		if val > 1: numbers.append((val, r, c))

print('Asking for factors')
for val, r, c in sorted(numbers):
	for s in search:
		if val % s == 0:
			[ask_gcd(val, n) for n in range(1, N + 1) if n != val]
			break
	else:
		continue
	search.remove(s)
	if len(search) == 0: break

solve()
1
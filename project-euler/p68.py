from itertools import permutations
from time import sleep

def sprint(*msg):
	print(*msg)
	sleep(.1)

def all_equal(lst):
	return not lst or [lst[0]] * len(lst) == lst

# splits = ((0, 1, 2), (3, 2, 4), (5, 4, 1))
splits = ((0, 1, 2), (3, 2, 4), (5, 4, 6), (7, 6, 8), (9, 8, 1))
N = len(splits)
string_len = 16

res = 0
for perm in permutations(range(1, N * 2 + 1)):
	# sprint(perm)
	if all_equal([sum(perm[d] for d in splits[n]) for n in range(N)]):
		arms = [[perm[d] for d in splits[n]] for n in range(N)]
		cut = min(enumerate(arms), key=lambda x: x[1][0])[0]
		arms = arms[cut:] + arms[:cut]
		v = int("".join(map(str, [n for arm in arms for n in arm])))
		if res < v < 10**string_len:
			res = v

print(res)
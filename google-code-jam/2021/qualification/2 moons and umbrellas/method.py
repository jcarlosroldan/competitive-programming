from validator import input, print  # DO NOT PASTE THIS LINE

def main():
	for case in range(int(input())):
		CJ, JC, mural = input().split(' ')
		print('Case #%s: %s' % (case + 1, solve(int(CJ), int(JC), mural)))

def solve(CJ, JC, mural):
	cost = 0
	i = 0
	length = 0
	while i < len(mural):
		if mural[i] == '?':
			if length == 0:
				before = mural[i - 1] if i > 0 else ''
			length += 1
		else:
			if length > 0:
				after = mural[i] if i < len(mural) else ''
				cost += compute_cost(CJ, JC, length, before, after)
				length = 0
			elif mural[i] == 'C':
				if i > 0 and mural[i - 1] == 'J': cost += JC
			elif mural[i] == 'J':
				if i > 0 and mural[i - 1] == 'C': cost += CJ
		i += 1
	return cost

def compute_cost(CJ, JC, length, before, after):
	all_c = (JC if before == 'J' else 0) + (CJ if after == 'J' else 0)
	all_j = (CJ if before == 'C' else 0) + (JC if after == 'C' else 0)
	alternate_from_c = (JC if before == 'J' else 0) + (JC if length % 2 == 0 and after == 'C' else CJ if length % 2 == 1 and after == 'J' else 0) + (CJ * length // 2 + JC * (length + 1) // 2)
	alternate_from_j = (CJ if before == 'C' else 0) + (CJ if length % 2 == 0 and after == 'J' else JC if length % 2 == 1 and after == 'C' else 0) + (JC * length // 2 + CJ * (length + 1) // 2)
	return min(all_c, all_j, alternate_from_c, alternate_from_j)

main()
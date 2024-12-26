from itertools import combinations, permutations
from re import findall

FNAME = 'submit'

def main():
	output = ''
	for p, problem in enumerate(load_input(), 1):
		print('Solving case #%d' % p)
		output += 'Case #%d: %s\n' % (p, solve(problem))
	with open('%sOutput.txt' % FNAME, 'w', encoding='utf-8') as fp:
		fp.write(output)

def load_input():
	with open('%sInput.txt' % FNAME, 'r', encoding='utf-8') as fp:
		for _ in range(int(fp.readline())):
			yield fp.readline().strip()

def solve(sentence):
	sentence = sentence.replace('=', '==')
	res = []
	letters = ''.join(sorted(set(s for s in sentence if s not in '+-*/= 0123456789.')))
	non_zero = {letters.index(e[1]) for e in findall(r'( |^)([A-Z])', sentence)}
	for comb in combinations(range(10), len(letters)):
		for perm in permutations(comb):
			if any(perm[i] == 0 for i in non_zero): continue
			replacements = dict(zip(letters, map(str, perm)))
			replaced = sentence.translate(str.maketrans(replacements))
			if eval(replaced):  # sorry for this
				res.append(replaced.replace('==', '='))
	return ';'.join(sorted(res)) if len(res) else 'IMPOSSIBLE'

if __name__ == '__main__':
	main()
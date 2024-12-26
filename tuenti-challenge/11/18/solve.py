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
			yield [fp.readline().strip().split(' ')[0] for _ in range(int(fp.readline()))]

def solve(instructions):
	freqs = list(sorted((instructions.count(i) for i in set(instructions))))
	tree = flatest_huffman(freqs)
	return f'{score(tree) + len(instructions) * 2}, {diff(tree)}'

def flatest_huffman(freqs):
	if len(freqs) == 1: return freqs
	freqs, tree = [(f, 1) for f in freqs], tuple(freqs)
	while len(freqs) > 1:
		mins, mins_idx = freqs[:2], [0, 1]
		for f, freq in enumerate(freqs[2:], 2):
			if freq < mins[0] and mins[0] < mins[1]:
				mins[0], mins_idx[0] = freq, f
			elif freq < mins[1]:
				mins[1], mins_idx[1] = freq, f
		freqs = [freq for f, freq in enumerate(freqs) if f not in mins_idx] + [(mins[0][0] + mins[1][0], max(mins[0][1], mins[1][1]) + 1)]
		tree = tuple(tree for t, tree in enumerate(tree) if t not in mins_idx) + ((tree[mins_idx[0]], tree[mins_idx[1]]),)
	return tree[0]

def score(tree, d=1):
	res = score(tree[0], d + 1) if isinstance(tree[0], tuple) else d * tree[0]
	if len(tree) > 1:
		res += score(tree[1], d + 1) if isinstance(tree[1], tuple) else d * tree[1]
	return res

def diff(tree):
	less = None
	depth = 0
	while len(tree):
		depth += 1
		if less is None and any(isinstance(t, int) for t in tree): less = depth
		tree = [child for t in tree if isinstance(t, tuple) for child in t]
	return depth - less

if __name__ == '__main__':
	main()
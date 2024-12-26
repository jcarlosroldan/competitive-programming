FNAME = 'submit'
SCALE = 'ABCDEFG'
NOTE_TO_OFFSET = None

def main():
	global NOTE_TO_OFFSET
	NOTE_TO_OFFSET = get_mapping()
	output = ''
	for p, problem in enumerate(load_input(), 1):
		print('Solving case #%d' % p)
		output += 'Case #%d: %s\n' % (p, solve(*problem))
	with open('%sOutput.txt' % FNAME, 'w', encoding='utf-8') as fp:
		fp.write(output)

def load_input():
	with open('%sInput.txt' % FNAME, 'r', encoding='utf-8') as fp:
		problems = int(fp.readline())
		for _ in range(problems):
			yield fp.readline().strip(), fp.readline().strip()

def solve(root, steps):
	res = root
	offset = NOTE_TO_OFFSET[root]
	scale_offset = SCALE.index(root[:1])
	for s, step in enumerate(steps, 1):
		offset = (offset + (1 if step == 'T' else .5)) % 6
		note = SCALE[(scale_offset + s) % len(SCALE)]
		for candidate in (note, note + 'b', note + '#'):
			if NOTE_TO_OFFSET[candidate] == offset:
				res += candidate
				break
	return res

def get_mapping():
	note = -1
	res = {n: (note := note + .5 if n in 'CF' else note + 1) for n in SCALE}
	res.update(
		**{'%s#' % k: (v + .5) % 6 for k, v in res.items()},
		**{'%sb' % k: (v + 5.5) % 6 for k, v in res.items()},
	)
	return res


if __name__ == '__main__':
	main()
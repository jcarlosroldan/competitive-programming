FNAME = 'submit'

def main():
	output = ''
	for p, problem in enumerate(load_input(), 1):
		print('Solving case #%d: %s' % (p, solve(problem)))
		output += 'Case #%d: %s\n' % (p, solve(problem))
	with open('%sOutput.txt' % FNAME, 'w', encoding='utf-8') as fp:
		fp.write(output)

def load_input():
	with open('%sInput.txt' % FNAME, 'r', encoding='utf-8') as fp:
		for _ in range(int(fp.readline())):
			fp.readline()
			yield fp.readline().split()

def solve(piles):
	piles = [int(p) % 3 for p in piles]
	parity = [piles.count(n) % 2 for n in range(3)]
	return 'Alberto' if parity[1] + parity[2] == 0 else 'Edu'

if __name__ == '__main__':
	main()
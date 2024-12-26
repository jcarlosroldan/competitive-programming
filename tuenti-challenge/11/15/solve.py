FNAME = 'submit'

MOD = int(1e8 + 7)
TUENTISTIC = [None, 1]

def main():
	populate_ntp()
	output = ''
	for p, problem in enumerate(load_input(), 1):
		print('Solving case #%d' % p)
		output += 'Case #%d: %s\n' % (p, solve(problem))
	with open('%sOutput.txt' % FNAME, 'w', encoding='utf-8') as fp:
		fp.write(output)

def load_input():
	with open('%sInput.txt' % FNAME, 'r', encoding='utf-8') as fp:
		for _ in range(int(fp.readline())):
			yield int(fp.readline())

def solve(n):
	return TUENTISTIC[n] if n < MOD else 0

def populate_ntp():
	print('Populating tuentistic non-tuentistic products...')
	[TUENTISTIC.append((TUENTISTIC[-1] * (1 if is_tuentistic(n) else n)) % MOD) for n in range(2, MOD)]

def is_tuentistic(n):
	''' Returns whether n contains the word "Twenty" when written in English. '''
	while n > 0:
		if 20 <= n % 100 <= 29:
			return True
		n //= 1000
	return False

if __name__ == '__main__':
	main()
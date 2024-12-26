FNAME = 'submit'

def main():
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
			P, R, _ = map(int, fp.readline().split())
			yield [fp.readline().strip() for _ in range(P)], [fp.readline().strip() for _ in range(R)]

def solve(pokemons, rows):
	res = ''.join(rows).replace(' ', '')
	while len(pokemons):
		for p in pokemons:
			reversed_p = p[::-1]
			if p in res:
				res = res.replace(p, '', 1)
				pokemons.remove(p)
			elif reversed_p in res:
				res = res.replace(reversed_p, '', 1)
				pokemons.remove(p)
				break
	for p in pokemons:
		res = res.replace(p, '')
	return res

if __name__ == '__main__':
	main()
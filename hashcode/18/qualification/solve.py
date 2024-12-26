from os import listdir

# --- problem specific --------------------------------------------------------

def main():
	for fname in sorted(listdir('data')):
		if fname.endswith('.in'):
			print(fname)
			problem = load('data/%s' % fname)
			answer = solve(*problem)
			save(answer)
			break

def solve(rows, cols, vehicles, rides, start_bonus, steps, trips):
	return rows

# --- i/o --------------------------------------------------------

def load(path):
	with open(path, 'r', encoding='utf-8') as fp:
		data = [line.split(' ') for line in fp.read().strip().split('\n')]
	data, trips = data[0], data[1:]
	return (*data, trips)

def save(problem):
	print(problem)

# --- entrypoint --------------------------------------------------------------

if __name__ == '__main__':
	main()

from networkx import prefix_tree
from networkx.algorithms.shortest_paths.generic import shortest_path_length

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
			N, K = map(int, fp.readline().split())
			methods = [fp.readline().strip() for _ in range(N)]
			yield K, methods

def solve(per_file, methods):
	score = 0
	G = prefix_tree(methods)
	G.remove_node(-1)
	for method in methods:
		n = 0
		for char in method:
			n = next(s for s in G.successors(n) if G.nodes[s]['source'] == char)
		G.nodes[n]['score'] = G.nodes[n].get('score', 0) + 1
	depths = shortest_path_length(G, 0)
	for n in sorted(depths, key=lambda n: -depths[n]):
		G.nodes[n]['score'] = G.nodes[n].get('score', 0) + sum(G.nodes[s]['score'] for s in G.successors(n))
		while G.nodes[n]['score'] >= per_file:
			G.nodes[n]['score'] -= per_file
			score += depths[n]
	return score

if __name__ == '__main__':
	main()
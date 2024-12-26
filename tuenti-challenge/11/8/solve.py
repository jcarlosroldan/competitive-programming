from networkx import Graph, number_connected_components

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
		problems = int(fp.readline())
		for _ in range(problems):
			yield [fp.readline().strip().split(',') for _ in range(int(fp.readline()))]

def cutter_nodes(G):
	for n in G.nodes():
		nG = G.copy()
		nG.remove_node(n)
		if number_connected_components(nG) > 1:
			yield n

def solve(tickets):
	G = Graph()
	[G.add_edge(src, dst) for src, dst in tickets]
	res = ','.join(sorted(cutter_nodes(G)))
	return res if len(res) > 0 else '-'

if __name__ == '__main__':
	main()
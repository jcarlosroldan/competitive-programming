import networkx as nx
from math import log10

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
			markets = {}
			for _ in range(int(fp.readline())):
				name, exchanges = fp.readline().split()
				markets[name] = []
				for _ in range(int(exchanges)):
					src, price, dst = fp.readline().strip().split('-')
					markets[name].append((src, dst, int(price)))
			yield markets

def solve(markets):
	G = nx.DiGraph()
	best_exchanges = {}
	for exchanges in markets.values():
		for src, dst, price in exchanges:
			if price == 0: continue
			if (src, dst) not in best_exchanges or price > best_exchanges[(src, dst)]:
				best_exchanges[(src, dst)] = price
	for (src, dst), price in best_exchanges.items():
		if src == 'BTC': src = 'BTC-src'
		if dst == 'BTC': dst = 'BTC-dst'
		G.add_edge(src, dst, weight=20 - log10(price))
	try:
		path = nx.shortest_path(G, 'BTC-src', 'BTC-dst', weight='weight')
	except:
		return 1
	return int(10 ** sum(20 - G[path[i]][path[i + 1]]['weight'] for i in range(len(path) - 1)))

if __name__ == '__main__':
	main()
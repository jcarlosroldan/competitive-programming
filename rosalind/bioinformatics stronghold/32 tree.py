from utils import *

# data = '10\n1 2\n2 8\n4 10\n5 9\n6 10\n7 9'
data = data.split('\n')
nodes = int(data[0])
edges = [tuple(map(int, edge.split(' '))) for edge in data[1:]]

components = list(range(nodes))
for n1, n2 in edges:
	old_comp = max(components[n1 - 1], components[n2 - 1])
	new_comp = min(components[n1 - 1], components[n2 - 1])
	components = [new_comp if c == old_comp else c for c in components]

save(len(set(components)) - 1)
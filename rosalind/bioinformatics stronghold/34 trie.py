from utils import *

words = data.split('\n')
tree = [(None, None)]  # each node is a tuple (letter, parent)

for word in words:
	current = 0
	for letter in word:
		if (letter, current) not in tree:
			tree.append((letter, current))
			current = len(tree) - 1
		else:
			current = tree.index((letter, current))
print(tree)
save('\n'.join(
	'%d %d %s' % (node[1] + 1, n + 1, node[0])
	for n, node in enumerate(tree)
	if n > 0
))
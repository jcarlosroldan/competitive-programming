import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()

with open("res/p83_matrix.txt","r") as f:
	rows = f.read().split("\n")
matrix = [list(map(int,n.split(","))) for n in rows]

# weight considered when entering the node
height = len(matrix)
width = len(matrix[0])
for y in range(0,height):
	# horizontal edges
	for x in range(0,width-1):
		g.add_edge((x,y),(x+1,y),weight=matrix[y][x+1])
	for x in range(1,width):
		g.add_edge((x,y),(x-1,y),weight=matrix[y][x-1])

# add vertical edges
for x in range(0,width):
	for y in range(0,width-1):
		g.add_edge((x,y),(x,y+1),weight=matrix[y+1][x])
	for y in range(1,width):
		g.add_edge((x,y),(x,y-1),weight=matrix[y-1][x])

path = nx.astar_path(g,(0,0),(width-1,height-1))
print(path)
total = sum(g[n1][n2]['weight'] for n1,n2 in zip(path[:-1],path[1:])) + matrix[0][0]
print(total)
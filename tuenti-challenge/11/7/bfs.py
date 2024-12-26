from networkx import Graph, shortest_path
from pwn import remote

PATH_LOG = 'log.txt'
PATH_OUTPUT = 'output.txt'
PATH_BOARD = 'board.txt'
BOARD_LIMIT = 100
DIR = {'north': (0, 1), 'west': (1, 0), 'east': (-1, 0), 'south': (0, -1)}
RID = {v: k for k, v in DIR.items()}

def main():
	pos = (0, 0)
	pending = []
	visited = [pos]
	[say() for _ in range(2)]
	while True:
		# see what's around
		dirs = say('look').split(': ')[1].split(' ')
		for d in DIR:
			coords = rel_to_abs(pos, d)
			board(*coords, ' ' if d in dirs else '#')
			if d in dirs and coords not in visited and coords not in pending:
				pending.append(coords)
		# move to the closest to origin
		dst = min(pending, key=lambda c: distance(c))
		if distance(dst) > 1:
			jump = min(visited, key=lambda c: distance(c, dst))
			say('go to %s,%s' % jump)
			pos = jump
		say(RID[(dst[0] - pos[0], dst[1] - pos[1])])
		pos = dst
		pending.remove(dst)
		visited.append(dst)
		# check if exit is here
		if say('is exit?').startswith('Yes'):
			break
	# compute bfs
	G = Graph()
	nodes = visited + pending
	for n1 in range(len(nodes)):
		for n2 in range(n1 + 1, len(nodes)):
			if distance(nodes[n1], nodes[n2]) == 1:
				G.add_edge(nodes[n1], nodes[n2])
	with open(PATH_OUTPUT, 'w') as fp:
		fp.write(', '.join(map(str, shortest_path(G, (0, 0), pos))))

def rel_to_abs(coords, rel):
	return (coords[0] + DIR[rel][0], coords[1] + DIR[rel][1])

_board = [['?' for _ in range(BOARD_LIMIT * 2)] for _ in range(BOARD_LIMIT * 2)]
def board(x, y, value=None):
	if value is None:
		return _board[x + BOARD_LIMIT][y + BOARD_LIMIT]
	_board[x + BOARD_LIMIT][y + BOARD_LIMIT] = value
	with open(PATH_BOARD, 'w') as fp:
		fp.write('\n'.join([''.join(row) for row in _board]))
board(19, 17, 'X')

_say_remote = remote('codechallenge-daemons.0x14.net', '4321')
def say(msg=None):
	if msg is not None:
		_say_remote.sendline(msg.encode())
	res = _say_remote.recvline().decode().strip()
	with open(PATH_LOG, 'a') as fp:
		fp.write('> %s\n%s\n' % (msg, res))
	return res

def distance(coords1, coords2=(0, 0)):
	return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])

if __name__ == '__main__':
	main()
from utils import *

# data = '6 3'

n, m = map(int, data.split(' '))
rabbits = [1] + [0 for _ in range(m - 1)]
for month in range(n - 1):
	rabbits = [sum(rabbits[1:])] + rabbits[:-1]

save(sum(rabbits))
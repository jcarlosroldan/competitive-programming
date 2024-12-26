from utils import *

# data = '5 3'

n, k = map(int, data.split(' '))
smalls = 1
bigs = 0
for month in range(n - 1):
	newbigs = bigs + smalls
	smalls = bigs * k
	bigs = newbigs

save(smalls + bigs)
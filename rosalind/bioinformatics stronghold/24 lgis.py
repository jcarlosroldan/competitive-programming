from utils import *

# data = '5\n5 1 4 2 3'

n, nums = data.split('\n')
n = int(n)
nums = list(map(int, nums.split(' ')))

mem = {}
def lis(pos, limit, asc):
	if (pos, limit) in mem: return mem[(pos, limit)]
	max_seq = []
	for p in range(pos, n):
		if asc and nums[p] > limit or not asc and nums[p] < limit:
			seq = [nums[p]] + lis(p + 1, nums[p], asc)
			if len(seq) > len(max_seq):
				max_seq = seq
	mem[(pos, limit)] = max_seq
	return max_seq

seq1 = lis(0, min(nums) - 1, True)
mem = {}
seq2 = lis(0, max(nums) + 1, False)

save('%s\n%s' % (
	' '.join(map(str, seq1)),
	' '.join(map(str, seq2))
))
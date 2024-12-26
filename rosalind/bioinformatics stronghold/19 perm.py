from utils import *

# data = '9'

def perms(nums):
	if len(nums) == 1:
		return [nums]
	res = []
	for num in nums:
		others = [n for n in nums if n != num]
		for perm in perms(others):
			res.append([num] + perm)
	return res

ps = perms(list(range(1, int(data) + 1)))
save('%s\n%s' % (
	len(ps),
	'\n'.join(' '.join(map(str, line)) for line in ps)
))
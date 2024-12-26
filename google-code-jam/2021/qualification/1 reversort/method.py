from validator import input, print, check

###############################################################################
#                        PASTE BELOW THIS COMMENT                             #
###############################################################################

def main():
	for case in range(int(input())):
		input()
		lst = list(map(int, input().split(' ')))
		print('Case #%s: %s' % (case + 1, solve(lst)))

def solve(lst):
	cost = 0
	for i in range(0, len(lst) - 1):
		sublst = lst[i:]
		j = i + sublst.index(min(sublst))
		lst[i:j + 1] = reversed(lst[i:j + 1])
		cost += j - i + 1
	return cost

main()

###############################################################################
#                        PASTE ABOVE THIS COMMENT                             #
###############################################################################

check()
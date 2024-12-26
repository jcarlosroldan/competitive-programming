from validator import input, print  # DO NOT PASTE THIS LINE

def main():
	for case in range(int(input())):
		N, C = map(int, input().split(' '))
		print('Case #%s: %s' % (case + 1, solve(N, C)))

def solve(N, C):
	if N - 1 <= C <= N * (N + 1) / 2 - 1:
		overcost = C - (N - 1)
		res = list(range(1, N + 1))
		for i in range(N - 2, -1, -1):
			max_overcost = min(overcost, N - i - 1)
			overcost -= max_overcost
			res[i: i + max_overcost + 1] = reversed(res[i: i + max_overcost + 1])
		return ' '.join(map(str, res))
	else:
		return 'IMPOSSIBLE'

main()
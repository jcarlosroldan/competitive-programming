# Troublesort = 2 intervowen bubblesorts
cases = int(input())
for case in range(1, cases + 1):
	input()
	ls = list(map(int, input().split(" ")))
	lss = [[], []]
	for n, l in enumerate(ls):
		lss[n%2].append(l)
	lss = [list(sorted(lss[0])), list(sorted(lss[1]))]
	res = []
	for n in range(min(len(lss[0]), len(lss[1]))):
		res.append(lss[0][n])
		res.append(lss[1][n])
	if len(ls) % 2:
		res.append(lss[0][-1])
	try:
		res = next(n for n in range(len(res) - 1) if res[n] > res[n+1])
	except:
		res = "OK"
	print("Case #%s: %s" % (case, res))
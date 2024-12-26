# https://code.google.com/codejam/contest/3274486/dashboard#s=p1
from math import pi


FNAME = "A-large"

def solve_all():
	# read the file
	with open("%s.in" % FNAME, "r") as f:
		lines = f.read().strip().split("\n")[1:]
	# join the lines in problems
	i = 0
	problems = []
	while i < len(lines):
		N, K = map(int, lines[i].split(" "))
		pancakes = [tuple(map(int, l.split(" "))) for l in lines[i+1:i+N+1]]
		i += N + 1
		problems.append((K, pancakes))
	# solve each problem
	case = 1
	text = ""
	for problem in problems:
		print("Solving Case #%s" % case)
		res = solve(*problem)
		text += "Case #%s: %s\n" % (case, res)
		case += 1
	with open("%s.out" % FNAME, "w") as out:
		out.write(text)

def solve(K, pancakes):
	# radius, size, stacked_increment
	sizes = sorted([(p[0], pi*p[0]**2 + 2*pi*p[0]*p[1], 2*pi*p[0]*p[1]) for p in pancakes], key = lambda p: -p[0])
	max_res = 0
	for n, first_p in enumerate(sizes):
		if len(sizes) - n < K:
			break
		res = first_p[1]
		res += sum(p[2] for p in sorted(sizes[n+1:], key = lambda p: -p[2])[:K-1])
		if max_res < res:
			max_res = res
	return max_res

if __name__ == "__main__":
	solve_all()
# https://code.google.com/codejam/contest/3264486/dashboard#s=p1

FNAME = "A-large"

def solve_all():
	# read the file
	with open("%s.in" % FNAME, "r") as f:
		lines = f.read().strip().split("\n")[1:]
	# join the lines in problems
	problems = [l.split(" ") for l in lines]
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

def solve(pancakes, K):
	pancakes = [c == "-" for c in pancakes]
	K = int(K)
	flips = 0
	for i in range(len(pancakes)-K+1):
		if pancakes[i]:
			pancakes[i:i+K] = [not p for p in pancakes[i:i+K]]
			flips += 1
	if any(pancakes):
		return "IMPOSSIBLE"
	else:
		return flips

if __name__ == "__main__":
	solve_all()
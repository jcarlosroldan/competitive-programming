# https://code.google.com/codejam/contest/3274486/dashboard#s=p2
from math import pi


FNAME = "example"

def solve_all():
	# read the file
	with open("%s.in" % FNAME, "r") as f:
		lines = f.read().strip().split("\n")[1:]
	# join the lines in problems
	i = 0
	problems = []
	while i < len(lines):
		C, J = map(int, lines[i].split(" "))
		C_acts = [tuple(map(int, l.split(" "))) for l in lines[i+1:i+C+1]]
		J_acts = [tuple(map(int, l.split(" "))) for l in lines[i+C+1:i+C+J+1]]
		i += C + J + 1
		problems.append((C_acts, J_acts))
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

def solve(C_acts, J_acts):
	# first find the most busy one
	C_b = sum(a[1] - a[0] for a in C_acts)
	J_b = sum(a[1] - a[0] for a in J_acts)
	if J_b > C_b:
		C_b, J_b = J_b, C_b
		C_acts, J_acts = J_acts, C_acts
	# organise all activities
	acts = [(0, a[0], a[1]) for a in C_acts] + [(1, a[0], a[1]) for a in J_acts]
	first = min(acts, key = lambda x: x[1])[1]
	# fix acts to start
	acts = [(a[0], a[1] - first, a[2] - first) for a in acts]
	acts = list(sorted(acts, key = lambda x: x[1]))
	print(acts)
	# find min exchanges
	min_exchanges = sum(acts[n][0] != acts[n+1][0] for n in range(-1, len(acts) - 1))
	T = sum(a[1]-a[0] for a in acts)
	D = sum(acts[n+1][1] - acts[n][2] for n in range(len(acts) - 1) if acts[n+1][0] != acts[n][0])
	if acts[0][0] != acts[-1][0]:
		D += (1440 - acts[-1][2]) + acts[0][1]
	print(T, D)
	if T + D >= 720 >= T - D:
		print("It's done")
		return min_exchanges
	time_to_cover = C_b - J_b
	return -1

if __name__ == "__main__":
	solve_all()
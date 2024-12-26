# https://code.google.com/codejam/contest/3264486/dashboard#s=p2

FNAME = "C-small-1-attempt0"

def solve_all():
	# read the file
	with open("%s.in" % FNAME, "r") as f:
		lines = f.read().strip().split("\n")[1:]
	# join the lines in problems
	problems = [map(int, l.split(" ")) for l in lines]
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

def solve(N, K):
	stalls = [0, N+1]
	for _ in range(K):
		score = 10**100
		pos = None
		index = None
		for s in range(len(stalls) - 1):
			if stalls[s+1]-stalls[s] == 1: continue
			new_pos = int((stalls[s] + stalls[s+1])/2)
			Ls = new_pos - stalls[s]
			Rs = stalls[s+1] - new_pos
			new_score = min(Ls, Rs)
			if new_score < score:
				score = new_score
				pos = new_pos
				index = s
		stalls.insert(index + 1, pos)
	return "%s %s" % (max(Ls, Rs) - 1, min(Ls, Rs) - 1)

if __name__ == "__main__":
	solve_all()
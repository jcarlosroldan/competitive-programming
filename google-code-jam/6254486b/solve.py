# https://code.google.com/codejam/contest/4224486/dashboard#s=p1

def read_file(fname):
	with open(fname,"r") as f:
		data = [l.strip() for l in f.readlines()][1:]
	return data

def solve_all(fname):
	problems = read_file("%s.in" % fname)
	case = 1
	text = ""
	for S in problems:
		print("Solving Case #%s" % case)
		res = solve(S)
		text += "Case #%s: %s\n" % (case, res)
		case+=1
	with open("%s.out" % fname, "w") as out:
		out.write(text)

def solve(S):
	tower = [c == "+" for c in S]
	if tower[-1]:
		score = 0
	else:
		score = 1
	if len(tower)>1:
		score += sum([tower[i]!=tower[i-1] for i in range(1,len(tower))])
	return score



















solve_all("B-large")
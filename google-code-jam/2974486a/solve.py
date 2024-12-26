# https://code.google.com/codejam/contest/2974486/dashboard#s=p1

FNAME = "A-small-practice"

def solve_all():
	# read the file
	with open("%s.in" % FNAME, "r") as f:
		lines = f.read().split("\n")[1:-1]
	# join the lines in problems
	problems = [lines[i:i+10] for i in range(0, len(lines), 10)]
	# solve each problem
	case = 1
	text = ""
	for problem in problems:
		print("Solving Case #%s" % case)
		res = solve(problem)
		text += "Case #%s: %s\n" % (case, res)
		case += 1
	with open("%s.out" % FNAME, "w") as out:
		out.write(text)

def solve(prob):
	a = set(prob[int(prob[0])].split(" "))
	b = prob[int(prob[5])+5].split(" ")
	l = a.intersection(b)
	if len(l) == 0:
		return "Volunteer cheated!"-
	elif len(l) == 1:
		return l.pop()
	else:
		return "Bad magician!"

if __name__ == "__main__":
	solve_all()
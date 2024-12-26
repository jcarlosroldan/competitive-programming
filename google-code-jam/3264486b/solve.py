# https://code.google.com/codejam/contest/3264486/dashboard#s=p1

FNAME = "B-large"

def solve_all():
	# read the file
	with open("%s.in" % FNAME, "r") as f:
		lines = f.read().strip().split("\n")[1:]
	# join the lines in problems
	problems = map(int, lines)
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

num2list = lambda x: [int(d) for d in str(x)]
list2num = lambda x: int(''.join(map(str, x)))

def solve(N):
	number = num2list(N)
	D = len(number)
	for i in range(D):
		new_number = list(number)
		new_number[i+1:] = [new_number[i]] * (D - i - 1)
		if list2num(new_number) > N:
			new_number[i] -= 1
			new_number[i+1:] = [9] * (D - i - 1)
			return list2num(new_number)
	return N

if __name__ == "__main__":
	solve_all()
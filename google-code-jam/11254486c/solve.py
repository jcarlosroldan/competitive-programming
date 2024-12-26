# http://code.google.com/codejam/contest/11254486/dashboard#s=p2
from collections import defaultdict
from re import match
from numpy import array
from numpy.linalg import matrix_rank

def read_file(fname):
	res = []
	with open(fname,"r") as f:
		data = [l.strip() for l in f.readlines()][2:]
		problem = []
		for line in data:
			if match("\d+",line):
				res.append(problem)
				problem = []
			else:
				problem.append([p+str(k) for k,p in enumerate(line.split(" "))])
		res.append(problem)
	return res

def solve_all(fname):
	problems = read_file("%s.in" % fname)
	case = 1
	text = ""
	for p in problems:
		print("Solving Case #%s" % case)
		res = solve(p)
		text += "Case #%s: %s\n" % (case, res)
		case+=1
	with open("%s.out" % fname, "w") as out:
		out.write(text)

def solve(titles):
	print(titles)
	left = defaultdict(int)
	right = defaultdict(int)
	res = 0
	for w1, w2 in titles:
		left[w1] += 1
		right[w2] += 1
	s_l = sum(left.values()) - len(left.items())
	s_r = sum(right.values()) - len(right.items())
	if s_l < s_r:
		return s_l
	else:
		return s_r




solve_all("small3")
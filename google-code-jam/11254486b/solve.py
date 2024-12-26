# http://code.google.com/codejam/contest/11254486/dashboard#s=p1
from collections import defaultdict

def read_file(fname):
	with open(fname,"r") as f:
		data = [l.strip() for l in f.readlines()][1:]
	return data

def solve_all(fname):
	problems = read_file("%s.in" % fname)
	case = 1
	text = ""
	for p in problems:
		print("Solving Case #%s" % case)
		C, J = p.split(" ")
		res = solve(C, J)
		text += "Case #%s: %s\n" % (case, res)
		case+=1
	with open("%s.out" % fname, "w") as out:
		out.write(text)

def solve(C, J):
	N = int(C.replace("?","0"))-int(J.replace("?","0"))
	print(N)
	print(C,J)











solve_all("small")
# http://code.google.com/codejam/contest/4314486/dashboard#s=p1
from collections import defaultdict
from re import match
from numpy import array, argsort
from time import sleep
from numpy.linalg import matrix_rank
from igraph import Graph

def read_file(fname):
	res = []
	with open(fname,"r") as f:
		data = [l.strip() for l in f.readlines()][1:]
		for p in data:
			res.append(list(map(int, p.split(" "))))
	return res

def solve_all(fname):
	problems = read_file("%s.in" % fname)
	case = 1
	text = ""
	for J, P, S, K in problems:
		print("Solving Case #%s" % case)
		res = solve(J, P, S, K)
		text += "Case #%s: %s\n" % (case, res)
		case+=1
	with open("%s.out" % fname, "w") as out:
		out.write(text)

def solve(J, P, S, K):
	combs = []
	print(J, P, S, K)
	for s in range(1,S+1):
		for j in range(1,J+1):
			for p in range(1,P+1):
				combs.append([j,p,s])
	if K<3:
		reps = {}
		for j,p,s in combs:	reps[(j,p)] = reps.get((j,p),0) + 1
		for k, v in reps.items():
			if v>K:
				
		reps = {}
		for j,p,s in combs:	reps[(j,s)] = reps.get((j,s),0) + 1

		reps = {}
		for j,p,s in combs:	reps[(p,s)] = reps.get((p,s),0) + 1




	return str(len(combs))+"\n"+"\n".join(" ".join(map(str,l)) for l in combs)



solve_all("example")
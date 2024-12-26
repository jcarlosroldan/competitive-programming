#https://code.google.com/codejam/contest/6254486/dashboard#s=p2
from itertools import product
from math import sqrt

def get_divisor(n):
	n = int(n)
	if n == 2 or n == 3: return -1
	if n%2 == 0: return 2
	if n < 9: return -1
	if n%3 == 0: return 3
	r = int(sqrt(n))
	f = 5
	while f <= r:
		if n%f == 0: return f
		if n%(f+2) == 0: return f+2
		f +=6
	return -1

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
		N, J = map(int, p.split(" "))
		res = solve(N, J)
		text += "Case #%s:\n%s\n" % (case, res)
		case+=1
	with open("%s.out" % fname, "w") as out:
		out.write(text)

def to_base(binary, base):
	res = 0
	L = len(binary)
	for b in range(L):
		if binary[b]:
			res += base**(L-b-1)
	return res

def solve(N,J):
	total = 0
	res = []
	for i in product([0,1],repeat=N-2):
		n = [1]+list(i)+[1]
		r = []
		exit = False
		for base in range(2,11):
			p = get_divisor(to_base(n,base))
			if p == -1:
				exit = True
				break
			else:
				r.append(str(p))
		if exit:
			continue
		res.append("".join(map(str,n))+" "+" ".join(r))
		total += 1
		print("olee",to_base(n,2))
		if total == J:
			break
	return "\n".join(res)














solve_all("example")
#print(list(count(0)))
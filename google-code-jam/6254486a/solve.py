# https://code.google.com/codejam/contest/6254486/dashboard#s=p1



def read_file(fname):
	with open(fname,"r") as f:
		data = f.read().split("\n")[1:]
	return data

def solve_all(fname):
	problems = read_file("%s.in" % fname)
	case = 1
	text = ""
	for N in problems:
		print("Solving Case #%s" % case)
		res = solve(int(N))
		text += "Case #%s: %s\n" % (case, res)
		case+=1
	with open("%s.out" % fname, "w") as out:
		out.write(text)

def digits(n):
	return set(map(int,list(str(n))))

target = {0,1,2,3,4,5,6,7,8,9}
MAX_I = 1000000
def solve(N):
	seen = set()
	i = 1
	while i<MAX_I:
		seen.update(digits(i*N))
		if seen == target:
			return i*N
		else:
			i += 1
	return "INSOMNIA"

def divisors_less_than(n,m):
	return n//m +1


















solve_all("A-large")
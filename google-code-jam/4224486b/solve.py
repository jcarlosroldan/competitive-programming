# https://code.google.com/codejam/contest/4224486/dashboard#s=p1



def read_file(fname):
	with open(fname,"r") as f:
		data = [l.strip() for l in f.readlines()][1:]
	return zip(data[::2],data[1::2])

def solve_all(fname):
	problems = read_file("%s.in" % fname)
	case = 1
	text = ""
	for l1, l2 in problems:
		print("Solving Case #%s" % case)
		B, N = map(int, l1.split(" "))
		M = list(map(int, l2.split(" ")))
		res = solve(B, N, M)
		text += "Case #%s: %s\n" % (case, res)
		case+=1
	with open("%s.out" % fname, "w") as out:
		out.write(text)

def solve(B,N,M):
	wait = [0]*B
	queue_pos = N
	minute = 0
	while True:
		print("At minute %s" % minute)
		for k in range(0,B):
			if wait[k] == 0:
				queue_pos -= 1
				wait[k] = M[k]
				if queue_pos == 0:
					return k+1
		nxt = min(wait)
		wait = [w-nxt for w in wait]
		minute += nxt

def divisors_less_than(n,m):
	return n//m +1


















solve_all("example")
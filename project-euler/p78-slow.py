import sys, time

sys.setrecursionlimit(10**8)

results = {}
def P(x):
	return p(x,x)
def p(n,m):
	if m==1 or n<=1:
		return 1
	k = (n,m)
	if k in results:
		return results[k]
	elif m==2:
		res = int(n/2)+1
	else:
		res = p(n-m,min(m,n-m))+p(n,m-1)
	results[k] = res
	return res

t = time.time()
for i in range(1000000):
	if P(i)%1000000 == 0:
		print(i)
	if i%100 == 0:
		nt = time.time()
		print("%s\t%s"%(i,nt-t))
		t = nt
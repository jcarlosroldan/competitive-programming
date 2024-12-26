import sys, time

sys.setrecursionlimit(10**9)

def g(k):
	n = (k+1)//2
	res = n*(3*n-1)/2
	if k%2==0:
		res+=n
	return res

results = {}
def p(n):
	if n==0:
		return 1
	if n<0:
		return 0
	if n in results:
		return results[n]
	add = 0#0,1 add 2,3 substract
	gr = 1
	tot = 0
	k = 1
	while gr>=0:
		gr = n-g(k)
		if add<2:
			tot+=p(gr)
		else:
			tot-=p(gr)
		k+=1
		add = (add+1)%4
	results[n] = tot
	return tot

t = time.time()
for i in range(1000000):
	if p(i)%1000000 == 0:
		print("p(%s)=%s"%(i,p(i)))
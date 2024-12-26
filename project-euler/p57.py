import Euler

results = {}

def f(n):
	if n==1:
		return (3,2)
	if n in results:
		return results[n]
	f_prev = f(n-1)
	res = (f_prev[0]+2*f_prev[1],f_prev[0]+f_prev[1])
	results[n] = res
	return res

total = 0
for n in range(1,1001):
	res = f(n)
	if len(str(res[0]))>len(str(res[1])):
		total+=1
print(total)
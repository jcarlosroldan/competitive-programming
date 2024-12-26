# https://code.google.com/codejam/contest/6224486/dashboard#s=p0
import numpy as np

def split_each(line, n):
	return [int(line[i:i+n]) for i in range(0, len(line), n)]

def res_print(res):
	result.write("Case #%d: %s\n"%(problem,res))

filename = "A-large"
data = open("%s.in"%filename, "r")
result = open("%s.out"%filename, "w")
num_problems = int(data.readline())
for problem in range(1,num_problems+1):
	# loading
	#print("Case #%s"%problem)
	people = split_each(data.readline().split()[1],1)
	
	# problem
	clapping = 0
	friends = 0
	for s,p in enumerate(people):
		if p == 0:
			continue
		if s>friends+clapping:
			friends += s-(friends+clapping)
		clapping+=p

	print(people,friends)

	# printing
	res_print(friends)

result.close()
data.close()
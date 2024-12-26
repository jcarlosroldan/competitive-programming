# https://code.google.com/codejam/contest/6224486/dashboard#s=p0
import numpy as np
from math import floor, ceil

def res_print(res):
	result.write("Case #%d: %s\n"%(problem,res))

filename = "B-small-attempt3"
data = open("%s.in"%filename, "r")
result = open("%s.out"%filename, "w")
num_problems = int(data.readline())
for problem in range(1,num_problems+1):
	# loading
	print("Case #%s"%problem)
	data.readline()
	pancakes = [int(n) for n in data.readline().split(' ')]
	first_max = max(pancakes)
	# problem
	print(pancakes)
	special = 0
	last_special = 0
	last_biggest = 9999999999
	biggest = max(pancakes)
	min_result = 9999999
	while any(n>1 for n in pancakes):
		last_biggest = biggest
		last_special = special
		max_count = pancakes.count(last_biggest)
		pancakes = [ceil(last_biggest/2) if n == last_biggest else n for n in pancakes]+[floor(last_biggest/2)]*max_count
		biggest = max(pancakes)
		special+=max_count
		min_result = min(min_result,last_biggest+last_special)
		min_result = min(min_result,biggest+special)
		print(pancakes,special," + ",biggest)

	print(min(min_result,first_max))
	#printing
	res_print(min(min_result,first_max))

result.close()
data.close()
# https://code.google.com/codejam/contest/2984486/dashboard#s=p0&a=0
import numpy as np

def equals(outlets, devices):
	outlets_str = ["".join(map(str,outlet)) for outlet in outlets]
	outlets_str.sort()
	devices_str = ["".join(map(str,device)) for device in devices]
	devices_str.sort()
	return all(outlets_str[n] == devices_str[n] for n in range(0,len(devices_str)))

def diff(arr1, arr2):
	return [arr1[i] != arr2[i] for i in range(0,len(arr1))]

def apply(diff_vector, devices):
	dev_res = []
	for dev in devices:
		dev_res.append([1 if d else 0 for d in np.logical_xor(diff_vector, dev)])
	return dev_res

def res_print(res):
	result.write("Case #%d: %s\n"%(problem,res))

filename = "A-large-practice"
data = open("%s.in"%filename, "r")
result = open("%s.out"%filename, "w")
num_problems = int(data.readline())
for problem in range(1,num_problems+1):
	print("Case #%s"%problem)
	l = data.readline().split(" ")
	num_devices = int(l[0])
	num_digits = int(l[1])
	outlets = [list(map(int, list(out))) for out in data.readline().rstrip().split(" ")]
	devices = [list(map(int, list(dev))) for dev in data.readline().rstrip().split(" ")]
	results = []
	for dev in devices:
		diff_vector = diff(outlets[0],dev)
		if equals(apply(diff_vector, outlets),devices):
			results.append(np.sum(diff_vector))
	if len(results)==0:
		res_print("NOT POSSIBLE")
	else:
		res_print(min(results))

result.close()
data.close()
from itertools import product
from numpy import matrix

class Fractile:
	def __init__(self, original, C):
		self.original = original
		self.K = len(original)
		self.C = C
		self.final = self.transform()
	def step(self, fractile):
		res = []
		for f in fractile:
			if f:
				res.extend([True]*self.K)
			else:
				res.extend(self.original)
		return res
	def transform(self):
		res = self.original
		for _ in range(self.C-1):
			res = self.step(res)
		return res
	def __str__(self):
		return " ".join(["1" if t else "0" for t in self.final])

def check(matrix):
	return _check(matrix, [])

def explore(matrix):
	visited = []
	to_visit = [(matrix,set())]
	found = False
	res = []
	while len(to_visit):
		state_m, state_i = to_visit.pop(0)
		visited.append(state_i)
		for i in range(0,K**C):
			if all(state_m[:,i]):
				new_res = state_i | {i+1}
				if not new_res in res and (not found or len(new_res)==len(res[0])):
					res.append(new_res)
				found = True
		if not found:
			for i in range(0,K**C):
				m = (state_m + state_m[:,i])!=0
				i = state_i | {i+1}
				if i in visited or len(i)==len(state_i) or i in visited or i in to_visit: continue
				to_visit.append((m, i))
	return res

for K in range(5,10):
	for C in range(1,6):
		m = []
		for frac in product([True, False],repeat=K):
			if not any(frac): continue
			m.append(str(Fractile(frac,C)))
		a = matrix("; ".join(m))
		print(K, C, explore(a))
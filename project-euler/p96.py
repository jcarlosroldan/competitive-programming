from copy import deepcopy
import hashlib
md5 = lambda x: (hashlib.md5(x.encode()).hexdigest())

class Sudoku:
	def __init__(self,matrix):
		self.matrix = matrix
		self.possibilities = []
		self.remaining = 0
		self.valid = True
		for line in matrix:
			pos = []
			for elem in line:
				if elem == 0:
					pos.append([1,2,3,4,5,6,7,8,9])
					self.remaining += 1
				else:
					pos.append([elem])
			self.possibilities.append(pos)
	def from_string(string):
		inp = list(map(int, list(string.replace(".","0"))))
		return Sudoku([inp[i:i+9] for i in range(0,81,9)])
	def __str__(self):
		res = "Remaining: %s" % self.remaining
		if not self.valid:
			res += " [INVALID]"
		res += "\n"
		numbers = tuple(d if d!=0 else " " for line in self.matrix for d in line)
		res += "+-----------------+\n|%s %s %s|%s %s %s|%s %s %s|\n|%s %s %s|%s %s %s|%s %s %s|\n|%s %s %s|%s %s %s|%s %s %s|\n|-----+-----+-----|\n|%s %s %s|%s %s %s|%s %s %s|\n|%s %s %s|%s %s %s|%s %s %s|\n|%s %s %s|%s %s %s|%s %s %s|\n|-----+-----+-----|\n|%s %s %s|%s %s %s|%s %s %s|\n|%s %s %s|%s %s %s|%s %s %s|\n|%s %s %s|%s %s %s|%s %s %s|\n+-----------------+" % numbers
		return res
	def elimination(self):
		last_remaining = self.remaining
		while self.remaining > 0:
			self.elimination_step()
			if last_remaining == self.remaining:
				break
			last_remaining = self.remaining
	def elimination_step(self):
		y = 0
		for line in self.possibilities:
			unit_y = 3*(y//3)
			x = 0
			for elem in line:
				if len(elem)>1:
					unit_x = 3*(x//3)
					around = set(self.matrix[y]) #row
					around |= set(self.matrix[i][x] for i in range(9)) #col
					for i in range(unit_y,unit_y+3):
						for j in range(unit_x,unit_x+3):
							around.add(self.matrix[i][j]) #unit
					self.possibilities[y][x] = [n for n in elem if n not in around]
					if len(self.possibilities[y][x])==1:
						self.remaining -= 1
						self.matrix[y][x] = self.possibilities[y][x][0]
					elif len(self.possibilities[y][x])==0:
						self.valid = False
						return
				x += 1
			y += 1
	def update_valid(self):
		# row constraint
		for row in self.matrix:
			line = [r for r in row if r!=0]
			if len(line) != len(set(line)):
				self.valid = False
				return
		# col constraint
		for x in range(9):
			line = [self.matrix[i][x] for i in range(9) if self.matrix[i][x]!=0]
			if len(line) != len(set(line)):
				self.valid = False
				return
		# unit constraint
		units = [[] for _ in range(9)]
		for u_x in range(9):
			for u_y in range(9):
				v = self.matrix[u_y][u_x]
				if v!=0:
					i = 3*(u_x//3) + (u_y//3)
					units[i].append(v)
		for unit in units:
			if len(unit) != len(set(unit)):
				self.valid = False
				return
	def next(self):
		x,y = next((x,y) for y in range(0,9) for x in range(0,9) if len(self.possibilities[y][x])>1)
		tot = len(self.possibilities[y][x])
		res = []
		for option in range(tot):
			r = deepcopy(self)
			v = r.possibilities[y][x][option]
			r.possibilities[y][x] = [v]
			r.matrix[y][x] = v
			r.remaining -= 1
			res.append(r)
		return res
	def solve(self):
		res = self._solve()
		if res == None:
			self.valid = False
		else:
			self.matrix = res.matrix
			self.possibilities = res.possibilities
			self.remaining = res.remaining
			self.valid = res.valid
	def _solve(self):
		self.elimination()
		self.update_valid()
		if self.valid:
			if self.remaining > 0:
				ss = self.next()
				m = None
				for s in ss:
					m = s._solve()
					if m != None:
						return m
			else:
				return self
	def all_solutions(self):
		return self._all_solutions(deepcopy(self))
	def _all_solutions(self,sud):
		self.elimination()
		self.update_valid()
		if self.valid:
			if self.remaining > 0:
				ss = self.next()
				res = []
				for s in ss:
					candidate = s.all_solutions()
					if candidate!=None:
						res.extend(candidate)
				if len(res)>1:
					print("Not unique")
				return res
			else:
				return [self]
		return []

def p96():
	sudokus = []
	with open("res/p96_sudoku.txt","r") as f:
		lines = f.read().split("\n")

	for i in range(1,len(lines),10):
		sudokus.append(Sudoku([list(map(int,list(l))) for l in lines[i:i+9]]))

	[sud.solve() for sud in sudokus]
	res = [sud.matrix[0][0:3] for sud in sudokus]
	res = [h*100+d*10+u for h,d,u in res]
	print(sum(res))

p96()
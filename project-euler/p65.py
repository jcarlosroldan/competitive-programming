class Fraction:
	def __init__(self, num, den=1):
		assert den != 0
		self.num = num
		self.den = den
		# self.reduce() # XXX commented for P65

	def reduce(self):
		gcd = Fraction.gcd(self.num, self.den)
		self.num = int(self.num / gcd)
		self.den = int(self.den / gcd)

	def gcd(a, b):
		if b == 0:
			return a
		else:
			return Fraction.gcd(b, a % b)

	def inverse(self):
		return Fraction(self.den, self.num)

	def real(self):
		return self.num / self.den

	def __add__(self, other):
		num = self.num * other.den + other.num * self.den
		den = self.den * other.den
		return Fraction(num, den)

	def __sub__(self, other):
		num = self.num * other.den - other.num * self.den
		den = self.den * other.den
		return Fraction(num, den)

	def __truediv__(self, other):
		num = self.num * other.den
		den = self.den * other.num
		return Fraction(num, den)

	def __mul__(self, other):
		num = self.num * other.num
		den = self.den * other.den
		return Fraction(num, den)

	def __pow__(self, exp):
		num = self.num ** exp
		den = self.den ** exp
		return Fraction(num, den)

	def __eq__(self, other):
		return self.num == other.num and self.den == other.den

	def __str__(self):
		return "%s/%s" % (self.num, self.den)

def problem65(size=100):
	den_list = [[1, 2 * n, 1] for n in range(1, size)]
	den_list = [2] + [x for ls in den_list for x in ls]
	for sz in range(size):
		n = Fraction(den_list[sz])
		for m in reversed(den_list[:sz]):
			n = Fraction(m) + n.inverse()
	res = sum(int(n) for n in str(n.num))
	print("%sth: %s. Sum of numerator: %s" % (size, n, res))


problem65(10)
problem65(100)
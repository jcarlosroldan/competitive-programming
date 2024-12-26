DEBUG = False
# -- jam i/o ---------------------------------------------------------------- #

_lines = None
def next_line():
	global _lines
	if DEBUG:
		if _lines is None:
			with open("sample.in", "r") as fp:
				_lines = fp.read().strip().split("\n")
		return _lines.pop(0)
	else:
		return input()

def solve_all():
	for p in range(int(next_line())):
		next_line()
		ants = list((map(int, next_line().split())))
		print("Case #%s: %s" % (p + 1, solve(ants)))

# -- jam specific functions ------------------------------------------------- #

"""class DynProg:
	def __init__(self, ants):
		self.initial_state = ants

	def alternatives(self, state):
		for n in range(len(state)):
			return state[:n] + state[n + 1:]

	def score(self, state):
		return [len(state), -sum(1 for n in range(len(state)) if state[n] * 6 < sum(state[:n])), sum(state)]

	def is_final(self, state):
		return self.score(state)[1] == 0"""

def solve(ants):
	res = ants
	try:
		n = next(n for n, a in enumerate(ants) if sum(res[:n]) > a * 6)
		m = max(range(n + 1), key=lambda x: res[x])
		return max(solve(ants[:n] + ants[n + 1:]), solve(ants[:m] + ants[m + 1:]))
	except:
		return len(res)

# -- entrypoint ------------------------------------------------------------- #

if __name__ == "__main__":
	solve_all()
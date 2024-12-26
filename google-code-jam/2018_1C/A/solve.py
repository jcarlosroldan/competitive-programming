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
		N, L = map(int, next_line().split())
		words = []
		for w in range(N):
			words.append(next_line())
		print("Case #%s: %s" % (p + 1, solve(N, L, words)))

# -- jam specific functions ------------------------------------------------- #

def solve(N, L, words):
	if L == 1: return "-"
	# build forbidden combinations set
	forbidden = set()
	for word in words:
		previous = None
		for n, letter in enumerate(word):
			if n > 0: forbidden.add((n, previous, letter))
			previous = letter
	# build available letters set
	letters = []
	for l in range(L): letters.append(set(w[l] for w in words))
	# find one non-used pair
	res = words[0]
	for n in range(L - 1):
		for l1 in letters[n]:
			for l2 in letters[n + 1]:
				if (n + 1, l1, l2) not in forbidden:
					return res[:n] + l1 + l2 + res[n + 2:]
	return "-"

def generate_word(n, letters, forbidden, last_letter):
	for l in letters[0]:
		w = generate_word(n + 1, letters, forbidden)

# -- entrypoint ------------------------------------------------------------- #

if __name__ == "__main__":
	solve_all()
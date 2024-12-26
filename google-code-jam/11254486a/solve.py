# http://code.google.com/codejam/contest/11254486/dashboard#s=p0
from collections import defaultdict

def read_file(fname):
	with open(fname,"r") as f:
		data = [l.strip() for l in f.readlines()][1:]
	return data

def solve_all(fname):
	problems = read_file("%s.in" % fname)
	case = 1
	text = ""
	for p in problems:
		print("Solving Case #%s" % case)
		letters = list(p)
		res = solve(letters)
		text += "Case #%s: %s\n" % (case, res)
		case+=1
	with open("%s.out" % fname, "w") as out:
		out.write(text)

numbers = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
def solve(letters):
	freqs = defaultdict(int)
	res = ""
	for letter in letters:
		freqs[letter] += 1
	# Zero
	reps = freqs["Z"]
	res += "0"*reps
	for c in list(numbers[0]):
		freqs[c] -= reps
	# siX
	reps = freqs["X"]
	res += "6"*reps
	for c in list(numbers[6]):
		freqs[c] -= reps
	# eiGht
	reps = freqs["G"]
	res += "8"*reps
	for c in list(numbers[8]):
		freqs[c] -= reps
	# tWo
	reps = freqs["W"]
	res += "2"*reps
	for c in list(numbers[2]):
		freqs[c] -= reps
	# foUr
	reps = freqs["U"]
	res += "4"*reps
	for c in list(numbers[4]):
		freqs[c] -= reps
	# Five
	reps = freqs["F"]
	res += "5"*reps
	for c in list(numbers[5]):
		freqs[c] -= reps
	# seVen
	reps = freqs["V"]
	res += "7"*reps
	for c in list(numbers[7]):
		freqs[c] -= reps
	# Three
	reps = freqs["T"]
	res += "3"*reps
	for c in list(numbers[3]):
		freqs[c] -= reps
	# nIne
	reps = freqs["I"]
	res += "9"*reps
	for c in list(numbers[9]):
		freqs[c] -= reps
	# One
	reps = freqs["O"]
	res += "1"*reps
	for c in list(numbers[1]):
		freqs[c] -= reps

	return "".join(sorted(res))


solve_all("large")
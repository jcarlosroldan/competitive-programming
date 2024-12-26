from simpler import load, mem_cache
from sys import setrecursionlimit

setrecursionlimit(10000)

test = [t for t in load('Object DNA Traces.txt').split('\n')[1::3]]
samples = load('Suspects And Victim Dna Samples.txt').split('\n')
samples = {k: v for k, v in zip(samples[::3], samples[1::3])}
samps = [t[s:s+20] for t in test for s in range(len(t) - 20)]

_lps_x = None
def lps(x):
	''' Longest Palindrome Substring of a string. '''
	global _lps_x
	_lps_x = x
	return _lps(0, len(x) - 1)

def _lps(i, j):
	if i > j: return 0
	if i == j: return 1
	if _lps_x[i] == _lps_x[j]:
		return 2 + _lps(i + 1, j - 1)
	else:
		return max(_lps(i + 1, j), _lps(i, j - 1))

_lcps_x, _lcps_y = None, None
def lcps(x, y):
	''' Longest Common Palindrome Subsequence of two strings. '''
	global _lcps_x, _lcps_y
	_lcps_x, _lcps_y = x, y
	return _lcps(0, len(x) - 1, 0, len(y) - 1)

@mem_cache
def _lcps(i, j, k, l, d=0):
	print(' '*d,i,j,k,l)
	if i > j or k > l: return 0
	if i == j and k == l and _lcps_x[i] == _lcps_x[j] == _lcps_y[k] == _lcps_y[l]: return 1
	if i < j and k < l and _lcps_x[i] == _lcps_x[j] == _lcps_y[k] == _lcps_y[l]: return 2 + _lcps(i+1, j-1, k+1, l-1, d+1)
	return max(_lcps(i + 1, j, k, l, d+1), _lcps(i, j - 1, k, l, d+1), _lcps(i, j, k + 1, l, d+1), _lcps(i, j, k, l - 1, d+1))

print(lps(test[0]))
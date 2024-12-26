from utils import *

# data = 'A C G T\n2'

alphabet, ln = data.split('\n')
alphabet = alphabet.split(' ')

res = alphabet.copy()
for _ in range(int(ln) - 1):
	res = [symbol + word for symbol in alphabet for word in res]
save('\n'.join(res))
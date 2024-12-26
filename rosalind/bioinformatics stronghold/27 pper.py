from utils import *
from math import factorial
from scipy.special import comb

# data = '21 7'

n, k = map(int, data.split(' '))
save(int(comb(n, k) * factorial(k) % 1e6))
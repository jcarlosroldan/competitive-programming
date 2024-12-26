from utils import *

# data = '1 0 0 1 0 1'

amounts = list(map(int, data.split(' ')))
probs = [1, 1, 1, 3 / 4, 1 / 2, 0]
probs = sum(2 * prob * amount for prob, amount in zip(probs, amounts))
save(probs)
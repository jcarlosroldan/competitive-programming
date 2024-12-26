from utils import *

# data = '2 2 2'

k, m, n = map(int, data.split(' '))
tot = k + m + n
# Compute P(k, *) + 3/4 * P(m, m) + 1/2 * P(m, n)
save(
	k / tot + k / (tot - 1) - k**2 / (tot * (tot - 1)) +
	+ (3 / 4) * (m / tot) * ((m - 1) / (tot - 1)) +
	+ (1 / 2) * (
		(m / tot) * (n / (tot - 1)) +
		+ (n / tot) * (m / (tot - 1))
	)
)
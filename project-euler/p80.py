from decimal import getcontext, Decimal

getcontext().prec = 102

def digital_sum(n):
	root = Decimal(n).sqrt()
	if root%1 != 0:
		return sum(int(d) for d in str(root*10**100)[:100])
	else:
		return 0

print(sum(digital_sum(n) for n in range(1,101)))
import Euler

side = lambda x: 1+2*x
d1 = lambda x: (1+2*x)**2 #bottom right
d2 = lambda x: d1(x)-2*x #bottom left
d3 = lambda x: d1(x)-4*x #top left
d4 = lambda x: d1(x)-6*x #top right

total_primes = 0
x = 0
while True:
	x += 1
	if Euler.is_prime(d1(x)):
		total_primes+=1
	if Euler.is_prime(d2(x)):
		total_primes+=1
	if Euler.is_prime(d3(x)):
		total_primes+=1
	if Euler.is_prime(d4(x)):
		total_primes+=1
	ratio = total_primes/(4*x+1)
	if ratio<0.1:
		print(side(x))
		break
from math import sqrt

get_x = lambda D,y: sqrt(1+D*y**2)
max_D = 1000

for D in range(1,max_D+1):
	if sqrt(D)%1>0:
		y = 0
		x = 0.5
		while x%1>0:
			y+=1
			x = get_x(D,y)
		print("x=%s, D=%s, y=%s"%(x,D,y))
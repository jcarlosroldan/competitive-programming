tot = lambda x: sum(range(0,x+1))
n = lambda w,h: tot(w)*tot(h)

area = None
distance = float("inf")

for i in range(0,100):
	for j in range(i,100):
		dist = abs(n(i,j)-2000000)
		if dist<distance:
			distance = dist
			area = i*j

print(area,distance)
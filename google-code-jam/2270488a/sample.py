#link: https://code.google.com/codejam/contest/2270488/dashboard#s=a&a=1

problem = 'A'
problem = 'B'
#problem = 'C'
#problem = 'D'

size = 'small'
size = 'large'
#size = 'example'

dataset = open('%s-%s.in' % (problem, size), 'r')
output = open('%s-%s.out' % (problem, size), 'w')
T = int(dataset.readline()) #number of test cases

for t in range(T):
	#problem solving follows
	N, M = map(int, dataset.readline().split())


	lawn = [list(map(int, dataset.readline().split())) for _ in range(N)]
	my_lawn = [[max(lawn[n])]*M for n in range(N)]

	for m in range(M):
		max1 = max([row[m] for row in lawn])
		for n in range(N):
			if (my_lawn[n][m]>max1):
				my_lawn[n][m] = max1


	output.write("Case #%s: %s\n"%(t+1, "YES" if lawn==my_lawn else "NO"))
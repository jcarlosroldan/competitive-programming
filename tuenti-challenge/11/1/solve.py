from simpler import load, save

MODE = 'submit'

res = []
for p, problem in enumerate(load('%sInput.txt' % MODE).strip().split('\n')[1:], 1):
	total = sum(map(int, problem.split(':')))
	res.append('Case #%d: %s' % (p, total + 1 if total < 12 else '-'))

save('%sOutput.txt' % MODE, '\n'.join(res))
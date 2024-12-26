def damage(program):
	res = 0
	force = 1
	for p in program:
		if p:
			res += force
		else:
			force *= 2
	return res

problems = int(input())

for n in range(1, problems + 1):
	res = "IMPOSSIBLE"
	# read problem
	inp = input().split(" ")
	shield, program = int(inp[0]), [e == "S" for e in inp[1]]
	# solve it
	changes = 0
	while damage(program) > shield:
		try:
			i = next(n for n in range(len(program) - 1, 0, -1) if program[n] and not program[n - 1])
			program[i], program[i - 1] = program[i - 1], program[i]
			changes += 1
		except:
			break
	else:
		res = changes
	print("Case #%s: %s" % (n, res))
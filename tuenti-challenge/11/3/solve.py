FNAME = 'submit'

def main():
	output = ''
	for p, problem in enumerate(load_input(), 1):
		print('Solving case #%d' % p)
		output += 'Case #%d: %s\n' % (p, solve(*problem))
	with open('%sOutput.txt' % FNAME, 'w', encoding='utf-8') as fp:
		fp.write(output)

def load_input():
	with open('%sInput.txt' % FNAME, 'r', encoding='utf-8') as fp:
		problems = int(fp.readline())
		for _ in range(problems):
			words, scores = fp.readline().strip().split('|')
			yield *words.split('-'), scores

def solve(word1, word2, score):
	if score[0] == '[':
		score = {k: v for k, v in eval(score)}
	elif score[0] == '{':
		score = eval(score)
	else:
		score = [kv.split('=') for kv in score.split(',')]
		score = {k: eval(v) for k, v in score}
	score1 = sum(score[c] for c in word1)
	score2 = sum(score[c] for c in word2)
	return word1 if score1 > score2 else '-' if score1 == score2 else word2

if __name__ == '__main__':
	main()
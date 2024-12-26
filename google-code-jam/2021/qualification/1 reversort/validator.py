from os import listdir

input_file = None
def input():
	global input_file
	if input_file is None:
		with open(next(f for f in listdir() if 'input' in f), 'r', encoding='utf-8') as fp:
			input_file = fp.read().strip().split('\n')
	res, *input_file = input_file
	return res

_print = print
print_file = []
def print(text):
	print_file.append(text)

def check():
	with open(next(f for f in listdir() if 'output' in f), 'r', encoding='utf-8') as fp:
		output_file = fp.read().strip().split('\n')
	for print_line, output_line in zip(print_file, output_file):
		if print_file == output_file:
			_print(print_line)
		else:
			_print('%s [FAIL]\n%s [EXPECTED]' % (print_line, output_line))
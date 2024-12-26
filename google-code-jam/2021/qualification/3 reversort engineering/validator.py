from os import listdir

input_file = None
output_file = None
def input():
	global input_file, output_file
	if input_file is None:
		with open(next(f for f in listdir() if 'input' in f), 'r', encoding='utf-8') as fp:
			input_file = fp.read().strip().split('\n')
		with open(next(f for f in listdir() if 'output' in f), 'r', encoding='utf-8') as fp:
			output_file = fp.read().strip().split('\n')
	res, *input_file = input_file
	return res

_print = print
print_file = []
def print(text):
	global output_file
	expected, *output_file = output_file
	if text == expected:
		_print(text)
	else:
		_print('%s [FAIL]\n%s [EXPECTED]' % (text, expected))
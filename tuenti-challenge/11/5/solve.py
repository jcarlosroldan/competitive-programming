from re import findall

LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

with open('Invictus.txt', 'rb') as fp:
	data = fp.read()

message = [int(char[0]) * 256 + int(char[1]) for char in findall(b'\xf3\xa0(..)', data)]
message = [m - min(message) + 17 for m in message]
message = ''.join([LETTERS[m] if m < len(LETTERS) else LETTERS[m - 0xC0] for m in message])

with open('solve.txt', 'w') as fp:
	fp.write(message)
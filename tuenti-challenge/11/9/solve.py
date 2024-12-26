from numpy import array, any

FNAME = 'submit'
SPRITES = []
EXTRA_OFFSET = []

def main():
	output = ''
	for p, problem in enumerate(load_input(), 1):
		if p == 4: break
		print('Solving case #%d' % p)
		output += 'Case #%d: %s\n' % (p, solve(problem, SPRITES, EXTRA_OFFSET))
	with open('%sOutput.txt' % FNAME, 'w', encoding='utf-8') as fp:
		fp.write(output)

def load_input():
	with open('%sInput.txt' % FNAME, 'r', encoding='utf-8') as fp:
		problems = int(fp.readline())
		for _ in range(int(fp.readline())):
			_, r = map(int, fp.readline().split(' '))
			sprite = array([list(map(int, fp.readline().strip())) for _ in range(r)], dtype='bool')
			sprite, off_row, off_col = crop(sprite)
			SPRITES.append(sprite)
			EXTRA_OFFSET.append((off_row, off_col))
		for _ in range(problems):
			yield [tuple(map(int, fp.readline().strip().split(' '))) for _ in range(int(fp.readline()))]

def crop(sprite):
	# offset from the start
	off_row = off_col = 0
	for row in range(sprite.shape[0]):
		if any(sprite[row]):
			off_row = row
			break
	for col in range(sprite.shape[1]):
		if any(sprite[:, col]):
			off_col = col
			break
	sprite = sprite[off_row:, off_col:]
	# offset from the end
	for row in range(sprite.shape[0] - 1, -1, -1):
		if any(sprite[row]):
			sprite = sprite[:row + 1, :]
			break
	for col in range(sprite.shape[1] - 1, -1, -1):
		if any(sprite[:, col]):
			sprite = sprite[:, :col + 1]
			break
	return sprite, off_row, off_col

def solve(locations, sprites, extra_offset):
	res = 0
	for l1 in range(len(locations)):
		i1, x1, y1 = locations[l1]
		shape1, off1 = sprites[i1], extra_offset[i1]
		for l2 in range(l1 + 1, len(locations)):
			i2, x2, y2 = locations[l2]
			shape2, off2 = sprites[i2], extra_offset[i2]
			x_start = max(x1 + off1[1], x2 + off2[1])
			y_start = max(y1 + off1[0], y2 + off2[0])
			x_end = min(x1 + off1[1] + shape1.shape[1], x2 + off2[1] + shape2.shape[1])
			y_end = min(y1 + off1[0] + shape1.shape[0], y2 + off2[0] + shape2.shape[0])
			if x_start >= x_end or y_start >= y_end:
				continue
			if any(
				shape1[y_start - y1 - off1[0]:y_end - y1 - off1[0], x_start - x1 - off1[1]:x_end - x1 - off1[1]] &
				shape2[y_start - y2 - off2[0]:y_end - y2 - off2[0], x_start - x2 - off2[1]:x_end - x2 - off2[1]]
			):
				res += 1
	return res

if __name__ == '__main__':
	main()
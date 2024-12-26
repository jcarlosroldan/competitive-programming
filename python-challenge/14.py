from requests import get
from PIL import Image
from io import BytesIO

url = "http://huge:file@www.pythonchallenge.com/pc/return/wire.png"
img = Image.open(BytesIO(get(url).content))
spiral = Image.new(img.mode, (100, 100))
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
x, y = -1, 0
_dir = 0
length = 100
times = 1
i = 0
while length > 0:
	for _ in range(length):
		x = x + dirs[_dir][0]
		y = y + dirs[_dir][1]
		spiral.putpixel((x,y), img.getpixel((i,0)))
		i += 1
	_dir = (_dir + 1) % 4
	times -= 1
	if times == 0:
		times = 2
		length -= 1
spiral.show()
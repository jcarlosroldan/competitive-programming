from requests import get
from PIL import Image
from io import BytesIO

is_pink = lambda c: c[0] == c[2] == 255 and c[1] == 0
url = "http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif"
img = Image.open(BytesIO(get(url).content)).convert('RGB')
aligned = Image.new(img.mode, (1300, 500))
w, h = img.size
x, y = 0, 0
on_pink = False
for p in range(w*h):
	c = img.getpixel((p%w, p//w))
	if is_pink(c):
		on_pink = True
	else:
		if on_pink:
			on_pink = False
			y += 1
			x = 0
		else:
			x += 1
			aligned.putpixel((x, y), c)
aligned.show()
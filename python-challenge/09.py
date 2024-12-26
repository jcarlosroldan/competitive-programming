from requests import get
from PIL import Image
from io import BytesIO
from re import findall
from PIL import Image,ImageDraw

url = "http://www.pythonchallenge.com/pc/return/good.html"
page = get(url, auth=('huge', 'file')).text
_, first, second = findall("<\!--([\s\S]+?)-->", page)[1].strip().split("\n\n")
first = list(map(int, findall("\d+", first)))
second = list(map(int, findall("\d+", second)))
img = Image.new('RGB', [max(first + second)]*2)
draw = ImageDraw.Draw(img)
draw.polygon(first)
draw.polygon(second)
img.show()
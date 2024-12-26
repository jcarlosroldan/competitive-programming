from requests import get
from PIL import Image, ImageOps
from io import BytesIO
from re import findall

url = "http://www.pythonchallenge.com/pc/return/cave.jpg"
img = Image.open(BytesIO(get(url, auth = ("huge", "file")).content))
w, h = img.size
img.crop((1,1,w,h))
img.thumbnail((w//2, h//2), Image.NEAREST)
ImageOps.equalize(img).show()
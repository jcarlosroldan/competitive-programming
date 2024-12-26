from requests import get
from PIL import Image
from io import BytesIO
from re import findall

url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
img = Image.open(BytesIO(get(url).content))
grays = [img.getpixel((i,50))[0] for i in range(0,img.width,7)][:-3]
text = "".join([chr(c) for c in grays])
grays = findall("\d+", text)
print("".join([chr(int(c)) for c in grays]))
print(" ".join([c for c in grays]))
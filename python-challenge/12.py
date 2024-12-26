from requests import get
from PIL import Image, ImageFile
from io import BytesIO

# aquí meter captura del hex viewer de notepad++
# leyendo la wiki me enteré de que las pilas de cartas eran para bla, bla, bla y que si seguíamos llegábamos a bert is evil print(sp.system.listMethods())
url = "http://www.pythonchallenge.com/pc/return/evil2.gfx"
img = get(url, auth = ("huge", "file")).content
ImageFile.LOAD_TRUNCATED_IMAGES = True
[Image.open(BytesIO(img[i::5])).show() for i in range(5)]
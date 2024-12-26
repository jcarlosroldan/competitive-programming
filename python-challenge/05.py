from requests import get
from pickle import loads

page = get("http://www.pythonchallenge.com/pc/def/banner.p").content
pobj = loads(page)
for line in pobj:
	print("".join([char * times for char, times in line]))
from requests import get
from re import findall
from io import BytesIO
from zipfile import ZipFile

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
zf = ZipFile(BytesIO(get(url).content))
comments = bytes()

def jump(number):
	global comments
	text = zf.read("%s.txt" % number).decode()
	comments += zf.getinfo("%s.txt" % number).comment
	matches = findall("\d+",text)
	if len(matches) > 0:
		return jump(matches[-1])
	elif "Divide by two" in text:
		return jump(int(number)/2)
	else:
		print(text)

jump(90052)
print(comments.decode())
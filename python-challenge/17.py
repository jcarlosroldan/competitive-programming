from requests import get
from urllib.parse import unquote_to_bytes
from re import findall
from bz2 import decompress
from xmlrpc.client import ServerProxy

# Step 1: Follow the chain
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s"
info = ""
def jump(nothing):
	global info
	print(nothing)
	page = get(url % nothing)
	info += page.cookies["info"]
	text = page.text
	matches = findall("\d+",text)
	if len(matches) > 0:
		return jump(matches[-1])
	elif "Divide by two" in text:
		return jump(int(nothing)/2)
	else:
		print(text)
jump("12345")

# Step 2: Decompress the message
print(decompress(unquote_to_bytes(info.replace("+", " "))))

# Step 3: Call the father
sp = ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(sp.phone('Leopold'))

# Step 4: Tell him the message
url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
print(get(url).text)
print("UNFINISHED LEVEL")
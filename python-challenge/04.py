from requests import get
from re import findall

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

def jump(nothing):
	print(nothing)
	text = get(url % nothing).text
	matches = findall("\d+",text)
	if len(matches) > 0:
		return jump(matches[-1])
	elif "Divide by two" in text:
		return jump(int(nothing)/2)
	else:
		print(text)

jump("12345")
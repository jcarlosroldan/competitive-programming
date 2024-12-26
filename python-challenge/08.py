from requests import get
from re import findall
from bz2 import decompress

page = get("http://www.pythonchallenge.com/pc/def/integrity.html").text
un, pw = findall("<\!--([\s\S]+?)-->", page)[0].strip().split("\n")
print(decompress(eval("b"+un[4:])))
print(decompress(eval("b"+pw[4:])))
from requests import get
from re import findall

page = get("http://www.pythonchallenge.com/pc/def/equality.html").text
mess = findall("<\!--([\s\S]+?)-->", page)[0].strip()
print("".join(findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", mess)))
from requests import get
from re import findall

page = get("http://www.pythonchallenge.com/pc/def/ocr.html").text
comments = findall("<\!--([\s\S]+?)-->", page)
mess = "".join(findall("[a-z]", comments[1]))
print(mess)
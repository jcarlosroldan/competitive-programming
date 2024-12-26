from requests import get
from re import findall

page = get("http://www.pythonchallenge.com/pc/def/map.html").text
text = findall('<font color="#f000f0">([\s\S]+?)</tr>', page)[0].strip()
frm = "abcdefghijklmnopqrstuvwxyz"
to =  "cdefghijklmnopqrstuvwxyzab"
trans = str.maketrans(frm,to)
print(text.translate(trans))
print("map".translate(trans))
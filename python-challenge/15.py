from requests import get
from re import findall
from datetime import date

page = get("https://en.wikipedia.org/wiki/January_27").text
people = findall('<li><a href="/wiki/(1\d+6)" title="\d+">\d+</a> – <a href="/wiki/([^"]+)', page)

for y, p in people:
	if date(int(y),1,1).weekday() == 3:
		print(p)
		break
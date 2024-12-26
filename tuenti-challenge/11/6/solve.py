from babel.dates import get_day_names
from datetime import datetime as dt

FNAME = 'submit'
LANGS = {'CA': 'ca', 'CZ': 'cs', 'DE': 'de', 'DK': 'da', 'EN': 'en', 'ES': 'es', 'FI': 'fi', 'FR': 'fr', 'GR': 'el', 'HU': 'hu', 'IS': 'is', 'IT': 'it', 'NL': 'nl', 'PL': 'pl', 'RO': 'ro', 'RU': 'ru', 'SE': 'sv', 'SI': 'sl', 'SK': 'sk', 'VI': 'vi'}
FINNISH = 'maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai'

def main():
	output = ''
	for p, problem in enumerate(load_input(), 1):
		print('Solving case #%d' % p)
		output += 'Case #%d: %s\n' % (p, solve(*problem))
	with open('%sOutput.txt' % FNAME, 'w', encoding='utf-8') as fp:
		fp.write(output)

def load_input():
	with open('%sInput.txt' % FNAME, 'r', encoding='utf-8') as fp:
		problems = int(fp.readline())
		for _ in range(problems):
			yield fp.readline().strip().split(':')

def solve(date, lang):
	if lang not in LANGS:
		return 'INVALID_LANGUAGE'
	else:
		try:
			if date[4] == '-':
				res = dt.strptime(date, '%Y-%m-%d')
			else:
				res = dt.strptime(date, '%d-%m-%Y')
		except:
			return 'INVALID_DATE'
		if lang == 'FI':
			res = FINNISH[res.weekday()]
		else:
			res = get_day_names('wide', locale=LANGS[lang])[res.weekday()].lower()
			if lang == 'RO': res = res.replace('ț', 'ţ')
		return res

if __name__ == '__main__':
	main()
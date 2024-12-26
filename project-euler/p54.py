from Euler import is_prime, prime_sieve
from random import getrandbits
class Scorer:
	def p1_wins(play):
		if Scorer.score(play[0])>Scorer.score(play[1]):
			return True
		else:
			return False
	def most_repeated_number(hand):
		reps = [0,0,0,0,0,0,0,0,0,0,0,0,0]
		for card in hand:
			reps[card[0]]+=1
		return reps.index(max(reps))
	def score(hand):
		res = 0
		if Scorer.royal_flush(hand):
			res = 1000
		elif Scorer.straight_flush(hand):
			res = 900
		elif Scorer.four(hand):
			res = 800
		elif Scorer.full(hand):
			res = 700
		elif Scorer.flush(hand):
			res = 600
		elif Scorer.straight(hand):
			res = 500
		elif Scorer.three(hand):
			res = 400
		elif Scorer.double_pair(hand):
			res = 300
		elif Scorer.single_pair(hand):
			res = 200
		return res+Scorer.most_repeated_number(hand)
	def royal_flush(hand):
		return False
	def straight_flush(hand):
		return False
	def four(hand):
		return False
	def full(hand):
		return False
	def flush(hand):
		return False
	def straight(hand):
		return False
	def three(hand):
		return False
	def double_pair(hand):
		return False
	def single_pair(hand):
		return False


plays = []
with open("res/p54_poker.txt","r") as infile:
	suits = ['C','D','H','S']
	numbers = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
	for line in infile.readlines():
		play = [[],[]]
		cards = line[:-1].split(" ")
		for card in cards[:5]:
			play[0].append((numbers.index(card[0]),suits.index(card[1])))
		for card in cards[5:]:
			play[1].append((numbers.index(card[0]),suits.index(card[1])))
		plays.append(play)

wins = 0
for play in plays:
	if Scorer.p1_wins(play):
		wins+=1
print(wins)
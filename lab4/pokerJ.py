# -*- coding: utf-8 -*-

#	Poker game by Node
#
#
#	We are going to use representants for all the 52 cards we use in poker
#		Suit: S = Spades, H = Hearts, D = Diamonds, C = Clubs 
#		Rank: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
#
#	Notater til Node (Fjernes for innlevering):
#		Les Lab4 oppgavetekst noye
#		Folg Udacity kurset som Janis la ut og snakker om i oppgaveteksten
#		Importer random. Vi kan bruke funksjoner som shuffle() som stokker
#		innehold i en variabel
#		Bruke max() funksjon: max("A", 3) = A
#								max('6C', 'QC') = 'QC'
#							tuples: 	max((3, 2), (11, 2)) = (11, 2)
#
#		Skriv en funksjon for å bestemme hvordan max() skal sortere input.
#		Default er ascii men man kan lage en egen funksjon for hvordan input
#		skal bli prioritert. 
#				print max([3, 4, -5, 0], key = abs) max will 
#												sort according to the abs function
#
#		join() og split() funksjoner
#		
#		
# 	max() 
#		returns the highest value available in a list
#		max([3, 4, -5]) 
#		returns 4 		
#
#	abs() 
#		returns the absolute value of a number, -5 is more than 4
#		max([10, 2, -12], key=abs) <- adds a key to max function
#		returns -12 as the absolute value of -12 is 12
#


import random

deck = []

def poker(hands):
	"Return the winner hand. poker([hand,...]) => hand"
	return max(hand, key=hand_rank) 

def hand_rank(hand):
	ranks = card_ranks(hand)
	if straight(ranks) and flush(hand):
		return (8, max(ranks))
	elif fk(4, ranks):
		return (7, kind(4, ranks), kind(1, ranks))
	elif pass 



def test():
	"Test that our functions work"
	sf = "6C 7C 8C 9C TC".split() # straight flush
	fk = "9D 9H 9S 9C 7D".split() # four of a kind
	fh = "TD TC TH 7C 7D".split() # full house

	# we assert that our function returns True
	# test wheter the winner between 4 of a kind and full house is correct
	assert ([fk, fh]) == fk 
	# test if we have 2 copies of full house playing each other
	assert ([fh, fh]) == fh 

	# decides the best hand
	assert poker([sf, fk, fh) == sf
	assert poker([sf]) == sf
	assert poker([sf], 99*[fk]) == sf

	# we rank our hands in poker()
	assert poker([sf]) == 8
	assert poker([fk]) == 7
	assert poker([fh] == 6

	# tuple that says straight flush is valued 8, with 10 being the highest rank
	assert hand_rank(sf) == (8, 10) 
	assert hand_rank(fk) == (7, 9, 7)
	assert hand_rank(fh) == (6, 10, 7)

	assert card_ranks(sf) == 
	assert card_ranks(fk) 
	assert card_ranks(fh) 

	return "test OK!"

print test()

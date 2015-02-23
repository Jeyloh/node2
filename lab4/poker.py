#   A script that simulates a poker game. Input how many players and how many cards in each hand, 
#   then return the best rank and declare a winner.
#
#
#   Author:     Jorgen Lybeck Hansen
#   Group:      Node 
#   Version:    02.23.2015
#   Notes:
#               I followed the UDACITY: Design of Computer Programs course while trying to write
#               my own functions. 
#
#   Bugs: 
#		         None
#
import random 


def deal(numhands, n=5):
    """Creates 52 cards. Then deals  out n cards to numhands of players.
        Will raise an error if numhands*n >= 52. random.sample(52, 5*numhands) 
        shuffles and deals out the amount of needed cards for the table.
        @param numhands how many players
        @param n how manycards per player."""
    deck = [card+suit for card in '23456789TJQKA' for suit in 'HDCS']
    if numhands*n > len(deck):
        raise Exception('Not enough cards.')
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]
            # [deck[i:i+n] 


def poker(hands):
    """Take all hands in play and return the best rank. Takes use of 
        allmax() to filter out ties. With this implemented, ties will share
        the pot equally.
        @param hands how many players around the table."""
    return allmax(hands, key=hand_rank)

def hand_rank(hand):
    """ Return the best hand in play, ranking them with
        tuples. Sort every hand from 1-8, then the next 
        value is based on ranks, suits etc."""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def allmax(iterable, key=None):
    """List comprehension:
        In poker(hands) we call this function with params 
        (hands, key=hand_rank). Iterates through hands and return 
        a list of all items = max of the iterable"""
    return [i for i in iterable if key(i) == max([key(j) for j in iterable])]


def straight(ranks):
    """ If ranks is equal to 5 straight cards, return True.
        @param ranks is the value of the card. ex. [2C, 3D, 4C, 5S, 6C]"""
    return ranks == range(ranks[0],ranks[0]-5, -1)


def flush(hand):
    """ If hand is equal to 5 of the same suit, return True.
    @param hand is the suit for each hand."""
    return [s for r,s in hand].count(hand[0][1]) == 5

def kind(n, ranks):
    #Return the first rank that this hand has exactly n of.
    #Return None if there is no n-of-a-kind in the hand.
    """ Checks for cards with more than one of the same rank.
        ex. [8C, 8D, 8H, 2D, 5H] <- Three of a kind
        @param n how many of ranks we have in our hand.
        @param ranks is the card we have more than 1 of
        @return none if no cards are duplicated."""
    for r in ranks:
        if ranks.count(r) == n: return r 
    return None


def two_pair(ranks):
    """ Check if there are two pairs. Return the highest pair 
        first and the lowest pair second, both as tuples.
        ex. [4C, 4H, 9S, 9H, QD] <- Two pairs
        @param ranks is the value of the card.
        @return none if not two pairs in hand."""
    if ranks.count(ranks[1]) + ranks.count(ranks[3]) == 4:
        return (ranks[1], ranks[3])


def card_ranks(cards):
    """ Creates a list to set integer values to the cards 
    	which represents T(en), J(ack), Q(ueen), K(ing) A(ce).
    	We then create an empty list called ranks.
    	We then loop through our current hand and store 
    	the cards with sorted values in the ranks list.
    	Also, if we get a flush from A - 5, we need to make the
    	A = 1. This is what we do in the last line"""
    assignValue = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }
    ranks = []
    for r, s in cards:
        if assignValue.has_key(r):
            ranks.append(assignValue[r])
        else:
            ranks.append(int(r))
    #ranks = [assignValue[r] if r in assignValue else int(r) for r,s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def test():
	"""Test different functions, to check if they
		return the right value"""
	sf = "6C 7C 8C 9C TC".split() # Straight Flush
	fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
	fh = "TD TC TH 7C 7D".split() # Full House
	tp = "5S 5D 9H 9C 6S".split() # Two pairs
	fkranks = card_ranks(fk)
	tpranks = card_ranks(tp)
	assert kind(4, fkranks) == 9
	assert kind(3, fkranks) == None
	assert kind(2, fkranks) == None
	assert kind(1, fkranks) == 7
	assert two_pair(tpranks) == (9, 5)
	assert two_pair(fkranks) == None
	return 'tests pass'


if __name__ == '__main__':
    """ Checks how much time the application runs in"""
    import timeit
    time = (timeit.timeit("straight([9, 8, 7, 6, 5])", setup = "from __main__ import straight"))
    print ("Script runs in: %s ms") % (time)
   
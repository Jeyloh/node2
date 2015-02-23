import random

mydeck = [r+s for s in 'DCHS' for r in '23456789TJQKA']

hand_names = {0:'high card',1:'pair',2:'two pair',3:'3 of a kind',4:'straight',5:'flush',6:'full house',7:'4 of a kind',8:'straight flush'}

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
    return ranks

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for i in ranks:
        if ranks.count(i) == n:
            return i

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def flush(hand):
    """Return True if all the cards have the same suit."""
    suits = [s for r,s in hand]
    for i in range(len(suits)-1):
        if suits[i] != suits[i+1]:
            return False
    return True

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    if kind(2, ranks) and kind(2,ranks[2:]):
        return kind(2, ranks), kind(2,ranks[2:])
    return None

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2,ranks))
    elif flush(hand):                              # flush
        return (5, [ranks])
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), [ranks])
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), [ranks])
    elif kind(2, ranks):                           # pair
        return (1, kind(2, ranks), [ranks])
    else:                                          # high card
        return (0, [ranks])

def deal(numhands, n=5, deck=mydeck):
    fresh_deck = []+deck
    random.shuffle(fresh_deck)
    hands = []
    for hand in range(numhands):
        hand = []
        for card in range(n):
            if len(fresh_deck):
                hand.append(fresh_deck.pop())
        hands.append(hand)
    return hands

def hand_percentages(n=700*1000):
    """Sample n random poker hands and print a table of percentages for each type of hand."""
    counts =[0] * 9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print "%14s: %6.3f %%" % (hand_names[i], 100.*counts[i]/n)

hand_percentages()
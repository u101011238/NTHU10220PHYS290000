import random as rand

class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Heart', 'Spades']
    rank_names = ['None','Ace', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])                    
                  
    def __init__(self, suit = 0, rank = 0):
        self.suit = suit
        self.rank = rank
        
    def __cmp__(self, other):
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    def sort(self):
        sort = []
        for i in range(len(self.cards)):
            m = min(self.cards)
            sort.append(m)
            self.cards.remove(m)
        self.cards = sort
        
    def deal_hands(self, num_hands, num_cards):
        if num_hands*num_cards > 52:
            return 'Not enough cards.'
        l = []
        for i in range(1, num_hands + 1):
            hand_i = Hand('Hand %d' % i)
            self.move_cards(hand_i, num_cards)
            l.append(hand_i)
        return l

class Hand(Deck):
    def __init__(self, label = ''):
        self.cards = []
        self.label = label

d = Deck()
print d
print '\n'

d.shuffle()
print d
print '\n'

d.sort()
print d
print '\n'

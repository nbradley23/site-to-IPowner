from random import shuffle


class Card:

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return '{} of {}'.format(self.value,self.suit )


class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7',
                             '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value,suit) for suit in suits for value in values]

    def __repr__(self):
        return 'Deck of {} cards'.format(self.count())
    
    def count(self):
        return len(self.cards)

    def _deal(self, num_to_deal=1):
        count = self.count()
        dealed_cards = []

        if count == 0:
            raise ValueError('All cards have been dealt')
        elif num_to_deal > self.count():
            num_to_deal = self.count()

        for x in range(num_to_deal):
            dealed_cards.append(self.cards.pop())
        return dealed_cards

    def shuffle(self):
        if self.count() != 52:
            raise ValueError('Only full decks can be shuffled')
        else:
            shuffle(self.cards)

    def deal_card (self):
        return self._deal()[0]
    
    def deal_hand (self,num_cards = 5):
        return self._deal(num_cards)

    
my_deck = Deck()
print(my_deck.deal_hand(52))
print(my_deck.deal_hand(10))

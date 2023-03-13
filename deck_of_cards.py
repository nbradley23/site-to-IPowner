from random import choice


class Card:

    def __init__(self):
        self.suit = choice(['Hearts', 'Diamonds', 'Clubs', 'Spades'])
        self.value = choice(['A', '2', '3', '4', '5', '6', '7',
                             '8', '9', '10', 'J', 'Q', 'K'])

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:
    def __init__(self):
        self.cards = ['A of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'J of Hearts', 'Q of Hearts', 'K of Hearts', 'A of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'J of Diamonds',
                      'Q of Diamonds', 'K of Diamonds', 'A of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'J of Clubs', 'Q of Clubs', 'K of Clubs', 'A of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades']

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def _deal(self, num_to_deal):
        self.num_to_deal = num_to_deal

        if self.count == 0:
            return 'All cards have been dealt'
        elif num_to_deal > self.count():
            num_to_deal = self.count()

        dealed_cards = self.cards[-num_to_deal:]
        self.cards[-num_to_deal:]
        return dealed_cards

    def shuffle():


my_card = Card()
my_deck = Deck()
print(my_deck._deal())

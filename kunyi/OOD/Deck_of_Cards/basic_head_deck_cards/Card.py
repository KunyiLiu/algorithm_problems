import enum

FACE_SYMBOLS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Suit(enum.Enum):
    Club = 0
    Diamond = 1
    Heart = 2
    Spade = 3


class Card:
    def __init__(self, value, suit):
        self.face_value = value
        self.suit = suit
        self.is_available = True

    def __str__(self):
        face = FACE_SYMBOLS[self.face_value - 1]
        suit = self.suit
        if suit == Suit.Club:
            suit = 'c'
        elif suit == Suit.Diamond:
            suit = 'd'
        elif suit == Suit.Heart:
            suit = 'h'
        elif suit == Suit.Spade:
            suit = 's'
        else:
            suit = 'NOT_RECOGNIZED'
        return 'Card with Face {} and Suit {}'.format(face, suit)

    def mark_not_available(self):
        self.is_available = False






import random

from Card import Card, Suit


class Deck:
    def __init__(self, num, cls):
        self.numofDeck = num
        self.dealtIndex = 0
        self.card_type = cls
        self.total_deck = self.new_deck()

    def new_deck(self):
        STD_DECK = [self.card_type(j, Suit(i)) for i in range(4) for j in range(13)]
        total_deck = STD_DECK * self.numofDeck
        random.shuffle(total_deck)
        # NOTICE when you return a list
        return total_deck[:]

    def remaining_card_size(self):
        return len(self.total_deck) - self.dealtIndex

    def deal_hand(self, num):
        if self.remaining_card_size() < num:
            print 'Use all the decks'
            return

        hand = []
        for i in range(num):
            card = self.deal_card()
            if card is not None:
                hand.append(card)

        return hand

    def deal_card(self):
        if self.remaining_card_size() == 0:
            return

        card = self.total_deck[self.dealtIndex]
        card.mark_not_available()
        self.dealtIndex += 1

        return card




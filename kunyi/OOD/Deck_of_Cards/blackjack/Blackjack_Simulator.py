from basic_head_deck_cards.Deck import Deck

from Blackjack_Card import BlackJackCard
from Blackjack_Hand import BlackJackHand

HIT_UNTIL = 16


class BlackJackSimulator:
    def __init__(self, number_players, number_of_deck):
        self.number_players = number_players
        self.hands = [BlackJackHand() for i in range(number_players)]
        self.deck = Deck(number_of_deck, BlackJackCard)

    def deal_initial(self):
        for hand in self.hands:
            card1 = self.desk.deal_card()
            card2 = self.deck.deal_card()
            if card1 is None or card2 is None:
                return False
            hand.add_card(card1)
            hand.add_card(card2)
        return True

    def get_black_jack(self):
        winners = []
        for i in range(len(self.hands)):
            hand = self.hands[i]
            if hand.is_black_jack():
                winners.append(i)

        return winners

    def play_hand(self, hand):
        # continue add card unitil the hit
        while hand.get_score() < HIT_UNTIL:
            card = self.deck.deal_card()
            if card is None:
                return False
            hand.add_card(card)

        return True

    def play_all_heads(self):
        for hand in self.hands:
            if not self.play_hand(hand):
                return False

        return True

    def get_winners(self):
        winners = []
        win_score = 0
        for i in range(len(self.hands)):
            hand = self.hands[i]
            if not hand.is_busted():
                win_score = hand.get_score()
                winners = list()
                winners.append(i)
            elif hand.get_score() == win_score:
                winners.append(i)

        return winners

    def __str__(self):
        returned_literal = []
        for i in range(self.hands):
            hand = self.hands[i]
            returned_literal.append('Hand {} with score {}'.format(i, hand.get_score()))

        return ';\n'.join(returned_literal)






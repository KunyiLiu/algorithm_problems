import sys

from Blackjack_Card import BlackJackCard
from basic_head_deck_cards.Hand import Hand


class BlackJackHand(Hand):
    # def __init__(self):
    #     super(BlackJackHand, self).__init__()
    #     self.score_list = []
    def get_score(self):
        score_list = self.get_possible_scores()
        max_under = - sys.maxint - 1
        min_over = sys.maxint
        for score in score_list:
            if 21 < score < min_over:
                min_over = score
            elif max_under < score <= 21:
                max_under = score
        # get max under?
        return min_over if max_under == - sys.maxint - 1 else max_under

    def get_possible_scores(self):
        score_list = []
        if len(self.hand_of_cards) == 0:
            return score_list
        for card in self.hand_of_cards:
            self.add_card_to_list(card, score_list)
        return score_list

    @staticmethod
    def add_card_to_list(card, score_list):
        """

        :param card: BlackJackCard
        :param score_list:
        :return:
        """
        if len(score_list) == 0:
            score_list.append(0)
        for i in range(len(score_list)):
            score = score_list[i]
            score_list[i] = score + card.get_min_value()
            if card.get_min_value() != card.get_max_value():
                score_list.append(score + card.get_max_value())
        return score_list

    def is_busted(self):
        score = self.get_score()
        return score > 21

    def is_21(self):
        return self.get_score() == 21

    def is_blackjack(self):
        if len(self.hand_of_cards) != 2:
            return False
        first_card, second_card = self.hand_of_cards[0], self.hand_of_cards[1]
        return (first_card.is_ace() and second_card.is_face_card()) \
            or (second_card.is_ace() and first_card.is_face_card())


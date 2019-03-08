from Card import Card, Suit


class Hand:
    def __init__(self):
        self.hand_of_cards = []

    def add_card(self, card):
        """
        :param card: Card
        :return: None
        """
        self.hand_of_cards.append(card)

    def get_score(self):
        return sum(self.hand_of_cards)

    def __str__(self):
        return 'Hand of cards: {}'.format(','.join(self.hand_of_cards))

from basic_head_deck_cards.Card import Card


class BlackJackCard(Card):
    def get_value(self):
        if self.is_ace():
            return 1
        elif self.is_face_card():
            return 10
        else:
            return self.face_value

    def get_min_value(self):
        if self.is_ace():
            return 1
        else:
            return self.face_value

    def get_max_value(self):
        if self.is_ace():
            return 11
        else:
            return self.face_value

    def is_ace(self):
        return self.face_value == 1

    def is_face_card(self):
        return 11 <= self.face_value <= 13
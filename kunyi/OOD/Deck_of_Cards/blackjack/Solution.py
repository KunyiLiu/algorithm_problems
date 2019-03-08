from Blackjack_Simulator import BlackJackSimulator


class Solution:
    def __init__(self, number_of_hands, number_of_decks):
        self.automator = BlackJackSimulator(number_of_hands, number_of_decks)

    def automate(self):
        success = self.automator.deal_initial()
        if not success:
            print 'Error. Out of cards'
        else:
            print '-----------Initial--------'
            print self.automator
            black_jack_winners = self.automator.get_black_jack()
            if len(black_jack_winners) > 0:
                print 'BlackJack at {}'.format(', '.join(black_jack_winners))
            else:
                success = self.automator.play_all_heads()
                if not success:
                    print 'Error. Out of cards'
                else:
                    print '--------Complete Game ---------'
                    print self.automator
                    winners = self.automator.get_winners()
                    if len(winners) > 0:
                        print 'Winners: {}'.format(', '.join(winners))
                    else:
                        print 'All players busted!'

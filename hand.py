
import card 
import deck
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        #card passed in
        #from Deck.deal() --> single Card(suit, rank)
        self.cards.append(card)
        self.value += card.values[card.rank]

        #track aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        #If total value > 21 and I still have an ace
        #then change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

test_deck = deck.Deck()
test_deck.shuffle()

#Player
test_player = Hand()
# Deal 1 card from the deck CARD(suit, rank)
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)

from card import Card
import random
class Deck:
    def __init__(self):
        self.deck = []

        for suit in Card.suits:
            for rank in Card.ranks:
                #Create a card object
                created_card = Card(rank, suit)
                self.deck.append(created_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()
    

# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)
class Chips:
    

    def __init__(self, total=100):
        self.total = total # this can be set a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    
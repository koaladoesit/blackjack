from shoe import shoe
'''create a Player class so we can play around with wins, losses and bets,
also store hands and make decisions'''
class Player:
    wins = []
    loss = []
    name = ""


#get the player's name (number will iterate
#to fill in as many of the three places as requested by user)
    def __init__(self, number):
        if number != 4:
            self.name = input("Player {}, please enter your name: ".format(number)) # in game_play we use a list iteration, so it starts at zero
            self.bet = []
        self.hand = []

# first hand is of two cards for each player (including the dealer) -
# needs help with the mutable element as argument  gotcha
        def deal_first_hand():
            self.hand.append(shoe.pop())
            self.hand.append(shoe.pop())
        deal_first_hand()

#to be used when player asks to hit:
    def deal(self):
        self.hand.append(shoe.pop())
#let's see if we can factor in some gambling!
#How do I make sure that the bet is an int?
    def place_bet(self):
        self.bet = input("{}, please place your bet! Enter the number of chips: ".format(self.name))
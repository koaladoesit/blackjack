from shoe import shoe
#create a Player class so we can play around with wins, losses and bets,
#also store hands

class Player:

    name = ""
    busted = False
    tie = False
    lost = False
    win = False
    stay = False
    wins = 0
    losses = 0
    has_blank = False


#get the player's name (number will iterate
#to fill in as many of the three places as requested by user)
    def __init__(self, number):
        if number != 4 and self.name == "":
            self.name = input("Player {}, please enter your name: ".format(number)) # in game_play we use a list iteration, so it starts at zero
            self.bet = []
        elif number == 4:
            self.name = "Dealer"
        self.hand = []

# first hand is of two cards for each player (including the dealer) -
# needs help with the mutable element as argument  gotcha
        def deal_first_hand():
            if shoe[-1][0] == "BLANK" or shoe[-2][0]=="BLANK":
                self.has_blank = True
                shoe.pop() #remove blank card so it doesn't get played
            self.hand.append(shoe.pop())
            self.hand.append(shoe.pop())
        deal_first_hand()
#player needs to see the cards
#to be used when player asks to hit:
    def deal(self):
        if shoe[-1][0] == "BLANK":
            self.has_blank = True
            shoe.pop()# remove blank card so it doesn't get played
        self.hand.append(shoe.pop())

#let's see if we can factor in some gambling!
#How do I make sure that the bet is an int?
    def place_bet(self):
        min_bet = 2
        max_bet = 10
        print('Minimum bet is 2, maximum is 10')
        self.bet = input("{}, please place your bet! Enter the number of chips: ".format(self.name))
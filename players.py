from shoe import shoe
'''
- There is a maximum of 3 players in a game, and one dealer
- Each player is dealt a two - cards hand at the beginning of the game, face-up.
- The dealer gets 2 cards as well, but one of them is face-down(hidden)
'''

class Player:

    name = ""
    busted = False # A player is busted if they go over 21.
                    #Need to record this so we know when all players are done with the current game
    tie = False # player ties if they have the same score as the dealer
                # (except for a blackjack on either side), or a blackjack when dealer has one
    lost = False
    win = False
    stay = False #Need to record this so we know when all players are done with the current game
    wins = 0 #For future development
    losses = 0 # idem
    has_blank = False


#get the player's name (number will iterate
#to fill in as many of the three places as requested by user)
    def __init__(self, number):
        if number != 4 and self.name == "":
            self.name = input("Player {}, please enter your name: ".format(number))
            self.bet = []
        elif number == 4:
            self.name = "Dealer"
        self.hand = []

# first hand is of two cards for each player (including the dealer) -
# included in init to solve the mutable element as argument gotcha (yes, I've hit it)
        def deal_first_hand():
            if shoe[-1][0] == "BLANK":
                self.has_blank = True
                shoe.pop() #remove blank card so it doesn't get played
            if shoe[-2][0]=="BLANK":
                self.has_blank = True
                shoe.pop(-2) #remove blank card so it doesn't get played
            self.hand.append(shoe.pop())
            self.hand.append(shoe.pop())
        deal_first_hand()
#to be used when player asks to hit:
    def deal(self):
        if shoe[-1][0] == "BLANK":
            self.has_blank = True
            shoe.pop()# remove blank card so it doesn't get played
        self.hand.append(shoe.pop())
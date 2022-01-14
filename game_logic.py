from shoe import shuffled_shoe

'''create a Player class so we can play around with wins, losses and bets,
also store hands and make decisions'''
class Player:
    bet = 0
    wins = 0
    loss = 0
    name = ""


#get the player's name (number will iterate
#to fill in as many of the three places as requested by user)
    def get_name(self, number):
        self.name = input("Player {}, please enter your name: ".format(number))

# first hand is of two cards for each player (including the dealer) -
# needs help with the mutable element as argument  gotcha

    def deal_first_hand(self):
        self.hand.append(shoe.pop())
        self.hand.append(shoe.pop())
#to be used when player asks to hit:
    def deal(self):
        self.hand.append(shoe.pop())
#let's see if we can factor in some gambling! How do I make sure that the bet is an int?
    def place_bet(self):
        self.bet = input("{}, please place your bet! Enter the number of chips: ".format(self.name))

# calculate the score of the current hand:
def score(hand):
    score = 0
    has_ace = False
    has_face = False
    blackjack =  False
    for card in hand:
        if type(card[0])== int:
            score+=card[0]
        elif card in ['JACK', 'QUEEN', 'KING']:
            score+=10
            has_face = True
        else: has_ace = True
    if has_ace and has_face:
        has_blackjack = True
    if has_ace and not has_face:
        if score <= 10:
            score += 11
        else:
            score+=1
    return (score, blackjack)

def check_if_busted(score):
    busted = False
    if score > 21:
        busted = True
    return busted



shoe = shuffled_shoe()
print (len(shoe))
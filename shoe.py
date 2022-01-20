import random


# There are 52 cards in a deck, ranks containing 10 numbers and 4 faces,
# each of them available in 4 different suits:
ranks = [r for r in range(2, 15)]

faces = ['ACE', 'JACK', 'QUEEN', 'KING']

values = {}

for r in ranks:
    if r<=10:
        values.update({r: r})
    else:
        values.update({r: faces[r-11]})

suits = ['♠', '♥', '♦', '♣']

def get_deck():
#Return a new deck of cards.
    deck =[]
    for rank in ranks:
        for suit in suits:
            deck.append([values[rank], suit])
    return deck

'''
- A shoe is a shuffled pack of 6 decks
- A blank card is a red plastic card inserted in a shoe at a random position so that when the blank
is drawn, the current game becomes the last

Note for testing: the game is played from the end of the shoe, not the beginning
(a higher position of the blank means fewer games)
'''
#create shoe:
def get_shoe(deck=get_deck()):
    shoe =[]
    for i in range(6):
        shoe += deck
    random.shuffle(shoe)
    red_card_position = random.randint(0, len(shoe))
    print(red_card_position) # this is to save the tester from blindly going into loooong games
    shoe.insert(red_card_position, ['BLANK', 0])
    return shoe

'''
- Cards marked 2-10 will score the value they show, for example a 2 will score a 2.
- Cards that have “faces” or “ranks” (Jack, Queen, King)  will score a 10
- Ace will score 1 or 11, depending on the current hand:
- If the current hand score <= 10, player decides Ace value (1 or 11).
- If the current score >10, Ace = 1
'''

# calculate the score of the current hand

def check_ace(hand):
    ace = False
    for card in hand:
        if card[0] == "ACE":
            ace = True
    return ace

def check_face(hand):
    face = False
    for card in hand:
        if card[0] in ['JACK', 'QUEEN', 'KING']:
            face = True
    return face

def check_blackjack(hand):
    blackjack =  False
    if len(hand) == 2:
        if check_face(hand) and check_ace(hand):
            blackjack = True
    return blackjack

def get_score(hand):
    score = 0

    for card in hand:
        if type(card[0])== int:
            score+=card[0]
        elif card[0] in ['JACK', 'QUEEN', 'KING']:
            score+=10
    if check_ace(hand) and not check_face(hand):
        if score <= 10:
            score += 11
        else:
            score+=1
    return score

def check_if_busted(score):
    busted = False
    if score > 21:
        busted = True
    return busted

shoe = get_shoe()